from enum import Enum, auto
from typing import Any, Optional, Dict, List, Union as PyUnion


class BaseType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    LIST = auto()
    DICT = auto()
    TUPLE = auto()
    SET = auto()
    NONE = auto()
    ANY = auto()
    FUNCTION = auto()
    CLASS = auto()
    OBJECT = auto()


TYPE_NAME_MAPPING = {
    "Integer": BaseType.INTEGER,
    "Bilangan": BaseType.INTEGER,
    "BilanganBulat": BaseType.INTEGER,
    "Float": BaseType.FLOAT,
    "Desimal": BaseType.FLOAT,
    "BilanganDesimal": BaseType.FLOAT,
    "String": BaseType.STRING,
    "Teks": BaseType.STRING,
    "Boolean": BaseType.BOOLEAN,
    "Bool": BaseType.BOOLEAN,
    "List": BaseType.LIST,
    "Daftar": BaseType.LIST,
    "Dict": BaseType.DICT,
    "Dictionary": BaseType.DICT,
    "Kamus": BaseType.DICT,
    "Tuple": BaseType.TUPLE,
    "Set": BaseType.SET,
    "Himpunan": BaseType.SET,
    "None": BaseType.NONE,
    "Kosong": BaseType.NONE,
    "Any": BaseType.ANY,
    "Apapun": BaseType.ANY,
    "Function": BaseType.FUNCTION,
    "Fungsi": BaseType.FUNCTION,
    "Class": BaseType.CLASS,
    "Kelas": BaseType.CLASS,
    "Object": BaseType.OBJECT,
    "Objek": BaseType.OBJECT,

    "int": BaseType.INTEGER,
    "integer": BaseType.INTEGER,
    "float": BaseType.FLOAT,
    "str": BaseType.STRING,
    "string": BaseType.STRING,
    "bool": BaseType.BOOLEAN,
    "boolean": BaseType.BOOLEAN,
    "list": BaseType.LIST,
    "dict": BaseType.DICT,
    "tuple": BaseType.TUPLE,
    "set": BaseType.SET,
    "none": BaseType.NONE,
    "any": BaseType.ANY,
    "function": BaseType.FUNCTION,
    "class": BaseType.CLASS,
    "object": BaseType.OBJECT,
}

TYPE_ALIASES = {}


class TypeValidator:

    @staticmethod
    def get_python_type(value: Any) -> BaseType:
        if value is None:
            return BaseType.NONE
        elif isinstance(value, bool):
            return BaseType.BOOLEAN
        elif isinstance(value, int):
            return BaseType.INTEGER
        elif isinstance(value, float):
            return BaseType.FLOAT
        elif isinstance(value, str):
            return BaseType.STRING
        elif isinstance(value, list):
            return BaseType.LIST
        elif isinstance(value, dict):
            return BaseType.DICT
        elif isinstance(value, tuple):
            return BaseType.TUPLE
        elif isinstance(value, set):
            return BaseType.SET
        elif callable(value):
            return BaseType.FUNCTION
        else:
            return BaseType.OBJECT

    @staticmethod
    def parse_type_hint(type_hint_str: str) -> Optional[BaseType]:
        if not type_hint_str:
            return None

        type_hint_str = type_hint_str.strip()

        if type_hint_str in TYPE_ALIASES:
            return TYPE_ALIASES[type_hint_str]

        if type_hint_str in TYPE_NAME_MAPPING:
            return TYPE_NAME_MAPPING[type_hint_str]

        return None

    @staticmethod
    def validate_type(value: Any, expected_type: BaseType, var_name: str = "") -> tuple[bool, str]:
        if expected_type == BaseType.ANY:
            return True, ""

        actual_type = TypeValidator.get_python_type(value)

        if actual_type == expected_type:
            return True, ""

        if expected_type == BaseType.FLOAT and actual_type == BaseType.INTEGER:
            return True, ""

        var_info = f"variabel '{var_name}'" if var_name else "nilai"
        error_msg = (
            f"Kesalahan Tipe: {var_info} diharapkan bertipe '{TypeValidator.type_to_string(expected_type)}', "
            f"tetapi mendapat '{TypeValidator.type_to_string(actual_type)}'"
        )
        return False, error_msg

    @staticmethod
    def type_to_string(base_type: BaseType) -> str:
        type_strings = {
            BaseType.INTEGER: "Integer",
            BaseType.FLOAT: "Float",
            BaseType.STRING: "String",
            BaseType.BOOLEAN: "Boolean",
            BaseType.LIST: "List",
            BaseType.DICT: "Dict",
            BaseType.TUPLE: "Tuple",
            BaseType.SET: "Set",
            BaseType.NONE: "None",
            BaseType.ANY: "Any",
            BaseType.FUNCTION: "Function",
            BaseType.CLASS: "Class",
            BaseType.OBJECT: "Object",
        }
        return type_strings.get(base_type, "Unknown")


