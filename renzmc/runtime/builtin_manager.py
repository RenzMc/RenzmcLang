import renzmc.builtins as renzmc_builtins
from renzmc.library.manager import get_library_manager


class BuiltinManager:

    @staticmethod
    def setup_builtin_functions():
        # Core built-in functions - only essential ones
        builtin_functions = {
            # Core Python built-ins
            "len": len,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "type": type,
            "isinstance": isinstance,
            "range": range,
            "enumerate": enumerate,
            "zip": zip,
            "all": all,
            "any": any,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
            "pow": pow,

            # RenzMcLang string functions
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
            "format_teks": renzmc_builtins.format_teks,
            "adalah_huruf": renzmc_builtins.adalah_huruf,
            "adalah_angka": renzmc_builtins.adalah_angka,
            "adalah_alfanumerik": renzmc_builtins.adalah_alfanumerik,
            "adalah_huruf_besar": renzmc_builtins.adalah_huruf_besar,
            "adalah_huruf_kecil": renzmc_builtins.adalah_huruf_kecil,
            "adalah_spasi": renzmc_builtins.adalah_spasi,

            # Type functions
            "panjang": renzmc_builtins.panjang,
            "jenis": renzmc_builtins.jenis,
            "ke_teks": renzmc_builtins.ke_teks,
            "ke_angka": renzmc_builtins.ke_angka,

            # Dict functions
            "hapus_kunci": renzmc_builtins.hapus_kunci,
            "item": renzmc_builtins.item,
            "kunci": renzmc_builtins.kunci,
            "nilai": renzmc_builtins.nilai,

            # Iteration functions
            "ada": renzmc_builtins.ada,
            "all_func": renzmc_builtins.all_func,
            "any_func": renzmc_builtins.any_func,
            "enumerate_func": renzmc_builtins.enumerate_func,
            "filter_func": renzmc_builtins.filter_func,
            "kurangi": renzmc_builtins.kurangi,
            "map_func": renzmc_builtins.map_func,
            "peta": renzmc_builtins.peta,
            "range_func": renzmc_builtins.range_func,
            "reduce_func": renzmc_builtins.reduce_func,
            "rentang": renzmc_builtins.rentang,
            "reversed": renzmc_builtins.reversed_renzmc,
            "saring": renzmc_builtins.saring,
            "semua": renzmc_builtins.semua,
            "sorted_func": renzmc_builtins.sorted_func,
            "terbalik": renzmc_builtins.terbalik,
            "terurut": renzmc_builtins.terurut,
            "zip_func": renzmc_builtins.zip_func,

            # List functions
            "balikkan": renzmc_builtins.balikkan,
            "extend": renzmc_builtins.extend,
            "hapus": renzmc_builtins.hapus,
            "hapus_pada": renzmc_builtins.hapus_pada,
            "hitung": renzmc_builtins.hitung,
            "indeks": renzmc_builtins.indeks,
            "masukkan": renzmc_builtins.masukkan,
            "salin": renzmc_builtins.salin,
            "salin_dalam": renzmc_builtins.salin_dalam,
            "tambah": renzmc_builtins.tambah,
            "urutkan": renzmc_builtins.urutkan,

            # Utility functions
            "hash_teks": renzmc_builtins.hash_teks,
            "url_encode": renzmc_builtins.url_encode,
            "url_decode": renzmc_builtins.url_decode,
            "regex_match": renzmc_builtins.regex_match,
            "regex_replace": renzmc_builtins.regex_replace,
            "base64_encode": renzmc_builtins.base64_encode,
            "base64_decode": renzmc_builtins.base64_decode,

            # Python integration
            "daftar_modul_python": renzmc_builtins.daftar_modul_python,
            "jalankan_python": renzmc_builtins.jalankan_python,
            "is_async_function": renzmc_builtins.is_async_function,
            "impor_semua_python": renzmc_builtins.impor_semua_python,
            "reload_python": renzmc_builtins.reload_python,
        }

        # Add library management functions
        builtin_functions.update({
            "impor_library": BuiltinManager._import_library,
            "dapatkan_library": BuiltinManager._get_libraries,
            "info_library": BuiltinManager._get_library_info,
            # Indonesian aliases
            "impor_stdlib": BuiltinManager._import_library,
            "daftar_library": BuiltinManager._get_libraries,
        })

        return builtin_functions

    @staticmethod
    def _import_library(library_name, function_names=None):
        """
        Import library or specific functions from library.

        Args:
            library_name: Name of the library to import
            function_names: Optional list of specific function names to import

        Returns:
            Library module or dictionary of functions
        """
        try:
            manager = get_library_manager()

            if function_names is None:
                # Import entire library
                return manager.import_library(library_name)
            else:
                # Import specific functions
                result = {}
                for func_name in function_names:
                    result[func_name] = manager.import_function(library_name, func_name)
                return result

        except Exception as e:
            raise ImportError(f"Gagal import library '{library_name}': {str(e)}")

    @staticmethod
    def _get_libraries():
        """
        Get list of available libraries.

        Returns:
            List of available library names
        """
        try:
            manager = get_library_manager()
            return manager.get_libraries()
        except Exception as e:
            return []

    @staticmethod
    def _get_library_info(library_name):
        """
        Get information about a library.

        Args:
            library_name: Name of the library

        Returns:
            Dictionary with library information
        """
        try:
            manager = get_library_manager()
            return manager.get_library_info(library_name)
        except Exception as e:
            return {"error": str(e)}
