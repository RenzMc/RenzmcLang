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
RenzMcLang Pathlib Library

Library untuk path manipulation object-oriented dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import pathlib as python_pathlib
import os


class Path:
    """
    Class untuk path manipulation object-oriented.
    """
    
    def __init__(self, *pathsegments):
        """
        Inisialisasi Path object.
        
        Args:
            *pathsegments: Path segments
        """
        self._path = python_pathlib.Path(*pathsegments)
    
    def __str__(self):
        """String representation."""
        return str(self._path)
    
    def __repr__(self):
        """Representation."""
        return f"Path('{self._path}')"
    
    def dapatkan_nama(self):
        """Dapatkan nama file atau direktori terakhir."""
        return self._path.name
    
    def dapatkan_stem(self):
        """Dapatkan nama tanpa extension."""
        return self._path.stem
    
    def dapatkan_extension(self):
        """Dapatkan file extension."""
        return self._path.suffix
    
    def dapatkan_parent(self):
        """Dapatkan parent directory."""
        return Path(self._path.parent)
    
    def dapatkan_absolute(self):
        """Dapatkan absolute path."""
        return Path(self._path.absolute())
    
    def dapatkan_resolve(self):
        """Resolve path (hilangkan symbolic links, .., .)."""
        return Path(self._path.resolve())
    
    def ada(self):
        """Cek apakah path ada."""
        return self._path.exists()
    
    def adalah_file(self):
        """Cek apakah path adalah file."""
        return self._path.is_file()
    
    def adalah_dir(self):
        """Cek apakah path adalah directory."""
        return self._path.is_dir()
    
    def adalah_symlink(self):
        """Cek apakah path adalah symbolic link."""
        return self._path.is_symlink()
    
    def buat_dir(self, parents=False, exist_ok=False):
        """
        Buat directory.
        
        Args:
            parents: Buat parent directories jika tidak ada
            exist_ok: Tidak error jika directory sudah ada
        """
        self._path.mkdir(parents=parents, exist_ok=exist_ok)
    
    def hapus_dir(self, ignore_errors=False):
        """
        Hapus directory tree.
        
        Args:
            ignore_errors: Ignore errors saat penghapusan
        """
        if self._path.is_dir():
            import shutil
            shutil.rmtree(self._path, ignore_errors=ignore_errors)
    
    def hapus_file(self):
        """Hapus file."""
        if self._path.is_file():
            self._path.unlink()
    
    def hapus(self):
        """Hapus file atau directory (jika kosong)."""
        if self._path.exists():
            self._path.unlink()
    
    def salin_ke(self, destination):
        """
        Salin file ke destination.
        
        Args:
            destination: Destination path
        """
        if self._path.is_file():
            import shutil
            shutil.copy2(self._path, destination)
    
    def pindah_ke(self, destination):
        """
        Pindah file ke destination.
        
        Args:
            destination: Destination path
        """
        self._path.replace(destination)
    
    def rename_ke(self, nama_baru):
        """
        Rename file atau directory.
        
        Args:
            nama_baru: Nama baru
        """
        self._path.rename(nama_baru)
    
    def gabung(self, *pathsegments):
        """
        Gabungkan dengan path segments lain.
        
        Args:
            *pathsegments: Path segments untuk digabungkan
            
        Returns:
            Path: Path baru yang digabungkan
        """
        return Path(self._path.joinpath(*pathsegments))
    
    def bagi_semua(self):
        """
        Bagi path menjadi semua components.
        
        Returns:
            list: List path components
        """
        return list(self._path.parts)
    
    def dapatkan_anchors(self):
        """Dapatkan anchor (drive atau root)."""
        return self._path.anchor
    
    def dapatkan_drive(self):
        """Dapatkan drive letter (Windows)."""
        return self._path.drive
    
    def dapatkan_root(self):
        """Dapatkan root (/ atau C:\\)."""
        return self._path.root
    
    def relatif_ke(self, other):
        """
        Dapatkan relative path terhadap path lain.
        
        Args:
            other: Path lain untuk reference
            
        Returns:
            Path: Relative path
        """
        return Path(self._path.relative_to(other))
    
    def dapatkan_stat(self):
        """Dapatkan file stat information."""
        stat = self._path.stat()
        return {
            'size': stat.st_size,
            'created': stat.st_ctime,
            'modified': stat.st_mtime,
            'accessed': stat.st_atime,
            'mode': stat.st_mode
        }
    
    def dapatkan_ukuran(self):
        """Dapatkan ukuran file dalam bytes."""
        return self._path.stat().st_size if self._path.is_file() else 0
    
    def buka_file(self, mode='r', encoding='utf-8'):
        """
        Buka file untuk membaca atau menulis.
        
        Args:
            mode: Mode file ('r', 'w', 'a', 'rb', 'wb', dll)
            encoding: Encoding (default utf-8)
            
        Returns:
            file object
        """
        return open(self._path, mode, encoding=encoding)
    
    def baca_teks(self, encoding='utf-8'):
        """
        Baca file sebagai teks.
        
        Args:
            encoding: File encoding
            
        Returns:
            str: File content
        """
        return self._path.read_text(encoding=encoding)
    
    def tulis_teks(self, content, encoding='utf-8'):
        """
        Tulis teks ke file.
        
        Args:
            content: Teks untuk ditulis
            encoding: File encoding
        """
        self._path.write_text(content, encoding=encoding)
    
    def baca_bytes(self):
        """
        Baca file sebagai bytes.
        
        Returns:
            bytes: File content
        """
        return self._path.read_bytes()
    
    def tulis_bytes(self, content):
        """
        Tulis bytes ke file.
        
        Args:
            content: Bytes untuk ditulis
        """
        self._path.write_bytes(content)
    
    def glob(self, pattern):
        """
        Cari files dengan pattern.
        
        Args:
            pattern: Glob pattern (*, ?, [abc], dll)
            
        Returns:
            generator: Generator Path objects
        """
        for path in self._path.glob(pattern):
            yield Path(path)
    
    def rglob(self, pattern):
        """
        Cari files secara rekursif dengan pattern.
        
        Args:
            pattern: Glob pattern
            
        Returns:
            generator: Generator Path objects
        """
        for path in self._path.rglob(pattern):
            yield Path(path)
    
    def iter_dir(self):
        """
        Iterasi isi directory.
        
        Returns:
            generator: Generator Path objects
        """
        for path in self._path.iterdir():
            yield Path(path)
    
    def dapatkan_isi_dir(self):
        """
        Dapatkan semua isi directory sebagai list.
        
        Returns:
            list: List Path objects
        """
        return [Path(path) for path in self._path.iterdir()]
    
    def kosongkan_dir(self):
        """Kosongkan directory (hapus semua isi)."""
        if self._path.is_dir():
            import shutil
            for item in self._path.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
    
    def bersihkan(self):
        """Bersihkan path (normalisasi)."""
        return Path(self._path.resolve())
    
    def sama_dengan(self, other):
        """
        Cek apakah path sama dengan path lain.
        
        Args:
            other: Path lain untuk dibandingkan
            
        Returns:
            bool: True jika sama
        """
        return self._path.samefile(other) if isinstance(other, (Path, python_pathlib.Path)) else False


