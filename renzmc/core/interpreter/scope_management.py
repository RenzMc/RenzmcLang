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
RenzmcLang Interpreter Scope Management Module

This module contains scope and variable management functionality.
"""

from renzmc.core.error import RenzmcNameError


class ScopeManagementMixin:
    """
    Mixin class for scope management functionality.

    Provides variable storage, retrieval, and scope delegation.
    """

    @property
    def global_scope(self):
        return self.scope_manager.global_scope

    @global_scope.setter
    def global_scope(self, value):
        self.scope_manager.global_scope = value

    @property
    def local_scope(self):
        return self.scope_manager.local_scope

    @local_scope.setter
    def local_scope(self, value):
        self.scope_manager.local_scope = value

    @property
    def functions(self):
        return self.scope_manager.functions

    @functions.setter
    def functions(self, value):
        self.scope_manager.functions = value

    @property
    def classes(self):
        return self.scope_manager.classes

    @classes.setter
    def classes(self, value):
        self.scope_manager.classes = value

    @property
    def modules(self):
        return self.scope_manager.modules

    @modules.setter
    def modules(self, value):
        self.scope_manager.modules = value

    @property
    def current_instance(self):
        return self.scope_manager.current_instance

    @current_instance.setter
    def current_instance(self, value):
        self.scope_manager.current_instance = value

    @property
    def instance_scopes(self):
        return self.scope_manager.instance_scopes

    @property
    def generators(self):
        return self.scope_manager.generators

    @property
    def async_functions(self):
        return self.scope_manager.async_functions

    @property
    def decorators(self):
        return self.scope_manager.decorators

    @property
    def type_registry(self):
        return self.scope_manager.type_registry

    def get_variable(self, name):
        """
        Get a variable from the appropriate scope.

        Args:
            name: Variable name to retrieve

        Returns:
            The variable value

        Raises:
            RenzmcNameError: If variable is not found
        """
        if (
            self.current_instance is not None
            and self.current_instance in self.instance_scopes
        ):
            instance_scope = self.instance_scopes[self.current_instance]
            if name in instance_scope:
                return instance_scope[name]
        if name in self.local_scope:
            return self.local_scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        if name in self.builtin_functions:
            return self.builtin_functions[name]
        raise RenzmcNameError(f"Variabel '{name}' tidak ditemukan")

    def set_variable(self, name, value, is_local=False):
        """
        Set a variable in the appropriate scope.

        Args:
            name: Variable name
            value: Variable value
            is_local: Whether to force local scope

        Returns:
            The set value
        """
        if self.current_instance is not None:
            if self.current_instance not in self.instance_scopes:
                self.instance_scopes[self.current_instance] = {}
            self.instance_scopes[self.current_instance][name] = value
            return value
        if is_local or name in self.local_scope:
            self.local_scope[name] = value
        else:
            self.global_scope[name] = value
        return value

    def create_class_instance(self, class_name, *args, **kwargs):
        """
        Create an instance of a class.

        Args:
            class_name: Name of the class
            *args: Positional arguments for constructor
            **kwargs: Keyword arguments for constructor

        Returns:
            The created instance
        """
        return self.scope_manager.create_class_instance(
            class_name, *args, **kwargs
        )
