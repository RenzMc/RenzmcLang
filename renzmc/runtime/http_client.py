"""
Built-in HTTP Client untuk RenzMcLang
Native HTTP client tanpa perlu import Python libraries
"""

import requests
import json as json_lib
from typing import Dict, Any, Optional

class HTTPResponse:
    """HTTP Response wrapper"""
    
    def __init__(self, response):
        self._response = response
        self.status_code = response.status_code
        self.headers = dict(response.headers)
        self.text = response.text
        self.url = response.url
        
    def json(self):
        """Parse response as JSON"""
        try:
            return self._response.json()
        except Exception as e:
            raise ValueError(f"Gagal parse JSON: {e}")
    
    def ok(self):
        """Check if request was successful"""
        return 200 <= self.status_code < 300
    
    def __str__(self):
        return f"<HTTPResponse [{self.status_code}]>"
    
    def __repr__(self):
        return self.__str__()

class HTTPClient:
    """Built-in HTTP Client"""
    
    def __init__(self):
        self.session = requests.Session()
        self.default_timeout = 30
        self.default_headers = {
            'User-Agent': 'RenzMcLang/0.0.3'
        }
    
    def get(self, url: str, params: Optional[Dict] = None, 
            headers: Optional[Dict] = None, timeout: Optional[int] = None) -> HTTPResponse:
        """HTTP GET request"""
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.get(
                url,
                params=params,
                headers=merged_headers,
                timeout=timeout or self.default_timeout
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP GET error: {e}")
    
    def post(self, url: str, data: Optional[Any] = None, 
             json: Optional[Dict] = None, headers: Optional[Dict] = None,
             timeout: Optional[int] = None) -> HTTPResponse:
        """HTTP POST request"""
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.post(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP POST error: {e}")
    
    def put(self, url: str, data: Optional[Any] = None,
            json: Optional[Dict] = None, headers: Optional[Dict] = None,
            timeout: Optional[int] = None) -> HTTPResponse:
        """HTTP PUT request"""
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.put(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP PUT error: {e}")
    
    def delete(self, url: str, headers: Optional[Dict] = None,
               timeout: Optional[int] = None) -> HTTPResponse:
        """HTTP DELETE request"""
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.delete(
                url,
                headers=merged_headers,
                timeout=timeout or self.default_timeout
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP DELETE error: {e}")
    
    def patch(self, url: str, data: Optional[Any] = None,
              json: Optional[Dict] = None, headers: Optional[Dict] = None,
              timeout: Optional[int] = None) -> HTTPResponse:
        """HTTP PATCH request"""
        try:
            merged_headers = {**self.default_headers, **(headers or {})}
            response = self.session.patch(
                url,
                data=data,
                json=json,
                headers=merged_headers,
                timeout=timeout or self.default_timeout
            )
            return HTTPResponse(response)
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timeout setelah {timeout or self.default_timeout} detik")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Gagal terhubung ke {url}")
        except Exception as e:
            raise RuntimeError(f"HTTP PATCH error: {e}")
    
    def set_header(self, key: str, value: str):
        """Set default header"""
        self.default_headers[key] = value
    
    def set_timeout(self, timeout: int):
        """Set default timeout"""
        self.default_timeout = timeout

# Global HTTP client instance
_http_client = HTTPClient()

# Convenience functions
def http_get(url: str, **kwargs) -> HTTPResponse:
    """HTTP GET request"""
    return _http_client.get(url, **kwargs)

def http_post(url: str, **kwargs) -> HTTPResponse:
    """HTTP POST request"""
    return _http_client.post(url, **kwargs)

def http_put(url: str, **kwargs) -> HTTPResponse:
    """HTTP PUT request"""
    return _http_client.put(url, **kwargs)

def http_delete(url: str, **kwargs) -> HTTPResponse:
    """HTTP DELETE request"""
    return _http_client.delete(url, **kwargs)

def http_patch(url: str, **kwargs) -> HTTPResponse:
    """HTTP PATCH request"""
    return _http_client.patch(url, **kwargs)

def http_set_header(key: str, value: str):
    """Set default HTTP header"""
    _http_client.set_header(key, value)

def http_set_timeout(timeout: int):
    """Set default HTTP timeout"""
    _http_client.set_timeout(timeout)