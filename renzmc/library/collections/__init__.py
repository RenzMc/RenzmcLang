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
RenzMcLang Collections Library

Library untuk advanced data structures dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

from collections import defaultdict as python_defaultdict
from collections import OrderedDict as python_ordereddict
from collections import Counter as python_counter
from collections import deque as python_deque
from collections import ChainMap as python_chainmap
from collections import namedtuple as python_namedtuple
from collections import UserDict, UserList, UserString
import math


class Antrian(python_deque):
    """
    Class untuk queue (antrian) dengan operasi FIFO.
    """

    def __init__(self, iterable=None):
        """
        Inisialisasi antrian.

        Args:
            iterable: Iterable awal (opsional)
        """
        super().__init__(iterable or [])

    def masuk(self, item):
        """
        Tambah item ke belakang antrian.

        Args:
            item: Item untuk ditambahkan
        """
        self.append(item)

    def keluar(self):
        """
        Ambil item dari depan antrian.

        Returns:
            Item dari depan antrian
        """
        if not self:
            raise IndexError("Antrian kosong")
        return self.popleft()

    def lihat_depan(self):
        """
        Lihat item di depan antrian tanpa menghapus.

        Returns:
            Item di depan antrian
        """
        if not self:
            raise IndexError("Antrian kosong")
        return self[0]

    def lihat_belakang(self):
        """
        Lihat item di belakang antrian tanpa menghapus.

        Returns:
            Item di belakang antrian
        """
        if not self:
            raise IndexError("Antrian kosong")
        return self[-1]

    def kosong(self):
        """
        Cek apakah antrian kosong.

        Returns:
            bool: True jika kosong
        """
        return len(self) == 0

    def ukuran(self):
        """
        Dapatkan ukuran antrian.

        Returns:
            int: Ukuran antrian
        """
        return len(self)


class Tumpukan(python_deque):
    """
    Class untuk stack (tumpukan) dengan operasi LIFO.
    """

    def __init__(self, iterable=None):
        """
        Inisialisasi tumpukan.

        Args:
            iterable: Iterable awal (opsional)
        """
        super().__init__(iterable or [])

    def dorong(self, item):
        """
        Push item ke atas tumpukan.

        Args:
            item: Item untuk didorong
        """
        self.append(item)

    def ambil(self):
        """
        Pop item dari atas tumpukan.

        Returns:
            Item dari atas tumpukan
        """
        if not self:
            raise IndexError("Tumpukan kosong")
        return self.pop()

    def lihat_atas(self):
        """
        Lihat item di atas tumpukan tanpa menghapus.

        Returns:
            Item di atas tumpukan
        """
        if not self:
            raise IndexError("Tumpukan kosong")
        return self[-1]

    def kosong(self):
        """
        Cek apakah tumpukan kosong.

        Returns:
            bool: True jika kosong
        """
        return len(self) == 0

    def ukuran(self):
        """
        Dapatkan ukuran tumpukan.

        Returns:
            int: Ukuran tumpukan
        """
        return len(self)


class DefaultDict(python_defaultdict):
    """
    Class untuk defaultdict dengan factory function.
    """

    def __init__(self, default_factory=None, **kwargs):
        """
        Inisialisasi defaultdict.

        Args:
            default_factory: Factory function untuk default value
            **kwargs: Initial key-value pairs
        """
        super().__init__(default_factory)
        self.update(kwargs)

    def dapatkan(self, key, default=None):
        """
        Dapatkan nilai dengan default.

        Args:
            key: Key untuk dicari
            default: Default value jika key tidak ada

        Returns:
            Value atau default
        """
        return self[key] if key in self else default

    def set_default(self, key, default=None):
        """
        Set default value untuk key.

        Args:
            key: Key
            default: Default value

        Returns:
            Value dari key
        """
        return self.setdefault(key, default)


