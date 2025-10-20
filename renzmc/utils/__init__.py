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

import asyncio
import base64
import datetime
import hashlib
import importlib
import inspect
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union


def is_identifier(name):
    return re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", name) is not None


def is_keyword(name):
    keywords = [
        "jika",
        "kalau",
        "maka",
        "tidak",
        "lainnya",
        "selesai",
        "selama",
        "ulangi",
        "kali",
        "untuk",
        "setiap",
        "dari",
        "sampai",
        "lanjut",
        "berhenti",
        "coba",
        "tangkap",
        "akhirnya",
        "simpan",
        "ke",
        "dalam",
        "itu",
        "adalah",
        "sebagai",
        "tampilkan",
        "tulis",
        "cetak",
        "tunjukkan",
        "tanya",
        "buat",
        "fungsi",
        "dengan",
        "parameter",
        "panggil",
        "jalankan",
        "kembali",
        "hasil",
        "kelas",
        "metode",
        "konstruktor",
        "warisi",
        "gunakan",
        "impor",
        "impor_python",
        "modul",
        "paket",
        "lambda",
        "async",
        "await",
        "yield",
        "dekorator",
        "tipe",
        "jenis_data",
        "generator",
        "asinkron",
        "dan",
        "atau",
        "benar",
        "salah",
        "self",
        "ini",
    ]
    return name in keywords


def format_code(code):
    lines = code.split("\n")
    result = []
    indent_level = 0
    for line in lines:
        stripped = line.strip()
        if stripped in [
            "selesai",
            "kalau tidak",
            "kalau tidak jika",
            "akhirnya",
            "tangkap",
        ]:
            indent_level = max(0, indent_level - 1)
        if stripped:
            result.append("    " * indent_level + stripped)
        else:
            result.append("")
        if stripped.endswith(":") or any(
            (
                stripped.startswith(keyword)
                for keyword in [
                    "jika",
                    "kalau tidak jika",
                    "kalau tidak",
                    "selama",
                    "untuk setiap",
                    "ulangi",
                    "buat fungsi",
                    "buat kelas",
                    "buat metode",
                    "konstruktor",
                    "coba",
                    "tangkap",
                ]
            )
        ):
            indent_level += 1
    return "\n".join(result)


