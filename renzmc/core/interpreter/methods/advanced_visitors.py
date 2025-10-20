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




from renzmc.core.ast import String

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class AdvancedVisitorsMixin:
    """
    Mixin class for advanced visitors.

    Provides 14 methods for handling advanced visitors.
    """

    def visit_IndexAccess(self, node):
        obj = self.visit(node.obj)
        index = self.visit(node.index)
        try:
            return obj[index]
        except (IndexError, KeyError):
            raise IndexError(
                f"Indeks '{index}' di luar jangkauan untuk objek tipe '{type(obj).__name__}'"
            )
        except TypeError:
            raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan")

    def visit_SliceAccess(self, node):
        obj = self.visit(node.obj)
        start = self.visit(node.start) if node.start else None
        end = self.visit(node.end) if node.end else None
        step = self.visit(node.step) if node.step else None
        try:
            return obj[start:end:step]
        except TypeError:
            raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak mendukung slicing")

    def visit_ListComp(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        result = []
        old_local_scope = self.local_scope.copy()
        for item in iterable:
            self.set_variable(var_name, item, is_local=True)
            if node.condition:
                condition_result = self.visit(node.condition)
                if not condition_result:
                    continue
            expr_result = self.visit(node.expr)
            result.append(expr_result)
        self.local_scope = old_local_scope
        return result

    def visit_DictComp(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        result = {}
        old_local_scope = self.local_scope.copy()
        for item in iterable:
            self.set_variable(var_name, item, is_local=True)
            if node.condition:
                condition_result = self.visit(node.condition)
                if not condition_result:
                    continue
            key_result = self.visit(node.key_expr)
            value_result = self.visit(node.value_expr)
            result[key_result] = value_result
        self.local_scope = old_local_scope
        return result

    def visit_SetComp(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        result = set()
        old_local_scope = self.local_scope.copy()
        for item in iterable:
            self.set_variable(var_name, item, is_local=True)
            if node.condition:
                condition_result = self.visit(node.condition)
                if not condition_result:
                    continue
            expr_result = self.visit(node.expr)
            result.add(expr_result)
        self.local_scope = old_local_scope
        return result

    def visit_Decorator(self, node):
        name = node.name
        args = [self.visit(arg) for arg in node.args]
        decorated = self.visit(node.decorated)
        if name in self.advanced_features.decorators:
            raw_decorator_func = self.advanced_features.decorators[name]
            try:
                from renzmc.runtime.advanced_features import RenzmcDecorator

                decorator_instance = RenzmcDecorator(raw_decorator_func, args)
                decorated_function = decorator_instance(decorated)

                # Check if this is a marker decorator
                marker_decorators = {"jit_compile", "jit_force", "gpu", "parallel"}

                if hasattr(node.decorated, "name"):
                    func_name = node.decorated.name

                    # For marker decorators, just set attributes on the function metadata
                    if name in marker_decorators:
                        # Store decorator hints in function metadata
                        if not hasattr(self, "_function_decorators"):
                            self._function_decorators = {}
                        if func_name not in self._function_decorators:
                            self._function_decorators[func_name] = []
                        self._function_decorators[func_name].append(name)

                        # Set attributes directly on the function if it exists
                        if func_name in self.functions:
                            # Mark the function with JIT hints
                            if name == "jit_compile":
                                if not hasattr(self, "_jit_hints"):
                                    self._jit_hints = set()
                                self._jit_hints.add(func_name)
                            elif name == "jit_force":
                                if not hasattr(self, "_jit_force"):
                                    self._jit_force = set()
                                self._jit_force.add(func_name)
                            elif name == "gpu":
                                if not hasattr(self, "_gpu_functions"):
                                    self._gpu_functions = set()
                                self._gpu_functions.add(func_name)
                            elif name == "parallel":
                                if not hasattr(self, "_parallel_functions"):
                                    self._parallel_functions = set()
                                self._parallel_functions.add(func_name)

                        # Don't add to _decorated_functions for marker decorators
                        return decorated_function

                    # For wrapper decorators (like @profile), store the wrapped function
                    self._decorated_functions = getattr(self, "_decorated_functions", {})

                    def original_func_callable(*call_args, **call_kwargs):
                        if func_name in self.functions:
                            params, body, return_type, param_types = self.functions[func_name]
                            return self._execute_user_function(
                                func_name,
                                params,
                                body,
                                return_type,
                                param_types,
                                call_args,
                                call_kwargs,
                            )
                        else:
                            raise NameError(f"Fungsi asli '{func_name}' tidak ditemukan")

                    original_func_callable.__name__ = func_name

                    # Apply the decorator to get the wrapped function
                    wrapped_function = raw_decorator_func(original_func_callable)

                    # Store the wrapped function directly
                    self._decorated_functions[func_name] = wrapped_function
                return decorated_function
            except Exception as e:
                raise RuntimeError(f"Error dalam dekorator '{name}': {str(e)}")
        if name in self.functions:
            try:
                if args:
                    decorator_factory = self._create_user_decorator_factory(name, args)
                    return decorator_factory(decorated)
                else:
                    user_decorator_func = self._create_user_function_wrapper(name)
                    from renzmc.runtime.advanced_features import RenzmcDecorator

                    decorator_instance = RenzmcDecorator(user_decorator_func)
                    return decorator_instance(decorated)
            except Exception as e:
                raise RuntimeError(f"Error dalam dekorator '{name}': {str(e)}")
        if hasattr(self, "decorators") and name in self.decorators:
            decorator_func = self.decorators[name]
            try:
                from renzmc.runtime.advanced_features import RenzmcDecorator

                decorator_instance = RenzmcDecorator(decorator_func, args)
                return decorator_instance(decorated)
            except Exception as e:
                raise RuntimeError(f"Error dalam dekorator '{name}': {str(e)}")
        raise NameError(f"Dekorator '{name}' tidak ditemukan")

    def visit_TypeHint(self, node):
        return node.type_name

    def visit_TypeAlias(self, node):
        self.type_registry[node.name] = node.type_expr
        return None

    def visit_LiteralType(self, node):
        return node

    def visit_TypedDictType(self, node):
        return node

    def visit_FormatString(self, node):
        result = ""
        for part in node.parts:
            if isinstance(part, String):
                result += part.value
            else:
                try:
                    value = self.visit(part)
                    if value is not None:
                        result += str(value)
                    else:
                        result += "None"
                except Exception as e:
                    result += f"<Error: {str(e)}>"
        return result

    def visit_Unpacking(self, node):
        value = self.visit(node.expr)
        if not hasattr(value, "__iter__"):
            raise TypeError(f"Objek tipe '{type(value).__name__}' tidak dapat diiterasi")
        return value

    def visit_ExtendedUnpacking(self, node):
        value = self.visit(node.value)
        if not isinstance(value, (list, tuple)):
            try:
                value = list(value)
            except (TypeError, ValueError) as e:
                self.error(
                    f"Nilai tidak dapat di-unpack: {type(value).__name__} - {e}",
                    node.token,
                )
        starred_index = None
        for i, (name, is_starred) in enumerate(node.targets):
            if is_starred:
                if starred_index is not None:
                    self.error(
                        "Hanya satu target yang dapat menggunakan * dalam unpacking",
                        node.token,
                    )
                starred_index = i
        num_targets = len(node.targets)
        num_values = len(value)
        if starred_index is None:
            if num_targets != num_values:
                self.error(
                    f"Jumlah nilai ({num_values}) tidak sesuai dengan jumlah target ({num_targets})",
                    node.token,
                )
            for (name, _), val in zip(node.targets, value):
                self.current_scope.set(name, val)
        else:
            num_required = num_targets - 1
            if num_values < num_required:
                self.error(
                    f"Tidak cukup nilai untuk unpack (dibutuhkan minimal {num_required}, ada {num_values})",
                    node.token,
                )
            for i in range(starred_index):
                name, _ = node.targets[i]
                self.current_scope.set(name, value[i])
            num_after_starred = num_targets - starred_index - 1
            starred_count = num_values - num_required
            starred_name, _ = node.targets[starred_index]
            starred_values = value[starred_index : starred_index + starred_count]
            self.current_scope.set(starred_name, list(starred_values))
            for i in range(num_after_starred):
                target_index = starred_index + 1 + i
                value_index = starred_index + starred_count + i
                name, _ = node.targets[target_index]
                self.current_scope.set(name, value[value_index])

    def visit_StarredExpr(self, node):
        value = self.visit(node.expr)
        if isinstance(value, (list, tuple)):
            return value
        try:
            return list(value)
        except (TypeError, ValueError) as e:
            self.error(f"Nilai tidak dapat di-unpack: {type(value).__name__} - {e}", node.token)
