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




import uuid

from renzmc.utils.error_handler import log_exception
from renzmc.utils.module_helpers import import_submodule, require_module


class UtilityMixin:
    """
    Mixin class for utility functionality.

    Provides helper methods for safe operations and utilities.
    """

    def _safe_import_module(self, module_name, operation="module import"):
        """
        Safely import a module with proper error handling

        Args:
            module_name: Name of the module to import
            operation: Description of the operation

        Returns:
            The imported module or None if not available
        """
        return require_module(module_name, operation, raise_on_missing=False)

    def _safe_import_submodule(self, parent_module, submodule_name, operation="submodule import"):
        """
        Safely import a submodule with proper error handling

        Args:
            parent_module: The parent module object
            submodule_name: Name of the submodule
            operation: Description of the operation

        Returns:
            The submodule or None if not available
        """
        return import_submodule(parent_module, submodule_name, operation)

    def _safe_isinstance(self, obj, type_obj):
        """
        Safely check isinstance with proper error handling

        Args:
            obj: Object to check
            type_obj: Type to check against

        Returns:
            bool: True if isinstance check passes, False on error
        """
        try:
            return isinstance(obj, type_obj)
        except TypeError as e:
            log_exception("isinstance check", e, level="debug")
            return False

    def _call_magic_method(self, obj, method_name, *args):
        """
        Call a magic method on an object safely.

        Args:
            obj: The object
            method_name: Name of the magic method
            *args: Arguments to pass to the method

        Returns:
            The result of the method call or NotImplemented
        """
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                try:
                    result = method(*args)
                    if result is not NotImplemented:
                        return result
                except (TypeError, ValueError, AttributeError) as e:
                    from renzmc.utils.logging import logger

                    logger.debug(f"Magic method {method_name} failed: {e}")
                except Exception as e:
                    from renzmc.utils.logging import logger

                    logger.error(
                        f"Unexpected error in magic method {method_name}: {e}",
                        exc_info=True,
                    )
                    raise
        return NotImplemented

    def _set_safe_mode(self, enabled=True):
        """
        Enable or disable safe mode.

        Args:
            enabled: Whether to enable safe mode

        Returns:
            The enabled state
        """
        self.safe_mode = enabled
        mode_text = "diaktifkan" if enabled else "dinonaktifkan"
        print(f"🔒 Mode aman {mode_text}")
        return enabled

    def _check_safe_mode(self):
        """
        Check if safe mode is enabled.

        Returns:
            bool: True if safe mode is enabled
        """
        return self.safe_mode

    def _setup_compatibility_adapters(self):
        """Setup compatibility adapters for backward compatibility."""

    def _format_string(self, template, **kwargs):
        """
        Format a string template with keyword arguments.

        Args:
            template: The template string
            **kwargs: Keyword arguments for formatting

        Returns:
            The formatted string
        """
        return template.format(**kwargs)

    def _create_uuid(self):
        """
        Create a new UUID.

        Returns:
            A UUID string
        """
        return str(uuid.uuid4())

    def _smart_getattr(self, obj, attr_name, default=None):
        """
        Smart getattr that works with both Python and RenzmcLang objects.

        Args:
            obj: The object
            attr_name: Attribute name
            default: Default value if attribute not found

        Returns:
            The attribute value or default
        """
        try:
            return getattr(obj, attr_name, default)
        except Exception:
            return default

    def _smart_setattr(self, obj, attr_name, value):
        """
        Smart setattr that works with both Python and RenzmcLang objects.

        Args:
            obj: The object
            attr_name: Attribute name
            value: Value to set

        Returns:
            The set value
        """
        try:
            setattr(obj, attr_name, value)
            return value
        except Exception as e:
            log_exception("setattr", e)
            return None

    def _smart_hasattr(self, obj, attr_name):
        """
        Smart hasattr that works with both Python and RenzmcLang objects.

        Args:
            obj: The object
            attr_name: Attribute name

        Returns:
            bool: True if attribute exists
        """
        try:
            return hasattr(obj, attr_name)
        except Exception:
            return False

    def _get_inline_cache_stats(self):
        """
        Get inline cache statistics.

        Returns:
            Dictionary with cache statistics
        """
        return self.scope_manager.inline_cache.get_stats()

    def _reset_inline_cache(self):
        """
        Reset inline cache statistics.

        Returns:
            Success message
        """
        self.scope_manager.inline_cache.reset_stats()
        return "Statistik cache inline telah direset"

    def _clear_inline_cache(self):
        """
        Clear all inline cache entries.

        Returns:
            Success message
        """
        self.scope_manager.inline_cache.clear()
        return "Cache inline telah dibersihkan"

    def _enable_inline_cache(self):
        """
        Enable inline cache.

        Returns:
            Success message
        """
        self.scope_manager.inline_cache.enable()
        return "Cache inline diaktifkan"

    def _disable_inline_cache(self):
        """
        Disable inline cache.

        Returns:
            Success message
        """
        self.scope_manager.inline_cache.disable()
        return "Cache inline dinonaktifkan"
