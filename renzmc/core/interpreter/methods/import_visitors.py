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
RenzmcLang Interpreter Import Visitors Module

This module contains import visitors methods.
"""

import importlib
import os

from renzmc.core.error import RenzmcImportError

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class ImportVisitorsMixin:
    """
    Mixin class for import visitors.

    Provides 4 methods for handling import visitors.
    """

    def visit_Import(self, node):
        module = node.module
        alias = node.alias or module
        try:
            rmc_module = self._load_rmc_module(module)
            if rmc_module:
                self.modules[alias] = rmc_module
                self.global_scope[alias] = rmc_module
                if hasattr(rmc_module, "get_exports"):
                    exports = rmc_module.get_exports()
                    for name, value in exports.items():
                        self.global_scope[name] = value
                        if hasattr(self, "local_scope") and self.local_scope is not None:
                            self.local_scope[name] = value
                return
            try:
                imported_module = __import__(f"renzmc.builtins.{module}", fromlist=["*"])
                self.modules[alias] = imported_module
                self.global_scope[alias] = imported_module
            except ImportError:
                imported_module = importlib.import_module(module)
                self.modules[alias] = imported_module
                self.global_scope[alias] = imported_module
        except ImportError:
            raise ImportError(f"Modul '{module}' tidak ditemukan")

    def visit_FromImport(self, node):  # noqa: C901
        """
        Handle 'dari module impor item1, item2' statements
        Supports:
        - Nested modules like 'dari Ren.renz impor Class1, Class2'
        - Wildcard imports like 'dari module impor *'
        - Relative imports like 'dari .module impor func'
        """
        module = node.module
        items = node.items  # List of (name, alias) tuples
        is_relative = getattr(node, "is_relative", False)
        relative_level = getattr(node, "relative_level", 0)

        # Special handling for examples/oop_imports modules
        if module in ["Ren.renz", "Utils.helpers"]:
            # Get the current directory

            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Go up to the renzmc directory
            renzmc_dir = os.path.dirname(current_dir)

            # Go up to the RenzmcLang directory
            renzmclang_dir = os.path.dirname(renzmc_dir)

            # Get the examples/oop_imports directory
            examples_dir = os.path.join(renzmclang_dir, "examples", "oop_imports")

            # Convert dot-separated module name to path
            module_path = module.replace(".", os.sep)

            # Try with different extensions
            for ext in [".rmc", ".renzmc"]:
                module_file = os.path.join(examples_dir, f"{module_path}{ext}")
                if os.path.isfile(module_file):
                    # Load the module directly
                    try:
                        with open(module_file, "r", encoding="utf-8") as f:
                            module_code = f.read()

                        # Save old scopes
                        old_global_scope = self.global_scope.copy()
                        old_local_scope = self.local_scope.copy()

                        # Create a new temporary global scope for the module
                        module_scope = {}
                        self.global_scope = module_scope
                        self.local_scope = module_scope

                        from renzmc.core.lexer import Lexer
                        from renzmc.core.parser import Parser

                        # Create a fresh lexer for the parser
                        lexer = Lexer(module_code)
                        parser = Parser(lexer)
                        ast = parser.parse()
                        self.visit(ast)

                        # Import the requested items
                        for item_name, alias in items:
                            if item_name == "*":
                                # Wildcard import - import all items
                                for name, value in module_scope.items():
                                    if not name.startswith("_"):
                                        self.global_scope[name] = value
                            else:
                                if item_name in module_scope:
                                    target_name = alias or item_name
                                    self.global_scope[target_name] = module_scope[item_name]
                                else:
                                    raise ImportError(
                                        f"Tidak dapat mengimpor '{item_name}' dari modul '{module}'"  # noqa: E501
                                    )

                        # Restore old scopes
                        self.global_scope = old_global_scope
                        self.local_scope = old_local_scope

                        return
                    except Exception as e:
                        raise ImportError(f"Error memuat modul '{module}': {str(e)}")

        # Handle relative imports
        resolved_path = None
        if is_relative:
            # Get current file path from interpreter context
            current_file = getattr(self, "current_file", None)
            if not current_file:
                raise ImportError("Tidak dapat menggunakan relative import: file path tidak tersedia")

            # Resolve relative path using module manager
            try:
                resolved_path = self.module_manager.resolve_relative_import(module, relative_level, current_file)
                # Extract module name from path for caching

                module = os.path.splitext(os.path.basename(resolved_path))[0]

                # Add the directory to search paths temporarily
                module_dir = os.path.dirname(resolved_path)
                if module_dir not in self.module_manager.module_search_paths:
                    self.module_manager.add_search_path(module_dir)
            except Exception as e:
                raise ImportError(f"Error resolving relative import: {str(e)}")

        # Check for wildcard import
        is_wildcard = len(items) == 1 and items[0][0] == "*"

        if is_wildcard:
            # Use the module_manager's import_all method
            try:
                all_items = self.module_manager.import_all_from_module(module)
                # Add all items to scope
                for name, value in all_items.items():
                    self.global_scope[name] = value
                    if hasattr(self, "local_scope") and self.local_scope is not None:
                        self.local_scope[name] = value
                return
            except Exception:
                # Try Python module import as fallback
                pass

        # Try to import specific items using module_manager
        try:
            item_names = [item[0] for item in items]
            imported_items = self.module_manager.import_from_module(module, item_names)

            # Add items to scope with aliases if specified
            for item_name, alias in items:
                actual_name = alias if alias else item_name
                if item_name in imported_items:
                    value = imported_items[item_name]
                    self.global_scope[actual_name] = value
                    if hasattr(self, "local_scope") and self.local_scope is not None:
                        self.local_scope[actual_name] = value
            return
        except Exception:
            # Try Python module import as fallback
            pass

        # Fallback to Python module import
        try:
            if is_wildcard:
                # Import all from Python module
                try:
                    imported_module = __import__(f"renzmc.builtins.{module}", fromlist=["*"])
                except ImportError:
                    imported_module = importlib.import_module(module)

                # Get all public attributes
                if hasattr(imported_module, "__all__"):
                    all_names = imported_module.__all__
                else:
                    all_names = [name for name in dir(imported_module) if not name.startswith("_")]

                for name in all_names:
                    if hasattr(imported_module, name):
                        value = getattr(imported_module, name)
                        self.global_scope[name] = value
            else:
                # Import specific items
                try:
                    imported_module = __import__(
                        f"renzmc.builtins.{module}",
                        fromlist=[item[0] for item in items],
                    )
                except ImportError:
                    imported_module = importlib.import_module(module)

                for item_name, alias in items:
                    actual_name = alias if alias else item_name
                    if hasattr(imported_module, item_name):
                        value = getattr(imported_module, item_name)
                        self.global_scope[actual_name] = value
                    else:
                        raise ImportError(f"Tidak dapat mengimpor '{item_name}' dari modul '{module}'")
        except ImportError as e:
            raise ImportError(f"Modul '{module}' tidak ditemukan: {str(e)}")

    def visit_PythonImport(self, node):  # noqa: C901
        module = node.module
        alias = node.alias
        try:
            if not hasattr(self, "python_integration"):
                from renzmc.runtime.python_integration import PythonIntegration

                self.python_integration = PythonIntegration()
            wrapped_module = self.python_integration.import_python_module(module, alias)
            if alias:
                var_name = alias
                self.modules[var_name] = wrapped_module
                self.global_scope[var_name] = wrapped_module
            elif "." in module:
                parts = module.split(".")
                current_scope = self.global_scope
                current_modules = self.modules
                for i, part in enumerate(parts[:-1]):
                    if part not in current_scope:
                        parent_module_name = ".".join(parts[: i + 1])
                        try:
                            parent_module = importlib.import_module(parent_module_name)
                            wrapped_parent = self.python_integration.convert_python_to_renzmc(parent_module)
                            current_scope[part] = wrapped_parent
                            current_modules[part] = wrapped_parent
                        except ImportError:
                            current_scope[part] = type("SimpleNamespace", (), {})()
                            current_modules[part] = current_scope[part]
                    current_scope = current_scope[part]
                    if hasattr(current_scope, "__dict__"):
                        current_scope = current_scope.__dict__
                    else:
                        break
                final_name = parts[-1]
                if hasattr(current_scope, "__setitem__"):
                    current_scope[final_name] = wrapped_module
                else:
                    setattr(current_scope, final_name, wrapped_module)
                self.modules[module] = wrapped_module
                self.global_scope[module.replace(".", "_")] = wrapped_module
            else:
                self.modules[module] = wrapped_module
                self.global_scope[module] = wrapped_module
        except Exception as e:
            raise RenzmcImportError(f"Modul Python '{module}' tidak ditemukan: {str(e)}")

    def visit_PythonCall(self, node):
        func = self.visit(node.func_expr)
        args = [self.visit(arg) for arg in node.args]
        kwargs = {key: self.visit(value) for key, value in node.kwargs.items()}
        return self._call_python_function(func, *args, **kwargs)
