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

import base64
import hashlib
import urllib.parse
import uuid

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    Fernet = None
    hashes = None
    PBKDF2HMAC = None
    CRYPTOGRAPHY_AVAILABLE = False


class CryptoOperations:

    @staticmethod
    def encrypt(text, key):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Cryptography library tidak tersedia")
        try:
            if isinstance(key, str):
                key_bytes = key.encode("utf-8")
            else:
                key_bytes = key
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"salt_", iterations=100000)
            derived_key = base64.urlsafe_b64encode(kdf.derive(key_bytes))
            cipher = Fernet(derived_key)
            encrypted = cipher.encrypt(text.encode("utf-8"))
            return base64.b64encode(encrypted).decode("utf-8")
        except Exception as e:
            raise ValueError(f"Error dalam enkripsi: {str(e)}")

    @staticmethod
    def decrypt(encrypted_text, key):
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Cryptography library tidak tersedia")
        try:
            if isinstance(key, str):
                key_bytes = key.encode("utf-8")
            else:
                key_bytes = key
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"salt_", iterations=100000)
            derived_key = base64.urlsafe_b64encode(kdf.derive(key_bytes))
            cipher = Fernet(derived_key)
            encrypted_bytes = base64.b64decode(encrypted_text.encode("utf-8"))
            decrypted = cipher.decrypt(encrypted_bytes)
            return decrypted.decode("utf-8")
        except Exception as e:
            raise ValueError(f"Error dalam dekripsi: {str(e)}")

    @staticmethod
    def hash_text(text, algorithm="sha256"):
        try:
            if algorithm == "md5":
                return hashlib.md5(text.encode("utf-8")).hexdigest()
            elif algorithm == "sha1":
                return hashlib.sha1(text.encode("utf-8")).hexdigest()
            elif algorithm == "sha256":
                return hashlib.sha256(text.encode("utf-8")).hexdigest()
            elif algorithm == "sha512":
                return hashlib.sha512(text.encode("utf-8")).hexdigest()
            else:
                raise ValueError(f"Algoritma hash tidak didukung: {algorithm}")
        except Exception as e:
            raise ValueError(f"Error dalam hashing: {str(e)}")

    @staticmethod
    def create_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def url_encode(text):
        return urllib.parse.quote(text)

    @staticmethod
    def url_decode(text):
        return urllib.parse.unquote(text)
