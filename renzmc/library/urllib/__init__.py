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
RenzMcLang Urllib Library

Library untuk URL handling dan manipulation dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import urllib.parse as python_urlparse
import urllib.request as python_urlrequest
import urllib.error as python_urlerror
import json
import os


def parse_url(url):
    """
    Parse URL menjadi komponen-komponennya.

    Args:
        url: URL string untuk di-parse

    Returns:
        dict: Komponen URL (scheme, netloc, path, params, query, fragment)
    """
    try:
        parsed = python_urlparse.urlparse(url)
        return {
            "scheme": parsed.scheme,
            "netloc": parsed.netloc,
            "path": parsed.path,
            "params": parsed.params,
            "query": parsed.query,
            "fragment": parsed.fragment,
            "username": parsed.username,
            "password": parsed.password,
            "hostname": parsed.hostname,
            "port": parsed.port,
        }
    except Exception as e:
        raise ValueError(f"Gagal parse URL: {str(e)}")


def buat_url(scheme, netloc, path="", params="", query="", fragment=""):
    """
    Buat URL dari komponen-komponennya.

    Args:
        scheme: Scheme (http, https, ftp, dll)
        netloc: Network location (domain:port)
        path: Path
        params: Parameters
        query: Query string
        fragment: Fragment

    Returns:
        str: URL lengkap
    """
    try:
        return python_urlparse.urlunparse((scheme, netloc, path, params, query, fragment))
    except Exception as e:
        raise ValueError(f"Gagal buat URL: {str(e)}")


def encode_url(params):
    """
    Encode parameter ke URL-encoded string.

    Args:
        params: Dictionary atau list of tuples

    Returns:
        str: URL-encoded string
    """
    try:
        if isinstance(params, dict):
            return python_urlparse.urlencode(params)
        elif isinstance(params, list):
            return python_urlparse.urlencode(params)
        else:
            raise ValueError("Params harus berupa dictionary atau list of tuples")
    except Exception as e:
        raise ValueError(f"Gagal encode URL: {str(e)}")


def decode_url(encoded_string):
    """
    Decode URL-encoded string.

    Args:
        encoded_string: URL-encoded string

    Returns:
        dict: Parameters sebagai dictionary
    """
    try:
        return dict(python_urlparse.parse_qsl(encoded_string))
    except Exception as e:
        raise ValueError(f"Gagal decode URL: {str(e)}")


def encode_component(component):
    """
    Encode URL component (khusus untuk path, query, dll).

    Args:
        component: String component untuk di-encode

    Returns:
        str: URL-encoded component
    """
    try:
        return python_urlparse.quote(str(component), safe="")
    except Exception as e:
        raise ValueError(f"Gagal encode component: {str(e)}")


def decode_component(encoded_component):
    """
    Decode URL component.

    Args:
        encoded_component: URL-encoded component

    Returns:
        str: Decoded component
    """
    try:
        return python_urlparse.unquote(encoded_component)
    except Exception as e:
        raise ValueError(f"Gagal decode component: {str(e)}")


def gabung_url(base_url, *paths):
    """
    Gabungkan base URL dengan path-path menggunakan proper URL joining.

    Args:
        base_url: Base URL
        *paths: Path-path untuk digabungkan

    Returns:
        str: URL lengkap
    """
    try:
        result = base_url
        for path in paths:
            result = python_urlparse.urljoin(result, str(path))
        return result
    except Exception as e:
        raise ValueError(f"Gagal gabung URL: {str(e)}")


def dapatkan_scheme(url):
    """Dapatkan scheme dari URL."""
    try:
        return python_urlparse.urlparse(url).scheme
    except Exception:
        return None


def dapatkan_domain(url):
    """Dapatkan domain/hostname dari URL."""
    try:
        return python_urlparse.urlparse(url).hostname
    except Exception:
        return None


def dapatkan_path(url):
    """Dapatkan path dari URL."""
    try:
        return python_urlparse.urlparse(url).path
    except Exception:
        return None


def dapatkan_query(url):
    """Dapatkan query string dari URL."""
    try:
        return python_urlparse.urlparse(url).query
    except Exception:
        return None


def parse_query(query_string):
    """
    Parse query string menjadi dictionary.

    Args:
        query_string: Query string

    Returns:
        dict: Parameters sebagai dictionary
    """
    try:
        return dict(python_urlparse.parse_qsl(query_string))
    except Exception as e:
        raise ValueError(f"Gagal parse query: {str(e)}")


def buat_query(params):
    """
    Buat query string dari dictionary.

    Args:
        params: Dictionary parameters

    Returns:
        str: Query string
    """
    try:
        return python_urlparse.urlencode(params)
    except Exception as e:
        raise ValueError(f"Gagal buat query: {str(e)}")


def url_valid(url):
    """
    Cek apakah URL valid.

    Args:
        url: URL untuk dicek

    Returns:
        bool: True jika URL valid
    """
    try:
        result = python_urlparse.urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def dapatkan_extension(path):
    """
    Dapatkan file extension dari path atau URL.

    Args:
        path: Path atau URL

    Returns:
        str: File extension (tanpa dot) atau None
    """
    try:
        _, ext = os.path.splitext(path)
        return ext[1:] if ext else None
    except Exception:
        return None


def dapatkan_filename(url):
    """
    Dapatkan filename dari URL.

    Args:
        url: URL

    Returns:
        str: Filename atau None
    """
    try:
        path = python_urlparse.urlparse(url).path
        filename = os.path.basename(path)
        return filename if filename else None
    except Exception:
        return None


def download_url(url, destination=None):
    """
    Download content dari URL.

    Args:
        url: URL untuk download
        destination: Path destination (jika None, return content)

    Returns:
        str: Content jika destination None, atau path file jika destination specified
    """
    try:
        with python_urlrequest.urlopen(url) as response:
            content = response.read()

        if destination:
            with open(destination, "wb") as file:
                file.write(content)
            return destination
        else:
            return content.decode("utf-8")
    except python_urlerror.URLError as e:
        raise ValueError(f"Gagal download URL: {str(e)}")
    except Exception as e:
        raise ValueError(f"Gagal download: {str(e)}")


def escape_url(url):
    """
    Escape URL untuk keamanan.

    Args:
        url: URL untuk di-escape

    Returns:
        str: Escaped URL
    """
    try:
        parsed = python_urlparse.urlparse(url)
        escaped_path = python_urlparse.quote(parsed.path)
        escaped_query = python_urlparse.quote(parsed.query, safe="=&?")

        return python_urlparse.urlunparse(
            (
                parsed.scheme,
                parsed.netloc,
                escaped_path,
                parsed.params,
                escaped_query,
                parsed.fragment,
            )
        )
    except Exception as e:
        raise ValueError(f"Gagal escape URL: {str(e)}")


# Daftar semua fungsi yang tersedia
__all__ = [
    "parse_url",
    "buat_url",
    "encode_url",
    "decode_url",
    "encode_component",
    "decode_component",
    "gabung_url",
    "dapatkan_scheme",
    "dapatkan_domain",
    "dapatkan_path",
    "dapatkan_query",
    "parse_query",
    "buat_query",
    "url_valid",
    "dapatkan_extension",
    "dapatkan_filename",
    "download_url",
    "escape_url",
]
