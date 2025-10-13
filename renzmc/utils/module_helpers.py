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
Module Helper Utilities for RenzmcLang
Provides reusable module import and requirement checking functions
"""
import importlib  # noqa: E402
import sys  # noqa: E402
from typing import Any, List, Optional  # noqa: E402

from renzmc.utils.error_handler import (  # noqa: E402
    handle_import_error,
    log_exception,
    logger,
)


def require_module(
    module_name: str,
    operation: str = "module operation",
    raise_on_missing: bool = False,
) -> Optional[Any]:
    """
    Safely import and return a module

    Args:
        module_name: Name of the module to import
        operation: Description of the operation requiring the module
        raise_on_missing: Whether to raise ImportError if module not found

    Returns:
        The imported module or None if not available

    Raises:
        ImportError: If raise_on_missing is True and module not found
    """
    try:
        return importlib.import_module(module_name)
    except ImportError:
        handle_import_error(
            module_name,
            operation,
            fallback_action=(
                "Continuing without this module" if not raise_on_missing else None
            ),
        )
        if raise_on_missing:
            raise
        return None


def check_module_available(module_name: str) -> bool:
    """
    Check if a module is available for import

    Args:
        module_name: Name of the module to check

    Returns:
        True if module is available, False otherwise
    """
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def get_module_attribute(module: Any, attr_name: str, default: Any = None) -> Any:
    """
    Safely get an attribute from a module

    Args:
        module: The module object
        attr_name: Name of the attribute to get
        default: Default value if attribute not found

    Returns:
        The attribute value or default
    """
    try:
        return getattr(module, attr_name, default)
    except AttributeError:
        logger.debug(
            f"Attribute '{attr_name}' not found in module "
            f"'{getattr(module, '__name__', 'unknown')}'"
        )
        return default


def import_submodule(
    parent_module: Any, submodule_name: str, operation: str = "submodule import"
) -> Optional[Any]:
    """
    Import a submodule from a parent module

    Args:
        parent_module: The parent module object
        submodule_name: Name of the submodule
        operation: Description of the operation

    Returns:
        The submodule or None if not available
    """
    try:
        parent_name = getattr(parent_module, "__name__", "")
        full_name = f"{parent_name}.{submodule_name}" if parent_name else submodule_name
        return importlib.import_module(full_name)
    except ImportError:
        handle_import_error(
            f"{parent_name}.{submodule_name}",
            operation,
            fallback_action="Submodule not available",
        )
        return None


def ensure_modules(module_names: List[str], operation: str = "operation") -> dict:
    """
    Ensure multiple modules are available

    Args:
        module_names: List of module names to check
        operation: Description of the operation requiring modules

    Returns:
        Dictionary mapping module names to module objects (or None if unavailable)
    """
    modules = {}
    for name in module_names:
        modules[name] = require_module(name, operation, raise_on_missing=False)

    return modules


def get_module_version(module_name: str) -> Optional[str]:
    """
    Get the version of an installed module

    Args:
        module_name: Name of the module

    Returns:
        Version string or None if not available
    """
    try:
        module = importlib.import_module(module_name)
        return getattr(module, "__version__", None)
    except (ImportError, AttributeError):
        return None


def reload_module(module_name: str) -> Optional[Any]:
    """
    Reload a module

    Args:
        module_name: Name of the module to reload

    Returns:
        The reloaded module or None if failed
    """
    try:
        if module_name in sys.modules:
            return importlib.reload(sys.modules[module_name])
        else:
            return importlib.import_module(module_name)
    except (ImportError, Exception) as e:
        log_exception(f"reload module '{module_name}'", e, level="warning")
        return None
