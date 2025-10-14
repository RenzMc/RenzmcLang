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

import asyncio
import importlib
import inspect


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def super_impl(*args, **kwargs):
    return super(*args, **kwargs)


def impor_semua_python(module_name):
    pass


def reload_python(module_name):
    pass


def daftar_modul_python():
    pass


def jalankan_python(code_string):
    pass


def is_async_function(func):
    return asyncio.iscoroutinefunction(func)


def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)


def wait_all_async(*coros):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(asyncio.gather(*coros))


def create_async_function(func):
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper


def get_function_signature(func):
    return str(inspect.signature(func))


def get_function_parameters(func):
    sig = inspect.signature(func)
    return [param.name for param in sig.parameters.values()]


def get_function_defaults(func):
    sig = inspect.signature(func)
    defaults = {}
    for param in sig.parameters.values():
        if param.default is not inspect.Parameter.empty:
            defaults[param.name] = param.default
    return defaults


def get_function_annotations(func):
    return func.__annotations__ if hasattr(func, "__annotations__") else {}


def get_function_doc(func):
    return func.__doc__ if hasattr(func, "__doc__") else None


def get_function_source(func):
    try:
        return inspect.getsource(func)
    except (OSError, TypeError):
        return None


def get_function_module(func):
    return func.__module__ if hasattr(func, "__module__") else None


def get_function_name(func):
    return func.__name__ if hasattr(func, "__name__") else None


def get_function_qualname(func):
    return func.__qualname__ if hasattr(func, "__qualname__") else None


def get_function_globals(func):
    return func.__globals__ if hasattr(func, "__globals__") else None


def get_function_closure(func):
    return func.__closure__ if hasattr(func, "__closure__") else None


def get_function_code(func):
    return func.__code__ if hasattr(func, "__code__") else None


def cek_modul_python_impl(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def path_modul_python_impl(module_name):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "__file__"):
            return module.__file__
        return None
    except ImportError:
        raise ImportError(f"Modul '{module_name}' tidak ditemukan")


def versi_modul_python_impl(module_name):
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "__version__"):
            return module.__version__
        return None
    except ImportError:
        raise ImportError(f"Modul '{module_name}' tidak ditemukan")


def evaluasi_python_impl(expression):
    try:
        return eval(expression)
    except Exception as e:
        raise Exception(f"Error evaluasi Python: {e}")


def eksekusi_python_impl(code):
    try:
        exec(code)
        return True
    except Exception as e:
        raise Exception(f"Error eksekusi Python: {e}")


super_func = RenzmcBuiltinFunction(super_impl, "super")
cek_modul_python = RenzmcBuiltinFunction(cek_modul_python_impl, "cek_modul_python")
path_modul_python = RenzmcBuiltinFunction(path_modul_python_impl, "path_modul_python")
versi_modul_python = RenzmcBuiltinFunction(versi_modul_python_impl, "versi_modul_python")
evaluasi_python = RenzmcBuiltinFunction(evaluasi_python_impl, "evaluasi_python")
eksekusi_python = RenzmcBuiltinFunction(eksekusi_python_impl, "eksekusi_python")
