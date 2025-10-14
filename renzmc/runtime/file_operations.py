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

from renzmc.utils.logging import logger
from renzmc.utils.rate_limiter import file_rate_limiter
from renzmc.utils.validation import PathValidator, ValidationError


class FileOperations:

    def __init__(self):
        self.validator = PathValidator()
        logger.info("FileOperations initialized")

    @file_rate_limiter
    def read_file(self, filename: str, encoding: str = "utf-8") -> str:
        try:
            filepath = self.validator.validate_file_read(filename)
            logger.debug(f"Reading file: {filepath}")
            with open(filepath, "r", encoding=encoding) as f:
                content = f.read()
            logger.info(f"Successfully read file: {filename} ({len(content)} bytes)")
            return content
        except ValidationError as e:
            logger.error(f"Validation error reading file '{filename}': {e}")
            raise
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            raise FileNotFoundError(f"File tidak ditemukan: {filename}")
        except PermissionError:
            logger.error(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk membaca file: {filename}")
        except UnicodeDecodeError as e:
            logger.error(f"Encoding error reading file '{filename}': {e}")
            raise UnicodeDecodeError(
                e.encoding,
                e.object,
                e.start,
                e.end,
                f"File bukan {encoding} yang valid: {filename}",
            )
        except Exception as e:
            logger.error(f"Unexpected error reading file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error membaca file: {e}")

    @file_rate_limiter
    def write_file(self, filename: str, content: str, encoding: str = "utf-8", mode: str = "w") -> None:
        if mode not in ("w", "a"):
            raise ValueError(f"Mode tidak valid: {mode} (harus 'w' atau 'a')")
        try:
            filepath = self.validator.validate_file_write(filename)
            logger.debug(f"Writing file: {filepath} (mode: {mode})")
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, mode, encoding=encoding) as f:
                f.write(content)
            logger.info(f"Successfully wrote file: {filename} ({len(content)} bytes)")
        except ValidationError as e:
            logger.error(f"Validation error writing file '{filename}': {e}")
            raise
        except PermissionError:
            logger.error(f"Permission denied writing file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk menulis file: {filename}")
        except Exception as e:
            logger.error(f"Unexpected error writing file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error menulis file: {e}")

    @file_rate_limiter
    def append_file(self, filename: str, content: str, encoding: str = "utf-8") -> None:
        self.write_file(filename, content, encoding=encoding, mode="a")

    @file_rate_limiter
    def delete_file(self, filename: str) -> None:
        try:
            filepath = self.validator.validate_path(filename)
            logger.debug(f"Deleting file: {filepath}")
            if not filepath.exists():
                raise FileNotFoundError(f"File tidak ditemukan: {filename}")
            if not filepath.is_file():
                raise ValueError(f"Bukan file: {filename}")
            filepath.unlink()
            logger.info(f"Successfully deleted file: {filename}")
        except ValidationError as e:
            logger.error(f"Validation error deleting file '{filename}': {e}")
            raise
        except FileNotFoundError:
            logger.error(f"File not found for deletion: {filename}")
            raise
        except PermissionError:
            logger.error(f"Permission denied deleting file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk menghapus file: {filename}")
        except Exception as e:
            logger.error(f"Unexpected error deleting file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error menghapus file: {e}")

    @file_rate_limiter
    def file_exists(self, filename: str) -> bool:
        try:
            filepath = self.validator.validate_path(filename)
            exists = filepath.exists() and filepath.is_file()
            logger.debug(f"File exists check: {filename} = {exists}")
            return exists
        except ValidationError as e:
            logger.warning(f"Validation error checking file existence '{filename}': {e}")
            return False
        except Exception as e:
            logger.error(f"Error checking file existence '{filename}': {e}")
            return False
