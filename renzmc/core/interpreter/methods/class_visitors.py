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

import builtins as py_builtins
import importlib

from renzmc.core.ast import (
    Block,
    Constructor,
    MethodDecl,
    VarDecl,
)
from renzmc.core.error import TypeHintError
from renzmc.utils.error_handler import handle_import_error, log_exception

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class ClassVisitorsMixin:
    """
    Mixin class for class visitors.

    Provides 9 methods for handling class visitors.
    """

    def visit_ClassDecl(self, node):
        name = node.name
        methods = {}
        constructor = None
        parent = node.parent
        class_vars = {}
        for var_decl in node.class_vars:
            if isinstance(var_decl, VarDecl):
                var_name = var_decl.var_name
                value = self.visit(var_decl.value)
                class_vars[var_name] = value
        for method in node.methods:
            if isinstance(method, MethodDecl):
                methods[method.name] = (
                    method.params,
                    method.body,
                    method.return_type,
                    method.param_types,
                )
            elif isinstance(method, Constructor):
                constructor = (method.params, method.body, method.param_types)
        self.classes[name] = {
            "methods": methods,
            "constructor": constructor,
            "parent": parent,
            "class_vars": class_vars,
        }

    def visit_MethodDecl(self, node):
        pass

    def visit_Constructor(self, node):
        pass

    def visit_AttributeRef(self, node):
        obj = self.visit(node.obj)
        attr = node.attr
        if id(obj) in self.instance_scopes:
            instance_scope = self.instance_scopes[id(obj)]
            if attr in instance_scope:
                return instance_scope[attr]
            else:
                raise AttributeError(f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'")
        elif hasattr(obj, attr):
            return getattr(obj, attr)
        elif isinstance(obj, dict) and attr in obj:
            return obj[attr]
        else:
            if hasattr(obj, "__name__") and hasattr(obj, "__package__") and (not isinstance(obj, dict)):
                try:
                    submodule_name = f"{obj.__name__}.{attr}"
                    submodule = importlib.import_module(submodule_name)
                    setattr(obj, attr, submodule)
                    return submodule
                except ImportError:
                    # Module not available - continuing without it
                    handle_import_error("module", "import operation", "Continuing without module")
            raise AttributeError(f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'")

    def visit_MethodCall(self, node):
        obj = self.visit(node.obj)
        method = node.method
        args = [self.visit(arg) for arg in node.args]
        if hasattr(obj, method) and callable(getattr(obj, method)):
            try:
                return getattr(obj, method)(*args)
            except KeyboardInterrupt:
                print(f"\n✓ Operasi '{method}' dihentikan oleh pengguna")
                return None
            except Exception as e:
                obj_type = type(obj).__name__
                raise RuntimeError(
                    f"Error saat memanggil metode '{method}' pada objek '{obj_type}': {str(e)}"
                ) from e
        if id(obj) in self.instance_scopes:
            class_name = obj.__class__.__name__
            if class_name in self.classes and method in self.classes[class_name]["methods"]:
                old_instance = self.current_instance
                old_local_scope = self.local_scope.copy()
                self.current_instance = id(obj)
                self.local_scope = {}
                params, body, return_type, param_types = self.classes[class_name]["methods"][method]
                self.local_scope["diri"] = obj
                if params and len(params) > 0:
                    start_param_idx = 1 if params[0] == "diri" else 0
                    expected_user_params = len(params) - start_param_idx
                    if len(args) != expected_user_params:
                        raise RuntimeError(
                            f"Metode '{method}' membutuhkan {expected_user_params} parameter, tetapi {len(args)} diberikan"
                        )
                    if param_types and len(param_types) > start_param_idx:
                        for i, (arg, type_hint) in enumerate(zip(args, param_types[start_param_idx:])):
                            type_name = type_hint.type_name
                            if type_name in self.type_registry:
                                expected_type = self.type_registry[type_name]
                                try:
                                    if isinstance(expected_type, type) and not isinstance(arg, expected_type):
                                        raise TypeHintError(
                                            f"Parameter ke-{i + 1} '{params[i + start_param_idx]}' harus bertipe '{type_name}'"
                                        )
                                except TypeError as e:
                                    # Type checking failed - this is expected for non-type objects
                                    log_exception("type validation", e, level="debug")
                            elif hasattr(py_builtins, type_name):
                                expected_type = getattr(py_builtins, type_name)
                                try:
                                    if isinstance(expected_type, type) and not isinstance(arg, expected_type):
                                        raise TypeHintError(
                                            f"Parameter ke-{i + 1} '{params[i + start_param_idx]}' harus bertipe '{type_name}'"
                                        )
                                except TypeError as e:
                                    # Type checking failed - this is expected for non-type objects
                                    log_exception("type validation", e, level="debug")
                    for i, param_name in enumerate(params[start_param_idx:]):
                        self.local_scope[param_name] = args[i]
                elif len(args) != 0:
                    raise RuntimeError(
                        f"Metode '{method}' tidak membutuhkan parameter, tetapi {len(args)} diberikan"
                    )
                self.return_value = None
                self.visit_Block(Block(body))
                return_value = self.return_value
                if return_type and return_value is not None:
                    type_name = return_type.type_name
                    if type_name in self.type_registry:
                        expected_type = self.type_registry[type_name]
                        try:
                            if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                                raise TypeHintError(
                                    f"Nilai kembali metode '{method}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                                raise TypeHintError(
                                    f"Nilai kembali metode '{method}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                self.current_instance = old_instance
                self.local_scope = old_local_scope
                self.return_value = None
                return return_value
        raise AttributeError(f"Objek '{type(obj).__name__}' tidak memiliki metode '{method}'")

    def visit_SelfVar(self, node):
        # Check if 'self' is used as a regular parameter in a function
        # In this case, it should be treated as a regular variable
        if "self" in self.local_scope:
            return self.local_scope["self"]

        # Otherwise, treat it as 'diri' in class context
        if self.current_instance is None:
            raise NameError("Variabel 'diri' tidak dapat diakses di luar konteks kelas")
        if "diri" in self.local_scope:
            return self.local_scope["diri"]
        else:
            raise NameError("Variabel 'diri' tidak ditemukan dalam konteks saat ini")

    def visit_PropertyDecl(self, node):
        prop = property(fget=node.getter, fset=node.setter, fdel=node.deleter)
        self.current_scope.set(node.name, prop)
        return prop

    def visit_StaticMethodDecl(self, node):
        static_func = staticmethod(node.func)
        self.current_scope.set(node.name, static_func)
        return static_func

    def visit_ClassMethodDecl(self, node):
        class_func = classmethod(node.func)
        self.current_scope.set(node.name, class_func)
        return class_func
