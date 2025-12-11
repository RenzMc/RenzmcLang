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

"""
RenzMcLang Library Manager

Module ini mengelola integrasi standard library dengan interpreter RenzMcLang.
Menyediakan fungsi untuk import dan manajemen library.

Classes:
- LibraryManager: Manajer utama untuk library
- LibraryImporter: Handler untuk import statements

Functions:
- import_library: Import library tertentu
- get_libraries: Dapatkan daftar available libraries
- register_library: Register custom library

Usage:
    manager = LibraryManager()
    math_lib = manager.import_library('math')
"""

from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import importlib
import sys


class LibraryManager:
    """
    Manajer untuk RenzMcLang standard library.

    Mengelola loading, caching, dan akses ke library modules.
    """

    def __init__(self):
        self._loaded_libraries: Dict[str, Any] = {}
        self._library_paths = [
            Path(__file__).parent,  # Current library directory
        ]
        self._available_libraries = self._discover_libraries()

    def _discover_libraries(self) -> List[str]:
        """
        Discover semua available libraries.

        Returns:
            List nama library yang available
        """
        libraries = []
        base_path = Path(__file__).parent

        for item in base_path.iterdir():
            if item.is_dir() and (item / "__init__.py").exists():
                libraries.append(item.name)

        return sorted(libraries)

    def import_library(self, library_name: str) -> Any:
        """
        Import library tertentu.

        Args:
            library_name: Nama library yang akan diimport

        Returns:
            Library module object

        Raises:
            ImportError: Jika library tidak ditemukan
            Exception: Jika ada error saat import

        Example:
            manager = LibraryManager()
            math_lib = manager.import_library('math')
            # math_lib.sin(0.5)
        """
        # Check cache
        if library_name in self._loaded_libraries:
            return self._loaded_libraries[library_name]

        # Validate library name
        if library_name not in self._available_libraries:
            raise ImportError(
                f"Library '{library_name}' tidak ditemukan. "
                f"Available: {self._available_libraries}"
            )

        try:
            # Import the library
            module_path = f"renzmc.library.{library_name}"
            module = importlib.import_module(module_path)

            # Cache the module
            self._loaded_libraries[library_name] = module

            return module

        except Exception as e:
            raise ImportError(f"Gagal import library '{library_name}': {str(e)}")

    def import_function(self, library_name: str, function_name: str) -> Any:
        """
        Import fungsi spesifik dari library.

        Args:
            library_name: Nama library
            function_name: Nama fungsi yang akan diimport

        Returns:
            Function object

        Example:
            sin_func = manager.import_function('math', 'sin')
            result = sin_func(0.5)
        """
        library = self.import_library(library_name)

        if not hasattr(library, function_name):
            raise ImportError(
                f"Fungsi '{function_name}' tidak ditemukan di library '{library_name}'"
            )

        return getattr(library, function_name)

    def get_libraries(self) -> List[str]:
        """
        Dapatkan daftar semua available libraries.

        Returns:
            List nama library yang available
        """
        return self._available_libraries.copy()

    def get_loaded_libraries(self) -> List[str]:
        """
        Dapatkan daftar libraries yang sudah di-load.

        Returns:
            List nama library yang sudah di-load
        """
        return list(self._loaded_libraries.keys())

    def reload_library(self, library_name: str) -> Any:
        """
        Reload library yang sudah di-load.

        Args:
            library_name: Nama library yang akan di-reload

        Returns:
            Library module yang sudah di-reload
        """
        if library_name in self._loaded_libraries:
            module = self._loaded_libraries[library_name]
            importlib.reload(module)
            return module
        else:
            return self.import_library(library_name)

    def register_library(self, library_name: str, library_module: Any):
        """
        Register custom library.

        Args:
            library_name: Nama library
            library_module: Module object
        """
        self._loaded_libraries[library_name] = library_module
        if library_name not in self._available_libraries:
            self._available_libraries.append(library_name)

    def get_library_info(self, library_name: str) -> Dict[str, Any]:
        """
        Dapatkan informasi tentang library.

        Args:
            library_name: Nama library

        Returns:
            Dictionary berisi informasi library
        """
        if library_name not in self._available_libraries:
            return {"error": f"Library '{library_name}' tidak ditemukan"}

        library = self.import_library(library_name)

        info = {
            "name": library_name,
            "loaded": library_name in self._loaded_libraries,
            "functions": [],
            "classes": [],
            "constants": [],
            "docstring": getattr(library, "__doc__", ""),
            "version": getattr(library, "__version__", "Unknown"),
            "author": getattr(library, "__author__", "Unknown"),
        }

        # Discover exported items
        if hasattr(library, "__all__"):
            for item_name in library.__all__:
                item = getattr(library, item_name, None)
                if item is not None:
                    if callable(item):
                        info["functions"].append(item_name)
                    elif isinstance(item, type):
                        info["classes"].append(item_name)
                    else:
                        info["constants"].append(item_name)

        return info


