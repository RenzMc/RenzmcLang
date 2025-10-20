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


_builtin_zip = zip
_builtin_enumerate = enumerate
_builtin_filter = filter
_builtin_map = map
_builtin_all = all
_builtin_any = any
_builtin_sorted = sorted


def zip_impl(*iterables):
    return list(_builtin_zip(*iterables))


def enumerate_impl(iterable, start=0):
    return list(_builtin_enumerate(iterable, start))


def filter_impl(function, iterable):
    return list(_builtin_filter(function, iterable))


def map_impl(function, *iterables):
    return list(_builtin_map(function, *iterables))


def reduce_impl(function, iterable, initial=None):
    from functools import reduce as _builtin_reduce

    if initial is None:
        return _builtin_reduce(function, iterable)
    return _builtin_reduce(function, iterable, initial)


def all_impl(iterable):
    return _builtin_all(iterable)


def any_impl(iterable):
    return _builtin_any(iterable)


def sorted_impl(iterable, key=None, reverse=False):
    return _builtin_sorted(iterable, key=key, reverse=reverse)


def range_impl(*args):
    if len(args) == 1:
        return list(range(args[0]))
    elif len(args) == 2:
        return list(range(args[0], args[1]))
    elif len(args) == 3:
        return list(range(args[0], args[1], args[2]))
    else:
        raise TypeError(f"range() membutuhkan 1-3 argumen, diberikan {len(args)} argumen")


def reversed_impl(seq):
    import builtins as _builtins

    return list(_builtins.reversed(seq))


zip_func = RenzmcBuiltinFunction(zip_impl, "zip")
enumerate_func = RenzmcBuiltinFunction(enumerate_impl, "enumerate")
filter_func = RenzmcBuiltinFunction(filter_impl, "filter")
saring = filter_func
map_func = RenzmcBuiltinFunction(map_impl, "map")
peta = map_func
reduce_func = RenzmcBuiltinFunction(reduce_impl, "reduce")
kurangi = reduce_func
all_func = RenzmcBuiltinFunction(all_impl, "all")
semua = all_func
any_func = RenzmcBuiltinFunction(any_impl, "any")
ada = any_func
sorted_func = RenzmcBuiltinFunction(sorted_impl, "sorted")
terurut = sorted_func
range_func = RenzmcBuiltinFunction(range_impl, "range")
rentang = range_func
reversed_renzmc = RenzmcBuiltinFunction(reversed_impl, "reversed")
terbalik = reversed_renzmc
