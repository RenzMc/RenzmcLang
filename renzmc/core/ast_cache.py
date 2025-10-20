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



import hashlib
import os
import pickle


class ASTCache:
    """
    AST Cache for storing and retrieving parsed Abstract Syntax Trees.

    This class manages a disk-based cache of parsed AST trees, using MD5
    hashing to identify unique source code versions. The cache automatically
    handles cache directory creation and provides simple load/save operations.

    Attributes:
        cache_dir: Directory path where cache files are stored
    """

    def __init__(self, cache_dir=".rmc_cache"):
        """
        Initialize the AST cache.

        Args:
            cache_dir: Directory path for storing cache files (default: .rmc_cache)
        """
        self.cache_dir = cache_dir

    def get_cache_key(self, source_code):
        """
        Generate a unique cache key for the given source code.

        Uses MD5 hashing to create a unique identifier for the source code.
        This key is used as the filename for the cached AST.

        Args:
            source_code: The source code string to hash

        Returns:
            A hexadecimal string representing the MD5 hash of the source code
        """
        return hashlib.md5(source_code.encode()).hexdigest()

    def load(self, key):
        """
        Load a cached AST from disk.

        Attempts to load a previously cached AST tree from the cache directory.
        Returns None if the cache file doesn't exist or if loading fails.

        Args:
            key: The cache key (hash) identifying the cached AST

        Returns:
            The cached AST tree if found, None otherwise
        """
        cache_file = os.path.join(self.cache_dir, f"{key}.ast")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                return None
        return None

    def save(self, key, ast):
        """
        Save an AST tree to the cache.

        Serializes the AST tree using pickle and saves it to the cache directory.
        Creates the cache directory if it doesn't exist.

        Args:
            key: The cache key (hash) to identify this cached AST
            ast: The AST tree to cache
        """
        os.makedirs(self.cache_dir, exist_ok=True)
        cache_file = os.path.join(self.cache_dir, f"{key}.ast")
        try:
            with open(cache_file, "wb") as f:
                pickle.dump(ast, f)
        except Exception:
            pass


__all__ = ["ASTCache"]
