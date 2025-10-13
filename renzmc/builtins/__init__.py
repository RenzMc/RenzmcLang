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

# Import dict functions
from renzmc.builtins.dict_functions import hapus_kunci, item, kunci, nilai
# Import file functions
from renzmc.builtins.file_functions import (adalah_direktori, adalah_file,
                                            baca, baca_file, buat_direktori,
                                            buka, daftar_direktori,
                                            direktori_ada, direktori_sekarang,
                                            ekstensi_file, file_dapat_dibaca,
                                            file_dapat_ditulis, file_exists,
                                            gabung_path, hapus_file,
                                            nama_file_tanpa_ekstensi,
                                            path_absolut, path_ada, pisah_path,
                                            tambah_file, tulis, tulis_file,
                                            tutup, ubah_direktori,
                                            waktu_buat_file,
                                            waktu_modifikasi_file)
# Import HTTP functions
from renzmc.builtins.http_functions import (ambil_http, hapus_http,
                                            http_delete, http_get, http_patch,
                                            http_post, http_put,
                                            http_set_header, http_set_timeout,
                                            kirim_http, perbarui_http)
# Import iteration functions
from renzmc.builtins.iteration_functions import (ada, all_func, any_func,
                                                 enumerate_func, filter_func,
                                                 kurangi, map_func, peta,
                                                 range_func, reduce_func,
                                                 rentang, reversed_renzmc,
                                                 saring, semua, sorted_func,
                                                 terbalik, terurut, zip_func)
# Import JSON functions
from renzmc.builtins.json_functions import (baca_json, dari_json, json_ke_teks,
                                            ke_json, teks_ke_json, tulis_json)
# Import list functions
from renzmc.builtins.list_functions import (balikkan, extend, hapus,
                                            hapus_pada, hitung, indeks,
                                            masukkan, salin, salin_dalam,
                                            tambah, urutkan)
# Import math functions
from renzmc.builtins.math_functions import (absolut, acak, akar, bulat,
                                            cosinus, desimal, jumlah, maksimum,
                                            median, minimum, mode, pangkat,
                                            pembulatan, pembulatan_atas,
                                            pembulatan_bawah, quantiles,
                                            rata_rata, sinus, stdev, tangen,
                                            variance)
# Import Python integration functions
from renzmc.builtins.python_integration import (cek_modul_python,
                                                create_async_function,
                                                daftar_modul_python,
                                                eksekusi_python,
                                                evaluasi_python,
                                                get_function_annotations,
                                                get_function_closure,
                                                get_function_code,
                                                get_function_defaults,
                                                get_function_doc,
                                                get_function_globals,
                                                get_function_module,
                                                get_function_name,
                                                get_function_parameters,
                                                get_function_qualname,
                                                get_function_signature,
                                                get_function_source,
                                                impor_semua_python,
                                                is_async_function,
                                                jalankan_python,
                                                path_modul_python,
                                                reload_python, run_async,
                                                super_func, versi_modul_python,
                                                wait_all_async)
# Import string functions
from renzmc.builtins.string_functions import (adalah_alfanumerik, adalah_angka,
                                              adalah_huruf, adalah_huruf_besar,
                                              adalah_huruf_kecil, adalah_spasi,
                                              akhir_dengan, berisi, gabung,
                                              ganti, hapus_spasi, huruf_besar,
                                              huruf_kecil, is_alnum, is_alpha,
                                              is_digit, is_lower, is_space,
                                              is_upper, mulai_dengan, pisah,
                                              potong)
# Import system functions
from renzmc.builtins.system_functions import (atur_sandbox, buat_uuid,
                                              hapus_perintah_aman,
                                              jalankan_perintah,
                                              tambah_perintah_aman, tanggal,
                                              tidur, validate_command_safety,
                                              validate_executable_path, waktu)
# Import type functions
from renzmc.builtins.type_functions import (abs_renzmc, bilangan_bulat,
                                            bilangan_desimal, bool_renzmc,
                                            boolean, bulatkan, cetak, daftar,
                                            dict_renzmc, float_renzmc,
                                            himpunan, input_renzmc, int_renzmc,
                                            jenis, jumlah_sum, kamus, ke_angka,
                                            ke_teks, len_renzmc, list_renzmc,
                                            maksimum_max, masukan, max_renzmc,
                                            min_renzmc, minimum_min,
                                            nilai_absolut, pangkat_pow,
                                            panjang, panjang_len, pow_renzmc,
                                            print_renzmc, round_renzmc,
                                            set_renzmc, str_renzmc, sum_renzmc,
                                            teks, tupel, tuple_renzmc)
# Import utility functions
from renzmc.builtins.utility_functions import (base64_decode, base64_encode,
                                               hash_teks, regex_match,
                                               regex_replace, url_decode,
                                               url_encode)

# Re-export for backward compatibility
format_teks = None  # Will be imported from string_functions if needed

# Aliases for compatibility
zip = zip_func
enumerate = enumerate_func
filter = filter_func
map = map_func
reduce = reduce_func
all = all_func
any = any_func
sorted = sorted_func
range = range_func
reversed = reversed_renzmc
super = super_func
input = input_renzmc
print = print_renzmc
list = list_renzmc
dict = dict_renzmc
set = set_renzmc
tuple = tuple_renzmc
str = str_renzmc
int = int_renzmc
float = float_renzmc
bool = bool_renzmc
sum = sum_renzmc
len = len_renzmc
min = min_renzmc
max = max_renzmc
abs = abs_renzmc
round = round_renzmc
pow = pow_renzmc

