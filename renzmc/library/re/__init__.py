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
RenzMcLang Regular Expression Library

Library untuk regular expression operations dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import re as python_re


def cocok(pattern, string, flags=0):
    """
    Cek apakah pattern cocok di awal string.
    
    Args:
        pattern: Regex pattern
        string: String untuk dicocokkan
        flags: Regex flags (opsional)
        
    Returns:
        Match object jika cocok, None jika tidak
    """
    try:
        return python_re.match(pattern, string, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def cari(pattern, string, flags=0):
    """
    Cari pattern dalam string.
    
    Args:
        pattern: Regex pattern
        string: String untuk dicari
        flags: Regex flags (opsional)
        
    Returns:
        Match object jika ditemukan, None jika tidak
    """
    try:
        return python_re.search(pattern, string, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def cari_semua(pattern, string, flags=0):
    """
    Cari semua pattern dalam string.
    
    Args:
        pattern: Regex pattern
        string: String untuk dicari
        flags: Regex flags (opsional)
        
    Returns:
        list: List semua matches
    """
    try:
        return python_re.findall(pattern, string, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def cari_iterasi(pattern, string, flags=0):
    """
    Cari pattern dengan iterator (untuk memory efficiency).
    
    Args:
        pattern: Regex pattern
        string: String untuk dicari
        flags: Regex flags (opsional)
        
    Returns:
        iterator: Iterator untuk matches
    """
    try:
        return python_re.finditer(pattern, string, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def bagi(pattern, string, maxsplit=0, flags=0):
    """
    Bagi string berdasarkan pattern.
    
    Args:
        pattern: Regex pattern
        string: String untuk dibagi
        maxsplit: Maximum split (0 untuk unlimited)
        flags: Regex flags (opsional)
        
    Returns:
        list: List hasil split
    """
    try:
        return python_re.split(pattern, string, maxsplit, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def ganti(pattern, replacement, string, count=0, flags=0):
    """
    Ganti pattern dengan replacement string.
    
    Args:
        pattern: Regex pattern
        replacement: String replacement
        string: String untuk diganti
        count: Maximum replacement (0 untuk unlimited)
        flags: Regex flags (opsional)
        
    Returns:
        str: String hasil replacement
    """
    try:
        return python_re.sub(pattern, replacement, string, count, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def ganti_dengan_fungsi(pattern, replacement_func, string, count=0, flags=0):
    """
    Ganti pattern dengan fungsi.
    
    Args:
        pattern: Regex pattern
        replacement_func: Function untuk replacement
        string: String untuk diganti
        count: Maximum replacement (0 untuk unlimited)
        flags: Regex flags (opsional)
        
    Returns:
        str: String hasil replacement
    """
    try:
        return python_re.sub(pattern, replacement_func, string, count, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def kompile(pattern, flags=0):
    """
    Kompile regex pattern untuk penggunaan berulang.
    
    Args:
        pattern: Regex pattern
        flags: Regex flags (opsional)
        
    Returns:
        Pattern object: Compiled pattern
    """
    try:
        return python_re.compile(pattern, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def escape(pattern):
    """
    Escape semua karakter non-alphanumeric dalam pattern.
    
    Args:
        pattern: String untuk di-escape
        
    Returns:
        str: Escaped pattern
    """
    try:
        return python_re.escape(pattern)
    except Exception as e:
        raise ValueError(f"Gagal escape pattern: {str(e)}")


def full_cocok(pattern, string, flags=0):
    """
    Cek apakah seluruh string cocok dengan pattern.
    
    Args:
        pattern: Regex pattern
        string: String untuk dicocokkan
        flags: Regex flags (opsional)
        
    Returns:
        Match object jika cocok, None jika tidak
    """
    try:
        return python_re.fullmatch(pattern, string, flags)
    except python_re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {str(e)}")


def dapatkan_grup(match, group=0):
    """
    Dapatkan grup dari match object.
    
    Args:
        match: Match object
        group: Nomor grup (default 0 untuk seluruh match)
        
    Returns:
        str: Grup string atau None
    """
    try:
        return match.group(group)
    except (AttributeError, IndexError):
        return None


def dapatkan_semua_grup(match):
    """
    Dapatkan semua grup dari match object.
    
    Args:
        match: Match object
        
    Returns:
        tuple: Tuple semua grup
    """
    try:
        return match.groups()
    except AttributeError:
        return ()


def dapatkan_nama_grup(match):
    """
    Dapatkan dictionary named groups dari match object.
    
    Args:
        match: Match object
        
    Returns:
        dict: Dictionary named groups
    """
    try:
        return match.groupdict()
    except AttributeError:
        return {}


def dapatkan_posisi(match):
    """
    Dapatkan posisi match dalam string.
    
    Args:
        match: Match object
        
    Returns:
        tuple: (start, end) position
    """
    try:
        return (match.start(), match.end())
    except AttributeError:
        return (None, None)


def validasi_email(email):
    """
    Validasi format email dengan regex.
    
    Args:
        email: Email string untuk validasi
        
    Returns:
        bool: True jika format email valid
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    try:
        return bool(python_re.match(pattern, email))
    except Exception:
        return False


def validasi_telepon(telepon):
    """
    Validasi format telepon Indonesia.
    
    Args:
        telepon: Nomor telepon string
        
    Returns:
        bool: True jika format telepon valid
    """
    pattern = r'^(\+62|62|0)8[1-9][0-9]{6,9}$'
    try:
        return bool(python_re.match(pattern, telepon.replace('-', '').replace(' ', '')))
    except Exception:
        return False


def validasi_url(url):
    """
    Validasi format URL dengan regex.
    
    Args:
        url: URL string untuk validasi
        
    Returns:
        bool: True jika format URL valid
    """
    pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w*))?)?$'
    try:
        return bool(python_re.match(pattern, url))
    except Exception:
        return False


def extract_email(teks):
    """
    Extract semua email dari teks.
    
    Args:
        teks: Teks untuk extract email
        
    Returns:
        list: List email yang ditemukan
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    try:
        return python_re.findall(pattern, teks)
    except Exception:
        return []


def extract_url(teks):
    """
    Extract semua URL dari teks.
    
    Args:
        teks: Teks untuk extract URL
        
    Returns:
        list: List URL yang ditemukan
    """
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    try:
        return python_re.findall(pattern, teks)
    except Exception:
        return []


def extract_angka(teks):
    """
    Extract semua angka dari teks.
    
    Args:
        teks: Teks untuk extract angka
        
    Returns:
        list: List angka yang ditemukan
    """
    pattern = r'\d+'
    try:
        return python_re.findall(pattern, teks)
    except Exception:
        return []


def extract_kata(teks):
    """
    Extract semua kata dari teks.
    
    Args:
        teks: Teks untuk extract kata
        
    Returns:
        list: List kata yang ditemukan
    """
    pattern = r'\b\w+\b'
    try:
        return python_re.findall(pattern, teks)
    except Exception:
        return []


# Regex flags constants
IGNORECASE = python_re.IGNORECASE
MULTILINE = python_re.MULTILINE
DOTALL = python_re.DOTALL
VERBOSE = python_re.VERBOSE
ASCII = python_re.ASCII
LOCALE = python_re.LOCALE


# Daftar semua fungsi yang tersedia
__all__ = [
    'cocok',
    'cari',
    'cari_semua',
    'cari_iterasi',
    'bagi',
    'ganti',
    'ganti_dengan_fungsi',
    'kompile',
    'escape',
    'full_cocok',
    'dapatkan_grup',
    'dapatkan_semua_grup',
    'dapatkan_nama_grup',
    'dapatkan_posisi',
    'validasi_email',
    'validasi_telepon',
    'validasi_url',
    'extract_email',
    'extract_url',
    'extract_angka',
    'extract_kata',
    'IGNORECASE',
    'MULTILINE',
    'DOTALL',
    'VERBOSE',
    'ASCII',
    'LOCALE'
]