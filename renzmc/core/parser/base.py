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
RenzmcLang Parser Base Module

This module contains the base Parser class with core functionality.
"""

from renzmc.core.ast import Program  # noqa: E402
from renzmc.core.error import ParserError  # noqa: E402
from renzmc.core.token import TokenType  # noqa: E402


class ParserBase:
    """
    Base parser class containing core parsing functionality.

    This class provides the fundamental methods for parsing including
    initialization, error handling, token consumption, and program structure.
    """

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self._in_comprehension = False

    def error(self, message):
        line = self.current_token.line if hasattr(self.current_token, "line") else None
        column = (
            self.current_token.column if hasattr(self.current_token, "column") else None
        )
        raise ParserError(message, line, column)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            # Check if we're expecting ITU but got a keyword token (common when using reserved word as variable)  # noqa: E501
            if token_type == TokenType.ITU and self.current_token.type in [
                TokenType.SELESAI,
                TokenType.JIKA,
                TokenType.SELAMA,
                TokenType.UNTUK,
                TokenType.FUNGSI,
                TokenType.KELAS,
                TokenType.HASIL,
                TokenType.BERHENTI,
                TokenType.LANJUT,
                TokenType.COBA,
                TokenType.TANGKAP,
                TokenType.AKHIRNYA,
            ]:
                # Get the actual keyword text from lexer
                keyword_text = (
                    self.current_token.value
                    if hasattr(self.current_token, "value")
                    else str(self.current_token.type)
                )
                self.error(
                    f"Kesalahan sintaks: Kata kunci '{keyword_text}' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                    f"Kata kunci ini adalah reserved keyword dalam RenzmcLang. "
                    f"Gunakan nama variabel yang berbeda (contoh: '{keyword_text}_value', '{keyword_text}_data', dll)."  # noqa: E501
                )
            else:
                self.error(
                    f"Kesalahan sintaks: Diharapkan '{token_type}', tetapi ditemukan '{self.current_token.type}'"  # noqa: E501
                )

    def parse(self):
        node = self.program()
        if self.current_token.type != TokenType.EOF:
            self.error(
                f"Kesalahan sintaks: Token tidak terduga '{self.current_token.type}'"
            )
        return node

    def program(self):
        statements = self.statement_list()
        return Program(statements)

    def statement_list(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
        return statements

    def advance_token(self):
        self.current_token = self.lexer.get_next_token()
