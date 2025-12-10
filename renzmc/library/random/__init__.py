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
RenzMcLang Random Library

Module ini menyediakan fungsi-fungsi untuk generate angka acak,
mengikuti standar Python random module dengan nama fungsi dalam Bahasa Indonesia.

Classes:
- Random: Random number generator class
- SystemRandom: Random menggunakan OS entropy

Functions:
- Basic: random, randint, randrange, uniform, triangular
- Sequences: choice, choices, sample, shuffle
- Distributions: betavariate, expovariate, gammavariate, gauss, etc.

Usage:
    dari random impor random, randint, choice, shuffle
    
    angka = random()  # 0.0 - 1.0
    dadu = randint(1, 6)
    pilihan = choice(['a', 'b', 'c'])
"""

import math as py_math
from typing import List, Sequence, Any, Optional, Union
import random as py_random

Number = Union[int, float]

# Basic random functions


def random() -> float:
    """
    Generate angka acak antara 0.0 dan 1.0.

    Returns:
        Float acak antara 0.0 (inklusif) dan 1.0 (eksklusif)

    Example:
        angka = random()  # 0.123456789
    """
    return py_random.random()


def randint(a: int, b: int) -> int:
    """
    Generate integer acak antara a dan b (inklusif).

    Args:
        a: Batas bawah
        b: Batas atas

    Returns:
        Integer acak antara a dan b

    Example:
        dadu = randint(1, 6)  # 1, 2, 3, 4, 5, atau 6
    """
    return py_random.randint(a, b)


def randrange(start: int, stop: Optional[int] = None, step: int = 1) -> int:
    """
    Generate integer acak dari range(start, stop, step).

    Args:
        start: Start value
        stop: Stop value (None untuk range(start))
        step: Step size

    Returns:
        Integer acak dari range

    Example:
        angka = randrange(0, 10, 2)  # 0, 2, 4, 6, atau 8
    """
    if stop is None:
        return py_random.randrange(start)
    return py_random.randrange(start, stop, step)


def uniform(a: float, b: float) -> float:
    """
    Generate float acak antara a dan b.

    Args:
        a: Batas bawah
        b: Batas atas

    Returns:
        Float acak antara a dan b

    Example:
        angka = uniform(1.0, 5.0)  # antara 1.0 dan 5.0
    """
    return py_random.uniform(a, b)


def triangular(low: float, high: float, mode: Optional[float] = None) -> float:
    """
    Generate float acak dengan distribusi triangular.

    Args:
        low: Batas bawah
        high: Batas atas
        mode: Puncak distribusi (default: rata-rata low dan high)

    Returns:
        Float acak dengan distribusi triangular

    Example:
        angka = triangular(0.0, 1.0, 0.5)
    """
    return py_random.triangular(low, high, mode)

# Sequence functions


def choice(sequence: Sequence[Any]) -> Any:
    """
    Pilih elemen acak dari sequence.

    Args:
        sequence: Sequence input

    Returns:
        Elemen acak dari sequence

    Raises:
        IndexError: Jika sequence kosong

    Example:
        pilihan = choice(['a', 'b', 'c'])  # 'a', 'b', atau 'c'
    """
    return py_random.choice(sequence)


def choices(sequence: Sequence[Any], weights: Optional[Sequence[Number]] = None,
            cum_weights: Optional[Sequence[Number]] = None, k: int = 1) -> List[Any]:
    """
    Pilih k elemen acak dari sequence dengan replacement.

    Args:
        sequence: Sequence input
        weights: Bobot untuk setiap elemen
        cum_weights: Bobot kumulatif
        k: Jumlah pilihan

    Returns:
        List k elemen acak

    Example:
        pilihan = choices(['a', 'b', 'c'], weights=[1, 2, 3], k=2)
    """
    return py_random.choices(sequence, weights=weights, cum_weights=cum_weights, k=k)


def sample(sequence: Sequence[Any], k: int) -> List[Any]:
    """
    Pilih k elemen unik acak dari sequence tanpa replacement.

    Args:
        sequence: Sequence input
        k: Jumlah elemen yang dipilih

    Returns:
        List k elemen unik acak

    Raises:
        ValueError: Jika k > panjang sequence

    Example:
        pilihan = sample([1, 2, 3, 4, 5], k=3)  # [2, 5, 1]
    """
    return py_random.sample(sequence, k)


def shuffle(x: list):
    """
    Acak urutan list secara in-place.

    Args:
        x: List yang akan diacak

    Example:
        items = [1, 2, 3, 4, 5]
        shuffle(items)  # items bisa jadi [3, 1, 5, 2, 4]
    """
    py_random.shuffle(x)

# Real-valued distributions


def betavariate(alpha: float, beta: float) -> float:
    """
    Beta distribution.

    Args:
        alpha: Alpha parameter (> 0)
        beta: Beta parameter (> 0)

    Returns:
        Float acak dengan Beta distribution
    """
    return py_random.betavariate(alpha, beta)


def expovariate(lambd: float) -> float:
    """
    Exponential distribution.

    Args:
        lambd: Lambda parameter (> 0)

    Returns:
        Float acak dengan Exponential distribution
    """
    return py_random.expovariate(lambd)


def gammavariate(alpha: float, beta: float) -> float:
    """
    Gamma distribution.

    Args:
        alpha: Alpha parameter (> 0)
        beta: Beta parameter (> 0)

    Returns:
        Float acak dengan Gamma distribution
    """
    return py_random.gammavariate(alpha, beta)


def gauss(mu: float, sigma: float) -> float:
    """
    Gaussian distribution (normal distribution).

    Args:
        mu: Mean
        sigma: Standard deviation

    Returns:
        Float acak dengan Gaussian distribution
    """
    return py_random.gauss(mu, sigma)


def lognormvariate(mu: float, sigma: float) -> float:
    """
    Log normal distribution.

    Args:
        mu: Mean dari log distribusi
        sigma: Standard deviation dari log distribusi

    Returns:
        Float acak dengan Log normal distribution
    """
    return py_random.lognormvariate(mu, sigma)


def normalvariate(mu: float, sigma: float) -> float:
    """
    Normal distribution.

    Args:
        mu: Mean
        sigma: Standard deviation

    Returns:
        Float acak dengan Normal distribution
    """
    return py_random.normalvariate(mu, sigma)


def vonmisesvariate(mu: float, kappa: float) -> float:
    """
    von Mises distribution.

    Args:
        mu: Mean angle (dalam radian antara 0 dan 2*pi)
        kappa: Concentration parameter (>= 0)

    Returns:
        Float acak dengan von Mises distribution
    """
    return py_random.vonmisesvariate(mu, kappa)


def paretovariate(alpha: float) -> float:
    """
    Pareto distribution.

    Args:
        alpha: Shape parameter

    Returns:
        Float acak dengan Pareto distribution
    """
    return py_random.paretovariate(alpha)


def weibullvariate(alpha: float, beta: float) -> float:
    """
    Weibull distribution.

    Args:
        alpha: Scale parameter
        beta: Shape parameter

    Returns:
        Float acak dengan Weibull distribution
    """
    return py_random.weibullvariate(alpha, beta)

# Utility functions


def seed(a: Optional[Union[int, float, str, bytes, bytearray]] = None):
    """
    Initialize random number generator.

    Args:
        a: Seed value (None untuk menggunakan system time)

    Example:
        seed(12345)  # Deterministic sequence
        seed()       # Random seed
    """
    py_random.seed(a)


def getstate() -> dict:
    """
    Dapatkan internal state dari generator.

    Returns:
        Dictionary internal state
    """
    return py_random.getstate()


def setstate(state: dict):
    """
    Set internal state dari generator.

    Args:
        state: State dictionary dari getstate()
    """
    py_random.setstate(state)

# String functions


def randbytes(n: int) -> bytes:
    """
    Generate n random bytes.

    Args:
        n: Jumlah bytes

    Returns:
        Bytes random

    Example:
        data = randbytes(10)  # 10 random bytes
    """
    return py_random.randbytes(n)

# Classes


class Random(py_random.Random):
    """
    Random number generator class.

    Bisa digunakan untuk membuat multiple independent generators.
    """
    pass


class SystemRandom(py_random.SystemRandom):
    """
    Random number generator menggunakan OS entropy.

    Lebih secure tapi mungkin lebih lambat.
    """
    pass


# Indonesian Aliases
acak = random
acak_bulat = randint
rentang_acak = randrange
seragam = uniform
segitiga = triangular
pilih_acak = choice
banyak_pilihan = choices
contoh_acak = sample
acak_urutan = shuffle
distribusi_beta = betavariate
distribusi_eksponensial = expovariate
distribusi_gamma = gammavariate
distribusi_gauss = gauss
distribusi_log_normal = lognormvariate
distribusi_normal = normalvariate
distribusi_von_mises = vonmisesvariate
distribusi_pareto = paretovariate
distribusi_weibull = weibullvariate
inisialisasi = seed
dapatkan_keadaan = getstate
atur_keadaan = setstate
byte_acak = randbytes
generator_acak = Random
generator_sistem = SystemRandom

__all__ = [
    # Basic Functions
    "random", "randint", "randrange", "uniform", "triangular",
    # Sequence Functions
    "choice", "choices", "sample", "shuffle",
    # Distributions
    "betavariate", "expovariate", "gammavariate", "gauss",
    "lognormvariate", "normalvariate", "vonmisesvariate",
    "paretovariate", "weibullvariate",
    # Utility
    "seed", "getstate", "setstate", "randbytes",
    # Classes
    "Random", "SystemRandom",
    # Indonesian Aliases
    "acak", "acak_bulat", "rentang_acak", "seragam", "segitiga",
    "pilih_acak", "banyak_pilihan", "contoh_acak", "acak_urutan",
    "distribusi_beta", "distribusi_eksponensial", "distribusi_gamma",
    "distribusi_gauss", "distribusi_log_normal", "distribusi_normal",
    "distribusi_von_mises", "distribusi_pareto", "distribusi_weibull",
    "inisialisasi", "dapatkan_keadaan", "atur_keadaan", "byte_acak",
    "generator_acak", "generator_sistem"
]