def path_current():
    """Dapatkan current working directory."""
    return Path(python_pathlib.Path.cwd())


def path_home():
    """Dapatkan home directory."""
    return Path(python_pathlib.Path.home())


def path_temp():
    """Dapatkan temporary directory."""
    import tempfile
    return Path(tempfile.gettempdir())


def gabung_path(*paths):
    """
    Gabungkan beberapa path segments.
    
    Args:
        *paths: Path segments
        
    Returns:
        Path: Combined path
    """
    return Path(*paths)


def path_absolute(path):
    """
    Dapatkan absolute path dari path string.
    
    Args:
        path: Path string
        
    Returns:
        Path: Absolute path
    """
    return Path(path).dapatkan_absolute()


def path_relatif(path, start='.'):
    """
    Dapatkan relative path.
    
    Args:
        path: Path untuk dikonversi
        start: Starting point (default current directory)
        
    Returns:
        Path: Relative path
    """
    return Path(path).relatif_ke(start)


def expand_user(path):
    """
    Expand ~ ke home directory.
    
    Args:
        path: Path dengan ~
        
    Returns:
        Path: Expanded path
    """
    return Path(python_pathlib.Path(path).expanduser())


def expand_vars(path):
    """
    Expand environment variables.
    
    Args:
        path: Path dengan environment variables
        
    Returns:
        str: Expanded path
    """
    return os.path.expandvars(path)


def path_normal(path):
    """
    Normalisasi path (hapus redundant separators, .., dll).
    
    Args:
        path: Path untuk dinormalisasi
        
    Returns:
        Path: Normalized path
    """
    return Path(path).bersihkan()


def split_path(path):
    """
    Bagi path menjadi head dan tail.
    
    Args:
        path: Path untuk dibagi
        
    Returns:
        tuple: (head, tail)
    """
    p = Path(path)
    return (str(p.dapatkan_parent()), str(p.dapatkan_nama()))


def split_ext(path):
    """
    Bagi path menjadi root dan extension.
    
    Args:
        path: Path untuk dibagi
        
    Returns:
        tuple: (root, ext)
    """
    p = Path(path)
    return (str(p.dapatkan_stem()), str(p.dapatkan_extension()))


def get_extension(path):
    """
    Dapatkan file extension dari path.
    
    Args:
        path: Path string
        
    Returns:
        str: Extension (tanpa dot)
    """
    return Path(path).dapatkan_extension()


def get_filename(path):
    """
    Dapatkan filename dari path.
    
    Args:
        path: Path string
        
    Returns:
        str: Filename
    """
    return Path(path).dapatkan_nama()


def get_basename(path):
    """
    Dapatkan basename (filename tanpa extension) dari path.
    
    Args:
        path: Path string
        
    Returns:
        str: Basename
    """
    return Path(path).dapatkan_stem()


def get_directory(path):
    """
    Dapatkan directory dari path.
    
    Args:
        path: Path string
        
    Returns:
        str: Directory path
    """
    return str(Path(path).dapatkan_parent())


# Extend Path class with class methods
@classmethod
def cwd(cls):
    return path_current()

@classmethod  
def home(cls):
    return path_home()

Path.cwd = cwd
Path.home = home


# Daftar semua fungsi yang tersedia
__all__ = [
    'Path',
    'path_current',
    'path_home', 
    'path_temp',
    'gabung_path',
    'path_absolute',
    'path_relatif',
    'expand_user',
    'expand_vars',
    'path_normal',
    'split_path',
    'split_ext',
    'get_extension',
    'get_filename',
    'get_basename',
    'get_directory'
]