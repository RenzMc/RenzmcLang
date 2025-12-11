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
RenzMcLang Base64 Library

Library untuk encoding dan decoding Base64 dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import base64 as python_base64
import io


def encode_base64(data):
    """
    Encode data ke Base64.

    Args:
        data: String atau bytes untuk di-encode

    Returns:
        str: Base64 encoded string
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    return python_base64.b64encode(data).decode("utf-8")


def decode_base64(encoded_data):
    """
    Decode Base64 string.

    Args:
        encoded_data: Base64 encoded string

    Returns:
        str: Decoded string
    """
    try:
        decoded = python_base64.b64decode(encoded_data)
        return decoded.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Gagal decode Base64: {str(e)}")


def encode_base64_bytes(data):
    """
    Encode data ke Base64 sebagai bytes.

    Args:
        data: String atau bytes untuk di-encode

    Returns:
        bytes: Base64 encoded bytes
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    return python_base64.b64encode(data)


def decode_base64_bytes(encoded_data):
    """
    Decode Base64 bytes.

    Args:
        encoded_data: Base64 encoded bytes atau string

    Returns:
        bytes: Decoded bytes
    """
    if isinstance(encoded_data, str):
        encoded_data = encoded_data.encode("utf-8")
    try:
        return python_base64.b64decode(encoded_data)
    except Exception as e:
        raise ValueError(f"Gagal decode Base64: {str(e)}")


def encode_base64_urlsafe(data):
    """
    Encode data ke URL-safe Base64.

    Args:
        data: String atau bytes untuk di-encode

    Returns:
        str: URL-safe Base64 encoded string
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    return python_base64.urlsafe_b64encode(data).decode("utf-8")


def decode_base64_urlsafe(encoded_data):
    """
    Decode URL-safe Base64 string.

    Args:
        encoded_data: URL-safe Base64 encoded string

    Returns:
        str: Decoded string
    """
    try:
        decoded = python_base64.urlsafe_b64decode(encoded_data)
        return decoded.decode("utf-8")
    except Exception as e:
        raise ValueError(f"Gagal decode URL-safe Base64: {str(e)}")


def encode_base64_file(file_path):
    """
    Encode file ke Base64.

    Args:
        file_path: Path ke file

    Returns:
        str: Base64 encoded content
    """
    try:
        with open(file_path, "rb") as file:
            return python_base64.b64encode(file.read()).decode("utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")
    except Exception as e:
        raise ValueError(f"Gagal encode file: {str(e)}")


def decode_base64_ke_file(encoded_data, file_path):
    """
    Decode Base64 dan simpan ke file.

    Args:
        encoded_data: Base64 encoded string
        file_path: Path untuk menyimpan file
    """
    try:
        decoded = python_base64.b64decode(encoded_data)
        with open(file_path, "wb") as file:
            file.write(decoded)
    except Exception as e:
        raise ValueError(f"Gagal decode ke file: {str(e)}")


def base64_valid(encoded_data):
    """
    Cek apakah string adalah Base64 yang valid.

    Args:
        encoded_data: String untuk dicek

    Returns:
        bool: True jika valid Base64
    """
    try:
        if isinstance(encoded_data, str):
            # Cek panjang harus kelipatan 4 dan hanya karakter Base64
            if len(encoded_data) % 4 != 0:
                return False
            # Cek karakter yang valid
            base64_pattern = r"^[A-Za-z0-9+/]*={0,2}$"
            if not re.match(base64_pattern, encoded_data):
                return False
            python_base64.b64decode(encoded_data, validate=True)
        return True
    except Exception:
        return False


import re


# Daftar semua fungsi yang tersedia
__all__ = [
    "encode_base64",
    "decode_base64",
    "encode_base64_bytes",
    "decode_base64_bytes",
    "encode_base64_urlsafe",
    "decode_base64_urlsafe",
    "encode_base64_file",
    "decode_base64_ke_file",
    "base64_valid",
]
