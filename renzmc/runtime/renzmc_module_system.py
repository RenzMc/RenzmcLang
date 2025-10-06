import os
from renzmc.core.error import (
    RenzmcImportError,
    RenzmcNameError,
)
from renzmc.core.token import TokenType


class RenzmcModule:

    def __init__(self, module_path, module_name, module_dict):
        self.module_path = module_path
        self.module_name = module_name
        self._module_dict = module_dict
        self._classes = {}
        self._functions = {}
        self._variables = {}
        for name, value in module_dict.items():
            if (
                hasattr(value, "__class__")
                and value.__class__.__name__ == "RenzmcClass"
            ):
                self._classes[name] = value
            elif callable(value):
                self._functions[name] = value
            else:
                self._variables[name] = value

    def __getattr__(self, name):
        if name in self._module_dict:
            return self._module_dict[name]
        raise RenzmcNameError(
            f"Modul '{self.module_name}' tidak memiliki atribut '{name}'"
        )

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
        extensions = [".rmc", ".renzmc"]
        for search_path in self.module_search_paths:
            for ext in extensions:
                module_file = os.path.join(search_path, f"{module_name}{ext}")
                if os.path.isfile(module_file):
                    return module_file
        return None

    def load_module(self, module_name, alias=None):
        cache_key = alias or module_name
        if cache_key in self.loaded_modules:
            return self.loaded_modules[cache_key]
        module_path = self.find_module(module_name)
        if not module_path:
            raise RenzmcImportError(
                f"Tidak dapat menemukan modul RenzmcLang '{module_name}'"
            )
        try:
            with open(module_path, "r", encoding="utf-8") as f:
                module_code = f.read()
            module_scope = {}
            old_global_scope = self.interpreter.global_scope.copy()
            old_local_scope = self.interpreter.local_scope.copy()
            self.interpreter.local_scope = module_scope
            from renzmc.core.lexer import Lexer
            from renzmc.core.parser import Parser

            lexer = Lexer(module_code)
            tokens = []
            while True:
                token = lexer.get_next_token()
                tokens.append(token)
                if token and token.type == TokenType.EOF:
                    break
            parser = Parser(lexer)
            ast = parser.parse()
            self.interpreter.visit(ast)
            module_obj = RenzmcModule(module_path, module_name, module_scope)
            self.loaded_modules[cache_key] = module_obj
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

    def import_all_from_module(self, module_name):
        module = self.load_module(module_name)
        return module._module_dict.copy()

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
