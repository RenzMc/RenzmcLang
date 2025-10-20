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

from enum import Enum
from typing import (
    Any,
)
from typing import Dict as PyDict
from typing import List as PyList
from typing import (
    Optional,
)
from typing import Union as PyUnion

from renzmc.core.type_system import BaseType, TypeValidator


class AdvancedTypeKind(Enum):
    UNION = "union"
    OPTIONAL = "optional"
    GENERIC = "generic"
    LITERAL = "literal"
    TUPLE_TYPE = "tuple"
    TYPED_DICT = "typed_dict"


class AdvancedType:

    def __init__(self, kind: AdvancedTypeKind):
        self.kind = kind

    def __repr__(self):
        return f"AdvancedType({self.kind})"


class UnionType(AdvancedType):

    def __init__(self, types: PyList[BaseType]):
        super().__init__(AdvancedTypeKind.UNION)
        self.types = types

    def __repr__(self):
        type_names = " | ".join([TypeValidator.type_to_string(t) for t in self.types])
        return f"Union[{type_names}]"

    def validate(self, value: Any) -> bool:
        validator = TypeValidator()
        actual_type = validator.get_python_type(value)
        return actual_type in self.types


class OptionalType(AdvancedType):

    def __init__(self, base_type: BaseType):
        super().__init__(AdvancedTypeKind.OPTIONAL)
        self.base_type = base_type

    def __repr__(self):
        return f"{TypeValidator.type_to_string(self.base_type)}?"

    def validate(self, value: Any) -> bool:
        if value is None:
            return True
        validator = TypeValidator()
        actual_type = validator.get_python_type(value)
        return actual_type == self.base_type


class GenericType(AdvancedType):

    def __init__(self, container_type: BaseType, element_types: PyList[BaseType]):
        super().__init__(AdvancedTypeKind.GENERIC)
        self.container_type = container_type
        self.element_types = element_types

    def __repr__(self):
        container_name = TypeValidator.type_to_string(self.container_type)
        element_names = ", ".join([TypeValidator.type_to_string(t) for t in self.element_types])
        return f"{container_name}[{element_names}]"

    def validate(self, value: Any) -> bool:
        validator = TypeValidator()
        actual_type = validator.get_python_type(value)

        if actual_type != self.container_type:
            return False

        if self.container_type == BaseType.LIST:
            return self._validate_list(value)
        elif self.container_type == BaseType.DICT:
            return self._validate_dict(value)
        elif self.container_type == BaseType.TUPLE:
            return self._validate_tuple(value)
        elif self.container_type == BaseType.SET:
            return self._validate_set(value)

        return True

    def _validate_list(self, value: list) -> bool:
        if not self.element_types:
            return True

        element_type = self.element_types[0]
        validator = TypeValidator()

        for item in value:
            item_type = validator.get_python_type(item)
            if item_type != element_type:
                if element_type == BaseType.FLOAT and item_type == BaseType.INTEGER:
                    continue
                return False

        return True

    def _validate_dict(self, value: dict) -> bool:
        if len(self.element_types) < 2:
            return True

        key_type = self.element_types[0]
        value_type = self.element_types[1]
        validator = TypeValidator()

        for k, v in value.items():
            k_type = validator.get_python_type(k)
            v_type = validator.get_python_type(v)

            if k_type != key_type:
                return False

            if v_type != value_type:
                if value_type == BaseType.FLOAT and v_type == BaseType.INTEGER:
                    continue
                return False

        return True

    def _validate_tuple(self, value: tuple) -> bool:
        if len(value) != len(self.element_types):
            return False

        validator = TypeValidator()

        for item, expected_type in zip(value, self.element_types):
            item_type = validator.get_python_type(item)
            if item_type != expected_type:
                if expected_type == BaseType.FLOAT and item_type == BaseType.INTEGER:
                    continue
                return False

        return True

    def _validate_set(self, value: set) -> bool:
        if not self.element_types:
            return True

        element_type = self.element_types[0]
        validator = TypeValidator()

        for item in value:
            item_type = validator.get_python_type(item)
            if item_type != element_type:
                return False

        return True


class TupleType(AdvancedType):

    def __init__(self, element_types: PyList[BaseType]):
        super().__init__(AdvancedTypeKind.TUPLE_TYPE)
        self.element_types = element_types

    def __repr__(self):
        element_names = ", ".join([TypeValidator.type_to_string(t) for t in self.element_types])
        return f"Tuple[{element_names}]"

    def validate(self, value: Any) -> bool:
        if not isinstance(value, tuple):
            return False

        if len(value) != len(self.element_types):
            return False

        validator = TypeValidator()

        for item, expected_type in zip(value, self.element_types):
            item_type = validator.get_python_type(item)
            if item_type != expected_type:
                if expected_type == BaseType.FLOAT and item_type == BaseType.INTEGER:
                    continue
                return False

        return True


class LiteralType(AdvancedType):

    def __init__(self, values: PyList[Any]):
        super().__init__(AdvancedTypeKind.LITERAL)
        self.values = values

    def __repr__(self):
        value_strs = ", ".join([repr(v) for v in self.values])
        return f"Literal[{value_strs}]"

    def validate(self, value: Any) -> bool:
        return value in self.values


