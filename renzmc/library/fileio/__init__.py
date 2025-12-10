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
RenzMcLang FileIO Library

Module ini menyediakan fungsi-fungsi untuk operasi file I/O,
mengikuti standar Python file operations dengan nama fungsi dalam Bahasa Indonesia.

Classes:
- File: File object wrapper
- TextIOWrapper: Text file wrapper
- BufferedReader: Binary file reader
- BufferedWriter: Binary file writer

Functions:
- Reading: read_text, read_lines, read_bytes, read_json, read_csv
- Writing: write_text, write_lines, write_bytes, write_json, write_csv
- File Operations: copy, move, delete, exists, size, is_file, is_dir
- Directory Operations: create_dir, remove_dir, list_dir, walk_dir

Usage:
    dari fileio impor read_text, write_text
    
    content = read_text('data.txt')
    write_text('output.txt', content)
"""

import shutil as py_shutil
import os as py_os
import json as py_json
import csv as py_csv
from pathlib import Path
from typing import List, Dict, Any, Optional, Union, TextIO, BinaryIO

# File Reading Functions


def read_text(file_path: str, encoding: str = 'utf-8') -> str:
    """
    Baca file sebagai text.

    Args:
        file_path: Path file yang akan dibaca
        encoding: Encoding file (default: utf-8)

    Returns:
        Content file sebagai string

    Raises:
        FileNotFoundError: Jika file tidak ada
        UnicodeDecodeError: Jika encoding tidak cocok

    Example:
        content = read_text('data.txt')
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()


def read_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
    """
    Baca file sebagai list of lines.

    Args:
        file_path: Path file yang akan dibaca
        encoding: Encoding file (default: utf-8)

    Returns:
        List of lines

    Example:
        lines = read_lines('data.txt')  # ['line1', 'line2', ...]
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.readlines()


def read_bytes(file_path: str) -> bytes:
    """
    Baca file sebagai bytes.

    Args:
        file_path: Path file yang akan dibaca

    Returns:
        Content file sebagai bytes

    Example:
        data = read_bytes('image.png')
    """
    with open(file_path, 'rb') as f:
        return f.read()


def read_json(file_path: str, encoding: str = 'utf-8') -> Dict[str, Any]:
    """
    Baca JSON file.

    Args:
        file_path: Path file JSON yang akan dibaca
        encoding: Encoding file (default: utf-8)

    Returns:
        Dictionary hasil parsing JSON

    Example:
        data = read_json('config.json')
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return py_json.load(f)


def read_csv(file_path: str, delimiter: str = ',', encoding: str = 'utf-8') -> List[List[str]]:
    """
    Baca CSV file.

    Args:
        file_path: Path file CSV yang akan dibaca
        delimiter: Delimiter (default: ',')
        encoding: Encoding file (default: utf-8)

    Returns:
        List of rows (setiap row adalah list of strings)

    Example:
        rows = read_csv('data.csv', delimiter=';')
    """
    with open(file_path, 'r', encoding=encoding, newline='') as f:
        reader = py_csv.reader(f, delimiter=delimiter)
        return list(reader)

# File Writing Functions


def write_text(file_path: str, content: str, encoding: str = 'utf-8'):
    """
    Tulis text ke file.

    Args:
        file_path: Path file yang akan ditulis
        content: Text content
        encoding: Encoding file (default: utf-8)

    Example:
        write_text('output.txt', 'Hello World')
    """
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(content)


def write_lines(file_path: str, lines: List[str], encoding: str = 'utf-8'):
    """
    Tulis list of lines ke file.

    Args:
        file_path: Path file yang akan ditulis
        lines: List of lines
        encoding: Encoding file (default: utf-8)

    Example:
        write_lines('output.txt', ['line1', 'line2'])
    """
    with open(file_path, 'w', encoding=encoding) as f:
        f.writelines(lines)


def write_bytes(file_path: str, content: bytes):
    """
    Tulis bytes ke file.

    Args:
        file_path: Path file yang akan ditulis
        content: Bytes content

    Example:
        write_bytes('output.bin', b'\\x00\\x01\\x02')
    """
    with open(file_path, 'wb') as f:
        f.write(content)


