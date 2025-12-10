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
RenzMcLang OS Library

Module ini menyediakan interface untuk fungsi-fungsi sistem operasi,
mengikuti standar Python os module dengan nama fungsi dalam Bahasa Indonesia.

Functions:
- Environment: getenv, setenv, unsetenv, environ
- Process: getpid, getppid, system, exec, spawn
- Path: getcwd, chdir, listdir, mkdir, rmdir, remove, rename
- File: stat, chmod, access, exists
- System: uname, platform, architecture

Usage:
    dari os impor getcwd, chdir, listdir
    
    dir_sekarang = getcwd()
    list_file = listdir('.')
"""

import sys
import os as py_os
from typing import List, Dict, Any, Optional, Union
import platform as py_platform

# Environment Variables


def getenv(key: str, default: str = None) -> Optional[str]:
    """
    Dapatkan nilai environment variable.

    Args:
        key: Nama environment variable
        default: Default value jika tidak ada

    Returns:
        Nilai environment variable atau default

    Example:
        path = getenv('PATH', '')
    """
    return py_os.getenv(key, default)


def setenv(key: str, value: str):
    """
    Set environment variable.

    Args:
        key: Nama environment variable
        value: Nilai yang akan diset

    Example:
        setenv('MY_VAR', 'hello')
    """
    py_os.environ[key] = value


def unsetenv(key: str):
    """
    Hapus environment variable.

    Args:
        key: Nama environment variable yang akan dihapus

    Example:
        unsetenv('MY_VAR')
    """
    if key in py_os.environ:
        del py_os.environ[key]


def environ() -> Dict[str, str]:
    """
    Dapatkan semua environment variables.

    Returns:
        Dictionary berisi semua environment variables
    """
    return dict(py_os.environ)

# Process Functions


def getpid() -> int:
    """
    Dapatkan process ID dari process saat ini.

    Returns:
        Process ID
    """
    return py_os.getpid()


def getppid() -> int:
    """
    Dapatkan parent process ID.

    Returns:
        Parent Process ID
    """
    return py_os.getppid()


def system(command: str) -> int:
    """
    Jalankan command di system shell.

    Args:
        command: Command yang akan dijalankan

    Returns:
        Exit code dari command

    Example:
        exit_code = system('ls -la')
    """
    return py_os.system(command)

# Path Functions


def getcwd() -> str:
    """
    Dapatkan current working directory.

    Returns:
        Path dari current working directory

    Example:
        cwd = getcwd()
    """
    return py_os.getcwd()


def chdir(path: str):
    """
    Ubah current working directory.

    Args:
        path: Path directory baru

    Example:
        chdir('/home/user')
    """
    py_os.chdir(path)


def listdir(path: str = '.') -> List[str]:
    """
    Daftar file dan directory dalam path.

    Args:
        path: Path yang akan di-list (default: current directory)

    Returns:
        List nama file dan directory

    Example:
        files = listdir('/home/user')
    """
    return py_os.listdir(path)


def mkdir(path: str, mode: int = 0o777):
    """
    Buat directory baru.

    Args:
        path: Path directory yang akan dibuat
        mode: Permission mode (default: 0o777)

    Example:
        mkdir('/home/user/new_dir')
    """
    py_os.mkdir(path, mode)


def makedirs(path: str, mode: int = 0o777, exist_ok: bool = False):
    """
    Buat directory beserta parent directories.

    Args:
        path: Path yang akan dibuat
        mode: Permission mode
        exist_ok: Tidak error jika directory sudah ada

    Example:
        makedirs('/home/user/a/b/c', exist_ok=True)
    """
    py_os.makedirs(path, mode=mode, exist_ok=exist_ok)


def rmdir(path: str):
    """
    Hapus directory (harus kosong).

    Args:
        path: Path directory yang akan dihapus

    Example:
        rmdir('/home/user/empty_dir')
    """
    py_os.rmdir(path)


def removedirs(path: str):
    """
    Hapus directory beserta parent directories yang kosong.

    Args:
        path: Path yang akan dihapus

    Example:
        removedirs('/home/user/a/b/c')
    """
    py_os.removedirs(path)


def remove(path: str):
    """
    Hapus file.

    Args:
        path: Path file yang akan dihapus

    Example:
        remove('/home/user/file.txt')
    """
    py_os.remove(path)


def rename(src: str, dst: str):
    """
    Rename file atau directory.

    Args:
        src: Path lama
        dst: Path baru

    Example:
        rename('/home/user/old.txt', '/home/user/new.txt')
    """
    py_os.rename(src, dst)

# File Functions


def exists(path: str) -> bool:
    """
    Cek apakah file atau directory ada.

    Args:
        path: Path yang akan dicek

    Returns:
        True jika ada, False jika tidak

    Example:
        if exists('/home/user/file.txt'):
            print('File ada')
    """
    return py_os.path.exists(path)


def isfile(path: str) -> bool:
    """
    Cek apakah path adalah file.

    Args:
        path: Path yang akan dicek

    Returns:
        True jika file, False jika tidak
    """
    return py_os.path.isfile(path)


def isdir(path: str) -> bool:
    """
    Cek apakah path adalah directory.

    Args:
        path: Path yang akan dicek

    Returns:
        True jika directory, False jika tidak
    """
    return py_os.path.isdir(path)


def islink(path: str) -> bool:
    """
    Cek apakah path adalah symbolic link.

    Args:
        path: Path yang akan dicek

    Returns:
        True jika symbolic link, False jika tidak
    """
    return py_os.path.islink(path)


def access(path: str, mode: int) -> bool:
    """
    Cek akses ke file/directory.

    Args:
        path: Path yang akan dicek
        mode: Mode akses (os.F_OK, os.R_OK, os.W_OK, os.X_OK)

    Returns:
        True jika bisa diakses, False jika tidak

    Example:
        if access('/home/user/file.txt', R_OK):
            print('File bisa dibaca')
    """
    return py_os.access(path, mode)


def stat(path: str) -> py_os.stat_result:
    """
    Dapatkan file/directory status.

    Args:
        path: Path yang akan dicek

    Returns:
        Stat result object

    Example:
        info = stat('/home/user/file.txt')
        size = info.st_size
    """
    return py_os.stat(path)


def chmod(path: str, mode: int):
    """
    Ubah file/directory mode.

    Args:
        path: Path yang akan diubah
        mode: Permission mode

    Example:
        chmod('/home/user/script.sh', 0o755)
    """
    py_os.chmod(path, mode)

# System Information


def uname() -> py_os.uname_result:
    """
    Dapatkan system information.

    Returns:
        System information object

    Example:
        info = uname()
        print(f"System: {info.sysname}")
        print(f"Node: {info.nodename}")
        print(f"Release: {info.release}")
        print(f"Version: {info.version}")
        print(f"Machine: {info.machine}")
    """
    return py_os.uname()


def platform() -> str:
    """
    Dapatkan platform information.

    Returns:
        Platform string

    Example:
        plat = platform()  # 'Linux', 'Windows', 'Darwin'
    """
    return sys.platform


def architecture() -> str:
    """
    Dapatkan system architecture.

    Returns:
        Architecture string

    Example:
        arch = architecture()  # 'x86_64', 'AMD64', dll
    """
    return py_platform.machine()

# Utility Functions


def join(*paths) -> str:
    """
    Gabungkan path components.

    Args:
        *paths: Path components yang akan digabungkan

    Returns:
        Joined path

    Example:
        path = join('/home', 'user', 'documents', 'file.txt')
    """
    return py_os.path.join(*paths)


def split(path: str) -> tuple:
    """
    Pisah path menjadi (head, tail).

    Args:
        path: Path yang akan dipisah

    Returns:
        Tuple (head, tail)

    Example:
        head, tail = split('/home/user/file.txt')
        # head = '/home/user', tail = 'file.txt'
    """
    return py_os.path.split(path)


def basename(path: str) -> str:
    """
    Dapatkan basename dari path.

    Args:
        path: Path input

    Returns:
        Basename

    Example:
        name = basename('/home/user/file.txt')  # 'file.txt'
    """
    return py_os.path.basename(path)


def dirname(path: str) -> str:
    """
    Dapatkan dirname dari path.

    Args:
        path: Path input

    Returns:
        Directory name

    Example:
        dir = dirname('/home/user/file.txt')  # '/home/user'
    """
    return py_os.path.dirname(path)


def abspath(path: str) -> str:
    """
    Dapatkan absolute path.

    Args:
        path: Path input

    Returns:
        Absolute path

    Example:
        abs_path = abspath('file.txt')
    """
    return py_os.path.abspath(path)


# Constants
F_OK = py_os.F_OK  # Test existence
R_OK = py_os.R_OK  # Test read permission
W_OK = py_os.W_OK  # Test write permission
X_OK = py_os.X_OK  # Test execute permission

# Environment Variables Object
environ_obj = py_os.environ

# Indonesian Aliases
dapatkan_env = getenv
atur_env = setenv
hapus_env = unsetenv
lingkungan = environ
id_proses = getpid
id_proses_orang_tua = getppid
jalankan_sistem = system
dapatkan_dir_sekarang = getcwd
ubah_dir = chdir
daftar_dir = listdir
buat_dir = mkdir
buat_dir_banyak = makedirs
hapus_dir = rmdir
hapus_dir_banyak = removedirs
hapus_file = remove
ganti_nama = rename
ada = exists
adalah_file = isfile
adalah_dir = isdir
adalah_link = islink
akses = access
info_file = stat
ubah_mode = chmod
info_sistem = uname
platform_sistem = platform
arsitektur = architecture
gabung_path = join
pisah_path = split
nama_file = basename
nama_dir = dirname
path_absolut = abspath

__all__ = [
    # Environment
    "getenv", "setenv", "unsetenv", "environ", "environ_obj",
    # Process
    "getpid", "getppid", "system",
    # Path
    "getcwd", "chdir", "listdir", "mkdir", "makedirs", "rmdir", "removedirs",
    "remove", "rename",
    # File
    "exists", "isfile", "isdir", "islink", "access", "stat", "chmod",
    # System
    "uname", "platform", "architecture",
    # Utility
    "join", "split", "basename", "dirname", "abspath",
    # Constants
    "F_OK", "R_OK", "W_OK", "X_OK",
    # Indonesian Aliases
    "dapatkan_env", "atur_env", "hapus_env", "lingkungan", "id_proses",
    "id_proses_orang_tua", "jalankan_sistem", "dapatkan_dir_sekarang",
    "ubah_dir", "daftar_dir", "buat_dir", "buat_dir_banyak", "hapus_dir",
    "hapus_dir_banyak", "hapus_file", "ganti_nama", "ada", "adalah_file",
    "adalah_dir", "adalah_link", "akses", "info_file", "ubah_mode",
    "info_sistem", "platform_sistem", "arsitektur", "gabung_path",
    "pisah_path", "nama_file", "nama_dir", "path_absolut"
]
