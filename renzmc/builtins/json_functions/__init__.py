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

import json


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


def json_ke_teks(obj, indent=None):
    try:
        return json.dumps(obj, indent=indent, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Error mengkonversi ke JSON: {e}")


def teks_ke_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e}")


def tulis_json_impl(filename, data, indent=2):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except Exception as e:
        raise Exception(f"Error menulis JSON ke file: {e}")


def baca_json_impl(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON dari file: {e}")


def ke_json_impl(data, indent=None):
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Error mengkonversi ke JSON: {e}")


def dari_json_impl(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e}")


tulis_json = RenzmcBuiltinFunction(tulis_json_impl, "tulis_json")
baca_json = RenzmcBuiltinFunction(baca_json_impl, "baca_json")
ke_json = RenzmcBuiltinFunction(ke_json_impl, "ke_json")
dari_json = RenzmcBuiltinFunction(dari_json_impl, "dari_json")