# Additional Indonesian aliases
nilai_tengah = median
nilai_modus = mode
deviasi_standar = stdev
simpangan_baku = stdev
variansi = variance
varians = variance
kuantil = quantiles
kuartil = quantiles
tampilkan = print_renzmc
open_file = buka
close_file = tutup
write_to_file = tulis
read_from_file = baca
write_json = tulis_json
read_json = baca_json
to_json = ke_json
from_json = dari_json
check_python_module = cek_modul_python
get_python_module_path = path_modul_python
get_python_module_version = versi_modul_python
eval_python = evaluasi_python
exec_python = eksekusi_python
teks_convert = str_renzmc
bulat_int = int_renzmc
pecahan = float_renzmc
min_nilai = min_renzmc
max_nilai = max_renzmc

__all__ = [
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
    "is_alpha",
    "is_digit",
    "is_alnum",
    "is_lower",
    "is_upper",
    "is_space",
    "adalah_huruf",
    "adalah_angka",
    "adalah_alfanumerik",
    "adalah_huruf_kecil",
    "adalah_huruf_besar",
    "adalah_spasi",
    # Math functions
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
    "minimum",
    "maksimum",
    "jumlah",
    "rata_rata",
    "acak",
    "median",
    "mode",
    "stdev",
    "variance",
    "quantiles",
    # List functions
    "tambah",
    "hapus",
    "hapus_pada",
    "masukkan",
    "urutkan",
    "balikkan",
    "hitung",
    "indeks",
    "extend",
    "salin",
    "salin_dalam",
    # Dict functions
    "kunci",
    "nilai",
    "item",
    "hapus_kunci",
    # File functions
    "baca_file",
    "tulis_file",
    "tambah_file",
    "hapus_file",
    "gabung_path",
    "file_exists",
    "buat_direktori",
    "daftar_direktori",
    "direktori_ada",
    "direktori_sekarang",
    "ubah_direktori",
    "pisah_path",
    "ekstensi_file",
    "nama_file_tanpa_ekstensi",
    "path_ada",
    "adalah_file",
    "adalah_direktori",
    "path_absolut",
    "waktu_modifikasi_file",
    "waktu_buat_file",
    "file_dapat_dibaca",
    "file_dapat_ditulis",
    "buka",
    "tutup",
    "tulis",
    "baca",
    # System functions
    "waktu",
    "tidur",
    "tanggal",
    "jalankan_perintah",
    "atur_sandbox",
    "tambah_perintah_aman",
    "hapus_perintah_aman",
    "validate_executable_path",
    "validate_command_safety",
    "buat_uuid",
    # JSON functions
    "json_ke_teks",
    "teks_ke_json",
    "tulis_json",
    "baca_json",
    "ke_json",
    "dari_json",
    # HTTP functions
    "http_get",
    "http_post",
    "http_put",
    "http_delete",
    "http_patch",
    "http_set_header",
    "http_set_timeout",
    "ambil_http",
    "kirim_http",
    "perbarui_http",
    "hapus_http",
    # Utility functions
    "hash_teks",
    "url_encode",
    "url_decode",
    "regex_match",
    "regex_replace",
    "base64_encode",
    "base64_decode",
    # Iteration functions
    "zip",
    "zip_func",
    "enumerate",
    "enumerate_func",
    "filter",
    "filter_func",
    "saring",
    "map",
    "map_func",
    "peta",
    "reduce",
    "reduce_func",
    "kurangi",
    "all",
    "all_func",
    "semua",
    "any",
    "any_func",
    "ada",
    "sorted",
    "sorted_func",
    "terurut",
    "range",
    "range_func",
    "rentang",
    "reversed",
    "reversed_renzmc",
    "terbalik",
    # Type functions
    "panjang",
    "jenis",
    "ke_teks",
    "ke_angka",
    "input",
    "input_renzmc",
    "masukan",
    "print",
    "print_renzmc",
    "cetak",
    "list",
    "list_renzmc",
    "daftar",
    "dict",
    "dict_renzmc",
    "kamus",
    "set",
    "set_renzmc",
    "himpunan",
    "tuple",
    "tuple_renzmc",
    "tupel",
    "str",
    "str_renzmc",
    "teks",
    "int",
    "int_renzmc",
    "bilangan_bulat",
    "float",
    "float_renzmc",
    "bilangan_desimal",
    "bool",
    "bool_renzmc",
    "boolean",
    "sum",
    "sum_renzmc",
    "jumlah_sum",
    "len",
    "len_renzmc",
    "panjang_len",
    "min",
    "min_renzmc",
    "minimum_min",
    "max",
    "max_renzmc",
    "maksimum_max",
    "abs",
    "abs_renzmc",
    "nilai_absolut",
    "round",
    "round_renzmc",
    "bulatkan",
    "pow",
    "pow_renzmc",
    "pangkat_pow",
    # Python integration
    "super",
    "super_func",
    "impor_semua_python",
    "reload_python",
    "daftar_modul_python",
    "jalankan_python",
    "is_async_function",
    "run_async",
    "wait_all_async",
    "create_async_function",
    "get_function_signature",
    "get_function_parameters",
    "get_function_defaults",
    "get_function_annotations",
    "get_function_doc",
    "get_function_source",
    "get_function_module",
    "get_function_name",
    "get_function_qualname",
    "get_function_globals",
    "get_function_closure",
    "get_function_code",
    "cek_modul_python",
    "path_modul_python",
    "versi_modul_python",
    "evaluasi_python",
    "eksekusi_python",
]
