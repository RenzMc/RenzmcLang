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

import base64
import hashlib
import re
import urllib.parse


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


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
        raise ValueError(f"Algoritma '{algorithm}' tidak didukung")


def url_encode(text):
    return urllib.parse.quote(text)


def url_decode(text):
    return urllib.parse.unquote(text)


def regex_match(pattern, text):
    try:
        match = re.search(pattern, text)
        return match.group() if match else None
    except re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {e}")


def regex_replace(pattern, replacement, text):
    try:
        return re.sub(pattern, replacement, text)
    except re.error as e:
        raise ValueError(f"Pattern regex tidak valid: {e}")


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        raise ValueError(f"Error decoding base64: {e}")
