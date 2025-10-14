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
RenzmcLang Interpreter Module System Module

This module contains RenzmcLang module system functionality.
"""


class RenzmcModulesMixin:
    """
    Mixin class for RenzmcLang module system functionality.

    Provides methods for importing and managing RenzmcLang modules.
    """

    def _import_renzmc_module(self, module_name, alias=None):
        """
        Import a RenzmcLang module.

        Args:
            module_name: Name of the module to import
            alias: Optional alias for the module

        Returns:
            The imported module

        Raises:
            RuntimeError: If import fails
        """
        try:
            module = self.module_manager.load_module(module_name, alias)
            module_var_name = alias or module_name.replace(".", "_")
            self.global_scope[module_var_name] = module
            return module
        except Exception as e:
            raise RuntimeError(f"Error mengimpor modul RenzmcLang '{module_name}': {str(e)}")

    def _import_from_renzmc_module(self, module_name, *items):
        """
        Import specific items from a RenzmcLang module.

        Args:
            module_name: Name of the module
            *items: Items to import

        Returns:
            Dictionary of imported items

        Raises:
            RuntimeError: If import fails
        """
        try:
            imported_items = self.module_manager.import_from_module(module_name, list(items))
            for item_name, item_value in imported_items.items():
                self.global_scope[item_name] = item_value
            return imported_items
        except Exception as e:
            raise RuntimeError(f"Error mengimpor dari modul RenzmcLang '{module_name}': {str(e)}")

    def _import_all_from_renzmc_module(self, module_name):
        """
        Import all items from a RenzmcLang module.

        Args:
            module_name: Name of the module

        Returns:
            Dictionary of imported items

        Raises:
            RuntimeError: If import fails
        """
        try:
            imported_items = self.module_manager.import_all_from_module(module_name)
            for item_name, item_value in imported_items.items():
                if not item_name.startswith("_"):
                    self.global_scope[item_name] = item_value
            return imported_items
        except Exception as e:
            raise RuntimeError(f"Error mengimpor semua dari modul RenzmcLang '{module_name}': {str(e)}")

    def _reload_renzmc_module(self, module_name):
        """
        Reload a RenzmcLang module.

        Args:
            module_name: Name of the module to reload

        Returns:
            The reloaded module

        Raises:
            RuntimeError: If reload fails
        """
        try:
            return self.module_manager.reload_module(module_name)
        except Exception as e:
            raise RuntimeError(f"Error memuat ulang modul RenzmcLang '{module_name}': {str(e)}")

    def _list_renzmc_modules(self):
        """
        List all available RenzmcLang modules.

        Returns:
            List of module names
        """
        return self.module_manager.list_available_modules()

    def _get_renzmc_module_info(self, module_name):
        """
        Get information about a RenzmcLang module.

        Args:
            module_name: Name of the module

        Returns:
            Module information dictionary
        """
        return self.module_manager.get_module_info(module_name)

    def _add_module_search_path(self, path):
        """
        Add a path to the module search paths.

        Args:
            path: Path to add

        Returns:
            bool: True if successful
        """
        try:
            self.module_manager.add_search_path(path)
            return True
        except Exception:
            return False
