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

from typing import Any, Dict, Optional

import requests


class HTTPResponse:

    def __init__(self, response):
        self._response = response
        self.status_code = response.status_code
        self.headers = dict(response.headers)
        self.text = response.text
        self.url = response.url

    def json(self):
        try:
            return self._response.json()
        except Exception as e:
            raise ValueError(f"Gagal parse JSON: {e}")

    def ok(self):
        return 200 <= self.status_code < 300

    def __str__(self):
        return f"<HTTPResponse [{self.status_code}]>"

    def __repr__(self):
        return self.__str__()


class HTTPClient:

    def __init__(self):
        self.session = requests.Session()
        self.default_timeout = 30
        self.default_headers = {"User-Agent": "RenzMcLang"}

    def get(
        self,
        url: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ) -> HTTPResponse:
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.get(
                url,
                params=params,
                headers=merged_headers,
                timeout=timeout or self.default_timeout,
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP GET error: {e}")

    def post(
        self,
        url: str,
        data: Optional[Any] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ) -> HTTPResponse:
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.post(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout,
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP POST error: {e}")

    def put(
        self,
        url: str,
        data: Optional[Any] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ) -> HTTPResponse:
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.put(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout,
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP PUT error: {e}")

    def delete(self, url: str, headers: Optional[Dict] = None, timeout: Optional[int] = None) -> HTTPResponse:
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.delete(url, headers=merged_headers, timeout=timeout or self.default_timeout)
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP DELETE error: {e}")

    def patch(
        self,
        url: str,
        data: Optional[Any] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ) -> HTTPResponse:
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.patch(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout,
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP PATCH error: {e}")

    def set_header(self, key: str, value: str):
        self.default_headers[key] = value

    def set_timeout(self, timeout: int):
        self.default_timeout = timeout


_http_client = HTTPClient()


def http_get(url: str, **kwargs) -> HTTPResponse:
    return _http_client.get(url, **kwargs)


def http_post(url: str, **kwargs) -> HTTPResponse:
    return _http_client.post(url, **kwargs)


def http_put(url: str, **kwargs) -> HTTPResponse:
    return _http_client.put(url, **kwargs)


def http_delete(url: str, **kwargs) -> HTTPResponse:
    return _http_client.delete(url, **kwargs)


def http_patch(url: str, **kwargs) -> HTTPResponse:
    return _http_client.patch(url, **kwargs)


def http_set_header(key: str, value: str):
    _http_client.set_header(key, value)


def http_set_timeout(timeout: int):
    _http_client.set_timeout(timeout)
