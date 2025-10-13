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
RenzmcLang Parser Oop Module

Object-oriented programming parsing methods.
"""

from renzmc.core.ast import (  # noqa: E402
    Assign,
)
from renzmc.core.token import Token, TokenType  # noqa: E402


class OOPParser:
    """
    Object-oriented programming parsing methods.
    """

    def handle_self_attribute(self):
        expr = self.expr()
        if self.current_token.type == TokenType.ASSIGNMENT:
            self.eat(TokenType.ASSIGNMENT)
            value = self.expr()
            return Assign(expr, value, self.current_token)
        elif self.current_token.type == TokenType.ITU:
            self.eat(TokenType.ITU)
            value = self.expr()
            return Assign(expr, value, self.current_token)
        else:
            return expr

    def handle_attribute_or_call(self):
        expr = self.expr()
        if self.current_token.type == TokenType.ASSIGNMENT:
            self.eat(TokenType.ASSIGNMENT)
            value = self.expr()
            return Assign(expr, value, self.current_token)
        elif self.current_token.type == TokenType.ITU:
            self.eat(TokenType.ITU)
            value = self.expr()
            return Assign(expr, value, self.current_token)
        else:
            return expr

    def _get_allowed_method_keywords(self):
        return {
            TokenType.KALI,
            TokenType.TAMBAH,
            TokenType.KURANG,
            TokenType.BAGI,
            TokenType.HASIL,
            TokenType.TULIS,
            TokenType.TANYA,
            TokenType.DARI,
            TokenType.KE,
            TokenType.DALAM,
        }

    def _get_allowed_attribute_keywords(self):
        excluded_tokens = {
            TokenType.KURUNG_AWAL,
            TokenType.KURUNG_AKHIR,
            TokenType.DAFTAR_AWAL,
            TokenType.DAFTAR_AKHIR,
            TokenType.KAMUS_AWAL,
            TokenType.KAMUS_AKHIR,
            TokenType.TITIK_KOMA,
            TokenType.KOMA,
            TokenType.NEWLINE,
            TokenType.EOF,
            TokenType.ANGKA,
            TokenType.TEKS,
            TokenType.TITIK,
        }
        all_token_types = set(TokenType)
        allowed_tokens = all_token_types - excluded_tokens
        return allowed_tokens
