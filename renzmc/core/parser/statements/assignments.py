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
RenzmcLang Parser Assignment Statements Module

Assignment statement parsing methods (simple, compound, multi-assign).
"""

from renzmc.core.ast import (  # noqa: E402
    Assign,
    CompoundAssign,
    ExtendedUnpacking,
    IndexAccess,
    MultiAssign,
    MultiVarDecl,
    SelfVar,
    Tuple,
    Var,
    VarDecl,
)
from renzmc.core.token import Token, TokenType  # noqa: E402


class AssignmentStatements:
    """
    Assignment statement parsing methods.
    """

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
