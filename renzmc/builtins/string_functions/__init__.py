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


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def huruf_besar(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.upper()


def huruf_kecil(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.lower()


def potong(text, start, end=None):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    try:
        if end is None:
            return text[start:]
        else:
            return text[start:end]
    except IndexError:
        raise IndexError(f"Indeks di luar jangkauan untuk teks '{text}'")


def gabung(separator, *items):
    if not isinstance(separator, str):
        raise TypeError(f"Pemisah harus berupa teks, bukan '{type(separator).__name__}'")
    return separator.join((str(item) for item in items))


def pisah(text, separator=None):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    return text.split(separator)


def ganti(text, old, new):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(old, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(old).__name__}'")
    if not isinstance(new, str):
        raise TypeError(f"Argumen ketiga harus berupa teks, bukan '{type(new).__name__}'")
    return text.replace(old, new)


def mulai_dengan(text, prefix):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(prefix, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(prefix).__name__}'")
    return text.startswith(prefix)


def akhir_dengan(text, suffix):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(suffix, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(suffix).__name__}'")
    return text.endswith(suffix)


def berisi(text, substring):
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(substring, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(substring).__name__}'")
    return substring in text


def hapus_spasi(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.strip()


def format_teks(template, *args, **kwargs):
    if not isinstance(template, str):
        raise TypeError(f"Template harus berupa teks, bukan '{type(template).__name__}'")
    try:
        return template.format(*args, **kwargs)
    except (KeyError, IndexError) as e:
        raise ValueError(f"Error dalam format teks: {e}")


def is_alpha_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.isalpha()


def is_digit_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.isdigit()


def is_alnum_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.isalnum()


def is_lower_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.islower()


def is_upper_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.isupper()


def is_space_impl(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.isspace()


is_alpha = RenzmcBuiltinFunction(is_alpha_impl, "is_alpha")
adalah_huruf = is_alpha

is_digit = RenzmcBuiltinFunction(is_digit_impl, "is_digit")
adalah_angka = is_digit

is_alnum = RenzmcBuiltinFunction(is_alnum_impl, "is_alnum")
adalah_alfanumerik = is_alnum

is_lower = RenzmcBuiltinFunction(is_lower_impl, "is_lower")
adalah_huruf_kecil = is_lower

is_upper = RenzmcBuiltinFunction(is_upper_impl, "is_upper")
adalah_huruf_besar = is_upper

is_space = RenzmcBuiltinFunction(is_space_impl, "is_space")
adalah_spasi = is_space
