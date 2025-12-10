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
RenzMcLang DateTime Library

Module ini menyediakan fungsi-fungsi untuk manipulasi tanggal dan waktu,
mengikuti standar Python datetime module dengan nama fungsi dalam Bahasa Indonesia.

Classes:
- datetime: Date dan time object
- date: Date object saja
- time: Time object saja
- timedelta: Durasi waktu
- tzinfo: Timezone information

Usage:
    dari datetime impor datetime, timedelta
    
    sekarang = datetime.sekarang()
    besok = sekarang + timedelta(hari=1)
"""

from typing import Optional, Union
import time as py_time
import datetime as py_datetime

# Import Python datetime classes
datetime = py_datetime.datetime
date = py_datetime.date
time = py_datetime.time
timedelta = py_datetime.timedelta
timezone = py_datetime.timezone
tzinfo = py_datetime.tzinfo

# Current time functions


def sekarang(tz: Optional[py_datetime.tzinfo] = None) -> py_datetime.datetime:
    """
    Dapatkan tanggal dan waktu saat ini.

    Args:
        tz: Timezone (optional)

    Returns:
        datetime object saat ini

    Example:
        skrng = sekarang()
        print(f"Sekarang: {skrng}")
    """
    if tz:
        return py_datetime.datetime.now(tz)
    return py_datetime.datetime.now()


def hari_ini() -> py_datetime.date:
    """
    Dapatkan tanggal hari ini.

    Returns:
        date object hari ini

    Example:
        today = hari_ini()
        print(f"Hari ini: {today}")
    """
    return py_datetime.date.today()


def utc_sekarang() -> py_datetime.datetime:
    """
    Dapatkan waktu saat ini dalam UTC.

    Returns:
        datetime object UTC saat ini

    Example:
        utc = utc_sekarang()
        print(f"UTC: {utc}")
    """
    return py_datetime.datetime.utcnow()

# String parsing


def parse_isoformat(date_string: str) -> py_datetime.datetime:
    """
    Parse ISO format date string.

    Args:
        date_string: ISO format date string

    Returns:
        datetime object

    Example:
        dt = parse_isoformat('2025-01-01T12:00:00')
    """
    return py_datetime.datetime.fromisoformat(date_string)


def strptime(date_string: str, format_string: str) -> py_datetime.datetime:
    """
    Parse date string dengan format tertentu.

    Args:
        date_string: Date string yang akan di-parse
        format_string: Format string

    Returns:
        datetime object

    Example:
        dt = strptime('01/01/2025', '%d/%m/%Y')
    """
    return py_datetime.datetime.strptime(date_string, format_string)

# Time functions


def waktu() -> float:
    """
    Dapatkan waktu saat ini dalam seconds sejak epoch.

    Returns:
        Float waktu dalam seconds

    Example:
        t = waktu()
        print(f"Waktu: {t}")
    """
    return py_time.time()


def sleep(detik: float):
    """
    Tidur/tunda eksekusi selama detik detik.

    Args:
        detik: Jumlah detik untuk tidur

    Example:
        sleep(2.5)  # Tidur 2.5 detik
    """
    py_time.sleep(detik)


# Constants
MINYEAR = py_datetime.MINYEAR  # Tahun minimum (1)
MAXYEAR = py_datetime.MAXYEAR  # Tahun maksimum (9999)

# Indonesian Aliases
waktu_sekarang = sekarang
tanggal_sekarang = hari_ini
utc_waktu_sekarang = utc_sekarang
pars_format_iso = parse_isoformat
pars_string_waktu = strptime
waktu_epoch = waktu
tidur = sleep
tahun_minimum = MINYEAR
tahun_maksimum = MAXYEAR

__all__ = [
    # Classes
    "datetime", "date", "time", "timedelta", "timezone", "tzinfo",
    # Functions
    "sekarang", "hari_ini", "utc_sekarang", "parse_isoformat",
    "strptime", "waktu", "sleep",
    # Constants
    "MINYEAR", "MAXYEAR",
    # Indonesian Aliases
    "waktu_sekarang", "tanggal_sekarang", "utc_waktu_sekarang",
    "pars_format_iso", "pars_string_waktu", "waktu_epoch", "tidur",
    "tahun_minimum", "tahun_maksimum"
]
