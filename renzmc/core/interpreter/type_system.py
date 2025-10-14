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
RenzmcLang Interpreter Type System Module

This module contains type validation and checking functionality.
"""

import builtins as py_builtins
import re

from renzmc.utils.error_handler import log_exception
from renzmc.utils.type_helpers import (
    check_parameter_type,
    check_return_type,
    get_type_from_registry,
)


class TypeSystemMixin:
    """
    Mixin class for type system functionality.

    Provides type validation, checking, and registry management.
    """

    def _validate_parameter_type(self, param_value, type_name, param_name, function_name=""):
        """
        Validate parameter type with proper error handling

        Args:
            param_value: The parameter value to check
            type_name: Expected type name
            param_name: Name of the parameter
            function_name: Name of the function (for error messages)

        Returns:
            bool: True if validation passes, False otherwise
        """
        return check_parameter_type(param_value, type_name, param_name, self.type_registry, function_name)

    def _validate_return_type(self, return_value, type_name, function_name=""):
        """
        Validate return type with proper error handling

        Args:
            return_value: The return value to check
            type_name: Expected type name
            function_name: Name of the function (for error messages)

        Returns:
            bool: True if validation passes, False otherwise
        """
        return check_return_type(return_value, type_name, self.type_registry, function_name)

    def _get_type_from_registry(self, type_name):
        """
        Get a type from the registry or builtins

        Args:
            type_name: Name of the type to retrieve

        Returns:
            The type object if found, None otherwise
        """
        return get_type_from_registry(type_name, self.type_registry)

    def _check_type(self, obj, type_name):
        """
        Check if an object matches a type specification.

        Args:
            obj: The object to check
            type_name: The type specification string

        Returns:
            bool: True if the object matches the type, False otherwise
        """
        if type_name == "None" or type_name == "NoneType":
            return obj is None
        if "|" in type_name:
            union_types = [t.strip() for t in type_name.split("|")]
            return any((self._check_type(obj, t) for t in union_types))
        list_match = re.match(r"(?:list|array)\[(.*)\]", type_name)
        if list_match:
            if not isinstance(obj, list):
                return False
            if not obj:
                return True
            element_type = list_match.group(1)
            return all((self._check_type(item, element_type) for item in obj))
        dict_match = re.match(r"dict\[(.*),(.*)\]", type_name)
        if dict_match:
            if not isinstance(obj, dict):
                return False
            if not obj:
                return True
            key_type = dict_match.group(1).strip()
            value_type = dict_match.group(2).strip()
            return all((self._check_type(k, key_type) and self._check_type(v, value_type) for k, v in obj.items()))
        tuple_match = re.match(r"tuple\[(.*)\]", type_name)
        if tuple_match:
            if not isinstance(obj, tuple):
                return False
            element_types = [t.strip() for t in tuple_match.group(1).split(",")]
            if len(obj) != len(element_types):
                return False
            return all((self._check_type(obj[i], element_types[i]) for i in range(len(obj))))
        optional_match = re.match(r"Optional\[(.*)\]", type_name)
        if optional_match:
            if obj is None:
                return True
            return self._check_type(obj, optional_match.group(1))
        if type_name.endswith("?"):
            if obj is None:
                return True
            return self._check_type(obj, type_name[:-1])
        if type_name == "callable" or type_name == "Callable":
            return callable(obj)
        if type_name in self.type_registry:
            try:
                expected_type = self.type_registry[type_name]
                if isinstance(expected_type, type):
                    return isinstance(obj, expected_type)
            except TypeError as e:
                log_exception("type validation", e, level="debug")
            return False
        elif hasattr(py_builtins, type_name):
            try:
                expected_type = getattr(py_builtins, type_name)
                if isinstance(expected_type, type):
                    return isinstance(obj, expected_type)
            except TypeError as e:
                log_exception("type validation", e, level="debug")
            return False
        elif type_name.lower() == "string" or type_name.lower() == "str":
            return isinstance(obj, str)
        elif type_name.lower() == "integer" or type_name.lower() == "int":
            return isinstance(obj, int)
        elif type_name.lower() == "float" or type_name.lower() == "double":
            return isinstance(obj, float)
        elif type_name.lower() == "boolean" or type_name.lower() == "bool":
            return isinstance(obj, bool)
        elif type_name.lower() == "list" or type_name.lower() == "array":
            return isinstance(obj, list)
        elif type_name.lower() == "dict" or type_name.lower() == "dictionary":
            return isinstance(obj, dict)
        elif type_name.lower() == "tuple":
            return isinstance(obj, tuple)
        elif type_name.lower() == "set":
            return isinstance(obj, set)
        elif type_name.lower() == "any":
            return True
        return False
