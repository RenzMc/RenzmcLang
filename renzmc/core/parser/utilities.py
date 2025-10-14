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
RenzmcLang Parser Utilities Module

Utility parsing methods for common operations.
"""

from renzmc.core.ast import (  # noqa: E402
    AttributeRef,
    FuncCall,
    IndexAccess,
    Lambda,
    MethodCall,
    NoOp,
    PythonCall,
    SelfVar,
    Var,
)
from renzmc.core.token import Token, TokenType  # noqa: E402


class UtilityParser:
    """
    Utility parsing methods for common operations.
    """

    def lambda_expr(self):
        token = self.current_token
        self.eat(TokenType.LAMBDA)

        params = []

        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            param_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            params.append(param_name)
            self.eat(TokenType.ARROW)
        else:
            param_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            params.append(param_name)
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
            self.eat(TokenType.TITIK_DUA)

        body = self.expr()
        return Lambda(params, body, token)

    def function_call(self):  # noqa: C901
        token = self.current_token
        self.eat(TokenType.PANGGIL)
        name = self.current_token.value
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
        else:
            self.current_token = self.lexer.get_next_token()
        if self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            method_name = self.current_token.value
            if self.current_token.type == TokenType.IDENTIFIER:
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.KONSTRUKTOR)
            elif self.current_token.type in self._get_allowed_method_keywords():
                self.current_token = self.lexer.get_next_token()
            else:
                self.error(f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'")  # noqa: E501
            args = []
            kwargs = {}
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
            elif self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args, kwargs = self.parse_arguments_with_separator(TokenType.NEWLINE)
            return MethodCall(Var(Token(TokenType.IDENTIFIER, name)), method_name, args, token, kwargs)
        else:
            args = []
            kwargs = {}
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
            elif self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args, kwargs = self.parse_arguments_with_separator(TokenType.NEWLINE)
            return FuncCall(name, args, token, kwargs)

    def parse_block_until(self, stop_tokens):
        statements = []
        while self.current_token.type not in stop_tokens and self.current_token.type != TokenType.EOF:
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return statements

    def empty(self):
        return NoOp()

    def parse_function_call(self, func_name, token):
        self.eat(TokenType.KURUNG_AWAL)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        args, kwargs = self.parse_arguments()
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        self.eat(TokenType.KURUNG_AKHIR)
        return FuncCall(func_name, args, token, kwargs)

    def parse_attribute_access(self, obj_token):
        obj = Var(obj_token)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            attr_name = self.current_token.value
            attr_token = self.current_token
            if self.current_token.type == TokenType.IDENTIFIER:
                self.eat(TokenType.IDENTIFIER)
            elif self.current_token.type in self._get_allowed_attribute_keywords():
                self.advance_token()
            else:
                self.error(
                    f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"  # noqa: E501
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
        return obj

    def parse_arguments(self):  # noqa: C901
        positional_args = []
        keyword_args = {}
        seen_keyword = False
        if self.current_token.type == TokenType.KURUNG_AKHIR:
            return (positional_args, keyword_args)
        while True:
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

            if self.current_token.type == TokenType.KURUNG_AKHIR:
                break

            if self.current_token.type == TokenType.IDENTIFIER:
                next_token = self.lexer.peek_token()
                is_keyword_arg = next_token and next_token.type == TokenType.ASSIGNMENT
                if is_keyword_arg:
                    seen_keyword = True
                    arg_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    self.eat(TokenType.ASSIGNMENT)
                    arg_value = self.expr()
                    keyword_args[arg_name] = arg_value
                else:
                    if seen_keyword:
                        self.error(
                            "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"  # noqa: E501
                        )
                    positional_args.append(self.expr())
            else:
                if seen_keyword:
                    self.error(
                        "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"  # noqa: E501
                    )
                positional_args.append(self.expr())

            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

            if self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                if self.current_token.type == TokenType.KURUNG_AKHIR:
                    break
            else:
                break
        return (positional_args, keyword_args)

    def parse_arguments_with_separator(self, separator_token):
        positional_args = []
        keyword_args = {}
        seen_keyword = False
        while self.current_token.type != separator_token and self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.IDENTIFIER:
                next_token = self.lexer.peek_token()
                is_keyword_arg = next_token and next_token.type == TokenType.ASSIGNMENT
                if is_keyword_arg:
                    seen_keyword = True
                    arg_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    self.eat(TokenType.ASSIGNMENT)
                    arg_value = self.expr()
                    keyword_args[arg_name] = arg_value
                else:
                    if seen_keyword:
                        self.error(
                            "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"  # noqa: E501
                        )
                    positional_args.append(self.expr())
            else:
                if seen_keyword:
                    self.error(
                        "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"  # noqa: E501
                    )
                positional_args.append(self.expr())
            if self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
            else:
                break
        return (positional_args, keyword_args)

    def parse_assignment_target(self):
        if self.current_token.type == TokenType.IDENTIFIER:
            token = self.current_token
            self.eat(TokenType.IDENTIFIER)
            target = Var(token)
            while self.current_token.type == TokenType.DAFTAR_AWAL:
                self.eat(TokenType.DAFTAR_AWAL)
                index = self.expr()
                self.eat(TokenType.DAFTAR_AKHIR)
                target = IndexAccess(target, index, token)
            return target
        elif self.current_token.type == TokenType.SELF:
            token = self.current_token
            self.eat(TokenType.SELF)
            target = SelfVar(token.value, token)
            while self.current_token.type == TokenType.DAFTAR_AWAL:
                self.eat(TokenType.DAFTAR_AWAL)
                index = self.expr()
                self.eat(TokenType.DAFTAR_AKHIR)
                target = IndexAccess(target, index, token)
            return target
        else:
            self.error(
                f"Diharapkan identifier untuk assignment target, ditemukan '{self.current_token.type}'"  # noqa: E501
            )

    def _parse_python_function_reference(self):
        token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        node = Var(token)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            attr_token = self.current_token
            attr_name = self.current_token.value
            self.current_token = self.lexer.get_next_token()
            node = AttributeRef(node, attr_name, attr_token)
        return node

    def python_call_expression(self):
        token = self.current_token
        self.eat(TokenType.PANGGIL_PYTHON)
        func_expr = self._parse_python_function_reference()
        args = []
        kwargs = {}
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            args, kwargs = self.parse_arguments()
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.KURUNG_AKHIR)
        return PythonCall(func_expr, args, token, kwargs)
