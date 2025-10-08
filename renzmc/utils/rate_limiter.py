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
