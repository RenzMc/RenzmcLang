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
RenzmcLang Parser Statement Router Module

Main statement routing logic for dispatching to appropriate parsers.
"""

from renzmc.core.token import Token, TokenType  # noqa: E402


class StatementRouter:
    """
    Main statement routing logic.
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
