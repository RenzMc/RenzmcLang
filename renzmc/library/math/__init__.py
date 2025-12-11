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
RenzMcLang Math Library

Module ini menyediakan fungsi-fungsi matematika yang komprehensif,
mengikuti standar Python math module dengan nama fungsi dalam Bahasa Indonesia.

Functions:
- Basic Operations: abs, round, pow, sqrt
- Trigonometry: sin, cos, tan, asin, acos, atan, atan2
- Logarithms: log, log10, log2, ln
- Constants: pi, e, tau, inf, nan
- Conversion: degrees, radians
- Hyperbolic: sinh, cosh, tanh, asinh, acosh, atanh
- Special: factorial, gcd, lcm, ceil, floor
- Utilities: fsum, isfinite, isinf, isnan

Usage:
    dari math impor pi, sin, cos
    
    sudut itu pi / 4
    hasil_sin itu sin(sudut)
    hasil_cos itu cos(sudut)
"""

import math as py_math
import builtins

# Constants
pi = py_math.pi  # Konstanta Pi
e = py_math.e  # Bilangan Euler
tau = py_math.tau  # 2*pi
inf = py_math.inf  # Tak terhingga
nan = py_math.nan  # Not a Number

# Basic Operations


def abs(x):
    """Nilai absolut dari x."""
    return py_math.fabs(x)


def round(x, digits=0):
    """Membulatkan x ke digits desimal."""
    return round(x, digits)


def pow(base, exp):
    """Menghitung base pangkat exp."""
    return py_math.pow(base, exp)


def sqrt(x):
    """Akar kuadrat dari x."""
    return py_math.sqrt(x)


# Trigonometry


def sin(x):
    """Sinus dari x (dalam radian)."""
    return py_math.sin(x)


def cos(x):
    """Cosinus dari x (dalam radian)."""
    return py_math.cos(x)


def tan(x):
    """Tangen dari x (dalam radian)."""
    return py_math.tan(x)


def asin(x):
    """Arc sinus dari x (hasil dalam radian)."""
    return py_math.asin(x)


def acos(x):
    """Arc cosinus dari x (hasil dalam radian)."""
    return py_math.acos(x)


def atan(x):
    """Arc tangen dari x (hasil dalam radian)."""
    return py_math.atan(x)


def atan2(y, x):
    """Arc tangen dari y/x (hasil dalam radian)."""
    return py_math.atan2(y, x)


# Logarithms


def log(x, base=py_math.e):
    """Logaritma dari x dengan basis tertentu (default: natural log)."""
    if base == py_math.e:
        return py_math.log(x)
    return py_math.log(x, base)


def log10(x):
    """Logaritma basis 10 dari x."""
    return py_math.log10(x)


def log2(x):
    """Logaritma basis 2 dari x."""
    return py_math.log2(x)


def ln(x):
    """Logaritma natural dari x."""
    return py_math.log(x)


# Conversion


def degrees(x):
    """Konversi radian ke derajat."""
    return py_math.degrees(x)


def radians(x):
    """Konversi derajat ke radian."""
    return py_math.radians(x)


# Hyperbolic Functions


def sinh(x):
    """Hyperbolic sinus dari x."""
    return py_math.sinh(x)


def cosh(x):
    """Hyperbolic cosinus dari x."""
    return py_math.cosh(x)


def tanh(x):
    """Hyperbolic tangen dari x."""
    return py_math.tanh(x)


def asinh(x):
    """Inverse hyperbolic sinus dari x."""
    return py_math.asinh(x)


def acosh(x):
    """Inverse hyperbolic cosinus dari x."""
    return py_math.acosh(x)


def atanh(x):
    """Inverse hyperbolic tangen dari x."""
    return py_math.atanh(x)


# Special Functions


def factorial(n):
    """Faktorial dari n (n!)."""
    return py_math.factorial(n)


def gcd(a, b):
    """Greatest Common Divisor dari a dan b."""
    return py_math.gcd(a, b)


def lcm(a, b):
    """Least Common Multiple dari a dan b."""
    return py_math.lcm(a, b)


def ceil(x):
    """Pembulatan ke atas dari x."""
    return py_math.ceil(x)


def floor(x):
    """Pembulatan ke bawah dari x."""
    return py_math.floor(x)


def trunc(x):
    """Menghapus bagian desimal dari x."""
    return py_math.trunc(x)


# Utilities


def fsum(iterable):
    """Penjumlahan presisi tinggi dari iterable."""
    return py_math.fsum(iterable)


def isfinite(x):
    """Cek apakah x bilangan finite."""
    return py_math.isfinite(x)


def isinf(x):
    """Cek apakah x bilangan tak terhingga."""
    return py_math.isinf(x)


def isnan(x):
    """Cek apakah x adalah NaN."""
    return py_math.isnan(x)


def copysign(x, y):
    """Salin sign dari y ke x."""
    return py_math.copysign(x, y)


def frexp(x):
    """Mantissa dan eksponen dari x."""
    return py_math.frexp(x)


def ldexp(x, i):
    """x * (2**i)."""
    return py_math.ldexp(x, i)


# Indonesian Aliases
nilai_absolut = abs
pangkat = pow
akar = sqrt
sinus = sin
cosinus = cos
tangen = tan
logaritma = log
logaritma_natural = ln
derajat = degrees
radian = radians
faktorial = factorial
pembulatan_atas = ceil
pembulatan_bawah = floor
jumlah_presisi = fsum

__all__ = [
    # Constants
    "pi",
    "e",
    "tau",
    "inf",
    "nan",
    # Basic Operations
    "abs",
    "round",
    "pow",
    "sqrt",
    # Trigonometry
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "atan2",
    # Logarithms
    "log",
    "log10",
    "log2",
    "ln",
    # Conversion
    "degrees",
    "radians",
    # Hyperbolic
    "sinh",
    "cosh",
    "tanh",
    "asinh",
    "acosh",
    "atanh",
    # Special Functions
    "factorial",
    "gcd",
    "lcm",
    "ceil",
    "floor",
    "trunc",
    # Utilities
    "fsum",
    "isfinite",
    "isinf",
    "isnan",
    "copysign",
    "frexp",
    "ldexp",
    # Indonesian Aliases
    "nilai_absolut",
    "pangkat",
    "akar",
    "sinus",
    "cosinus",
    "tangen",
    "logaritma",
    "logaritma_natural",
    "derajat",
    "radian",
    "faktorial",
    "pembulatan_atas",
    "pembulatan_bawah",
    "jumlah_presisi",
]
