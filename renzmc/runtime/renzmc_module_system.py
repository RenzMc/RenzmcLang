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

import os

from renzmc.core.error import (
    RenzmcImportError,
    RenzmcNameError,
)


class RenzmcModule:

    def __init__(self, module_path, module_name, module_dict):
        self.module_path = module_path
        self.module_name = module_name
        self._module_dict = module_dict
        self._classes = {}
        self._functions = {}
        self._variables = {}
        for name, value in module_dict.items():
            if hasattr(value, "__class__") and value.__class__.__name__ == "RenzmcClass":
                self._classes[name] = value
            elif callable(value):
                self._functions[name] = value
            else:
                self._variables[name] = value

    def __getattr__(self, name):
        if name in self._module_dict:
            return self._module_dict[name]
        raise RenzmcNameError(f"Modul '{self.module_name}' tidak memiliki atribut '{name}'")

    def get_classes(self):
        return self._classes

    def get_functions(self):
        return self._functions

    def get_variables(self):
        return self._variables

    def list_contents(self):
        return {
            "classes": list(self._classes.keys()),
            "functions": list(self._functions.keys()),
            "variables": list(self._variables.keys()),
        }


class RenzmcModuleManager:

    def __init__(self, interpreter_instance):
        self.interpreter = interpreter_instance
        self.loaded_modules = {}
        self.module_search_paths = []
        self.module_cache = {}
        self.add_search_path(".")
        self.add_search_path("./lib")
        self.add_search_path("./modules")

    def add_search_path(self, path):
        abs_path = os.path.abspath(path)
        if abs_path not in self.module_search_paths:
            self.module_search_paths.append(abs_path)

    def find_module(self, module_name):
        """
        Find a module file by name, supporting both simple and nested paths.
        Examples:
        - "math_utils" -> searches for "math_utils.rmc"
        - "Ren.renz" -> searches for "Ren/renz.rmc"
        """
        extensions = [".rmc", ".renzmc"]

        # Convert dot-separated module name to path
        # e.g., "Ren.renz" becomes "Ren/renz"
        module_path = module_name.replace(".", os.sep)

        for search_path in self.module_search_paths:
            for ext in extensions:
                # Try direct file path
                module_file = os.path.join(search_path, f"{module_path}{ext}")
                if os.path.isfile(module_file):
                    return module_file

                # Try as package with __init__ file
                package_init = os.path.join(search_path, module_path, f"__init__{ext}")
                if os.path.isfile(package_init):
                    return package_init

        return None

    def load_module(self, module_name, alias=None):
        cache_key = alias or module_name
        if cache_key in self.loaded_modules:
            return self.loaded_modules[cache_key]
        module_path = self.find_module(module_name)
        if not module_path:
            raise RenzmcImportError(f"Tidak dapat menemukan modul RenzmcLang '{module_name}'")
        try:
            with open(module_path, "r", encoding="utf-8") as f:
                module_code = f.read()

            # Save old scopes
            old_global_scope = self.interpreter.global_scope.copy()
            old_local_scope = self.interpreter.local_scope.copy()

            # Create a new temporary global scope for the module
            module_scope = {}
            self.interpreter.global_scope = module_scope
            self.interpreter.local_scope = module_scope

            from renzmc.core.lexer import Lexer
            from renzmc.core.parser import Parser

            # Create a fresh lexer for the parser
            lexer = Lexer(module_code)
            parser = Parser(lexer)
            ast = parser.parse()
            self.interpreter.visit(ast)

            # Capture everything that was added to the module scope
            module_obj = RenzmcModule(module_path, module_name, module_scope)
            self.loaded_modules[cache_key] = module_obj

            # Restore old scopes
            self.interpreter.global_scope = old_global_scope
            self.interpreter.local_scope = old_local_scope

            return module_obj
        except Exception as e:
            raise RenzmcImportError(f"Error memuat modul '{module_name}': {str(e)}")

    def import_from_module(self, module_name, items):
        module = self.load_module(module_name)
        imported_items = {}
        for item in items:
            if hasattr(module, item):
                imported_items[item] = getattr(module, item)
            else:
                raise RenzmcImportError(
                    f"Tidak dapat mengimpor '{item}' dari modul '{module_name}'"
                )
        return imported_items

    def get_module_info(self, module_name):
        if module_name in self.loaded_modules:
            module = self.loaded_modules[module_name]
            return {
                "name": module.module_name,
                "path": module.module_path,
                "contents": module.list_contents(),
                "loaded": True,
            }
        module_path = self.find_module(module_name)
        if module_path:
            return {
                "name": module_name,
                "path": module_path,
                "contents": None,
                "loaded": False,
            }
        return None

    def reload_module(self, module_name):
        if module_name in self.loaded_modules:
            del self.loaded_modules[module_name]
        return self.load_module(module_name)

    def resolve_relative_import(self, module_name, relative_level, current_file_path):
        """
        Resolve relative import path based on current file location.

        Args:
            module_name: The module name (can be empty for 'dari . impor')
            relative_level: Number of dots (1 for ., 2 for .., etc.)
            current_file_path: Path of the file doing the import

        Returns:
            Resolved absolute module path
        """
        if not current_file_path:
            raise RenzmcImportError("Tidak dapat menggunakan relative import tanpa file path")

        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(current_file_path))

        # Go up 'relative_level' directories
        for _ in range(relative_level):
            current_dir = os.path.dirname(current_dir)

        # If module_name is provided, append it
        if module_name:
            module_path = os.path.join(current_dir, module_name.replace(".", os.sep))
        else:
            module_path = current_dir

        # Try to find the module file
        extensions = [".rmc", ".renzmc"]
        for ext in extensions:
            test_path = f"{module_path}{ext}"
            if os.path.isfile(test_path):
                return test_path

            # Try as package with __init__ file
            init_path = os.path.join(module_path, f"__init__{ext}")
            if os.path.isfile(init_path):
                return init_path

        raise RenzmcImportError(
            f"Tidak dapat menemukan modul relatif: {module_name} " f"(level: {relative_level})"
        )

    def import_all_from_module(self, module_name):
        """
        Import all items from a module (wildcard import).
        Returns a dictionary of all exported items.
        """
        module = self.load_module(module_name)

        # Check if module has __all__ attribute (explicit exports)
        if hasattr(module, "_module_dict") and "__all__" in module._module_dict:
            all_items = module._module_dict["__all__"]
            result = {}
            for item_name in all_items:
                if item_name in module._module_dict:
                    result[item_name] = module._module_dict[item_name]
            return result

        # Otherwise, return all public items (not starting with _)
        result = {}
        for name, value in module._module_dict.items():
            if not name.startswith("_"):
                result[name] = value
        return result

    def list_available_modules(self):
        modules = []
        extensions = [".rmc", ".renzmc"]
        for search_path in self.module_search_paths:
            if os.path.isdir(search_path):
                for file in os.listdir(search_path):
                    for ext in extensions:
                        if file.endswith(ext):
                            module_name = file[: -len(ext)]
                            if module_name not in modules:
                                modules.append(module_name)
        return modules
