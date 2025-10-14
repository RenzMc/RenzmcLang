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

from functools import wraps
from typing import Any, Callable

from renzmc.utils.logging import logger


class RecursionGuard:

    def __init__(self, max_depth: int = 1000):
        self.max_depth = max_depth
        self.current_depth = 0

    def check(self):
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            raise RecursionError(
                f"⚠️ Kedalaman rekursi maksimum tercapai: {self.max_depth}\nKode Anda mungkin terlalu kompleks atau memiliki struktur nested yang terlalu dalam.\nPertimbangkan untuk menyederhanakan struktur kode atau mengurangi tingkat nested."
            )
        logger.debug(f"Recursion depth: {self.current_depth}/{self.max_depth}")

    def release(self):
        if self.current_depth > 0:
            self.current_depth -= 1

    def reset(self):
        self.current_depth = 0

    def __enter__(self):
        self.check()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False


def with_recursion_guard(max_depth: int = 1000):

    def decorator(func: Callable) -> Callable:
        guard = RecursionGuard(max_depth)

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with guard:
                return func(*args, **kwargs)

        wrapper._recursion_guard = guard
        return wrapper

    return decorator
