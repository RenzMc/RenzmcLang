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

from renzmc.core.token import Token, TokenType
from renzmc.utils.logging import logger


class LexerHelpers:

    @staticmethod
    def is_comment_start(current_char: str, next_char: str) -> bool:
        return (
            current_char == "/"
            and next_char in ("/", "*")
            or (current_char == "-" and next_char == "-")
            or current_char == "#"
        )

    @staticmethod
    def is_string_start(current_char: str, next_char: str = None) -> bool:
        return current_char in ('"', "'") or (
            current_char == "f" and next_char in ('"', "'")
        )

    @staticmethod
    def is_identifier_start(char: str) -> bool:
        return char.isalpha() or char == "_"

    @staticmethod
    def make_newline_token(line: int, column: int) -> Token:
        return Token(TokenType.NEWLINE, "\n", line, column)

    @staticmethod
    def make_eof_token(line: int, column: int) -> Token:
        return Token(TokenType.EOF, None, line, column)


class OperatorTokenizer:

    def __init__(self, lexer):
        self.lexer = lexer

    def make_plus_token(self) -> Token:
        token = Token(TokenType.TAMBAH, "+", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(TokenType.TAMBAH_SAMA_DENGAN, "+=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_minus_token(self) -> Token:
        token = Token(TokenType.KURANG, "-", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(TokenType.KURANG_SAMA_DENGAN, "-=", token.line, token.column)
            self.lexer.advance()
        elif self.lexer.current_char == ">":
            token = Token(TokenType.ARROW, "->", token.line, token.column)
            self.lexer.advance()
        return token

    def make_multiply_token(self) -> Token:
        token = Token(TokenType.KALI_OP, "*", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "*":
            self.lexer.advance()
            if self.lexer.current_char == "=":
                token = Token(
                    TokenType.PANGKAT_SAMA_DENGAN, "**=", token.line, token.column
                )
                self.lexer.advance()
            else:
                token = Token(TokenType.PANGKAT, "**", token.line, token.column)
        elif self.lexer.current_char == "=":
            token = Token(TokenType.KALI_SAMA_DENGAN, "*=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_divide_token(self) -> Token:
        token = Token(TokenType.BAGI, "/", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "/":
            self.lexer.advance()
            if self.lexer.current_char == "=":
                token = Token(
                    TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN,
                    "//=",
                    token.line,
                    token.column,
                )
                self.lexer.advance()
            else:
                token = Token(TokenType.PEMBAGIAN_BULAT, "//", token.line, token.column)
        elif self.lexer.current_char == "=":
            token = Token(TokenType.BAGI_SAMA_DENGAN, "/=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_modulo_token(self) -> Token:
        token = Token(TokenType.SISA_BAGI, "%", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(TokenType.SISA_SAMA_DENGAN, "%=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_equals_token(self) -> Token:
        token = Token(TokenType.ASSIGNMENT, "=", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(TokenType.SAMA_DENGAN, "==", token.line, token.column)
            self.lexer.advance()
        return token

    def make_not_equals_token(self) -> Token:
        token = Token(TokenType.TIDAK_SAMA, "!=", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        self.lexer.advance()
        return token

    def make_greater_token(self) -> Token:
        token = Token(TokenType.LEBIH_DARI, ">", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == ">":
            self.lexer.advance()
            if self.lexer.current_char == "=":
                token = Token(
                    TokenType.GESER_KANAN_SAMA_DENGAN, ">>=", token.line, token.column
                )
                self.lexer.advance()
            else:
                token = Token(TokenType.GESER_KANAN, ">>", token.line, token.column)
        elif self.lexer.current_char == "=":
            token = Token(TokenType.LEBIH_SAMA, ">=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_less_token(self) -> Token:
        token = Token(TokenType.KURANG_DARI, "<", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "<":
            self.lexer.advance()
            if self.lexer.current_char == "=":
                token = Token(
                    TokenType.GESER_KIRI_SAMA_DENGAN, "<<=", token.line, token.column
                )
                self.lexer.advance()
            else:
                token = Token(TokenType.GESER_KIRI, "<<", token.line, token.column)
        elif self.lexer.current_char == "=":
            token = Token(TokenType.KURANG_SAMA, "<=", token.line, token.column)
            self.lexer.advance()
        return token

    def make_ampersand_token(self) -> Token:
        token = Token(TokenType.BITWISE_AND, "&", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(
                TokenType.BITWISE_AND_SAMA_DENGAN, "&=", token.line, token.column
            )
            self.lexer.advance()
        return token

    def make_pipe_token(self) -> Token:
        token = Token(TokenType.BITWISE_OR, "|", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(
                TokenType.BITWISE_OR_SAMA_DENGAN, "|=", token.line, token.column
            )
            self.lexer.advance()
        return token

    def make_caret_token(self) -> Token:
        token = Token(TokenType.BITWISE_XOR, "^", self.lexer.line, self.lexer.column)
        self.lexer.advance()
        if self.lexer.current_char == "=":
            token = Token(
                TokenType.BITWISE_XOR_SAMA_DENGAN, "^=", token.line, token.column
            )
            self.lexer.advance()
        return token
