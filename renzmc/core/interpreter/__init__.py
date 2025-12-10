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

from renzmc.core.interpreter.advanced_features import AdvancedFeaturesMixin
from renzmc.core.interpreter.base import InterpreterBase
from renzmc.core.interpreter.builtin_setup import BuiltinSetupMixin
from renzmc.core.interpreter.crypto_operations import CryptoOperationsMixin
from renzmc.core.interpreter.file_operations import FileOperationsMixin
from renzmc.core.interpreter.http_operations import HTTPOperationsMixin
from renzmc.core.interpreter.methods import ExecutionMethodsMixin
from renzmc.core.interpreter.python_integration import PythonIntegrationMixin
from renzmc.core.interpreter.renzmc_modules import RenzmcModulesMixin
from renzmc.core.interpreter.rust_execution import RustExecutionMixin
from renzmc.core.interpreter.scope_management import ScopeManagementMixin
from renzmc.core.interpreter.type_system import TypeSystemMixin
from renzmc.core.interpreter.utility import UtilityMixin


class Interpreter(
    InterpreterBase,
    TypeSystemMixin,
    ScopeManagementMixin,
    UtilityMixin,
    BuiltinSetupMixin,
    PythonIntegrationMixin,
    RenzmcModulesMixin,
    FileOperationsMixin,
    CryptoOperationsMixin,
    HTTPOperationsMixin,
    AdvancedFeaturesMixin,
    ExecutionMethodsMixin,
    RustExecutionMixin,
):
    """
    Main Interpreter class for RenzmcLang.

    This class combines all functionality mixins to provide a complete
    interpreter implementation. The modular design allows for easy
    maintenance and feature additions.

    Functionality Areas:
        - InterpreterBase: Core initialization and setup
        - TypeSystemMixin: Type validation and checking
        - ScopeManagementMixin: Variable and scope management
        - UtilityMixin: Helper methods and utilities
        - BuiltinSetupMixin: Builtin function registration
        - PythonIntegrationMixin: Python interoperability
        - RenzmcModulesMixin: RenzmcLang module system
        - FileOperationsMixin: File I/O operations
        - CryptoOperationsMixin: Cryptographic operations
        - HTTPOperationsMixin: HTTP request handling
        - AdvancedFeaturesMixin: Decorators, generators, async
        - ExecutionMethodsMixin: AST visitor and execution methods
    """

    def interpret(self, tree):
        """
        Interpret an AST tree.

        Args:
            tree: The AST tree to interpret

        Returns:
            The result of interpretation
        """
        return self.visit_with_rust(tree)


__all__ = ["Interpreter"]
