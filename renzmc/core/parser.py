"""
RenzmcLang Parser Module

This module implements the parser for RenzmcLang, converting tokens
into an Abstract Syntax Tree (AST).
"""

from renzmc.core.token import TokenType, Token
from renzmc.core.parser_type_helpers import parse_type_hint_advanced
from renzmc.core.ast import (
    PropertyDecl,
    StaticMethodDecl,
    ClassMethodDecl,
    ExtendedUnpacking,
    StarredExpr,
    SliceAssign,
    AST,
    Program,
    Block,
    BinOp,
    UnaryOp,
    Num,
    String,
    Boolean,
    NoneValue,
    List,
    Dict,
    Set,
    Tuple,
    DictComp,
    Var,
    VarDecl,
    Assign,
    MultiVarDecl,
    MultiAssign,
    NoOp,
    Print,
    Input,
    If,
    While,
    For,
    ForEach,
    Break,
    Continue,
    FuncDecl,
    FuncCall,
    Return,
    ClassDecl,
    MethodDecl,
    Constructor,
    AttributeRef,
    MethodCall,
    Import,
    PythonImport,
    PythonCall,
    TryCatch,
    Raise,
    IndexAccess,
    SliceAccess,
    SelfVar,
    Lambda,
    ListComp,
    SetComp,
    Generator,
    Yield,
    YieldFrom,
    Decorator,
    AsyncFuncDecl,
    AsyncMethodDecl,
    Await,
    TypeHint,
    FormatString,
    Ternary,
    Unpacking,
    WalrusOperator,
    CompoundAssign,
    Switch,
    Case,
    With,
    TypeAlias,
    LiteralType,
    TypedDictType,
)
from renzmc.core.error import ParserError, LexerError
from renzmc.core.lexer import Lexer