class LibraryImporter:
    """
    Handler untuk import statements di RenzMcLang.

    Memproses statement seperti:
    - dari math impor sin, cos
    - impor math
    - dari math impor sin sebagai sinus
    """

    def __init__(self, library_manager: LibraryManager):
        self.library_manager = library_manager

    def process_import_statement(self, statement: str) -> Dict[str, Any]:
        """
        Process import statement.

        Args:
            statement: Import statement string

        Returns:
            Dictionary berisi hasil import

        Example:
            importer = LibraryImporter(manager)
            result = importer.process_import_statement("dari math impor sin, cos")
        """
        statement = statement.strip()

        # Handle "dari X impor A, B" format
        if statement.startswith("dari ") and " impor " in statement:
            return self._process_from_import(statement)

        # Handle "impor X" format
        elif statement.startswith("impor "):
            return self._process_direct_import(statement)

        else:
            raise ValueError(f"Invalid import statement: {statement}")

    def _process_from_import(self, statement: str) -> Dict[str, Any]:
        """
        Process "dari X impor A, B" format.
        """
        # Parse "dari library impor item1, item2"
        parts = statement.split(" impor ", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid from import statement: {statement}")

        from_part = parts[0][5:]  # Remove "dari "
        import_part = parts[1]

        library_name = from_part.strip()
        items = import_part.split(",")

        result = {"type": "from_import", "library": library_name, "imports": {}}

        library = self.library_manager.import_library(library_name)

        for item in items:
            item = item.strip()

            # Handle alias: "sin sebagai sinus"
            if " sebagai " in item:
                func_name, alias = item.split(" sebagai ", 1)
                func_name = func_name.strip()
                alias = alias.strip()
            else:
                func_name = item
                alias = item

            # Get the function/object
            func = getattr(library, func_name, None)
            if func is None:
                raise ImportError(f"'{func_name}' tidak ditemukan di library '{library_name}'")

            result["imports"][alias] = func

        return result

    def _process_direct_import(self, statement: str) -> Dict[str, Any]:
        """
        Process "impor X" format.
        """
        library_name = statement[6:].strip()  # Remove "impor "

        if not library_name:
            raise ValueError("Library name tidak boleh kosong")

        library = self.library_manager.import_library(library_name)

        return {"type": "direct_import", "library": library_name, "module": library}


# Global instance
_library_manager = None


def get_library_manager() -> LibraryManager:
    """
    Dapatkan global library manager instance.

    Returns:
        LibraryManager instance
    """
    global _library_manager
    if _library_manager is None:
        _library_manager = LibraryManager()
    return _library_manager


def import_library(library_name: str) -> Any:
    """
    Import library (shortcut function).

    Args:
        library_name: Nama library

    Returns:
        Library module
    """
    return get_library_manager().import_library(library_name)


def get_available_libraries() -> List[str]:
    """
    Dapatkan daftar available libraries (shortcut function).

    Returns:
        List nama library
    """
    return get_library_manager().get_libraries()


# Indonesian Aliases
manajer_library = get_library_manager
impor_library = import_library
dapatkan_library_tersedia = get_available_libraries

__all__ = [
    "LibraryManager",
    "LibraryImporter",
    "get_library_manager",
    "import_library",
    "get_available_libraries",
    "manajer_library",
    "impor_library",
    "dapatkan_library_tersedia",
]
