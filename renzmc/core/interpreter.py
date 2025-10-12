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
import importlib
import inspect
import os
import re
import sys
import time
from pathlib import Path

import renzmc.builtins as renzmc_builtins
from renzmc.core.base_visitor import NodeVisitor
from renzmc.core.token import TokenType
from renzmc.core.type_integration import TypeIntegrationMixin
from renzmc.core.type_system import BaseType, TypeChecker, TypeValidator
from renzmc.runtime.advanced_features import (
    AdvancedFeatureManager,
    cache_decorator,
    retry_decorator,
    simple_retry_decorator,
    timing_decorator,
    universal_retry_decorator,
)
from renzmc.runtime.builtin_manager import BuiltinManager
from renzmc.runtime.crypto_operations import CryptoOperations
from renzmc.runtime.file_operations import FileOperations
from renzmc.runtime.python_integration import PythonIntegration
from renzmc.runtime.renzmc_module_system import RenzmcModuleManager
from renzmc.runtime.scope_manager import ScopeManager

# Import error handling utilities
from renzmc.utils.error_handler import (
    ErrorContext,
    handle_attribute_error,
    handle_import_error,
    handle_type_error,
    log_exception,
)
from renzmc.utils.module_helpers import import_submodule, require_module
from renzmc.utils.type_helpers import (
    check_parameter_type,
    check_return_type,
    get_type_from_registry,
    validate_type,
)

try:
    import numba

    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None
from renzmc.core.ast import (
    AST,
    Assign,
    AsyncFuncDecl,
    AsyncMethodDecl,
    AttributeRef,
    Await,
    BinOp,
    Block,
    Boolean,
    Break,
    Case,
    ClassDecl,
    CompoundAssign,
    Constructor,
    Continue,
    Decorator,
    Dict,
    DictComp,
    For,
    ForEach,
    FormatString,
    FuncCall,
    FuncDecl,
    Generator,
    If,
    Import,
    IndexAccess,
    Input,
    Lambda,
    List,
    ListComp,
    MethodCall,
    MethodDecl,
    MultiAssign,
    MultiVarDecl,
    NoOp,
    Num,
    Print,
    Program,
    PythonCall,
    PythonImport,
    Raise,
    Return,
    SelfVar,
    Set,
    SetComp,
    SliceAccess,
    String,
    Switch,
    Ternary,
    TryCatch,
    Tuple,
    TypeHint,
    UnaryOp,
    Unpacking,
    Var,
    VarDecl,
    WalrusOperator,
    While,
    With,
    Yield,
    YieldFrom,
)
from renzmc.core.error import (
    AsyncError,
    DivisionByZeroError,
    FileError,
    InterpreterError,
    LexerError,
    ParserError,
    PythonIntegrationError,
    RenzmcAttributeError,
    RenzmcError,
    RenzmcImportError,
    RenzmcIndexError,
    RenzmcKeyError,
    RenzmcNameError,
    RenzmcRuntimeError,
    RenzmcSyntaxError,
    RenzmcTypeError,
    RenzmcValueError,
    TypeHintError,
)

NameError = RenzmcNameError
TypeError = RenzmcTypeError
ValueError = RenzmcValueError
ImportError = RenzmcImportError
AttributeError = RenzmcAttributeError
IndexError = RenzmcIndexError
KeyError = RenzmcKeyError
RuntimeError = RenzmcRuntimeError
SyntaxError = RenzmcSyntaxError

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    Fernet = None
    hashes = None
    PBKDF2HMAC = None
    CRYPTOGRAPHY_AVAILABLE = False


