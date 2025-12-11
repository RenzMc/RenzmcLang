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

import functools

from renzmc.core.error import RenzmcRuntimeError


class RenzmcDecorator:

    def __init__(self, decorator_func, decorator_args=None, decorator_kwargs=None):
        self.decorator_func = decorator_func
        self.decorator_args = decorator_args or ()
        self.decorator_kwargs = decorator_kwargs or {}
        self.name = getattr(decorator_func, "__name__", "decorator")
        if self.decorator_args or self.decorator_kwargs:
            try:
                self.actual_decorator = self.decorator_func(
                    *self.decorator_args, **self.decorator_kwargs
                )
                if not callable(self.actual_decorator):
                    raise RenzmcRuntimeError(
                        f"Decorator factory '{self.name}' must return a callable"
                    )
            except Exception as e:
                raise RenzmcRuntimeError(
                    f"Error creating decorator '{self.name}' with args: {str(e)}"
                )
        else:
            self.actual_decorator = self.decorator_func

    def __call__(self, func):
        # Marker decorators that just set attributes on the function
        marker_decorators = {
            "jit_compile_decorator",
            "jit_force_decorator",
            "gpu_decorator",
            "parallel_decorator",
        }

        # Wrapper decorators that wrap the function execution
        wrapper_decorators = {
            "profile_decorator",
            "timing_decorator",
            "cache_decorator",
        }

        if self.name in marker_decorators:
            # For marker decorators, just call them with the function
            result = self.actual_decorator(func)
            return result if result is not None else func

        if self.name in wrapper_decorators:
            # For wrapper decorators, they return a wrapped function
            try:
                wrapped = self.actual_decorator(func)
                return wrapped if wrapped is not None else func
            except Exception as e:
                raise RenzmcRuntimeError(f"Error dalam decorator '{self.name}': {str(e)}")

        # For other decorators, use the old behavior
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return self.actual_decorator(func, *args, **kwargs)
            except Exception as e:
                raise RenzmcRuntimeError(f"Error dalam decorator '{self.name}': {str(e)}")

        return wrapper

    def __repr__(self):
        return f"<RenzmcDecorator '{self.name}'>"


