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
RenzMcLang Statistics Library

Module ini menyediakan fungsi-fungsi statistika matematika,
mengikuti standar Python statistics module dengan nama fungsi dalam Bahasa Indonesia.

Functions:
- Measures of Central Tendency: mean, median, mode
- Measures of Spread: stdev, variance, pstdev, pvariance
- Other Statistics: geometric_mean, harmonic_mean, quantiles

Usage:
    dari statistics impor mean, median, stdev
    
    data = [1, 2, 3, 4, 5]
    rata = mean(data)
    tengah = median(data)
    deviasi = stdev(data)
"""

import math as py_math
from typing import List, Union, Sequence, Any, Optional
import statistics as py_statistics

Number = Union[int, float]


def mean(data: Sequence[Number]) -> float:
    """
    Hitung rata-rata aritmetika dari data.

    Args:
        data: Sequence numeric data

    Returns:
        Rata-rata aritmetika

    Raises:
        StatisticsError: Jika data kosong

    Example:
        data = [1, 2, 3, 4, 5]
        rata = mean(data)  # 3.0
    """
    return py_statistics.mean(data)


def median(data: Sequence[Number]) -> float:
    """
    Hitung median (nilai tengah) dari data.

    Args:
        data: Sequence numeric data

    Returns:
        Median dari data

    Example:
        data = [1, 2, 3, 4, 5]
        tengah = median(data)  # 3
    """
    return py_statistics.median(data)


def mode(data: Sequence[Number]) -> Any:
    """
    Hitung mode (nilai yang paling sering muncul) dari data.

    Args:
        data: Sequence data

    Returns:
        Mode dari data

    Raises:
        StatisticsError: Jika tidak ada mode atau multiple modes

    Example:
        data = [1, 2, 2, 3, 4]
        modus = mode(data)  # 2
    """
    return py_statistics.mode(data)


def multimode(data: Sequence[Number]) -> List[Any]:
    """
    Hitung semua modes dari data.

    Args:
        data: Sequence data

    Returns:
        List semua modes

    Example:
        data = [1, 2, 2, 3, 3]
        modus = multimode(data)  # [2, 3]
    """
    return py_statistics.multimode(data)


def stdev(data: Sequence[Number], xbar: Optional[float] = None) -> float:
    """
    Hitung standard deviasi sampel.

    Args:
        data: Sequence numeric data
        xbar: Mean yang sudah dihitung (optional)

    Returns:
        Standard deviasi sampel

    Example:
        data = [1, 2, 3, 4, 5]
        dev = stdev(data)  # ~1.58
    """
    return py_statistics.stdev(data, xbar)


def pstdev(data: Sequence[Number], mu: Optional[float] = None) -> float:
    """
    Hitung standard deviasi populasi.

    Args:
        data: Sequence numeric data
        mu: Mean populasi (optional)

    Returns:
        Standard deviasi populasi

    Example:
        data = [1, 2, 3, 4, 5]
        dev = pstdev(data)  # ~1.41
    """
    return py_statistics.pstdev(data, mu)


def variance(data: Sequence[Number], xbar: Optional[float] = None) -> float:
    """
    Hitung variansi sampel.

    Args:
        data: Sequence numeric data
        xbar: Mean yang sudah dihitung (optional)

    Returns:
        Variansi sampel

    Example:
        data = [1, 2, 3, 4, 5]
        var = variance(data)  # 2.5
    """
    return py_statistics.variance(data, xbar)


def pvariance(data: Sequence[Number], mu: Optional[float] = None) -> float:
    """
    Hitung variansi populasi.

    Args:
        data: Sequence numeric data
        mu: Mean populasi (optional)

    Returns:
        Variansi populasi

    Example:
        data = [1, 2, 3, 4, 5]
        var = pvariance(data)  # 2.0
    """
    return py_statistics.pvariance(data, mu)


def geometric_mean(data: Sequence[Number]) -> float:
    """
    Hitung geometric mean dari data.

    Args:
        data: Sequence numeric data (harus positif)

    Returns:
        Geometric mean

    Example:
        data = [1, 4, 9]
        gm = geometric_mean(data)  # ~3.36
    """
    return py_statistics.geometric_mean(data)


def harmonic_mean(data: Sequence[Number], weights: Optional[Sequence[Number]] = None) -> float:
    """
    Hitung harmonic mean dari data.

    Args:
        data: Sequence numeric data (harus positif)
        weights: Optional weights untuk weighted harmonic mean

    Returns:
        Harmonic mean

    Example:
        data = [1, 2, 4]
        hm = harmonic_mean(data)  # ~1.71
    """
    if weights:
        return py_statistics.harmonic_mean(data, weights=weights)
    return py_statistics.harmonic_mean(data)


def quantiles(data: Sequence[Number], n: int = 4) -> List[float]:
    """
    Bagi data menjadi n interval yang sama.

    Args:
        data: Sequence numeric data
        n: Jumlah quantiles (default: 4 untuk quartiles)

    Returns:
        List quantile values

    Example:
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        q = quantiles(data, n=4)  # Quartiles
    """
    return py_statistics.quantiles(data, n=n)

# Additional statistical functions


def fmean(data: Sequence[Number]) -> float:
    """
    Fast mean menggunakan fsum.

    Args:
        data: Sequence numeric data

    Returns:
        Fast mean

    Example:
        data = [1, 2, 3, 4, 5]
        fm = fmean(data)  # 3.0
    """
    return py_statistics.fmean(data)


def geometric_mean_low(data: Sequence[Number]) -> float:
    """
    Lower bound geometric mean.

    Args:
        data: Sequence numeric data

    Returns:
        Lower bound geometric mean
    """
    return py_statistics.geometric_mean(data)


def geometric_mean_high(data: Sequence[Number]) -> float:
    """
    Upper bound geometric mean.

    Args:
        data: Sequence numeric data

    Returns:
        Upper bound geometric mean
    """
    return py_statistics.geometric_mean(data)

# Custom functions


def range_data(data: Sequence[Number]) -> float:
    """
    Hitung range (max - min) dari data.

    Args:
        data: Sequence numeric data

    Returns:
        Range dari data

    Example:
        data = [1, 2, 3, 4, 5]
        r = range_data(data)  # 4.0
    """
    return max(data) - min(data)


def cv(data: Sequence[Number]) -> float:
    """
    Hitung coefficient of variation.

    Args:
        data: Sequence numeric data

    Returns:
        Coefficient of variation

    Example:
        data = [1, 2, 3, 4, 5]
        coef_var = cv(data)  # ~0.53
    """
    m = mean(data)
    if m == 0:
        raise ValueError("Mean tidak boleh 0 untuk coefficient of variation")
    return stdev(data) / m


def z_score(x: Number, data: Sequence[Number]) -> float:
    """
    Hitung z-score untuk x dalam data.

    Args:
        x: Value yang akan dihitung z-score
        data: Sequence numeric data

    Returns:
        Z-score

    Example:
        data = [1, 2, 3, 4, 5]
        z = z_score(4, data)  # ~1.26
    """
    m = mean(data)
    s = stdev(data)
    if s == 0:
        raise ValueError("Standard deviasi tidak boleh 0")
    return (x - m) / s


# Indonesian Aliases
rata_rata = mean
nilai_tengah = median
modus = mode
banyak_modus = multimode
deviasi_standar = stdev
deviasi_standar_populasi = pstdev
variansi = variance
variansi_populasi = pvariance
rata_rata_geometrik = geometric_mean
rata_rata_harmonik = harmonic_mean
kuantil = quantiles
rata_rata_cepat = fmean
rentang_data = range_data
koefisien_variasi = cv
nilai_z = z_score

# Exception


class StatisticsError(py_statistics.StatisticsError):
    """
    Exception untuk error statistika.
    """
    pass


__all__ = [
    # Basic Statistics
    "mean", "median", "mode", "multimode",
    # Spread Measures
    "stdev", "pstdev", "variance", "pvariance",
    # Other Means
    "geometric_mean", "harmonic_mean", "fmean",
    # Quantiles
    "quantiles",
    # Custom Functions
    "range_data", "cv", "z_score",
    # Exception
    "StatisticsError",
    # Indonesian Aliases
    "rata_rata", "nilai_tengah", "modus", "banyak_modus",
    "deviasi_standar", "deviasi_standar_populasi", "variansi",
    "variansi_populasi", "rata_rata_geometrik", "rata_rata_harmonik",
    "kuantil", "rata_rata_cepat", "rentang_data", "koefisien_variasi",
    "nilai_z"
]
