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

"""
RenzmcLang Interpreter Expression Visitors Module

This module contains expression visitors methods.
"""


from renzmc.core.error import DivisionByZeroError
from renzmc.core.token import TokenType

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class ExpressionVisitorsMixin:
    """
    Mixin class for expression visitors.

    Provides 4 methods for handling expression visitors.
    """

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op.type == TokenType.TAMBAH:
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.op.type == TokenType.KURANG:
            return left - right
        elif node.op.type == TokenType.KALI_OP:
            if isinstance(left, str) and isinstance(right, int):
                return left * right
            elif isinstance(left, int) and isinstance(right, str):
                return right * left
            return left * right
        elif node.op.type == TokenType.BAGI:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left / right
        elif node.op.type == TokenType.SISA_BAGI:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left % right
        elif node.op.type == TokenType.PANGKAT:
            return left**right
        elif node.op.type == TokenType.PEMBAGIAN_BULAT:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left // right
        elif node.op.type == TokenType.SAMA_DENGAN:
            return left == right
        elif node.op.type == TokenType.TIDAK_SAMA:
            return left != right
        elif node.op.type == TokenType.LEBIH_DARI:
            return left > right
        elif node.op.type == TokenType.KURANG_DARI:
            return left < right
        elif node.op.type == TokenType.LEBIH_SAMA:
            return left >= right
        elif node.op.type == TokenType.KURANG_SAMA:
            return left <= right
        elif node.op.type == TokenType.DAN:
            return left and right
        elif node.op.type == TokenType.ATAU:
            return left or right
        elif node.op.type in (TokenType.BIT_DAN, TokenType.BITWISE_AND):
            return int(left) & int(right)
        elif node.op.type in (TokenType.BIT_ATAU, TokenType.BITWISE_OR):
            return int(left) | int(right)
        elif node.op.type in (TokenType.BIT_XOR, TokenType.BITWISE_XOR):
            return int(left) ^ int(right)
        elif node.op.type == TokenType.GESER_KIRI:
            return int(left) << int(right)
        elif node.op.type == TokenType.GESER_KANAN:
            return int(left) >> int(right)
        elif node.op.type in (TokenType.DALAM, TokenType.DALAM_OP):
            if not hasattr(right, "__iter__") and not hasattr(right, "__contains__"):
                raise TypeError(f"argument of type '{type(right).__name__}' is not iterable")
            return left in right
        elif node.op.type == TokenType.TIDAK_DALAM:
            if not hasattr(right, "__iter__") and not hasattr(right, "__contains__"):
                raise TypeError(f"argument of type '{type(right).__name__}' is not iterable")
            return left not in right
        elif node.op.type in (TokenType.ADALAH, TokenType.ADALAH_OP):
            return left is right
        elif node.op.type == TokenType.BUKAN:
            return left is not right
        raise RuntimeError(f"Operator tidak didukung: {node.op.type}")

    def visit_UnaryOp(self, node):
        expr = self.visit(node.expr)
        if node.op.type == TokenType.TAMBAH:
            return +expr
        elif node.op.type == TokenType.KURANG:
            return -expr
        elif node.op.type in (TokenType.TIDAK, TokenType.NOT):
            return not expr
        elif node.op.type in (TokenType.BIT_NOT, TokenType.BITWISE_NOT):
            return ~int(expr)
        raise RuntimeError(f"Operator unary tidak didukung: {node.op.type}")

    def visit_Ternary(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.if_expr)
        else:
            return self.visit(node.else_expr)

    def visit_WalrusOperator(self, node):
        value = self.visit(node.value)
        self.set_variable(node.var_name, value)
        return value
