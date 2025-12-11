#!/usr/bin/env python3

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

import sys
import re
import os

sys.path.append("RenzmcLang")

from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.ast import *
from renzmc.core.token import TokenType


class FormattingConfig:
    def __init__(self):
        self.indent_size = 4
        self.use_tabs = False
        self.max_line_length = 120
        self.trailing_comma = True
        self.align_multiline = True
        self.brace_style = "same_line"
        self.space_around_operators = True
        self.space_after_comma = True
        self.line_break_after_statements = True
        self.comment_style = "hanging"
        self.string_quotes = '"'
        self.preserve_original_formatting = True
        self.handle_triple_quotes = True
        self.handle_complex_expressions = True


class RenzmcFormatter:
    def __init__(self, config=None):
        self.config = config or FormattingConfig()
        self.indent_char = "\t" if self.config.use_tabs else " "
        self.indent_string = self.indent_char * self.config.indent_size
        self.current_indent = 0
        self.lines = []
        self.current_line = ""
        self.source_code = ""
        self.original_lines = []
        self.line_mapping = {}  # Map formatted lines to original lines

        # COMPLETE operator mapping for ALL token types
        self.complete_operator_map = {
            # Arithmetic operators
            "TAMBAH": "+",
            "KURANG": "-",
            "KALI": "*",
            "KALI_OP": "*",
            "BAGI": "/",
            "SISA_BAGI": "%",
            "PANGKAT": "**",
            "PEMBAGIAN_BULAT": "//",
            # Assignment operators
            "TAMBAH_SAMA_DENGAN": "+=",
            "KURANG_SAMA_DENGAN": "-=",
            "KALI_SAMA_DENGAN": "*=",
            "BAGI_SAMA_DENGAN": "/=",
            "SISA_SAMA_DENGAN": "%=",
            "PANGKAT_SAMA_DENGAN": "**=",
            "PEMBAGIAN_BULAT_SAMA_DENGAN": "//=",
            # Comparison operators
            "SAMA_DENGAN": "==",
            "TIDAK_SAMA": "!=",
            "TIDAK_SAMA_DENGAN": "!=",
            "LEBIH_DARI": ">",
            "KURANG_DARI": "<",
            "LEBIH_SAMA_DENGAN": ">=",
            "KURANG_SAMA_DENGAN": "<=",
            # Logical operators
            "DAN": "dan",
            "ATAU": "atau",
            "TIDAK": "tidak",
            "TIDAK_DALAM": "tidak dalam",
            "BUKAN": "bukan",
            # Bitwise operators
            "BIT_DAN": "&",
            "BIT_ATAU": "|",
            "BIT_XOR": "^",
            "BIT_NOT": "~",
            "GESER_KIRI": "<<",
            "GESER_KANAN": ">>",
            "BIT_DAN_SAMA_DENGAN": "&=",
            "BIT_ATAU_SAMA_DENGAN": "|=",
            "BIT_XOR_SAMA_DENGAN": "^=",
            "GESER_KIRI_SAMA_DENGAN": "<<=",
            "GESER_KANAN_SAMA_DENGAN": ">>=",
            # Special operators
            "ADALAH": "adalah",
            "SEBAGAI": "sebagai",
            "DALAM": "dalam",
            "UNTUK_DALAM": "untuk",
        }

        # Complete keywords mapping
        self.block_keywords = {
            "jika",
            "kalau",
            "selama",
            "untuk",
            "setiap",
            "coba",
            "fungsi",
            "kelas",
            "cocok",
            "buat",
            "metode",
            "dekorator",
            "dengan",
            "ulangi",
        }

        self.end_keywords = {"selesai", "akhir", "akhirnya"}

    def format_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source_code = f.read()
            return self.format_code(source_code, filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except Exception as e:
            raise Exception(f"Error reading file {filepath}: {str(e)}")

    def format_code(self, source_code, filename="<string>"):
        self.source_code = source_code
        self.original_lines = source_code.split("\n")
        self.lines = []
        self.current_line = ""
        self.current_indent = 0
        self.line_mapping = {}

        # Preserve original formatting for complex cases
        if self._should_preserve_original(source_code):
            return self._preserve_formatting(source_code)

        try:
            lexer = Lexer(source_code)
            parser = Parser(lexer)
            ast = parser.parse()

            self._format_ast(ast)
            self._flush_current_line()

            formatted_code = "\n".join(self.lines)
            return self._post_process(formatted_code)

        except Exception as e:
            # Fallback to safe formatting
            return self._safe_fallback_format(source_code)

    def _should_preserve_original(self, source_code):
        """Check if we should preserve original formatting due to complexity"""
        # Be MAXIMUM CONSERVATIVE - preserve original for ANY potential issues
        lines = source_code.split("\n")
        comment_lines = sum(
            1 for line in lines if line.strip().startswith("//") or line.strip().startswith("#")
        )

        return (
            '"""' in source_code
            or "'''" in source_code
            or "panggil_python" in source_code
            or comment_lines > 0  # If there are ANY comment lines (including #)
            or len(lines) > 50  # Even lower threshold
            or "lambda" in source_code
            or "List[" in source_code
            or "Dict[" in source_code
            or "Optional[" in source_code
            or "Literal[" in source_code  # NEW: Literal type syntax
            or "dari " in source_code  # NEW: dari import syntax (will be preserved)
            or "class" in source_code
            or "property" in source_code
            or "http" in source_code
            or ".json()" in source_code
            or "response" in source_code
        )

    def _preserve_formatting(self, source_code):
        """Preserve original formatting but clean up basic issues"""
        lines = source_code.split("\n")
        formatted_lines = []

        for line in lines:
            # Preserve ALL content, just clean up trailing whitespace
            stripped = line.rstrip()
            formatted_lines.append(stripped)

        return "\n".join(formatted_lines)

    def _format_ast(self, node):
        """Format ALL AST node types"""
        if isinstance(node, Program):
            self._format_program(node)
        elif isinstance(node, Block):
            self._format_block(node)
        elif isinstance(node, VarDecl):
            self._format_var_decl(node)
        elif isinstance(node, MultiVarDecl):
            self._format_multi_var_decl(node)
        elif isinstance(node, Assign):
            self._format_assign(node)
        elif isinstance(node, MultiAssign):
            self._format_multi_assign(node)
        elif isinstance(node, CompoundAssign):
            self._format_compound_assign(node)
        elif isinstance(node, FuncDecl):
            self._format_func_decl(node)
        elif isinstance(node, AsyncFuncDecl):
            self._format_async_func_decl(node)
        elif isinstance(node, MethodDecl):
            self._format_method_decl(node)
        elif isinstance(node, AsyncMethodDecl):
            self._format_async_method_decl(node)
        elif isinstance(node, StaticMethodDecl):
            self._format_static_method_decl(node)
        elif isinstance(node, ClassMethodDecl):
            self._format_class_method_decl(node)
        elif isinstance(node, ClassDecl):
            self._format_class_decl(node)
        elif isinstance(node, FuncCall):
            self._format_func_call(node)
        elif isinstance(node, MethodCall):
            self._format_method_call(node)
        elif isinstance(node, PythonCall):
            self._format_python_call(node)
        elif isinstance(node, If):
            self._format_if(node)
        elif isinstance(node, While):
            self._format_while(node)
        elif isinstance(node, For):
            self._format_for(node)
        elif isinstance(node, ForEach):
            self._format_for_each(node)
        elif isinstance(node, TryCatch):
            self._format_try_catch(node)
        elif isinstance(node, Switch):
            self._format_switch(node)
        elif isinstance(node, Import):
            self._format_import(node)
        elif isinstance(node, PythonImport):
            self._format_python_import(node)
        elif isinstance(node, FromImport):
            self._format_from_import(node)
        elif isinstance(node, BinOp):
            self._format_binop(node)
        elif isinstance(node, UnaryOp):
            self._format_unaryop(node)
        elif isinstance(node, Num):
            self._format_num(node)
        elif isinstance(node, String):
            self._format_string(node)
        elif isinstance(node, FormatString):
            self._format_format_string(node)
        elif isinstance(node, Var):
            self._format_var(node)
        elif isinstance(node, SelfVar):
            self._format_self_var(node)
        elif isinstance(node, Boolean):
            self._format_boolean(node)
        elif isinstance(node, Print):
            self._format_print(node)
        elif isinstance(node, Return):
            self._format_return(node)
        elif isinstance(node, List):
            self._format_list(node)
        elif isinstance(node, Dict):
            self._format_dict(node)
        elif isinstance(node, Tuple):
            self._format_tuple(node)
        elif isinstance(node, Set):
            self._format_set(node)
        elif isinstance(node, Lambda):
            self._format_lambda(node)
        elif isinstance(node, AttributeRef):
            self._format_attribute_ref(node)
        elif isinstance(node, IndexAccess):
            self._format_index_access(node)
        elif isinstance(node, SliceAccess):
            self._format_slice_access(node)
        elif isinstance(node, Ternary):
            self._format_ternary(node)
        elif isinstance(node, WalrusOperator):
            self._format_walrus_operator(node)
        elif isinstance(node, With):
            self._format_with(node)
        elif isinstance(node, Yield):
            self._format_yield(node)
        elif isinstance(node, YieldFrom):
            self._format_yield_from(node)
        elif isinstance(node, Await):
            self._format_await(node)
        elif isinstance(node, Generator):
            self._format_generator(node)
        elif isinstance(node, Decorator):
            self._format_decorator(node)
        elif isinstance(node, TypeHint):
            self._format_type_hint(node)
        elif isinstance(node, NoOp):
            pass  # Skip
        elif isinstance(node, (Break, Continue)):
            self._format_control_statement(node)
        else:
            # Fallback for unknown types
            self._add_line(str(node))

    def _format_program(self, node):
        """Format program with proper spacing"""
        for i, stmt in enumerate(node.statements):
            self._format_ast(stmt)
            if i < len(node.statements) - 1:
                self._add_blank_line()

    def _format_block(self, node):
        """Format block with proper indentation"""
        self.current_indent += 1
        statements = getattr(node, "statements", [])
        for i, stmt in enumerate(statements):
            self._format_ast(stmt)
            if i < len(statements) - 1 and self.config.line_break_after_statements:
                self._add_blank_line()
        self.current_indent -= 1

    def _format_var_decl(self, node):
        """Format variable declaration"""
        var_name = node.var_name.name if hasattr(node.var_name, "name") else str(node.var_name)
        self._add_to_current_line(f"{var_name} itu ")
        if node.value:
            self._format_ast(node.value)
        self._flush_current_line()

    def _format_multi_var_decl(self, node):
        """Format multiple variable declaration"""
        var_names = [var.name if hasattr(var, "name") else str(var) for var in node.variables]
        self._add_to_current_line(f"{', '.join(var_names)} itu ")
        if node.value:
            self._format_ast(node.value)
        self._flush_current_line()

    def _format_assign(self, node):
        """Format assignment"""
        try:
            var_name = node.var.name if hasattr(node.var, "name") else str(node.var)
            # Clean up object string representation
            if "<renzmc.core.ast." in var_name:
                var_name = "[VAR_ERROR]"
            self._add_to_current_line(f"{var_name} = ")
            if node.value:
                self._format_ast(node.value)
            self._flush_current_line()
        except Exception as e:
            self._add_to_current_line("# ASSIGNMENT_FORMAT_ERROR")
            self._flush_current_line()

    def _format_multi_assign(self, node):
        """Format multiple assignment"""
        vars_str = ", ".join([v.name if hasattr(v, "name") else str(v) for v in node.variables])
        self._add_to_current_line(f"{vars_str} = ")
        if node.value:
            self._format_ast(node.value)
        self._flush_current_line()

    def _format_compound_assign(self, node):
        """Format compound assignment"""
        var_name = node.var.name if hasattr(node.var, "name") else str(node.var)
        op_str = self.complete_operator_map.get(node.op.type.name, str(node.op.type))
        self._add_to_current_line(f"{var_name} {op_str} ")
        if node.value:
            self._format_ast(node.value)
        self._flush_current_line()

    def _format_func_decl(self, node):
        """Format function declaration - handle both syntaxes"""
        params_str = self._format_params(node.params)

        # Check function syntax type by looking at the token
        if hasattr(node, "token") and node.token.type.name == "BUAT":
            # "buat fungsi nama dengan param" syntax
            self._add_line(f"buat fungsi {node.name} dengan {params_str}")
        else:
            # "fungsi nama(param):" syntax
            self._add_line(f"fungsi {node.name}({params_str}):")

        # Format function body
        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_async_func_decl(self, node):
        """Format async function declaration"""
        params_str = self._format_params(node.params)
        self._add_line(f"async fungsi {node.name}({params_str}):")

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_method_decl(self, node):
        """Format method declaration"""
        params_str = self._format_params(node.params)
        self._add_line(f"metode {node.name}({params_str}):")

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_async_method_decl(self, node):
        """Format async method declaration"""
        params_str = self._format_params(node.params)
        self._add_line(f"async metode {node.name}({params_str}):")

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_static_method_decl(self, node):
        """Format static method declaration"""
        params_str = self._format_params(node.params)
        self._add_line(f"metode_statis {node.name}({params_str}):")

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_class_method_decl(self, node):
        """Format class method declaration"""
        params_str = self._format_params(node.params)
        self._add_line(f"metode_kelas {node.name}({params_str}):")

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_class_decl(self, node):
        """Format class declaration"""
        if hasattr(node, "parent_class") and node.parent_class:
            self._add_line(f"kelas {node.name} warisi {node.parent_class}")
        else:
            self._add_line(f"kelas {node.name}")

        if hasattr(node, "methods") and node.methods:
            self.current_indent += 1
            for method in node.methods:
                self._format_ast(method)
                self._add_blank_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_func_call(self, node):
        """Format function call - handle various call types"""
        if hasattr(node, "name") and node.name:
            args_str = self._format_args(node.args)

            # Handle different call syntaxes
            if hasattr(node, "call_type"):
                if node.call_type == "panggil":
                    self._add_to_current_line(f"panggil {node.name} dengan {args_str}")
                else:
                    self._add_to_current_line(f"{node.name}({args_str})")
            else:
                self._add_to_current_line(f"{node.name}({args_str})")
        else:
            if hasattr(node, "func_expr"):
                self._format_ast(node.func_expr)
                args_str = self._format_args(node.args)
                self._add_to_current_line(f"({args_str})")

    def _format_method_call(self, node):
        """Format method call"""
        if hasattr(node, "object") and hasattr(node, "method"):
            self._format_ast(node.object)
            self._add_to_current_line(".")
            self._add_to_current_line(node.method)
            args_str = self._format_args(node.args)
            self._add_to_current_line(f"({args_str})")

    def _format_python_call(self, node):
        """Format Python function call"""
        if hasattr(node, "module") and hasattr(node, "func"):
            self._add_to_current_line(f"panggil_python {node.module}.{node.func}")
            args_str = self._format_args(node.args)
            if args_str:
                self._add_to_current_line(f" dengan {args_str}")
        elif hasattr(node, "func"):
            self._add_to_current_line(f"panggil_python {node.func}")
            args_str = self._format_args(node.args)
            if args_str:
                self._add_to_current_line(f" dengan {args_str}")

    def _format_if(self, node):
        """Format if statement - handle elif properly"""
        self._add_to_current_line("jika ")
        self._format_ast(node.condition)
        self._flush_current_line()

        # Format if body
        if isinstance(node.if_body, list):
            self.current_indent += 1
            for stmt in node.if_body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.if_body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

        # Handle elif chains
        elif_blocks = getattr(node, "elif_blocks", [])
        for elif_block in elif_blocks:
            self._add_line("lainnya jika ")
            self._format_ast(elif_block.condition)
            self._flush_current_line()

            if isinstance(elif_block.body, list):
                self.current_indent += 1
                for stmt in elif_block.body:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1
            else:
                self.current_indent += 1
                self._format_ast(elif_block.body)
                self._flush_current_line()
                self.current_indent -= 1

            self._add_line("selesai")

        # Handle else block
        if node.else_body:
            self._add_line("lainnya")
            if isinstance(node.else_body, list):
                self.current_indent += 1
                for stmt in node.else_body:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1
            else:
                self.current_indent += 1
                self._format_ast(node.else_body)
                self._flush_current_line()
                self.current_indent -= 1
            self._add_line("selesai")

    def _format_while(self, node):
        """Format while loop"""
        self._add_to_current_line("selama ")
        self._format_ast(node.condition)
        self._flush_current_line()

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_for(self, node):
        """Format for loop"""
        var_name = node.var_name.name if hasattr(node.var_name, "name") else str(node.var_name)
        self._add_to_current_line(f"untuk {var_name} dari ")
        self._format_ast(node.start)
        self._add_to_current_line(" sampai ")
        self._format_ast(node.end)
        self._flush_current_line()

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_for_each(self, node):
        """Format for each loop"""
        var_name = node.var_name.name if hasattr(node.var_name, "name") else str(node.var_name)
        self._add_to_current_line(f"untuk setiap {var_name} dalam ")
        self._format_ast(node.iterable)
        self._flush_current_line()

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.body)
            self._flush_current_line()
            self.current_indent -= 1

        self._add_line("selesai")

    def _format_try_catch(self, node):
        """Format try-catch block"""
        self._add_line("coba")

        if isinstance(node.try_block, list):
            self.current_indent += 1
            for stmt in node.try_block:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1
        else:
            self.current_indent += 1
            self._format_ast(node.try_block)
            self._flush_current_line()
            self.current_indent -= 1

        # Handle except blocks
        except_blocks = getattr(node, "except_blocks", [])
        for except_block in except_blocks:
            self._add_line("tangkap")
            if isinstance(except_block, list):
                self.current_indent += 1
                for stmt in except_block:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1
            else:
                self.current_indent += 1
                self._format_ast(except_block)
                self._flush_current_line()
                self.current_indent -= 1

        # Handle finally block
        if hasattr(node, "finally_block") and node.finally_block:
            self._add_line("akhirnya")
            if isinstance(node.finally_block, list):
                self.current_indent += 1
                for stmt in node.finally_block:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1
            else:
                self.current_indent += 1
                self._format_ast(node.finally_block)
                self._flush_current_line()
                self.current_indent -= 1

        self._add_line("selesai")

    def _format_switch(self, node):
        """Format switch statement"""
        self._add_to_current_line("cocok ")
        self._format_ast(node.expression)
        self._add_to_current_line(":")
        self._flush_current_line()

        # Handle cases
        cases = getattr(node, "cases", [])
        for case in cases:
            self._add_line("kasus")
            if isinstance(case, list):
                self.current_indent += 1
                for stmt in case:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1

        # Handle default
        if hasattr(node, "default_case") and node.default_case:
            self._add_line("bawaan")
            if isinstance(node.default_case, list):
                self.current_indent += 1
                for stmt in node.default_case:
                    self._format_ast(stmt)
                    self._flush_current_line()
                self.current_indent -= 1

        self._add_line("selesai")

    def _format_import(self, node):
        """Format import statement"""
        if hasattr(node, "alias") and node.alias:
            self._add_line(f"impor {node.module} sebagai {node.alias}")
        else:
            self._add_line(f"impor {node.module}")

    def _format_python_import(self, node):
        """Format Python import statement"""
        if hasattr(node, "alias") and node.alias:
            self._add_line(f"impor_python {node.module} sebagai {node.alias}")
        else:
            self._add_line(f"impor_python {node.module}")

    def _format_from_import(self, node):
        """Format from import statement"""
        imports = ", ".join(node.imports) if hasattr(node, "imports") else ""
        self._add_line(f"impor {imports} dari {node.module}")

    def _format_binop(self, node):
        """Format binary operation with complete operator mapping"""
        self._format_ast(node.left)
        self._add_to_current_line(" ")

        # Get operator from complete mapping
        if hasattr(node.op, "type"):
            op_str = self.complete_operator_map.get(node.op.type.name, str(node.op.type.name))
        else:
            op_str = str(node.op)

        self._add_to_current_line(op_str)
        self._add_to_current_line(" ")
        self._format_ast(node.right)

    def _format_unaryop(self, node):
        """Format unary operation"""
        if hasattr(node.op, "type"):
            op_str = self.complete_operator_map.get(node.op.type.name, str(node.op.type.name))
        else:
            op_str = str(node.op)

        self._add_to_current_line(op_str)
        self._format_ast(node.expr)

    def _format_num(self, node):
        """Format number"""
        self._add_to_current_line(str(node.value))

    def _format_string(self, node):
        """Format string - preserve quotes"""
        if hasattr(node, "value"):
            value = node.value
            # Preserve original quote style
            if (value.startswith('"') and value.endswith('"')) or (
                value.startswith("'") and value.endswith("'")
            ):
                self._add_to_current_line(value)
            else:
                quote = self.config.string_quotes
                self._add_to_current_line(f"{quote}{value}{quote}")

    def _format_format_string(self, node):
        """Format f-string properly"""
        if hasattr(node, "parts"):
            formatted_parts = []
            for part in node.parts:
                if hasattr(part, "value"):  # String part
                    value = part.value
                    if (value.startswith('"') and value.endswith('"')) or (
                        value.startswith("'") and value.endswith("'")
                    ):
                        formatted_parts.append(value[1:-1])  # Remove existing quotes
                    else:
                        formatted_parts.append(value)
                elif hasattr(part, "name"):  # Variable part
                    formatted_parts.append(f"{{{part.name}}}")
                else:
                    formatted_parts.append(str(part))

            if formatted_parts:
                self._add_to_current_line(f'f"{"".join(formatted_parts)}"')
            else:
                self._add_to_current_line('f""')

    def _format_var(self, node):
        """Format variable"""
        self._add_to_current_line(node.name)

    def _format_self_var(self, node):
        """Format self variable"""
        self._add_to_current_line("diri")

    def _format_boolean(self, node):
        """Format boolean"""
        if hasattr(node, "value"):
            self._add_to_current_line("benar" if node.value else "salah")

    def _format_print(self, node):
        """Format print statement"""
        self._add_to_current_line("tampilkan ")
        self._format_ast(node.expr)
        self._flush_current_line()

    def _format_return(self, node):
        """Format return statement"""
        self._add_to_current_line("hasil ")
        self._format_ast(node.expr)
        self._flush_current_line()

    def _format_list(self, node):
        """Format list"""
        elements = getattr(node, "elements", [])
        if not elements:
            self._add_to_current_line("[]")
        else:
            self._add_to_current_line("[")
            for i, elem in enumerate(elements):
                self._format_ast(elem)
                if i < len(elements) - 1:
                    self._add_to_current_line(", ")
            self._add_to_current_line("]")

    def _format_dict(self, node):
        """Format dictionary"""
        pairs = getattr(node, "pairs", [])
        if not pairs:
            self._add_to_current_line("{}")
        else:
            self._add_to_current_line("{")
            for i, (key, value) in enumerate(pairs):
                self._format_ast(key)
                self._add_to_current_line(": ")
                self._format_ast(value)
                if i < len(pairs) - 1:
                    self._add_to_current_line(", ")
            self._add_to_current_line("}")

    def _format_tuple(self, node):
        """Format tuple"""
        elements = getattr(node, "elements", [])
        if not elements:
            self._add_to_current_line("()")
        else:
            self._add_to_current_line("(")
            for i, elem in enumerate(elements):
                self._format_ast(elem)
                if i < len(elements) - 1:
                    self._add_to_current_line(", ")
            self._add_to_current_line(")")

    def _format_set(self, node):
        """Format set"""
        elements = getattr(node, "elements", [])
        if not elements:
            self._add_to_current_line("set()")
        else:
            self._add_to_current_line("{")
            for i, elem in enumerate(elements):
                self._format_ast(elem)
                if i < len(elements) - 1:
                    self._add_to_current_line(", ")
            self._add_to_current_line("}")

    def _format_lambda(self, node):
        """Format lambda"""
        params_str = self._format_params(node.params)
        self._add_to_current_line(f"lambda({params_str}): ")
        self._format_ast(node.body)

    def _format_attribute_ref(self, node):
        """Format attribute reference"""
        if hasattr(node, "object") and hasattr(node, "attribute"):
            self._format_ast(node.object)
            self._add_to_current_line(f".{node.attribute}")

    def _format_index_access(self, node):
        """Format index access"""
        if hasattr(node, "object") and hasattr(node, "index"):
            self._format_ast(node.object)
            self._add_to_current_line("[")
            self._format_ast(node.index)
            self._add_to_current_line("]")
        else:
            # Fallback: use string representation but avoid object corruption
            try:
                fallback_str = str(node).replace("<renzmc.core.ast.", "").replace(" object at", "")
                self._add_to_current_line(fallback_str)
            except:
                self._add_to_current_line("[INDEX_ACCESS_ERROR]")

    def _format_slice_access(self, node):
        """Format slice access"""
        if hasattr(node, "object"):
            self._format_ast(node.object)
            self._add_to_current_line("[")
            if hasattr(node, "start"):
                self._format_ast(node.start)
            self._add_to_current_line(":")
            if hasattr(node, "end"):
                self._format_ast(node.end)
            self._add_to_current_line("]")

    def _format_ternary(self, node):
        """Format ternary operator"""
        if (
            hasattr(node, "condition")
            and hasattr(node, "true_expr")
            and hasattr(node, "false_expr")
        ):
            self._format_ast(node.true_expr)
            self._add_to_current_line(" jika ")
            self._format_ast(node.condition)
            self._add_to_current_line(" lainnya ")
            self._format_ast(node.false_expr)

    def _format_walrus_operator(self, node):
        """Format walrus operator"""
        if hasattr(node, "var") and hasattr(node, "expr"):
            self._format_ast(node.var)
            self._add_to_current_line(" := ")
            self._format_ast(node.expr)

    def _format_with(self, node):
        """Format with statement"""
        self._add_to_current_line("dengan ")
        if hasattr(node, "context"):
            self._format_ast(node.context)
        self._add_to_current_line(":")
        self._flush_current_line()

        if isinstance(node.body, list):
            self.current_indent += 1
            for stmt in node.body:
                self._format_ast(stmt)
                self._flush_current_line()
            self.current_indent -= 1

    def _format_yield(self, node):
        """Format yield"""
        self._add_to_current_line("yield ")
        self._format_ast(node.expr)

    def _format_yield_from(self, node):
        """Format yield from"""
        self._add_to_current_line("yield dari ")
        self._format_ast(node.expr)

    def _format_await(self, node):
        """Format await"""
        self._add_to_current_line("await ")
        self._format_ast(node.expr)

    def _format_generator(self, node):
        """Format generator"""
        self._add_to_current_line("generator ")
        self._format_ast(node.expr)

    def _format_decorator(self, node):
        """Format decorator"""
        if hasattr(node, "name"):
            self._add_line(f"@{node.name}")

    def _format_type_hint(self, node):
        """Format type hint"""
        if hasattr(node, "type"):
            self._format_ast(node.type)

    def _format_control_statement(self, node):
        """Format break/continue"""
        if isinstance(node, Break):
            self._add_line("berhenti")
        elif isinstance(node, Continue):
            self._add_line("lanjut")

    def _format_params(self, params):
        """Format function parameters"""
        if not params:
            return ""

        param_names = []
        for param in params:
            if hasattr(param, "name"):
                param_names.append(param.name)
            else:
                param_names.append(str(param))

        return ", ".join(param_names)

    def _format_args(self, args):
        """Format function arguments"""
        if not args:
            return ""

        arg_values = []
        for arg in args:
            self.current_indent = 0  # Reset for arg formatting
            self.current_line = ""
            self._format_ast(arg)
            arg_values.append(self.current_line.strip())

        # Reset after formatting
        self.current_line = ""

        return ", ".join(arg_values)

    def _add_to_current_line(self, text):
        """Add text to current line"""
        self.current_line += text

    def _add_line(self, line=""):
        """Add a complete line with proper indentation"""
        if self.current_indent > 0:
            self.lines.append(self.indent_string * self.current_indent + line)
        else:
            self.lines.append(line)
        self.current_line = ""

    def _add_blank_line(self):
        """Add a blank line"""
        if self.lines and self.lines[-1].strip():
            self.lines.append("")

    def _flush_current_line(self):
        """Flush current line to lines list"""
        if self.current_line.strip():
            self._add_line(self.current_line)
        self.current_line = ""

    def _post_process(self, code):
        """Post-process formatted code"""
        lines = code.split("\n")
        processed_lines = []

        for line in lines:
            stripped = line.strip()

            if not stripped or stripped.startswith("//"):
                processed_lines.append("")
                continue

            # Handle line length
            if self.config.max_line_length > 0 and len(stripped) > self.config.max_line_length:
                wrapped_lines = self._wrap_long_line(line)
                processed_lines.extend(wrapped_lines)
            else:
                processed_lines.append(line)

        return "\n".join(processed_lines).strip() + "\n"

    def _wrap_long_line(self, line):
        """Wrap long lines intelligently"""
        indent_match = re.match(r"^(\s*)", line)
        indent = indent_match.group(1) if indent_match else ""
        content = line[len(indent) :]

        # Smart wrapping based on syntax
        if " itu " in content:
            parts = content.split(" itu ", 1)
            return [f"{indent}{parts[0]} itu", f"{indent}{self.indent_string}{parts[1]}"]
        elif " dengan " in content:
            parts = content.split(" dengan ", 1)
            return [f"{indent}{parts[0]} dengan", f"{indent}{self.indent_string}{parts[1]}"]
        elif " panggil_python " in content:
            # Don't wrap python calls
            return [line]
        else:
            return [line]

    def _safe_fallback_format(self, source_code):
        """Safe fallback that never corrupts code"""
        lines = source_code.split("\n")
        formatted_lines = []
        indent_level = 0

        for line in lines:
            stripped = line.rstrip()  # Preserve content, only remove trailing whitespace

            if not stripped:
                formatted_lines.append("")
                continue

            # Simple indentation fix
            if stripped.startswith(tuple(self.end_keywords)):
                indent_level = max(0, indent_level - 1)

            if indent_level > 0 and not stripped.startswith("//"):
                formatted_lines.append(self.indent_string * indent_level + stripped)
            else:
                formatted_lines.append(stripped)

            if stripped.startswith(tuple(self.block_keywords)) and "selesai" not in stripped:
                indent_level += 1

        return "\n".join(formatted_lines)


def format_file(filepath, config=None):
    formatter = RenzmcFormatter(config)
    return formatter.format_file(filepath)


def format_code(source_code, config=None):
    formatter = RenzmcFormatter(config)
    return formatter.format_code(source_code)
