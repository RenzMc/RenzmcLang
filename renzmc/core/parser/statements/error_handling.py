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
RenzmcLang Parser Error Handling Statements Module

Error handling statement parsing methods (try-catch).
"""

from renzmc.core.ast import TryCatch
from renzmc.core.token import TokenType


class ErrorHandlingStatements:
    """
    Error handling statement parsing methods.
    """

    def try_catch_statement(self):
        token = self.current_token
        self.eat(TokenType.COBA)
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
        try_block = self.parse_block_until([TokenType.TANGKAP, TokenType.AKHIRNYA, TokenType.SELESAI])
        except_blocks = []
        while self.current_token.type == TokenType.TANGKAP:
            self.eat(TokenType.TANGKAP)
            exception_type = None
            var_name = None
            if self.current_token.type == TokenType.SEBAGAI:
                self.eat(TokenType.SEBAGAI)
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
            elif self.current_token.type == TokenType.IDENTIFIER:
                exception_type = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.TITIK:
                    self.eat(TokenType.TITIK)
                    exception_type += "." + self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                if self.current_token.type == TokenType.SEBAGAI:
                    self.eat(TokenType.SEBAGAI)
                    var_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            except_block = self.parse_block_until([TokenType.TANGKAP, TokenType.AKHIRNYA, TokenType.SELESAI])
            except_blocks.append((exception_type, var_name, except_block))
        finally_block = None
        if self.current_token.type == TokenType.AKHIRNYA:
            self.eat(TokenType.AKHIRNYA)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            finally_block = self.parse_block_until([TokenType.SELESAI])
        self.eat(TokenType.SELESAI)
        return TryCatch(try_block, except_blocks, finally_block, token)
