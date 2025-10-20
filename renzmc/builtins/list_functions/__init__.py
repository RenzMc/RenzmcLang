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

import copy


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def tambah(lst, item):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa list, bukan '{type(lst).__name__}'")
    lst.append(item)
    return lst


def hapus(lst, item):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa list, bukan '{type(lst).__name__}'")
    try:
        lst.remove(item)
        return lst
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam list")


def hapus_pada(lst, index):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa list, bukan '{type(lst).__name__}'")
    try:
        del lst[index]
        return lst
    except IndexError:
        raise IndexError(f"Indeks {index} di luar jangkauan")


def masukkan(lst, index, item):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa list, bukan '{type(lst).__name__}'")
    try:
        lst.insert(index, item)
        return lst
    except IndexError:
        raise IndexError(f"Indeks {index} di luar jangkauan")


def urutkan(lst, terbalik=False):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa list, bukan '{type(lst).__name__}'")
    try:
        lst.sort(reverse=terbalik)
        return lst
    except TypeError:
        raise TypeError("List berisi item yang tidak dapat dibandingkan")


def balikkan(lst):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa list, bukan '{type(lst).__name__}'")
    lst.reverse()
    return lst


def hitung(lst, item):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa list, bukan '{type(lst).__name__}'")
    return lst.count(item)


def indeks(lst, item):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa list, bukan '{type(lst).__name__}'")
    try:
        return lst.index(item)
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam list")


def extend(lst, iterable):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa list, bukan '{type(lst).__name__}'")
    lst.extend(iterable)
    return lst


def salin(obj):
    return copy.copy(obj)


def salin_dalam(obj):
    return copy.deepcopy(obj)