def write_json(file_path: str, data: Dict[str, Any], indent: Optional[int] = None,
               encoding: str = 'utf-8'):
    """
    Tulis data ke JSON file.

    Args:
        file_path: Path file JSON yang akan ditulis
        data: Data yang akan ditulis (dictionary)
        indent: Indentasi untuk pretty printing (optional)
        encoding: Encoding file (default: utf-8)

    Example:
        write_json('config.json', {'name': 'Budi'}, indent=2)
    """
    with open(file_path, 'w', encoding=encoding) as f:
        py_json.dump(data, f, indent=indent, ensure_ascii=False)


def write_csv(file_path: str, rows: List[List[str]], delimiter: str = ',',
              encoding: str = 'utf-8'):
    """
    Tulis data ke CSV file.

    Args:
        file_path: Path file CSV yang akan ditulis
        rows: List of rows
        delimiter: Delimiter (default: ',')
        encoding: Encoding file (default: utf-8)

    Example:
        write_csv('output.csv', [['Name', 'Age'], ['Budi', '25']])
    """
    with open(file_path, 'w', encoding=encoding, newline='') as f:
        writer = py_csv.writer(f, delimiter=delimiter)
        writer.writerows(rows)

# File Operations


def copy(src: str, dst: str):
    """
    Salin file dari src ke dst.

    Args:
        src: Source file path
        dst: Destination file path

    Example:
        copy('source.txt', 'backup.txt')
    """
    py_shutil.copy2(src, dst)


def move(src: str, dst: str):
    """
    Pindahkan file dari src ke dst.

    Args:
        src: Source file path
        dst: Destination file path

    Example:
        move('old.txt', 'new.txt')
    """
    py_shutil.move(src, dst)


def delete(file_path: str):
    """
    Hapus file.

    Args:
        file_path: Path file yang akan dihapus

    Example:
        delete('temp.txt')
    """
    py_os.remove(file_path)


def exists(file_path: str) -> bool:
    """
    Cek apakah file ada.

    Args:
        file_path: Path file yang akan dicek

    Returns:
        True jika file ada, False jika tidak
    """
    return py_os.path.exists(file_path)


def size(file_path: str) -> int:
    """
    Dapatkan ukuran file dalam bytes.

    Args:
        file_path: Path file

    Returns:
        Ukuran file dalam bytes
    """
    return py_os.path.getsize(file_path)


def is_file(file_path: str) -> bool:
    """
    Cek apakah path adalah file.

    Args:
        file_path: Path yang akan dicek

    Returns:
        True jika file, False jika tidak
    """
    return py_os.path.isfile(file_path)


def is_dir(file_path: str) -> bool:
    """
    Cek apakah path adalah directory.

    Args:
        file_path: Path yang akan dicek

    Returns:
        True jika directory, False jika tidak
    """
    return py_os.path.isdir(file_path)

# Directory Operations


def create_dir(dir_path: str, exist_ok: bool = True):
    """
    Buat directory.

    Args:
        dir_path: Path directory yang akan dibuat
        exist_ok: Tidak error jika directory sudah ada

    Example:
        create_dir('data/output')
    """
    py_os.makedirs(dir_path, exist_ok=exist_ok)


def remove_dir(dir_path: str, ignore_errors: bool = False):
    """
    Hapus directory dan isinya.

    Args:
        dir_path: Path directory yang akan dihapus
        ignore_errors: Ignore errors saat penghapusan

    Example:
        remove_dir('temp_dir')
    """
    py_shutil.rmtree(dir_path, ignore_errors=ignore_errors)


def list_dir(dir_path: str = '.') -> List[str]:
    """
    Daftar file dan directory dalam directory.

    Args:
        dir_path: Path directory (default: current directory)

    Returns:
        List nama file dan directory

    Example:
        files = list_dir('/home/user')
    """
    return py_os.listdir(dir_path)


def walk_dir(dir_path: str):
    """
    Walk directory tree.

    Args:
        dir_path: Root directory

    Yields:
        Tuple (dirpath, dirnames, filenames)

    Example:
        for dirpath, dirnames, filenames in walk_dir('/home'):
            print(f'Directory: {dirpath}')
            for filename in filenames:
                print(f'  File: {filename}')
    """
    for dirpath, dirnames, filenames in py_os.walk(dir_path):
        yield (dirpath, dirnames, filenames)

# File Context Managers


