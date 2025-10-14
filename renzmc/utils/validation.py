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

import re
from pathlib import Path
from typing import Optional, Set, Union


class ValidationError(Exception):
    pass


class PathValidator:

    def __init__(
        self,
        base_dir: Optional[Path] = None,
        allowed_extensions: Optional[Set[str]] = None,
        max_file_size: int = 10000000,
    ):
        self.base_dir = (base_dir or Path.cwd()).resolve()
        self.allowed_extensions = allowed_extensions or {
            ".txt",
            ".json",
            ".csv",
            ".md",
            ".rmc",
            ".py",
            ".yaml",
            ".yml",
            ".xml",
            ".html",
            ".css",
            ".js",
        }
        self.max_file_size = max_file_size
        self.dangerous_patterns = ["..", "~", "$", "`", "|", ";", "&", "\x00"]

    def validate_path(self, filepath: Union[str, Path]) -> Path:
        if not filepath:
            raise ValidationError("Nama file tidak boleh kosong")
        filepath_str = str(filepath)
        for pattern in self.dangerous_patterns:
            if pattern in filepath_str:
                raise ValidationError(f"Nama file mengandung karakter berbahaya: '{pattern}'")
        try:
            abs_path = (self.base_dir / filepath).resolve()
        except (ValueError, OSError) as e:
            raise ValidationError(f"Path tidak valid: {e}")
        try:
            abs_path.relative_to(self.base_dir)
        except ValueError:
            raise ValidationError(
                f"Akses ditolak: File di luar direktori yang diizinkan\nBase: {self.base_dir}\nRequested: {abs_path}"
            )
        return abs_path

    def validate_file_read(self, filepath: Union[str, Path]) -> Path:
        abs_path = self.validate_path(filepath)
        if not abs_path.exists():
            raise ValidationError(f"File tidak ditemukan: {filepath}")
        if not abs_path.is_file():
            raise ValidationError(f"Bukan file: {filepath}")
        size = abs_path.stat().st_size
        if size > self.max_file_size:
            raise ValidationError(
                f"File terlalu besar: {size:,} bytes (maksimum: {self.max_file_size:,} bytes)"
            )
        if abs_path.suffix.lower() not in self.allowed_extensions:
            raise ValidationError(
                f"Ekstensi file tidak diizinkan: {abs_path.suffix}\nEkstensi yang diizinkan: {', '.join(sorted(self.allowed_extensions))}"
            )
        return abs_path

    def validate_file_write(self, filepath: Union[str, Path]) -> Path:
        abs_path = self.validate_path(filepath)
        if abs_path.suffix.lower() not in self.allowed_extensions:
            raise ValidationError(
                f"Ekstensi file tidak diizinkan: {abs_path.suffix}\nEkstensi yang diizinkan: {', '.join(sorted(self.allowed_extensions))}"
            )
        if not abs_path.parent.exists():
            raise ValidationError(f"Direktori tidak ditemukan: {abs_path.parent}")
        return abs_path


class StringValidator:

    @staticmethod
    def validate_identifier(name: str) -> str:
        if not name:
            raise ValidationError("Nama identifier tidak boleh kosong")
        if not re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", name):
            raise ValidationError(
                f"Identifier tidak valid: '{name}'\nIdentifier harus dimulai dengan huruf atau underscore, dan hanya boleh mengandung huruf, angka, dan underscore"
            )
        if len(name) > 255:
            raise ValidationError("Identifier terlalu panjang (maksimum 255 karakter)")
        return name

    @staticmethod
    def validate_url(url: str) -> str:
        if not url:
            raise ValidationError("URL tidak boleh kosong")
        url_pattern = re.compile(
            "^https?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+[A-Z]{2,6}\\.?|localhost|\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})(?::\\d+)?(?:/?|[/?]\\S+)$",
            re.IGNORECASE,
        )
        if not url_pattern.match(url):
            raise ValidationError(f"URL tidak valid: {url}")
        if url.lower().startswith(("file://", "ftp://", "data:")):
            raise ValidationError(f"Protocol tidak diizinkan: {url}")
        return url


path_validator = PathValidator()
string_validator = StringValidator()
