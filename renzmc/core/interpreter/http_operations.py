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
RenzmcLang Interpreter HTTP Operations Module

This module contains HTTP request functionality.
"""


class HTTPOperationsMixin:
    """
    Mixin class for HTTP operations functionality.

    Provides methods for making HTTP requests.
    """

    def _http_request(
        self, url, method="GET", headers=None, data=None, json=None, timeout=30
    ):
        """
        Make an HTTP request.

        Args:
            url: Request URL
            method: HTTP method
            headers: Request headers
            data: Request data
            json: JSON data
            timeout: Request timeout

        Returns:
            Response dictionary

        Raises:
            ImportError: If requests module not available
            ValueError: If request fails
        """
        try:
            import requests

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                json=json,
                timeout=timeout,
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP request: {str(e)}")

    def _http_get(self, url, headers=None, params=None, timeout=30):
        """
        Make an HTTP GET request.

        Args:
            url: Request URL
            headers: Request headers
            params: Query parameters
            timeout: Request timeout

        Returns:
            Response dictionary

        Raises:
            ImportError: If requests module not available
            ValueError: If request fails
        """
        try:
            import requests

            response = requests.get(
                url, headers=headers, params=params, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP GET request: {str(e)}")

    def _http_post(self, url, headers=None, data=None, json=None, timeout=30):
        """
        Make an HTTP POST request.

        Args:
            url: Request URL
            headers: Request headers
            data: Request data
            json: JSON data
            timeout: Request timeout

        Returns:
            Response dictionary

        Raises:
            ImportError: If requests module not available
            ValueError: If request fails
        """
        try:
            import requests

            response = requests.post(
                url, headers=headers, data=data, json=json, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP POST request: {str(e)}")

    def _http_put(self, url, headers=None, data=None, json=None, timeout=30):
        """
        Make an HTTP PUT request.

        Args:
            url: Request URL
            headers: Request headers
            data: Request data
            json: JSON data
            timeout: Request timeout

        Returns:
            Response dictionary

        Raises:
            ImportError: If requests module not available
            ValueError: If request fails
        """
        try:
            import requests

            response = requests.put(
                url, headers=headers, data=data, json=json, timeout=timeout
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP PUT request: {str(e)}")

    def _http_delete(self, url, headers=None, timeout=30):
        """
        Make an HTTP DELETE request.

        Args:
            url: Request URL
            headers: Request headers
            timeout: Request timeout

        Returns:
            Response dictionary

        Raises:
            ImportError: If requests module not available
            ValueError: If request fails
        """
        try:
            import requests

            response = requests.delete(url, headers=headers, timeout=timeout)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": (
                    response.json()
                    if response.headers.get("content-type", "").startswith(
                        "application/json"
                    )
                    else None
                ),
                "content": response.content,
            }
        except ImportError:
            raise ImportError(
                "Modul 'requests' tidak terinstal. Silakan instal dengan 'pip install requests'"
            )
        except Exception as e:
            raise ValueError(f"Gagal melakukan HTTP DELETE request: {str(e)}")
