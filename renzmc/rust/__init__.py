#!/usr/bin/env python3

"""
Mock Rust integration for testing without actual Rust compilation.
This will be replaced by the actual compiled Rust module when available.
"""

import warnings
from typing import Any, Dict


def is_available() -> bool:
    """Mock function - returns False until Rust is properly compiled."""
    return False


def version() -> str:
    """Mock function - returns mock version."""
    return "0.1.0-mock"


class MockRenzmcVM:
    """Mock RenzmcVM class for testing without Rust."""
    
    def __init__(self):
        self._globals = {}
        self._stats = {"instructions_executed": 0, "memory_used": 0}
    
    def compile(self, ast_json: str) -> bytes:
        """Mock compile - returns empty bytecode."""
        warnings.warn("Using mock Rust VM - no actual compilation")
        return b"mock_bytecode"
    
    def execute(self, bytecode: bytes, globals_json: str = None) -> Any:
        """Mock execute - returns None."""
        warnings.warn("Using mock Rust VM - no actual execution")
        self._stats["instructions_executed"] += 1
        return None
    
    def compile_and_execute(self, ast_json: str) -> Any:
        """Mock compile and execute - returns None."""
        warnings.warn("Using mock Rust VM - no actual compilation or execution")
        self._stats["instructions_executed"] += 1
        return None
    
    def set_variable(self, name: str, value: Any) -> None:
        """Mock set variable."""
        self._globals[name] = value
    
    def get_variable(self, name: str) -> Any:
        """Mock get variable."""
        return self._globals.get(name)
    
    def clear(self) -> None:
        """Mock clear."""
        self._globals.clear()
        self._stats["instructions_executed"] = 0
    
    def get_stats(self) -> str:
        """Mock get stats."""
        return str(self._stats)


# Mock classes and functions
RenzmcVM = MockRenzmcVM