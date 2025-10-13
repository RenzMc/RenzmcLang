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


class RenzmcBuiltinFunction:

    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return f"<builtin function '{self.name}'>"


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
