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
RenzmcLang Parser Statements Module

Statement parsing methods for control flow and assignments.
"""

from renzmc.core.ast import (  # noqa: E402
    Assign,
    AttributeRef,
    Break,
    Case,
    CompoundAssign,
    Continue,
    Decorator,
    ExtendedUnpacking,
    For,
    ForEach,
    FuncCall,
    If,
    IndexAccess,
    MethodCall,
    MultiAssign,
    MultiVarDecl,
    Print,
    PythonCall,
    Return,
    SelfVar,
    Switch,
    TryCatch,
    Tuple,
    TypeAlias,
    Var,
    VarDecl,
    While,
    With,
    Yield,
    YieldFrom,
)
from renzmc.core.token import Token, TokenType  # noqa: E402
from renzmc.core.parser_type_helpers import parse_type_hint_advanced  # noqa: E402


class StatementParser:
    """
    Statement parsing methods for control flow and assignments.
    """

    def statement(self):  # noqa: C901
        if self.current_token.type == TokenType.IDENTIFIER:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.ITU:
                return self.variable_declaration()
            elif next_token is not None and next_token.type == TokenType.TITIK_DUA:
                return self.variable_declaration()
            elif next_token is not None and next_token.type == TokenType.KOMA:
                return self.parse_comma_separated_statement()
            elif next_token is not None and next_token.type == TokenType.ASSIGNMENT:
                return self.simple_assignment_statement()
            elif next_token is not None and next_token.type in (
                TokenType.TAMBAH_SAMA_DENGAN,
                TokenType.KURANG_SAMA_DENGAN,
                TokenType.KALI_SAMA_DENGAN,
                TokenType.BAGI_SAMA_DENGAN,
                TokenType.SISA_SAMA_DENGAN,
                TokenType.PANGKAT_SAMA_DENGAN,
                TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN,
                TokenType.BIT_DAN_SAMA_DENGAN,
                TokenType.BIT_ATAU_SAMA_DENGAN,
                TokenType.BIT_XOR_SAMA_DENGAN,
                TokenType.GESER_KIRI_SAMA_DENGAN,
                TokenType.GESER_KANAN_SAMA_DENGAN,
            ):
                return self.compound_assignment_statement()
            elif next_token is not None and next_token.type == TokenType.DAFTAR_AWAL:
                return self.index_access_statement()
            elif next_token is not None and next_token.type == TokenType.TITIK:
                return self.handle_attribute_or_call()
            else:
                return self.expr()
        elif self.current_token.type == TokenType.SELF:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.TITIK:
                return self.handle_self_attribute()
            elif next_token is not None and next_token.type == TokenType.DAFTAR_AWAL:
                return self.self_index_access_statement()
            else:
                return self.expr()
        elif self.current_token.type == TokenType.TAMPILKAN:
            return self.print_statement()
        elif self.current_token.type == TokenType.JIKA:
            return self.if_statement()
        elif self.current_token.type == TokenType.SELAMA:
            return self.while_statement()
        elif self.current_token.type == TokenType.UNTUK:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.SETIAP:
                return self.foreach_statement()
            else:
                return self.for_or_foreach_statement()
        elif self.current_token.type == TokenType.FUNGSI:
            return self.function_declaration()
        elif self.current_token.type == TokenType.KELAS:
            return self.class_declaration()
        elif self.current_token.type == TokenType.BUAT:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.FUNGSI:
                return self.function_declaration()
            elif next_token is not None and next_token.type == TokenType.KELAS:
                return self.class_declaration()
            elif next_token is not None and next_token.type == TokenType.IDENTIFIER:
                return self.buat_sebagai_declaration()
            else:
                return self.expr()
        elif self.current_token.type == TokenType.ASYNC:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.FUNGSI:
                return self.async_function_declaration()
            elif next_token is not None and next_token.type == TokenType.BUAT:
                return self.async_function_declaration()
            else:
                self.error(
                    "Kata kunci 'asinkron' hanya dapat digunakan untuk deklarasi fungsi"
                )
        elif self.current_token.type == TokenType.HASIL:
            next_token = self.lexer.peek_token()
            if next_token is not None and next_token.type == TokenType.ITU:
                saved_token = self.current_token
                identifier_token = Token(
                    TokenType.IDENTIFIER,
                    saved_token.value,
                    saved_token.line,
                    saved_token.column,
                )
                self.current_token = identifier_token
                return self.variable_declaration()
            else:
                return self.return_statement()
        elif self.current_token.type == TokenType.YIELD:
            next_token = self.lexer.peek_token()
            if next_token and next_token.type == TokenType.DARI:
                return self.yield_from_statement()
            else:
                return self.yield_statement()
        elif self.current_token.type == TokenType.YIELD_FROM:
            return self.yield_from_statement()
        elif self.current_token.type == TokenType.BERHENTI:
            return self.break_statement()
        elif self.current_token.type == TokenType.LANJUT:
            return self.continue_statement()
        elif self.current_token.type == TokenType.SIMPAN:
            return self.assignment_statement()
        elif self.current_token.type == TokenType.DARI:
            return self.from_import_statement()
        elif self.current_token.type == TokenType.IMPOR:
            return self.import_statement()
        elif self.current_token.type == TokenType.IMPOR_PYTHON:
            return self.python_import_statement()
        elif self.current_token.type == TokenType.PANGGIL_PYTHON:
            return self.python_call_statement()
        elif self.current_token.type == TokenType.PANGGIL:
            return self.call_statement()
        elif self.current_token.type == TokenType.COBA:
            return self.try_catch_statement()
        elif self.current_token.type == TokenType.COCOK:
            return self.switch_statement()
        elif self.current_token.type == TokenType.DENGAN:
            return self.with_statement()
        elif self.current_token.type == TokenType.AT:
            return self.decorator_statement()
        elif self.current_token.type == TokenType.TIPE:
            return self.type_alias_statement()
        elif self.current_token.type == TokenType.SELESAI:
            # User might be trying to use 'akhir' or 'selesai' as variable name
            self.error(
                "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                "Ini adalah reserved keyword dalam RenzmcLang. "
                "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
            )
        elif self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
            return None
        else:
            if self.current_token.type != TokenType.EOF:
                # Check if it's a reserved keyword being used incorrectly
                reserved_keywords = {
                    TokenType.SELESAI: "selesai/akhir",
                    TokenType.JIKA: "jika",
                    TokenType.SELAMA: "selama",
                    TokenType.UNTUK: "untuk",
                    TokenType.FUNGSI: "fungsi",
                    TokenType.KELAS: "kelas",
                    TokenType.HASIL: "hasil",
                    TokenType.BERHENTI: "berhenti",
                    TokenType.LANJUT: "lanjut",
                    TokenType.COBA: "coba",
                    TokenType.TANGKAP: "tangkap",
                    TokenType.AKHIRNYA: "akhirnya",
                    TokenType.DAN: "dan",
                    TokenType.ATAU: "atau",
                    TokenType.TIDAK: "tidak",
                    TokenType.DALAM: "dalam",
                    TokenType.DARI: "dari",
                    TokenType.SAMPAI: "sampai",
                }

                if self.current_token.type in reserved_keywords:
                    keyword = reserved_keywords[self.current_token.type]
                    self.error(
                        f"Kata kunci '{keyword}' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                        f"Ini adalah reserved keyword dalam RenzmcLang. "
                        f"Gunakan nama yang berbeda (contoh: '{keyword}_value', '{keyword}_data', 'my_{keyword}', dll)."  # noqa: E501
                    )
                else:
                    self.error(f"Token tidak dikenal: '{self.current_token.type}'")
            return self.empty()

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

    def if_statement(self):  # noqa: C901
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

    def for_or_foreach_statement(self):  # noqa: C901
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
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
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
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
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
                        "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                        "Ini adalah reserved keyword dalam RenzmcLang. "
                        "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
                    )
                break
            body.append(self.statement())
        self.eat(TokenType.SELESAI)
        return For(var_name, start, end, body, token)

    def foreach_statement(self):  # noqa: C901
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
                # Check if we've reached the end
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    # Check if this is actually someone trying to use 'akhir' as a variable  # noqa: E501
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
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
                # Check if we've reached the end
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    # Check if this is actually someone trying to use 'akhir' as a variable  # noqa: E501
                    next_token = self.lexer.peek_token()
                    if next_token and next_token.type == TokenType.ITU:
                        self.error(
                            "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "  # noqa: E501
                            "Ini adalah reserved keyword dalam RenzmcLang. "
                            "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."  # noqa: E501
                        )
                    break
                stmt = self.statement()
                if stmt is not None:
                    body.append(stmt)
            self.eat(TokenType.SELESAI)
            return ForEach(var_name, iterable, body, token)

    def try_catch_statement(self):
        token = self.current_token
        self.eat(TokenType.COBA)
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
        try_block = self.parse_block_until(
            [TokenType.TANGKAP, TokenType.AKHIRNYA, TokenType.SELESAI]
        )
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
            except_block = self.parse_block_until(
                [TokenType.TANGKAP, TokenType.AKHIRNYA, TokenType.SELESAI]
            )
            except_blocks.append((exception_type, var_name, except_block))
        finally_block = None
        if self.current_token.type == TokenType.AKHIRNYA:
            self.eat(TokenType.AKHIRNYA)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
            finally_block = self.parse_block_until([TokenType.SELESAI])
        self.eat(TokenType.SELESAI)
        return TryCatch(try_block, except_blocks, finally_block, token)

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
                case_body = self.parse_block_until(
                    [TokenType.KASUS, TokenType.BAWAAN, TokenType.SELESAI]
                )
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

    def assignment_statement(self):
        token = self.current_token
        self.eat(TokenType.SIMPAN)
        vars_list = []
        first_target = self.parse_assignment_target()
        vars_list.append(first_target)
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            target = self.parse_assignment_target()
            vars_list.append(target)
        self.eat(TokenType.KE)
        values = []
        values.append(self.expr())
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            values.append(self.expr())
        if len(vars_list) == 1 and len(values) == 1:
            return Assign(vars_list[0], values[0], token)
        else:
            if len(values) > 1:
                values_expr = Tuple(values, token)
            else:
                values_expr = values[0]
            return MultiAssign(vars_list, values_expr, token)

    def index_access_statement(self):
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        target = Var(var_token)
        while self.current_token.type == TokenType.DAFTAR_AWAL:
            self.eat(TokenType.DAFTAR_AWAL)
            index = self.expr()
            self.eat(TokenType.DAFTAR_AKHIR)
            target = IndexAccess(target, index, var_token)
        if self.current_token.type == TokenType.ITU:
            self.eat(TokenType.ITU)
            value = self.expr()
            return Assign(target, value, var_token)
        elif self.current_token.type in (
            TokenType.TAMBAH_SAMA_DENGAN,
            TokenType.KURANG_SAMA_DENGAN,
            TokenType.KALI_SAMA_DENGAN,
            TokenType.BAGI_SAMA_DENGAN,
        ):
            op_token = self.current_token
            if self.current_token.type == TokenType.TAMBAH_SAMA_DENGAN:
                self.eat(TokenType.TAMBAH_SAMA_DENGAN)
            elif self.current_token.type == TokenType.KURANG_SAMA_DENGAN:
                self.eat(TokenType.KURANG_SAMA_DENGAN)
            elif self.current_token.type == TokenType.KALI_SAMA_DENGAN:
                self.eat(TokenType.KALI_SAMA_DENGAN)
            elif self.current_token.type == TokenType.BAGI_SAMA_DENGAN:
                self.eat(TokenType.BAGI_SAMA_DENGAN)
            value = self.expr()
            return CompoundAssign(target, op_token, value, var_token)
        else:
            self.error(
                f"Diharapkan 'itu' atau operator assignment gabungan, ditemukan '{self.current_token.type}'"  # noqa: E501
            )

    def self_index_access_statement(self):
        """Handle self[index] = value statements"""
        var_token = self.current_token
        self.eat(TokenType.SELF)
        target = SelfVar(var_token.value, var_token)
        while self.current_token.type == TokenType.DAFTAR_AWAL:
            self.eat(TokenType.DAFTAR_AWAL)
            index = self.expr()
            self.eat(TokenType.DAFTAR_AKHIR)
            target = IndexAccess(target, index, var_token)
        if self.current_token.type == TokenType.ITU:
            self.eat(TokenType.ITU)
            value = self.expr()
            return Assign(target, value, var_token)
        elif self.current_token.type in (
            TokenType.TAMBAH_SAMA_DENGAN,
            TokenType.KURANG_SAMA_DENGAN,
            TokenType.KALI_SAMA_DENGAN,
            TokenType.BAGI_SAMA_DENGAN,
        ):
            op_token = self.current_token
            if self.current_token.type == TokenType.TAMBAH_SAMA_DENGAN:
                self.eat(TokenType.TAMBAH_SAMA_DENGAN)
            elif self.current_token.type == TokenType.KURANG_SAMA_DENGAN:
                self.eat(TokenType.KURANG_SAMA_DENGAN)
            elif self.current_token.type == TokenType.KALI_SAMA_DENGAN:
                self.eat(TokenType.KALI_SAMA_DENGAN)
            elif self.current_token.type == TokenType.BAGI_SAMA_DENGAN:
                self.eat(TokenType.BAGI_SAMA_DENGAN)
            value = self.expr()
            return CompoundAssign(target, op_token, value, var_token)
        else:
            self.error(
                f"Diharapkan 'itu' atau operator assignment gabungan, ditemukan '{self.current_token.type}'"  # noqa: E501
            )

    def parse_comma_separated_statement(self):  # noqa: C901
        start_token = self.current_token
        targets = []
        has_starred = False
        var_name = start_token.value
        self.eat(TokenType.IDENTIFIER)
        targets.append(("normal", var_name))
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            if self.current_token.type == TokenType.KALI_OP:
                self.eat(TokenType.KALI_OP)
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                targets.append(("starred", var_name))
                has_starred = True
            elif self.current_token.type == TokenType.IDENTIFIER:
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                targets.append(("normal", var_name))
            else:
                self.error("Expected identifier or *identifier after comma")
        if self.current_token.type == TokenType.ITU:
            self.eat(TokenType.ITU)
            values = []
            values.append(self.expr())
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                values.append(self.expr())
            if len(targets) == 1 and len(values) == 1:
                return VarDecl(targets[0][1], values[0], start_token)
            else:
                var_names = [t[1] for t in targets]
                value_expr = (
                    Tuple(values, start_token) if len(values) > 1 else values[0]
                )
                return MultiVarDecl(var_names, value_expr, start_token)
        elif self.current_token.type == TokenType.ASSIGNMENT:
            self.eat(TokenType.ASSIGNMENT)
            values = []
            values.append(self.expr())
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                values.append(self.expr())
            if has_starred:
                return ExtendedUnpacking(
                    targets, values[0] if len(values) == 1 else values, start_token
                )
            elif len(targets) == 1 and len(values) == 1:
                return Assign(
                    Var(
                        Token(
                            TokenType.IDENTIFIER,
                            targets[0][1],
                            start_token.line,
                            start_token.column,
                        )
                    ),
                    values[0],
                    start_token,
                )
            else:
                var_nodes = [
                    Var(
                        Token(
                            TokenType.IDENTIFIER,
                            t[1],
                            start_token.line,
                            start_token.column,
                        )
                    )
                    for t in targets
                ]
                value_expr = (
                    Tuple(values, start_token) if len(values) > 1 else values[0]
                )
                return MultiAssign(var_nodes, value_expr, start_token)
        else:
            self.error(
                f"Expected 'itu' or '=' after comma-separated identifiers, got {self.current_token.type}"  # noqa: E501
            )

    def simple_assignment_statement(self):
        token = self.current_token
        targets = []
        if self.current_token.type == TokenType.KALI_OP:
            self.eat(TokenType.KALI_OP)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            targets.append(("starred", var_name))
        else:
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            targets.append(("normal", var_name))
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            if self.current_token.type == TokenType.KALI_OP:
                self.eat(TokenType.KALI_OP)
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                targets.append(("starred", var_name))
            else:
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                targets.append(("normal", var_name))
        self.eat(TokenType.ASSIGNMENT)
        values = []
        values.append(self.expr())
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            values.append(self.expr())
        has_starred = any((t[0] == "starred" for t in targets))
        if has_starred:
            return ExtendedUnpacking(
                targets, values[0] if len(values) == 1 else values, token
            )
        elif len(targets) == 1 and len(values) == 1:
            return Assign(
                Var(
                    Token(TokenType.IDENTIFIER, targets[0][1], token.line, token.column)
                ),
                values[0],
                token,
            )
        else:
            var_nodes = [
                Var(Token(TokenType.IDENTIFIER, t[1], token.line, token.column))
                for t in targets
            ]
            value_expr = Tuple(values, token) if len(values) > 1 else values[0]
            return MultiAssign(var_nodes, value_expr, token)

    def compound_assignment_statement(self):  # noqa: C901
        var_token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        target = Var(var_token)
        while self.current_token.type == TokenType.DAFTAR_AWAL:
            self.eat(TokenType.DAFTAR_AWAL)
            index = self.expr()
            self.eat(TokenType.DAFTAR_AKHIR)
            target = IndexAccess(target, index, var_token)
        op_token = self.current_token
        if self.current_token.type == TokenType.TAMBAH_SAMA_DENGAN:
            self.eat(TokenType.TAMBAH_SAMA_DENGAN)
        elif self.current_token.type == TokenType.KURANG_SAMA_DENGAN:
            self.eat(TokenType.KURANG_SAMA_DENGAN)
        elif self.current_token.type == TokenType.KALI_SAMA_DENGAN:
            self.eat(TokenType.KALI_SAMA_DENGAN)
        elif self.current_token.type == TokenType.BAGI_SAMA_DENGAN:
            self.eat(TokenType.BAGI_SAMA_DENGAN)
        elif self.current_token.type == TokenType.SISA_SAMA_DENGAN:
            self.eat(TokenType.SISA_SAMA_DENGAN)
        elif self.current_token.type == TokenType.PANGKAT_SAMA_DENGAN:
            self.eat(TokenType.PANGKAT_SAMA_DENGAN)
        elif self.current_token.type == TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN:
            self.eat(TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN)
        elif self.current_token.type == TokenType.BIT_DAN_SAMA_DENGAN:
            self.eat(TokenType.BIT_DAN_SAMA_DENGAN)
        elif self.current_token.type == TokenType.BIT_ATAU_SAMA_DENGAN:
            self.eat(TokenType.BIT_ATAU_SAMA_DENGAN)
        elif self.current_token.type == TokenType.BIT_XOR_SAMA_DENGAN:
            self.eat(TokenType.BIT_XOR_SAMA_DENGAN)
        elif self.current_token.type == TokenType.GESER_KIRI_SAMA_DENGAN:
            self.eat(TokenType.GESER_KIRI_SAMA_DENGAN)
        elif self.current_token.type == TokenType.GESER_KANAN_SAMA_DENGAN:
            self.eat(TokenType.GESER_KANAN_SAMA_DENGAN)
        else:
            self.error(
                f"Diharapkan operator assignment gabungan, ditemukan '{self.current_token.type}'"  # noqa: E501
            )
        value = self.expr()
        return CompoundAssign(target, op_token, value, var_token)

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
                    f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"  # noqa: E501
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

    def _old_call_statement(self):  # noqa: C901
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
                self.error(
                    f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'"  # noqa: E501
                )
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
            return MethodCall(
                Var(Token(TokenType.IDENTIFIER, name)), method_name, args, token
            )
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
