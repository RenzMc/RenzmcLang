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




import renzmc.builtins as renzmc_builtins


class BuiltinSetupMixin:
    """
    Mixin class for builtin function setup.

    Provides methods for registering builtin functions.
    """

    def _setup_builtin_functions(self):
        """Setup all builtin functions."""
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
        }

    def _set_static(self, *args, **kwargs):
        """Placeholder for static file serving (not implemented)."""
        raise NotImplementedError("Static file serving not yet implemented")

    def _render_template(self, *args, **kwargs):
        """Placeholder for template rendering (not implemented)."""
        raise NotImplementedError("Template rendering not yet implemented")

    def _create_form(self, *args, **kwargs):
        """Placeholder for form creation (not implemented)."""
        raise NotImplementedError("Form creation not yet implemented")

    def _validate_form(self, *args, **kwargs):
        """Placeholder for form validation (not implemented)."""
        raise NotImplementedError("Form validation not yet implemented")