class Interpreter(NodeVisitor, TypeIntegrationMixin):

    def __init__(self):
        self.safe_mode = True
        self.scope_manager = ScopeManager()
        self.python_integration = PythonIntegration()
        self.file_ops = FileOperations()
        self.crypto_ops = CryptoOperations()
        self.module_manager = RenzmcModuleManager(self)
        self.advanced_features = AdvancedFeatureManager()
        self.advanced_features.create_decorator("waktu", timing_decorator)
        self.advanced_features.create_decorator("cache", cache_decorator)
        self.advanced_features.create_decorator("coba_ulang", universal_retry_decorator)
        from renzmc.runtime.advanced_features import (
            clear_cache,
            create_custom_decorator,
            get_cache_stats,
            gpu_decorator,
            jit_compile_decorator,
            jit_force_decorator,
            parallel_decorator,
            profile_decorator,
            web_route_decorator,
        )

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
                "impor_renzmc": self._import_renzmc_module,
                "impor_dari_renzmc": self._import_from_renzmc_module,
                "impor_semua_dari_renzmc": self._import_all_from_renzmc_module,
                "muat_ulang_modul": self._reload_renzmc_module,
                "daftar_modul_renzmc": self._list_renzmc_modules,
                "info_modul_renzmc": self._get_renzmc_module_info,
                "tambah_jalur_modul": self._add_module_search_path,
                "buat_decorator": self._create_decorator,
                "terapkan_decorator": self._apply_decorator,
                "buat_context_manager": self._create_context_manager,
                "gunakan_context": self._use_context_manager,
                "buat_generator_lanjutan": self._create_advanced_generator,
                "buat_async_function": self._create_async_function,
                "daftar_fitur_lanjutan": self._list_advanced_features,
            }
        )
        self.builtin_functions.update(
            {
                "atur_mode_aman": self._set_safe_mode,
                "cek_mode_aman": self._check_safe_mode,
            }
        )
        self.scope_manager.builtin_functions = self.builtin_functions
        self._setup_python_builtins()
        self._setup_compatibility_adapters()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    # ========================================================================
    # HELPER METHODS - Added to reduce code duplication
    # ========================================================================

    def _validate_parameter_type(
        self, param_value, type_name, param_name, function_name=""
    ):
        """
        Validate parameter type with proper error handling

        Args:
            param_value: The parameter value to check
            type_name: Expected type name
            param_name: Name of the parameter
            function_name: Name of the function (for error messages)

        Returns:
            bool: True if validation passes, False otherwise
        """
        # Using imported check_parameter_type
        return check_parameter_type(
            param_value, type_name, param_name, self.type_registry, function_name
        )

    def _validate_return_type(self, return_value, type_name, function_name=""):
        """
        Validate return type with proper error handling

        Args:
            return_value: The return value to check
            type_name: Expected type name
            function_name: Name of the function (for error messages)

        Returns:
            bool: True if validation passes, False otherwise
        """
        # Using imported check_return_type
        return check_return_type(
            return_value, type_name, self.type_registry, function_name
        )

    def _get_type_from_registry(self, type_name):
        """
        Get a type from the registry or builtins

        Args:
            type_name: Name of the type to retrieve

        Returns:
            The type object if found, None otherwise
        """
        # Using imported get_type_from_registry
        return get_type_from_registry(type_name, self.type_registry)

    def _safe_import_module(self, module_name, operation="module import"):
        """
        Safely import a module with proper error handling

        Args:
            module_name: Name of the module to import
            operation: Description of the operation

        Returns:
            The imported module or None if not available
        """
        # Using imported require_module
        return require_module(module_name, operation, raise_on_missing=False)

    def _safe_import_submodule(
        self, parent_module, submodule_name, operation="submodule import"
    ):
        """
        Safely import a submodule with proper error handling

        Args:
            parent_module: The parent module object
            submodule_name: Name of the submodule
            operation: Description of the operation

        Returns:
            The submodule or None if not available
        """
        # Using imported import_submodule
        return import_submodule(parent_module, submodule_name, operation)

    def _safe_isinstance(self, obj, type_obj):
        """
        Safely check isinstance with proper error handling

        Args:
            obj: Object to check
            type_obj: Type to check against

        Returns:
            bool: True if isinstance check passes, False on error
        """
        try:
            return isinstance(obj, type_obj)
        except TypeError as e:
            log_exception("isinstance check", e, level="debug")
            return False

    # ========================================================================
    # END OF HELPER METHODS
    # ========================================================================

    def _call_magic_method(self, obj, method_name, *args):
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                try:
                    result = method(*args)
                    if result is not NotImplemented:
                        return result
                except (TypeError, ValueError, AttributeError) as e:
                    from renzmc.utils.logging import logger

                    logger.debug(f"Magic method {method_name} failed: {e}")
                except Exception as e:
                    from renzmc.utils.logging import logger

                    logger.error(
                        f"Unexpected error in magic method {method_name}: {e}",
                        exc_info=True,
                    )
                    raise
        return NotImplemented

    def _set_safe_mode(self, enabled=True):
        self.safe_mode = enabled
        mode_text = "diaktifkan" if enabled else "dinonaktifkan"
        print(f"🔒 Mode aman {mode_text}")
        return enabled

    def _check_safe_mode(self):
        return self.safe_mode

    def _setup_compatibility_adapters(self):
        pass

    @property
    def global_scope(self):
        return self.scope_manager.global_scope

    @global_scope.setter
    def global_scope(self, value):
        self.scope_manager.global_scope = value

    @property
    def local_scope(self):
        return self.scope_manager.local_scope

    @local_scope.setter
    def local_scope(self, value):
        self.scope_manager.local_scope = value

    @property
    def functions(self):
        return self.scope_manager.functions

    @functions.setter
    def functions(self, value):
        self.scope_manager.functions = value

    @property
    def classes(self):
        return self.scope_manager.classes

    @classes.setter
    def classes(self, value):
        self.scope_manager.classes = value

    @property
    def modules(self):
        return self.scope_manager.modules

    @modules.setter
    def modules(self, value):
        self.scope_manager.modules = value

    @property
    def current_instance(self):
        return self.scope_manager.current_instance

    @current_instance.setter
    def current_instance(self, value):
        self.scope_manager.current_instance = value

    @property
    def instance_scopes(self):
        return self.scope_manager.instance_scopes

    @property
    def generators(self):
        return self.scope_manager.generators

    @property
    def async_functions(self):
        return self.scope_manager.async_functions

    @property
    def decorators(self):
        return self.scope_manager.decorators

    @property
    def type_registry(self):
        return self.scope_manager.type_registry

    def _setup_builtin_functions(self):
        self.builtin_functions = {
            "panjang": renzmc_builtins.panjang,
            "jenis": renzmc_builtins.jenis,
            "ke_teks": renzmc_builtins.ke_teks,
            "ke_angka": renzmc_builtins.ke_angka,
            "huruf_besar": renzmc_builtins.huruf_besar,
            "huruf_kecil": renzmc_builtins.huruf_kecil,
            "potong": renzmc_builtins.potong,
            "gabung": renzmc_builtins.gabung,
            "pisah": renzmc_builtins.pisah,
            "ganti": renzmc_builtins.ganti,
            "mulai_dengan": renzmc_builtins.mulai_dengan,
            "akhir_dengan": renzmc_builtins.akhir_dengan,
            "berisi": renzmc_builtins.berisi,
            "hapus_spasi": renzmc_builtins.hapus_spasi,
            "bulat": renzmc_builtins.bulat,
            "desimal": renzmc_builtins.desimal,
            "akar": renzmc_builtins.akar,
            "pangkat": renzmc_builtins.pangkat,
            "absolut": renzmc_builtins.absolut,
            "pembulatan": renzmc_builtins.pembulatan,
            "pembulatan_atas": renzmc_builtins.pembulatan_atas,
            "pembulatan_bawah": renzmc_builtins.pembulatan_bawah,
            "sinus": renzmc_builtins.sinus,
            "cosinus": renzmc_builtins.cosinus,
            "tangen": renzmc_builtins.tangen,
            "tambah": renzmc_builtins.tambah,
            "hapus": renzmc_builtins.hapus,
            "hapus_pada": renzmc_builtins.hapus_pada,
            "masukkan": renzmc_builtins.masukkan,
            "urutkan": renzmc_builtins.urutkan,
            "balikkan": renzmc_builtins.balikkan,
            "hitung": renzmc_builtins.hitung,
            "indeks": renzmc_builtins.indeks,
            "extend": renzmc_builtins.extend,
            "gabung_daftar": renzmc_builtins.extend,
            "zip": renzmc_builtins.zip,
            "enumerate": renzmc_builtins.enumerate,
            "filter": renzmc_builtins.filter,
            "saring": renzmc_builtins.saring,
            "map": renzmc_builtins.map,
            "peta": renzmc_builtins.peta,
            "reduce": renzmc_builtins.reduce,
            "kurangi": renzmc_builtins.kurangi,
            "all": renzmc_builtins.all,
            "semua": renzmc_builtins.semua,
            "any": renzmc_builtins.any,
            "ada": renzmc_builtins.ada,
            "sorted": renzmc_builtins.sorted,
            "terurut": renzmc_builtins.terurut,
            "kunci": renzmc_builtins.kunci,
            "nilai": renzmc_builtins.nilai,
            "item": renzmc_builtins.item,
            "hapus_kunci": renzmc_builtins.hapus_kunci,
            "acak": renzmc_builtins.acak,
            "waktu": renzmc_builtins.waktu,
            "tidur": renzmc_builtins.tidur,
            "tanggal": renzmc_builtins.tanggal,
            "baca_file": renzmc_builtins.baca_file,
            "tulis_file": renzmc_builtins.tulis_file,
            "tambah_file": renzmc_builtins.tambah_file,
            "hapus_file": renzmc_builtins.hapus_file,
            "jalankan_perintah": renzmc_builtins.jalankan_perintah,
            "atur_sandbox": renzmc_builtins.atur_sandbox,
            "tambah_perintah_aman": renzmc_builtins.tambah_perintah_aman,
            "hapus_perintah_aman": renzmc_builtins.hapus_perintah_aman,
            "impor_python": self._import_python_module,
            "panggil_python": self._call_python_function,
            "impor_dari_python": self._from_python_import,
            "buat_objek_python": self._create_python_object,
            "daftar_atribut_python": self._list_python_attributes,
            "bantuan_python": self._python_help,
            "instal_paket_python": self._install_python_package,
            "buat_generator": self._create_generator,
            "buat_async": self._create_async_function,
            "jalankan_async": self._run_async_function,
            "tunggu_semua": self._wait_all_async,
            "daftar_ke_generator": self._list_to_generator,
            "cek_tipe": self._check_type,
            "format_teks": self._format_string,
            "buka_file": self._open_file,
            "tutup_file": self._close_file,
            "baca_baris": self._read_line,
            "baca_semua_baris": self._read_all_lines,
            "tulis_baris": self._write_line,
            "flush_file": self._flush_file,
            "cek_file_ada": self._file_exists,
            "buat_direktori": self._make_directory,
            "hapus_direktori": self._remove_directory,
            "daftar_direktori": self._list_directory,
            "gabung_path": self._join_path,
            "path_file": self._file_path,
            "path_direktori": self._directory_path,
            "ukuran_file": self._file_size,
            "waktu_modifikasi": self._file_modification_time,
            "json_ke_teks": self._json_to_text,
            "teks_ke_json": self._text_to_json,
            "enkripsi": self._encrypt,
            "dekripsi": self._decrypt,
            "hash_teks": self._hash_text,
            "buat_uuid": self._create_uuid,
            "url_encode": self._url_encode,
            "url_decode": self._url_decode,
            "http_request": self._http_request,
            "http_get": self._http_get,
            "http_post": self._http_post,
            "http_put": self._http_put,
            "http_delete": self._http_delete,
            "atur_static": self._set_static,
            "template_html": self._render_template,
            "buat_form": self._create_form,
            "validate_form": self._validate_form,
        }

    def _setup_python_builtins(self):
        for name in dir(py_builtins):
            if not name.startswith("_"):
                self.global_scope[f"py_{name}"] = getattr(py_builtins, name)

    def _import_python_module(self, module_name, alias=None):
        try:
            wrapped_module = self.python_integration.import_python_module(
                module_name, alias
            )
            if alias:
                if isinstance(wrapped_module, dict):
                    self.global_scope[alias] = wrapped_module[alias]
                    return wrapped_module[alias]
                else:
                    self.global_scope[alias] = wrapped_module
                    return wrapped_module
            else:
                module_var_name = module_name.replace(".", "_")
                self.global_scope[module_var_name] = wrapped_module
                return wrapped_module
        except RenzmcImportError as e:
            print(f"❌ Gagal mengimpor modul Python '{module_name}': {str(e)}")
            print(
                f"""💡 Saran: Pastikan modul terinstal dengan 'instal_paket_python("{module_name}")'"""
            )
            raise e
        except Exception as e:
            import_error = RenzmcImportError(
                f"Error tidak terduga saat mengimpor '{module_name}': {str(e)}"
            )
            print(f"❌ {import_error}")
            raise import_error

    def _call_python_function(self, func, *args, **kwargs):
        return self.python_integration.call_python_function(func, *args, **kwargs)

    def _from_python_import(self, module_name, *items):
        try:
            imported_items = self.python_integration.import_python_module(
                module_name, from_items=list(items)
            )
            for item_name, item_value in imported_items.items():
                enhanced_value = self.python_integration.convert_python_to_renzmc(
                    item_value
                )
                self.global_scope[item_name] = enhanced_value
            print(
                f"✓ Berhasil mengimpor {len(imported_items)} item dari modul '{module_name}'"
            )
            return imported_items
        except RenzmcImportError as e:
            print(f"❌ Gagal mengimpor dari modul Python '{module_name}': {str(e)}")
            print("💡 Saran: Periksa nama modul dan item yang akan diimpor")
            raise e
        except Exception as e:
            import_error = RenzmcImportError(
                f"Error tidak terduga saat mengimpor dari '{module_name}': {str(e)}"
            )
            print(f"❌ {import_error}")
            raise import_error

    def _create_python_object(self, class_obj, *args, **kwargs):
        return self.python_integration.create_python_object(class_obj, *args, **kwargs)

    def _list_python_attributes(self, module_name):
        return self.python_integration.list_module_attributes(module_name)

    def _python_help(self, obj):
        return self.python_integration.get_python_help(obj)

    def _install_python_package(self, package_name):
        if self.safe_mode:
            raise RuntimeError(
                "🔒 Instalasi paket Python diblokir dalam mode aman. Gunakan `atur_mode_aman(salah)` untuk mengaktifkan (tidak disarankan untuk server)."
            )
        return self.python_integration.install_package(package_name)

    def _auto_import_python(self, module_name):
        return self.python_integration.auto_import_on_demand(module_name)

    def _convert_to_python(self, obj):
        return self.python_integration.convert_renzmc_to_python(obj)

    def _convert_from_python(self, obj):
        return self.python_integration.convert_python_to_renzmc(obj)

    def _create_smart_wrapper(self, obj):
        return self.python_integration.create_smart_wrapper(obj)

    def _import_all_from_python(self, module_name):
        return self.python_integration.enable_star_imports(
            module_name, self.global_scope
        )

    def _list_python_modules(self):
        return self.python_integration.get_all_python_modules()

    def _check_module_available(self, module_name):
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            return False

    def _execute_python_code(self, code_string, local_vars=None):
        raise RuntimeError(
            "🔒 Eksekusi kode Python dinamis dinonaktifkan untuk keamanan.\nGunakan fungsi built-in atau impor modul Python secara eksplisit.\nContoh: gunakan 'impor_python &quot;math&quot;' lalu 'panggil_python math.sqrt(16)'"
        )

    def _evaluate_python_expression(self, expression, context=None):
        raise RuntimeError(
            "🔒 Evaluasi ekspresi Python dinamis dinonaktifkan untuk keamanan.\nGunakan fungsi built-in atau impor modul Python secara eksplisit.\nContoh: gunakan 'impor_python &quot;math&quot;' lalu 'panggil_python math.sqrt(16)'"
        )

    def _import_renzmc_module(self, module_name, alias=None):
        try:
            module = self.module_manager.load_module(module_name, alias)
            module_var_name = alias or module_name.replace(".", "_")
            self.global_scope[module_var_name] = module
            return module
        except Exception as e:
            raise RuntimeError(
                f"Error mengimpor modul RenzmcLang '{module_name}': {str(e)}"
            )

    def _import_from_renzmc_module(self, module_name, *items):
        try:
            imported_items = self.module_manager.import_from_module(
                module_name, list(items)
            )
            for item_name, item_value in imported_items.items():
                self.global_scope[item_name] = item_value
            return imported_items
        except Exception as e:
            raise RuntimeError(
                f"Error mengimpor dari modul RenzmcLang '{module_name}': {str(e)}"
            )

    def _import_all_from_renzmc_module(self, module_name):
        try:
            imported_items = self.module_manager.import_all_from_module(module_name)
            for item_name, item_value in imported_items.items():
                if not item_name.startswith("_"):
                    self.global_scope[item_name] = item_value
            return imported_items
        except Exception as e:
            raise RuntimeError(
                f"Error mengimpor semua dari modul RenzmcLang '{module_name}': {str(e)}"
            )

    def _reload_renzmc_module(self, module_name):
        try:
            return self.module_manager.reload_module(module_name)
        except Exception as e:
            raise RuntimeError(
                f"Error memuat ulang modul RenzmcLang '{module_name}': {str(e)}"
            )

    def _list_renzmc_modules(self):
        return self.module_manager.list_available_modules()

    def _get_renzmc_module_info(self, module_name):
        return self.module_manager.get_module_info(module_name)

    def _add_module_search_path(self, path):
        try:
            self.module_manager.add_search_path(path)
            return True
        except Exception:
            return False

    def _create_decorator(self, name, decorator_func):
        return self.advanced_features.create_decorator(name, decorator_func)

    def _apply_decorator(self, decorator_name, func):
        return self.advanced_features.apply_decorator(decorator_name, func)

    def _create_context_manager(self, name, enter_func=None, exit_func=None):
        return self.advanced_features.create_context_manager(
            name, enter_func, exit_func
        )

    def _use_context_manager(self, context_manager, action_func):
        try:
            with context_manager:
                return action_func()
        except Exception as e:
            raise RuntimeError(f"Error menggunakan context manager: {str(e)}")

    def _create_advanced_generator(self, name, generator_func, *args, **kwargs):
        return self.advanced_features.create_generator(
            name, generator_func, *args, **kwargs
        )

    def _create_async_function(self, name, func):
        return self.advanced_features.create_async_function(name, func)

    def _list_advanced_features(self):
        return self.advanced_features.list_features()

    def _create_generator(self, func, *args, **kwargs):
        if callable(func):
            return func(*args, **kwargs)
        else:
            raise TypeError(f"Objek '{func}' tidak dapat dipanggil sebagai generator")

    def _run_async_function(self, coro):
        if asyncio.iscoroutine(coro):
            return self.loop.run_until_complete(coro)
        else:
            raise TypeError(f"Objek '{coro}' bukan coroutine")

    def _wait_all_async(self, coros):
        if all((asyncio.iscoroutine(coro) for coro in coros)):
            return self.loop.run_until_complete(asyncio.gather(*coros))
        else:
            raise TypeError("Semua objek harus berupa coroutine")

    def _list_to_generator(self, lst):
        if hasattr(lst, "__iter__"):

            def gen():
                for item in lst:
                    yield item

            return gen()
        else:
            raise TypeError(f"Objek '{lst}' tidak dapat diiterasi")

    def _check_type(self, obj, type_name):
        if type_name == "None" or type_name == "NoneType":
            return obj is None
        if "|" in type_name:
            union_types = [t.strip() for t in type_name.split("|")]
            return any((self._check_type(obj, t) for t in union_types))
        list_match = re.match("(?:list|array)\\[(.*)\\]", type_name)
        if list_match:
            if not isinstance(obj, list):
                return False
            if not obj:
                return True
            element_type = list_match.group(1)
            return all((self._check_type(item, element_type) for item in obj))
        dict_match = re.match("dict\\[(.*),(.*)\\]", type_name)
        if dict_match:
            if not isinstance(obj, dict):
                return False
            if not obj:
                return True
            key_type = dict_match.group(1).strip()
            value_type = dict_match.group(2).strip()
            return all(
                (
                    self._check_type(k, key_type) and self._check_type(v, value_type)
                    for k, v in obj.items()
                )
            )
        tuple_match = re.match("tuple\\[(.*)\\]", type_name)
        if tuple_match:
            if not isinstance(obj, tuple):
                return False
            element_types = [t.strip() for t in tuple_match.group(1).split(",")]
            if len(obj) != len(element_types):
                return False
            return all(
                (self._check_type(obj[i], element_types[i]) for i in range(len(obj)))
            )
        optional_match = re.match("Optional\\[(.*)\\]", type_name)
        if optional_match:
            if obj is None:
                return True
            return self._check_type(obj, optional_match.group(1))
        if type_name.endswith("?"):
            if obj is None:
                return True
            return self._check_type(obj, type_name[:-1])
        if type_name == "callable" or type_name == "Callable":
            return callable(obj)
        if type_name in self.type_registry:
            try:
                expected_type = self.type_registry[type_name]
                if isinstance(expected_type, type):
                    return isinstance(obj, expected_type)
            except TypeError as e:
                # Type checking failed - this is expected for non-type objects
                log_exception("type validation", e, level="debug")
            return False
        elif hasattr(py_builtins, type_name):
            try:
                expected_type = getattr(py_builtins, type_name)
                if isinstance(expected_type, type):
                    return isinstance(obj, expected_type)
            except TypeError as e:
                # Type checking failed - this is expected for non-type objects
                log_exception("type validation", e, level="debug")
            return False
        elif type_name.lower() == "string" or type_name.lower() == "str":
            return isinstance(obj, str)
        elif type_name.lower() == "integer" or type_name.lower() == "int":
            return isinstance(obj, int)
        elif type_name.lower() == "float" or type_name.lower() == "double":
            return isinstance(obj, float)
        elif type_name.lower() == "boolean" or type_name.lower() == "bool":
            return isinstance(obj, bool)
        elif type_name.lower() == "list" or type_name.lower() == "array":
            return isinstance(obj, list)
        elif type_name.lower() == "dict" or type_name.lower() == "dictionary":
            return isinstance(obj, dict)
        elif type_name.lower() == "tuple":
            return isinstance(obj, tuple)
        elif type_name.lower() == "set":
            return isinstance(obj, set)
        elif type_name.lower() == "any":
            return True
        return False

    def _format_string(self, template, **kwargs):
        return template.format(**kwargs)

    def _open_file(self, filename, mode="r"):
        try:
            return open(filename, mode)
        except Exception as e:
            raise FileError(f"Gagal membuka file '{filename}': {str(e)}")

    def _close_file(self, file):
        try:
            file.close()
        except Exception as e:
            raise FileError(f"Gagal menutup file: {str(e)}")

    def _read_line(self, file):
        try:
            return file.readline()
        except Exception as e:
            raise FileError(f"Gagal membaca baris dari file: {str(e)}")

    def _read_all_lines(self, file):
        try:
            return file.readlines()
        except Exception as e:
            raise FileError(f"Gagal membaca semua baris dari file: {str(e)}")

    def _write_line(self, file, line):
        try:
            file.write(line)
        except Exception as e:
            raise FileError(f"Gagal menulis ke file: {str(e)}")

    def _flush_file(self, file):
        try:
            file.flush()
        except Exception as e:
            raise FileError(f"Gagal flush file: {str(e)}")

    def _file_exists(self, path):
        try:
            import os.path

            return os.path.exists(path)
        except Exception as e:
            raise FileError(f"Gagal memeriksa keberadaan file '{path}': {str(e)}")

    def _make_directory(self, path):
        try:
            import os

            os.makedirs(path, exist_ok=True)
        except Exception as e:
            raise FileError(f"Gagal membuat direktori '{path}': {str(e)}")

    def _remove_directory(self, path):
        try:
            import shutil

            shutil.rmtree(path)
        except Exception as e:
            raise FileError(f"Gagal menghapus direktori '{path}': {str(e)}")

    def _list_directory(self, path="."):
        try:
            import os

            return os.listdir(path)
        except Exception as e:
            raise FileError(f"Gagal membaca direktori '{path}': {str(e)}")

    def _join_path(self, *paths):
        try:
            import os.path

            return os.path.join(*paths)
        except Exception as e:
            raise FileError(f"Gagal menggabungkan path: {str(e)}")

    def _file_path(self, path):
        try:
            import os.path

            return os.path.basename(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan nama file dari '{path}': {str(e)}")

    def _directory_path(self, path):
        try:
            import os.path

            return os.path.dirname(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan direktori dari '{path}': {str(e)}")

    def _file_size(self, path):
        try:
            import os.path

            return os.path.getsize(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan ukuran file '{path}': {str(e)}")

    def _file_modification_time(self, path):
        try:
            import os.path

            return os.path.getmtime(path)
        except Exception as e:
            raise FileError(
                f"Gagal mendapatkan waktu modifikasi file '{path}': {str(e)}"
            )

    def _json_to_text(self, obj):
        try:
            import json

            return json.dumps(obj)
        except Exception as e:
            raise ValueError(f"Gagal mengkonversi objek ke JSON: {str(e)}")

    def _text_to_json(self, text):
        try:
            import json

            return json.loads(text)
        except Exception as e:
            raise ValueError(f"Gagal mengkonversi JSON ke objek: {str(e)}")

    def _encrypt(self, text, key):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError(
                "Modul 'cryptography' tidak terinstal. Silakan instal dengan 'pip install cryptography'"
            )
        try:
            import base64

            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

            salt = b"renzmc_salt"
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000
            )
            key_bytes = kdf.derive(key.encode())
            key_base64 = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(key_base64)
            encrypted = f.encrypt(text.encode())
            return base64.urlsafe_b64encode(encrypted).decode()
        except Exception as e:
            raise ValueError(f"Gagal mengenkripsi teks: {str(e)}")

    def _decrypt(self, encrypted_text, key):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError(
                "Modul 'cryptography' tidak terinstal. Silakan instal dengan 'pip install cryptography'"
            )
        try:
            import base64

            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

            salt = b"renzmc_salt"
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000
            )
            key_bytes = kdf.derive(key.encode())
            key_base64 = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(key_base64)
            encrypted = base64.urlsafe_b64decode(encrypted_text.encode())
            decrypted = f.decrypt(encrypted)
            return decrypted.decode()
        except Exception as e:
            raise ValueError(f"Gagal mendekripsi teks: {str(e)}")

    def _hash_text(self, text, algorithm="sha256"):
        try:
            import hashlib

            if algorithm == "md5":
                return hashlib.md5(text.encode()).hexdigest()
            elif algorithm == "sha1":
                return hashlib.sha1(text.encode()).hexdigest()
            elif algorithm == "sha256":
                return hashlib.sha256(text.encode()).hexdigest()
            elif algorithm == "sha512":
                return hashlib.sha512(text.encode()).hexdigest()
            else:
                raise ValueError(f"Algoritma hash '{algorithm}' tidak didukung")
        except Exception as e:
            raise ValueError(f"Gagal melakukan hash teks: {str(e)}")

    def _create_uuid(self):
        try:
            import uuid

            return str(uuid.uuid4())
        except Exception as e:
            raise ValueError(f"Gagal membuat UUID: {str(e)}")

    def _url_encode(self, text):
        try:
            import urllib.parse

            return urllib.parse.quote(text)
        except Exception as e:
            raise ValueError(f"Gagal melakukan URL encode: {str(e)}")

    def _url_decode(self, text):
        try:
            import urllib.parse

            return urllib.parse.unquote(text)
        except Exception as e:
            raise ValueError(f"Gagal melakukan URL decode: {str(e)}")

    def _http_request(
        self, url, method="GET", headers=None, data=None, json=None, timeout=30
    ):
        try:
            import requests

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                json=json,
                timeout=timeout,
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP request: {str(e)}")

    def _http_get(self, url, headers=None, params=None, timeout=30):
        try:
            import requests

            response = requests.get(
                url, headers=headers, params=params, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP GET request: {str(e)}")

    def _http_post(self, url, headers=None, data=None, json=None, timeout=30):
        try:
            import requests

            response = requests.post(
                url, headers=headers, data=data, json=json, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP POST request: {str(e)}")

    def _http_put(self, url, headers=None, data=None, json=None, timeout=30):
        try:
            import requests

            response = requests.put(
                url, headers=headers, data=data, json=json, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP PUT request: {str(e)}")

    def _http_delete(self, url, headers=None, timeout=30):
        try:
            import requests

            response = requests.delete(url, headers=headers, timeout=timeout)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP DELETE request: {str(e)}")

    def get_variable(self, name):
        if (
            self.current_instance is not None
            and self.current_instance in self.instance_scopes
        ):
            instance_scope = self.instance_scopes[self.current_instance]
            if name in instance_scope:
                return instance_scope[name]
        if name in self.local_scope:
            return self.local_scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        if name in self.builtin_functions:
            return self.builtin_functions[name]
        raise NameError(f"Variabel '{name}' tidak ditemukan")

    def set_variable(self, name, value, is_local=False):
        if self.current_instance is not None:
            if self.current_instance not in self.instance_scopes:
                self.instance_scopes[self.current_instance] = {}
            self.instance_scopes[self.current_instance][name] = value
            return value
        if is_local or name in self.local_scope:
            self.local_scope[name] = value
        else:
            self.global_scope[name] = value
        return value

    def visit_Program(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
        return result

    def visit_Block(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
        return result

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op.type == TokenType.TAMBAH:
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.op.type == TokenType.KURANG:
            return left - right
        elif node.op.type == TokenType.KALI_OP:
            if isinstance(left, str) and isinstance(right, int):
                return left * right
            elif isinstance(left, int) and isinstance(right, str):
                return right * left
            return left * right
        elif node.op.type == TokenType.BAGI:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left / right
        elif node.op.type == TokenType.SISA_BAGI:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left % right
        elif node.op.type == TokenType.PANGKAT:
            return left**right
        elif node.op.type == TokenType.PEMBAGIAN_BULAT:
            if right == 0:
                raise DivisionByZeroError("Pembagian dengan nol tidak diperbolehkan")
            return left // right
        elif node.op.type == TokenType.SAMA_DENGAN:
            return left == right
        elif node.op.type == TokenType.TIDAK_SAMA:
            return left != right
        elif node.op.type == TokenType.LEBIH_DARI:
            return left > right
        elif node.op.type == TokenType.KURANG_DARI:
            return left < right
        elif node.op.type == TokenType.LEBIH_SAMA:
            return left >= right
        elif node.op.type == TokenType.KURANG_SAMA:
            return left <= right
        elif node.op.type == TokenType.DAN:
            return left and right
        elif node.op.type == TokenType.ATAU:
            return left or right
        elif node.op.type in (TokenType.BIT_DAN, TokenType.BITWISE_AND):
            return int(left) & int(right)
        elif node.op.type in (TokenType.BIT_ATAU, TokenType.BITWISE_OR):
            return int(left) | int(right)
        elif node.op.type in (TokenType.BIT_XOR, TokenType.BITWISE_XOR):
            return int(left) ^ int(right)
        elif node.op.type == TokenType.GESER_KIRI:
            return int(left) << int(right)
        elif node.op.type == TokenType.GESER_KANAN:
            return int(left) >> int(right)
        elif node.op.type in (TokenType.DALAM, TokenType.DALAM_OP):
            if not hasattr(right, "__iter__") and not hasattr(right, "__contains__"):
                raise TypeError(
                    f"argument of type '{type(right).__name__}' is not iterable"
                )
            return left in right
        elif node.op.type == TokenType.TIDAK_DALAM:
            if not hasattr(right, "__iter__") and not hasattr(right, "__contains__"):
                raise TypeError(
                    f"argument of type '{type(right).__name__}' is not iterable"
                )
            return left not in right
        elif node.op.type in (TokenType.ADALAH, TokenType.ADALAH_OP):
            return left is right
        elif node.op.type == TokenType.BUKAN:
            return left is not right
        raise RuntimeError(f"Operator tidak didukung: {node.op.type}")

    def visit_UnaryOp(self, node):
        expr = self.visit(node.expr)
        if node.op.type == TokenType.TAMBAH:
            return +expr
        elif node.op.type == TokenType.KURANG:
            return -expr
        elif node.op.type in (TokenType.TIDAK, TokenType.NOT):
            return not expr
        elif node.op.type in (TokenType.BIT_NOT, TokenType.BITWISE_NOT):
            return ~int(expr)
        raise RuntimeError(f"Operator unary tidak didukung: {node.op.type}")

    def visit_Num(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_NoneValue(self, node):
        return None

    def visit_List(self, node):
        return [self.visit(element) for element in node.elements]

    def visit_Dict(self, node):
        return {self.visit(key): self.visit(value) for key, value in node.pairs}

    def visit_Set(self, node):
        return {self.visit(element) for element in node.elements}

    def visit_Tuple(self, node):
        return tuple((self.visit(element) for element in node.elements))

    def visit_Var(self, node):
        return self.get_variable(node.name)

    def visit_VarDecl(self, node):
        value = self.visit(node.value)

        if node.type_hint:
            try:
                self._check_variable_type(node.var_name, value, node.type_hint)
            except Exception:
                type_name = node.type_hint.type_name
                if type_name in self.type_registry:
                    expected_type = self.type_registry[type_name]
                    try:
                        if isinstance(expected_type, type) and not isinstance(
                            value, expected_type
                        ):
                            raise TypeHintError(
                                f"Nilai '{value}' bukan tipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(
                            value, expected_type
                        ):
                            raise TypeHintError(
                                f"Nilai '{value}' bukan tipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")

        return self.set_variable(node.var_name, value)

    def visit_Assign(self, node):
        value = self.visit(node.value)
        if isinstance(node.var, Var):
            return self.set_variable(node.var.name, value)
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                self.instance_scopes[id(obj)][attr] = value
                return value
            elif hasattr(obj, attr):
                setattr(obj, attr, value)
                return value
            elif isinstance(obj, dict):
                obj[attr] = value
                return value
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            if isinstance(obj, (list, dict)):
                obj[index] = value
                return value
            else:
                raise TypeError(
                    f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan"
                )
        raise RuntimeError(f"Tipe assignment tidak didukung: {type(node.var).__name__}")

    def visit_CompoundAssign(self, node):
        from renzmc.core.token import TokenType

        if isinstance(node.var, Var):
            current_value = self.get_variable(node.var.name)
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            current_value = obj[index]
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                current_value = self.instance_scopes[id(obj)].get(attr)
            elif hasattr(obj, attr):
                current_value = getattr(obj, attr)
            elif isinstance(obj, dict):
                current_value = obj[attr]
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
        else:
            raise RuntimeError(
                f"Tipe compound assignment tidak didukung: {type(node.var).__name__}"
            )
        operand = self.visit(node.value)
        if node.op.type == TokenType.TAMBAH_SAMA_DENGAN:
            new_value = current_value + operand
        elif node.op.type == TokenType.KURANG_SAMA_DENGAN:
            new_value = current_value - operand
        elif node.op.type == TokenType.KALI_SAMA_DENGAN:
            new_value = current_value * operand
        elif node.op.type == TokenType.BAGI_SAMA_DENGAN:
            new_value = current_value / operand
        elif node.op.type == TokenType.SISA_SAMA_DENGAN:
            new_value = current_value % operand
        elif node.op.type == TokenType.PANGKAT_SAMA_DENGAN:
            new_value = current_value**operand
        elif node.op.type == TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN:
            new_value = current_value // operand
        elif node.op.type in (
            TokenType.BIT_DAN_SAMA_DENGAN,
            TokenType.BITWISE_AND_SAMA_DENGAN,
        ):
            new_value = current_value & operand
        elif node.op.type in (
            TokenType.BIT_ATAU_SAMA_DENGAN,
            TokenType.BITWISE_OR_SAMA_DENGAN,
        ):
            new_value = current_value | operand
        elif node.op.type in (
            TokenType.BIT_XOR_SAMA_DENGAN,
            TokenType.BITWISE_XOR_SAMA_DENGAN,
        ):
            new_value = current_value ^ operand
        elif node.op.type == TokenType.GESER_KIRI_SAMA_DENGAN:
            new_value = current_value << operand
        elif node.op.type == TokenType.GESER_KANAN_SAMA_DENGAN:
            new_value = current_value >> operand
        else:
            raise RuntimeError(
                f"Operator compound assignment tidak dikenal: {node.op.type}"
            )
        if isinstance(node.var, Var):
            return self.set_variable(node.var.name, new_value)
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            obj[index] = new_value
            return new_value
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                self.instance_scopes[id(obj)][attr] = new_value
            elif hasattr(obj, attr):
                setattr(obj, attr, new_value)
            elif isinstance(obj, dict):
                obj[attr] = new_value
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
            return new_value

    def visit_MultiVarDecl(self, node):
        values = self.visit(node.values)
        if isinstance(values, (list, tuple)):
            if len(node.var_names) != len(values):
                raise ValueError(
                    f"Tidak dapat membongkar {len(values)} nilai menjadi {len(node.var_names)} variabel"
                )
            results = []
            for var_name, value in zip(node.var_names, values):
                result = self.set_variable(var_name, value)
                results.append(result)
            return tuple(results)
        elif len(node.var_names) == 1:
            return self.set_variable(node.var_names[0], values)
        else:
            raise ValueError(
                f"Tidak dapat membongkar 1 nilai menjadi {len(node.var_names)} variabel"
            )

    def visit_MultiAssign(self, node):
        values = self.visit(node.values)
        if isinstance(values, (list, tuple)):
            if len(node.vars) != len(values):
                raise ValueError(
                    f"Tidak dapat membongkar {len(values)} nilai menjadi {len(node.vars)} variabel"
                )
            results = []
            for var_node, value in zip(node.vars, values):
                if isinstance(var_node, Var):
                    result = self.set_variable(var_node.name, value)
                elif isinstance(var_node, AttributeRef):
                    obj = self.visit(var_node.obj)
                    attr = var_node.attr
                    if hasattr(obj, attr):
                        setattr(obj, attr, value)
                    elif isinstance(obj, dict):
                        obj[attr] = value
                    else:
                        raise AttributeError(
                            f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                        )
                    result = value
                elif isinstance(var_node, IndexAccess):
                    obj = self.visit(var_node.obj)
                    index = self.visit(var_node.index)
                    if isinstance(obj, (list, dict)):
                        obj[index] = value
                    else:
                        raise TypeError(
                            f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan"
                        )
                    result = value
                else:
                    raise RuntimeError(
                        f"Tipe assignment tidak didukung: {type(var_node).__name__}"
                    )
                results.append(result)
            return tuple(results)
        elif len(node.vars) == 1:
            var_node = node.vars[0]
            if isinstance(var_node, Var):
                return self.set_variable(var_node.name, values)
            else:
                from renzmc.core.ast import Assign as AssignNode

                temp_assign = AssignNode(var_node, node.values)
                return self.visit_Assign(temp_assign)
        else:
            raise ValueError(
                f"Tidak dapat membongkar 1 nilai menjadi {len(node.vars)} variabel"
            )

    def visit_NoOp(self, node):
        pass

    def visit_Print(self, node):
        value = self.visit(node.expr)
        print(value)
        return None

    def visit_Input(self, node):
        prompt = self.visit(node.prompt)
        value = input(prompt)
        if node.var_name:
            try:
                int_value = int(value)
                self.set_variable(node.var_name, int_value)
                return int_value
            except ValueError:
                try:
                    float_value = float(value)
                    self.set_variable(node.var_name, float_value)
                    return float_value
                except ValueError:
                    self.set_variable(node.var_name, value)
                    return value
        return value

    def visit_If(self, node):
        condition = self.visit(node.condition)
        if condition:
            if_block = Block(node.if_body)
            return self.visit(if_block)
        elif node.else_body:
            else_block = Block(node.else_body)
            return self.visit(else_block)
        return None

    def visit_While(self, node):
        result = None
        while self.visit(node.condition):
            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_For(self, node):
        var_name = node.var_name
        start = self.visit(node.start)
        end = self.visit(node.end)
        result = None
        for i in range(start, end + 1):
            self.set_variable(var_name, i)
            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_ForEach(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        result = None
        if not hasattr(iterable, "__iter__"):
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
        for item in iterable:
            if isinstance(var_name, tuple):
                if hasattr(item, "__iter__") and not isinstance(item, str):
                    unpacked = list(item)
                    if len(unpacked) != len(var_name):
                        raise ValueError(
                            f"Tidak dapat unpack {len(unpacked)} nilai ke {len(var_name)} variabel"
                        )
                    for var, val in zip(var_name, unpacked):
                        self.set_variable(var, val)
                else:
                    raise TypeError(
                        f"Tidak dapat unpack nilai tipe '{type(item).__name__}'"
                    )
            else:
                self.set_variable(var_name, item)

            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_Break(self, node):
        self.break_flag = True

    def visit_Continue(self, node):
        self.continue_flag = True

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
            has_manual_jit = (
                hasattr(self, "_jit_hints") and name in self._jit_hints
            ) or (hasattr(self, "_jit_force") and name in self._jit_force)
            if not has_manual_jit:
                self.jit_call_counts[name] = 0
                self.jit_execution_times[name] = 0.0

        def renzmc_function(*args, **kwargs):
            return self._execute_user_function(
                name, params, body, return_type, param_types, list(args), kwargs
            )

        renzmc_function.__name__ = name
        renzmc_function.__renzmc_function__ = True
        self.global_scope[name] = renzmc_function

        # Return the function so decorators can work with it
        return renzmc_function

    def visit_FuncCall(self, node):
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
                        raise RuntimeError(
                            f"Error dalam pemanggilan fungsi '{func_name}': {str(e)}"
                        )
                else:
                    raise RuntimeError(
                        f"Objek '{type(func).__name__}' tidak dapat dipanggil"
                    )
            except NameError:
                if isinstance(node.func_expr, Var):
                    func_name = node.func_expr.name
                    args = [self.visit(arg) for arg in node.args]
                    kwargs = {k: self.visit(v) for k, v in node.kwargs.items()}
                    if func_name in self.functions:
                        params, body, return_type, param_types = self.functions[
                            func_name
                        ]
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
            if (
                hasattr(self, "_decorated_functions")
                and name in self._decorated_functions
            ):
                decorator_data = self._decorated_functions[name]

                # Check if this is a wrapped function (new style) or decorator+func tuple (old style)
                if callable(decorator_data):
                    # New style: decorator_data is the already-wrapped function
                    try:
                        return decorator_data(*args, **kwargs)
                    except Exception as e:
                        raise RuntimeError(
                            f"Error dalam fungsi terdekorasi '{name}': {str(e)}"
                        )
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
                            # For wrapper decorators, call the decorator with function and args
                            return raw_decorator_func(original_func, *args, **kwargs)
                    except Exception as e:
                        raise RuntimeError(
                            f"Error dalam fungsi terdekorasi '{name}': {str(e)}"
                        )
            if name not in self.functions:
                raise NameError(f"Fungsi '{name}' tidak ditemukan")
            function_data = self.functions[name]
            if len(function_data) == 5 and function_data[4] == "ASYNC":
                params, body, return_type, param_types, _ = function_data

                async def async_coroutine():
                    return self._execute_user_function(
                        name, params, body, return_type, param_types, args, kwargs
                    )

                return async_coroutine()
            else:
                params, body, return_type, param_types = function_data
                return self._execute_user_function(
                    name, params, body, return_type, param_types, args, kwargs
                )

    def _execute_user_function(
        self, name, params, body, return_type, param_types, args, kwargs
    ):
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
                raise RuntimeError(
                    f"Parameter '{param_name}' tidak ada dalam fungsi '{name}'"
                )
            if param_name in param_values:
                raise RuntimeError(
                    f"Parameter '{param_name}' mendapat nilai ganda (posisional dan kata kunci)"
                )
            param_values[param_name] = value
        missing_params = [p for p in params if p not in param_values]
        if missing_params:
            raise RuntimeError(
                f"Parameter hilang dalam fungsi '{name}': {', '.join(missing_params)}"
            )
        if param_types:
            for param_name, value in param_values.items():
                if param_name in param_types:
                    type_hint = param_types[param_name]
                    type_name = type_hint.type_name
                    if type_name in self.type_registry:
                        expected_type = self.type_registry[type_name]
                        try:
                            if isinstance(expected_type, type) and not isinstance(
                                value, expected_type
                            ):
                                raise TypeHintError(
                                    f"Parameter '{param_name}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(
                                value, expected_type
                            ):
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
                        if isinstance(expected_type, type) and not isinstance(
                            return_value, expected_type
                        ):
                            raise TypeHintError(
                                f"Nilai kembali fungsi '{name}' harus bertipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(
                            return_value, expected_type
                        ):
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
                    is_valid, error_msg = AdvancedTypeValidator.validate(
                        return_value, type_spec, "return"
                    )
                    if not is_valid:
                        raise TypeHintError(f"Fungsi '{name}': {error_msg}")
        self.local_scope = old_local_scope
        self.return_value = None

        if JIT_AVAILABLE and name in self.jit_call_counts:
            execution_time = time.time() - start_time
            self.jit_call_counts[name] += 1
            self.jit_execution_times[name] += execution_time

            if (
                self.jit_call_counts[name] >= self.jit_threshold
                and name not in self.jit_compiled_functions
            ):
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
                compiled_func = self.jit_compiler.force_compile(
                    name, params, body, interpreter_func
                )
            else:
                compiled_func = self.jit_compiler.compile_function(
                    name, params, body, interpreter_func
                )

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
                return self._execute_user_function(
                    name, params, body, return_type, param_types, all_args, kwargs
                )
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
                raise RuntimeError(
                    f"User function '{name}' not found for decorator factory"
                )

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
            constructor_params, constructor_body, param_types = class_info[
                "constructor"
            ]
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

    def visit_Return(self, node):
        if node.expr:
            self.return_value = self.visit(node.expr)
        else:
            self.return_value = None
        return self.return_value

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
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
        elif hasattr(obj, attr):
            return getattr(obj, attr)
        elif isinstance(obj, dict) and attr in obj:
            return obj[attr]
        else:
            if (
                hasattr(obj, "__name__")
                and hasattr(obj, "__package__")
                and (not isinstance(obj, dict))
            ):
                try:
                    submodule_name = f"{obj.__name__}.{attr}"
                    submodule = importlib.import_module(submodule_name)
                    setattr(obj, attr, submodule)
                    return submodule
                except ImportError:
                    # Module not available - continuing without it
                    handle_import_error(
                        "module", "import operation", "Continuing without module"
                    )
            raise AttributeError(
                f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
            )

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
            if (
                class_name in self.classes
                and method in self.classes[class_name]["methods"]
            ):
                old_instance = self.current_instance
                old_local_scope = self.local_scope.copy()
                self.current_instance = id(obj)
                self.local_scope = {}
                params, body, return_type, param_types = self.classes[class_name][
                    "methods"
                ][method]
                self.local_scope["diri"] = obj
                if params and len(params) > 0:
                    start_param_idx = 1 if params[0] == "diri" else 0
                    expected_user_params = len(params) - start_param_idx
                    if len(args) != expected_user_params:
                        raise RuntimeError(
                            f"Metode '{method}' membutuhkan {expected_user_params} parameter, tetapi {len(args)} diberikan"
                        )
                    if param_types and len(param_types) > start_param_idx:
                        for i, (arg, type_hint) in enumerate(
                            zip(args, param_types[start_param_idx:])
                        ):
                            type_name = type_hint.type_name
                            if type_name in self.type_registry:
                                expected_type = self.type_registry[type_name]
                                try:
                                    if isinstance(
                                        expected_type, type
                                    ) and not isinstance(arg, expected_type):
                                        raise TypeHintError(
                                            f"Parameter ke-{i + 1} '{params[i + start_param_idx]}' harus bertipe '{type_name}'"
                                        )
                                except TypeError as e:
                                    # Type checking failed - this is expected for non-type objects
                                    log_exception("type validation", e, level="debug")
                            elif hasattr(py_builtins, type_name):
                                expected_type = getattr(py_builtins, type_name)
                                try:
                                    if isinstance(
                                        expected_type, type
                                    ) and not isinstance(arg, expected_type):
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
                            if isinstance(expected_type, type) and not isinstance(
                                return_value, expected_type
                            ):
                                raise TypeHintError(
                                    f"Nilai kembali metode '{method}' harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(
                                return_value, expected_type
                            ):
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
        raise AttributeError(
            f"Objek '{type(obj).__name__}' tidak memiliki metode '{method}'"
        )

    def visit_Import(self, node):
        module = node.module
        alias = node.alias or module
        try:
            rmc_module = self._load_rmc_module(module)
            if rmc_module:
                self.modules[alias] = rmc_module
                self.global_scope[alias] = rmc_module
                if hasattr(rmc_module, "get_exports"):
                    exports = rmc_module.get_exports()
                    for name, value in exports.items():
                        self.global_scope[name] = value
                        if (
                            hasattr(self, "local_scope")
                            and self.local_scope is not None
                        ):
                            self.local_scope[name] = value
                return
            try:
                imported_module = __import__(
                    f"renzmc.builtins.{module}", fromlist=["*"]
                )
                self.modules[alias] = imported_module
                self.global_scope[alias] = imported_module
            except ImportError:
                imported_module = importlib.import_module(module)
                self.modules[alias] = imported_module
                self.global_scope[alias] = imported_module
        except ImportError:
            raise ImportError(f"Modul '{module}' tidak ditemukan")

    def visit_FromImport(self, node):
        """
        Handle 'dari module impor item1, item2' statements
        Supports:
        - Nested modules like 'dari Ren.renz impor Class1, Class2'
        - Wildcard imports like 'dari module impor *'
        - Relative imports like 'dari .module impor func'
        """
        module = node.module
        items = node.items  # List of (name, alias) tuples
        is_relative = getattr(node, "is_relative", False)
        relative_level = getattr(node, "relative_level", 0)

        # Handle relative imports
        resolved_path = None
        if is_relative:
            # Get current file path from interpreter context
            current_file = getattr(self, "current_file", None)
            if not current_file:
                raise ImportError(
                    "Tidak dapat menggunakan relative import: file path tidak tersedia"
                )

            # Resolve relative path using module manager
            try:
                resolved_path = self.module_manager.resolve_relative_import(
                    module, relative_level, current_file
                )
                # Extract module name from path for caching
                import os

                module = os.path.splitext(os.path.basename(resolved_path))[0]

                # Add the directory to search paths temporarily
                module_dir = os.path.dirname(resolved_path)
                if module_dir not in self.module_manager.module_search_paths:
                    self.module_manager.add_search_path(module_dir)
            except Exception as e:
                raise ImportError(f"Error resolving relative import: {str(e)}")

        # Check for wildcard import
        is_wildcard = len(items) == 1 and items[0][0] == "*"

        if is_wildcard:
            # Use the module_manager's import_all method
            try:
                all_items = self.module_manager.import_all_from_module(module)
                # Add all items to scope
                for name, value in all_items.items():
                    self.global_scope[name] = value
                    if hasattr(self, "local_scope") and self.local_scope is not None:
                        self.local_scope[name] = value
                return
            except Exception as e:
                # Try Python module import as fallback
                pass

        # Try to import specific items using module_manager
        try:
            item_names = [item[0] for item in items]
            imported_items = self.module_manager.import_from_module(module, item_names)

            # Add items to scope with aliases if specified
            for item_name, alias in items:
                actual_name = alias if alias else item_name
                if item_name in imported_items:
                    value = imported_items[item_name]
                    self.global_scope[actual_name] = value
                    if hasattr(self, "local_scope") and self.local_scope is not None:
                        self.local_scope[actual_name] = value
            return
        except Exception as e:
            # Try Python module import as fallback
            pass

        # Fallback to Python module import
        try:
            if is_wildcard:
                # Import all from Python module
                try:
                    imported_module = __import__(
                        f"renzmc.builtins.{module}", fromlist=["*"]
                    )
                except ImportError:
                    imported_module = importlib.import_module(module)

                # Get all public attributes
                if hasattr(imported_module, "__all__"):
                    all_names = imported_module.__all__
                else:
                    all_names = [
                        name
                        for name in dir(imported_module)
                        if not name.startswith("_")
                    ]

                for name in all_names:
                    if hasattr(imported_module, name):
                        value = getattr(imported_module, name)
                        self.global_scope[name] = value
            else:
                # Import specific items
                try:
                    imported_module = __import__(
                        f"renzmc.builtins.{module}",
                        fromlist=[item[0] for item in items],
                    )
                except ImportError:
                    imported_module = importlib.import_module(module)

                for item_name, alias in items:
                    actual_name = alias if alias else item_name
                    if hasattr(imported_module, item_name):
                        value = getattr(imported_module, item_name)
                        self.global_scope[actual_name] = value
                    else:
                        raise ImportError(
                            f"Tidak dapat mengimpor '{item_name}' dari modul '{module}'"
                        )
        except ImportError as e:
            raise ImportError(f"Modul '{module}' tidak ditemukan: {str(e)}")

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
                                            builtin_func = getattr(
                                                renzmc_builtins, name
                                            )
                                            if value is builtin_func:
                                                is_builtin = True
                                    except:
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
                    raise ImportError(
                        f"Gagal memuat modul RenzMC '{module_name}': {str(e)}"
                    )
        return None

    def visit_PythonImport(self, node):
        module = node.module
        alias = node.alias
        try:
            if not hasattr(self, "python_integration"):
                from renzmc.runtime.python_integration import PythonIntegration

                self.python_integration = PythonIntegration()
            wrapped_module = self.python_integration.import_python_module(module, alias)
            if alias:
                var_name = alias
                self.modules[var_name] = wrapped_module
                self.global_scope[var_name] = wrapped_module
            elif "." in module:
                parts = module.split(".")
                current_scope = self.global_scope
                current_modules = self.modules
                for i, part in enumerate(parts[:-1]):
                    if part not in current_scope:
                        parent_module_name = ".".join(parts[: i + 1])
                        try:
                            parent_module = importlib.import_module(parent_module_name)
                            wrapped_parent = (
                                self.python_integration.convert_python_to_renzmc(
                                    parent_module
                                )
                            )
                            current_scope[part] = wrapped_parent
                            current_modules[part] = wrapped_parent
                        except ImportError:
                            current_scope[part] = type("SimpleNamespace", (), {})()
                            current_modules[part] = current_scope[part]
                    current_scope = current_scope[part]
                    if hasattr(current_scope, "__dict__"):
                        current_scope = current_scope.__dict__
                    else:
                        break
                final_name = parts[-1]
                if hasattr(current_scope, "__setitem__"):
                    current_scope[final_name] = wrapped_module
                else:
                    setattr(current_scope, final_name, wrapped_module)
                self.modules[module] = wrapped_module
                self.global_scope[module.replace(".", "_")] = wrapped_module
            else:
                self.modules[module] = wrapped_module
                self.global_scope[module] = wrapped_module
        except Exception as e:
            raise RenzmcImportError(
                f"Modul Python '{module}' tidak ditemukan: {str(e)}"
            )

    def visit_PythonCall(self, node):
        func = self.visit(node.func_expr)
        args = [self.visit(arg) for arg in node.args]
        kwargs = {key: self.visit(value) for key, value in node.kwargs.items()}
        return self._call_python_function(func, *args, **kwargs)

    def visit_TryCatch(self, node):
        try:
            return self.visit_Block(Block(node.try_block))
        except Exception as e:
            for exception_type, var_name, except_block in node.except_blocks:
                should_catch = False
                if exception_type is None:
                    should_catch = True
                else:
                    try:
                        exc_type = eval(exception_type)
                        if isinstance(exc_type, type):
                            should_catch = isinstance(e, exc_type)
                    except Exception:
                        should_catch = True

                if should_catch:
                    if var_name:
                        self.set_variable(var_name, e)
                    return self.visit_Block(Block(except_block))
            raise e
        finally:
            if node.finally_block:
                self.visit_Block(Block(node.finally_block))

    def visit_Raise(self, node):
        exception = self.visit(node.exception)
        raise exception

    def visit_Switch(self, node):
        match_value = self.visit(node.expr)
        for case in node.cases:
            for case_value_node in case.values:
                case_value = self.visit(case_value_node)
                if match_value == case_value:
                    return self.visit_Block(Block(case.body))
        if node.default_case:
            return self.visit_Block(Block(node.default_case))
        return None

    def visit_Case(self, node):
        pass

    def visit_With(self, node):
        context_manager = self.visit(node.context_expr)
        if not (
            hasattr(context_manager, "__enter__")
            and hasattr(context_manager, "__exit__")
        ):
            raise TypeError(
                f"Objek tipe '{type(context_manager).__name__}' tidak mendukung context manager protocol"
            )
        context_value = context_manager.__enter__()
        if node.var_name:
            self.set_variable(node.var_name, context_value)
        try:
            result = self.visit_Block(Block(node.body))
            return result
        except Exception as e:
            exc_type = type(e)
            exc_value = e
            exc_traceback = e.__traceback__
            if not context_manager.__exit__(exc_type, exc_value, exc_traceback):
                raise
        finally:
            if not hasattr(self, "_exception_occurred"):
                context_manager.__exit__(None, None, None)

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
            raise TypeError(
                f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan"
            )

    def visit_SliceAccess(self, node):
        obj = self.visit(node.obj)
        start = self.visit(node.start) if node.start else None
        end = self.visit(node.end) if node.end else None
        step = self.visit(node.step) if node.step else None
        try:
            return obj[start:end:step]
        except TypeError:
            raise TypeError(
                f"Objek tipe '{type(obj).__name__}' tidak mendukung slicing"
            )

    def visit_Lambda(self, node):
        params = node.params
        body = node.body
        param_types = node.param_types
        return_type = node.return_type

        def lambda_func(*args):
            if len(args) != len(params):
                raise RuntimeError(
                    f"Lambda membutuhkan {len(params)} parameter, tetapi {len(args)} diberikan"
                )
            if param_types:
                for i, (arg, type_hint) in enumerate(zip(args, param_types)):
                    type_name = type_hint.type_name
                    if type_name in self.type_registry:
                        expected_type = self.type_registry[type_name]
                        try:
                            if isinstance(expected_type, type) and not isinstance(
                                arg, expected_type
                            ):
                                raise TypeHintError(
                                    f"Parameter ke-{i + 1} harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
                            log_exception("type validation", e, level="debug")
                    elif hasattr(py_builtins, type_name):
                        expected_type = getattr(py_builtins, type_name)
                        try:
                            if isinstance(expected_type, type) and not isinstance(
                                arg, expected_type
                            ):
                                raise TypeHintError(
                                    f"Parameter ke-{i + 1} harus bertipe '{type_name}'"
                                )
                        except TypeError as e:
                            # Type checking failed - this is expected for non-type objects
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
                        if isinstance(expected_type, type) and not isinstance(
                            result, expected_type
                        ):
                            raise TypeHintError(
                                f"Nilai kembali lambda harus bertipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(
                            result, expected_type
                        ):
                            raise TypeHintError(
                                f"Nilai kembali lambda harus bertipe '{type_name}'"
                            )
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
            self.local_scope = old_local_scope
            return result

        return lambda_func

    def visit_ListComp(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
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
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
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
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
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

    def visit_Generator(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        if not hasattr(iterable, "__iter__"):
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
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
            raise TypeError(
                f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi"
            )
        return list(iterable)

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
                    self._decorated_functions = getattr(
                        self, "_decorated_functions", {}
                    )

                    def original_func_callable(*call_args, **call_kwargs):
                        if func_name in self.functions:
                            params, body, return_type, param_types = self.functions[
                                func_name
                            ]
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
                            raise NameError(
                                f"Fungsi asli '{func_name}' tidak ditemukan"
                            )

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

    def visit_Ternary(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.if_expr)
        else:
            return self.visit(node.else_expr)

    def visit_Unpacking(self, node):
        value = self.visit(node.expr)
        if not hasattr(value, "__iter__"):
            raise TypeError(
                f"Objek tipe '{type(value).__name__}' tidak dapat diiterasi"
            )
        return value

    def visit_WalrusOperator(self, node):
        value = self.visit(node.value)
        self.set_variable(node.var_name, value)
        return value

    def visit_SelfVar(self, node):
        if self.current_instance is None:
            raise NameError("Variabel 'diri' tidak dapat diakses di luar konteks kelas")
        if "diri" in self.local_scope:
            return self.local_scope["diri"]
        else:
            raise NameError("Variabel 'diri' tidak ditemukan dalam konteks saat ini")

    def visit_NoneType(self, node):
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
                converted_value = self.python_integration.convert_renzmc_to_python(
                    value
                )
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

    def visit_SliceAssign(self, node):
        target = self.visit(node.target)
        start = self.visit(node.start) if node.start else None
        end = self.visit(node.end) if node.end else None
        step = self.visit(node.step) if node.step else None
        value = self.visit(node.value)
        try:
            slice_obj = slice(start, end, step)
            target[slice_obj] = value
        except Exception as e:
            self.error(f"Kesalahan dalam slice assignment: {str(e)}", node.token)

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
            self.error(
                f"Nilai tidak dapat di-unpack: {type(value).__name__} - {e}", node.token
            )

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
