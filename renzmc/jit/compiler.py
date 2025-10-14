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

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from .code_generator import CodeGenerator
from .type_inference import TypeInferenceEngine

try:
    import numba

    NUMBA_AVAILABLE = True
except ImportError:
    NUMBA_AVAILABLE = False


class JITCompiler:

    def __init__(self):
        self.code_generator = CodeGenerator()
        self.type_inference = TypeInferenceEngine()
        self.compiled_cache: Dict[str, Callable] = {}
        self.compilation_stats: Dict[str, Dict[str, Any]] = {}

    def can_compile(self, name: str, params: List[str], body: List) -> bool:
        if not NUMBA_AVAILABLE:
            return False

        is_numeric = self.type_inference.is_numeric_function(params, body)

        complexity = self.type_inference.analyze_function_complexity(body, name)

        # Skip recursive functions for now - they cause issues with JIT compilation
        if complexity["has_recursion"]:
            return False

        should_compile = is_numeric and (complexity["has_loops"] or complexity["operation_count"] > 5)

        return should_compile

    def compile_function(
        self, name: str, params: List[str], body: List, interpreter_func: Callable
    ) -> Optional[Callable]:
        if name in self.compiled_cache:
            return self.compiled_cache[name]

        if not self.can_compile(name, params, body):
            self._record_compilation(name, success=False, reason="not_suitable")
            return None

        try:
            python_code = self.code_generator.generate_function(name, params, body)

            if not python_code or python_code.strip() == "":
                self._record_compilation(name, success=False, reason="empty_code")
                return None

            compiled_func = self._compile_with_numba(name, python_code, params, interpreter_func)

            if compiled_func:
                self.compiled_cache[name] = compiled_func
                self._record_compilation(name, success=True, code=python_code)
                return compiled_func
            else:
                self._record_compilation(name, success=False, reason="compilation_failed", code=python_code)
                return None

        except Exception as e:
            import traceback

            error_detail = f"{str(e)}\n{traceback.format_exc()}"
            self._record_compilation(name, success=False, reason=error_detail)
            return None

    def _compile_with_numba(
        self, name: str, python_code: str, params: List[str], fallback_func: Callable
    ) -> Optional[Callable]:
        try:
            namespace = {
                "range": range,
                "int": int,
                "float": float,
                "abs": abs,
                "min": min,
                "max": max,
                "sum": sum,
                "len": len,
                "pow": pow,
            }

            exec(python_code, namespace)

            if name not in namespace:
                return None

            original_func = namespace[name]

            try:
                jit_func = numba.jit(nopython=True)(original_func)

                def jit_wrapper(*args, **kwargs):
                    try:
                        return jit_func(*args, **kwargs)
                    except Exception:
                        return fallback_func(*args, **kwargs)

                jit_wrapper.__name__ = name
                jit_wrapper.__jit_compiled__ = True

                return jit_wrapper

            except Exception:
                try:
                    jit_func = numba.jit()(original_func)

                    def jit_wrapper(*args, **kwargs):
                        try:
                            return jit_func(*args, **kwargs)
                        except Exception:
                            return fallback_func(*args, **kwargs)

                    jit_wrapper.__name__ = name
                    jit_wrapper.__jit_compiled__ = True

                    return jit_wrapper
                except Exception:
                    return None

        except Exception:
            return None

    def _record_compilation(self, name: str, success: bool, reason: str = "", code: str = ""):
        self.compilation_stats[name] = {
            "success": success,
            "reason": reason,
            "code": code,
        }

    def get_compilation_stats(self, name: str) -> Optional[Dict[str, Any]]:
        return self.compilation_stats.get(name)

    def get_all_stats(self) -> Dict[str, Dict[str, Any]]:
        return self.compilation_stats.copy()

    def clear_cache(self):
        self.compiled_cache.clear()
        self.compilation_stats.clear()

    def force_compile(self, name: str, params: List[str], body: List, interpreter_func: Callable) -> Optional[Callable]:
        if name in self.compiled_cache:
            return self.compiled_cache[name]

        try:
            # Check for recursion even in force compile
            complexity = self.type_inference.analyze_function_complexity(body, name)
            if complexity["has_recursion"]:
                self._record_compilation(name, success=False, reason="recursive_function_not_supported")
                return None

            python_code = self.code_generator.generate_function(name, params, body)

            if not python_code or python_code.strip() == "":
                self._record_compilation(name, success=False, reason="empty_code")
                return None

            compiled_func = self._compile_with_numba(name, python_code, params, interpreter_func)

            if compiled_func:
                self.compiled_cache[name] = compiled_func
                self._record_compilation(name, success=True, code=python_code)
                return compiled_func
            else:
                self._record_compilation(name, success=False, reason="compilation_failed", code=python_code)
                return None

        except Exception as e:
            import traceback

            error_detail = f"{str(e)}\n{traceback.format_exc()}"
            self._record_compilation(name, success=False, reason=error_detail)
            return None

    def compile_with_gpu(
        self, name: str, params: List[str], body: List, interpreter_func: Callable
    ) -> Optional[Callable]:
        if not NUMBA_AVAILABLE:
            return None

        try:
            from numba import cuda

            if not cuda.is_available():
                self._record_compilation(name, success=False, reason="cuda_not_available")
                return None

            python_code = self.code_generator.generate_function(name, params, body)

            if not python_code or python_code.strip() == "":
                self._record_compilation(name, success=False, reason="empty_code")
                return None

            namespace = {
                "range": range,
                "int": int,
                "float": float,
                "abs": abs,
                "min": min,
                "max": max,
                "sum": sum,
                "len": len,
                "pow": pow,
                "cuda": cuda,
            }

            exec(python_code, namespace)

            if name not in namespace:
                return None

            original_func = namespace[name]
            gpu_func = cuda.jit(original_func)

            def gpu_wrapper(*args, **kwargs):
                try:
                    return gpu_func(*args, **kwargs)
                except Exception:
                    return interpreter_func(*args, **kwargs)

            gpu_wrapper.__name__ = name
            gpu_wrapper.__gpu_compiled__ = True

            self.compiled_cache[name] = gpu_wrapper
            self._record_compilation(name, success=True, code=python_code, reason="gpu_compiled")
            return gpu_wrapper

        except Exception as e:
            import traceback

            error_detail = f"{str(e)}\n{traceback.format_exc()}"
            self._record_compilation(name, success=False, reason=error_detail)
            return None
