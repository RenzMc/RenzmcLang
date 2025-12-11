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
    FuncCall,
    MethodCall,
    PythonCall,
    Var,
)
from renzmc.core.token import Token, TokenType


class CallStatements:
    """
    Call statement parsing methods.
    """

    def python_call_statement(self):
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
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                args, kwargs = self.parse_arguments()
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.KURUNG_AKHIR)
        return PythonCall(func_expr, args, token, kwargs)

    def call_statement(self):
        token = self.current_token
        self.eat(TokenType.PANGGIL)
        name_token = self.current_token
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
        else:
            self.error(
                "Diharapkan nama fungsi atau metode, tetapi ditemukan '{}'".format(
                    self.current_token.type
                )
            )
        func_expr = Var(name_token)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            attr_name = self.current_token.value
            if self.current_token.type == TokenType.IDENTIFIER:
                self.eat(TokenType.IDENTIFIER)
            elif self.current_token.type in self._get_allowed_attribute_keywords():
                self.advance_token()
            else:
                self.error(
                    f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                )
            func_expr = AttributeRef(func_expr, attr_name, self.current_token)
        args = []
        kwargs = {}
        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                args, kwargs = self.parse_arguments()
            self.eat(TokenType.KURUNG_AKHIR)
        elif self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type not in (TokenType.NEWLINE, TokenType.EOF):
                args, kwargs = self.parse_arguments_with_separator(TokenType.NEWLINE)
        return FuncCall(func_expr, args, token, kwargs)

    def _old_call_statement(self):
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
                self.error(f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'")
            args = []
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        args.append(self.expr())
                self.eat(TokenType.KURUNG_AKHIR)
            elif self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        args.append(self.expr())
            return MethodCall(Var(Token(TokenType.IDENTIFIER, name)), method_name, args, token)
        else:
            args = []
            if self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        args.append(self.expr())
            return FuncCall(name, args, token, {})
