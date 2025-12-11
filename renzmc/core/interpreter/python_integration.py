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

import builtins as py_builtins
import importlib

from renzmc.core.error import RenzmcImportError


class PythonIntegrationMixin:
    """
    Mixin class for Python integration functionality.

    Provides methods for importing and interacting with Python modules.
    """

    def _setup_python_builtins(self):
        """Setup Python builtin functions in global scope."""
        for name in dir(py_builtins):
            if not name.startswith("_"):
                self.global_scope[f"py_{name}"] = getattr(py_builtins, name)

    def _import_python_module(self, module_name, alias=None):
        """
        Import a Python module.

        Args:
            module_name: Name of the module to import
            alias: Optional alias for the module

        Returns:
            The imported module

        Raises:
            RenzmcImportError: If import fails
        """
        try:
            wrapped_module = self.python_integration.import_python_module(module_name, alias)
            if alias:
                if isinstance(wrapped_module, dict):
                    self.global_scope[alias] = wrapped_module[alias]
                    return wrapped_module[alias]
                else:
                    self.global_scope[alias] = wrapped_module
                    return wrapped_module
            else:
                module_var_name = module_name.replace(".", "_")
                self.global_scope[module_var_name] = wrapped_module
                return wrapped_module
        except RenzmcImportError as e:
            print(f"❌ Gagal mengimpor modul Python '{module_name}': {str(e)}")
            print(
                f"""💡 Saran: Pastikan modul terinstal dengan 'instal_paket_python("{module_name}")'"""
            )
            raise e
        except Exception as e:
            import_error = RenzmcImportError(
                f"Error tidak terduga saat mengimpor '{module_name}': {str(e)}"
            )
            print(f"❌ {import_error}")
            raise import_error

    def _call_python_function(self, func, *args, **kwargs):
        """
        Call a Python function.

        Args:
            func: The function to call
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The function result
        """
        return self.python_integration.call_python_function(func, *args, **kwargs)

    def _from_python_import(self, module_name, *items):
        """
        Import specific items from a Python module.

        Args:
            module_name: Name of the module
            *items: Items to import

        Returns:
            Dictionary of imported items

        Raises:
            RenzmcImportError: If import fails
        """
        try:
            imported_items = self.python_integration.import_python_module(
                module_name, from_items=list(items)
            )
            for item_name, item_value in imported_items.items():
                enhanced_value = self.python_integration.convert_python_to_renzmc(item_value)
                self.global_scope[item_name] = enhanced_value
            print(f"✓ Berhasil mengimpor {len(imported_items)} item dari modul '{module_name}'")
            return imported_items
        except RenzmcImportError as e:
            print(f"❌ Gagal mengimpor dari modul Python '{module_name}': {str(e)}")
            print("💡 Saran: Periksa nama modul dan item yang akan diimpor")
            raise e
        except Exception as e:
            import_error = RenzmcImportError(
                f"Error tidak terduga saat mengimpor dari '{module_name}': {str(e)}"
            )
            print(f"❌ {import_error}")
            raise import_error

    def _create_python_object(self, class_obj, *args, **kwargs):
        """
        Create a Python object instance.

        Args:
            class_obj: The class to instantiate
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            The created object
        """
        return self.python_integration.create_python_object(class_obj, *args, **kwargs)

    def _list_python_attributes(self, module_name):
        """
        List attributes of a Python module.

        Args:
            module_name: Name of the module

        Returns:
            List of attribute names
        """
        return self.python_integration.list_module_attributes(module_name)

    def _python_help(self, obj):
        """
        Get help for a Python object.

        Args:
            obj: The object to get help for

        Returns:
            Help text
        """
        return self.python_integration.get_python_help(obj)

    def _install_python_package(self, package_name):
        """
        Install a Python package.

        Args:
            package_name: Name of the package to install

        Returns:
            Installation result

        Raises:
            RuntimeError: If safe mode is enabled
        """
        if self.safe_mode:
            raise RuntimeError(
                "🔒 Instalasi paket Python diblokir dalam mode aman. Gunakan `atur_mode_aman(salah)` untuk mengaktifkan (tidak disarankan untuk server)."
            )
        return self.python_integration.install_package(package_name)

    def _auto_import_python(self, module_name):
        """
        Auto-import a Python module on demand.

        Args:
            module_name: Name of the module

        Returns:
            The imported module
        """
        return self.python_integration.auto_import_on_demand(module_name)

    def _convert_to_python(self, obj):
        """
        Convert a RenzmcLang object to Python.

        Args:
            obj: The object to convert

        Returns:
            The converted Python object
        """
        return self.python_integration.convert_renzmc_to_python(obj)

    def _convert_from_python(self, obj):
        """
        Convert a Python object to RenzmcLang.

        Args:
            obj: The object to convert

        Returns:
            The converted RenzmcLang object
        """
        return self.python_integration.convert_python_to_renzmc(obj)

    def _create_smart_wrapper(self, obj):
        """
        Create a smart wrapper for a Python object.

        Args:
            obj: The object to wrap

        Returns:
            The wrapped object
        """
        return self.python_integration.create_smart_wrapper(obj)

    def _import_all_from_python(self, module_name):
        """
        Import all items from a Python module.

        Args:
            module_name: Name of the module

        Returns:
            Import result
        """
        return self.python_integration.enable_star_imports(module_name, self.global_scope)

    def _list_python_modules(self):
        """
        List all available Python modules.

        Returns:
            List of module names
        """
        return self.python_integration.get_all_python_modules()

    def _check_module_available(self, module_name):
        """
        Check if a Python module is available.

        Args:
            module_name: Name of the module

        Returns:
            bool: True if module is available
        """
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            return False

    def _execute_python_code(self, code_string, local_vars=None):
        """
        Execute Python code (disabled for security).

        Args:
            code_string: The code to execute
            local_vars: Local variables

        Raises:
            RuntimeError: Always raises for security
        """
        raise RuntimeError(
            "🔒 Eksekusi kode Python dinamis dinonaktifkan untuk keamanan.\nGunakan fungsi built-in atau impor modul Python secara eksplisit.\nContoh: gunakan 'impor_python &quot;math&quot;' lalu 'panggil_python math.sqrt(16)'"
        )

    def _evaluate_python_expression(self, expression, context=None):
        """
        Evaluate Python expression (disabled for security).

        Args:
            expression: The expression to evaluate
            context: Evaluation context

        Raises:
            RuntimeError: Always raises for security
        """
        raise RuntimeError(
            "🔒 Evaluasi ekspresi Python dinamis dinonaktifkan untuk keamanan.\nGunakan fungsi built-in atau impor modul Python secara eksplisit.\nContoh: gunakan 'impor_python &quot;math&quot;' lalu 'panggil_python math.sqrt(16)'"
        )
