"""
MIT License

Copyright (c) 2025 RenzMc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations
from typing import Any, Optional
from typing import List as PyList
from typing import Dict as PyDict
from renzmc.core.ast import (
    AST, Assign, BinOp, Boolean, Break, Continue, Dict, For, FuncCall, If, List, NoOp, Num, Return, String, UnaryOp, Var, VarDecl, While
)
from renzmc.core.token import TokenType


class CodeGenerator:

    def __init__(self):
        self.indent_level = 0
        self.indent_str = "    "

    def generate(self, node: AST, context: Dict[str, Any] = None) -> str:
        if context is None:
            context = {}

        method_name = f'generate_{type(node).__name__}'
        generator = getattr(self, method_name, self.generic_generate)
        return generator(node, context)

    def generate_function(self, name: str, params: List[str],
                         body: List[AST], context: Dict[str, Any] = None) -> str:
        if context is None:
            context = {}

        lines = []

        params_str = ", ".join(params)
        lines.append(f"def {name}({params_str}):")

        self.indent_level += 1

        if not body:
            lines.append(self._indent("pass"))
        else:
            for stmt in body:
                stmt_code = self.generate(stmt, context)
                if stmt_code:
                    lines.append(self._indent(stmt_code))

        self.indent_level -= 1

        return "\n".join(lines)

    def generate_Num(self, node: Num, context: Dict[str, Any]) -> str:
        return str(node.value)

    def generate_String(self, node: String, context: Dict[str, Any]) -> str:
        value = node.value.replace('"', r'\&quot;')
        return f'"{value}"'

    def generate_Boolean(self, node: Boolean, context: Dict[str, Any]) -> str:
        return "True" if node.value else "False"

    def generate_Var(self, node: Var, context: Dict[str, Any]) -> str:
        return node.name

    def generate_BinOp(self, node: BinOp, context: Dict[str, Any]) -> str:
        left = self.generate(node.left, context)
        right = self.generate(node.right, context)

        op_map = {
            TokenType.TAMBAH: '+',
            TokenType.KURANG: '-',
            TokenType.KALI: '*',
            TokenType.BAGI: '/',
            TokenType.PEMBAGIAN_BULAT: '//',
            TokenType.SISA_BAGI: '%',
            TokenType.PANGKAT: '**',
            TokenType.SAMA_DENGAN: '==',
            TokenType.TIDAK_SAMA: '!=',
            TokenType.KURANG_DARI: '<',
            TokenType.LEBIH_DARI: '>',
            TokenType.KURANG_SAMA: '<=',
            TokenType.LEBIH_SAMA: '>=',
            TokenType.DAN: 'and',
            TokenType.ATAU: 'or',
            TokenType.BITWISE_AND: '&',
            TokenType.BITWISE_OR: '|',
            TokenType.BITWISE_XOR: '^',
            TokenType.GESER_KIRI: '<<',
            TokenType.GESER_KANAN: '>>',
        }

        op = op_map.get(node.op.type, str(node.op.value))
        return f"({left} {op} {right})"

    def generate_UnaryOp(self, node: UnaryOp, context: Dict[str, Any]) -> str:
        expr = self.generate(node.expr, context)

        op_map = {
            TokenType.TAMBAH: '+',
            TokenType.KURANG: '-',
            TokenType.TIDAK: 'not ',
            TokenType.BITWISE_NOT: '~',
        }

        op = op_map.get(node.op.type, str(node.op.value))
        return f"({op}{expr})"

    def generate_VarDecl(self, node: VarDecl, context: Dict[str, Any]) -> str:
        value = self.generate(node.value, context)
        context[node.var_name] = node.value
        return f"{node.var_name} = {value}"

    def generate_Assign(self, node: Assign, context: Dict[str, Any]) -> str:
        var_name = node.var.name if isinstance(node.var, Var) else str(node.var)
        value = self.generate(node.value, context)
        context[var_name] = node.value
        return f"{var_name} = {value}"

    def generate_Return(self, node: Return, context: Dict[str, Any]) -> str:
        if hasattr(node, 'expr') and node.expr:
            value = self.generate(node.expr, context)
            return f"return {value}"
        return "return"

    def generate_If(self, node: If, context: Dict[str, Any]) -> str:
        lines = []

        condition = self.generate(node.condition, context)
        lines.append(f"if {condition}:")

        self.indent_level += 1
        if not node.if_body:
            lines.append(self._indent("pass"))
        else:
            for stmt in node.if_body:
                stmt_code = self.generate(stmt, context.copy())
                if stmt_code:
                    lines.append(self._indent(stmt_code))
        self.indent_level -= 1

        if node.else_body:
            lines.append("else:")
            self.indent_level += 1
            for stmt in node.else_body:
                stmt_code = self.generate(stmt, context.copy())
                if stmt_code:
                    lines.append(self._indent(stmt_code))
            self.indent_level -= 1

        return "\n".join(lines)

    def generate_While(self, node: While, context: Dict[str, Any]) -> str:
        lines = []

        condition = self.generate(node.condition, context)
        lines.append(f"while {condition}:")

        self.indent_level += 1
        if not node.body:
            lines.append(self._indent("pass"))
        else:
            for stmt in node.body:
                stmt_code = self.generate(stmt, context.copy())
                if stmt_code:
                    lines.append(self._indent(stmt_code))
        self.indent_level -= 1

        return "\n".join(lines)

    def generate_For(self, node: For, context: Dict[str, Any]) -> str:
        lines = []

        start = self.generate(node.start, context)
        end = self.generate(node.end, context)
        lines.append(f"for {node.var_name} in range({start}, {end} + 1):")

        self.indent_level += 1
        loop_context = context.copy()
        loop_context[node.var_name] = int

        if not node.body:
            lines.append(self._indent("pass"))
        else:
            for stmt in node.body:
                stmt_code = self.generate(stmt, loop_context)
                if stmt_code:
                    lines.append(self._indent(stmt_code))
        self.indent_level -= 1

        return "\n".join(lines)

    def generate_Break(self, node: Break, context: Dict[str, Any]) -> str:
        return "break"

    def generate_Continue(self, node: Continue, context: Dict[str, Any]) -> str:
        return "continue"

    def generate_FuncCall(self, node: FuncCall, context: Dict[str, Any]) -> str:
        args = [self.generate(arg, context) for arg in node.args]
        args_str = ", ".join(args)

        func_name = node.name

        return f"{func_name}({args_str})"

    def generate_List(self, node: List, context: Dict[str, Any]) -> str:
        elements = [self.generate(elem, context) for elem in node.elements]
        return f"[{', '.join(elements)}]"

    def generate_NoOp(self, node: NoOp, context: Dict[str, Any]) -> str:
        return ""

    def generic_generate(self, node: AST, context: Dict[str, Any]) -> str:
        return ""

    def _indent(self, code: str) -> str:
        if not code:
            return ""
        indent = self.indent_str * self.indent_level
        lines = code.split('\n')
        return '\n'.join(indent + line if line.strip() else line for line in lines)
