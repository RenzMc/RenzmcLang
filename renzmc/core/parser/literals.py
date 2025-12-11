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
    Dict,
    DictComp,
    List,
    ListComp,
    Set,
    String,
    Tuple,
)
from renzmc.core.error import LexerError, ParserError
from renzmc.core.lexer import Lexer
from renzmc.core.token import Token, TokenType


class LiteralParser:
    """
    Literal parsing methods for data structures.
    """

    def parse_format_string(self, text):
        import re

        parts = []
        last_end = 0
        pattern = "\\{([^{}]*)\\}"
        for match in re.finditer(pattern, text):
            if match.start() > last_end:
                parts.append(String(Token(TokenType.TEKS, text[last_end : match.start()])))
            expr_text = match.group(1)
            if expr_text.strip():
                try:
                    from renzmc.core.parser import Parser

                    expr_lexer = Lexer(expr_text)
                    expr_parser = Parser(expr_lexer)
                    expr_ast = expr_parser.expr()
                    parts.append(expr_ast)
                except (LexerError, ParserError) as e:
                    from renzmc.utils.logging import logger

                    logger.debug(f"F-string expression parsing failed: {e}")
                    parts.append(String(Token(TokenType.TEKS, "{" + expr_text + "}")))
            last_end = match.end()
        if last_end < len(text):
            parts.append(String(Token(TokenType.TEKS, text[last_end:])))
        if not parts:
            parts.append(String(Token(TokenType.TEKS, text)))
        return parts

    def list_literal(self):
        token = self.current_token
        self.eat(TokenType.DAFTAR_AWAL)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        if self.current_token.type == TokenType.DAFTAR_AKHIR:
            self.eat(TokenType.DAFTAR_AKHIR)
            return List([], token)
        expr = self.expr()
        if self.current_token.type == TokenType.UNTUK:
            self.eat(TokenType.UNTUK)
            self.eat(TokenType.SETIAP)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.DARI)
            old_context = self._in_comprehension
            self._in_comprehension = True
            iterable = self.expr()
            condition = None
            if self.current_token.type == TokenType.JIKA:
                self.eat(TokenType.JIKA)
                condition = self.expr()
            self._in_comprehension = old_context
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.DAFTAR_AKHIR)
            return ListComp(expr, var_name, iterable, condition, token)
        else:
            elements = [expr]
            while self.current_token.type in (TokenType.KOMA, TokenType.NEWLINE):
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                if self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    while self.current_token.type == TokenType.NEWLINE:
                        self.eat(TokenType.NEWLINE)
                    if self.current_token.type == TokenType.DAFTAR_AKHIR:
                        break
                    elements.append(self.expr())
                elif self.current_token.type == TokenType.DAFTAR_AKHIR:
                    break
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.DAFTAR_AKHIR)
            return List(elements, token)

    def dict_literal(self):
        token = self.current_token
        self.eat(TokenType.KAMUS_AWAL)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)

        if self.current_token.type == TokenType.BIT_ATAU:
            self.eat(TokenType.BIT_ATAU)
            elements = []
            if self.current_token.type != TokenType.BIT_ATAU:
                elements.append(self.bitwise_xor())
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    while self.current_token.type == TokenType.NEWLINE:
                        self.eat(TokenType.NEWLINE)
                    if self.current_token.type != TokenType.BIT_ATAU:
                        elements.append(self.bitwise_xor())
            self.eat(TokenType.BIT_ATAU)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.KAMUS_AKHIR)
            return Set(elements, token)

        if self.current_token.type == TokenType.KAMUS_AKHIR:
            self.eat(TokenType.KAMUS_AKHIR)
            return Dict([], token)
        key_expr = self.expr()
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
            value_expr = self.expr()
            if self.current_token.type == TokenType.UNTUK:
                self.eat(TokenType.UNTUK)
                self.eat(TokenType.SETIAP)
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.DARI)
                iterable = self.expr()
                condition = None
                if self.current_token.type == TokenType.JIKA:
                    self.eat(TokenType.JIKA)
                    condition = self.expr()
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                self.eat(TokenType.KAMUS_AKHIR)
                return DictComp(key_expr, value_expr, var_name, iterable, condition, token)
            else:
                pairs = [(key_expr, value_expr)]
                while self.current_token.type in (TokenType.KOMA, TokenType.NEWLINE):
                    while self.current_token.type == TokenType.NEWLINE:
                        self.eat(TokenType.NEWLINE)
                    if self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        while self.current_token.type == TokenType.NEWLINE:
                            self.eat(TokenType.NEWLINE)
                        if self.current_token.type == TokenType.KAMUS_AKHIR:
                            break
                        key = self.expr()
                        while self.current_token.type == TokenType.NEWLINE:
                            self.eat(TokenType.NEWLINE)
                        self.eat(TokenType.TITIK_DUA)
                        while self.current_token.type == TokenType.NEWLINE:
                            self.eat(TokenType.NEWLINE)
                        value = self.expr()
                        pairs.append((key, value))
                    elif self.current_token.type == TokenType.KAMUS_AKHIR:
                        break
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                self.eat(TokenType.KAMUS_AKHIR)
                return Dict(pairs, token)
        else:
            self.error("Diharapkan ':' setelah kunci dalam kamus")

    def set_literal(self):
        token = self.current_token
        self.eat(TokenType.HIMPUNAN_AWAL)
        elements = []
        if self.current_token.type != TokenType.HIMPUNAN_AKHIR:
            elements.append(self.expr())
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                elements.append(self.expr())
        self.eat(TokenType.HIMPUNAN_AKHIR)
        return Set(elements, token)

    def tuple_literal(self):
        token = self.current_token
        self.eat(TokenType.TUPLE_AWAL)
        elements = []
        if self.current_token.type != TokenType.TUPLE_AKHIR:
            elements.append(self.expr())
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                elements.append(self.expr())
        self.eat(TokenType.TUPLE_AKHIR)
        return Tuple(elements, token)
