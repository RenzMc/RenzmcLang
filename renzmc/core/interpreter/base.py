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

import asyncio
import builtins as py_builtins

from renzmc.core.base_visitor import NodeVisitor
from renzmc.core.type_integration import TypeIntegrationMixin
from renzmc.runtime.advanced_features import (
    AdvancedFeatureManager,
    cache_decorator,
    clear_cache,
    create_custom_decorator,
    get_cache_stats,
    gpu_decorator,
    jit_compile_decorator,
    jit_force_decorator,
    parallel_decorator,
    profile_decorator,
    timing_decorator,
    universal_retry_decorator,
    web_route_decorator,
)
from renzmc.runtime.builtin_manager import BuiltinManager
from renzmc.runtime.crypto_operations import CryptoOperations
from renzmc.runtime.file_operations import FileOperations
from renzmc.runtime.modulehelper import add_examples_path
from renzmc.runtime.python_integration import PythonIntegration
from renzmc.runtime.renzmc_module_system import RenzmcModuleManager
from renzmc.runtime.scope_manager import ScopeManager

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class InterpreterBase(NodeVisitor, TypeIntegrationMixin):
    """
    Base interpreter class containing initialization and core setup.

    This class provides the foundation for the RenzmcLang interpreter,
    including scope management, builtin functions, and runtime managers.
    """

    def __init__(self):
        self.safe_mode = True
        self.scope_manager = ScopeManager()
        self.python_integration = PythonIntegration()
        self.file_ops = FileOperations()
        self.crypto_ops = CryptoOperations()
        self.module_manager = RenzmcModuleManager(self)
        add_examples_path(self)
        self.advanced_features = AdvancedFeatureManager()
        self.advanced_features.create_decorator("waktu", timing_decorator)
        self.advanced_features.create_decorator("cache", cache_decorator)
        self.advanced_features.create_decorator("coba_ulang", universal_retry_decorator)
        self.advanced_features.create_decorator("jit_compile", jit_compile_decorator)
        self.advanced_features.create_decorator("jit_force", jit_force_decorator)
        self.advanced_features.create_decorator("parallel", parallel_decorator)
        self.advanced_features.create_decorator("gpu", gpu_decorator)
        self.advanced_features.create_decorator("profile", profile_decorator)

        self._init_type_system(strict_mode=False)

        self.jit_call_counts = {}
        self.jit_execution_times = {}
        self.jit_compiled_functions = {}
        self.jit_threshold = 10

        if JIT_AVAILABLE and JITCompiler:
            self.jit_compiler = JITCompiler()
        else:
            self.jit_compiler = None

        self.builtin_functions = BuiltinManager.setup_builtin_functions()
        self.builtin_functions.update(
            {
                "buat_decorator_kustom": create_custom_decorator,
                "route": web_route_decorator,
                "bersihkan_cache": clear_cache,
                "info_cache": get_cache_stats,
                "jit_compile": jit_compile_decorator,
                "jit_force": jit_force_decorator,
                "parallel": parallel_decorator,
                "gpu": gpu_decorator,
                "profile": profile_decorator,
            }
        )
        self.return_value = None
        self.break_flag = False
        self.continue_flag = False
        self.scope_manager.builtin_functions = self.builtin_functions

        self._register_python_integration_builtins()
        self._register_renzmc_module_builtins()
        self._register_advanced_feature_builtins()
        self._register_safety_builtins()
        self._register_inline_cache_builtins()

        self.scope_manager.builtin_functions = self.builtin_functions
        self._setup_python_builtins()
        self._setup_compatibility_adapters()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def _register_python_integration_builtins(self):
        """Register Python integration builtin functions."""
        self.builtin_functions.update(
            {
                "impor_python": self._import_python_module,
                "panggil_python": self._call_python_function,
                "impor_dari_python": self._from_python_import,
                "buat_objek_python": self._create_python_object,
                "daftar_atribut_python": self._list_python_attributes,
                "bantuan_python": self._python_help,
                "instal_paket_python": self._install_python_package,
                "impor_otomatis": self._auto_import_python,
                "konversi_ke_python": self._convert_to_python,
                "konversi_dari_python": self._convert_from_python,
                "bungkus_pintar": self._create_smart_wrapper,
                "cek_modul_tersedia": self._check_module_available,
                "getattr": py_builtins.getattr,
                "setattr": py_builtins.setattr,
                "hasattr": py_builtins.hasattr,
                "dir": py_builtins.dir,
                "isinstance": py_builtins.isinstance,
                "callable": py_builtins.callable,
                "len": py_builtins.len,
                "ambil_atribut": self._smart_getattr,
                "atur_atribut": self._smart_setattr,
                "cek_atribut": self._smart_hasattr,
            }
        )

    def _register_renzmc_module_builtins(self):
        """Register RenzmcLang module system builtin functions."""
        self.builtin_functions.update(
            {
                "impor_renzmc": self._import_renzmc_module,
                "impor_dari_renzmc": self._import_from_renzmc_module,
                "impor_semua_dari_renzmc": self._import_all_from_renzmc_module,
                "muat_ulang_modul": self._reload_renzmc_module,
                "daftar_modul_renzmc": self._list_renzmc_modules,
                "info_modul_renzmc": self._get_renzmc_module_info,
                "tambah_jalur_modul": self._add_module_search_path,
            }
        )

    def _register_advanced_feature_builtins(self):
        """Register advanced feature builtin functions."""
        self.builtin_functions.update(
            {
                "buat_decorator": self._create_decorator,
                "terapkan_decorator": self._apply_decorator,
                "buat_context_manager": self._create_context_manager,
                "gunakan_context": self._use_context_manager,
                "buat_generator_lanjutan": self._create_advanced_generator,
                "buat_async_function": self._create_async_function,
                "daftar_fitur_lanjutan": self._list_advanced_features,
            }
        )

    def _register_safety_builtins(self):
        """Register safety mode builtin functions."""
        self.builtin_functions.update(
            {
                "atur_mode_aman": self._set_safe_mode,
                "cek_mode_aman": self._check_safe_mode,
            }
        )

    def _register_inline_cache_builtins(self):
        """Register inline cache builtin functions."""
        self.builtin_functions.update(
            {
                "info_cache_inline": self._get_inline_cache_stats,
                "reset_cache_inline": self._reset_inline_cache,
                "bersihkan_cache_inline": self._clear_inline_cache,
                "aktifkan_cache_inline": self._enable_inline_cache,
                "nonaktifkan_cache_inline": self._disable_inline_cache,
            }
        )
