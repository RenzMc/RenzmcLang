import math
import random
import time
import datetime
import os
import subprocess
import json
import re
import base64
import hashlib
import uuid
import urllib.parse
import urllib.request
import sys
import inspect
import asyncio
import shlex
from typing import Any, List, Dict, Set, Tuple, Optional, Union, Callable
import shutil
from pathlib import Path
import statistics

try:
    from renzmc.core.error import RenzmcError
except ImportError:

    class RenzmcError(Exception):
        pass


class SecurityError(RenzmcError):

    def __init__(self, message, line=None, column=None):
        super().__init__(message, line, column)
        self.message = message


def panjang(obj):
    try:
        return len(obj)
    except TypeError:
        raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak memiliki panjang")


def jenis(obj):
    return type(obj).__name__


def ke_teks(obj):
    return str(obj)


def ke_angka(obj):
    try:
        return int(obj)
    except ValueError:
        try:
            return float(obj)
        except ValueError:
            raise ValueError(f"Tidak dapat mengkonversi '{obj}' ke angka")


def huruf_besar(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.upper()


def huruf_kecil(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.lower()


def potong(text, start, end=None):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    try:
        if end is None:
            return text[start:]
        else:
            return text[start:end]
    except IndexError:
        raise IndexError(f"Indeks di luar jangkauan untuk teks '{text}'")


def gabung(separator, *items):
    if not isinstance(separator, str):
        raise TypeError(
            f"Pemisah harus berupa teks, bukan '{type(separator).__name__}'"
        )
    return separator.join((str(item) for item in items))


def pisah(text, separator=None):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    return text.split(separator)


def ganti(text, old, new):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    if not isinstance(old, str):
        raise TypeError(
            f"Argumen kedua harus berupa teks, bukan '{type(old).__name__}'"
        )
    if not isinstance(new, str):
        raise TypeError(
            f"Argumen ketiga harus berupa teks, bukan '{type(new).__name__}'"
        )
    return text.replace(old, new)


def mulai_dengan(text, prefix):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    if not isinstance(prefix, str):
        raise TypeError(
            f"Argumen kedua harus berupa teks, bukan '{type(prefix).__name__}'"
        )
    return text.startswith(prefix)


def akhir_dengan(text, suffix):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    if not isinstance(suffix, str):
        raise TypeError(
            f"Argumen kedua harus berupa teks, bukan '{type(suffix).__name__}'"
        )
    return text.endswith(suffix)


def berisi(text, substring):
    if not isinstance(text, str):
        raise TypeError(
            f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'"
        )
    if not isinstance(substring, str):
        raise TypeError(
            f"Argumen kedua harus berupa teks, bukan '{type(substring).__name__}'"
        )
    return substring in text


def hapus_spasi(text):
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.strip()


def bulat(number):
    try:
        return int(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke bilangan bulat")


def desimal(number):
    try:
        return float(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke bilangan desimal")


def akar(number):
    if number < 0:
        raise ValueError("Tidak dapat menghitung akar kuadrat dari bilangan negatif")
    return math.sqrt(number)


def pangkat(base, exponent):
    return base**exponent


def absolut(number):
    return abs(number)


def pembulatan(number):
    return round(number)


def pembulatan_atas(number):
    return math.ceil(number)


def pembulatan_bawah(number):
    return math.floor(number)


def sinus(angle):
    return math.sin(angle)


def cosinus(angle):
    return math.cos(angle)


def tangen(angle):
    return math.tan(angle)


def tambah(lst, item):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    lst.append(item)
    return lst


def hapus(lst, item):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    try:
        lst.remove(item)
        return lst
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam daftar")


def hapus_pada(lst, index):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    try:
        del lst[index]
        return lst
    except IndexError:
        raise IndexError(
            f"Indeks {index} di luar jangkauan untuk daftar dengan panjang {len(lst)}"
        )


def masukkan(lst, index, item):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    try:
        lst.insert(index, item)
        return lst
    except IndexError:
        raise IndexError(
            f"Indeks {index} di luar jangkauan untuk daftar dengan panjang {len(lst)}"
        )


def urutkan(lst, terbalik=False):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )

    terbalik = _convert_to_bool(terbalik)

    try:
        lst.sort(reverse=terbalik)
        return None
    except TypeError:
        raise TypeError("Tidak dapat mengurutkan daftar dengan tipe item yang berbeda")


def balikkan(lst):
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa daftar, bukan '{type(lst).__name__}'")
    lst.reverse()
    return None


def hitung(lst, item):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    return lst.count(item)


def indeks(lst, item):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    try:
        return lst.index(item)
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam daftar")


def extend(lst, iterable):
    if not isinstance(lst, list):
        raise TypeError(
            f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'"
        )
    lst.extend(iterable)
    return lst


def salin(obj):
    import copy

    return copy.copy(obj)


def salin_dalam(obj):
    import copy

    return copy.deepcopy(obj)


def minimum(*args):
    if len(args) == 0:
        raise ValueError("minimum() memerlukan setidaknya satu argumen")
    if (
        len(args) == 1
        and hasattr(args[0], "__iter__")
        and (not isinstance(args[0], str))
    ):
        return min(args[0])
    else:
        return min(args)


def maksimum(*args):
    if len(args) == 0:
        raise ValueError("maksimum() memerlukan setidaknya satu argumen")
    if (
        len(args) == 1
        and hasattr(args[0], "__iter__")
        and (not isinstance(args[0], str))
    ):
        return max(args[0])
    else:
        return max(args)


def jumlah(*args):
    if len(args) == 0:
        return 0
    if (
        len(args) == 1
        and hasattr(args[0], "__iter__")
        and (not isinstance(args[0], str))
    ):
        return sum(args[0])
    else:
        return sum(args)


def rata_rata(*args):
    if len(args) == 0:
        raise ValueError("rata_rata() memerlukan setidaknya satu argumen")
    if (
        len(args) == 1
        and hasattr(args[0], "__iter__")
        and (not isinstance(args[0], str))
    ):
        items = list(args[0])
        return sum(items) / len(items) if len(items) > 0 else 0
    else:
        return sum(args) / len(args)


def kunci(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError(
            f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'"
        )
    return list(dictionary.keys())


def nilai(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError(
            f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'"
        )
    return list(dictionary.values())


def item(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError(
            f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'"
        )
    return list(dictionary.items())


def hapus_kunci(dictionary, key):
    if not isinstance(dictionary, dict):
        raise TypeError(
            f"Argumen pertama harus berupa kamus, bukan '{type(dictionary).__name__}'"
        )
    try:
        del dictionary[key]
        return dictionary
    except KeyError:
        raise KeyError(f"Kunci '{key}' tidak ditemukan dalam kamus")


def acak(min_val=0, max_val=1):
    if isinstance(min_val, int) and isinstance(max_val, int):
        return random.randint(min_val, max_val)
    else:
        return random.uniform(min_val, max_val)


def waktu():
    return time.time()


def tidur(seconds):
    time.sleep(seconds)


def tanggal():
    return datetime.datetime.now()


def baca_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except IOError as e:
        raise IOError(f"Error membaca file '{filename}': {str(e)}")


def tulis_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error menulis ke file '{filename}': {str(e)}")


def tambah_file(filename, content):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error menambahkan ke file '{filename}': {str(e)}")


def hapus_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except IOError as e:
        raise IOError(f"Error menghapus file '{filename}': {str(e)}")


SANDBOX_MODE = True
ALLOWED_COMMANDS = {
    "echo",
    "ls",
    "pwd",
    "cat",
    "head",
    "tail",
    "wc",
    "date",
    "whoami",
    "which",
    "sort",
    "uniq",
    "cut",
    "grep",
}
COMPOUND_COMMANDS = {
    "git status": [],
    "git log": ["--oneline", "--graph", "--decorate"],
    "git show": ["--stat", "--name-only"],
    "git diff": ["--stat", "--name-only"],
    "git branch": ["-r", "--list"],
    "pip list": [],
    "pip show": [],
}
ALLOWED_PATHS = {"/bin", "/usr/bin", "/usr/local/bin"}
MAX_OUTPUT_SIZE = 1024 * 1024
MAX_COMMAND_TIMEOUT = 10
DANGEROUS_PATTERNS = [
    "[;&|`$()]",
    "[<>]",
    "\\$\\(",
    "`",
    "\\b(rm|del|format|fdisk|mkfs|dd|sudo|su|chmod\\s+777|chown\\s+root)\\b",
]


def validate_executable_path(cmd_path):
    if not cmd_path:
        return False
    real_path = shutil.which(cmd_path)
    if not real_path:
        return False
    try:
        resolved_path = Path(real_path).resolve()
        real_dir = str(resolved_path.parent)
        for allowed_dir in ALLOWED_PATHS:
            try:
                Path(allowed_dir).resolve()
                common_path = os.path.commonpath([real_dir, allowed_dir])
                if common_path == allowed_dir:
                    return True
            except (ValueError, OSError):
                continue
        return False
    except (OSError, RuntimeError):
        return False


def validate_command_safety(command, use_sandbox=None):
    if not isinstance(command, str):
        return (False, "Perintah harus berupa teks")
    command = command.strip()
    if not command:
        return (False, "Perintah tidak boleh kosong")
    sandbox_enabled = SANDBOX_MODE if use_sandbox is None else use_sandbox
    try:
        cmd_tokens = shlex.split(command)
    except ValueError as e:
        return (False, f"Format perintah tidak valid: {str(e)}")
    if not cmd_tokens:
        return (False, "Perintah kosong setelah parsing")
    base_command = cmd_tokens[0].lower()
    if os.path.isabs(cmd_tokens[0]):
        if sandbox_enabled:
            return (False, "Path absolut tidak diizinkan dalam mode sandbox")
    if sandbox_enabled:
        if base_command in ALLOWED_COMMANDS:
            if not validate_executable_path(base_command):
                return (
                    False,
                    f"Perintah '{base_command}' tidak ditemukan di direktori aman",
                )
            for token in cmd_tokens[1:]:
                if re.search("[;&|`$<>()]", token):
                    return (False, f"Argumen '{token}' mengandung karakter berbahaya")
                if os.path.isabs(token):
                    return (
                        False,
                        f"Path absolut '{token}' tidak diizinkan dalam argumen",
                    )
            return (True, "Perintah aman")
        for compound_cmd, allowed_flags in COMPOUND_COMMANDS.items():
            if command.lower().startswith(compound_cmd.lower()):
                compound_base = compound_cmd.split()[0]
                if not validate_executable_path(compound_base):
                    return (
                        False,
                        f"Perintah compound '{compound_base}' tidak ditemukan di direktori aman",
                    )
                remaining_args = cmd_tokens[len(compound_cmd.split()) :]
                for arg in remaining_args:
                    if allowed_flags and arg not in allowed_flags:
                        return (
                            False,
                            f"Argumen '{arg}' tidak diizinkan untuk perintah '{compound_cmd}'",
                        )
                    if re.search("[;&|`$<>()]", arg):
                        return (False, f"Argumen '{arg}' mengandung karakter berbahaya")
                    if os.path.isabs(arg) and (not arg.startswith(("-", "--"))):
                        return (
                            False,
                            f"Path absolut '{arg}' tidak diizinkan dalam argumen",
                        )
                return (True, "Perintah compound aman")
        return (
            False,
            f"Perintah '{base_command}' tidak diizinkan dalam mode sandbox. Perintah yang diizinkan: {sorted(list(ALLOWED_COMMANDS))}",
        )
    return (True, "Sandbox dinonaktifkan - perintah diizinkan")


def jalankan_perintah(command, sandbox=None, working_dir=None, timeout=None):
    use_sandbox = SANDBOX_MODE if sandbox is None else sandbox
    command_timeout = timeout if timeout is not None else MAX_COMMAND_TIMEOUT
    if use_sandbox:
        is_safe, reason = validate_command_safety(command, use_sandbox)
        if not is_safe:
            raise SecurityError(f"Keamanan: {reason}")
    if working_dir is not None:
        if not os.path.isdir(working_dir):
            raise SecurityError(f"Direktori kerja '{working_dir}' tidak valid")
        try:
            real_path = os.path.realpath(working_dir)
            if not real_path.startswith(os.getcwd()):
                raise SecurityError(
                    f"Direktori kerja '{working_dir}' berada di luar direktori yang diizinkan"
                )
        except (OSError, RuntimeError):
            raise SecurityError(
                f"Tidak dapat memvalidasi direktori kerja '{working_dir}'"
            )
    else:
        working_dir = os.getcwd()
    cmd_args = []
    process = None
    try:
        cmd_args = shlex.split(command)
        if not cmd_args:
            raise SecurityError("Perintah kosong")
        command_str = " ".join(cmd_args).lower()
        suspicious_patterns = [
            "(^|\\s)(wget|curl)(\\s|$)",
            "(^|\\s)(nc|netcat|ncat)(\\s|$)",
            "(^|\\s)(telnet|ssh|ftp)(\\s|$)",
            "(^|\\s)(chmod\\s+[0-7]*7[0-7]*|chmod\\s+.*\\+x)(\\s|$)",
            "(^|\\s)(eval|exec)(\\s|$)",
            "(^|\\s)(base64\\s+-d)(\\s|$)",
            "(^|\\s)(mkfifo|mknod)(\\s|$)",
        ]
        for pattern in suspicious_patterns:
            if re.search(pattern, command_str):
                raise SecurityError(f"Perintah mencurigakan terdeteksi: '{command}'")
        safe_env = {
            "PATH": "/usr/local/bin:/usr/bin:/bin",
            "HOME": os.environ.get("HOME", ""),
            "USER": os.environ.get("USER", ""),
            "PWD": working_dir,
            "LANG": os.environ.get("LANG", "en_US.UTF-8"),
            "LC_ALL": os.environ.get("LC_ALL", "en_US.UTF-8"),
            "TMPDIR": "/tmp",
            "TZ": "UTC",
        }
        for dangerous_var in [
            "LD_PRELOAD",
            "LD_LIBRARY_PATH",
            "PYTHONPATH",
            "PERL5LIB",
        ]:
            if dangerous_var in safe_env:
                del safe_env[dangerous_var]

        def set_limits():
            import resource

            resource.setrlimit(
                resource.RLIMIT_CPU, (command_timeout, command_timeout + 1)
            )
            resource.setrlimit(
                resource.RLIMIT_FSIZE, (10 * 1024 * 1024, 10 * 1024 * 1024)
            )
            try:
                resource.setrlimit(resource.RLIMIT_NPROC, (10, 10))
            except (ValueError, AttributeError):
                pass
            try:
                resource.setrlimit(
                    resource.RLIMIT_AS, (500 * 1024 * 1024, 500 * 1024 * 1024)
                )
            except (ValueError, AttributeError):
                pass

        process = subprocess.Popen(
            cmd_args,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
            universal_newlines=True,
            cwd=working_dir,
            env=safe_env,
            close_fds=True,
            start_new_session=True,
            preexec_fn=set_limits if os.name != "nt" else None,
        )
        try:
            stdout, stderr = process.communicate(timeout=command_timeout)
            if len(stdout) > MAX_OUTPUT_SIZE:
                stdout = (
                    stdout[:MAX_OUTPUT_SIZE]
                    + "\n[OUTPUT TRUNCATED - EXCEEDED SIZE LIMIT]"
                )
            if len(stderr) > MAX_OUTPUT_SIZE:
                stderr = (
                    stderr[:MAX_OUTPUT_SIZE]
                    + "\n[ERROR TRUNCATED - EXCEEDED SIZE LIMIT]"
                )
            sensitive_patterns = [
                "password\\s*=\\s*[\\'\"][^\\'\"]+[\\'\"]",
                "api[_-]?key\\s*=\\s*[\\'\"][^\\'\"]+[\\'\"]",
                "secret\\s*=\\s*[\\'\"][^\\'\"]+[\\'\"]",
                "token\\s*=\\s*[\\'\"][^\\'\"]+[\\'\"]",
            ]
            for pattern in sensitive_patterns:
                stdout = re.sub(pattern, "\\1=*****", stdout, flags=re.IGNORECASE)
                stderr = re.sub(pattern, "\\1=*****", stderr, flags=re.IGNORECASE)
            return (process.returncode, stdout, stderr)
        except subprocess.TimeoutExpired:
            try:
                import signal

                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                process.wait(timeout=2)
            except (ProcessLookupError, PermissionError, subprocess.TimeoutExpired):
                process.kill()
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    pass
            try:
                import psutil

                parent = psutil.Process(process.pid)
                for child in parent.children(recursive=True):
                    child.kill()
            except (ImportError, psutil.NoSuchProcess, psutil.AccessDenied):
                pass
            raise SecurityError(
                f"Perintah '{command}' melebihi batas waktu ({command_timeout} detik)"
            )
    except SecurityError:
        raise
    except FileNotFoundError:
        cmd_name = cmd_args[0] if cmd_args else "unknown"
        raise SecurityError(
            f"Perintah '{cmd_name}' tidak ditemukan atau tidak diizinkan"
        )
    except PermissionError:
        cmd_name = cmd_args[0] if cmd_args else "unknown"
        raise SecurityError(f"Tidak ada izin untuk menjalankan perintah '{cmd_name}'")
    except subprocess.SubprocessError as e:
        raise SecurityError(f"Error menjalankan perintah '{command}': {str(e)}")
    except Exception as e:
        raise SecurityError(
            f"Error tidak terduga saat menjalankan perintah '{command}': {str(e)}"
        )


def atur_sandbox(enabled):
    global SANDBOX_MODE
    SANDBOX_MODE = enabled
    return f"Mode sandbox {('diaktifkan' if enabled else 'dinonaktifkan')}"


def tambah_perintah_aman(command):
    if isinstance(command, str) and command.strip():
        ALLOWED_COMMANDS.add(command.strip().lower())
        return f"Perintah '{command}' ditambahkan ke daftar aman"
    else:
        raise ValueError("Perintah harus berupa teks yang tidak kosong")


def hapus_perintah_aman(command):
    if isinstance(command, str) and command.strip():
        cmd = command.strip().lower()
        if cmd in ALLOWED_COMMANDS:
            ALLOWED_COMMANDS.remove(cmd)
            return f"Perintah '{command}' dihapus dari daftar aman"
        else:
            return f"Perintah '{command}' tidak ada dalam daftar aman"
    else:
        raise ValueError("Perintah harus berupa teks yang tidak kosong")


def format_teks(template, **kwargs):
    return template.format(**kwargs)


def gabung_path(*paths):
    return os.path.join(*paths)


def file_exists(path):
    return os.path.exists(path)


def buat_direktori(path):
    os.makedirs(path, exist_ok=True)


def daftar_direktori(path="."):
    return os.listdir(path)


def json_ke_teks(obj):
    return json.dumps(obj, ensure_ascii=False)


def teks_ke_json(text):
    return json.loads(text)


def hash_teks(text, algorithm="sha256"):
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


def buat_uuid():
    return str(uuid.uuid4())


def url_encode(text):
    return urllib.parse.quote(text)


def url_decode(text):
    return urllib.parse.unquote(text)

def regex_match(pattern, text):
    return re.findall(pattern, text)


def regex_replace(pattern, replacement, text):
    return re.sub(pattern, replacement, text)


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(text):
    return base64.b64decode(text.encode()).decode()


def is_async_function(func):
    return asyncio.iscoroutinefunction(func)


def run_async(coro):
    return asyncio.run(coro)


def wait_all_async(coros):

    async def gather_coros():
        return await asyncio.gather(*coros)

    return asyncio.run(gather_coros())


def create_async_function(func):

    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def get_function_signature(func):
    return str(inspect.signature(func))


def get_function_parameters(func):
    return list(inspect.signature(func).parameters.keys())


def get_function_defaults(func):
    signature = inspect.signature(func)
    return {
        name: param.default
        for name, param in signature.parameters.items()
        if param.default is not inspect.Parameter.empty
    }


def get_function_annotations(func):
    return func.__annotations__


def get_function_doc(func):
    return func.__doc__


def get_function_source(func):
    return inspect.getsource(func)


def get_function_module(func):
    return func.__module__


def get_function_name(func):
    return func.__name__


def get_function_qualname(func):
    return func.__qualname__


def get_function_globals(func):
    return func.__globals__


def get_function_closure(func):
    return func.__closure__


def get_function_code(func):
    return func.__code__


def super_impl(*args, **kwargs):

    class SuperProxy:

        def __call__(self, *args, **kwargs):
            return None

        def __getattr__(self, name):

            def method_proxy(*method_args, **method_kwargs):
                return f"super().{name}() called"

            return method_proxy

    return SuperProxy()


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


super = RenzmcBuiltinFunction(super_impl, "super")


def impor_semua_python(module_name):
    pass

def reload_python(module_name):
    pass

def daftar_modul_python():
    pass

def jalankan_python(code_string):
    pass

_builtin_zip = zip
_builtin_enumerate = enumerate
_builtin_filter = filter
_builtin_map = map
_builtin_all = all
_builtin_any = any
_builtin_sorted = sorted


def zip_impl(*iterables):
    return list(_builtin_zip(*iterables))


zip = RenzmcBuiltinFunction(zip_impl, "zip")


def enumerate_impl(iterable, start=0):
    return list(_builtin_enumerate(iterable, start))


enumerate = RenzmcBuiltinFunction(enumerate_impl, "enumerate")


def filter_impl(function, iterable):
    return list(_builtin_filter(function, iterable))


filter = RenzmcBuiltinFunction(filter_impl, "filter")
saring = filter


def map_impl(function, *iterables):
    return list(_builtin_map(function, *iterables))


map = RenzmcBuiltinFunction(map_impl, "map")
peta = map


def reduce_impl(function, iterable, initial=None):
    from functools import reduce as _builtin_reduce

    if initial is None:
        return _builtin_reduce(function, iterable)
    else:
        return _builtin_reduce(function, iterable, initial)


reduce = RenzmcBuiltinFunction(reduce_impl, "reduce")
kurangi = reduce


def all_impl(iterable):
    return _builtin_all(iterable)


all = RenzmcBuiltinFunction(all_impl, "all")
semua = all


def any_impl(iterable):
    return _builtin_any(iterable)


any = RenzmcBuiltinFunction(any_impl, "any")
ada = any


def sorted_impl(iterable, key=None, reverse=False):
    reverse = _convert_to_bool(reverse)

    if key is None:
        return _builtin_sorted(iterable, reverse=reverse)
    else:
        if hasattr(key, '__call__'):
            def key_wrapper(item):
                try:
                    result = key(item)
                    return result
                except Exception:
                    import traceback
                    traceback.print_exc()
                    raise
            return _builtin_sorted(iterable, key=key_wrapper, reverse=reverse)
        else:
            return _builtin_sorted(iterable, key=key, reverse=reverse)


sorted = RenzmcBuiltinFunction(sorted_impl, "sorted")
terurut = sorted


def is_alpha_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isalpha()


is_alpha = RenzmcBuiltinFunction(is_alpha_impl, "is_alpha")
adalah_huruf = is_alpha


def is_digit_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isdigit()


is_digit = RenzmcBuiltinFunction(is_digit_impl, "is_digit")
adalah_angka = is_digit


def is_alnum_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isalnum()


is_alnum = RenzmcBuiltinFunction(is_alnum_impl, "is_alnum")
adalah_alfanumerik = is_alnum


def is_lower_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.islower()


is_lower = RenzmcBuiltinFunction(is_lower_impl, "is_lower")
adalah_huruf_kecil = is_lower


def is_upper_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isupper()


is_upper = RenzmcBuiltinFunction(is_upper_impl, "is_upper")
adalah_huruf_besar = is_upper


def is_space_impl(text):
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isspace()


is_space = RenzmcBuiltinFunction(is_space_impl, "is_space")
adalah_spasi = is_space

def direktori_ada_impl(path):
    return os.path.isdir(path)


direktori_ada = RenzmcBuiltinFunction(direktori_ada_impl, "direktori_ada")


def direktori_sekarang_impl():
    return os.getcwd()


direktori_sekarang = RenzmcBuiltinFunction(
    direktori_sekarang_impl, "direktori_sekarang"
)


def ubah_direktori_impl(path):
    os.chdir(path)
    return None


ubah_direktori = RenzmcBuiltinFunction(ubah_direktori_impl, "ubah_direktori")


def pisah_path_impl(path):
    return os.path.split(path)


pisah_path = RenzmcBuiltinFunction(pisah_path_impl, "pisah_path")


def ekstensi_file_impl(path):
    return os.path.splitext(path)[1]


ekstensi_file = RenzmcBuiltinFunction(ekstensi_file_impl, "ekstensi_file")


def nama_file_tanpa_ekstensi_impl(path):
    return os.path.splitext(os.path.basename(path))[0]


nama_file_tanpa_ekstensi = RenzmcBuiltinFunction(
    nama_file_tanpa_ekstensi_impl, "nama_file_tanpa_ekstensi"
)


def path_ada_impl(path):
    return os.path.exists(path)


path_ada = RenzmcBuiltinFunction(path_ada_impl, "path_ada")


def adalah_file_impl(path):
    return os.path.isfile(path)


adalah_file = RenzmcBuiltinFunction(adalah_file_impl, "adalah_file")


def adalah_direktori_impl(path):
    return os.path.isdir(path)


adalah_direktori = RenzmcBuiltinFunction(adalah_direktori_impl, "adalah_direktori")


def path_absolut_impl(path):
    return os.path.abspath(path)


path_absolut = RenzmcBuiltinFunction(path_absolut_impl, "path_absolut")


def waktu_modifikasi_file_impl(path):
    return os.path.getmtime(path)


waktu_modifikasi_file = RenzmcBuiltinFunction(
    waktu_modifikasi_file_impl, "waktu_modifikasi_file"
)


def waktu_buat_file_impl(path):
    return os.path.getctime(path)


waktu_buat_file = RenzmcBuiltinFunction(waktu_buat_file_impl, "waktu_buat_file")


def file_dapat_dibaca_impl(path):
    return os.access(path, os.R_OK)


file_dapat_dibaca = RenzmcBuiltinFunction(file_dapat_dibaca_impl, "file_dapat_dibaca")


def file_dapat_ditulis_impl(path):
    return os.access(path, os.W_OK)


file_dapat_ditulis = RenzmcBuiltinFunction(
    file_dapat_ditulis_impl, "file_dapat_ditulis"
)

def median_impl(data):
    return statistics.median(data)


median = RenzmcBuiltinFunction(median_impl, "median")
nilai_tengah = median


def mode_impl(data):
    return statistics.mode(data)


mode = RenzmcBuiltinFunction(mode_impl, "mode")
nilai_modus = mode


def stdev_impl(data):
    return statistics.stdev(data)


stdev = RenzmcBuiltinFunction(stdev_impl, "stdev")
deviasi_standar = stdev


def variance_impl(data):
    return statistics.variance(data)


variance = RenzmcBuiltinFunction(variance_impl, "variance")
variansi = variance


def quantiles_impl(data, n=4):
    return statistics.quantiles(data, n=n)


quantiles = RenzmcBuiltinFunction(quantiles_impl, "quantiles")
kuantil = quantiles



def _convert_to_bool(value):
    if isinstance(value, str):
        if value == "benar" or value == "true" or value == "True":
            return True
        elif value == "salah" or value == "false" or value == "False":
            return False
        else:
            return bool(value)
    return bool(value)



def range_impl(*args):
    import builtins
    if len(args) == 1:
        return list(builtins.range(args[0]))
    elif len(args) == 2:
        return list(builtins.range(args[0], args[1]))
    elif len(args) == 3:
        return list(builtins.range(args[0], args[1], args[2]))
    else:
        raise TypeError(f"range() mengharapkan 1-3 argumen, mendapat {len(args)}")


range_func = RenzmcBuiltinFunction(range_impl, "range")
range = range_func
rentang = range_func



def buka_impl(filename, mode='r', encoding='utf-8', **kwargs):
    import builtins
    if 'b' in mode:
        return builtins.open(filename, mode, **kwargs)
    else:
        return builtins.open(filename, mode, encoding=encoding, **kwargs)


buka = RenzmcBuiltinFunction(buka_impl, "buka")
open_file = buka



def tutup_impl(file_obj):
    if hasattr(file_obj, 'close'):
        file_obj.close()
    else:
        raise TypeError("Objek tidak memiliki metode close()")


tutup = RenzmcBuiltinFunction(tutup_impl, "tutup")
close_file = tutup



def tulis_impl(file_obj, content):
    if hasattr(file_obj, 'write'):
        file_obj.write(content)
    else:
        raise TypeError("Objek tidak memiliki metode write()")


tulis = RenzmcBuiltinFunction(tulis_impl, "tulis")
write_to_file = tulis



def baca_impl(file_obj, size=-1):
    if hasattr(file_obj, 'read'):
        return file_obj.read(size)
    else:
        raise TypeError("Objek tidak memiliki metode read()")


baca = RenzmcBuiltinFunction(baca_impl, "baca")
read_from_file = baca



def tulis_json_impl(filename, data, indent=2):
    import json
    import builtins as _builtins
    with _builtins.open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


tulis_json = RenzmcBuiltinFunction(tulis_json_impl, "tulis_json")
write_json = tulis_json



def baca_json_impl(filename):
    import json
    import builtins as _builtins
    with _builtins.open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


baca_json = RenzmcBuiltinFunction(baca_json_impl, "baca_json")
read_json = baca_json



def ke_json_impl(data, indent=None):
    import json
    return json.dumps(data, indent=indent, ensure_ascii=False)


ke_json = RenzmcBuiltinFunction(ke_json_impl, "ke_json")
to_json = ke_json



def dari_json_impl(json_string):
    import json
    return json.loads(json_string)


dari_json = RenzmcBuiltinFunction(dari_json_impl, "dari_json")
from_json = dari_json



def cek_modul_python_impl(module_name):
    try:
        import importlib
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


cek_modul_python = RenzmcBuiltinFunction(cek_modul_python_impl, "cek_modul_python")
check_python_module = cek_modul_python



def path_modul_python_impl(module_name):
    try:
        import importlib
        module = importlib.import_module(module_name)
        if hasattr(module, '__file__'):
            return module.__file__
        else:
            return f"<built-in module '{module_name}'>"
    except ImportError:
        return None


path_modul_python = RenzmcBuiltinFunction(path_modul_python_impl, "path_modul_python")
get_python_module_path = path_modul_python



def versi_modul_python_impl(module_name):
    try:
        import importlib
        module = importlib.import_module(module_name)
        if hasattr(module, '__version__'):
            return module.__version__
        else:
            return "Unknown"
    except ImportError:
        return None


versi_modul_python = RenzmcBuiltinFunction(versi_modul_python_impl, "versi_modul_python")
get_python_module_version = versi_modul_python



def evaluasi_python_impl(expression):
    try:
        return eval(expression)
    except Exception as e:
        raise RuntimeError(f"Error evaluating Python expression: {str(e)}")


evaluasi_python = RenzmcBuiltinFunction(evaluasi_python_impl, "evaluasi_python")
eval_python = evaluasi_python



def eksekusi_python_impl(code):
    try:
        exec(code)
        return None
    except Exception as e:
        raise RuntimeError(f"Error executing Python code: {str(e)}")


eksekusi_python = RenzmcBuiltinFunction(eksekusi_python_impl, "eksekusi_python")
exec_python = eksekusi_python



def input_impl(prompt=''):
    import builtins
    return builtins.input(prompt)


input_func = RenzmcBuiltinFunction(input_impl, "input")
input = input_func
masukan = input_func



def print_impl(*args, sep=' ', end='\n'):
    import builtins
    builtins.print(*args, sep=sep, end=end)


print_func = RenzmcBuiltinFunction(print_impl, "print")
print = print_func
cetak = print_func
tampilkan = print_func



def list_impl(iterable):
    import builtins as _builtins
    return _builtins.list(iterable)


list_renzmc = RenzmcBuiltinFunction(list_impl, "list")
daftar = RenzmcBuiltinFunction(list_impl, "daftar")



def dict_impl(*args, **kwargs):
    import builtins as _builtins
    return _builtins.dict(*args, **kwargs)


dict_renzmc = RenzmcBuiltinFunction(dict_impl, "dict")
kamus = RenzmcBuiltinFunction(dict_impl, "kamus")



def set_impl(iterable=None):
    import builtins as _builtins
    if iterable is None:
        return _builtins.set()
    return _builtins.set(iterable)


set_renzmc = RenzmcBuiltinFunction(set_impl, "set")
himpunan = RenzmcBuiltinFunction(set_impl, "himpunan")



def tuple_impl(iterable=None):
    import builtins as _builtins
    if iterable is None:
        return _builtins.tuple()
    return _builtins.tuple(iterable)


tuple_renzmc = RenzmcBuiltinFunction(tuple_impl, "tuple")
tupel = RenzmcBuiltinFunction(tuple_impl, "tupel")



def str_impl(obj):
    import builtins as _builtins
    return _builtins.str(obj)


str_renzmc = RenzmcBuiltinFunction(str_impl, "str")
teks_convert = RenzmcBuiltinFunction(str_impl, "teks")



def int_impl(obj, base=10):
    import builtins as _builtins
    if isinstance(obj, str) and base != 10:
        return _builtins.int(obj, base)
    return _builtins.int(obj)


int_renzmc = RenzmcBuiltinFunction(int_impl, "int")
bulat_int = RenzmcBuiltinFunction(int_impl, "bulat_int")



def float_impl(obj):
    import builtins as _builtins
    return _builtins.float(obj)


float_renzmc = RenzmcBuiltinFunction(float_impl, "float")
pecahan = RenzmcBuiltinFunction(float_impl, "pecahan")



def bool_impl(obj):
    import builtins as _builtins
    return _builtins.bool(obj)


bool_renzmc = RenzmcBuiltinFunction(bool_impl, "bool")
boolean = RenzmcBuiltinFunction(bool_impl, "boolean")



def sum_impl(iterable, start=0):
    import builtins as _builtins
    return _builtins.sum(iterable, start)


sum_renzmc = RenzmcBuiltinFunction(sum_impl, "sum")



def len_impl(obj):
    import builtins as _builtins
    return _builtins.len(obj)


len_renzmc = RenzmcBuiltinFunction(len_impl, "len")
panjang_len = RenzmcBuiltinFunction(len_impl, "panjang_len")



def min_impl(*args, **kwargs):
    import builtins as _builtins
    return _builtins.min(*args, **kwargs)


min_renzmc = RenzmcBuiltinFunction(min_impl, "min")
min_nilai = RenzmcBuiltinFunction(min_impl, "min_nilai")



def max_impl(*args, **kwargs):
    import builtins as _builtins
    return _builtins.max(*args, **kwargs)


max_renzmc = RenzmcBuiltinFunction(max_impl, "max")
max_nilai = RenzmcBuiltinFunction(max_impl, "max_nilai")



def abs_impl(x):
    import builtins as _builtins
    return _builtins.abs(x)


abs_renzmc = RenzmcBuiltinFunction(abs_impl, "abs")
nilai_absolut = RenzmcBuiltinFunction(abs_impl, "nilai_absolut")



def round_impl(number, ndigits=None):
    import builtins as _builtins
    if ndigits is None:
        return _builtins.round(number)
    return _builtins.round(number, ndigits)


round_renzmc = RenzmcBuiltinFunction(round_impl, "round")
bulatkan = RenzmcBuiltinFunction(round_impl, "bulatkan")



def pow_impl(base, exp, mod=None):
    import builtins as _builtins
    if mod is None:
        return _builtins.pow(base, exp)
    return _builtins.pow(base, exp, mod)


pow_renzmc = RenzmcBuiltinFunction(pow_impl, "pow")
pangkat_pow = RenzmcBuiltinFunction(pow_impl, "pangkat_pow")



def reversed_impl(seq):
    import builtins as _builtins
    return list(_builtins.reversed(seq))


reversed_renzmc = RenzmcBuiltinFunction(reversed_impl, "reversed")
terbalik = RenzmcBuiltinFunction(reversed_impl, "terbalik")



def http_get_impl(url, **kwargs):
    from renzmc.runtime.http_client import http_get
    return http_get(url, **kwargs)

def http_post_impl(url, **kwargs):
    from renzmc.runtime.http_client import http_post
    return http_post(url, **kwargs)

def http_put_impl(url, **kwargs):
    from renzmc.runtime.http_client import http_put
    return http_put(url, **kwargs)

def http_delete_impl(url, **kwargs):
    from renzmc.runtime.http_client import http_delete
    return http_delete(url, **kwargs)

def http_patch_impl(url, **kwargs):
    from renzmc.runtime.http_client import http_patch
    return http_patch(url, **kwargs)

def http_set_header_impl(key, value):
    from renzmc.runtime.http_client import http_set_header
    return http_set_header(key, value)

def http_set_timeout_impl(timeout):
    from renzmc.runtime.http_client import http_set_timeout
    return http_set_timeout(timeout)

http_get = RenzmcBuiltinFunction(http_get_impl, "http_get")
http_post = RenzmcBuiltinFunction(http_post_impl, "http_post")
http_put = RenzmcBuiltinFunction(http_put_impl, "http_put")
http_delete = RenzmcBuiltinFunction(http_delete_impl, "http_delete")
http_patch = RenzmcBuiltinFunction(http_patch_impl, "http_patch")
http_set_header = RenzmcBuiltinFunction(http_set_header_impl, "http_set_header")
http_set_timeout = RenzmcBuiltinFunction(http_set_timeout_impl, "http_set_timeout")

ambil_http = RenzmcBuiltinFunction(http_get_impl, "ambil_http")
kirim_http = RenzmcBuiltinFunction(http_post_impl, "kirim_http")
perbarui_http = RenzmcBuiltinFunction(http_put_impl, "perbarui_http")
hapus_http = RenzmcBuiltinFunction(http_delete_impl, "hapus_http")
