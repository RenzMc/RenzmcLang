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
RenzmcLang Interpreter Function Visitors Module

This module contains function visitors methods.
"""

import asyncio
import builtins as py_builtins

from renzmc.core.ast import Var
from renzmc.core.error import (
    AsyncError,
    TypeHintError,
)
from renzmc.utils.error_handler import log_exception

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class FunctionVisitorsMixin:
    """
    Mixin class for function visitors.

    Provides 10 methods for handling function visitors.
    """

    def visit_FuncDecl(self, node):
        name = node.name
        params = node.params
        body = node.body
        return_type = node.return_type
        param_types = node.param_types
        self.functions[name] = (params, body, return_type, param_types)

        # Only enable JIT tracking if function doesn't have manual JIT decorators
        # Manual decorators handle compilation themselves
        if JIT_AVAILABLE:
            has_manual_jit = (hasattr(self, "_jit_hints") and name in self._jit_hints) or (
                hasattr(self, "_jit_force") and name in self._jit_force
            )
            if not has_manual_jit:
                self.jit_call_counts[name] = 0
                self.jit_execution_times[name] = 0.0

        def renzmc_function(*args, **kwargs):
            return self._execute_user_function(name, params, body, return_type, param_types, list(args), kwargs)

        renzmc_function.__name__ = name
        renzmc_function.__renzmc_function__ = True
        self.global_scope[name] = renzmc_function

        # Return the function so decorators can work with it
        return renzmc_function

    def visit_FuncCall(self, node):  # noqa: C901
        # Initialize return_type to avoid UnboundLocal error
        return_type = None

        if hasattr(node, "func_expr") and node.func_expr is not None:
            try:
                func = self.visit(node.func_expr)
                args = [self.visit(arg) for arg in node.args]
                kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
                if callable(func):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        func_name = getattr(func, "__name__", str(type(func).__name__))
                        raise RuntimeError(f"Error dalam pemanggilan fungsi '{func_name}': {str(e)}")
                else:
                    raise RuntimeError(f"Objek '{type(func).__name__}' tidak dapat dipanggil")
            except NameError:
                if isinstance(node.func_expr, Var):
                    func_name = node.func_expr.name
                    args = [self.visit(arg) for arg in node.args]
                    kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
                    if func_name in self.functions:
                        params, body, return_type, param_types = self.functions[func_name]
                        return self._execute_user_function(
                            func_name,
                            params,
                            body,
                            return_type,
                            param_types,
                            args,
                            kwargs,
                        )
                    else:
                        raise NameError(f"Fungsi '{func_name}' tidak ditemukan")
                else:
                    raise
        elif hasattr(node, "name"):
            return_type = None
            name = node.name
            args = [self.visit(arg) for arg in node.args]
            kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
            if name in self.builtin_functions:
                try:
                    return self.builtin_functions[name](*args, **kwargs)
                except Exception as e:
                    raise RuntimeError(f"Error dalam fungsi '{name}': {str(e)}")
            if name in self.classes:
                return self.create_class_instance(name, args)
            if name not in self.functions:
                try:
                    lambda_func = self.get_variable(name)
                    if callable(lambda_func):
                        try:
                            return lambda_func(*args, **kwargs)
                        except Exception as e:
                            raise RuntimeError(f"Error dalam lambda '{name}': {str(e)}")
                except NameError as e:
                    # Name not found - this is expected in some contexts
                    log_exception("name lookup", e, level="debug")
            if hasattr(self, "_decorated_functions") and name in self._decorated_functions:
                decorator_data = self._decorated_functions[name]

                # Check if this is a wrapped function (new style) or decorator+func tuple (old style)  # noqa: E501
                if callable(decorator_data):
                    # New style: decorator_data is the already-wrapped function
                    try:
                        return decorator_data(*args, **kwargs)
                    except Exception as e:
                        raise RuntimeError(f"Error dalam fungsi terdekorasi '{name}': {str(e)}")
                else:
                    # Old style: tuple of (decorator_func, original_func)
                    raw_decorator_func, original_func = decorator_data
                    try:
                        # Check if this is a marker decorator (JIT, GPU, parallel)
                        marker_decorators = {
                            "jit_compile_decorator",
                            "jit_force_decorator",
                            "gpu_decorator",
                            "parallel_decorator",
                        }
                        decorator_name = getattr(raw_decorator_func, "__name__", "")

                        if decorator_name in marker_decorators:
                            # For marker decorators, just call the original function
                            # The decorator has already set the necessary attributes
                            return original_func(*args, **kwargs)
                        else:
                            # For wrapper decorators, call the decorator with function and args  # noqa: E501
                            return raw_decorator_func(original_func, *args, **kwargs)
                    except Exception as e:
                        raise RuntimeError(f"Error dalam fungsi terdekorasi '{name}': {str(e)}")
            if name not in self.functions:
                raise NameError(f"Fungsi '{name}' tidak ditemukan")
            function_data = self.functions[name]
            if len(function_data) == 5 and function_data[4] == "ASYNC":
                params, body, return_type, param_types, _ = function_data

                async def async_coroutine():
                    return self._execute_user_function(name, params, body, return_type, param_types, args, kwargs)

                return async_coroutine()
            else:
                params, body, return_type, param_types = function_data
                return self._execute_user_function(name, params, body, return_type, param_types, args, kwargs)

    def visit_Return(self, node):
        if node.expr:
            self.return_value = self.visit(node.expr)
        else:
            self.return_value = None
        return self.return_value

    def visit_Lambda(self, node):  # noqa: C901
        params = node.params
        body = node.body
        param_types = node.param_types
        return_type = node.return_type

        def lambda_func(*args):
            if len(args) != len(params):
                raise RuntimeError(
                    f"Lambda membutuhkan {len(params)} parameter, tetapi {len(args)} diberikan"  # noqa: E501
                )
            if param_types:
                for i, (arg, type_hint) in enumerate(zip(args, param_types)):
                    type_name = type_hint.type_name
                    if type_name in self.type_registry:
                        expected_type = self.type_registry[type_name]
                        try:
                            if isinstance(expected_type, type) and not isinstance(arg, expected_type):
                                raise TypeHintError(f"Parameter ke-{i + 1} harus bertipe '{type_name}'")
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects  # noqa: E501
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(arg, expected_type):
                                raise TypeHintError(f"Parameter ke-{i + 1} harus bertipe '{type_name}'")
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects  # noqa: E501
                            log_exception("type validation", e, level="debug")
            old_local_scope = self.local_scope.copy()
            self.local_scope = {}
            for i in range(len(params)):
                self.set_variable(params[i], args[i], is_local=True)
            result = self.visit(body)
            if return_type:
                type_name = return_type.type_name
                if type_name in self.type_registry:
                    expected_type = self.type_registry[type_name]
                    try:
                        if isinstance(expected_type, type) and not isinstance(result, expected_type):
                            raise TypeHintError(f"Nilai kembali lambda harus bertipe '{type_name}'")
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(result, expected_type):
                            raise TypeHintError(f"Nilai kembali lambda harus bertipe '{type_name}'")
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
            self.local_scope = old_local_scope
            return result

        return lambda_func

    def visit_Generator(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        old_local_scope = self.local_scope.copy()

        def gen():
            self.local_scope = old_local_scope.copy()
            for item in iterable:
                self.set_variable(var_name, item, is_local=True)
                if node.condition:
                    condition_result = self.visit(node.condition)
                    if not condition_result:
                        continue
                expr_result = self.visit(node.expr)
                yield expr_result

        return gen()

    def visit_Yield(self, node):
        if node.expr:
            value = self.visit(node.expr)
        else:
            value = None
        return value

    def visit_YieldFrom(self, node):
        iterable = self.visit(node.expr)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        return list(iterable)

    def visit_AsyncFuncDecl(self, node):
        name = node.name
        params = node.params
        body = node.body
        return_type = node.return_type
        param_types = node.param_types
        self.async_functions[name] = (params, body, return_type, param_types)
        self.functions[name] = (params, body, return_type, param_types, "ASYNC")

    def visit_AsyncMethodDecl(self, node):
        pass

    def visit_Await(self, node):
        coro = self.visit(node.expr)
        if asyncio.iscoroutine(coro):
            return self.loop.run_until_complete(coro)
        else:
            raise AsyncError(f"Objek '{coro}' bukan coroutine")