class RenzmcContextManager:

    def __init__(self, enter_func, exit_func, name="ContextManager"):
        self.enter_func = enter_func
        self.exit_func = exit_func
        self.name = name
        self.active = False
        self.resource = None

    def __enter__(self):
        try:
            self.active = True
            if self.enter_func:
                self.resource = self.enter_func()
                return self.resource
            return self
        except Exception as e:
            self.active = False
            raise RenzmcRuntimeError(f"Error masuk ke context manager '{self.name}': {str(e)}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.exit_func and self.active:
                self.exit_func(self.resource, exc_type, exc_val, exc_tb)
            return False
        except Exception as e:
            raise RenzmcRuntimeError(f"Error keluar dari context manager '{self.name}': {str(e)}")
        finally:
            self.active = False

    def __repr__(self):
        status = "active" if self.active else "inactive"
        return f"<RenzmcContextManager '{self.name}' ({status})>"


class RenzmcGenerator:

    def __init__(self, generator_func, *args, **kwargs):
        self.generator_func = generator_func
        self.args = args
        self.kwargs = kwargs
        self.generator = None
        self.started = False
        self.finished = False

    def __iter__(self):
        if not self.started:
            self.generator = self.generator_func(*self.args, **self.kwargs)
            self.started = True
        return self

    def __next__(self):
        try:
            if self.finished:
                raise StopIteration
            if not self.started:
                self.generator = self.generator_func(*self.args, **self.kwargs)
                self.started = True
            if self.generator is not None:
                return next(self.generator)
            else:
                raise StopIteration
        except StopIteration:
            self.finished = True
            raise
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam generator: {str(e)}")

    def send(self, value):
        try:
            if not self.started:
                self.generator = self.generator_func(*self.args, **self.kwargs)
                self.started = True
            if self.generator is not None:
                return self.generator.send(value)
            else:
                raise StopIteration
        except StopIteration:
            self.finished = True
            raise
        except Exception as e:
            raise RenzmcRuntimeError(f"Error mengirim nilai ke generator: {str(e)}")

    def close(self):
        if self.generator and self.started:
            try:
                self.generator.close()
            except (StopIteration, GeneratorExit):
                pass
            except Exception as e:
                from renzmc.utils.logging import logger

                logger.warning(f"Error closing generator: {e}")
        self.finished = True

    def __repr__(self):
        status = "finished" if self.finished else "active" if self.started else "ready"
        return f"<RenzmcGenerator ({status})>"


class AsyncFunction:

    def __init__(self, func, name=None):
        self.func = func
        self.name = name or getattr(func, "__name__", "async_function")
        self.is_coroutine = True

    async def __call__(self, *args, **kwargs):
        try:
            if hasattr(self.func, "__call__"):
                result = self.func(*args, **kwargs)
                if hasattr(result, "__await__"):
                    return await result
                return result
            else:
                raise RenzmcRuntimeError(f"'{self.name}' bukan fungsi yang dapat dipanggil")
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam fungsi async '{self.name}': {str(e)}")

    def __repr__(self):
        return f"<AsyncFunction '{self.name}'>"


class AdvancedFeatureManager:

    def __init__(self):
        self.decorators = {}
        self.context_managers = {}
        self.generators = {}
        self.async_functions = {}

    def create_decorator(self, name, decorator_func):
        self.decorators[name] = decorator_func
        return decorator_func

    def create_context_manager(self, name, enter_func=None, exit_func=None):
        context_manager = RenzmcContextManager(enter_func, exit_func, name)
        self.context_managers[name] = context_manager
        return context_manager

    def create_generator(self, name, generator_func, *args, **kwargs):
        generator = RenzmcGenerator(generator_func, *args, **kwargs)
        self.generators[name] = generator
        return generator

    def create_async_function(self, name, func):
        async_func = AsyncFunction(func, name)
        self.async_functions[name] = async_func
        return async_func

    def apply_decorator(self, decorator_name, func):
        if decorator_name not in self.decorators:
            raise RenzmcRuntimeError(f"Decorator '{decorator_name}' tidak ditemukan")
        decorator = self.decorators[decorator_name]
        return decorator(func)

    def get_context_manager(self, name):
        if name not in self.context_managers:
            raise RenzmcRuntimeError(f"Context manager '{name}' tidak ditemukan")
        return self.context_managers[name]

    def list_features(self):
        return {
            "decorators": list(self.decorators.keys()),
            "context_managers": list(self.context_managers.keys()),
            "generators": list(self.generators.keys()),
            "async_functions": list(self.async_functions.keys()),
        }


def timing_decorator(func, *args, **kwargs):
    import time

    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Fungsi '{func.__name__}' selesai dalam {end_time - start_time:.4f} detik")
    return result


def retry_decorator(*decorator_args, **decorator_kwargs):
    if decorator_args:
        max_attempts = decorator_args[0]

        def parameterized_retry_decorator(func, *call_args, **call_kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*call_args, **call_kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
            return None

        return parameterized_retry_decorator
    if decorator_args:
        func = decorator_args[0]
        call_args = decorator_args[1:]
    else:
        raise RenzmcRuntimeError("retry_decorator called without function argument")
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            return func(*call_args, **decorator_kwargs)
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
    return None


def simple_retry_decorator(func, *args, **kwargs):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
    return None


def universal_retry_decorator(*decorator_args, **decorator_kwargs):
    if decorator_args and (not callable(decorator_args[0])):
        max_attempts = decorator_args[0]

        def parameterized_retry_decorator(func, *call_args, **call_kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*call_args, **call_kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
            return None

        return parameterized_retry_decorator
    elif decorator_args and callable(decorator_args[0]):
        func = decorator_args[0]
        call_args = decorator_args[1:]
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                return func(*call_args, **decorator_kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
        return None
    else:
        return simple_retry_decorator


def create_parameterized_retry_decorator(max_attempts):

    def parameterized_retry_decorator(func, *args, **kwargs):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
        return None

    return parameterized_retry_decorator


def create_retry_decorator_with_attempts(attempts):

    def retry_decorator_n(func, *args, **kwargs):
        for attempt in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == attempts - 1:
                    raise e
                print(f"Percobaan {attempt + 1} dari {attempts} gagal, mencoba lagi...")
        return None

    return retry_decorator_n


_GLOBAL_CACHE = {}


def cache_decorator(func, *args, **kwargs):
    func_name = getattr(func, "__name__", str(func))
    try:
        args_str = str(args) if args else ""
        kwargs_str = str(sorted(kwargs.items())) if kwargs else ""
        cache_key = f"{func_name}_{hash(args_str)}_{hash(kwargs_str)}"
    except (TypeError, ValueError) as e:
        from renzmc.utils.logging import logger

        logger.debug(f"Cache key generation failed, using simple key: {e}")
        cache_key = f"{func_name}_{str(args)}_{str(kwargs)}"
    if cache_key in _GLOBAL_CACHE:
        print(f"Cache HIT untuk {func_name} dengan args {args}")
        return _GLOBAL_CACHE[cache_key]
    print(f"Cache MISS untuk {func_name} dengan args {args}")
    result = func(*args, **kwargs)
    _GLOBAL_CACHE[cache_key] = result
    return result


def create_custom_decorator(decorator_name, decorator_func):

    def custom_decorator_wrapper(func, *args, **kwargs):
        try:
            return decorator_func(func, *args, **kwargs)
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam decorator '{decorator_name}': {str(e)}")

    custom_decorator_wrapper.__name__ = decorator_name
    return custom_decorator_wrapper


def web_route_decorator(path_or_func, method="GET"):

    def route_decorator(func, *args, **kwargs):
        if not hasattr(func, "_routes"):
            func._routes = []
        route_info = {
            "path": (path_or_func if isinstance(path_or_func, str) else args[0] if args else "/"),
            "method": method,
            "handler": func,
        }
        func._routes.append(route_info)
        return func(*args, **kwargs)

    if callable(path_or_func):
        return lambda *args, **kwargs: route_decorator(path_or_func, *args, **kwargs)
    return route_decorator


def clear_cache():
    _GLOBAL_CACHE.clear()
    print("Cache global telah dibersihkan")


def get_cache_stats():
    return {
        "cache_size": len(_GLOBAL_CACHE),
        "cached_items": list(_GLOBAL_CACHE.keys()),
    }


def jit_compile_decorator(func):
    """Marker decorator for JIT compilation hint"""
    if callable(func):
        func.__jit_hint__ = True
        func.__jit_compile__ = True
    return func


def jit_force_decorator(func):
    """Marker decorator to force JIT compilation"""
    if callable(func):
        func.__jit_force__ = True
        func.__jit_compile__ = True
    return func


def parallel_decorator(func):
    """Marker decorator for parallel execution"""
    if callable(func):
        func.__parallel__ = True
    return func


def gpu_decorator(func):
    """Marker decorator for GPU acceleration"""
    if callable(func):
        func.__gpu__ = True
    return func


def profile_decorator(func):
    """Profiling decorator that wraps function execution"""
    import time
    import tracemalloc

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        start_memory = tracemalloc.get_traced_memory()[0]

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        end_memory = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()

        execution_time = end_time - start_time
        memory_used = (end_memory - start_memory) / 1024 / 1024

        func_name = getattr(func, "__name__", "anonymous")
        print(f"Profile [{func_name}]:")
        print(f"  Execution Time: {execution_time:.6f} seconds")
        print(f"  Memory Used: {memory_used:.2f} MB")

        return result

    return wrapper


__all__ = [
    "AdvancedFeatureManager",
    "RenzmcDecorator",
    "RenzmcContextManager",
    "RenzmcGenerator",
    "AsyncFunction",
    "timing_decorator",
    "retry_decorator",
    "cache_decorator",
    "create_custom_decorator",
    "web_route_decorator",
    "clear_cache",
    "get_cache_stats",
    "jit_compile_decorator",
    "jit_force_decorator",
    "parallel_decorator",
    "gpu_decorator",
    "profile_decorator",
]
