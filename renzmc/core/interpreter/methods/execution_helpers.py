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
RenzmcLang Interpreter Execution Helpers Module

This module contains execution helpers methods.
"""

import builtins as py_builtins
import os
import time
from pathlib import Path

from renzmc.core.ast import Block
from renzmc.core.error import TypeHintError
from renzmc.utils.error_handler import log_exception

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class ExecutionHelpersMixin:
    """
    Mixin class for execution helpers.

    Provides 10 methods for handling execution helpers.
    """

    def _execute_user_function(self, name, params, body, return_type, param_types, args, kwargs):
        # Check if function should be force-compiled with JIT
        # Only try to compile once - if it's already in jit_compiled_functions (even if None), skip
        if JIT_AVAILABLE and hasattr(self, "_jit_force") and name in self._jit_force:
            if name not in self.jit_compiled_functions:
                self._compile_function_with_jit(name, params, body, force=True)

        # Check if function has JIT hint and should be compiled
        if JIT_AVAILABLE and hasattr(self, "_jit_hints") and name in self._jit_hints:
            if name not in self.jit_compiled_functions:
                self._compile_function_with_jit(name, params, body, force=True)

        if JIT_AVAILABLE and name in self.jit_compiled_functions:
            compiled_func = self.jit_compiled_functions[name]
            if compiled_func is not None:
                try:
                    return compiled_func(*args, **kwargs)
                except Exception as e:
                    # Unexpected exception - logging for debugging
                    log_exception("operation", e, level="warning")

        start_time = time.time()
        param_values = {}
        for i, arg in enumerate(args):
            if i >= len(params):
                raise RuntimeError(
                    f"Fungsi '{name}' membutuhkan {len(params)} parameter, tetapi {len(args)} posisional diberikan"
                )
            param_values[params[i]] = arg
        for param_name, value in kwargs.items():
            if param_name not in params:
                raise RuntimeError(f"Parameter '{param_name}' tidak ada dalam fungsi '{name}'")
            if param_name in param_values:
                raise RuntimeError(
                    f"Parameter '{param_name}' mendapat nilai ganda (posisional dan kata kunci)"
                )
            param_values[param_name] = value
        missing_params = [p for p in params if p not in param_values]
        if missing_params:
            raise RuntimeError(f"Parameter hilang dalam fungsi '{name}': {', '.join(missing_params)}")
        if param_types:
            for param_name, value in param_values.items():
                if param_name in param_types:
                    type_hint = param_types[param_name]
                    type_name = type_hint.type_name
                    if type_name in self.type_registry:
                        expected_type = self.type_registry[type_name]
                        try:
                            if isinstance(expected_type, type) and not isinstance(value, expected_type):
                                raise TypeHintError(
                                    f"Parameter '{param_name}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(value, expected_type):
                                raise TypeHintError(
                                    f"Parameter '{param_name}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
        old_local_scope = self.local_scope.copy()
        self.local_scope = {}
        for param_name, value in param_values.items():
            self.set_variable(param_name, value, is_local=True)
        self.return_value = None
        for stmt in body:
            self.visit(stmt)
            if hasattr(self, "return_flag") and self.return_flag:
                break
            if (
                hasattr(self, "break_flag")
                and self.break_flag
                or (hasattr(self, "continue_flag") and self.continue_flag)
            ):
                if hasattr(self, "break_flag"):
                    self.break_flag = False
                if hasattr(self, "continue_flag"):
                    self.continue_flag = False
                break
        return_value = self.return_value
        if return_type and return_value is not None:
            if hasattr(return_type, "type_name"):
                type_name = return_type.type_name
                if type_name in self.type_registry:
                    expected_type = self.type_registry[type_name]
                    try:
                        if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                            raise TypeHintError(
                                f"Nilai kembali fungsi '{name}' harus bertipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(return_value, expected_type):
                            raise TypeHintError(
                                f"Nilai kembali fungsi '{name}' harus bertipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
            else:
                from renzmc.core.advanced_types import AdvancedTypeValidator, TypeParser

                if isinstance(return_type, str):
                    type_spec = TypeParser.parse_type_string(return_type)
                else:
                    type_spec = return_type
                if type_spec:
                    is_valid, error_msg = AdvancedTypeValidator.validate(return_value, type_spec, "return")
                    if not is_valid:
                        raise TypeHintError(f"Fungsi '{name}': {error_msg}")
        self.local_scope = old_local_scope
        self.return_value = None

        if JIT_AVAILABLE and name in self.jit_call_counts:
            execution_time = time.time() - start_time
            self.jit_call_counts[name] += 1
            self.jit_execution_times[name] += execution_time

            if self.jit_call_counts[name] >= self.jit_threshold and name not in self.jit_compiled_functions:
                # Check if function is recursive before auto-compiling
                from renzmc.jit.type_inference import TypeInferenceEngine

                type_inference = TypeInferenceEngine()
                complexity = type_inference.analyze_function_complexity(body, name)
                if not complexity["has_recursion"]:
                    self._compile_function_with_jit(name, params, body)

        return return_value

    def _compile_function_with_jit(self, name, params, body, force=False):
        if not self.jit_compiler:
            self.jit_compiled_functions[name] = None
            return

        try:
            interpreter_func = self.global_scope.get(name)

            if not interpreter_func:
                self.jit_compiled_functions[name] = None
                return

            # Use force_compile if force flag is set
            if force:
                compiled_func = self.jit_compiler.force_compile(name, params, body, interpreter_func)
            else:
                compiled_func = self.jit_compiler.compile_function(name, params, body, interpreter_func)

            if compiled_func:
                self.jit_compiled_functions[name] = compiled_func

            else:
                self.jit_compiled_functions[name] = None

        except Exception:
            self.jit_compiled_functions[name] = None

    def _create_user_function_wrapper(self, name):

        def user_decorator_wrapper(func, *args, **kwargs):
            if name in self.functions:
                function_data = self.functions[name]
                if len(function_data) == 5:
                    params, body, return_type, param_types, _ = function_data
                else:
                    params, body, return_type, param_types = function_data
                all_args = [func] + list(args)
                return self._execute_user_function(name, params, body, return_type, param_types, all_args, kwargs)
            else:
                raise RuntimeError(f"User function '{name}' not found for decorator")

        return user_decorator_wrapper

    def _create_user_decorator_factory(self, name, decorator_args):

        def decorator_factory(func):
            if name in self.functions:
                function_data = self.functions[name]
                if len(function_data) == 5:
                    params, body, return_type, param_types, _ = function_data
                else:
                    params, body, return_type, param_types = function_data
                all_args = list(decorator_args) + [func]
                decorator_result = self._execute_user_function(
                    name, params, body, return_type, param_types, all_args, {}
                )
                if callable(decorator_result):
                    return decorator_result
                else:
                    return func
            else:
                raise RuntimeError(f"User function '{name}' not found for decorator factory")

        return decorator_factory

    def create_class_instance(self, class_name, args):
        class_info = self.classes[class_name]

        class Instance:

            def __init__(self, class_name):
                self.__class__.__name__ = class_name

        instance = Instance(class_name)
        instance_id = id(instance)
        self.instance_scopes[instance_id] = {}
        if class_info["constructor"]:
            constructor_params, constructor_body, param_types = class_info["constructor"]
            if len(args) != len(constructor_params):
                raise RuntimeError(
                    f"Konstruktor kelas '{class_name}' membutuhkan {len(constructor_params)} parameter, tetapi {len(args)} diberikan"
                )
            old_instance = self.current_instance
            old_local_scope = self.local_scope.copy()
            self.current_instance = instance_id
            self.local_scope = {}
            self.local_scope["diri"] = instance
            for i, param in enumerate(constructor_params):
                self.set_variable(param, args[i], is_local=True)
            self.visit_Block(Block(constructor_body))
            self.current_instance = old_instance
            self.local_scope = old_local_scope
        return instance

    def _load_rmc_module(self, module_name):
        # Check if module is already loaded in cache
        if module_name in self.modules:
            return self.modules[module_name]

        # Convert dot-separated module name to path (e.g., "Ren.renz" -> "Ren/renz")
        module_path = module_name.replace(".", os.sep)

        search_paths = [
            f"{module_path}.rmc",
            f"modules/{module_path}.rmc",
            f"examples/{module_path}.rmc",
            f"examples/modules/{module_path}.rmc",
            f"lib/{module_path}.rmc",
            f"rmc_modules/{module_path}.rmc",
        ]
        if "__file__" in globals():
            script_dir = Path(__file__).parent
            search_paths.extend(
                [
                    str(script_dir / f"{module_path}.rmc"),
                    str(script_dir / "modules" / f"{module_path}.rmc"),
                    str(script_dir / "lib" / f"{module_path}.rmc"),
                ]
            )
        for file_path in search_paths:
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        source_code = f.read()
                    # Import Interpreter here to avoid circular import
                    from renzmc.core.interpreter import Interpreter
                    from renzmc.core.lexer import Lexer
                    from renzmc.core.parser import Parser

                    module_interpreter = Interpreter()
                    lexer = Lexer(source_code)
                    parser = Parser(lexer)
                    ast = parser.parse()
                    module_interpreter.visit(ast)

                    class RenzmcModule:

                        def __init__(self, scope):
                            self._exports = {}
                            builtin_names = set(self._get_builtin_names())
                            for name, value in scope.items():
                                # Export user-defined items, but skip:
                                # - Private items (starting with _)
                                # - Python integration items (starting with py_)
                                # - Builtin functions that are the same object as the builtin
                                # (Allow user-defined functions even if they have the same name as builtins)
                                if name.startswith("_") or name.startswith("py_"):
                                    continue

                                # Check if it's actually a builtin by comparing object identity
                                is_builtin = False
                                if name in builtin_names:
                                    # Only skip if it's the actual builtin function, not a user-defined one
                                    try:
                                        import renzmc.builtins as renzmc_builtins

                                        if hasattr(renzmc_builtins, name):
                                            builtin_func = getattr(renzmc_builtins, name)
                                            if value is builtin_func:
                                                is_builtin = True
                                    except Exception:
                                        pass

                                if not is_builtin:
                                    setattr(self, name, value)
                                    self._exports[name] = value

                        def _get_builtin_names(self):
                            return {
                                "tampilkan",
                                "panjang",
                                "jenis",
                                "ke_teks",
                                "ke_angka",
                                "huruf_besar",
                                "huruf_kecil",
                                "potong",
                                "gabung",
                                "pisah",
                                "ganti",
                                "mulai_dengan",
                                "akhir_dengan",
                                "berisi",
                                "hapus_spasi",
                                "bulat",
                                "desimal",
                                "akar",
                                "pangkat",
                                "absolut",
                                "pembulatan",
                                "pembulatan_atas",
                                "pembulatan_bawah",
                                "sinus",
                                "cosinus",
                                "tangen",
                                "tambah",
                                "hapus",
                                "hapus_pada",
                                "masukkan",
                                "urutkan",
                                "balikkan",
                                "hitung",
                                "indeks",
                                "extend",
                                "kunci",
                                "nilai",
                                "item",
                                "hapus_kunci",
                                "acak",
                                "waktu",
                                "tanggal",
                                "tidur",
                                "tulis_file",
                                "baca_file",
                                "tambah_file",
                                "file_exists",
                                "ukuran_file",
                                "hapus_file",
                                "json_ke_teks",
                                "teks_ke_json",
                                "url_encode",
                                "url_decode",
                                "hash_teks",
                                "base64_encode",
                                "base64_decode",
                                "buat_uuid",
                                "regex_match",
                                "regex_replace",
                                "regex_split",
                                "http_get",
                                "http_post",
                                "http_put",
                                "http_delete",
                                "panggil",
                                "daftar_direktori",
                                "buat_direktori",
                                "direktori_exists",
                            }

                        def get_exports(self):
                            return self._exports.copy()

                        def __getitem__(self, key):
                            return getattr(self, key)

                        def __contains__(self, key):
                            return hasattr(self, key)

                    loaded_module = RenzmcModule(module_interpreter.global_scope)
                    # Cache the loaded module
                    self.modules[module_name] = loaded_module
                    return loaded_module
                except Exception as e:
                    raise ImportError(f"Gagal memuat modul RenzMC '{module_name}': {str(e)}")
        return None

    def _smart_getattr(self, obj, name, default=None):
        try:
            if hasattr(obj, "_obj"):
                actual_obj = obj._obj
            else:
                actual_obj = obj
            result = getattr(actual_obj, name, default)
            if hasattr(obj, "_integration"):
                return obj._integration.convert_python_to_renzmc(result)
            elif hasattr(self, "python_integration"):
                return self.python_integration.convert_python_to_renzmc(result)
            else:
                return result
        except Exception as e:
            if default is not None:
                return default
            raise AttributeError(f"Error mengakses atribut '{name}': {str(e)}")

    def _smart_setattr(self, obj, name, value):
        try:
            if hasattr(obj, "_obj"):
                actual_obj = obj._obj
                converted_value = obj._integration.convert_renzmc_to_python(value)
            else:
                actual_obj = obj
                converted_value = self.python_integration.convert_renzmc_to_python(value)
            setattr(actual_obj, name, converted_value)
            return True
        except Exception as e:
            raise AttributeError(f"Error mengatur atribut '{name}': {str(e)}")

    def _smart_hasattr(self, obj, name):
        try:
            if hasattr(obj, "_obj"):
                actual_obj = obj._obj
            else:
                actual_obj = obj
            return hasattr(actual_obj, name)
        except Exception:
            return False

    def interpret(self, tree):
        return self.visit(tree)