def parse_type_annotation(annotation):
    if annotation == "int" or annotation == "bilangan_bulat":
        return int
    elif annotation == "float" or annotation == "desimal":
        return float
    elif annotation == "str" or annotation == "teks":
        return str
    elif annotation == "bool" or annotation == "boolean":
        return bool
    elif annotation == "list" or annotation == "daftar":
        return list
    elif annotation == "dict" or annotation == "kamus":
        return dict
    elif annotation == "set" or annotation == "himpunan":
        return set
    elif annotation == "tuple" or annotation == "tupel":
        return tuple
    elif annotation == "None" or annotation == "kosong":
        return type(None)
    elif annotation == "Any" or annotation == "apapun":
        return Any
    elif annotation.startswith("List[") or annotation.startswith("Daftar["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        return List[parse_type_annotation(inner)]
    elif annotation.startswith("Dict[") or annotation.startswith("Kamus["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        key_type, value_type = inner.split(",")
        return Dict[
            parse_type_annotation(key_type.strip()),
            parse_type_annotation(value_type.strip()),
        ]
    elif annotation.startswith("Set[") or annotation.startswith("Himpunan["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        return Set[parse_type_annotation(inner)]
    elif annotation.startswith("Tuple[") or annotation.startswith("Tupel["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        types = [parse_type_annotation(t.strip()) for t in inner.split(",")]
        return Tuple[tuple(types)]
    elif annotation.startswith("Optional[") or annotation.startswith("Opsional["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        return Optional[parse_type_annotation(inner)]
    elif annotation.startswith("Union[") or annotation.startswith("Gabungan["):
        inner = annotation[annotation.index("[") + 1 : annotation.rindex("]")]
        types = [parse_type_annotation(t.strip()) for t in inner.split(",")]
        return Union[tuple(types)]
    elif annotation.startswith("Callable[") or annotation.startswith("Fungsi["):
        return Callable
    else:
        return annotation


def check_type(value, type_annotation):
    if type_annotation is Any:
        return True
    if isinstance(type_annotation, str):
        type_annotation = parse_type_annotation(type_annotation)
    if isinstance(type_annotation, type):
        return isinstance(value, type_annotation)
    origin = getattr(type_annotation, "__origin__", None)
    args = getattr(type_annotation, "__args__", None)
    if origin is list or origin is List:
        return isinstance(value, list) and all((check_type(item, args[0]) for item in value))
    elif origin is dict or origin is Dict:
        return isinstance(value, dict) and all(
            (check_type(k, args[0]) and check_type(v, args[1]) for k, v in value.items())
        )
    elif origin is set or origin is Set:
        return isinstance(value, set) and all((check_type(item, args[0]) for item in value))
    elif origin is tuple or origin is Tuple:
        return (
            isinstance(value, tuple)
            and len(value) == len(args)
            and all((check_type(value[i], args[i]) for i in range(len(args))))
        )
    elif origin is Union:
        return any((check_type(value, arg) for arg in args))
    elif origin is Optional:
        return value is None or check_type(value, args[0])
    elif origin is Callable:
        return callable(value)
    return False


def format_error_message(error, source_code=None):
    if not hasattr(error, "line") or not hasattr(error, "column") or error.line is None or (error.column is None):
        return str(error)
    result = f"Error: {error.message}\n"
    result += f"Pada baris {error.line}, kolom {error.column}\n"
    code_to_use = error.source_code if hasattr(error, "source_code") and error.source_code else source_code
    if code_to_use:
        lines = code_to_use.split("\n")
        if 0 <= error.line - 1 < len(lines):
            line = lines[error.line - 1]
            result += f"\n{error.line} | {line}\n"
            result += " " * (len(str(error.line)) + 3 + error.column - 1) + "^\n"
            context_lines = 2
            start_line = max(0, error.line - 1 - context_lines)
            end_line = min(len(lines), error.line - 1 + context_lines + 1)
            if start_line > 0:
                result += "...\n"
            for i in range(start_line, end_line):
                if i == error.line - 1:
                    continue
                result += f"{i + 1} | {lines[i]}\n"
            if end_line < len(lines):
                result += "...\n"
    return result


def load_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        raise ImportError(f"Tidak dapat mengimpor modul '{module_name}'")


def get_module_functions(module):
    return {name: obj for name, obj in inspect.getmembers(module, inspect.isfunction) if not name.startswith("_")}


def get_module_classes(module):
    return {name: obj for name, obj in inspect.getmembers(module, inspect.isclass) if not name.startswith("_")}


def get_module_variables(module):
    return {
        name: obj
        for name, obj in inspect.getmembers(module)
        if not name.startswith("_") and (not inspect.isfunction(obj)) and (not inspect.isclass(obj))
    }


def get_class_methods(cls):
    return {name: obj for name, obj in inspect.getmembers(cls, inspect.isfunction) if not name.startswith("_")}


def get_class_attributes(cls):
    return {
        name: obj
        for name, obj in inspect.getmembers(cls)
        if not name.startswith("_") and (not inspect.isfunction(obj)) and (not inspect.ismethod(obj))
    }


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


def is_async_function(func):
    return asyncio.iscoroutinefunction(func)


def run_async(coro):
    return asyncio.run(coro)


def wait_all_async(coros):
    return asyncio.run(asyncio.gather(*coros))


def create_async_function(func):

    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def json_to_dict(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON tidak valid: {str(e)}")


def dict_to_json(dictionary):
    try:
        return json.dumps(dictionary, ensure_ascii=False)
    except TypeError as e:
        raise TypeError(f"Tidak dapat mengkonversi kamus ke JSON: {str(e)}")


def get_current_time():
    return datetime.datetime.now()


def format_time(dt, format_str="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(format_str)


def parse_time(time_str, format_str="%Y-%m-%d %H:%M:%S"):
    try:
        return datetime.datetime.strptime(time_str, format_str)
    except ValueError:
        raise ValueError(f"Format waktu tidak valid: '{time_str}' (format: '{format_str}')")


def get_timestamp():
    return time.time()


def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def datetime_to_timestamp(dt):
    return dt.timestamp()


def hash_string(string, algorithm="sha256"):
    if algorithm == "md5":
        return hashlib.md5(string.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(string.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(string.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(string.encode()).hexdigest()
    else:
        raise ValueError(f"Algoritma hash tidak valid: '{algorithm}'")


def generate_uuid():
    return str(uuid.uuid4())


def base64_encode(string):
    return base64.b64encode(string.encode()).decode()


def base64_decode(string):
    try:
        return base64.b64decode(string.encode()).decode()
    except Exception:
        raise ValueError(f"String Base64 tidak valid: '{string}'")


def url_encode(string):
    return urllib.parse.quote(string)


def url_decode(string):
    return urllib.parse.unquote(string)


def http_get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return {
            "status": response.status,
            "headers": dict(response.headers),
            "content": response.read().decode("utf-8"),
        }


def http_post(url, data, headers=None):
    data_bytes = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers=headers or {}, method="POST")
    with urllib.request.urlopen(req) as response:
        return {
            "status": response.status,
            "headers": dict(response.headers),
            "content": response.read().decode("utf-8"),
        }


def file_exists(path):
    return os.path.exists(path)


def is_file(path):
    return os.path.isfile(path)


def is_directory(path):
    return os.path.isdir(path)


def get_file_size(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    return os.path.getsize(path)


def get_file_modification_time(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    return os.path.getmtime(path)


def list_directory(path="."):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    return os.listdir(path)


def create_directory(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            raise FileExistsError(f"Direktori sudah ada: '{path}'")
        else:
            raise FileExistsError(f"File sudah ada dengan nama yang sama: '{path}'")
    os.makedirs(path)


def remove_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    if os.path.isdir(path):
        raise IsADirectoryError(f"Tidak dapat menghapus direktori dengan fungsi ini: '{path}'")
    os.remove(path)


def remove_directory(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    os.rmdir(path)


def join_path(*paths):
    return os.path.join(*paths)


def get_absolute_path(path):
    return os.path.abspath(path)


def get_basename(path):
    return os.path.basename(path)


def get_dirname(path):
    return os.path.dirname(path)


def get_extension(path):
    return os.path.splitext(path)[1]


def change_extension(path, extension):
    return os.path.splitext(path)[0] + extension


def normalize_path(path):
    return os.path.normpath(path)


def get_current_directory():
    return os.getcwd()


def change_directory(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    os.chdir(path)


def get_environment_variable(name):
    if name not in os.environ:
        raise KeyError(f"Variabel lingkungan tidak ditemukan: '{name}'")
    return os.environ[name]


def set_environment_variable(name, value):
    os.environ[name] = value


def get_python_version():
    return sys.version


def get_platform():
    return sys.platform


def get_executable():
    return sys.executable


def get_path():
    return sys.path


def add_to_path(path):
    sys.path.append(path)


def get_modules():
    return sys.modules


def get_arguments():
    return sys.argv


def exit(code=0):
    sys.exit(code)
