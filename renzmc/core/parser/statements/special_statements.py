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
RenzmcLang Parser Special Statements Module

Special statement parsing methods (print, with, decorator, type_alias).
"""

from renzmc.core.ast import Decorator, Print, Tuple, TypeAlias, With  # noqa: E402
from renzmc.core.parser_type_helpers import parse_type_hint_advanced  # noqa: E402
from renzmc.core.token import TokenType  # noqa: E402


class SpecialStatements:
    """
    Special statement parsing methods.
    """

    def print_statement(self):  # noqa: C901
        token = self.current_token
        self.eat(TokenType.TAMPILKAN)

        has_parentheses = False
        if self.current_token.type == TokenType.KURUNG_AWAL:
            has_parentheses = True
            self.eat(TokenType.KURUNG_AWAL)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

        exprs = [self.expr()]

        if has_parentheses:
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            if has_parentheses:
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
            exprs.append(self.expr())
            if has_parentheses:
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)

        if has_parentheses:
            self.eat(TokenType.KURUNG_AKHIR)

        if len(exprs) == 1:
            return Print(exprs[0], token)
        else:
            return Print(Tuple(exprs, token), token)

    def with_statement(self):
        token = self.current_token
        self.eat(TokenType.DENGAN)
        context_expr = self.expr()
        var_name = None
        if self.current_token.type == TokenType.SEBAGAI:
            self.eat(TokenType.SEBAGAI)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        body = self.parse_block_until([TokenType.SELESAI])
        self.eat(TokenType.SELESAI)
        return With(context_expr, var_name, body, token)

    def type_alias_statement(self):
        token = self.current_token
        self.eat(TokenType.TIPE)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.ASSIGNMENT)
        type_expr = parse_type_hint_advanced(self)
        return TypeAlias(name, type_expr, token)

    def decorator_statement(self):
        decorator_token = self.current_token
        self.eat(TokenType.AT)
        decorator_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            decorator_name += "." + self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        decorator_args = []
        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                decorator_args.append(self.expr())
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    decorator_args.append(self.expr())
            self.eat(TokenType.KURUNG_AKHIR)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        decorated = None
        if self.current_token.type == TokenType.BUAT:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.FUNGSI:
                decorated = self.function_declaration()
            elif next_token is not None and next_token.type == TokenType.KELAS:
                decorated = self.class_declaration()
            else:
                self.error("Dekorator hanya dapat diterapkan pada fungsi atau kelas")
        elif self.current_token.type == TokenType.ASYNC:
            decorated = self.async_function_declaration()
        else:
            self.error("Dekorator hanya dapat diterapkan pada fungsi atau kelas")
        return Decorator(decorator_name, decorator_args, decorated, decorator_token)
