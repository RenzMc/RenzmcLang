from typing import Callable, Any
from functools import wraps
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
