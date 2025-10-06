from functools import wraps
import time
from collections import defaultdict
from threading import Lock
from typing import Callable, Any


class RateLimiter:

    def __init__(self, max_calls: int = 100, period: int = 60):
        self.max_calls = max_calls
        self.period = period
        self.calls = defaultdict(list)
        self.lock = Lock()

    def __call__(self, func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with self.lock:
                now = time.time()
                key = func.__name__
                self.calls[key] = [
                    call_time
                    for call_time in self.calls[key]
                    if now - call_time < self.period
                ]
                if len(self.calls[key]) >= self.max_calls:
                    raise RuntimeError(
                        f"⚠️ Rate limit tercapai untuk '{func.__name__}'\nMaksimum: {self.max_calls} panggilan per {self.period} detik\nSilakan tunggu beberapa saat sebelum mencoba lagi."
                    )
                self.calls[key].append(now)
            return func(*args, **kwargs)

        return wrapper

    def reset(self, func_name: str = None):
        with self.lock:
            if func_name:
                self.calls[func_name] = []
            else:
                self.calls.clear()


http_rate_limiter = RateLimiter(max_calls=100, period=60)
file_rate_limiter = RateLimiter(max_calls=1000, period=60)
