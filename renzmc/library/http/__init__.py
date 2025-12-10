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
RenzMcLang HTTP Library

Module ini menyediakan fungsi untuk melakukan HTTP requests,
mengikuti standar requests library dengan nama fungsi dalam Bahasa Indonesia.

Functions:
- get: HTTP GET request
- post: HTTP POST request  
- put: HTTP PUT request
- delete: HTTP DELETE request
- patch: HTTP PATCH request
- head: HTTP HEAD request
- options: HTTP OPTIONS request

Classes:
- Response: HTTP response object
- Session: HTTP session untuk connection pooling
- Request: HTTP request object

Usage:
    dari http impor get, post
    
    response = get('https://api.example.com/data')
    data = response.json()
    
    post_response = post('https://api.example.com/users', json={'name': 'Budi'})
"""

import urllib.parse
import urllib.request
import urllib.error
import json as py_json
import ssl
from typing import Dict, Any, Optional, Union, Tuple

# Global settings
DEFAULT_TIMEOUT = 30
DEFAULT_HEADERS = {
    'User-Agent': 'RenzMcLang-HTTP/1.0'
}


class HTTPResponse:
    """
    HTTP Response object yang menyimpan hasil dari request.
    """

    def __init__(self, response: urllib.request.addinfourl, content: bytes = None):
        self._response = response
        self._content = content
        self._url = response.geturl()
        self._status_code = response.getcode()
        self._headers = dict(response.headers)

    @property
    def url(self) -> str:
        """URL dari response."""
        return self._url

    @property
    def status_code(self) -> int:
        """HTTP status code."""
        return self._status_code

    @property
    def headers(self) -> Dict[str, str]:
        """Response headers."""
        return self._headers

    @property
    def text(self) -> str:
        """Response body sebagai string."""
        if self._content is not None:
            return self._content.decode('utf-8')
        return self._response.read().decode('utf-8')

    def json(self) -> Dict[str, Any]:
        """Parse response body sebagai JSON."""
        return py_json.loads(self.text)

    def content(self) -> bytes:
        """Response body sebagai bytes."""
        if self._content is not None:
            return self._content
        return self._response.read()

    def ok(self) -> bool:
        """Cek apakah request berhasil (status code 200-299)."""
        return 200 <= self._status_code < 300

    def raise_for_status(self):
        """Raise exception jika status code menunjukkan error."""
        if not self.ok():
            raise HTTPError(f"HTTP {self._status_code} Error for {self._url}")


class HTTPError(Exception):
    """
    HTTP Error exception untuk request failures.
    """

    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class HTTPSession:
    """
    HTTP Session untuk connection pooling dan persistent connections.
    """

    def __init__(self):
        self.headers = DEFAULT_HEADERS.copy()
        self.timeout = DEFAULT_TIMEOUT

    def request(self, method: str, url: str, **kwargs) -> HTTPResponse:
        """
        Perform HTTP request dengan method tertentu.
        """
        return _make_request(method, url, headers=self.headers, timeout=self.timeout, **kwargs)

    def get(self, url: str, **kwargs) -> HTTPResponse:
        """HTTP GET request."""
        return self.request('GET', url, **kwargs)

    def post(self, url: str, **kwargs) -> HTTPResponse:
        """HTTP POST request."""
        return self.request('POST', url, **kwargs)

    def put(self, url: str, **kwargs) -> HTTPResponse:
        """HTTP PUT request."""
        return self.request('PUT', url, **kwargs)

    def delete(self, url: str, **kwargs) -> HTTPResponse:
        """HTTP DELETE request."""
        return self.request('DELETE', url, **kwargs)

    def patch(self, url: str, **kwargs) -> HTTPResponse:
        """HTTP PATCH request."""
        return self.request('PATCH', url, **kwargs)


def _make_request(method: str, url: str, params: Dict[str, Any] = None,
                  data: Union[str, bytes, Dict] = None, json: Dict[str, Any] = None,
                  headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT,
                  allow_redirects: bool = True) -> HTTPResponse:
    """
    Internal function untuk membuat HTTP request.
    """
    if headers is None:
        headers = DEFAULT_HEADERS.copy()
    else:
        headers = {**DEFAULT_HEADERS, **headers}

    # Add parameters to URL
    if params:
        query_string = urllib.parse.urlencode(params)
        if '?' in url:
            url += '&' + query_string
        else:
            url += '?' + query_string

    # Prepare data
    if json is not None:
        data = py_json.dumps(json).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode('utf-8')
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    elif isinstance(data, str):
        data = data.encode('utf-8')

    # Create request
    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        # Create SSL context yang tidak verify certificates (untuk compatibility)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as response:
            content = response.read()
            return HTTPResponse(response, content)

    except urllib.error.HTTPError as e:
        error_content = e.read() if hasattr(e, 'read') else None
        return HTTPResponse(e, error_content)
    except Exception as e:
        raise HTTPError(str(e))

# Main HTTP Functions


def get(url: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None,
        timeout: int = DEFAULT_TIMEOUT, **kwargs) -> HTTPResponse:
    """
    HTTP GET request.

    Args:
        url: URL untuk request
        params: Query parameters
        headers: Additional headers
        timeout: Request timeout in seconds
        **kwargs: Additional arguments

    Returns:
        HTTPResponse object

    Example:
        response = get('https://api.example.com/users', params={'page': 1})
        users = response.json()
    """
    return _make_request('GET', url, params=params, headers=headers, timeout=timeout, **kwargs)


def post(url: str, data: Union[str, bytes, Dict] = None, json: Dict[str, Any] = None,
         headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT, **kwargs) -> HTTPResponse:
    """
    HTTP POST request.

    Args:
        url: URL untuk request
        data: Data untuk POST (form data)
        json: JSON data untuk POST
        headers: Additional headers
        timeout: Request timeout in seconds
        **kwargs: Additional arguments

    Returns:
        HTTPResponse object

    Example:
        response = post('https://api.example.com/users', json={'name': 'Budi'})
        user = response.json()
    """
    return _make_request('POST', url, data=data, json=json, headers=headers, timeout=timeout, **kwargs)


def put(url: str, data: Union[str, bytes, Dict] = None, json: Dict[str, Any] = None,
        headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT, **kwargs) -> HTTPResponse:
    """
    HTTP PUT request.
    """
    return _make_request('PUT', url, data=data, json=json, headers=headers, timeout=timeout, **kwargs)


def delete(url: str, headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT,
           **kwargs) -> HTTPResponse:
    """
    HTTP DELETE request.
    """
    return _make_request('DELETE', url, headers=headers, timeout=timeout, **kwargs)


def patch(url: str, data: Union[str, bytes, Dict] = None, json: Dict[str, Any] = None,
          headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT, **kwargs) -> HTTPResponse:
    """
    HTTP PATCH request.
    """
    return _make_request('PATCH', url, data=data, json=json, headers=headers, timeout=timeout, **kwargs)


def head(url: str, headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT,
         **kwargs) -> HTTPResponse:
    """
    HTTP HEAD request.
    """
    return _make_request('HEAD', url, headers=headers, timeout=timeout, **kwargs)


def options(url: str, headers: Dict[str, str] = None, timeout: int = DEFAULT_TIMEOUT,
            **kwargs) -> HTTPResponse:
    """
    HTTP OPTIONS request.
    """
    return _make_request('OPTIONS', url, headers=headers, timeout=timeout, **kwargs)

# Utility Functions


def set_default_header(key: str, value: str):
    """
    Set default header untuk semua requests.

    Args:
        key: Header name
        value: Header value

    Example:
        set_default_header('Authorization', 'Bearer token123')
    """
    DEFAULT_HEADERS[key] = value


def set_default_timeout(timeout: int):
    """
    Set default timeout untuk semua requests.

    Args:
        timeout: Timeout in seconds
    """
    global DEFAULT_TIMEOUT
    DEFAULT_TIMEOUT = timeout


def create_session() -> HTTPSession:
    """
    Create HTTP session object.

    Returns:
        HTTPSession object
    """
    return HTTPSession()


# Indonesian Aliases
ambil = get
kirim = post
perbarui = put
hapus = delete
tambal = patch
kepala = head
opsi = options
respon = HTTPResponse
sesi = HTTPSession
error_http = HTTPError
atur_header_default = set_default_header
atur_timeout_default = set_default_timeout
buat_sesi = create_session

__all__ = [
    # Classes
    "HTTPResponse", "HTTPSession", "HTTPError",
    # Main Functions
    "get", "post", "put", "delete", "patch", "head", "options",
    # Utility Functions
    "set_default_header", "set_default_timeout", "create_session",
    # Indonesian Aliases
    "ambil", "kirim", "perbarui", "hapus", "tambal", "kepala", "opsi",
    "respon", "sesi", "error_http", "atur_header_default",
    "atur_timeout_default", "buat_sesi"
]
