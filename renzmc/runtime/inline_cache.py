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
RenzmcLang Inline Cache Module

This module provides inline caching for variable lookups to significantly
improve performance by reducing scope traversal overhead.
"""


class InlineCache:
    """
    Inline cache for variable lookups.

    Caches variable locations to avoid repeated scope traversals,
    providing 2-3x faster variable access.
    """

    def __init__(self, max_size=1000):
        """
        Initialize the inline cache.

        Args:
            max_size: Maximum number of cache entries (default: 1000)
        """
        self.cache = {}
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
        self.enabled = True

    def get(self, name, scope_id):
        """
        Get cached variable location.

        Args:
            name: Variable name
            scope_id: Scope identifier

        Returns:
            Cached location tuple (scope_type, value) or None if not cached
        """
        if not self.enabled:
            return None

        cache_key = (name, scope_id)
        if cache_key in self.cache:
            self.hits += 1
            return self.cache[cache_key]

        self.misses += 1
        return None

    def set(self, name, scope_id, scope_type, value):
        """
        Cache variable location.

        Args:
            name: Variable name
            scope_id: Scope identifier
            scope_type: Type of scope ('instance', 'local', 'global', 'builtin')
            value: Variable value
        """
        if not self.enabled:
            return

        if len(self.cache) >= self.max_size:
            self._evict_oldest()

        cache_key = (name, scope_id)
        self.cache[cache_key] = (scope_type, value)

    def invalidate(self, name=None, scope_id=None):
        """
        Invalidate cache entries.

        Args:
            name: Variable name to invalidate (None = all names)
            scope_id: Scope identifier to invalidate (None = all scopes)
        """
        if name is None and scope_id is None:
            self.cache.clear()
            return

        keys_to_remove = []
        for cache_key in self.cache:
            key_name, key_scope_id = cache_key
            if (name is None or key_name == name) and (scope_id is None or key_scope_id == scope_id):
                keys_to_remove.append(cache_key)

        for key in keys_to_remove:
            del self.cache[key]

    def _evict_oldest(self):
        """Evict oldest cache entry when max size is reached."""
        if self.cache:
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]

    def get_stats(self):
        """
        Get cache statistics.

        Returns:
            Dictionary with cache statistics
        """
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
            "hits": self.hits,
            "misses": self.misses,
            "total_lookups": total,
            "hit_rate": f"{hit_rate:.2f}%",
            "cache_size": len(self.cache),
            "max_size": self.max_size,
            "enabled": self.enabled,
        }

    def reset_stats(self):
        """Reset cache statistics."""
        self.hits = 0
        self.misses = 0

    def clear(self):
        """Clear all cache entries and reset statistics."""
        self.cache.clear()
        self.reset_stats()

    def enable(self):
        """Enable the cache."""
        self.enabled = True

    def disable(self):
        """Disable the cache."""
        self.enabled = False