class TypedDictType(AdvancedType):

    def __init__(self, fields: PyDict[str, BaseType]):
        super().__init__(AdvancedTypeKind.TYPED_DICT)
        self.fields = fields

    def __repr__(self):
        field_strs = ", ".join([f"{k}: {TypeValidator.type_to_string(v)}" for k, v in self.fields.items()])
        return f"TypedDict[{field_strs}]"

    def validate(self, value: Any) -> bool:
        if not isinstance(value, dict):
            return False

        validator = TypeValidator()

        for key, expected_type in self.fields.items():
            if key not in value:
                return False

            item_type = validator.get_python_type(value[key])
            if item_type != expected_type:
                if expected_type == BaseType.FLOAT and item_type == BaseType.INTEGER:
                    continue
                return False

        return True


class TypeParser:

    @staticmethod
    def parse_type_string(
        type_str: str,
    ) -> PyUnion[BaseType, AdvancedType]:
        type_str = type_str.strip()

        if type_str.endswith("?"):
            base_type_str = type_str[:-1].strip()
            base_type = TypeValidator().parse_type_hint(base_type_str)
            if base_type:
                return OptionalType(base_type)

        if "|" in type_str:
            type_parts = [part.strip() for part in type_str.split("|")]
            types = []
            for part in type_parts:
                parsed = TypeValidator().parse_type_hint(part)
                if parsed:
                    types.append(parsed)
            if types:
                return UnionType(types)

        if "[" in type_str and "]" in type_str:
            bracket_start = type_str.index("[")
            bracket_end = type_str.rindex("]")

            container_str = type_str[:bracket_start].strip()
            elements_str = type_str[bracket_start + 1 : bracket_end].strip()

            if container_str in ["Literal", "literal"]:
                values = []
                parts = elements_str.split(",")
                for part in parts:
                    part = part.strip()
                    if part.startswith('"') and part.endswith('"'):
                        values.append(part[1:-1])
                    elif part.startswith("'") and part.endswith("'"):
                        values.append(part[1:-1])
                    elif part.lower() == "benar" or part.lower() == "true":
                        values.append(True)
                    elif part.lower() == "salah" or part.lower() == "false":
                        values.append(False)
                    elif "." in part:
                        try:
                            values.append(float(part))
                        except ValueError:
                            pass
                    else:
                        try:
                            values.append(int(part))
                        except ValueError:
                            pass
                if values:
                    return LiteralType(values)

            if container_str in ["TypedDict", "typed_dict", "KamusTipe", "kamus_tipe"]:
                fields = {}
                parts = elements_str.split(",")
                for part in parts:
                    if ":" in part:
                        key_val = part.split(":", 1)
                        key = key_val[0].strip().strip('"').strip("'")
                        type_str_inner = key_val[1].strip()
                        parsed_type = TypeValidator().parse_type_hint(type_str_inner)
                        if parsed_type:
                            fields[key] = parsed_type
                if fields:
                    return TypedDictType(fields)

            container_type = TypeValidator().parse_type_hint(container_str)
            if not container_type:
                return None

            element_parts = [part.strip() for part in elements_str.split(",")]
            element_types = []
            for part in element_parts:
                parsed = TypeValidator().parse_type_hint(part)
                if parsed:
                    element_types.append(parsed)

            if element_types:
                return GenericType(container_type, element_types)

        return TypeValidator().parse_type_hint(type_str)


class AdvancedTypeValidator:

    @staticmethod
    def validate(value: Any, type_spec: PyUnion[BaseType, AdvancedType], var_name: str = "") -> tuple[bool, str]:
        if isinstance(type_spec, BaseType):
            validator = TypeValidator()
            return validator.validate_type(value, type_spec, var_name)

        if isinstance(type_spec, AdvancedType):
            is_valid = type_spec.validate(value)
            if not is_valid:
                var_info = f"variabel '{var_name}'" if var_name else "nilai"
                error_msg = (
                    f"Kesalahan Tipe: {var_info} diharapkan bertipe '{type_spec}', "
                    f"tetapi mendapat nilai yang tidak sesuai"
                )
                return False, error_msg
            return True, ""

        return True, ""


class TypeInference:

    @staticmethod
    def infer_type(value: Any) -> BaseType:
        return TypeValidator.get_python_type(value)

    @staticmethod
    def infer_list_type(values: list) -> PyUnion[BaseType, GenericType]:
        if not values:
            return BaseType.LIST

        element_types = set()
        for item in values:
            element_types.add(TypeInference.infer_type(item))

        if len(element_types) == 1:
            element_type = list(element_types)[0]
            return GenericType(BaseType.LIST, [element_type])

        return BaseType.LIST

    @staticmethod
    def infer_dict_type(value: dict) -> PyUnion[BaseType, GenericType]:
        if not value:
            return BaseType.DICT

        key_types = set()
        value_types = set()

        for k, v in value.items():
            key_types.add(TypeInference.infer_type(k))
            value_types.add(TypeInference.infer_type(v))

        if len(key_types) == 1 and len(value_types) == 1:
            key_type = list(key_types)[0]
            value_type = list(value_types)[0]
            return GenericType(BaseType.DICT, [key_type, value_type])

        return BaseType.DICT

    @staticmethod
    def infer_function_return_type(function_body: list) -> Optional[BaseType]:
        return None
