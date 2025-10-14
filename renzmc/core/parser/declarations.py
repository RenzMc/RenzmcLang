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
RenzmcLang Parser Declarations Module

Declaration parsing methods for variables, functions, and classes.
"""

from renzmc.core.ast import (  # noqa: E402
    AsyncFuncDecl,
    ClassDecl,
    Constructor,
    FuncDecl,
    MethodDecl,
    MultiVarDecl,
    Tuple,
    VarDecl,
)
from renzmc.core.parser_type_helpers import parse_type_hint_advanced  # noqa: E402
from renzmc.core.token import TokenType


class DeclarationParser:
    """
    Declaration parsing methods for variables, functions, and classes.
    """

    def variable_declaration(self):
        var_info = []
        first_var = self.current_token.value
        token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        first_type = None
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
            first_type = parse_type_hint_advanced(self)
        var_info.append((first_var, first_type))
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            var_type = None
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
                var_type = parse_type_hint_advanced(self)
            var_info.append((var_name, var_type))
        self.eat(TokenType.ITU)
        if len(var_info) == 1 and self.current_token.type == TokenType.LAMBDA:
            value = self.lambda_expr()
            return VarDecl(var_info[0][0], value, token, var_info[0][1])
        values = []
        values.append(self.expr())
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            values.append(self.expr())
        if len(var_info) == 1 and len(values) == 1:
            return VarDecl(var_info[0][0], values[0], token, var_info[0][1])
        else:
            if len(values) > 1:
                values_expr = Tuple(values, token)
            else:
                values_expr = values[0]
            var_names = [info[0] for info in var_info]
            type_hints = {info[0]: info[1] for info in var_info if info[1] is not None}
            return MultiVarDecl(var_names, values_expr, token, type_hints)

    def buat_sebagai_declaration(self):
        token = self.current_token
        self.eat(TokenType.BUAT)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.SEBAGAI)
        value = self.expr()
        return VarDecl(var_name, value, token, None)

    def function_declaration(self):  # noqa: C901
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.FUNGSI)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        params = []
        param_types = {}
        return_type = None  # Initialize to avoid UnboundLocal error
        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type in (TokenType.IDENTIFIER, TokenType.SELF):
                param_name = self.current_token.value
                params.append(param_name)
                if self.current_token.type == TokenType.SELF:
                    self.eat(TokenType.SELF)
                else:
                    self.eat(TokenType.IDENTIFIER)
                if self.current_token.type == TokenType.TITIK_DUA:
                    self.eat(TokenType.TITIK_DUA)
                    # # type_name = self.current_token.value  # Unused variable  # Unused variable  # noqa: E501
                    param_types[param_name] = parse_type_hint_advanced(self)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    params.append(param_name)
                    if self.current_token.type == TokenType.SELF:
                        self.eat(TokenType.SELF)
                    else:
                        self.eat(TokenType.IDENTIFIER)
                    if self.current_token.type == TokenType.TITIK_DUA:
                        self.eat(TokenType.TITIK_DUA)
                        # # type_name = self.current_token.value  # Unused variable  # Unused variable  # noqa: E501
                        param_types[param_name] = parse_type_hint_advanced(self)
            self.eat(TokenType.KURUNG_AKHIR)
            return_type = None
            if self.current_token.type == TokenType.ARROW:
                self.eat(TokenType.ARROW)
                return_type = parse_type_hint_advanced(self)
            self.eat(TokenType.TITIK_DUA)
        elif self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type in (TokenType.IDENTIFIER, TokenType.SELF):
                params.append(self.current_token.value)
                if self.current_token.type == TokenType.SELF:
                    self.eat(TokenType.SELF)
                else:
                    self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    if self.current_token.type == TokenType.SELF:
                        self.eat(TokenType.SELF)
                    else:
                        self.eat(TokenType.IDENTIFIER)
            return_type = None
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            stmt = self.statement()
            if stmt is not None:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return FuncDecl(name, params, body, token, return_type, param_types)

    def async_function_declaration(self):  # noqa: C901
        token = self.current_token
        self.eat(TokenType.ASYNC)
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.FUNGSI)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.KURUNG_AWAL)
        params = []
        param_types = {}
        if self.current_token.type in (TokenType.IDENTIFIER, TokenType.SELF):
            param_name = self.current_token.value
            params.append(param_name)
            if self.current_token.type == TokenType.SELF:
                self.eat(TokenType.SELF)
            else:
                self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
                # # type_name = self.current_token.value  # Unused variable  # Unused variable  # noqa: E501
                param_types[param_name] = parse_type_hint_advanced(self)
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                param_name = self.current_token.value
                params.append(param_name)
                if self.current_token.type == TokenType.SELF:
                    self.eat(TokenType.SELF)
                else:
                    self.eat(TokenType.IDENTIFIER)
                if self.current_token.type == TokenType.TITIK_DUA:
                    self.eat(TokenType.TITIK_DUA)
                    # # type_name = self.current_token.value  # Unused variable  # Unused variable  # noqa: E501
                    param_types[param_name] = parse_type_hint_advanced(self)
        self.eat(TokenType.KURUNG_AKHIR)
        return_type = None
        if self.current_token.type == TokenType.ARROW:
            self.eat(TokenType.ARROW)
            return_type = parse_type_hint_advanced(self)
        self.eat(TokenType.TITIK_DUA)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            stmt = self.statement()
            if stmt is not None:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return AsyncFuncDecl(name, params, body, token, return_type, param_types)

    def class_declaration(self):  # noqa: C901
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.KELAS)
        class_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        parent = None
        if self.current_token.type == TokenType.WARISI:
            self.eat(TokenType.WARISI)
            parent = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.TITIK_DUA)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        methods = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            if self.current_token.type == TokenType.AT:
                self.eat(TokenType.AT)
                decorator_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.TITIK:
                    self.eat(TokenType.TITIK)
                    decorator_name += "." + self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                if self.current_token.type == TokenType.FUNGSI:
                    method = self.function_declaration()
                    if not hasattr(method, "decorator"):
                        method.decorator = decorator_name
                    methods.append(method)
                else:
                    self.error("Expected function after decorator")
            elif self.current_token.type == TokenType.KONSTRUKTOR:
                methods.append(self.constructor_declaration())
            elif self.current_token.type == TokenType.METODE:
                methods.append(self.method_declaration())
            elif self.current_token.type == TokenType.FUNGSI:
                methods.append(self.function_declaration())
            else:
                stmt = self.statement()
                if stmt:
                    methods.append(stmt)
        self.eat(TokenType.SELESAI)
        return ClassDecl(class_name, methods, parent, token)

    def constructor_declaration(self):  # noqa: C901
        token = self.current_token
        self.eat(TokenType.KONSTRUKTOR)
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    params.append(param_name)
            self.eat(TokenType.KURUNG_AKHIR)
            self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return Constructor(params, body, token)

    def constructor_declaration_with_buat(self):
        token = self.current_token
        self.eat(TokenType.BUAT)
        self.eat(TokenType.KONSTRUKTOR)
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return Constructor(params, body, token)

    def method_declaration(self):  # noqa: C901
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.METODE)
        method_name = self.current_token.value
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type in self._get_allowed_method_keywords():
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'")
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    params.append(param_name)
            self.eat(TokenType.KURUNG_AKHIR)
            self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return MethodDecl(method_name, params, body, token)
