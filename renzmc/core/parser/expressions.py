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

from renzmc.core.ast import (
    AttributeRef,
    Await,
    BinOp,
    Boolean,
    FormatString,
    IndexAccess,
    MethodCall,
    NoneValue,
    Num,
    SelfVar,
    SliceAccess,
    String,
    Ternary,
    Tuple,
    UnaryOp,
    Var,
    WalrusOperator,
)
from renzmc.core.token import Token, TokenType


class ExpressionParser:
    """
    Expression parsing methods for handling operators and precedence.
    """

    def _validate_slice_index(self, node, param_name):
        """
        Validate that a slice index is an integer, not a float.

        Args:
            node: The AST node to validate
            param_name: Name of the parameter (for error message)


        Raises:
            Exception: If the index is a float literal
        """
        if node is None:
            return

        if isinstance(node, Num):
            if isinstance(node.value, float):
                self.error(
                    f"[RMC-P009] Indeks slice '{param_name}' harus integer, bukan float. "
                    f"Gunakan {int(node.value)} atau konversi dengan ke_bulat().",
                )

    def _validate_slice_step(self, step_node):
        """
        Validate that slice step is not zero.

        Args:
            step_node: The AST node for the step parameter


        Raises:
            Exception: If step is zero
        """
        if step_node is None:
            return

        if isinstance(step_node, Num):
            if step_node.value == 0:
                self.error(
                    "[RMC-P008] Slice step tidak boleh nol (0). "
                    "Gunakan step positif (1, 2, ...) atau negatif (-1, -2, ...) untuk reverse.",
                )

    def expr(self):
        return self.ternary()

    def ternary(self):
        node = self.walrus_expr()
        if self.current_token.type == TokenType.JIKA and (not self._in_comprehension):
            if_expr = node
            self.eat(TokenType.JIKA)
            condition = self.walrus_expr()
            if self.current_token.type == TokenType.LAINNYA:
                self.eat(TokenType.LAINNYA)
                else_expr = self.walrus_expr()
                node = Ternary(condition, if_expr, else_expr)
            elif (
                self.current_token.type == TokenType.KALAU
                and self.lexer.peek_token()
                and (self.lexer.peek_token().type == TokenType.TIDAK)
            ):
                self.eat(TokenType.KALAU)
                self.eat(TokenType.TIDAK)
                else_expr = self.walrus_expr()
                node = Ternary(condition, if_expr, else_expr)
            else:
                self.error(
                    "Operator ternary tidak lengkap: diharapkan 'kalau tidak' atau 'lainnya'"
                )
        return node

    def walrus_expr(self):
        if (
            self.current_token.type == TokenType.IDENTIFIER
            and self.lexer.peek_token()
            and (self.lexer.peek_token().type == TokenType.WALRUS)
        ):
            var_token = self.current_token
            var_name = var_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.WALRUS)
            value = self.logical_or()
            return WalrusOperator(var_name, value, var_token)
        else:
            return self.logical_or()

    def logical_or(self):
        node = self.logical_and()
        while self.current_token.type == TokenType.ATAU:
            token = self.current_token
            self.eat(TokenType.ATAU)
            node = BinOp(node, token, self.logical_and())
        return node

    def logical_and(self):
        node = self.identity()
        while self.current_token.type == TokenType.DAN:
            token = self.current_token
            self.eat(TokenType.DAN)
            node = BinOp(node, token, self.identity())
        return node

    def identity(self):
        node = self.membership()
        while self.current_token.type in (
            TokenType.ADALAH,
            TokenType.ADALAH_OP,
            TokenType.BUKAN,
        ):
            token = self.current_token
            if token.type == TokenType.ADALAH:
                self.eat(TokenType.ADALAH)
            elif token.type == TokenType.ADALAH_OP:
                self.eat(TokenType.ADALAH_OP)
            elif token.type == TokenType.BUKAN:
                self.eat(TokenType.BUKAN)
            node = BinOp(node, token, self.membership())
        return node

    def membership(self):
        node = self.equality()
        while self.current_token.type in (
            TokenType.DALAM,
            TokenType.DALAM_OP,
            TokenType.TIDAK_DALAM,
        ):
            token = self.current_token
            if token.type == TokenType.DALAM:
                self.eat(TokenType.DALAM)
            elif token.type == TokenType.DALAM_OP:
                self.eat(TokenType.DALAM_OP)
            elif token.type == TokenType.TIDAK_DALAM:
                self.eat(TokenType.TIDAK_DALAM)
            node = BinOp(node, token, self.equality())
        return node

    def equality(self):
        node = self.comparison()
        while self.current_token.type in (TokenType.SAMA_DENGAN, TokenType.TIDAK_SAMA):
            token = self.current_token
            if token.type == TokenType.SAMA_DENGAN:
                self.eat(TokenType.SAMA_DENGAN)
            elif token.type == TokenType.TIDAK_SAMA:
                self.eat(TokenType.TIDAK_SAMA)
            node = BinOp(node, token, self.comparison())
        return node

    def bitwise_or(self):
        node = self.bitwise_xor()
        while self.current_token.type == TokenType.BIT_ATAU:
            token = self.current_token
            self.eat(TokenType.BIT_ATAU)
            node = BinOp(node, token, self.bitwise_xor())
        return node

    def bitwise_xor(self):
        node = self.bitwise_and()
        while self.current_token.type == TokenType.BIT_XOR:
            token = self.current_token
            self.eat(TokenType.BIT_XOR)
            node = BinOp(node, token, self.bitwise_and())
        return node

    def bitwise_and(self):
        node = self.shift()
        while self.current_token.type == TokenType.BIT_DAN:
            token = self.current_token
            self.eat(TokenType.BIT_DAN)
            node = BinOp(node, token, self.shift())
        return node

    def shift(self):
        node = self.addition()
        while self.current_token.type in (TokenType.GESER_KIRI, TokenType.GESER_KANAN):
            token = self.current_token
            if token.type == TokenType.GESER_KIRI:
                self.eat(TokenType.GESER_KIRI)
            elif token.type == TokenType.GESER_KANAN:
                self.eat(TokenType.GESER_KANAN)
            node = BinOp(node, token, self.addition())
        return node

    def comparison(self):
        node = self.bitwise_or()
        while self.current_token.type in (
            TokenType.LEBIH_DARI,
            TokenType.KURANG_DARI,
            TokenType.LEBIH_SAMA,
            TokenType.KURANG_SAMA,
        ):
            token = self.current_token
            if token.type == TokenType.LEBIH_DARI:
                self.eat(TokenType.LEBIH_DARI)
            elif token.type == TokenType.KURANG_DARI:
                self.eat(TokenType.KURANG_DARI)
            elif token.type == TokenType.LEBIH_SAMA:
                self.eat(TokenType.LEBIH_SAMA)
            elif token.type == TokenType.KURANG_SAMA:
                self.eat(TokenType.KURANG_SAMA)
            node = BinOp(node, token, self.bitwise_or())
        return node

    def addition(self):
        node = self.term()
        while self.current_token.type in (TokenType.TAMBAH, TokenType.KURANG):
            token = self.current_token
            if token.type == TokenType.TAMBAH:
                self.eat(TokenType.TAMBAH)
            elif token.type == TokenType.KURANG:
                self.eat(TokenType.KURANG)
            node = BinOp(node, token, self.term())
        return node

    def term(self):
        node = self.unary()
        while self.current_token.type in (
            TokenType.KALI_OP,
            TokenType.BAGI,
            TokenType.SISA_BAGI,
            TokenType.PEMBAGIAN_BULAT,  # FIX BUG #2: Add floor division operator
        ):
            token = self.current_token
            if token.type == TokenType.KALI_OP:
                self.eat(TokenType.KALI_OP)
            elif token.type == TokenType.BAGI:
                self.eat(TokenType.BAGI)
            elif token.type == TokenType.SISA_BAGI:
                self.eat(TokenType.SISA_BAGI)
            elif token.type == TokenType.PEMBAGIAN_BULAT:  # FIX BUG #2: Handle floor division
                self.eat(TokenType.PEMBAGIAN_BULAT)
            node = BinOp(node, token, self.unary())
        return node

    def power(self):
        node = self.factor()
        if self.current_token.type == TokenType.PANGKAT:
            token = self.current_token
            self.eat(TokenType.PANGKAT)
            right = self.unary()
            node = BinOp(node, token, right)
        return node

    def unary(self):
        if self.current_token.type in (
            TokenType.TAMBAH,
            TokenType.KURANG,
            TokenType.TIDAK,
            TokenType.BUKAN,
            TokenType.BIT_NOT,
        ):
            token = self.current_token
            if token.type == TokenType.TAMBAH:
                self.eat(TokenType.TAMBAH)
            elif token.type == TokenType.KURANG:
                self.eat(TokenType.KURANG)
            elif token.type == TokenType.TIDAK:
                self.eat(TokenType.TIDAK)
            elif token.type == TokenType.BUKAN:
                self.eat(TokenType.BUKAN)
            elif token.type == TokenType.BIT_NOT:
                self.eat(TokenType.BIT_NOT)
            return UnaryOp(token, self.unary())
        else:
            return self.power()

    def end_of_expression(self):
        return self.current_token.type in (
            TokenType.NEWLINE,
            TokenType.EOF,
            TokenType.KURUNG_AKHIR,
            TokenType.DAFTAR_AKHIR,
            TokenType.KAMUS_AKHIR,
            TokenType.TUPLE_AKHIR,
            TokenType.HIMPUNAN_AKHIR,
            TokenType.KOMA,
            TokenType.TITIK_KOMA,
        )

    def factor(self):
        token = self.current_token
        if self.end_of_expression():
            self.error(f"Kesalahan sintaks: Diharapkan ekspresi, ditemukan '{token.type}'")
        primary = None
        if token.type == TokenType.ANGKA:
            self.eat(TokenType.ANGKA)
            primary = Num(token)
        elif token.type == TokenType.TEKS:
            self.eat(TokenType.TEKS)
            primary = String(token)
        elif token.type == TokenType.FORMAT_STRING:
            self.eat(TokenType.FORMAT_STRING)
            parts = self.parse_format_string(token.value)
            primary = FormatString(parts, token)
        elif token.type == TokenType.BOOLEAN:
            self.eat(TokenType.BOOLEAN)
            primary = Boolean(token)
        elif token.type == TokenType.BENAR:
            self.eat(TokenType.BENAR)
            # FIX: Convert string "benar" to Python boolean True
            bool_token = Token(TokenType.BENAR, True, token.line, token.column)
            primary = Boolean(bool_token)
        elif token.type == TokenType.SALAH:
            self.eat(TokenType.SALAH)
            # FIX: Convert string "salah" to Python boolean False
            bool_token = Token(TokenType.SALAH, False, token.line, token.column)
            primary = Boolean(bool_token)
        elif token.type == TokenType.NONE:
            self.eat(TokenType.NONE)
            primary = NoneValue(token)
        elif token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type == TokenType.BIT_ATAU:
                self.eat(TokenType.BIT_ATAU)
                elements = []
                while self.current_token.type != TokenType.BIT_ATAU:
                    elements.append(self.bitwise_xor())
                    if self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                    elif self.current_token.type == TokenType.BIT_ATAU:
                        break
                    else:
                        self.error(
                            f"Expected ',' or '|' in pipe tuple, got {self.current_token.type}"
                        )
                self.eat(TokenType.BIT_ATAU)
                self.eat(TokenType.KURUNG_AKHIR)
                primary = Tuple(elements, token)
            else:
                first_expr = self.expr()
                if self.current_token.type == TokenType.KOMA:
                    elements = [first_expr]
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        elements.append(self.expr())
                    self.eat(TokenType.KURUNG_AKHIR)
                    primary = Tuple(elements, token)
                else:
                    self.eat(TokenType.KURUNG_AKHIR)
                    primary = first_expr
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.KURUNG_AWAL:
                primary = self.parse_function_call(token.value, token)
            else:
                primary = Var(token)
        elif token.type == TokenType.HASIL:
            self.eat(TokenType.HASIL)
            identifier_token = Token(TokenType.IDENTIFIER, token.value, token.line, token.column)
            primary = Var(identifier_token)
        elif token.type == TokenType.SELF:
            self.eat(TokenType.SELF)
            primary = SelfVar(token.value, token)
        elif token.type == TokenType.AWAIT:
            self.eat(TokenType.AWAIT)
            expr = self.factor()
            primary = Await(expr, token)
        elif token.type == TokenType.PANGGIL:
            primary = self.function_call()
        elif token.type == TokenType.PANGGIL_PYTHON:
            primary = self.python_call_expression()
        elif token.type == TokenType.DAFTAR_AWAL:
            primary = self.list_literal()
        elif token.type == TokenType.KAMUS_AWAL:
            primary = self.dict_literal()
        elif token.type == TokenType.HIMPUNAN_AWAL:
            primary = self.set_literal()
        elif token.type == TokenType.TUPLE_AWAL:
            primary = self.tuple_literal()
        elif token.type == TokenType.AWAIT:
            self.eat(TokenType.AWAIT)
            expr = self.factor()
            primary = Await(expr, token)
        elif token.type == TokenType.LAMBDA:
            primary = self.lambda_expr()
        else:
            self.error(f"Kesalahan sintaks: Token tidak terduga '{token.type}'")
        return self.apply_postfix_operations(primary)

    def parse_postfix_expression(self, obj_token):
        obj = Var(obj_token)
        while self.current_token.type in (TokenType.TITIK, TokenType.DAFTAR_AWAL):
            if self.current_token.type == TokenType.TITIK:
                self.eat(TokenType.TITIK)
                attr_name = self.current_token.value
                attr_token = self.current_token
                if self.current_token.type == TokenType.IDENTIFIER:
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type in self._get_allowed_attribute_keywords():
                    self.advance_token()
                else:
                    self.error(
                        f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                    )
                if self.current_token.type == TokenType.KURUNG_AWAL:
                    self.eat(TokenType.KURUNG_AWAL)
                    args = []
                    if self.current_token.type != TokenType.KURUNG_AKHIR:
                        args.append(self.expr())
                        while self.current_token.type == TokenType.KOMA:
                            self.eat(TokenType.KOMA)
                            args.append(self.expr())
                    self.eat(TokenType.KURUNG_AKHIR)
                    obj = MethodCall(obj, attr_name, args, attr_token)
                else:
                    obj = AttributeRef(obj, attr_name, attr_token)
            elif self.current_token.type == TokenType.DAFTAR_AWAL:
                index_token = self.current_token
                self.eat(TokenType.DAFTAR_AWAL)

                # Check if this is a slice or simple index
                start = None
                end = None
                step = None
                is_slice = False

                # Parse start (or check for leading colon)
                if self.current_token.type != TokenType.TITIK_DUA:
                    start = self.expr()

                # Check for colon (indicates slice)
                if self.current_token.type == TokenType.TITIK_DUA:
                    is_slice = True
                    self.eat(TokenType.TITIK_DUA)

                    # Parse end (or check for another colon)
                    if (
                        self.current_token.type != TokenType.TITIK_DUA
                        and self.current_token.type != TokenType.DAFTAR_AKHIR
                    ):
                        end = self.expr()

                    # Check for step (second colon)
                    if self.current_token.type == TokenType.TITIK_DUA:
                        self.eat(TokenType.TITIK_DUA)
                        if self.current_token.type != TokenType.DAFTAR_AKHIR:
                            step = self.expr()

                self.eat(TokenType.DAFTAR_AKHIR)

                # Create appropriate AST node
                if is_slice:
                    self._validate_slice_index(start, "start")
                    self._validate_slice_index(end, "end")
                    self._validate_slice_index(step, "step")
                    self._validate_slice_step(step)
                    obj = SliceAccess(obj, start, end, step, index_token)
                else:
                    obj = IndexAccess(obj, start, index_token)

    def apply_postfix_operations(self, primary):
        expr = primary
        while self.current_token.type in (
            TokenType.TITIK,
            TokenType.DAFTAR_AWAL,
            TokenType.KURUNG_AWAL,
        ):
            if self.current_token.type == TokenType.TITIK:
                self.eat(TokenType.TITIK)
                attr_name = self.current_token.value
                attr_token = self.current_token
                if self.current_token.type == TokenType.IDENTIFIER:
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type in self._get_allowed_attribute_keywords():
                    self.advance_token()
                else:
                    self.error(
                        f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                    )
                if self.current_token.type == TokenType.KURUNG_AWAL:
                    self.eat(TokenType.KURUNG_AWAL)
                    args, kwargs = self.parse_arguments()
                    self.eat(TokenType.KURUNG_AKHIR)
                    expr = MethodCall(expr, attr_name, args, attr_token, kwargs)
                else:
                    expr = AttributeRef(expr, attr_name, attr_token)
            elif self.current_token.type == TokenType.DAFTAR_AWAL:
                index_token = self.current_token
                self.eat(TokenType.DAFTAR_AWAL)

                # Check if this is a slice or simple index
                start = None
                end = None
                step = None
                is_slice = False

                # Parse start (or check for leading colon)
                if self.current_token.type != TokenType.TITIK_DUA:
                    start = self.expr()

                # Check for colon (indicates slice)
                if self.current_token.type == TokenType.TITIK_DUA:
                    is_slice = True
                    self.eat(TokenType.TITIK_DUA)

                    # Parse end (or check for another colon)
                    if (
                        self.current_token.type != TokenType.TITIK_DUA
                        and self.current_token.type != TokenType.DAFTAR_AKHIR
                    ):
                        end = self.expr()

                    # Check for step (second colon)
                    if self.current_token.type == TokenType.TITIK_DUA:
                        self.eat(TokenType.TITIK_DUA)
                        if self.current_token.type != TokenType.DAFTAR_AKHIR:
                            step = self.expr()

                self.eat(TokenType.DAFTAR_AKHIR)

                # Create appropriate AST node
                if is_slice:
                    # Validate slice parameters
                    self._validate_slice_index(start, "start")
                    self._validate_slice_index(end, "end")
                    self._validate_slice_index(step, "step")
                    self._validate_slice_step(step)
                    expr = SliceAccess(expr, start, end, step, index_token)
                else:
                    expr = IndexAccess(expr, start, index_token)
            elif self.current_token.type == TokenType.KURUNG_AWAL:
                call_token = self.current_token
                self.eat(TokenType.KURUNG_AWAL)
                args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
                expr = MethodCall(expr, "", args, call_token, kwargs)
        return expr