class TypeChecker:

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode
        self.validator = TypeValidator()
        self.enable_advanced_types = True
        self.enable_type_inference = True

    def check_variable_assignment(self, var_name: str, value: Any,
                                  type_hint: Optional[str]) -> tuple[bool, str]:
        if not type_hint:
            if self.strict_mode:
                return False, f"Mode Ketat: Variabel '{var_name}' harus memiliki anotasi tipe"
            return True, ""

        if self.enable_advanced_types:
            try:
                from renzmc.core.advanced_types import TypeParser, AdvancedTypeValidator
                type_spec = TypeParser.parse_type_string(type_hint)
                if type_spec:
                    return AdvancedTypeValidator.validate(value, type_spec, var_name)
            except Exception:
                pass

        expected_type = self.validator.parse_type_hint(type_hint)
        if expected_type is None:
            return True, ""

        return self.validator.validate_type(value, expected_type, var_name)

    def check_function_parameter(self, param_name: str, value: Any,
                                type_hint: Optional[str], func_name: str = "") -> tuple[bool, str]:
        if not type_hint:
            if self.strict_mode:
                func_info = f" di fungsi '{func_name}'" if func_name else ""
                return False, f"Mode Ketat: Parameter '{param_name}'{func_info} harus memiliki anotasi tipe"
            return True, ""

        if self.enable_advanced_types:
            try:
                from renzmc.core.advanced_types import TypeParser, AdvancedTypeValidator
                type_spec = TypeParser.parse_type_string(type_hint)
                if type_spec:
                    is_valid, error_msg = AdvancedTypeValidator.validate(value, type_spec, param_name)
                    if not is_valid and func_name:
                        error_msg = f"Fungsi '{func_name}': {error_msg}"
                    return is_valid, error_msg
            except Exception:
                pass

        expected_type = self.validator.parse_type_hint(type_hint)
        if expected_type is None:
            return True, ""

        is_valid, error_msg = self.validator.validate_type(value, expected_type, param_name)

        if not is_valid and func_name:
            error_msg = f"Fungsi '{func_name}': {error_msg}"

        return is_valid, error_msg

    def check_function_return(self, return_value: Any, return_type_hint: Optional[str],
                            func_name: str = "") -> tuple[bool, str]:
        if not return_type_hint:
            if self.strict_mode:
                func_info = f"Fungsi '{func_name}'" if func_name else "Fungsi"
                return False, f"Mode Ketat: {func_info} harus memiliki anotasi tipe return"
            return True, ""

        if self.enable_advanced_types:
            try:
                from renzmc.core.advanced_types import TypeParser, AdvancedTypeValidator
                type_spec = TypeParser.parse_type_string(return_type_hint)
                if type_spec:
                    is_valid, error_msg = AdvancedTypeValidator.validate(return_value, type_spec, "nilai return")
                    if not is_valid and func_name:
                        error_msg = f"Fungsi '{func_name}': {error_msg}"
                    return is_valid, error_msg
            except Exception:
                pass

        expected_type = self.validator.parse_type_hint(return_type_hint)
        if expected_type is None:
            return True, ""

        is_valid, error_msg = self.validator.validate_type(return_value, expected_type, "nilai return")

        if not is_valid and func_name:
            error_msg = f"Fungsi '{func_name}': {error_msg}"

        return is_valid, error_msg


def check_type(value: Any, type_hint: str, context: str = "") -> tuple[bool, str]:
    validator = TypeValidator()
    expected_type = validator.parse_type_hint(type_hint)
    if expected_type is None:
        return True, ""
    return validator.validate_type(value, expected_type, context)


def infer_type(value: Any) -> str:
    try:
        from renzmc.core.advanced_types import TypeInference

        if isinstance(value, list):
            inferred = TypeInference.infer_list_type(value)
            return str(inferred)
        elif isinstance(value, dict):
            inferred = TypeInference.infer_dict_type(value)
            return str(inferred)
        else:
            inferred = TypeInference.infer_type(value)
            return TypeValidator.type_to_string(inferred)
    except Exception:
        base_type = TypeValidator.get_python_type(value)
        return TypeValidator.type_to_string(base_type)
