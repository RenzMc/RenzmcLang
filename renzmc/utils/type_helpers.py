"""
Type Helper Utilities for RenzmcLang
Provides reusable type checking and validation functions
"""
import builtins as py_builtins
from typing import Any, Optional, Union, Type
from renzmc.utils.error_handler import handle_type_error, log_exception, logger


def validate_type(obj: Any, type_name: str, type_registry: dict, 
                  operation: str = "type validation") -> bool:
    """
    Validate if an object matches a given type name
    
    Args:
        obj: The object to validate
        type_name: The type name to check against
        type_registry: Registry of custom types
        operation: Description of the operation (for logging)
        
    Returns:
        True if type matches, False otherwise
    """
    # Check in type registry first
    if type_name in type_registry:
        try:
            expected_type = type_registry[type_name]
            if isinstance(expected_type, type):
                return isinstance(obj, expected_type)
        except TypeError as e:
            log_exception(
                f"{operation} - type registry check for '{type_name}'",
                e,
                level='debug'
            )
            return False
    
    # Check in Python builtins
    elif hasattr(py_builtins, type_name):
        try:
            expected_type = getattr(py_builtins, type_name)
            if isinstance(expected_type, type):
                return isinstance(obj, expected_type)
        except TypeError as e:
            log_exception(
                f"{operation} - builtin check for '{type_name}'",
                e,
                level='debug'
            )
            return False
    
    # Check common type aliases
    type_aliases = {
        'string': str, 'str': str,
        'integer': int, 'int': int,
        'float': float, 'double': float,
        'boolean': bool, 'bool': bool,
        'list': list, 'array': list,
        'dict': dict, 'dictionary': dict,
        'tuple': tuple,
        'set': set,
    }
    
    type_lower = type_name.lower()
    if type_lower in type_aliases:
        return isinstance(obj, type_aliases[type_lower])
    
    # Type not found
    logger.debug(f"Type '{type_name}' not found in {operation}")
    return False


def check_parameter_type(param_value: Any, type_name: str, param_name: str,
                        type_registry: dict, function_name: str = "") -> bool:
    """
    Check if a parameter value matches the expected type
    
    Args:
        param_value: The parameter value to check
        type_name: Expected type name
        param_name: Name of the parameter
        type_registry: Registry of custom types
        function_name: Name of the function (for error messages)
        
    Returns:
        True if type matches, False otherwise
        
    Raises:
        TypeError: If type validation fails and strict mode is enabled
    """
    operation = f"parameter type check for '{param_name}'"
    if function_name:
        operation += f" in function '{function_name}'"
    
    # Check in type registry
    if type_name in type_registry:
        try:
            expected_type = type_registry[type_name]
            if isinstance(expected_type, type) and not isinstance(param_value, expected_type):
                logger.warning(
                    f"Parameter '{param_name}' expected type '{type_name}' "
                    f"but got '{type(param_value).__name__}'"
                )
                return False
        except TypeError as e:
            log_exception(operation, e, level='debug')
            return False
    
    # Check in Python builtins
    elif hasattr(py_builtins, type_name):
        try:
            expected_type = getattr(py_builtins, type_name)
            if isinstance(expected_type, type) and not isinstance(param_value, expected_type):
                logger.warning(
                    f"Parameter '{param_name}' expected type '{type_name}' "
                    f"but got '{type(param_value).__name__}'"
                )
                return False
        except TypeError as e:
            log_exception(operation, e, level='debug')
            return False
    
    return True


def check_return_type(return_value: Any, type_name: str, type_registry: dict,
                     function_name: str = "") -> bool:
    """
    Check if a return value matches the expected type
    
    Args:
        return_value: The return value to check
        type_name: Expected type name
        type_registry: Registry of custom types
        function_name: Name of the function (for error messages)
        
    Returns:
        True if type matches, False otherwise
    """
    operation = f"return type check"
    if function_name:
        operation += f" for function '{function_name}'"
    
    # Check in type registry
    if type_name in type_registry:
        try:
            expected_type = type_registry[type_name]
            if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                logger.warning(
                    f"Return value expected type '{type_name}' "
                    f"but got '{type(return_value).__name__}'"
                )
                return False
        except TypeError as e:
            log_exception(operation, e, level='debug')
            return False
    
    # Check in Python builtins
    elif hasattr(py_builtins, type_name):
        try:
            expected_type = getattr(py_builtins, type_name)
            if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                logger.warning(
                    f"Return value expected type '{type_name}' "
                    f"but got '{type(return_value).__name__}'"
                )
                return False
        except TypeError as e:
            log_exception(operation, e, level='debug')
            return False
    
    return True


def get_type_from_registry(type_name: str, type_registry: dict) -> Optional[Type]:
    """
    Get a type from the registry or builtins
    
    Args:
        type_name: Name of the type to retrieve
        type_registry: Registry of custom types
        
    Returns:
        The type object if found, None otherwise
    """
    # Check type registry
    if type_name in type_registry:
        try:
            expected_type = type_registry[type_name]
            if isinstance(expected_type, type):
                return expected_type
        except TypeError as e:
            log_exception(f"get type '{type_name}' from registry", e, level='debug')
    
    # Check Python builtins
    if hasattr(py_builtins, type_name):
        try:
            expected_type = getattr(py_builtins, type_name)
            if isinstance(expected_type, type):
                return expected_type
        except TypeError as e:
            log_exception(f"get type '{type_name}' from builtins", e, level='debug')
    
    return None


def is_valid_type_name(type_name: str, type_registry: dict) -> bool:
    """
    Check if a type name is valid (exists in registry or builtins)
    
    Args:
        type_name: Name of the type to check
        type_registry: Registry of custom types
        
    Returns:
        True if type name is valid, False otherwise
    """
    return get_type_from_registry(type_name, type_registry) is not None