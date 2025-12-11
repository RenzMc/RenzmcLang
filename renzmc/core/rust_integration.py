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

import json
import warnings
from typing import Any, Dict, List, Optional, Union

try:
    try:
        import renzmc_vm

        RenzmcVM = renzmc_vm.RenzmcVM

        def is_available():
            return True

        version = renzmc_vm.version
        rust_version = renzmc_vm.version()
    except ImportError:
        from ..rust.renzmc_vm import RenzmcVM, is_available, version as rust_version
    RUST_AVAILABLE = True
except ImportError:
    try:
        from ..rust import RenzmcVM, is_available, version

        rust_version = version()
        RUST_AVAILABLE = True
    except ImportError:
        warnings.warn("Rust components not available. Falling back to Python implementation.")
        RUST_AVAILABLE = False
        RenzmcVM = None
        rust_version = "0.0.0"


class RustIntegration:
    """
    Integration layer for Rust VM and compiler components.

    This class provides a Python interface to the Rust Virtual Machine
    and bytecode compiler, enabling high-performance execution of
    RenzmcLang code.
    """

    def __init__(self, enable_rust: bool = True):
        """
        Initialize Rust integration.

        Args:
            enable_rust: Whether to use Rust components if available
        """
        self.enable_rust = enable_rust and RUST_AVAILABLE
        self._rust_vm = None

        if self.enable_rust:
            try:
                self._rust_vm = RenzmcVM()
            except Exception as e:
                warnings.warn(f"Failed to initialize Rust VM: {e}")
                self.enable_rust = False

    @property
    def is_rust_enabled(self) -> bool:
        """Check if Rust components are enabled and available."""
        return self.enable_rust and self._rust_vm is not None

    @property
    def rust_info(self) -> Dict[str, Any]:
        """Get information about Rust components."""
        return {
            "available": RUST_AVAILABLE,
            "enabled": self.is_rust_enabled,
            "version": (
                version()
                if RUST_AVAILABLE and callable(version)
                else str(version) if RUST_AVAILABLE else None
            ),
        }

    def compile_to_bytecode(self, ast_json: str) -> Optional[bytes]:
        """
        Compile AST to bytecode using Rust compiler.

        Args:
            ast_json: JSON representation of the AST

        Returns:
            Compiled bytecode or None if Rust is not available
        """
        if not self.is_rust_enabled:
            return None

        try:
            return self._rust_vm.compile(ast_json)
        except Exception as e:
            warnings.warn(f"Rust compilation failed: {e}")
            return None

    def execute_bytecode(
        self, bytecode: bytes, globals_dict: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Execute bytecode using Rust VM.

        Args:
            bytecode: Compiled bytecode to execute
            globals_dict: Global variables to set before execution

        Returns:
            Result of execution or None if Rust is not available
        """
        if not self.is_rust_enabled:
            return None

        try:
            if globals_dict:
                globals_json = json.dumps(globals_dict, default=str)
                return self._rust_vm.execute(bytecode, globals_json)
            else:
                return self._rust_vm.execute(bytecode)
        except Exception as e:
            warnings.warn(f"Rust execution failed: {e}")
            return None

    def compile_and_execute(
        self, ast_json: str, globals_dict: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Compile AST to bytecode and execute it using Rust VM.

        Args:
            ast_json: JSON representation of the AST
            globals_dict: Global variables to set before execution

        Returns:
            Result of execution or None if Rust is not available
        """
        if not self.is_rust_enabled:
            return None

        try:
            if globals_dict:
                # Set global variables first
                for name, value in globals_dict.items():
                    self._rust_vm.set_variable(name, value)

            return self._rust_vm.compile_and_execute(ast_json)
        except Exception as e:
            warnings.warn(f"Rust compile and execute failed: {e}")
            return None

    def set_variable(self, name: str, value: Any) -> bool:
        """
        Set a variable in the Rust VM.

        Args:
            name: Variable name
            value: Variable value

        Returns:
            True if successful, False otherwise
        """
        if not self.is_rust_enabled:
            return False

        try:
            self._rust_vm.set_variable(name, value)
            return True
        except Exception as e:
            warnings.warn(f"Failed to set variable in Rust VM: {e}")
            return False

    def get_variable(self, name: str) -> Any:
        """
        Get a variable from the Rust VM.

        Args:
            name: Variable name

        Returns:
            Variable value or None if not found or Rust is not available
        """
        if not self.is_rust_enabled:
            return None

        try:
            return self._rust_vm.get_variable(name)
        except Exception as e:
            warnings.warn(f"Failed to get variable from Rust VM: {e}")
            return None

    def clear_vm(self) -> bool:
        """
        Clear the Rust VM state.

        Returns:
            True if successful, False otherwise
        """
        if not self.is_rust_enabled:
            return False

        try:
            self._rust_vm.clear()
            return True
        except Exception as e:
            warnings.warn(f"Failed to clear Rust VM: {e}")
            return False

    def get_performance_stats(self) -> Optional[str]:
        """
        Get performance statistics from Rust VM.

        Returns:
            JSON string with performance stats or None if Rust is not available
        """
        if not self.is_rust_enabled:
            return None

        try:
            return self._rust_vm.get_stats()
        except Exception as e:
            warnings.warn(f"Failed to get Rust VM stats: {e}")
            return None


# Global instance for Rust integration
_rust_integration = None


def get_rust_integration() -> RustIntegration:
    """
    Get the global Rust integration instance.

    Returns:
        RustIntegration instance
    """
    global _rust_integration
    if _rust_integration is None:
        _rust_integration = RustIntegration()
    return _rust_integration


def is_rust_available() -> bool:
    """
    Check if Rust components are available.

    Returns:
        True if Rust is available, False otherwise
    """
    return RUST_AVAILABLE


def get_rust_version() -> str:
    """
    Get the Rust component version.

    Returns:
        Version string
    """
    return rust_version if RUST_AVAILABLE else "Not available"


__all__ = ["RustIntegration", "get_rust_integration", "is_rust_available", "get_rust_version"]