class OrderedDict(python_ordereddict):
    """
    Class untuk ordered dictionary (memperhatikan urutan insertion).
    """

    def __init__(self, *args, **kwargs):
        """
        Inisialisasi ordered dictionary.
        """
        super().__init__(*args, **kwargs)

    def dapatkan_kunci_pertama(self):
        """Dapatkan key pertama."""
        return next(iter(self)) if self else None

    def dapatkan_kunci_terakhir(self):
        """Dapatkan key terakhir."""
        return next(reversed(self)) if self else None

    def pindah_ke_akhir(self, key, last=True):
        """
        Pindah key ke akhir.

        Args:
            key: Key untuk dipindahkan
            last: True untuk pindah ke akhir
        """
        self.move_to_end(key, last=last)

    def pop_item(self, last=True):
        """
        Pop item (key, value).

        Args:
            last: True untuk pop dari akhir

        Returns:
            tuple: (key, value)
        """
        return self.popitem(last=last)


class Counter(python_counter):
    """
    Class untuk counter (multiset).
    """

    def __init__(self, iterable=None, **kwargs):
        """
        Inisialisasi counter.

        Args:
            iterable: Iterable untuk dihitung
            **kwargs: Initial counts
        """
        super().__init__(iterable or [], **kwargs)

    def paling_umum(self, n=None):
        """
        Dapatkan n elements yang paling umum.

        Args:
            n: Jumlah elements (None untuk semua)

        Returns:
            list: List (element, count)
        """
        return self.most_common(n)

    def tambah(self, iterable=None, **kwargs):
        """
        Tambah counts.

        Args:
            iterable: Iterable untuk ditambahkan
            **kwargs: Counts untuk ditambahkan
        """
        if iterable:
            self.update(iterable)
        if kwargs:
            self.update(kwargs)

    def kurangi(self, iterable=None, **kwargs):
        """
        Kurangi counts.

        Args:
            iterable: Iterable untuk dikurangi
            **kwargs: Counts untuk dikurangi
        """
        if iterable:
            self.subtract(iterable)
        if kwargs:
            self.subtract(kwargs)

    def hitung_total(self):
        """
        Hitung total semua counts.

        Returns:
            int: Total counts
        """
        return sum(self.values())

    def dapatkan_elements(self):
        """
        Dapatkan semua unique elements.

        Returns:
            list: List elements
        """
        return list(self.elements())


class RantaiMap(python_chainmap):
    """
    Class untuk chain map (multiple maps viewed as single map).
    """

    def __init__(self, *maps):
        """
        Inisialisasi chain map.

        Args:
            *maps: Maps untuk di-chain
        """
        super().__init__(*maps)

    def dapatkan_peta(self):
        """
        Dapatkan semua maps.

        Returns:
            list: List maps
        """
        return self.maps

    def tambah_peta(self, map):
        """
        Tambah map ke depan chain.

        Args:
            map: Map untuk ditambahkan
        """
        self.maps = [map] + self.maps

    def buat_child(self, **kwargs):
        """
        Buat child chain map.

        Args:
            **kwargs: Additional mappings

        Returns:
            ChainMap: Child chain map
        """
        return self.new_child(**kwargs)


