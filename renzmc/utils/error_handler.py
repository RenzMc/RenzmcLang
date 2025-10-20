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


import logging
from functools import wraps
from typing import Any, Callable, Optional

# Configure logger
logger = logging.getLogger("renzmc.error_handler")
logger.setLevel(logging.DEBUG)

# Create console handler with formatting
if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class ErrorContext:
    """Context manager for error handling with logging"""

    def __init__(
        self,
        operation: str,
        reraise: bool = False,
        default_value: Any = None,
        log_level: str = "warning",
    ):
        """
        Initialize error context

        Args:
            operation: Description of the operation being performed
            reraise: Whether to re-raise the exception after logging
            default_value: Default value to return if exception occurs
            log_level: Logging level ('debug', 'info', 'warning', 'error', 'critical')
        """
        self.operation = operation
        self.reraise = reraise
        self.default_value = default_value
        self.log_level = log_level.lower()
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.exception = exc_val

            # Log the exception with appropriate level
            log_func = getattr(logger, self.log_level, logger.warning)
            log_func(
                f"Exception in {self.operation}: {exc_type.__name__}: {exc_val}",
                exc_info=True,
            )

            if self.reraise:
                return False  # Re-raise the exception
            else:
                return True  # Suppress the exception
        return False


def safe_operation(
    operation_name: str,
    default_value: Any = None,
    log_level: str = "warning",
    reraise: bool = False,
):
    """
    Decorator for safe operation execution with logging

    Args:
        operation_name: Name of the operation for logging
        default_value: Default value to return on exception
        log_level: Logging level for exceptions
        reraise: Whether to re-raise exceptions
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            with ErrorContext(
                operation=f"{operation_name} ({func.__name__})",
                default_value=default_value,
                log_level=log_level,
                reraise=reraise,
            ) as ctx:
                return func(*args, **kwargs)

            # If exception occurred and not re-raised, return default value
            if ctx.exception is not None:
                return default_value

        return wrapper

    return decorator


def log_exception(
    operation: str,
    exception: Exception,
    level: str = "error",
    context: Optional[dict] = None,
):
    """
    Log an exception with context information

    Args:
        operation: Description of the operation that failed
        exception: The exception that occurred
        level: Logging level
        context: Additional context information
    """
    log_func = getattr(logger, level.lower(), logger.error)

    message = f"Exception in {operation}: {type(exception).__name__}: {exception}"
    if context:
        message += f"\nContext: {context}"

    log_func(message, exc_info=True)


def handle_type_error(obj: Any, expected_type: str, operation: str) -> bool:
    """
    Handle TypeError with proper logging

    Args:
        obj: The object being checked
        expected_type: The expected type name
        operation: Description of the operation

    Returns:
        False to indicate type check failed
    """
    logger.debug(f"Type check failed in {operation}: " f"object of type {type(obj).__name__} is not {expected_type}")
    return False


def handle_import_error(module_name: str, operation: str, fallback_action: Optional[str] = None) -> None:
    """
    Handle ImportError with proper logging

    Args:
        module_name: Name of the module that failed to import
        operation: Description of the operation
        fallback_action: Description of fallback action taken
    """
    message = f"Failed to import '{module_name}' in {operation}"
    if fallback_action:
        message += f". {fallback_action}"

    logger.warning(message)


def handle_attribute_error(obj: Any, attr: str, operation: str) -> None:
    """
    Handle AttributeError with proper logging

    Args:
        obj: The object being accessed
        attr: The attribute name
        operation: Description of the operation
    """
    logger.debug(f"Attribute '{attr}' not found on {type(obj).__name__} in {operation}")


def handle_resource_limit_error(resource_name: str, operation: str) -> None:
    """
    Handle resource limit setting errors (common on some platforms)

    Args:
        resource_name: Name of the resource limit
        operation: Description of the operation
    """
    logger.debug(
        f"Could not set resource limit '{resource_name}' in {operation}. "
        f"This is normal on some platforms and can be safely ignored."
    )


def handle_timeout_error(operation: str, timeout: float, cleanup_action: Optional[str] = None) -> None:
    """
    Handle timeout errors with proper logging

    Args:
        operation: Description of the operation that timed out
        timeout: The timeout value
        cleanup_action: Description of cleanup action taken
    """
    message = f"Operation '{operation}' timed out after {timeout} seconds"
    if cleanup_action:
        message += f". {cleanup_action}"

    logger.warning(message)


def create_error_context(operation: str, **kwargs) -> ErrorContext:
    """
    Factory function to create ErrorContext with common defaults

    Args:
        operation: Description of the operation
        **kwargs: Additional arguments for ErrorContext

    Returns:
        ErrorContext instance
    """
    return ErrorContext(operation=operation, **kwargs)