def open_text(file_path: str, mode: str = 'r', encoding: str = 'utf-8') -> TextIO:
    """
    Buka text file dengan mode tertentu.

    Args:
        file_path: Path file
        mode: Mode ('r', 'w', 'a', dll)
        encoding: Encoding file

    Returns:
        Text file object

    Example:
        dengan open_text('data.txt', 'w') sebagai f:
            f.write('Hello')
    """
    return open(file_path, mode, encoding=encoding)


def open_binary(file_path: str, mode: str = 'rb') -> BinaryIO:
    """
    Buka binary file dengan mode tertentu.

    Args:
        file_path: Path file
        mode: Mode ('rb', 'wb', 'ab', dll)

    Returns:
        Binary file object

    Example:
        dengan open_binary('data.bin', 'wb') sebagai f:
            f.write(b'Hello')
    """
    return open(file_path, mode)

# Utility Functions


def get_extension(file_path: str) -> str:
    """
    Dapatkan file extension.

    Args:
        file_path: Path file

    Returns:
        File extension (termasuk dot)

    Example:
        ext = get_extension('file.txt')  # '.txt'
    """
    return Path(file_path).suffix


def get_basename(file_path: str) -> str:
    """
    Dapatkan filename tanpa path.

    Args:
        file_path: Path file

    Returns:
        Filename saja

    Example:
        name = get_basename('/path/to/file.txt')  # 'file.txt'
    """
    return Path(file_path).name


def get_stem(file_path: str) -> str:
    """
    Dapatkan filename tanpa extension.

    Args:
        file_path: Path file

    Returns:
        Filename tanpa extension

    Example:
        stem = get_stem('file.txt')  # 'file'
    """
    return Path(file_path).stem


def get_parent(file_path: str) -> str:
    """
    Dapatkan parent directory.

    Args:
        file_path: Path file

    Returns:
        Parent directory path

    Example:
        parent = get_parent('/path/to/file.txt')  # '/path/to'
    """
    return str(Path(file_path).parent)


def join_paths(*paths) -> str:
    """
    Gabungkan path components.

    Args:
        *paths: Path components

    Returns:
        Joined path

    Example:
        path = join_paths('/home', 'user', 'file.txt')
    """
    return str(Path(*paths))


def absolute_path(file_path: str) -> str:
    """
    Dapatkan absolute path.

    Args:
        file_path: Relative path

    Returns:
        Absolute path
    """
    return str(Path(file_path).resolve())


# Indonesian Aliases
baca_teks = read_text
baca_baris = read_lines
baca_bytes = read_bytes
baca_json = read_json
baca_csv = read_csv
tulis_teks = write_text
tulis_baris = write_lines
tulis_bytes = write_bytes
tulis_json = write_json
tulis_csv = write_csv
salin = copy
pindahkan = move
hapus = delete
ada = exists
ukuran = size
adalah_file = is_file
adalah_dir = is_dir
buat_dir = create_dir
hapus_dir = remove_dir
daftar_dir = list_dir
jelajahi_dir = walk_dir
buka_teks = open_text
buka_binary = open_binary
dapatkan_ekstensi = get_extension
dapatkan_nama_file = get_basename
dapatkan_stem = get_stem
dapatkan_induk = get_parent
gabungkan_path = join_paths
path_absolut = absolute_path

__all__ = [
    # Reading Functions
    "read_text", "read_lines", "read_bytes", "read_json", "read_csv",
    # Writing Functions
    "write_text", "write_lines", "write_bytes", "write_json", "write_csv",
    # File Operations
    "copy", "move", "delete", "exists", "size", "is_file", "is_dir",
    # Directory Operations
    "create_dir", "remove_dir", "list_dir", "walk_dir",
    # Context Managers
    "open_text", "open_binary",
    # Utility Functions
    "get_extension", "get_basename", "get_stem", "get_parent",
    "join_paths", "absolute_path",
    # Indonesian Aliases
    "baca_teks", "baca_baris", "baca_bytes", "baca_json", "baca_csv",
    "tulis_teks", "tulis_baris", "tulis_bytes", "tulis_json", "tulis_csv",
    "salin", "pindahkan", "hapus", "ada", "ukuran", "adalah_file",
    "adalah_dir", "buat_dir", "hapus_dir", "daftar_dir", "jelajahi_dir",
    "buka_teks", "buka_binary", "dapatkan_ekstensi", "dapatkan_nama_file",
    "dapatkan_stem", "dapatkan_induk", "gabungkan_path", "path_absolut"
]
