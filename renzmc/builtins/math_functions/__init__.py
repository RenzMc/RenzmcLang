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

import math
import random
import statistics


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def bulat(number):
    try:
        return int(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke bilangan bulat")


def desimal(number):
    try:
        return float(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke desimal")


def akar(number):
    if number < 0:
        raise ValueError("Tidak dapat menghitung akar dari bilangan negatif")
    return math.sqrt(number)


def pangkat(base, exponent):
    return base**exponent


def absolut(number):
    return abs(number)


def pembulatan(number):
    return round(number)


def pembulatan_atas(number):
    return math.ceil(number)


def pembulatan_bawah(number):
    return math.floor(number)


def sinus(angle):
    return math.sin(angle)


def cosinus(angle):
    return math.cos(angle)


def tangen(angle):
    return math.tan(angle)


def minimum(*args):
    if len(args) == 0:
        raise ValueError("minimum() membutuhkan setidaknya satu argumen")
    if len(args) == 1 and hasattr(args[0], "__iter__"):
        return min(args[0])
    return min(args)


def maksimum(*args):
    if len(args) == 0:
        raise ValueError("maksimum() membutuhkan setidaknya satu argumen")
    if len(args) == 1 and hasattr(args[0], "__iter__"):
        return max(args[0])
    return max(args)


def jumlah(*args):
    if len(args) == 0:
        return 0
    if len(args) == 1 and hasattr(args[0], "__iter__"):
        return sum(args[0])
    return sum(args)


def rata_rata(*args):
    if len(args) == 0:
        raise ValueError("rata_rata() membutuhkan setidaknya satu argumen")
    if len(args) == 1 and hasattr(args[0], "__iter__"):
        items = list(args[0])
    else:
        items = args
    return sum(items) / len(items)


def acak(min_val=0, max_val=1):
    if isinstance(min_val, int) and isinstance(max_val, int):
        return random.randint(min_val, max_val)
    return random.uniform(min_val, max_val)


def median_impl(data):
    if not hasattr(data, "__iter__"):
        raise TypeError("Data harus berupa iterable")
    return statistics.median(data)


def mode_impl(data):
    if not hasattr(data, "__iter__"):
        raise TypeError("Data harus berupa iterable")
    return statistics.mode(data)


def stdev_impl(data):
    if not hasattr(data, "__iter__"):
        raise TypeError("Data harus berupa iterable")
    return statistics.stdev(data)


def variance_impl(data):
    if not hasattr(data, "__iter__"):
        raise TypeError("Data harus berupa iterable")
    return statistics.variance(data)


def quantiles_impl(data, n=4):
    if not hasattr(data, "__iter__"):
        raise TypeError("Data harus berupa iterable")
    return statistics.quantiles(data, n=n)


median = RenzmcBuiltinFunction(median_impl, "median")
mode = RenzmcBuiltinFunction(mode_impl, "mode")
stdev = RenzmcBuiltinFunction(stdev_impl, "stdev")
variance = RenzmcBuiltinFunction(variance_impl, "variance")
quantiles = RenzmcBuiltinFunction(quantiles_impl, "quantiles")
