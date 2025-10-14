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

from renzmc.core.error import RenzmcNameError


class ScopeManager:

    def __init__(self):
        self.global_scope = {}
        self.local_scope = {}
        self.functions = {}
        self.classes = {}
        self.modules = {}
        self.current_instance = None
        self.instance_scopes = {}
        self.generators = {}
        self.async_functions = {}
        self.decorators = {}
        self.type_registry = {}
        self.builtin_functions = {}

    def get_variable(self, name):
        if self.current_instance is not None:
            instance_id = id(self.current_instance)
            if instance_id in self.instance_scopes and name in self.instance_scopes[instance_id]:
                return self.instance_scopes[instance_id][name]
        if name in self.local_scope:
            return self.local_scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        if hasattr(self, "builtin_functions") and name in self.builtin_functions:
            return self.builtin_functions[name]
        raise RenzmcNameError(f"Variabel '{name}' tidak terdefinisi")

    def set_variable(self, name, value, is_local=False):
        if self.current_instance is not None and (not is_local):
            instance_id = id(self.current_instance)
            if instance_id not in self.instance_scopes:
                self.instance_scopes[instance_id] = {}
            self.instance_scopes[instance_id][name] = value
        elif is_local or self.local_scope:
            self.local_scope[name] = value
        else:
            self.global_scope[name] = value
