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
RenzMcLang UUID Library

Library untuk generating UUID (Universally Unique Identifier) dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import uuid as python_uuid
import re


def buat_uuid1(node=None, clock_seq=None):
    """
    Buat UUID berdasarkan host ID dan current time.
    
    Args:
        node: Node ID (opsional)
        clock_seq: Clock sequence (opsional)
        
    Returns:
        str: UUID string
    """
    return str(python_uuid.uuid1(node, clock_seq))


def buat_uuid3(namespace, name):
    """
    Buat UUID berdasarkan MD5 hash dari namespace dan name.
    
    Args:
        namespace: Namespace UUID
        name: String name
        
    Returns:
        str: UUID string
    """
    return str(python_uuid.uuid3(namespace, name))


def buat_uuid4():
    """
    Buat UUID random.
    
    Returns:
        str: UUID string random
    """
    return str(python_uuid.uuid4())


def buat_uuid5(namespace, name):
    """
    Buat UUID berdasarkan SHA-1 hash dari namespace dan name.
    
    Args:
        namespace: Namespace UUID
        name: String name
        
    Returns:
        str: UUID string
    """
    return str(python_uuid.uuid5(namespace, name))


def parse_uuid(uuid_string):
    """
    Parse UUID string ke UUID object.
    
    Args:
        uuid_string: UUID string
        
    Returns:
        str: UUID object sebagai string
    """
    try:
        parsed = python_uuid.UUID(uuid_string)
        return str(parsed)
    except ValueError:
        raise ValueError(f"UUID tidak valid: {uuid_string}")


def uuid_valid(uuid_string):
    """
    Cek apakah UUID string valid.
    
    Args:
        uuid_string: UUID string untuk dicek
        
    Returns:
        bool: True jika valid, False jika tidak
    """
    try:
        python_uuid.UUID(uuid_string)
        return True
    except ValueError:
        return False


def dapatkan_namespace_dns():
    """Dapatkan DNS namespace."""
    return python_uuid.NAMESPACE_DNS


def dapatkan_namespace_url():
    """Dapatkan URL namespace."""
    return python_uuid.NAMESPACE_URL


def dapatkan_namespace_oid():
    """Dapatkan OID namespace."""
    return python_uuid.NAMESPACE_OID


def dapatkan_namespace_x500():
    """Dapatkan X500 namespace."""
    return python_uuid.NAMESPACE_X500


# Mapping untuk memudahkan penggunaan
NAMESPACE_DNS = python_uuid.NAMESPACE_DNS
NAMESPACE_URL = python_uuid.NAMESPACE_URL
NAMESPACE_OID = python_uuid.NAMESPACE_OID
NAMESPACE_X500 = python_uuid.NAMESPACE_X500


# Daftar semua fungsi yang tersedia
__all__ = [
    'buat_uuid1',
    'buat_uuid3', 
    'buat_uuid4',
    'buat_uuid5',
    'parse_uuid',
    'uuid_valid',
    'dapatkan_namespace_dns',
    'dapatkan_namespace_url',
    'dapatkan_namespace_oid',
    'dapatkan_namespace_x500',
    'NAMESPACE_DNS',
    'NAMESPACE_URL',
    'NAMESPACE_OID',
    'NAMESPACE_X500'
]