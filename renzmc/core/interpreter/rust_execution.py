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
from typing import Any, Dict, Optional

from renzmc.core.ast import Program, Block
from renzmc.core.ast_serializer import ast_to_json
from renzmc.core.rust_integration import get_rust_integration


class RustExecutionMixin:
    """
    Mixin class for Rust execution integration.

    This mixin provides methods to execute RenzmcLang code using the
    Rust Virtual Machine for improved performance while maintaining
    full compatibility with the existing Python implementation.
    """

    def __init__(self):
        """
        Initialize Rust execution components.
        """
        super().__init__()
        self._rust_integration = get_rust_integration()
        # Otomatis enable Rust jika tersedia
        self._use_rust = self._rust_integration.is_rust_enabled
        self._rust_fallback_enabled = True

        # Track execution statistics
        self._rust_executions = 0
        self._python_executions = 0
        self._rust_failures = 0

    def _ensure_rust_initialized(self):
        """Ensure Rust integration is properly initialized."""
        if not hasattr(self, "_rust_integration"):
            self._rust_integration = get_rust_integration()
            # Otomatis enable Rust jika tersedia
            self._use_rust = self._rust_integration.is_rust_enabled
            self._rust_fallback_enabled = True
            self._rust_executions = 0
            self._python_executions = 0
            self._rust_failures = 0

    def _auto_enable_rust(self) -> bool:
        """
        Automatically enable Rust execution if available.

        Returns:
            True if Rust is enabled, False otherwise
        """
        self._ensure_rust_initialized()

        if self._rust_integration.is_rust_enabled:
            self._use_rust = True
            return True
        else:
            self._use_rust = False
            return False

    def is_rust_execution_enabled(self) -> bool:
        """
        Check if Rust execution is enabled (automatic based on availability).

        Returns:
            True if Rust execution is enabled, False otherwise
        """
        self._ensure_rust_initialized()
        return self._use_rust

    def get_rust_info(self) -> Dict[str, Any]:
        """
        Get information about Rust components.

        Returns:
            Dictionary with Rust component information
        """
        self._ensure_rust_initialized()

        return {
            "rust_info": self._rust_integration.rust_info,
            "rust_enabled": self._use_rust,
            "rust_executions": self._rust_executions,
            "python_executions": self._python_executions,
            "rust_failures": self._rust_failures,
            "success_rate": (
                self._rust_executions / (self._rust_executions + self._rust_failures)
                if (self._rust_executions + self._rust_failures) > 0
                else 0.0
            ),
        }

    def _should_use_rust(self, ast_node) -> bool:
        """
        Determine if Rust execution should be used for this AST.

        Args:
            ast_node: The AST node to evaluate

        Returns:
            True if Rust should be used, False otherwise
        """
        # Auto-initialize Rust if not already done
        if not hasattr(self, "_rust_integration"):
            self._auto_enable_rust()
            return False

        if not self._use_rust:
            return False

        if not self._rust_integration.is_rust_enabled:
            return False

        # Check if this is a supported node type for Rust
        if isinstance(ast_node, (Program, Block)):
            return True

        # For now, try Rust for most statement types
        return True

    def _execute_with_rust(self, ast_node) -> Any:
        """
        Execute AST node using Rust VM.

        Args:
            ast_node: The AST node to execute

        Returns:
            Result of execution

        Raises:
            Exception: If Rust execution fails and fallback is disabled
        """
        try:
            # Convert AST to JSON
            ast_json = ast_to_json(ast_node)

            # Get current global variables
            globals_dict = self._get_global_variables_for_rust()

            # Execute with Rust
            result = self._rust_integration.compile_and_execute(ast_json, globals_dict)

            if result is not None:
                self._rust_executions += 1

                # Update local variables from Rust VM if needed
                self._update_variables_from_rust()

                return result

        except Exception as e:
            self._rust_failures += 1
            warnings.warn(f"Rust execution failed: {e}")

            if not self._rust_fallback_enabled:
                raise

        # Fallback to Python execution
        return None

    def _get_global_variables_for_rust(self) -> Dict[str, Any]:
        """
        Get current global variables for Rust VM.

        Returns:
            Dictionary of global variables
        """
        globals_dict = {}

        if hasattr(self, "GLOBAL_SCOPE"):
            for name, value in self.GLOBAL_SCOPE.items():
                # Filter out non-serializable objects
                try:
                    json.dumps(value, default=str)  # Test serializability
                    globals_dict[name] = value
                except (TypeError, ValueError):
                    # Skip non-serializable objects
                    pass

        return globals_dict

    def _update_variables_from_rust(self):
        """
        Update Python variables from Rust VM state.
        """
        if not self._rust_integration.is_rust_enabled:
            return

        # This is a placeholder for future implementation
        # Currently, variables are primarily managed in Python
        pass

    def visit_with_rust(self, ast_node) -> Any:
        """
        Visit AST node with Rust execution fallback.

        This method attempts to execute the AST using Rust VM,
        and falls back to Python execution if Rust fails.

        Args:
            ast_node: The AST node to visit

        Returns:
            Result of execution
        """
        # Try Rust execution first
        if self._should_use_rust(ast_node):
            rust_result = self._execute_with_rust(ast_node)
            if rust_result is not None:
                return rust_result

        # Fall back to Python execution
        self._python_executions += 1
        return self._visit_python_fallback(ast_node)

    def _visit_python_fallback(self, ast_node) -> Any:
        """
        Execute AST using Python fallback.

        Args:
            ast_node: The AST node to execute

        Returns:
            Result of execution
        """
        # Import the base visitor and use its visit method directly
        from renzmc.core.base_visitor import NodeVisitor

        return NodeVisitor.visit(self, ast_node)

    def execute_program_with_rust(self, statements: list) -> Any:
        """
        Execute a program using Rust when possible.

        Args:
            statements: List of statements to execute

        Returns:
            Result of execution
        """
        program = Program(statements)
        return self.visit_with_rust(program)

    def execute_block_with_rust(self, statements: list) -> Any:
        """
        Execute a block using Rust when possible.

        Args:
            statements: List of statements to execute

        Returns:
            Result of execution
        """
        block = Block(statements)
        return self.visit_with_rust(block)

    def benchmark_execution(self, ast_node, iterations: int = 100) -> Dict[str, float]:
        """
        Benchmark Rust vs Python execution for an AST node.

        Args:
            ast_node: The AST node to benchmark
            iterations: Number of iterations to run

        Returns:
            Dictionary with timing results
        """
        import time

        results = {}

        # Benchmark Python execution
        if self._rust_fallback_enabled:
            start_time = time.time()
            for _ in range(iterations):
                self._visit_python_fallback(ast_node)
            python_time = time.time() - start_time
            results["python_time"] = python_time

        # Benchmark Rust execution
        if self._rust_integration.is_rust_enabled:
            start_time = time.time()
            for _ in range(iterations):
                self._execute_with_rust(ast_node)
            rust_time = time.time() - start_time
            results["rust_time"] = rust_time

            if "python_time" in results:
                results["speedup"] = python_time / rust_time if rust_time > 0 else float("inf")

        results["iterations"] = iterations
        return results

    def clear_rust_stats(self):
        """Clear execution statistics."""
        self._rust_executions = 0
        self._python_executions = 0
        self._rust_failures = 0

    def set_rust_fallback_enabled(self, enabled: bool):
        """
        Enable or disable fallback to Python execution.

        Args:
            enabled: Whether to enable fallback
        """
        self._rust_fallback_enabled = enabled

    def is_rust_fallback_enabled(self) -> bool:
        """
        Check if Rust fallback to Python is enabled.

        Returns:
            True if fallback is enabled, False otherwise
        """
        return self._rust_fallback_enabled

    def get_performance_stats(self) -> Optional[str]:
        """
        Get performance statistics from Rust VM.

        Returns:
            JSON string with performance stats or None if not available
        """
        return self._rust_integration.get_performance_stats()

    def clear_rust_vm(self) -> bool:
        """
        Clear the Rust VM state.

        Returns:
            True if successful, False otherwise
        """
        return self._rust_integration.clear_vm()


__all__ = ["RustExecutionMixin"]
