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
RenzmcLang Parser Control Flow Statements Module

Control flow statement parsing methods (if, while, for, foreach, switch).
"""

from renzmc.core.ast import Case, For, ForEach, If, Switch, While
from renzmc.core.token import TokenType


class ControlFlowStatements:
    """
    Control flow statement parsing methods.
    """

    def if_statement(self):
        token = self.current_token
        self.eat(TokenType.JIKA)
        condition = self.expr()
        if self.current_token.type == TokenType.MAKA:
            self.eat(TokenType.MAKA)
        if self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        if_body = []
        while self.current_token.type not in (
            TokenType.KALAU,
            TokenType.LAINNYA,
            TokenType.SELESAI,
            TokenType.EOF,
        ):
            stmt = self.statement()
            if stmt is not None:
                if_body.append(stmt)
        else_body = []
        if self.current_token.type == TokenType.LAINNYA:
            self.eat(TokenType.LAINNYA)
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            if self.current_token.type == TokenType.JIKA:
                nested_if = self.if_statement()
                else_body.append(nested_if)
            else:
                while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
                    stmt = self.statement()
                    if stmt is not None:
                        else_body.append(stmt)
        elif (
            self.current_token.type == TokenType.KALAU
            and self.lexer.peek_token()
            and (self.lexer.peek_token().type == TokenType.TIDAK)
        ):
            self.eat(TokenType.KALAU)
            self.eat(TokenType.TIDAK)
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            if self.current_token.type == TokenType.JIKA:
                nested_if = self.if_statement()
                else_body.append(nested_if)
            else:
                while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
                    stmt = self.statement()
                    if stmt is not None:
                        else_body.append(stmt)
        if self.current_token.type == TokenType.SELESAI:
            self.eat(TokenType.SELESAI)
        return If(condition, if_body, else_body, token)

    def while_statement(self):
        token = self.current_token
        self.eat(TokenType.SELAMA)
        condition = self.expr()
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            stmt = self.statement()
            if stmt is not None:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return While(condition, body, token)

    def for_or_foreach_statement(self):
        token = self.current_token
        self.eat(TokenType.UNTUK)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        if self.current_token.type == TokenType.DALAM:
            self.eat(TokenType.DALAM)
            iterable = self.expr()
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            body = []
            while True:
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
                        )
                    break
                stmt = self.statement()
                if stmt is not None:
                    body.append(stmt)
            self.eat(TokenType.SELESAI)
            return ForEach(var_name, iterable, body, token)
        elif self.current_token.type == TokenType.DARI:
            self.eat(TokenType.DARI)
            start_expr = self.expr()
            self.eat(TokenType.SAMPAI)
            end_expr = self.expr()
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            body = []
            while True:
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
                        )
                    break
                stmt = self.statement()
                if stmt is not None:
                    body.append(stmt)
            self.eat(TokenType.SELESAI)
            return For(var_name, start_expr, end_expr, body, token)
        else:
            self.error("Expected 'dalam' or 'dari' after variable in for loop")

    def for_statement(self):
        token = self.current_token
        self.eat(TokenType.UNTUK)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.DARI)
        start = self.expr()
        self.eat(TokenType.SAMPAI)
        end = self.expr()
        body = []
        while True:
            if self.current_token.type == TokenType.EOF:
                break
            if self.current_token.type == TokenType.SELESAI:
                next_token = self.lexer.peek_token()
                if next_token and next_token.type == TokenType.ITU:
                    self.error(
                        "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                        "Ini adalah reserved keyword dalam RenzmcLang. "
                        "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
                    )
                break
            body.append(self.statement())
        self.eat(TokenType.SELESAI)
        return For(var_name, start, end, body, token)

    def foreach_statement(self):
        token = self.current_token
        self.eat(TokenType.UNTUK)
        self.eat(TokenType.SETIAP)

        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            var_names = [self.current_token.value]
            self.eat(TokenType.IDENTIFIER)
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                var_names.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.KURUNG_AKHIR)
            var_name = tuple(var_names)
        else:
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.DARI)
        start_expr = self.expr()
        if self.current_token.type == TokenType.SAMPAI:
            self.eat(TokenType.SAMPAI)
            end_expr = self.expr()
            body = []
            while True:
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
                        )
                    break
                stmt = self.statement()
                if stmt is not None:
                    body.append(stmt)
            self.eat(TokenType.SELESAI)
            return For(var_name, start_expr, end_expr, body, token)
        else:
            iterable = start_expr
            body = []
            while True:
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
                        )
                    break
                stmt = self.statement()
                if stmt is not None:
                    body.append(stmt)
            self.eat(TokenType.SELESAI)
            return ForEach(var_name, iterable, body, token)

    def switch_statement(self):
        token = self.current_token
        self.eat(TokenType.COCOK)
        match_expr = self.expr()
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        cases = []
        default_case = None
        while self.current_token.type not in (
            TokenType.BAWAAN,
            TokenType.SELESAI,
            TokenType.EOF,
        ):
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            if self.current_token.type == TokenType.KASUS:
                self.eat(TokenType.KASUS)
                values = [self.expr()]
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    values.append(self.expr())
                if self.current_token.type == TokenType.TITIK_DUA:
                    self.eat(TokenType.TITIK_DUA)
                case_body = self.parse_block_until([TokenType.KASUS, TokenType.BAWAAN, TokenType.SELESAI])
                cases.append(Case(values, case_body, token))
            else:
                break
        if self.current_token.type == TokenType.BAWAAN:
            self.eat(TokenType.BAWAAN)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            default_case = self.parse_block_until([TokenType.SELESAI])
        self.eat(TokenType.SELESAI)
        return Switch(match_expr, cases, default_case, token)
