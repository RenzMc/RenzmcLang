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
RenzMcLang Standard Library

The standard library provides essential modules for common programming tasks,
following Python's standard library design principles but adapted for
RenzMcLang with Indonesian function names and comprehensive documentation.

Available Modules:
- math: Mathematical functions and constants
- os: Operating system interface
- pathlib: Object-oriented path manipulation
- datetime: Date and time operations
- collections: Advanced data structures
- itertools: Iterator utilities
- statistics: Statistical functions
- random: Random number generation
- string: String operations and constants
- re: Regular expressions
- urllib: URL handling utilities
- http: HTTP client functionality
- hashlib: Hash functions
- base64: Base64 encoding/decoding
- uuid: UUID generation
- fileio: File I/O operations

Usage:
    # Import specific functions
    dari math impor sin, cos, tan
    
    # Import entire module
    impor math
    
    # Use functions
    hasil itu math.sin(0.5)
"""

from renzmc.library import fileio
from renzmc.library import uuid
from renzmc.library import base64
from renzmc.library import hashlib
from renzmc.library import http
from renzmc.library import urllib
from renzmc.library import re
from renzmc.library import string
from renzmc.library import random
from renzmc.library import statistics
from renzmc.library import itertools
from renzmc.library import collections
from renzmc.library import datetime
from renzmc.library import pathlib
from renzmc.library import os
from renzmc.library import math

__version__ = "1.0.0"
__author__ = "RenzMc"

# Import all submodules for easy access

__all__ = [
    "math",
    "os",
    "pathlib",
    "datetime",
    "collections",
    "itertools",
    "statistics",
    "random",
    "string",
    "re",
    "urllib",
    "http",
    "hashlib",
    "base64",
    "uuid",
    "fileio",
]
