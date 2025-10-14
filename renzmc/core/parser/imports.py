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
RenzmcLang Parser Imports Module

Import statement parsing methods.
"""

from renzmc.core.ast import FromImport, Import, PythonImport  # noqa: E402
from renzmc.core.token import TokenType  # noqa: E402


class ImportParser:
    """
    Import statement parsing methods.
    """

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
            self.error("Diharapkan nama modul (string atau identifier) setelah 'impor_python'")
        alias = None
        if self.current_token.type == TokenType.SEBAGAI:
            self.eat(TokenType.SEBAGAI)
            alias = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        return PythonImport(module_name, alias, token)

    def from_import_statement(self):  # noqa: C901
        """
        Parse 'dari module impor item1, item2, ...' statements
        Supports:
        - Nested modules: 'dari Ren.renz impor Class1, Class2'
        - Wildcard import: 'dari module impor *'
        - Relative import: 'dari .module impor func'
        """
        token = self.current_token
        self.eat(TokenType.DARI)

        # Check for relative import (starts with .)
        is_relative = False
        relative_level = 0

        while self.current_token.type == TokenType.TITIK:
            is_relative = True
            relative_level += 1
            self.eat(TokenType.TITIK)

        # Parse module path (can be dot-separated like "Ren.renz")
        module_parts = []

        # For relative imports, module name is optional (e.g., 'dari . impor func')
        if self.current_token.type == TokenType.IDENTIFIER:
            module_parts.append(self.current_token.value)
            self.eat(TokenType.IDENTIFIER)
        elif self.current_token.type == TokenType.TEKS:
            module_parts.append(self.current_token.value)
            self.eat(TokenType.TEKS)
        elif not is_relative:
            self.error("Diharapkan nama modul setelah 'dari'")

        # Handle dot-separated module paths (e.g., Ren.renz)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            if self.current_token.type == TokenType.IDENTIFIER:
                module_parts.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            else:
                self.error("Diharapkan nama modul setelah '.'")

        module_name = ".".join(module_parts) if module_parts else ""

        # Expect 'impor' keyword
        if self.current_token.type != TokenType.IMPOR:
            self.error("Diharapkan 'impor' setelah nama modul")
        self.eat(TokenType.IMPOR)

        # Check for wildcard import (*)
        if self.current_token.type == TokenType.KALI_OP:
            self.eat(TokenType.KALI_OP)
            # Return special marker for wildcard import
            return FromImport(
                module_name,
                [("*", None)],
                token,
                is_relative=is_relative,
                relative_level=relative_level,
            )

        # Parse items to import (can be comma-separated)
        items = []

        # First item
        if self.current_token.type == TokenType.IDENTIFIER:
            item_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)

            # Check for alias
            alias = None
            if self.current_token.type == TokenType.SEBAGAI:
                self.eat(TokenType.SEBAGAI)
                alias = self.current_token.value
                self.eat(TokenType.IDENTIFIER)

            items.append((item_name, alias))
        else:
            self.error("Diharapkan nama item untuk diimpor")

        # Additional items (comma-separated)
        while self.current_token.type == TokenType.KOMA:
            self.eat(TokenType.KOMA)

            if self.current_token.type == TokenType.IDENTIFIER:
                item_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)

                # Check for alias
                alias = None
                if self.current_token.type == TokenType.SEBAGAI:
                    self.eat(TokenType.SEBAGAI)
                    alias = self.current_token.value
                    self.eat(TokenType.IDENTIFIER)

                items.append((item_name, alias))
            else:
                self.error("Diharapkan nama item setelah koma")

        return FromImport(
            module_name,
            items,
            token,
            is_relative=is_relative,
            relative_level=relative_level,
        )

    def import_statement(self):
        token = self.current_token
        self.eat(TokenType.IMPOR)

        # Parse module path (can be dot-separated like "Ren.renz")
        module_parts = []
        if self.current_token.type == TokenType.TEKS:
            module_parts.append(self.current_token.value)
            self.eat(TokenType.TEKS)
        elif self.current_token.type == TokenType.IDENTIFIER:
            module_parts.append(self.current_token.value)
            self.eat(TokenType.IDENTIFIER)
        else:
            self.error("Diharapkan nama modul setelah 'impor'")

        # Handle dot-separated module paths (e.g., Ren.renz)
        while self.current_token.type == TokenType.TITIK:
            self.eat(TokenType.TITIK)
            if self.current_token.type == TokenType.IDENTIFIER:
                module_parts.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
            else:
                self.error("Diharapkan nama modul setelah '.'")

        module_name = ".".join(module_parts)

        alias = None
        if self.current_token.type == TokenType.SEBAGAI:
            self.eat(TokenType.SEBAGAI)
            alias = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
        return Import(module_name, alias, token)
