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
RenzMcLang String Library

Library untuk string operations dan utilities dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import string as python_string
import random


def huruf_besar(teks):
    """
    Konversi teks ke uppercase.

    Args:
        teks: String untuk dikonversi

    Returns:
        str: Uppercase string
    """
    return str(teks).upper()


def huruf_kecil(teks):
    """
    Konversi teks ke lowercase.

    Args:
        teks: String untuk dikonversi

    Returns:
        str: Lowercase string
    """
    return str(teks).lower()


def huruf_besar_awal(teks):
    """
    Konversi teks ke capitalize (huruf besar di awal).

    Args:
        teks: String untuk dikonversi

    Returns:
        str: Capitalized string
    """
    return str(teks).capitalize()


def judul(teks):
    """
    Konversi teks ke title case.

    Args:
        teks: String untuk dikonversi

    Returns:
        str: Title case string
    """
    return str(teks).title()


def swap_case(teks):
    """
    Swap case (besar ke kecil, kecil ke besar).

    Args:
        teks: String untuk di-swap case

    Returns:
        str: Swapped case string
    """
    return str(teks).swapcase()


def hapus_spasi(teks):
    """
    Hapus whitespace di awal dan akhir string.

    Args:
        teks: String untuk di-trim

    Returns:
        str: Trimmed string
    """
    return str(teks).strip()


def hapus_spasi_kiri(teks):
    """
    Hapus whitespace di awal string.

    Args:
        teks: String untuk di-ltrim

    Returns:
        str: Left trimmed string
    """
    return str(teks).lstrip()


def hapus_spasi_kanan(teks):
    """
    Hapus whitespace di akhir string.

    Args:
        teks: String untuk di-rtrim

    Returns:
        str: Right trimmed string
    """
    return str(teks).rstrip()


def tengah(teks, lebar, fillchar=" "):
    """
    Center string dengan karakter pengisi.

    Args:
        teks: String untuk di-center
        lebar: Lebar total
        fillchar: Karakter pengisi (default space)

    Returns:
        str: Centered string
    """
    return str(teks).center(lebar, fillchar)


def kiri(teks, lebar, fillchar=" "):
    """
    Left align string dengan karakter pengisi.

    Args:
        teks: String untuk di-left align
        lebar: Lebar total
        fillchar: Karakter pengisi (default space)

    Returns:
        str: Left aligned string
    """
    return str(teks).ljust(lebar, fillchar)


def kanan(teks, lebar, fillchar=" "):
    """
    Right align string dengan karakter pengisi.

    Args:
        teks: String untuk di-right align
        lebar: Lebar total
        fillchar: Karakter pengisi (default space)

    Returns:
        str: Right aligned string
    """
    return str(teks).rjust(lebar, fillchar)


def zfill(teks, lebar):
    """
    Pad string dengan nol di sebelah kiri.

    Args:
        teks: String untuk di-zfill
        lebar: Lebar total

    Returns:
        str: Zero-filled string
    """
    return str(teks).zfill(lebar)


def hapus_prefix(teks, prefix):
    """
    Hapus prefix dari string.

    Args:
        teks: String
        prefix: Prefix untuk dihapus

    Returns:
        str: String tanpa prefix
    """
    return str(teks).removeprefix(prefix)


def hapus_suffix(teks, suffix):
    """
    Hapus suffix dari string.

    Args:
        teks: String
        suffix: Suffix untuk dihapus

    Returns:
        str: String tanpa suffix
    """
    return str(teks).removesuffix(suffix)


def is_alpha(teks):
    """
    Cek apakah string hanya mengandung alphabet.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika hanya alphabet
    """
    return str(teks).isalpha()


def is_digit(teks):
    """
    Cek apakah string hanya mengandung digit.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika hanya digit
    """
    return str(teks).isdigit()


def is_alnum(teks):
    """
    Cek apakah string hanya mengandung alphanumeric.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika alphanumeric
    """
    return str(teks).isalnum()


def is_space(teks):
    """
    Cek apakah string hanya mengandung whitespace.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika hanya whitespace
    """
    return str(teks).isspace()


def is_lower(teks):
    """
    Cek apakah string lowercase.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika lowercase
    """
    return str(teks).islower()


def is_upper(teks):
    """
    Cek apakah string uppercase.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika uppercase
    """
    return str(teks).isupper()


def is_title(teks):
    """
    Cek apakah string title case.

    Args:
        teks: String untuk dicek

    Returns:
        bool: True jika title case
    """
    return str(teks).istitle()


def huruf_vokal():
    """Dapatkan semua huruf vokal."""
    return "aeiouAEIOU"


def huruf_konsonan():
    """Dapatkan semua huruf konsonan."""
    return "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"


def angka():
    """Dapatkan semua digit angka."""
    return python_string.digits


