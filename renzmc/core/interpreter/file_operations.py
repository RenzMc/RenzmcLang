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
RenzmcLang Interpreter File Operations Module

This module contains file and directory operations functionality.
"""

import json
import os
import os.path
import shutil

from renzmc.core.error import FileError


class FileOperationsMixin:
    """
    Mixin class for file operations functionality.

    Provides methods for file I/O and directory management.
    """

    def _open_file(self, filename, mode="r"):
        """
        Open a file.

        Args:
            filename: Path to the file
            mode: File open mode

        Returns:
            File object

        Raises:
            FileError: If file cannot be opened
        """
        try:
            return open(filename, mode)
        except Exception as e:
            raise FileError(f"Gagal membuka file '{filename}': {str(e)}")

    def _close_file(self, file):
        """
        Close a file.

        Args:
            file: File object to close

        Raises:
            FileError: If file cannot be closed
        """
        try:
            file.close()
        except Exception as e:
            raise FileError(f"Gagal menutup file: {str(e)}")

    def _read_line(self, file):
        """
        Read a line from a file.

        Args:
            file: File object

        Returns:
            The read line

        Raises:
            FileError: If read fails
        """
        try:
            return file.readline()
        except Exception as e:
            raise FileError(f"Gagal membaca baris dari file: {str(e)}")

    def _read_all_lines(self, file):
        """
        Read all lines from a file.

        Args:
            file: File object

        Returns:
            List of lines

        Raises:
            FileError: If read fails
        """
        try:
            return file.readlines()
        except Exception as e:
            raise FileError(f"Gagal membaca semua baris dari file: {str(e)}")

    def _write_line(self, file, line):
        """
        Write a line to a file.

        Args:
            file: File object
            line: Line to write

        Raises:
            FileError: If write fails
        """
        try:
            file.write(line)
        except Exception as e:
            raise FileError(f"Gagal menulis ke file: {str(e)}")

    def _flush_file(self, file):
        """
        Flush a file buffer.

        Args:
            file: File object

        Raises:
            FileError: If flush fails
        """
        try:
            file.flush()
        except Exception as e:
            raise FileError(f"Gagal flush file: {str(e)}")

    def _file_exists(self, path):
        """
        Check if a file exists.

        Args:
            path: Path to check

        Returns:
            bool: True if file exists

        Raises:
            FileError: If check fails
        """
        try:
            return os.path.exists(path)
        except Exception as e:
            raise FileError(f"Gagal memeriksa keberadaan file '{path}': {str(e)}")

    def _make_directory(self, path):
        """
        Create a directory.

        Args:
            path: Directory path to create

        Raises:
            FileError: If creation fails
        """
        try:
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            raise FileError(f"Gagal membuat direktori '{path}': {str(e)}")

    def _remove_directory(self, path):
        """
        Remove a directory.

        Args:
            path: Directory path to remove

        Raises:
            FileError: If removal fails
        """
        try:
            shutil.rmtree(path)
        except Exception as e:
            raise FileError(f"Gagal menghapus direktori '{path}': {str(e)}")

    def _list_directory(self, path="."):
        """
        List directory contents.

        Args:
            path: Directory path to list

        Returns:
            List of filenames

        Raises:
            FileError: If listing fails
        """
        try:
            return os.listdir(path)
        except Exception as e:
            raise FileError(f"Gagal membaca direktori '{path}': {str(e)}")

    def _join_path(self, *paths):
        """
        Join path components.

        Args:
            *paths: Path components to join

        Returns:
            Joined path

        Raises:
            FileError: If join fails
        """
        try:
            return os.path.join(*paths)
        except Exception as e:
            raise FileError(f"Gagal menggabungkan path: {str(e)}")

    def _file_path(self, path):
        """
        Get filename from path.

        Args:
            path: Full path

        Returns:
            Filename

        Raises:
            FileError: If extraction fails
        """
        try:
            return os.path.basename(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan nama file dari '{path}': {str(e)}")

    def _directory_path(self, path):
        """
        Get directory from path.

        Args:
            path: Full path

        Returns:
            Directory path

        Raises:
            FileError: If extraction fails
        """
        try:
            return os.path.dirname(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan direktori dari '{path}': {str(e)}")

    def _file_size(self, path):
        """
        Get file size.

        Args:
            path: File path

        Returns:
            File size in bytes

        Raises:
            FileError: If size check fails
        """
        try:
            return os.path.getsize(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan ukuran file '{path}': {str(e)}")

    def _file_modification_time(self, path):
        """
        Get file modification time.

        Args:
            path: File path

        Returns:
            Modification timestamp

        Raises:
            FileError: If time check fails
        """
        try:
            return os.path.getmtime(path)
        except Exception as e:
            raise FileError(f"Gagal mendapatkan waktu modifikasi file '{path}': {str(e)}")

    def _json_to_text(self, obj):
        """
        Convert object to JSON string.

        Args:
            obj: Object to convert

        Returns:
            JSON string

        Raises:
            ValueError: If conversion fails
        """
        try:
            return json.dumps(obj)
        except Exception as e:
            raise ValueError(f"Gagal mengkonversi objek ke JSON: {str(e)}")

    def _text_to_json(self, text):
        """
        Convert JSON string to object.

        Args:
            text: JSON string

        Returns:
            Parsed object

        Raises:
            ValueError: If parsing fails
        """
        try:
            return json.loads(text)
        except Exception as e:
            raise ValueError(f"Gagal mengkonversi JSON ke objek: {str(e)}")
