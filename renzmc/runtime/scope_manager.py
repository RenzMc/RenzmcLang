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

from renzmc.core.error import RenzmcNameError
from renzmc.runtime.inline_cache import InlineCache


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
        self.inline_cache = InlineCache()

    def get_variable(self, name):
        scope_id = id(self.local_scope) if self.local_scope else id(self.global_scope)

        cached = self.inline_cache.get(name, scope_id)
        if cached is not None:
            scope_type, value = cached
            if scope_type == "instance" and self.current_instance is not None:
                instance_id = id(self.current_instance)
                if instance_id in self.instance_scopes and name in self.instance_scopes[instance_id]:
                    return self.instance_scopes[instance_id][name]
            elif scope_type == "local" and name in self.local_scope:
                return self.local_scope[name]
            elif scope_type == "global" and name in self.global_scope:
                return self.global_scope[name]
            elif scope_type == "builtin" and hasattr(self, "builtin_functions") and name in self.builtin_functions:
                return self.builtin_functions[name]

        if self.current_instance is not None:
            instance_id = id(self.current_instance)
            if instance_id in self.instance_scopes and name in self.instance_scopes[instance_id]:
                value = self.instance_scopes[instance_id][name]
                self.inline_cache.set(name, scope_id, "instance", value)
                return value
        if name in self.local_scope:
            value = self.local_scope[name]
            self.inline_cache.set(name, scope_id, "local", value)
            return value
        if name in self.global_scope:
            value = self.global_scope[name]
            self.inline_cache.set(name, scope_id, "global", value)
            return value
        if hasattr(self, "builtin_functions") and name in self.builtin_functions:
            value = self.builtin_functions[name]
            self.inline_cache.set(name, scope_id, "builtin", value)
            return value
        raise RenzmcNameError(f"Variabel '{name}' tidak terdefinisi")

    def set_variable(self, name, value, is_local=False):
        scope_id = id(self.local_scope) if self.local_scope else id(self.global_scope)
        self.inline_cache.invalidate(name, scope_id)

        if self.current_instance is not None and (not is_local):
            instance_id = id(self.current_instance)
            if instance_id not in self.instance_scopes:
                self.instance_scopes[instance_id] = {}
            self.instance_scopes[instance_id][name] = value
        elif is_local or self.local_scope:
            self.local_scope[name] = value
        else:
            self.global_scope[name] = value
