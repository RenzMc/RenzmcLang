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

import os
import shutil
from pathlib import Path


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def baca_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except Exception as e:
        raise Exception(f"Error membaca file: {e}")


def tulis_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise Exception(f"Error menulis file: {e}")


def tambah_file(filename, content):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(str(content))
        return True
    except Exception as e:
        raise Exception(f"Error menambah ke file: {e}")


def hapus_file(filename):
    try:
        os.remove(filename)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except Exception as e:
        raise Exception(f"Error menghapus file: {e}")


def gabung_path(*paths):
    return os.path.join(*paths)


def file_exists(path):
    return os.path.exists(path)


def buat_direktori(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        raise Exception(f"Error membuat direktori: {e}")


def daftar_direktori(path="."):
    try:
        return os.listdir(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Direktori '{path}' tidak ditemukan")
    except Exception as e:
        raise Exception(f"Error membaca direktori: {e}")


def direktori_ada_impl(path):
    return os.path.isdir(path)


def direktori_sekarang_impl():
    return os.getcwd()


def ubah_direktori_impl(path):
    try:
        os.chdir(path)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"Direktori '{path}' tidak ditemukan")
    except Exception as e:
        raise Exception(f"Error mengubah direktori: {e}")


def pisah_path_impl(path):
    return os.path.split(path)


def ekstensi_file_impl(path):
    return os.path.splitext(path)[1]


def nama_file_tanpa_ekstensi_impl(path):
    return os.path.splitext(os.path.basename(path))[0]


def path_ada_impl(path):
    return os.path.exists(path)


def adalah_file_impl(path):
    return os.path.isfile(path)


def adalah_direktori_impl(path):
    return os.path.isdir(path)


def path_absolut_impl(path):
    return os.path.abspath(path)


def waktu_modifikasi_file_impl(path):
    try:
        return os.path.getmtime(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' tidak ditemukan")


def waktu_buat_file_impl(path):
    try:
        return os.path.getctime(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' tidak ditemukan")


def file_dapat_dibaca_impl(path):
    return os.access(path, os.R_OK)


def file_dapat_ditulis_impl(path):
    return os.access(path, os.W_OK)


def buka_impl(filename, mode="r", encoding="utf-8", **kwargs):
    try:
        return open(filename, mode, encoding=encoding, **kwargs)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except Exception as e:
        raise Exception(f"Error membuka file: {e}")


def tutup_impl(file_obj):
    try:
        file_obj.close()
        return True
    except Exception as e:
        raise Exception(f"Error menutup file: {e}")


def tulis_impl(file_obj, content):
    try:
        file_obj.write(str(content))
        return True
    except Exception as e:
        raise Exception(f"Error menulis ke file: {e}")


def baca_impl(file_obj, size=-1):
    try:
        return file_obj.read(size)
    except Exception as e:
        raise Exception(f"Error membaca file: {e}")


direktori_ada = RenzmcBuiltinFunction(direktori_ada_impl, "direktori_ada")
direktori_sekarang = RenzmcBuiltinFunction(
    direktori_sekarang_impl, "direktori_sekarang"
)
ubah_direktori = RenzmcBuiltinFunction(ubah_direktori_impl, "ubah_direktori")
pisah_path = RenzmcBuiltinFunction(pisah_path_impl, "pisah_path")
ekstensi_file = RenzmcBuiltinFunction(ekstensi_file_impl, "ekstensi_file")
nama_file_tanpa_ekstensi = RenzmcBuiltinFunction(
    nama_file_tanpa_ekstensi_impl, "nama_file_tanpa_ekstensi"
)
path_ada = RenzmcBuiltinFunction(path_ada_impl, "path_ada")
adalah_file = RenzmcBuiltinFunction(adalah_file_impl, "adalah_file")
adalah_direktori = RenzmcBuiltinFunction(adalah_direktori_impl, "adalah_direktori")
path_absolut = RenzmcBuiltinFunction(path_absolut_impl, "path_absolut")
waktu_modifikasi_file = RenzmcBuiltinFunction(
    waktu_modifikasi_file_impl, "waktu_modifikasi_file"
)
waktu_buat_file = RenzmcBuiltinFunction(waktu_buat_file_impl, "waktu_buat_file")
file_dapat_dibaca = RenzmcBuiltinFunction(file_dapat_dibaca_impl, "file_dapat_dibaca")
file_dapat_ditulis = RenzmcBuiltinFunction(
    file_dapat_ditulis_impl, "file_dapat_ditulis"
)
buka = RenzmcBuiltinFunction(buka_impl, "buka")
tutup = RenzmcBuiltinFunction(tutup_impl, "tutup")
tulis = RenzmcBuiltinFunction(tulis_impl, "tulis")
baca = RenzmcBuiltinFunction(baca_impl, "baca")
