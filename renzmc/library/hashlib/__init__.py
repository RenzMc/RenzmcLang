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
RenzMcLang Hashlib Library

Library untuk hashing dengan berbagai algoritma (MD5, SHA1, SHA256, dll) 
dengan fungsi-fungsi dalam bahasa Indonesia.
"""

import hashlib as python_hashlib
import os


def hash_md5(data):
    """
    Generate MD5 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: MD5 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.md5(data).hexdigest()


def hash_sha1(data):
    """
    Generate SHA1 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA1 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha1(data).hexdigest()


def hash_sha224(data):
    """
    Generate SHA224 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA224 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha224(data).hexdigest()


def hash_sha256(data):
    """
    Generate SHA256 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA256 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha256(data).hexdigest()


def hash_sha384(data):
    """
    Generate SHA384 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA384 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha384(data).hexdigest()


def hash_sha512(data):
    """
    Generate SHA512 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA512 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha512(data).hexdigest()


def hash_blake2b(data, digest_size=64):
    """
    Generate BLAKE2b hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        digest_size: Ukuran digest (default 64)
        
    Returns:
        str: BLAKE2b hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.blake2b(data, digest_size=digest_size).hexdigest()


def hash_blake2s(data, digest_size=32):
    """
    Generate BLAKE2s hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        digest_size: Ukuran digest (default 32)
        
    Returns:
        str: BLAKE2s hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.blake2s(data, digest_size=digest_size).hexdigest()


def hash_sha3_224(data):
    """
    Generate SHA3-224 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA3-224 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha3_224(data).hexdigest()


def hash_sha3_256(data):
    """
    Generate SHA3-256 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA3-256 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha3_256(data).hexdigest()


def hash_sha3_384(data):
    """
    Generate SHA3-384 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA3-384 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha3_384(data).hexdigest()


def hash_sha3_512(data):
    """
    Generate SHA3-512 hash dari data.
    
    Args:
        data: String atau bytes untuk di-hash
        
    Returns:
        str: SHA3-512 hash hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    return python_hashlib.sha3_512(data).hexdigest()


def hash_file_md5(file_path):
    """
    Generate MD5 hash dari file.
    
    Args:
        file_path: Path ke file
        
    Returns:
        str: MD5 hash hexadecimal string
    """
    try:
        with open(file_path, 'rb') as file:
            return python_hashlib.md5(file.read()).hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
    except Exception as e:
        raise ValueError(f"Gagal hash file: {str(e)}")


def hash_file_sha256(file_path):
    """
    Generate SHA256 hash dari file.
    
    Args:
        file_path: Path ke file
        
    Returns:
        str: SHA256 hash hexadecimal string
    """
    try:
        with open(file_path, 'rb') as file:
            return python_hashlib.sha256(file.read()).hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
    except Exception as e:
        raise ValueError(f"Gagal hash file: {str(e)}")


def hash_file_chunked(file_path, algorithm='sha256', chunk_size=8192):
    """
    Generate hash dari file dengan chunked reading (untuk file besar).
    
    Args:
        file_path: Path ke file
        algorithm: Algoritma hash ('md5', 'sha1', 'sha256', dll)
        chunk_size: Ukuran chunk untuk dibaca
        
    Returns:
        str: Hash hexadecimal string
    """
    try:
        hash_obj = getattr(python_hashlib, algorithm)()
        with open(file_path, 'rb') as file:
            while chunk := file.read(chunk_size):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
    except AttributeError:
        raise ValueError(f"Algoritma tidak didukung: {algorithm}")
    except Exception as e:
        raise ValueError(f"Gagal hash file: {str(e)}")


def hmac_hash(data, key, algorithm='sha256'):
    """
    Generate HMAC hash.
    
    Args:
        data: Data untuk di-hash
        key: Secret key
        algorithm: Algoritma hash ('md5', 'sha1', 'sha256', dll)
        
    Returns:
        str: HMAC hexadecimal string
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    
    try:
        return python_hashlib.hmac(key, data, getattr(python_hashlib, algorithm)).hexdigest()
    except AttributeError:
        raise ValueError(f"Algoritma tidak didukung: {algorithm}")
    except Exception as e:
        raise ValueError(f"Gagal generate HMAC: {str(e)}")


def buat_salt(length=32):
    """
    Generate random salt untuk hashing.
    
    Args:
        length: Panjang salt dalam bytes
        
    Returns:
        str: Salt sebagai hexadecimal string
    """
    return os.urandom(length).hex()


def hash_with_salt(data, salt=None, algorithm='sha256'):
    """
    Generate hash dengan salt.
    
    Args:
        data: Data untuk di-hash
        salt: Salt (jika None, akan dibuat random)
        algorithm: Algoritma hash
        
    Returns:
        tuple: (hash, salt)
    """
    if salt is None:
        salt = buat_salt()
    
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(salt, str):
        salt = bytes.fromhex(salt)
    
    combined = data + salt
    hash_obj = getattr(python_hashlib, algorithm)(combined)
    
    return hash_obj.hexdigest(), salt.hex()


def verify_hash_with_salt(data, hash_value, salt, algorithm='sha256'):
    """
    Verify hash dengan salt.
    
    Args:
        data: Original data
        hash_value: Hash untuk diverifikasi
        salt: Salt yang digunakan
        algorithm: Algoritma hash
        
    Returns:
        bool: True jika hash cocok
    """
    try:
        computed_hash, _ = hash_with_salt(data, salt, algorithm)
        return computed_hash == hash_value
    except Exception:
        return False


# Daftar semua fungsi yang tersedia
__all__ = [
    'hash_md5',
    'hash_sha1',
    'hash_sha224',
    'hash_sha256',
    'hash_sha384',
    'hash_sha512',
    'hash_blake2b',
    'hash_blake2s',
    'hash_sha3_224',
    'hash_sha3_256',
    'hash_sha3_384',
    'hash_sha3_512',
    'hash_file_md5',
    'hash_file_sha256',
    'hash_file_chunked',
    'hmac_hash',
    'buat_salt',
    'hash_with_salt',
    'verify_hash_with_salt'
]