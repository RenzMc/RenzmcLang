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


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def panjang(obj):
    try:
        return len(obj)
    except TypeError:
        raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak memiliki panjang")


def jenis(obj):
    return type(obj).__name__


def ke_teks(obj):
    return str(obj)


def ke_angka(obj):
    try:
        return int(obj)
    except ValueError:
        try:
            return float(obj)
        except ValueError:
            raise ValueError(f"Tidak dapat mengkonversi '{obj}' ke angka")


def _convert_to_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "ya", "benar")
    return bool(value)


def input_impl(prompt=""):
    return input(prompt)


def print_impl(*args, sep=" ", end="\n"):
    print(*args, sep=sep, end=end)


def list_impl(iterable):
    import builtins as _builtins

    return _builtins.list(iterable)


def dict_impl(*args, **kwargs):
    import builtins as _builtins

    return _builtins.dict(*args, **kwargs)


def set_impl(iterable=None):
    import builtins as _builtins

    if iterable is None:
        return _builtins.set()
    return _builtins.set(iterable)


def tuple_impl(iterable=None):
    import builtins as _builtins

    if iterable is None:
        return ()
    return _builtins.tuple(iterable)


def str_impl(obj):
    import builtins as _builtins

    return _builtins.str(obj)


def int_impl(obj, base=10):
    import builtins as _builtins

    return _builtins.int(obj, base)


def float_impl(obj):
    import builtins as _builtins

    return _builtins.float(obj)


def bool_impl(obj):
    import builtins as _builtins

    return _builtins.bool(obj)


def sum_impl(iterable, start=0):
    import builtins as _builtins

    return _builtins.sum(iterable, start)


def len_impl(obj):
    import builtins as _builtins

    return _builtins.len(obj)


def min_impl(*args, **kwargs):
    import builtins as _builtins

    return _builtins.min(*args, **kwargs)


def max_impl(*args, **kwargs):
    import builtins as _builtins

    return _builtins.max(*args, **kwargs)


def abs_impl(x):
    import builtins as _builtins

    return _builtins.abs(x)


def round_impl(number, ndigits=None):
    import builtins as _builtins

    if ndigits is None:
        return _builtins.round(number)
    return _builtins.round(number, ndigits)


def pow_impl(base, exp, mod=None):
    import builtins as _builtins

    if mod is None:
        return _builtins.pow(base, exp)
    return _builtins.pow(base, exp, mod)


input_renzmc = RenzmcBuiltinFunction(input_impl, "input")
masukan = input_renzmc

print_renzmc = RenzmcBuiltinFunction(print_impl, "print")
cetak = print_renzmc

list_renzmc = RenzmcBuiltinFunction(list_impl, "list")
daftar = list_renzmc

dict_renzmc = RenzmcBuiltinFunction(dict_impl, "dict")
kamus = dict_renzmc

set_renzmc = RenzmcBuiltinFunction(set_impl, "set")
himpunan = set_renzmc

tuple_renzmc = RenzmcBuiltinFunction(tuple_impl, "tuple")
tupel = tuple_renzmc

str_renzmc = RenzmcBuiltinFunction(str_impl, "str")
teks = str_renzmc

int_renzmc = RenzmcBuiltinFunction(int_impl, "int")
bilangan_bulat = int_renzmc

float_renzmc = RenzmcBuiltinFunction(float_impl, "float")
bilangan_desimal = float_renzmc

bool_renzmc = RenzmcBuiltinFunction(bool_impl, "bool")
boolean = bool_renzmc

sum_renzmc = RenzmcBuiltinFunction(sum_impl, "sum")
jumlah_sum = sum_renzmc

len_renzmc = RenzmcBuiltinFunction(len_impl, "len")
panjang_len = len_renzmc

min_renzmc = RenzmcBuiltinFunction(min_impl, "min")
minimum_min = min_renzmc

max_renzmc = RenzmcBuiltinFunction(max_impl, "max")
maksimum_max = max_renzmc

abs_renzmc = RenzmcBuiltinFunction(abs_impl, "abs")
nilai_absolut = abs_renzmc

round_renzmc = RenzmcBuiltinFunction(round_impl, "round")
bulatkan = round_renzmc

pow_renzmc = RenzmcBuiltinFunction(pow_impl, "pow")
pangkat_pow = pow_renzmc
