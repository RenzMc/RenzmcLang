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
    Break,
    Continue,
    Return,
    Tuple,
    Yield,
    YieldFrom,
)
from renzmc.core.token import TokenType


class FlowControlStatements:
    """
    Flow control statement parsing methods.
    """

    def return_statement(self):
        token = self.current_token
        self.eat(TokenType.HASIL)
        expr = None
        if self.current_token.type != TokenType.NEWLINE:
            exprs = [self.expr()]
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                exprs.append(self.expr())
            if len(exprs) == 1:
                expr = exprs[0]
            else:
                expr = Tuple(exprs, token)
        return Return(expr, token)

    def yield_statement(self):
        token = self.current_token
        self.eat(TokenType.YIELD)
        expr = None
        if self.current_token.type not in (TokenType.NEWLINE, TokenType.EOF):
            expr = self.expr()
        return Yield(expr, token)

    def yield_from_statement(self):
        token = self.current_token
        if self.current_token.type == TokenType.YIELD_FROM:
            self.eat(TokenType.YIELD_FROM)
        else:
            self.eat(TokenType.YIELD)
            if self.current_token.type == TokenType.DARI:
                self.eat(TokenType.DARI)
            else:
                self.error("Expected 'dari' after 'hasil_bertahap'")
        expr = self.expr()
        return YieldFrom(expr, token)

    def break_statement(self):
        token = self.current_token
        self.eat(TokenType.BERHENTI)
        return Break(token)

    def continue_statement(self):
        token = self.current_token
        self.eat(TokenType.LANJUT)
        return Continue(token)