def huruf_besar_all():
    """Dapatkan semua huruf besar."""
    return python_string.ascii_uppercase


def huruf_kecil_all():
    """Dapatkan semua huruf kecil."""
    return python_string.ascii_lowercase


def huruf_all():
    """Dapatkan semua huruf."""
    return python_string.ascii_letters


def punctuation():
    """Dapatkan semua punctuation."""
    return python_string.punctuation


def whitespace():
    """Dapatkan semua whitespace."""
    return python_string.whitespace


def printable():
    """Dapatkan semua printable characters."""
    return python_string.printable


def acak_huruf(length=10):
    """
    Generate random string huruf.

    Args:
        length: Panjang string (default 10)

    Returns:
        str: Random string
    """
    return "".join(random.choices(huruf_all(), k=length))


def acak_angka(length=10):
    """
    Generate random string angka.

    Args:
        length: Panjang string (default 10)

    Returns:
        str: Random numeric string
    """
    return "".join(random.choices(angka(), k=length))


def acak_alphanumeric(length=10):
    """
    Generate random alphanumeric string.

    Args:
        length: Panjang string (default 10)

    Returns:
        str: Random alphanumeric string
    """
    return "".join(random.choices(huruf_all() + angka(), k=length))


def balik_kata(teks):
    """
    Balik setiap kata dalam string.

    Args:
        teks: String untuk dibalik kata-katanya

    Returns:
        str: String dengan kata terbalik
    """
    words = str(teks).split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


def balik_kalimat(teks):
    """
    Balik urutan kata dalam kalimat.

    Args:
        teks: String untuk dibalik kalimatnya

    Returns:
        str: String dengan urutan kata terbalik
    """
    words = str(teks).split()
    return " ".join(reversed(words))


def hitung_vokal(teks):
    """
    Hitung jumlah huruf vokal dalam string.

    Args:
        teks: String untuk dihitung vokalnya

    Returns:
        int: Jumlah huruf vokal
    """
    return sum(1 for char in str(teks).lower() if char in "aeiou")


def hitung_konsonan(teks):
    """
    Hitung jumlah huruf konsonan dalam string.

    Args:
        teks: String untuk dihitung konsonannya

    Returns:
        int: Jumlah huruf konsonan
    """
    return sum(1 for char in str(teks).lower() if char in "bcdfghjklmnpqrstvwxyz")


def hitung_kata(teks):
    """
    Hitung jumlah kata dalam string.

    Args:
        teks: String untuk dihitung katanya

    Returns:
        int: Jumlah kata
    """
    return len(str(teks).split())


def extract_angka(teks):
    """
    Extract semua angka dari string.

    Args:
        teks: String untuk extract angka

    Returns:
        str: String yang hanya berisi angka
    """
    return "".join(char for char in str(teks) if char.isdigit())


def extract_huruf(teks):
    """
    Extract semua huruf dari string.

    Args:
        teks: String untuk extract huruf

    Returns:
        str: String yang hanya berisi huruf
    """
    return "".join(char for char in str(teks) if char.isalpha())


def bersihkan_spasi(teks):
    """
    Bersihkan multiple whitespace menjadi single space.

    Args:
        teks: String untuk dibersihkan

    Returns:
        str: Cleaned string
    """
    return " ".join(str(teks).split())


def rot13(teks):
    """
    ROT13 encryption/decryption.

    Args:
        teks: String untuk ROT13

    Returns:
        str: ROT13 string
    """
    result = []
    for char in str(teks):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + 13) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def caesar(teks, shift=3):
    """
    Caesar cipher encryption/decryption.

    Args:
        teks: String untuk Caesar cipher
        shift: Jumlah pergeseran (default 3)

    Returns:
        str: Caesar cipher string
    """
    result = []
    for char in str(teks):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


# Daftar semua fungsi yang tersedia
__all__ = [
    "huruf_besar",
    "huruf_kecil",
    "huruf_besar_awal",
    "judul",
    "swap_case",
    "hapus_spasi",
    "hapus_spasi_kiri",
    "hapus_spasi_kanan",
    "tengah",
    "kiri",
    "kanan",
    "zfill",
    "hapus_prefix",
    "hapus_suffix",
    "is_alpha",
    "is_digit",
    "is_alnum",
    "is_space",
    "is_lower",
    "is_upper",
    "is_title",
    "huruf_vokal",
    "huruf_konsonan",
    "angka",
    "huruf_besar_all",
    "huruf_kecil_all",
    "huruf_all",
    "punctuation",
    "whitespace",
    "printable",
    "acak_huruf",
    "acak_angka",
    "acak_alphanumeric",
    "balik_kata",
    "balik_kalimat",
    "hitung_vokal",
    "hitung_konsonan",
    "hitung_kata",
    "extract_angka",
    "extract_huruf",
    "bersihkan_spasi",
    "rot13",
    "caesar",
]
