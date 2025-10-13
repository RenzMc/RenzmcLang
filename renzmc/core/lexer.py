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
RenzmcLang Lexer Module

This module implements the lexical analyzer (tokenizer) for RenzmcLang.
It converts source code text into a stream of tokens.
"""

from renzmc.core.error import LexerError  # noqa: E402
from renzmc.core.token import Token, TokenType  # noqa: E402


class Lexer:
    """
    Lexical analyzer for RenzmcLang.

    The Lexer breaks down source code into tokens, handling keywords,
    identifiers, operators, literals, and comments.
    """

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        self.line = 1
        self.column = 1
        self.keywords = {
            "jika": TokenType.JIKA,
            "kalau": TokenType.KALAU,
            "maka": TokenType.MAKA,
            "tidak": TokenType.TIDAK,
            "lainnya": TokenType.LAINNYA,
            "kalau_tidak": TokenType.LAINNYA,
            "selesai": TokenType.SELESAI,
            "akhir": TokenType.SELESAI,
            "selama": TokenType.SELAMA,
            "ulangi": TokenType.ULANGI,
            "kali": TokenType.KALI,
            "untuk": TokenType.UNTUK,
            "setiap": TokenType.SETIAP,
            "dari": TokenType.DARI,
            "sampai": TokenType.SAMPAI,
            "lanjut": TokenType.LANJUT,
            "berhenti": TokenType.BERHENTI,
            "lewati": TokenType.LEWATI,
            "coba": TokenType.COBA,
            "tangkap": TokenType.TANGKAP,
            "akhirnya": TokenType.AKHIRNYA,
            "cocok": TokenType.COCOK,
            "kasus": TokenType.KASUS,
            "bawaan": TokenType.BAWAAN,
            "simpan": TokenType.SIMPAN,
            "ke": TokenType.KE,
            "dalam": TokenType.DALAM,
            "itu": TokenType.ITU,
            "adalah": TokenType.ADALAH,
            "bukan": TokenType.BUKAN,
            "tampilkan": TokenType.TAMPILKAN,
            "tunjukkan": TokenType.TUNJUKKAN,
            "tanya": TokenType.TANYA,
            "buat": TokenType.BUAT,
            "fungsi": TokenType.FUNGSI,
            "dengan": TokenType.DENGAN,
            "parameter": TokenType.PARAMETER,
            "panggil": TokenType.PANGGIL,
            "jalankan": TokenType.JALANKAN,
            "kembali": TokenType.KEMBALI,
            "hasil": TokenType.HASIL,
            "kembalikan": TokenType.HASIL,
            "kelas": TokenType.KELAS,
            "metode": TokenType.METODE,
            "konstruktor": TokenType.KONSTRUKTOR,
            "warisi": TokenType.WARISI,
            "gunakan": TokenType.GUNAKAN,
            "impor": TokenType.IMPOR,
            "impor_python": TokenType.IMPOR_PYTHON,
            "panggil_python": TokenType.PANGGIL_PYTHON,
            "modul": TokenType.MODUL,
            "paket": TokenType.PAKET,
            "lambda": TokenType.LAMBDA,
            "fungsi_cepat": TokenType.LAMBDA,
            "async": TokenType.ASYNC,
            "asinkron": TokenType.ASYNC,
            "await": TokenType.AWAIT,
            "tunggu": TokenType.AWAIT,
            "yield": TokenType.YIELD,
            "hasilkan": TokenType.YIELD,
            "hasil_bertahap": TokenType.YIELD,
            "hasil_dari": TokenType.YIELD_FROM,
            "dekorator": TokenType.DEKORATOR,
            "properti": TokenType.PROPERTI,
            "metode_statis": TokenType.METODE_STATIS,
            "metode_kelas": TokenType.METODE_KELAS,
            "sebagai": TokenType.SEBAGAI,
            "jenis_data": TokenType.JENIS_DATA,
            "tipe": TokenType.TIPE,
            "generator": TokenType.GENERATOR,
            "dan": TokenType.DAN,
            "atau": TokenType.ATAU,
            "benar": TokenType.BENAR,
            "salah": TokenType.SALAH,
            "self": TokenType.SELF,
            "ini": TokenType.SELF,
            "diri": TokenType.SELF,
            "rute": TokenType.ROUTE,
            "get": TokenType.GET,
            "post": TokenType.POST,
            "put": TokenType.PUT,
            "delete": TokenType.DELETE,
            "api": TokenType.API,
            "endpoint": TokenType.ENDPOINT,
            "stream": TokenType.STREAM,
            "aliran": TokenType.STREAM,
            "emit": TokenType.EMIT,
            "pancar": TokenType.EMIT,
            "listen": TokenType.LISTEN,
            "dengar": TokenType.LISTEN,
            "map": TokenType.MAP,
            "peta": TokenType.MAP,
            "filter": TokenType.FILTER,
            "saring": TokenType.FILTER,
            "reduce": TokenType.REDUCE,
            "kurangi": TokenType.REDUCE,
            "error": TokenType.ERROR,
            "kesalahan": TokenType.ERROR,
            "some": TokenType.SOME,
            "none": TokenType.NONE,
            "kosong": TokenType.NONE,
            "simpan_cache": TokenType.CACHE,
            "lazy": TokenType.LAZY,
            "malas": TokenType.LAZY,
        }
        self.comparison_ops = {
            "sama dengan": TokenType.SAMA_DENGAN,
            "tidak sama dengan": TokenType.TIDAK_SAMA,
            "lebih dari": TokenType.LEBIH_DARI,
            "kurang dari": TokenType.KURANG_DARI,
            "lebih dari atau sama dengan": TokenType.LEBIH_SAMA,
            "kurang dari atau sama dengan": TokenType.KURANG_SAMA,
        }

    def error(self, message):
        raise LexerError(message, self.line, self.column)

    def advance(self):
        if self.current_char == "\n":
            self.line += 1
            self.column = 0
        self.pos += 1
        self.column += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self, n=1):
        peek_pos = self.pos + n
        if peek_pos >= len(self.text):
            return None
        else:
            return self.text[peek_pos]

    def peek_token(self):
        current_pos = self.pos
        current_char = self.current_char
        current_line = self.line
        current_column = self.column
        token = self.get_next_token()
        self.pos = current_pos
        self.current_char = current_char
        self.line = current_line
        self.column = current_column
        return token

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == "\n":
                break
            self.advance()

    def skip_comment(self):  # noqa: C901
        if self.current_char == "/" and self.peek() == "/":
            while self.current_char is not None and self.current_char != "\n":
                self.advance()
            if self.current_char == "\n":
                self.advance()
        elif self.current_char == "/" and self.peek() == "*":
            self.advance()
            self.advance()
            while True:
                if self.current_char is None:
                    self.error("Komentar multi-baris tidak ditutup")
                if self.current_char == "*" and self.peek() == "/":
                    self.advance()
                    self.advance()
                    break
                self.advance()
        elif self.current_char == "-" and self.peek() == "-":
            if self.peek(2) == "[":
                self.advance()
                self.advance()
                self.advance()
                while True:
                    if self.current_char is None:
                        self.error("Komentar multi-baris tidak ditutup")
                    if (
                        self.current_char == "]"
                        and self.peek() == "-"
                        and (self.peek(2) == "-")
                    ):
                        self.advance()
                        self.advance()
                        self.advance()
                        break
                    self.advance()
            else:
                while self.current_char is not None and self.current_char != "\n":
                    self.advance()
                if self.current_char == "\n":
                    self.advance()
        elif self.current_char == "#":
            while self.current_char is not None and self.current_char != "\n":
                self.advance()
            if self.current_char == "\n":
                self.advance()

    def number(self):
        result = ""
        start_line = self.line
        start_column = self.column
        while self.current_char is not None and (
            self.current_char.isdigit() or self.current_char == "."
        ):
            result += self.current_char
            self.advance()

        if "." in result:
            return Token(TokenType.ANGKA, float(result), start_line, start_column)
        else:
            return Token(TokenType.ANGKA, int(result), start_line, start_column)

    def string(self):  # noqa: C901
        start_line = self.line
        start_column = self.column
        is_f_string = False

        if self.current_char == "f":
            is_f_string = True
            self.advance()

        quote_type = self.current_char
        self.advance()

        is_triple = False
        if self.current_char == quote_type and self.peek() == quote_type:
            is_triple = True
            self.advance()
            self.advance()

        result = ""

        if is_triple:
            found_closing = False
            while self.current_char is not None:
                if self.current_char == quote_type:
                    if self.peek() == quote_type and self.peek(2) == quote_type:
                        self.advance()
                        self.advance()
                        self.advance()
                        found_closing = True
                        break
                    else:
                        result += self.current_char
                        self.advance()
                else:
                    result += self.current_char
                    self.advance()

            if not found_closing:
                self.error("Triple-quoted string not closed")
        else:
            while self.current_char is not None and self.current_char != quote_type:
                if self.current_char == chr(92):
                    self.advance()
                    if self.current_char == "n":
                        result += chr(10)
                    elif self.current_char == "t":
                        result += chr(9)
                    elif self.current_char == "r":
                        result += chr(13)
                    elif self.current_char == chr(92):
                        result += chr(92)
                    elif self.current_char == quote_type:
                        result += quote_type
                    else:
                        result += chr(92) + self.current_char
                else:
                    result += self.current_char
                self.advance()

            if self.current_char is None:
                self.error("String not closed")

            self.advance()

        if is_f_string:
            return Token(TokenType.FORMAT_STRING, result, start_line, start_column)
        else:
            return Token(TokenType.TEKS, result, start_line, start_column)

    def identifier(self):  # noqa: C901
        result = ""
        start_line = self.line
        start_column = self.column

        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            result += self.current_char
            self.advance()

        if result == "r" and self.current_char in ('"', "'"):
            quote_type = self.current_char
            self.advance()
            raw_result = ""
            while self.current_char is not None and self.current_char != quote_type:
                raw_result += self.current_char
                self.advance()
            if self.current_char is None:
                self.error("Raw string not closed")
            self.advance()
            return Token(TokenType.TEKS, raw_result, start_line, start_column)

        if result == "tidak":
            saved_pos = self.pos
            saved_char = self.current_char
            saved_line = self.line
            saved_column = self.column

            while self.current_char is not None and self.current_char in (" ", "\t"):
                self.advance()

            if self.current_char is not None and self.current_char.isalpha():
                next_word = ""
                while self.current_char is not None and (
                    self.current_char.isalnum() or self.current_char == "_"
                ):
                    next_word += self.current_char
                    self.advance()

                if next_word == "dalam":
                    return Token(
                        TokenType.TIDAK_DALAM, "tidak dalam", start_line, start_column
                    )

            self.pos = saved_pos
            self.current_char = saved_char
            self.line = saved_line
            self.column = saved_column

        if result in self.keywords:
            token_type = self.keywords[result]
            return Token(token_type, result, start_line, start_column)
        else:
            return Token(TokenType.IDENTIFIER, result, start_line, start_column)

    def get_next_token(self):  # noqa: C901
        while self.current_char is not None:
            if self.current_char.isspace() and self.current_char != "\n":
                self.skip_whitespace()
                continue

            if self.current_char == "\n":
                line = self.line
                column = self.column
                self.advance()
                return Token(TokenType.NEWLINE, "\n", line, column)

            if (
                self.current_char == "#"
                or (self.current_char == "/" and self.peek() in ("/", "*"))
                or (self.current_char == "-" and self.peek() == "-")
            ):
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == "f" and self.peek() in ('"', "'"):
                return self.string()

            if self.current_char in ('"', "'"):
                return self.string()

            if self.current_char.isalpha() or self.current_char == "_":
                return self.identifier()

            if self.current_char == "+":
                token = Token(TokenType.TAMBAH, "+", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.TAMBAH_SAMA_DENGAN, "+=", token.line, token.column
                    )
                    self.advance()
                return token

            if self.current_char == "-":
                token = Token(TokenType.KURANG, "-", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.KURANG_SAMA_DENGAN, "-=", token.line, token.column
                    )
                    self.advance()
                elif self.current_char == ">":
                    token = Token(TokenType.ARROW, "->", token.line, token.column)
                    self.advance()
                return token

            if self.current_char == "*":
                token = Token(TokenType.KALI_OP, "*", self.line, self.column)
                self.advance()
                if self.current_char == "*":
                    self.advance()
                    if self.current_char == "=":
                        token = Token(
                            TokenType.PANGKAT_SAMA_DENGAN,
                            "**=",
                            token.line,
                            token.column,
                        )
                        self.advance()
                    else:
                        token = Token(TokenType.PANGKAT, "**", token.line, token.column)
                elif self.current_char == "=":
                    token = Token(
                        TokenType.KALI_SAMA_DENGAN, "*=", token.line, token.column
                    )
                    self.advance()
                return token

            if self.current_char == "/":
                token = Token(TokenType.BAGI, "/", self.line, self.column)
                self.advance()
                if self.current_char == "/":
                    self.advance()
                    if self.current_char == "=":
                        token = Token(
                            TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN,
                            "//=",
                            token.line,
                            token.column,
                        )
                        self.advance()
                    else:
                        token = Token(
                            TokenType.PEMBAGIAN_BULAT, "//", token.line, token.column
                        )
                elif self.current_char == "=":
                    token = Token(
                        TokenType.BAGI_SAMA_DENGAN, "/=", token.line, token.column
                    )
                    self.advance()
                return token

            if self.current_char == "%":
                token = Token(TokenType.SISA_BAGI, "%", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.SISA_SAMA_DENGAN, "%=", token.line, token.column
                    )
                    self.advance()
                return token

            if self.current_char == "=":
                token = Token(TokenType.ASSIGNMENT, "=", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(TokenType.SAMA_DENGAN, "==", token.line, token.column)
                    self.advance()
                return token

            if self.current_char == "!":
                if self.peek() == "=":
                    token = Token(TokenType.TIDAK_SAMA, "!=", self.line, self.column)
                    self.advance()
                    self.advance()
                    return token
                else:
                    token = Token(TokenType.NOT, "!", self.line, self.column)
                    self.advance()
                    return token

            if self.current_char == ">":
                token = Token(TokenType.LEBIH_DARI, ">", self.line, self.column)
                self.advance()
                if self.current_char == ">":
                    self.advance()
                    if self.current_char == "=":
                        token = Token(
                            TokenType.GESER_KANAN_SAMA_DENGAN,
                            ">>=",
                            token.line,
                            token.column,
                        )
                        self.advance()
                    else:
                        token = Token(
                            TokenType.GESER_KANAN, ">>", token.line, token.column
                        )
                elif self.current_char == "=":
                    token = Token(TokenType.LEBIH_SAMA, ">=", token.line, token.column)
                    self.advance()
                return token

            if self.current_char == "<":
                token = Token(TokenType.KURANG_DARI, "<", self.line, self.column)
                self.advance()
                if self.current_char == "<":
                    self.advance()
                    if self.current_char == "=":
                        token = Token(
                            TokenType.GESER_KIRI_SAMA_DENGAN,
                            "<<=",
                            token.line,
                            token.column,
                        )
                        self.advance()
                    else:
                        token = Token(
                            TokenType.GESER_KIRI, "<<", token.line, token.column
                        )
                elif self.current_char == "=":
                    token = Token(TokenType.KURANG_SAMA, "<=", token.line, token.column)
                    self.advance()
                return token

            if self.current_char == "&":
                token = Token(TokenType.BIT_DAN, "&", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.BIT_DAN_SAMA_DENGAN,
                        "&=",
                        token.line,
                        token.column,
                    )
                    self.advance()
                return token

            if self.current_char == "|":
                token = Token(TokenType.BIT_ATAU, "|", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.BIT_ATAU_SAMA_DENGAN, "|=", token.line, token.column
                    )
                    self.advance()
                return token

            if self.current_char == "^":
                token = Token(TokenType.BIT_XOR, "^", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(
                        TokenType.BIT_XOR_SAMA_DENGAN,
                        "^=",
                        token.line,
                        token.column,
                    )
                    self.advance()
                return token

            if self.current_char == "~":
                token = Token(TokenType.BIT_NOT, "~", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "(":
                token = Token(TokenType.KURUNG_AWAL, "(", self.line, self.column)
                self.advance()
                return token

            if self.current_char == ")":
                token = Token(TokenType.KURUNG_AKHIR, ")", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "{":
                token = Token(TokenType.KAMUS_AWAL, "{", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "}":
                token = Token(TokenType.KAMUS_AKHIR, "}", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "[":
                token = Token(TokenType.DAFTAR_AWAL, "[", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "]":
                token = Token(TokenType.DAFTAR_AKHIR, "]", self.line, self.column)
                self.advance()
                return token

            if self.current_char == ",":
                token = Token(TokenType.KOMA, ",", self.line, self.column)
                self.advance()
                return token

            if self.current_char == ".":
                token = Token(TokenType.TITIK, ".", self.line, self.column)
                self.advance()
                return token

            if self.current_char == ":":
                token = Token(TokenType.TITIK_DUA, ":", self.line, self.column)
                self.advance()
                if self.current_char == "=":
                    token = Token(TokenType.WALRUS, ":=", token.line, token.column)
                    self.advance()
                return token

            if self.current_char == ";":
                token = Token(TokenType.SEMICOLON, ";", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "?":
                token = Token(TokenType.TANYA_MARK, "?", self.line, self.column)
                self.advance()
                return token

            if self.current_char == "@":
                token = Token(TokenType.AT, "@", self.line, self.column)
                self.advance()
                return token

            self.error(f"Karakter tidak dikenal: '{self.current_char}'")

        return Token(TokenType.EOF, None, self.line, self.column)