class NamedTuple:
    """
    Class factory untuk named tuple.
    """

    def __init__(self, typename, field_names):
        """
        Inisialisasi named tuple.

        Args:
            typename: Nama type
            field_names: List field names
        """
        self._typename = typename
        self._field_names = (
            field_names
            if isinstance(field_names, (list, tuple))
            else field_names.replace(",", " ").split()
        )
        self._cls = python_namedtuple(typename, self._field_names)

    def buat(self, *args, **kwargs):
        """
        Buat instance named tuple.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Named tuple instance
        """
        return self._cls(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.buat(*args, **kwargs)

    @property
    def fields(self):
        """Dapatkan field names."""
        return self._field_names

    @property
    def typename(self):
        """Dapatkan type name."""
        return self._typename


def buat_antrian(iterable=None):
    """
    Buat antrian baru.

    Args:
        iterable: Iterable awal

    Returns:
        Antrian: Antrian baru
    """
    return Antrian(iterable)


def buat_tumpukan(iterable=None):
    """
    Buat tumpukan baru.

    Args:
        iterable: Iterable awal

    Returns:
        Tumpukan: Tumpukan baru
    """
    return Tumpukan(iterable)


def buat_defaultdict(default_factory=None, **kwargs):
    """
    Buat defaultdict baru.

    Args:
        default_factory: Factory function
        **kwargs: Initial items

    Returns:
        DefaultDict: DefaultDict baru
    """
    return DefaultDict(default_factory, **kwargs)


def buat_ordered_dict(*args, **kwargs):
    """
    Buat ordered dict baru.

    Args:
        *args: Arguments
        **kwargs: Keyword arguments

    Returns:
        OrderedDict: Ordered dict baru
    """
    return OrderedDict(*args, **kwargs)


def buat_counter(iterable=None, **kwargs):
    """
    Buat counter baru.

    Args:
        iterable: Iterable untuk dihitung
        **kwargs: Initial counts

    Returns:
        Counter: Counter baru
    """
    return Counter(iterable, **kwargs)


def buat_named_tuple(typename, field_names):
    """
    Buat named tuple class.

    Args:
        typename: Nama type
        field_names: Field names

    Returns:
        NamedTuple: Named tuple factory
    """
    return NamedTuple(typename, field_names)


def buat_chain_map(*maps):
    """
    Buat chain map baru.

    Args:
        *maps: Maps untuk di-chain

    Returns:
        ChainMap: Chain map baru
    """
    return RantaiMap(*maps)


def deque_siklus(iterable, maxlen=None):
    """
    Buat deque dengan cyclic behavior.

    Args:
        iterable: Iterable awal
        maxlen: Maximum length

    Returns:
        deque: Deque baru
    """
    dq = python_deque(iterable, maxlen)
    return dq


def heapify(list_items):
    """
    Konversi list ke heap.

    Args:
        list_items: List untuk di-heapify
    """
    import heapq

    heapq.heapify(list_items)


def heappush(heap, item):
    """
    Push item ke heap.

    Args:
        heap: Heap list
        item: Item untuk di-push
    """
    import heapq

    heapq.heappush(heap, item)


def heappop(heap):
    """
    Pop smallest item dari heap.

    Args:
        heap: Heap list

    Returns:
        Smallest item
    """
    import heapq

    return heapq.heappop(heap)


def heappushpop(heap, item):
    """
    Push item lalu pop smallest.

    Args:
        heap: Heap list
        item: Item untuk di-push

    Returns:
        Smallest item
    """
    import heapq

    return heapq.heappushpop(heap, item)


def heapreplace(heap, item):
    """
    Pop smallest lalu push item.

    Args:
        heap: Heap list
        item: Item untuk di-push

    Returns:
        Smallest item
    """
    import heapq

    return heapq.heapreplace(heap, item)


def nlargest(n, iterable, key=None):
    """
    Dapatkan n largest items.

    Args:
        n: Jumlah items
        iterable: Input iterable
        key: Key function

    Returns:
        list: N largest items
    """
    import heapq

    return heapq.nlargest(n, iterable, key)


def nsmallest(n, iterable, key=None):
    """
    Dapatkan n smallest items.

    Args:
        n: Jumlah items
        iterable: Input iterable
        key: Key function

    Returns:
        list: N smallest items
    """
    import heapq

    return heapq.nsmallest(n, iterable, key)


# Daftar semua fungsi yang tersedia
__all__ = [
    "Antrian",
    "Tumpukan",
    "DefaultDict",
    "OrderedDict",
    "Counter",
    "RantaiMap",
    "NamedTuple",
    "buat_antrian",
    "buat_tumpukan",
    "buat_defaultdict",
    "buat_ordered_dict",
    "buat_counter",
    "buat_named_tuple",
    "buat_chain_map",
    "deque_siklus",
    "heapify",
    "heappush",
    "heappop",
    "heappushpop",
    "heapreplace",
    "nlargest",
    "nsmallest",
]
