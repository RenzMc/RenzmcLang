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
RenzMcLang JSON Library

Module ini menyediakan fungsi untuk encoding dan decoding JSON,
mengikuti standar Python json module dengan nama fungsi dalam Bahasa Indonesia.

Functions:
- loads: Parse JSON string menjadi Python object
- dumps: Convert Python object menjadi JSON string
- load: Parse JSON dari file object
- dump: Write JSON ke file object

Classes:
- JSONDecoder: Custom decoder untuk parsing JSON
- JSONEncoder: Custom encoder untuk serialisasi JSON

Usage:
    dari json impor loads, dumps
    
    data = {"nama": "Budi", "umur": 25}
    json_str = dumps(data, indent=2)
    parsed = loads(json_str)
"""

import json as py_json
from typing import Any, Dict, List, Union, Optional

# JSON Types
JSONType = Union[Dict[str, Any], List[Any], str, int, float, bool, None]


def loads(s: str, *, encoding: Optional[str] = None, cls=None,
          object_hook=None, parse_float=None, parse_int=None,
          parse_constant=None, object_pairs_hook=None, **kw) -> JSONType:
    """
    Parse JSON string menjadi Python object.

    Args:
        s: JSON string yang akan di-parse
        encoding: Encoding yang digunakan (deprecated)
        cls: Custom JSON decoder class
        object_hook: Function untuk custom object parsing
        parse_float: Function untuk parsing float
        parse_int: Function untuk parsing integer
        parse_constant: Function untuk parsing constants (NaN, Inf, -Inf)
        object_pairs_hook: Function untuk parsing object pairs
        **kw: Additional keyword arguments

    Returns:
        Python object hasil parsing JSON

    Raises:
        JSONDecodeError: Jika JSON string tidak valid

    Example:
        json_str = '{"nama": "Budi", "umur": 25}'
        data = loads(json_str)
        # data = {"nama": "Budi", "umur": 25}
    """
    return py_json.loads(
        s, encoding=encoding, cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook, **kw
    )


def dumps(obj: JSONType, *, skipkeys=False, ensure_ascii=True,
          check_circular=True, allow_nan=True, cls=None, indent=None,
          separators=None, default=None, sort_keys=False, **kw) -> str:
    """
    Convert Python object menjadi JSON string.

    Args:
        obj: Python object yang akan di-serialize
        skipkeys: Skip keys yang bukan string
        ensure_ascii: Ensure output ASCII
        check_circular: Check circular reference
        allow_nan: Allow NaN, Inf, -Inf
        cls: Custom JSON encoder class
        indent: Number of spaces untuk indentasi
        separators: Tuple item separator dan key separator
        default: Function untuk object yang tidak bisa di-serialize
        sort_keys: Sort keys alphabetically
        **kw: Additional keyword arguments

    Returns:
        JSON string

    Raises:
        TypeError: Jika object tidak bisa di-serialize

    Example:
        data = {"nama": "Budi", "umur": 25}
        json_str = dumps(data, indent=2, sort_keys=True)
        # {
        #   "nama": "Budi",
        #   "umur": 25
        # }
    """
    return py_json.dumps(
        obj, skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, cls=cls,
        indent=indent, separators=separators, default=default,
        sort_keys=sort_keys, **kw
    )


def load(fp, *, cls=None, object_hook=None, parse_float=None,
         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) -> JSONType:
    """
    Parse JSON dari file-like object.

    Args:
        fp: File-like object yang berisi JSON
        cls: Custom JSON decoder class
        object_hook: Function untuk custom object parsing
        parse_float: Function untuk parsing float
        parse_int: Function untuk parsing integer
        parse_constant: Function untuk parsing constants
        object_pairs_hook: Function untuk parsing object pairs
        **kw: Additional keyword arguments

    Returns:
        Python object hasil parsing JSON

    Example:
        dengan open('data.json', 'r') sebagai f:
            data = load(f)
    """
    return py_json.load(
        fp, cls=cls, object_hook=object_hook, parse_float=parse_float,
        parse_int=parse_int, parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook, **kw
    )


def dump(obj: JSONType, fp, *, skipkeys=False, ensure_ascii=True,
         check_circular=True, allow_nan=True, cls=None, indent=None,
         separators=None, default=None, sort_keys=False, **kw) -> None:
    """
    Write JSON object ke file-like object.

    Args:
        obj: Python object yang akan di-serialize
        fp: File-like object untuk write output
        skipkeys: Skip keys yang bukan string
        ensure_ascii: Ensure output ASCII
        check_circular: Check circular reference
        allow_nan: Allow NaN, Inf, -Inf
        cls: Custom JSON encoder class
        indent: Number of spaces untuk indentasi
        separators: Tuple item separator dan key separator
        default: Function untuk object yang tidak bisa di-serialize
        sort_keys: Sort keys alphabetically
        **kw: Additional keyword arguments

    Example:
        data = {"nama": "Budi", "umur": 25}
        dengan open('output.json', 'w') sebagai f:
            dump(data, f, indent=2)
    """
    py_json.dump(
        obj, fp, skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, cls=cls,
        indent=indent, separators=separators, default=default,
        sort_keys=sort_keys, **kw
    )

# Custom JSON Decoder


class JSONDecoder(py_json.JSONDecoder):
    """
    Custom JSON decoder dengan additional functionality.

    Inherits dari Python's JSONDecoder dan menambahkan fitur-fitur khusus.
    """
    pass

# Custom JSON Encoder


class JSONEncoder(py_json.JSONEncoder):
    """
    Custom JSON encoder dengan additional functionality.

    Inherits dari Python's JSONEncoder dan menambahkan fitur-fitur khusus.
    """

    def default(self, obj):
        """
        Override default method untuk handling custom types.
        """
        # Add custom type handling here
        return super().default(obj)

# Exception


class JSONDecodeError(py_json.JSONDecodeError):
    """
    Exception yang di-raised saat JSON parsing gagal.
    """
    pass


# Indonesian Aliases
baca_json = loads
tulis_json = dumps
baca_dari_file = load
tulis_ke_file = dump
parser_json = JSONDecoder
encoder_json = JSONEncoder
error_json = JSONDecodeError

# Utility Functions


def format_json(obj: JSONType, indent: int = 2) -> str:
    """
    Format JSON string dengan indentasi yang rapi.

    Args:
        obj: Python object yang akan di-format
        indent: Number of spaces untuk indentasi

    Returns:
        JSON string yang sudah di-format
    """
    return dumps(obj, indent=indent, sort_keys=True, ensure_ascii=False)


def validate_json(s: str) -> bool:
    """
    Validasi apakah string adalah JSON yang valid.

    Args:
        s: String yang akan divalidasi

    Returns:
        True jika valid, False jika tidak
    """
    try:
        loads(s)
        return True
    except JSONDecodeError:
        return False


def minify_json(obj: JSONType) -> str:
    """
    Convert object menjadi JSON string yang minimal (tanpa spasi).

    Args:
        obj: Python object yang akan di-minify

    Returns:
        Minified JSON string
    """
    return dumps(obj, separators=(',', ':'), ensure_ascii=True)


__all__ = [
    # Main Functions
    "loads", "dumps", "load", "dump",
    # Classes
    "JSONDecoder", "JSONEncoder",
    # Exception
    "JSONDecodeError",
    # Indonesian Aliases
    "baca_json", "tulis_json", "baca_dari_file", "tulis_ke_file",
    "parser_json", "encoder_json", "error_json",
    # Utility Functions
    "format_json", "validate_json", "minify_json"
]