class Parser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self._in_comprehension = False

    def error(self, message):
        line = self.current_token.line if hasattr(self.current_token, "line") else None
        column = (
            self.current_token.column if hasattr(self.current_token, "column") else None
        )
        raise ParserError(message, line, column)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            # Check if we're expecting ITU but got a keyword token (common when using reserved word as variable)
            if token_type == TokenType.ITU and self.current_token.type in [
                TokenType.SELESAI, TokenType.JIKA, TokenType.SELAMA, TokenType.UNTUK,
                TokenType.FUNGSI, TokenType.KELAS, TokenType.HASIL, TokenType.BERHENTI,
                TokenType.LANJUT, TokenType.COBA, TokenType.TANGKAP, TokenType.AKHIRNYA
            ]:
                # Get the actual keyword text from lexer
                keyword_text = self.current_token.value if hasattr(self.current_token, 'value') else str(self.current_token.type)
                self.error(
                    f"Kesalahan sintaks: Kata kunci '{keyword_text}' tidak dapat digunakan sebagai nama variabel. "
                    f"Kata kunci ini adalah reserved keyword dalam RenzmcLang. "
                    f"Gunakan nama variabel yang berbeda (contoh: '{keyword_text}_value', '{keyword_text}_data', dll)."
                )
            else:
                self.error(
                    f"Kesalahan sintaks: Diharapkan '{token_type}', tetapi ditemukan '{self.current_token.type}'"
                )

    def parse(self):
        node = self.program()
        if self.current_token.type != TokenType.EOF:
            self.error(
                f"Kesalahan sintaks: Token tidak terduga '{self.current_token.type}'"
            )
        return node

    def program(self):
        statements = self.statement_list()
        return Program(statements)

    def statement_list(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
        return statements

    def statement(self):
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
                "Kata kunci 'akhir' atau 'selesai' tidak dapat digunakan sebagai nama variabel. "
                "Ini adalah reserved keyword dalam RenzmcLang. "
                "Gunakan nama yang berbeda seperti: 'akhir_waktu', 'waktu_akhir', 'end_time', 'akhir_data', dll."
            )
        elif self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
            return None
        else:
            if self.current_token.type != TokenType.EOF:
                # Check if it's a reserved keyword being used incorrectly
                reserved_keywords = {
                    TokenType.SELESAI: 'selesai/akhir',
                    TokenType.JIKA: 'jika',
                    TokenType.SELAMA: 'selama',
                    TokenType.UNTUK: 'untuk',
                    TokenType.FUNGSI: 'fungsi',
                    TokenType.KELAS: 'kelas',
                    TokenType.HASIL: 'hasil',
                    TokenType.BERHENTI: 'berhenti',
                    TokenType.LANJUT: 'lanjut',
                    TokenType.COBA: 'coba',
                    TokenType.TANGKAP: 'tangkap',
                    TokenType.AKHIRNYA: 'akhirnya',
                    TokenType.DAN: 'dan',
                    TokenType.ATAU: 'atau',
                    TokenType.TIDAK: 'tidak',
                    TokenType.DALAM: 'dalam',
                    TokenType.DARI: 'dari',
                    TokenType.SAMPAI: 'sampai',
                }
                
                if self.current_token.type in reserved_keywords:
                    keyword = reserved_keywords[self.current_token.type]
                    self.error(
                        f"Kata kunci '{keyword}' tidak dapat digunakan sebagai nama variabel. "
                        f"Ini adalah reserved keyword dalam RenzmcLang. "
                        f"Gunakan nama yang berbeda (contoh: '{keyword}_value', '{keyword}_data', 'my_{keyword}', dll)."
                    )
                else:
                    self.error(f"Token tidak dikenal: '{self.current_token.type}'")
            return self.empty()

    def variable_declaration(self):
        var_info = []
        first_var = self.current_token.value
        token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        first_type = None
        if self.current_token.type == TokenType.TITIK_DUA:
            self.eat(TokenType.TITIK_DUA)
            first_type = parse_type_hint_advanced(self)
        var_info.append((first_var, first_type))
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            var_type = None
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
                var_type = parse_type_hint_advanced(self)
            var_info.append((var_name, var_type))
        self.eat(TokenType.ITU)
        if len(var_info) == 1 and self.current_token.type == TokenType.LAMBDA:
            value = self.lambda_expr()
            return VarDecl(var_info[0][0], value, token, var_info[0][1])
        values = []
        values.append(self.expr())
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)
            values.append(self.expr())
        if len(var_info) == 1 and len(values) == 1:
            return VarDecl(var_info[0][0], values[0], token, var_info[0][1])
        else:
            if len(values) > 1:
                values_expr = Tuple(values, token)
            else:
                values_expr = values[0]
            var_names = [info[0] for info in var_info]
            type_hints = {info[0]: info[1] for info in var_info if info[1] is not None}
            return MultiVarDecl(var_names, values_expr, token, type_hints)

    def buat_sebagai_declaration(self):
        token = self.current_token
        self.eat(TokenType.BUAT)
        var_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.SEBAGAI)
        value = self.expr()
        return VarDecl(var_name, value, token, None)

    def lambda_expr(self):
        token = self.current_token
        self.eat(TokenType.LAMBDA)

        params = []

        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            param_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            params.append(param_name)
            self.eat(TokenType.ARROW)
        else:
            param_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            params.append(param_name)
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
            self.eat(TokenType.TITIK_DUA)

        body = self.expr()
        return Lambda(params, body, token)

    def print_statement(self):
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
                # Check if we've reached the end
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    # Check if this is actually someone trying to use 'akhir' as a variable
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
                # Check if we've reached the end
                if self.current_token.type == TokenType.EOF:
                    break
                if self.current_token.type == TokenType.SELESAI:
                    # Check if this is actually someone trying to use 'akhir' as a variable
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

    def function_declaration(self):
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.FUNGSI)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        params = []
        param_types = {}
        return_type = None  # Initialize to avoid UnboundLocal error
        if self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type in (TokenType.IDENTIFIER, TokenType.SELF):
                param_name = self.current_token.value
                params.append(param_name)
                if self.current_token.type == TokenType.SELF:
                    self.eat(TokenType.SELF)
                else:
                    self.eat(TokenType.IDENTIFIER)
                if self.current_token.type == TokenType.TITIK_DUA:
                    self.eat(TokenType.TITIK_DUA)
                    # # type_name = self.current_token.value  # Unused variable  # Unused variable
                    param_types[param_name] = parse_type_hint_advanced(self)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    params.append(param_name)
                    if self.current_token.type == TokenType.SELF:
                        self.eat(TokenType.SELF)
                    else:
                        self.eat(TokenType.IDENTIFIER)
                    if self.current_token.type == TokenType.TITIK_DUA:
                        self.eat(TokenType.TITIK_DUA)
                        # # type_name = self.current_token.value  # Unused variable  # Unused variable
                        param_types[param_name] = parse_type_hint_advanced(self)
            self.eat(TokenType.KURUNG_AKHIR)
            return_type = None
            if self.current_token.type == TokenType.ARROW:
                self.eat(TokenType.ARROW)
                return_type = parse_type_hint_advanced(self)
            self.eat(TokenType.TITIK_DUA)
        elif self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
            return_type = None
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            stmt = self.statement()
            if stmt is not None:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return FuncDecl(name, params, body, token, return_type, param_types)

    def async_function_declaration(self):
        token = self.current_token
        self.eat(TokenType.ASYNC)
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.FUNGSI)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.KURUNG_AWAL)
        params = []
        param_types = {}
        if self.current_token.type in (TokenType.IDENTIFIER, TokenType.SELF):
            param_name = self.current_token.value
            params.append(param_name)
            if self.current_token.type == TokenType.SELF:
                self.eat(TokenType.SELF)
            else:
                self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.TITIK_DUA:
                self.eat(TokenType.TITIK_DUA)
                # # type_name = self.current_token.value  # Unused variable  # Unused variable
                param_types[param_name] = parse_type_hint_advanced(self)
            while self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                param_name = self.current_token.value
                params.append(param_name)
                if self.current_token.type == TokenType.SELF:
                    self.eat(TokenType.SELF)
                else:
                    self.eat(TokenType.IDENTIFIER)
                if self.current_token.type == TokenType.TITIK_DUA:
                    self.eat(TokenType.TITIK_DUA)
                    # # type_name = self.current_token.value  # Unused variable  # Unused variable
                    param_types[param_name] = parse_type_hint_advanced(self)
        self.eat(TokenType.KURUNG_AKHIR)
        return_type = None
        if self.current_token.type == TokenType.ARROW:
            self.eat(TokenType.ARROW)
            return_type = parse_type_hint_advanced(self)
        self.eat(TokenType.TITIK_DUA)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            stmt = self.statement()
            if stmt is not None:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return AsyncFuncDecl(name, params, body, token, return_type, param_types)

    def function_call(self):
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
                    f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'"
                )
            args = []
            kwargs = {}
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
            elif self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args, kwargs = self.parse_arguments_with_separator(
                        TokenType.NEWLINE
                    )
            return MethodCall(
                Var(Token(TokenType.IDENTIFIER, name)), method_name, args, token, kwargs
            )
        else:
            args = []
            kwargs = {}
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
            elif self.current_token.type == TokenType.DENGAN:
                self.eat(TokenType.DENGAN)
                if self.current_token.type != TokenType.NEWLINE:
                    args, kwargs = self.parse_arguments_with_separator(
                        TokenType.NEWLINE
                    )
            return FuncCall(name, args, token, kwargs)

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

    def parse_block_until(self, stop_tokens):
        statements = []
        while (
            self.current_token.type not in stop_tokens
            and self.current_token.type != TokenType.EOF
        ):
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return statements

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

    def empty(self):
        return NoOp()

    def expr(self):
        return self.ternary()

    def ternary(self):
        node = self.walrus_expr()
        if self.current_token.type == TokenType.JIKA and (not self._in_comprehension):
            if_expr = node
            self.eat(TokenType.JIKA)
            condition = self.walrus_expr()
            if self.current_token.type == TokenType.LAINNYA:
                self.eat(TokenType.LAINNYA)
                else_expr = self.walrus_expr()
                node = Ternary(condition, if_expr, else_expr)
            elif (
                self.current_token.type == TokenType.KALAU
                and self.lexer.peek_token()
                and (self.lexer.peek_token().type == TokenType.TIDAK)
            ):
                self.eat(TokenType.KALAU)
                self.eat(TokenType.TIDAK)
                else_expr = self.walrus_expr()
                node = Ternary(condition, if_expr, else_expr)
            else:
                self.error("Operator ternary tidak lengkap: diharapkan 'kalau tidak' atau 'lainnya'")
        return node

    def walrus_expr(self):
        if (
            self.current_token.type == TokenType.IDENTIFIER
            and self.lexer.peek_token()
            and (self.lexer.peek_token().type == TokenType.WALRUS)
        ):
            var_token = self.current_token
            var_name = var_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.WALRUS)
            value = self.logical_or()
            return WalrusOperator(var_name, value, var_token)
        else:
            return self.logical_or()

    def logical_or(self):
        node = self.logical_and()
        while self.current_token.type == TokenType.ATAU:
            token = self.current_token
            self.eat(TokenType.ATAU)
            node = BinOp(node, token, self.logical_and())
        return node

    def logical_and(self):
        node = self.identity()
        while self.current_token.type == TokenType.DAN:
            token = self.current_token
            self.eat(TokenType.DAN)
            node = BinOp(node, token, self.identity())
        return node

    def identity(self):
        node = self.membership()
        while self.current_token.type in (
            TokenType.ADALAH,
            TokenType.ADALAH_OP,
            TokenType.BUKAN,
        ):
            token = self.current_token
            if token.type == TokenType.ADALAH:
                self.eat(TokenType.ADALAH)
            elif token.type == TokenType.ADALAH_OP:
                self.eat(TokenType.ADALAH_OP)
            elif token.type == TokenType.BUKAN:
                self.eat(TokenType.BUKAN)
            node = BinOp(node, token, self.membership())
        return node

    def membership(self):
        node = self.equality()
        while self.current_token.type in (
            TokenType.DALAM,
            TokenType.DALAM_OP,
            TokenType.TIDAK_DALAM,
        ):
            token = self.current_token
            if token.type == TokenType.DALAM:
                self.eat(TokenType.DALAM)
            elif token.type == TokenType.DALAM_OP:
                self.eat(TokenType.DALAM_OP)
            elif token.type == TokenType.TIDAK_DALAM:
                self.eat(TokenType.TIDAK_DALAM)
            node = BinOp(node, token, self.equality())
        return node

    def equality(self):
        node = self.comparison()
        while self.current_token.type in (TokenType.SAMA_DENGAN, TokenType.TIDAK_SAMA):
            token = self.current_token
            if token.type == TokenType.SAMA_DENGAN:
                self.eat(TokenType.SAMA_DENGAN)
            elif token.type == TokenType.TIDAK_SAMA:
                self.eat(TokenType.TIDAK_SAMA)
            node = BinOp(node, token, self.comparison())
        return node

    def bitwise_or(self):
        node = self.bitwise_xor()
        while self.current_token.type == TokenType.BIT_ATAU:
            token = self.current_token
            self.eat(TokenType.BIT_ATAU)
            node = BinOp(node, token, self.bitwise_xor())
        return node

    def bitwise_xor(self):
        node = self.bitwise_and()
        while self.current_token.type == TokenType.BIT_XOR:
            token = self.current_token
            self.eat(TokenType.BIT_XOR)
            node = BinOp(node, token, self.bitwise_and())
        return node

    def bitwise_and(self):
        node = self.shift()
        while self.current_token.type == TokenType.BIT_DAN:
            token = self.current_token
            self.eat(TokenType.BIT_DAN)
            node = BinOp(node, token, self.shift())
        return node

    def shift(self):
        node = self.addition()
        while self.current_token.type in (TokenType.GESER_KIRI, TokenType.GESER_KANAN):
            token = self.current_token
            if token.type == TokenType.GESER_KIRI:
                self.eat(TokenType.GESER_KIRI)
            elif token.type == TokenType.GESER_KANAN:
                self.eat(TokenType.GESER_KANAN)
            node = BinOp(node, token, self.addition())
        return node

    def comparison(self):
        node = self.bitwise_or()
        while self.current_token.type in (
            TokenType.LEBIH_DARI,
            TokenType.KURANG_DARI,
            TokenType.LEBIH_SAMA,
            TokenType.KURANG_SAMA,
        ):
            token = self.current_token
            if token.type == TokenType.LEBIH_DARI:
                self.eat(TokenType.LEBIH_DARI)
            elif token.type == TokenType.KURANG_DARI:
                self.eat(TokenType.KURANG_DARI)
            elif token.type == TokenType.LEBIH_SAMA:
                self.eat(TokenType.LEBIH_SAMA)
            elif token.type == TokenType.KURANG_SAMA:
                self.eat(TokenType.KURANG_SAMA)
            node = BinOp(node, token, self.bitwise_or())
        return node

    def addition(self):
        node = self.term()
        while self.current_token.type in (TokenType.TAMBAH, TokenType.KURANG):
            token = self.current_token
            if token.type == TokenType.TAMBAH:
                self.eat(TokenType.TAMBAH)
            elif token.type == TokenType.KURANG:
                self.eat(TokenType.KURANG)
            node = BinOp(node, token, self.term())
        return node

    def term(self):
        node = self.unary()
        while self.current_token.type in (
            TokenType.KALI_OP,
            TokenType.BAGI,
            TokenType.SISA_BAGI,
        ):
            token = self.current_token
            if token.type == TokenType.KALI_OP:
                self.eat(TokenType.KALI_OP)
            elif token.type == TokenType.BAGI:
                self.eat(TokenType.BAGI)
            elif token.type == TokenType.SISA_BAGI:
                self.eat(TokenType.SISA_BAGI)
            node = BinOp(node, token, self.unary())
        return node

    def power(self):
        node = self.factor()
        if self.current_token.type == TokenType.PANGKAT:
            token = self.current_token
            self.eat(TokenType.PANGKAT)
            right = self.unary()
            node = BinOp(node, token, right)
        return node

    def unary(self):
        if self.current_token.type in (
            TokenType.TAMBAH,
            TokenType.KURANG,
            TokenType.TIDAK,
            TokenType.BUKAN,
            TokenType.BIT_NOT,
        ):
            token = self.current_token
            if token.type == TokenType.TAMBAH:
                self.eat(TokenType.TAMBAH)
            elif token.type == TokenType.KURANG:
                self.eat(TokenType.KURANG)
            elif token.type == TokenType.TIDAK:
                self.eat(TokenType.TIDAK)
            elif token.type == TokenType.BUKAN:
                self.eat(TokenType.BUKAN)
            elif token.type == TokenType.BIT_NOT:
                self.eat(TokenType.BIT_NOT)
            return UnaryOp(token, self.unary())
        else:
            return self.power()

    def end_of_expression(self):
        return self.current_token.type in (
            TokenType.NEWLINE,
            TokenType.EOF,
            TokenType.KURUNG_AKHIR,
            TokenType.DAFTAR_AKHIR,
            TokenType.KAMUS_AKHIR,
            TokenType.TUPLE_AKHIR,
            TokenType.HIMPUNAN_AKHIR,
            TokenType.KOMA,
            TokenType.TITIK_KOMA,
        )

    def factor(self):
        token = self.current_token
        if self.end_of_expression():
            self.error(
                f"Kesalahan sintaks: Diharapkan ekspresi, ditemukan '{token.type}'"
            )
        primary = None
        if token.type == TokenType.ANGKA:
            self.eat(TokenType.ANGKA)
            primary = Num(token)
        elif token.type == TokenType.TEKS:
            self.eat(TokenType.TEKS)
            primary = String(token)
        elif token.type == TokenType.FORMAT_STRING:
            self.eat(TokenType.FORMAT_STRING)
            parts = self.parse_format_string(token.value)
            primary = FormatString(parts, token)
        elif token.type == TokenType.BOOLEAN:
            self.eat(TokenType.BOOLEAN)
            primary = Boolean(token)
        elif token.type == TokenType.BENAR:
            self.eat(TokenType.BENAR)
            primary = Boolean(token)
        elif token.type == TokenType.SALAH:
            self.eat(TokenType.SALAH)
            primary = Boolean(token)
        elif token.type == TokenType.NONE:
            self.eat(TokenType.NONE)
            primary = NoneValue(token)
        elif token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type == TokenType.BIT_ATAU:
                self.eat(TokenType.BIT_ATAU)
                elements = []
                while self.current_token.type != TokenType.BIT_ATAU:
                    elements.append(self.bitwise_xor())
                    if self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                    elif self.current_token.type == TokenType.BIT_ATAU:
                        break
                    else:
                        self.error(f"Expected ',' or '|' in pipe tuple, got {self.current_token.type}")
                self.eat(TokenType.BIT_ATAU)
                self.eat(TokenType.KURUNG_AKHIR)
                primary = Tuple(elements, token)
            else:
                first_expr = self.expr()
                if self.current_token.type == TokenType.KOMA:
                    elements = [first_expr]
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        elements.append(self.expr())
                    self.eat(TokenType.KURUNG_AKHIR)
                    primary = Tuple(elements, token)
                else:
                    self.eat(TokenType.KURUNG_AKHIR)
                    primary = first_expr
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.KURUNG_AWAL:
                primary = self.parse_function_call(token.value, token)
            else:
                primary = Var(token)
        elif token.type == TokenType.HASIL:
            self.eat(TokenType.HASIL)
            identifier_token = Token(
                TokenType.IDENTIFIER, token.value, token.line, token.column
            )
            primary = Var(identifier_token)
        elif token.type == TokenType.SELF:
            self.eat(TokenType.SELF)
            primary = SelfVar(token.value, token)
        elif token.type == TokenType.AWAIT:
            self.eat(TokenType.AWAIT)
            expr = self.factor()
            primary = Await(expr, token)
        elif token.type == TokenType.PANGGIL:
            primary = self.function_call()
        elif token.type == TokenType.PANGGIL_PYTHON:
            primary = self.python_call_expression()
        elif token.type == TokenType.DAFTAR_AWAL:
            primary = self.list_literal()
        elif token.type == TokenType.KAMUS_AWAL:
            primary = self.dict_literal()
        elif token.type == TokenType.HIMPUNAN_AWAL:
            primary = self.set_literal()
        elif token.type == TokenType.TUPLE_AWAL:
            primary = self.tuple_literal()
        elif token.type == TokenType.AWAIT:
            self.eat(TokenType.AWAIT)
            expr = self.factor()
            primary = Await(expr, token)
        elif token.type == TokenType.LAMBDA:
            primary = self.lambda_expr()
        else:
            self.error(f"Kesalahan sintaks: Token tidak terduga '{token.type}'")
        return self.apply_postfix_operations(primary)

    def parse_format_string(self, text):
        import re

        parts = []
        last_end = 0
        pattern = "\\{([^{}]*)\\}"
        for match in re.finditer(pattern, text):
            if match.start() > last_end:
                parts.append(
                    String(Token(TokenType.TEKS, text[last_end : match.start()]))
                )
            expr_text = match.group(1)
            if expr_text.strip():
                try:
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
                return DictComp(
                    key_expr, value_expr, var_name, iterable, condition, token
                )
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

    def parse_function_call(self, func_name, token):
        self.eat(TokenType.KURUNG_AWAL)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        args, kwargs = self.parse_arguments()
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        self.eat(TokenType.KURUNG_AKHIR)
        return FuncCall(func_name, args, token, kwargs)

    def parse_attribute_access(self, obj_token):
        obj = Var(obj_token)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            attr_name = self.current_token.value
            attr_token = self.current_token
            if self.current_token.type == TokenType.IDENTIFIER:
                self.eat(TokenType.IDENTIFIER)
            elif self.current_token.type in self._get_allowed_attribute_keywords():
                self.advance_token()
            else:
                self.error(
                    f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                )
            if self.current_token.type == TokenType.KURUNG_AWAL:
                self.eat(TokenType.KURUNG_AWAL)
                args = []
                if self.current_token.type != TokenType.KURUNG_AKHIR:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.KOMA:
                        self.eat(TokenType.KOMA)
                        args.append(self.expr())
                self.eat(TokenType.KURUNG_AKHIR)
                obj = MethodCall(obj, attr_name, args, attr_token)
            else:
                obj = AttributeRef(obj, attr_name, attr_token)
        return obj

    def parse_postfix_expression(self, obj_token):
        obj = Var(obj_token)
        while self.current_token.type in (TokenType.TITIK, TokenType.DAFTAR_AWAL):
            if self.current_token.type == TokenType.TITIK:
                self.eat(TokenType.TITIK)
                attr_name = self.current_token.value
                attr_token = self.current_token
                if self.current_token.type == TokenType.IDENTIFIER:
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type in self._get_allowed_attribute_keywords():
                    self.advance_token()
                else:
                    self.error(
                        f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                    )
                if self.current_token.type == TokenType.KURUNG_AWAL:
                    self.eat(TokenType.KURUNG_AWAL)
                    args = []
                    if self.current_token.type != TokenType.KURUNG_AKHIR:
                        args.append(self.expr())
                        while self.current_token.type == TokenType.KOMA:
                            self.eat(TokenType.KOMA)
                            args.append(self.expr())
                    self.eat(TokenType.KURUNG_AKHIR)
                    obj = MethodCall(obj, attr_name, args, attr_token)
                else:
                    obj = AttributeRef(obj, attr_name, attr_token)
            elif self.current_token.type == TokenType.DAFTAR_AWAL:
                index_token = self.current_token
                self.eat(TokenType.DAFTAR_AWAL)
                index_expr = self.expr()
                self.eat(TokenType.DAFTAR_AKHIR)
                obj = IndexAccess(obj, index_expr, index_token)
        return obj

    def apply_postfix_operations(self, primary):
        expr = primary
        while self.current_token.type in (
            TokenType.TITIK,
            TokenType.DAFTAR_AWAL,
            TokenType.KURUNG_AWAL,
        ):
            if self.current_token.type == TokenType.TITIK:
                self.eat(TokenType.TITIK)
                attr_name = self.current_token.value
                attr_token = self.current_token
                if self.current_token.type == TokenType.IDENTIFIER:
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type in self._get_allowed_attribute_keywords():
                    self.advance_token()
                else:
                    self.error(
                        f"Diharapkan nama atribut atau metode, tetapi ditemukan '{self.current_token.type}'"
                    )
                if self.current_token.type == TokenType.KURUNG_AWAL:
                    self.eat(TokenType.KURUNG_AWAL)
                    args, kwargs = self.parse_arguments()
                    self.eat(TokenType.KURUNG_AKHIR)
                    expr = MethodCall(expr, attr_name, args, attr_token, kwargs)
                else:
                    expr = AttributeRef(expr, attr_name, attr_token)
            elif self.current_token.type == TokenType.DAFTAR_AWAL:
                index_token = self.current_token
                self.eat(TokenType.DAFTAR_AWAL)
                index_expr = self.expr()
                self.eat(TokenType.DAFTAR_AKHIR)
                expr = IndexAccess(expr, index_expr, index_token)
            elif self.current_token.type == TokenType.KURUNG_AWAL:
                call_token = self.current_token
                self.eat(TokenType.KURUNG_AWAL)
                args, kwargs = self.parse_arguments()
                self.eat(TokenType.KURUNG_AKHIR)
                expr = MethodCall(expr, "", args, call_token, kwargs)
        return expr

    def parse_arguments(self):
        positional_args = []
        keyword_args = {}
        seen_keyword = False
        if self.current_token.type == TokenType.KURUNG_AKHIR:
            return (positional_args, keyword_args)
        while True:
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

            if self.current_token.type == TokenType.KURUNG_AKHIR:
                break

            if self.current_token.type == TokenType.IDENTIFIER:
                next_token = self.lexer.peek_token()
                is_keyword_arg = next_token and next_token.type == TokenType.ASSIGNMENT
                if is_keyword_arg:
                    seen_keyword = True
                    arg_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    self.eat(TokenType.ASSIGNMENT)
                    arg_value = self.expr()
                    keyword_args[arg_name] = arg_value
                else:
                    if seen_keyword:
                        self.error(
                            "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"
                        )
                    positional_args.append(self.expr())
            else:
                if seen_keyword:
                    self.error(
                        "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"
                    )
                positional_args.append(self.expr())

            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)

            if self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                if self.current_token.type == TokenType.KURUNG_AKHIR:
                    break
            else:
                break
        return (positional_args, keyword_args)

    def parse_arguments_with_separator(self, separator_token):
        positional_args = []
        keyword_args = {}
        seen_keyword = False
        while (
            self.current_token.type != separator_token
            and self.current_token.type != TokenType.EOF
        ):
            if self.current_token.type == TokenType.IDENTIFIER:
                next_token = self.lexer.peek_token()
                is_keyword_arg = next_token and next_token.type == TokenType.ASSIGNMENT
                if is_keyword_arg:
                    seen_keyword = True
                    arg_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    self.eat(TokenType.ASSIGNMENT)
                    arg_value = self.expr()
                    keyword_args[arg_name] = arg_value
                else:
                    if seen_keyword:
                        self.error(
                            "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"
                        )
                    positional_args.append(self.expr())
            else:
                if seen_keyword:
                    self.error(
                        "Kesalahan sintaks: Argumen posisional tidak dapat muncul setelah argumen kata kunci"
                    )
                positional_args.append(self.expr())
            if self.current_token.type == TokenType.KOMA:
                self.eat(TokenType.KOMA)
            else:
                break
        return (positional_args, keyword_args)

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

    def advance_token(self):
        self.current_token = self.lexer.get_next_token()

    def parse_assignment_target(self):
        if self.current_token.type == TokenType.IDENTIFIER:
            token = self.current_token
            self.eat(TokenType.IDENTIFIER)
            target = Var(token)
            while self.current_token.type == TokenType.DAFTAR_AWAL:
                self.eat(TokenType.DAFTAR_AWAL)
                index = self.expr()
                self.eat(TokenType.DAFTAR_AKHIR)
                target = IndexAccess(target, index, token)
            return target
        else:
            self.error(
                f"Diharapkan identifier untuk assignment target, ditemukan '{self.current_token.type}'"
            )

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
                f"Diharapkan 'itu' atau operator assignment gabungan, ditemukan '{self.current_token.type}'"
            )

    def parse_comma_separated_statement(self):
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
                f"Expected 'itu' or '=' after comma-separated identifiers, got {self.current_token.type}"
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

    def compound_assignment_statement(self):
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
                f"Diharapkan operator assignment gabungan, ditemukan '{self.current_token.type}'"
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

    def _parse_python_function_reference(self):
        token = self.current_token
        self.eat(TokenType.IDENTIFIER)
        node = Var(token)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            attr_token = self.current_token
            attr_name = self.current_token.value
            self.current_token = self.lexer.get_next_token()
            node = AttributeRef(node, attr_name, attr_token)
        return node

    def python_call_expression(self):
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
            args, kwargs = self.parse_arguments()
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
            self.eat(TokenType.KURUNG_AKHIR)
        return PythonCall(func_expr, args, token, kwargs)

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

    def class_declaration(self):
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.KELAS)
        class_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        parent = None
        if self.current_token.type == TokenType.WARISI:
            self.eat(TokenType.WARISI)
            parent = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.TITIK_DUA)
        while self.current_token.type == TokenType.NEWLINE:
            self.eat(TokenType.NEWLINE)
        methods = []
        while self.current_token.type not in (TokenType.SELESAI, TokenType.EOF):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            if self.current_token.type == TokenType.AT:
                self.eat(TokenType.AT)
                decorator_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.TITIK:
                    self.eat(TokenType.TITIK)
                    decorator_name += "." + self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.NEWLINE:
                    self.eat(TokenType.NEWLINE)
                if self.current_token.type == TokenType.FUNGSI:
                    method = self.function_declaration()
                    if not hasattr(method, "decorator"):
                        method.decorator = decorator_name
                    methods.append(method)
                else:
                    self.error("Expected function after decorator")
            elif self.current_token.type == TokenType.KONSTRUKTOR:
                methods.append(self.constructor_declaration())
            elif self.current_token.type == TokenType.METODE:
                methods.append(self.method_declaration())
            elif self.current_token.type == TokenType.FUNGSI:
                methods.append(self.function_declaration())
            else:
                stmt = self.statement()
                if stmt:
                    methods.append(stmt)
        self.eat(TokenType.SELESAI)
        return ClassDecl(class_name, methods, parent, token)

    def constructor_declaration(self):
        token = self.current_token
        self.eat(TokenType.KONSTRUKTOR)
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    params.append(param_name)
            self.eat(TokenType.KURUNG_AKHIR)
            self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return Constructor(params, body, token)

    def constructor_declaration_with_buat(self):
        token = self.current_token
        self.eat(TokenType.BUAT)
        self.eat(TokenType.KONSTRUKTOR)
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return Constructor(params, body, token)

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

    def method_declaration(self):
        token = self.current_token
        if self.current_token.type == TokenType.BUAT:
            self.eat(TokenType.BUAT)
        self.eat(TokenType.METODE)
        method_name = self.current_token.value
        if self.current_token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type in self._get_allowed_method_keywords():
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(
                f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'"
            )
        params = []
        if self.current_token.type == TokenType.DENGAN:
            self.eat(TokenType.DENGAN)
            if self.current_token.type == TokenType.IDENTIFIER:
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    params.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type == TokenType.KURUNG_AWAL:
            self.eat(TokenType.KURUNG_AWAL)
            if self.current_token.type != TokenType.KURUNG_AKHIR:
                param_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                params.append(param_name)
                while self.current_token.type == TokenType.KOMA:
                    self.eat(TokenType.KOMA)
                    param_name = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)
                    params.append(param_name)
            self.eat(TokenType.KURUNG_AKHIR)
            self.eat(TokenType.TITIK_DUA)
            while self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
        body = []
        while self.current_token.type not in (
            TokenType.SELESAI,
            TokenType.EOF,
            TokenType.BUAT,
        ):
            if self.current_token.type == TokenType.NEWLINE:
                self.eat(TokenType.NEWLINE)
                continue
            stmt = self.statement()
            if stmt:
                body.append(stmt)
        self.eat(TokenType.SELESAI)
        return MethodDecl(method_name, params, body, token)

    def python_import_statement(self):
        token = self.current_token
        self.eat(TokenType.IMPOR_PYTHON)
        module_name = None
        if self.current_token.type == TokenType.TEKS:
            module_name = self.current_token.value
            self.eat(TokenType.TEKS)
        elif self.current_token.type == TokenType.IDENTIFIER:
            module_parts = [self.current_token.value]
            self.eat(TokenType.IDENTIFIER)
            while self.current_token.type == TokenType.TITIK:
                self.eat(TokenType.TITIK)
                if self.current_token.type == TokenType.IDENTIFIER:
                    module_parts.append(self.current_token.value)
                    self.eat(TokenType.IDENTIFIER)
                else:
                    self.error("Diharapkan identifier setelah titik dalam nama modul")
            module_name = ".".join(module_parts)
        else:
            self.error(
                "Diharapkan nama modul (string atau identifier) setelah 'impor_python'"
            )
        alias = None
        if self.current_token.type == TokenType.SEBAGAI:
            self.eat(TokenType.SEBAGAI)
            alias = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        return PythonImport(module_name, alias, token)

    def import_statement(self):
        token = self.current_token
        self.eat(TokenType.IMPOR)
        module_name = None
        if self.current_token.type == TokenType.TEKS:
            module_name = self.current_token.value
            self.eat(TokenType.TEKS)
        elif self.current_token.type == TokenType.IDENTIFIER:
            module_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        else:
            self.error("Diharapkan nama modul setelah 'impor'")
        alias = None
        if self.current_token.type == TokenType.SEBAGAI:
            self.eat(TokenType.SEBAGAI)
            alias = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        return Import(module_name, alias, token)

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
                self.error(
                    f"Diharapkan nama metode, tetapi ditemukan '{self.current_token.type}'"
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
