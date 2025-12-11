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

"""
RenzMcLang Built-in Functions

Core built-in functions that are always available without importing.
Math, JSON, HTTP, and file operations have been moved to standard library.

Available standard libraries:
- math: dari math impor sin, cos, sqrt, etc.
- json: dari json impor loads, dumps, etc.
- http: dari http impor get, post, etc.
- os: dari os impor getcwd, mkdir, etc.
- datetime: dari datetime impor sekarang, hari_ini, etc.
- statistics: dari statistics impor mean, median, etc.
- random: dari random impor random, randint, etc.
- fileio: dari fileio impor read_text, write_text, etc.
"""

# Import string functions that actually exist
from renzmc.builtins.string_functions import (
    huruf_besar,
    huruf_kecil,
    potong,
    gabung,
    pisah,
    ganti,
    mulai_dengan,
    akhir_dengan,
    berisi,
    hapus_spasi,
    format_teks,
    adalah_huruf,
    adalah_angka,
    adalah_alfanumerik,
    adalah_huruf_besar,
    adalah_huruf_kecil,
    adalah_spasi,
)

# Import type functions that actually exist
from renzmc.builtins.type_functions import panjang, jenis, ke_teks, ke_angka

# Import dict functions that actually exist
from renzmc.builtins.dict_functions import hapus_kunci, item, kunci, nilai

# Import iteration functions that actually exist
from renzmc.builtins.iteration_functions import (
    ada,
    all_func,
    any_func,
    enumerate_func,
    filter_func,
    kurangi,
    map_func,
    peta,
    range_func,
    reduce_func,
    rentang,
    reversed_renzmc,
    saring,
    semua,
    sorted_func,
    terbalik,
    terurut,
    zip_func,
)

# Import list functions that actually exist
from renzmc.builtins.list_functions import (
    balikkan,
    extend,
    hapus,
    hapus_pada,
    hitung,
    indeks,
    masukkan,
    salin,
    salin_dalam,
    tambah,
    urutkan,
)

# Import system functions that actually exist
from renzmc.builtins.system_functions import buka, open_file

# Import utility functions that actually exist
from renzmc.builtins.utility_functions import (
    hash_teks,
    url_encode,
    url_decode,
    regex_match,
    regex_replace,
    base64_encode,
    base64_decode,
)

# Import Python integration functions that actually exist
from renzmc.builtins.python_integration import (
    daftar_modul_python,
    jalankan_python,
    is_async_function,
    impor_semua_python,
    reload_python,
)

# Note: The following function groups have been moved to standard library:
# - Math functions: dari math impor sin, cos, tan, sqrt, log, etc.
# - JSON functions: dari json impor loads, dumps, load, dump
# - HTTP functions: dari http impor get, post, put, delete
# - File operations: dari fileio impor read_text, write_text, read_json, write_json
# - Statistics: dari statistics impor mean, median, stdev, variance
# - Random: dari random impor random, randint, choice
# - OS operations: dari os impor getcwd, mkdir, listdir

# Core built-in function exports
__all__ = [
    # Type functions
    "panjang",
    "jenis",
    "ke_teks",
    "ke_angka",
    # File functions
    "buka",
    "buka_file",
    "open_file",
    # String functions
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
    "format_teks",
    "adalah_huruf",
    "adalah_angka",
    "adalah_alfanumerik",
    "adalah_huruf_besar",
    "adalah_huruf_kecil",
    "adalah_spasi",
    # Dict functions
    "hapus_kunci",
    "item",
    "kunci",
    "nilai",
    # Iteration functions
    "ada",
    "all_func",
    "any_func",
    "enumerate_func",
    "filter_func",
    "kurangi",
    "map_func",
    "peta",
    "range_func",
    "reduce_func",
    "rentang",
    "reversed_renzmc",
    "saring",
    "semua",
    "sorted_func",
    "terbalik",
    "terurut",
    "zip_func",
    # List functions
    "balikkan",
    "extend",
    "hapus",
    "hapus_pada",
    "hitung",
    "indeks",
    "masukkan",
    "salin",
    "salin_dalam",
    "tambah",
    "urutkan",
    # Utility functions
    "hash_teks",
    "url_encode",
    "url_decode",
    "regex_match",
    "regex_replace",
    "base64_encode",
    "base64_decode",
    # Python integration
    "daftar_modul_python",
    "jalankan_python",
    "is_async_function",
    "impor_semua_python",
    "reload_python",
]
