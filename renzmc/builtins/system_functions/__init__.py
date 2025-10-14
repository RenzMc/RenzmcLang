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

import datetime
import os
import shlex
import subprocess
import time
import uuid

try:
    from renzmc.core.error import RenzmcError
except ImportError:

    class RenzmcError(Exception):
        pass


class SecurityError(RenzmcError):

    def __init__(self, message, line=None, column=None):
        super().__init__(message, line, column)
        self.message = message


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


_sandbox_enabled = False
_safe_commands = {
    "ls",
    "cat",
    "echo",
    "pwd",
    "date",
    "whoami",
    "uname",
    "grep",
    "find",
    "wc",
    "head",
    "tail",
    "sort",
    "uniq",
}


def validate_executable_path(path):
    if not os.path.isabs(path):
        return False
    if not os.path.exists(path):
        return False
    if not os.access(path, os.X_OK):
        return False
    return True


def validate_command_safety(command):
    if _sandbox_enabled:
        parts = shlex.split(command)
        if not parts:
            return False
        cmd = parts[0]
        if cmd not in _safe_commands:
            raise SecurityError(
                f"Perintah '{cmd}' tidak diizinkan dalam mode sandbox. "
                f"Perintah yang diizinkan: {', '.join(sorted(_safe_commands))}"
            )
    return True


def jalankan_perintah(command, shell=True, capture_output=True):
    try:
        validate_command_safety(command)
        result = subprocess.run(command, shell=shell, capture_output=capture_output, text=True, timeout=30)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        raise TimeoutError("Perintah melebihi batas waktu 30 detik")
    except Exception as e:
        raise Exception(f"Error menjalankan perintah: {e}")


def atur_sandbox(enabled=True):
    global _sandbox_enabled
    _sandbox_enabled = enabled
    return _sandbox_enabled


def tambah_perintah_aman(command):
    if not isinstance(command, str):
        raise TypeError("Perintah harus berupa string")
    _safe_commands.add(command)
    return True


def hapus_perintah_aman(command):
    if command in _safe_commands:
        _safe_commands.remove(command)
        return True
    return False


def waktu():
    return time.time()


def tidur(seconds):
    time.sleep(seconds)


def tanggal():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def buat_uuid():
    return str(uuid.uuid4())
