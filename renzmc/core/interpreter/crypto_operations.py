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
RenzmcLang Interpreter Crypto Operations Module

This module contains cryptographic operations functionality.
"""

import hashlib
import urllib.parse

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


class CryptoOperationsMixin:
    """
    Mixin class for cryptographic operations functionality.

    Provides encryption, decryption, hashing, and URL encoding.
    """

    def _encrypt(self, text, key):
        """
        Encrypt text using Fernet encryption.

        Args:
            text: Text to encrypt
            key: Encryption key

        Returns:
            Encrypted text (base64 encoded)

        Raises:
            ImportError: If cryptography module not available
            ValueError: If encryption fails
        """
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Modul 'cryptography' tidak terinstal. Silakan instal dengan 'pip install cryptography'")
        try:
            import base64

            salt = b"renzmc_salt"
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
            key_bytes = kdf.derive(key.encode())
            key_base64 = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(key_base64)
            encrypted = f.encrypt(text.encode())
            return base64.urlsafe_b64encode(encrypted).decode()
        except Exception as e:
            raise ValueError(f"Gagal mengenkripsi teks: {str(e)}")

    def _decrypt(self, encrypted_text, key):
        """
        Decrypt text using Fernet encryption.

        Args:
            encrypted_text: Encrypted text (base64 encoded)
            key: Decryption key

        Returns:
            Decrypted text

        Raises:
            ImportError: If cryptography module not available
            ValueError: If decryption fails
        """
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Modul 'cryptography' tidak terinstal. Silakan instal dengan 'pip install cryptography'")
        try:
            import base64

            salt = b"renzmc_salt"
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
            key_bytes = kdf.derive(key.encode())
            key_base64 = base64.urlsafe_b64encode(key_bytes)
            f = Fernet(key_base64)
            encrypted = base64.urlsafe_b64decode(encrypted_text.encode())
            decrypted = f.decrypt(encrypted)
            return decrypted.decode()
        except Exception as e:
            raise ValueError(f"Gagal mendekripsi teks: {str(e)}")

    def _hash_text(self, text, algorithm="sha256"):
        """
        Hash text using specified algorithm.

        Args:
            text: Text to hash
            algorithm: Hash algorithm (md5, sha1, sha256, sha512)

        Returns:
            Hexadecimal hash string

        Raises:
            ValueError: If algorithm not supported or hashing fails
        """
        try:
            if algorithm == "md5":
                return hashlib.md5(text.encode()).hexdigest()
            elif algorithm == "sha1":
                return hashlib.sha1(text.encode()).hexdigest()
            elif algorithm == "sha256":
                return hashlib.sha256(text.encode()).hexdigest()
            elif algorithm == "sha512":
                return hashlib.sha512(text.encode()).hexdigest()
            else:
                raise ValueError(f"Algoritma hash '{algorithm}' tidak didukung")
        except Exception as e:
            raise ValueError(f"Gagal melakukan hash teks: {str(e)}")

    def _url_encode(self, text):
        """
        URL encode text.

        Args:
            text: Text to encode

        Returns:
            URL encoded text

        Raises:
            ValueError: If encoding fails
        """
        try:
            return urllib.parse.quote(text)
        except Exception as e:
            raise ValueError(f"Gagal melakukan URL encode: {str(e)}")

    def _url_decode(self, text):
        """
        URL decode text.

        Args:
            text: Text to decode

        Returns:
            URL decoded text

        Raises:
            ValueError: If decoding fails
        """
        try:
            return urllib.parse.unquote(text)
        except Exception as e:
            raise ValueError(f"Gagal melakukan URL decode: {str(e)}")
