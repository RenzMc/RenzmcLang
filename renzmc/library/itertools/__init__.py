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
RenzMcLang Itertools Library

Library untuk iterator operations dan utilities dengan fungsi-fungsi 
dalam bahasa Indonesia.
"""

import itertools as python_itertools
from collections import deque


def hitung(start=0, step=1):
    """
    Buat iterator yang menghitung dari start dengan step tertentu.

    Args:
        start: Nilai awal (default 0)
        step: Step increment (default 1)

    Returns:
        iterator: Count iterator
    """
    return python_itertools.count(start, step)


def siklus(iterable):
    """
    Buat iterator yang mengulang iterable secara infinit.

    Args:
        iterable: Iterable untuk diulang

    Returns:
        iterator: Cycle iterator
    """
    return python_itertools.cycle(iterable)


def ulangi(object, times=None):
    """
    Ulangi object sebanyak times (infinit jika None).

    Args:
        object: Object untuk diulang
        times: Jumlah pengulangan (None untuk infinit)

    Returns:
        iterator: Repeat iterator
    """
    return python_itertools.repeat(object, times)


def akumulasi(iterable, func=lambda x, y: x + y):
    """
    Buat iterator yang mengakumulasi hasil.

    Args:
        iterable: Iterable input
        func: Fungsi akumulasi (default penjumlahan)

    Returns:
        iterator: Accumulate iterator
    """
    return python_itertools.accumulate(iterable, func)


def rantai(*iterables):
    """
    Gabungkan beberapa iterables.

    Args:
        *iterables: Iterables untuk digabungkan

    Returns:
        iterator: Chained iterator
    """
    return python_itertools.chain(*iterables)


def rantai_dari_iterable(iterable):
    """
    Gabungkan iterable dari iterable.

    Args:
        iterable: Iterable yang berisi iterables

    Returns:
        iterator: Chained iterator
    """
    return python_itertools.chain.from_iterable(iterable)


def kompres(data, selectors):
    """
    Kompres data dengan selectors (hanya items yang selectors-nya True).

    Args:
        data: Data iterable
        selectors: Selector iterable (boolean)

    Returns:
        iterator: Compressed iterator
    """
    return python_itertools.compress(data, selectors)


def teteskan(iterable, n):
    """
    Buat iterator yang "meneteskan" item setiap n iterasi.

    Args:
        iterable: Input iterable
        n: Drop rate

    Returns:
        iterator: Dropwhile iterator
    """
    return (
        python_itertools.dropwhile(lambda x: True, iterable)
        if n <= 1
        else python_itertools.islice(iterable, 0, None, n)
    )


def filterfalse(predicate, iterable):
    """
    Filter items yang predicate-nya False.

    Args:
        predicate: Fungsi predicate
        iterable: Input iterable

    Returns:
        iterator: Filterfalse iterator
    """
    return python_itertools.filterfalse(predicate, iterable)


def grupby(iterable, key=None):
    """
    Group consecutive items yang sama.

    Args:
        iterable: Input iterable
        key: Key function untuk grouping

    Returns:
        iterator: Groupby iterator
    """
    return python_itertools.groupby(iterable, key)


def islice(iterable, start, stop=None, step=1):
    """
    Slice iterator seperti list slicing.

    Args:
        iterable: Input iterable
        start: Start index
        stop: Stop index (None untuk sampai akhir)
        step: Step (default 1)

    Returns:
        iterator: Isliced iterator
    """
    if stop is None:
        return python_itertools.islice(iterable, start, None, step)
    return python_itertools.islice(iterable, start, stop, step)


def perpanjang(iterable, fillvalue=None):
    """
    Tambahkan fillvalue ke iterable untuk membuat panjang yang sama.

    Args:
        iterable: Input iterable
        fillvalue: Nilai untuk pengisi

    Returns:
        iterator: Extended iterator
    """

    # Python's itertools tidak punya extend, kita implement sendiri
    class ExtendedIterator:
        def __init__(self, it, fillvalue):
            self.it = iter(it)
            self.fillvalue = fillvalue
            self.exhausted = False

        def __iter__(self):
            return self

        def __next__(self):
            if not self.exhausted:
                try:
                    return next(self.it)
                except StopIteration:
                    self.exhausted = True
                    return self.fillvalue
            return self.fillvalue

    return ExtendedIterator(iterable, fillvalue)


def zip_longest(*iterables, fillvalue=None):
    """
    Zip iterables dengan panjang berbeda, isi dengan fillvalue.

    Args:
        *iterables: Iterables untuk di-zip
        fillvalue: Nilai untuk pengisi (default None)

    Returns:
        iterator: Zipped longest iterator
    """
    return python_itertools.zip_longest(*iterables, fillvalue=fillvalue)


def produk(*iterables, repeat=1):
    """
    Cartesian product dari iterables.

    Args:
        *iterables: Input iterables
        repeat: Jumlah repeat (default 1)

    Returns:
        iterator: Product iterator
    """
    return python_itertools.product(*iterables, repeat=repeat)


def permutasi(iterable, r=None):
    """
    Generate permutasi dari iterable.

    Args:
        iterable: Input iterable
        r: Panjang permutasi (default panjang iterable)

    Returns:
        iterator: Permutation iterator
    """
    return python_itertools.permutations(iterable, r)


def kombinasi(iterable, r):
    """
    Generate kombinasi dari iterable.

    Args:
        iterable: Input iterable
        r: Panjang kombinasi

    Returns:
        iterator: Combination iterator
    """
    return python_itertools.combinations(iterable, r)


def kombinasi_dengan_pengulangan(iterable, r):
    """
    Generate kombinasi dengan pengulangan.

    Args:
        iterable: Input iterable
        r: Panjang kombinasi

    Returns:
        iterator: Combination with replacement iterator
    """
    return python_itertools.combinations_with_replacement(iterable, r)


def ambil_while(predicate, iterable):
    """
    Ambil items selama predicate True.

    Args:
        predicate: Fungsi predicate
        iterable: Input iterable

    Returns:
        iterator: Takewhile iterator
    """
    return python_itertools.takewhile(predicate, iterable)


def filter_tee(iterable, n=2):
    """
    Bagi iterator menjadi n iterator independen.

    Args:
        iterable: Input iterable
        n: Jumlah iterator (default 2)

    Returns:
        tuple: Tuple of n iterators
    """
    return python_itertools.tee(iterable, n)


def konsumsi(iterator, n=None):
    """
    Konsumsi n items dari iterator.

    Args:
        iterator: Input iterator
        n: Jumlah items untuk dikonsumsi (None untuk semua)
    """
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(python_itertools.islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    """
    Dapatkan item ke-n dari iterable.

    Args:
        iterable: Input iterable
        n: Index item
        default: Default value jika index out of range

    Returns:
        Item ke-n atau default
    """
    return next(python_itertools.islice(iterable, n, None), default)


def quantify(iterable, pred=bool):
    """
    Hitung jumlah items yang bernilai True.

    Args:
        iterable: Input iterable
        pred: Predicate function (default bool)

    Returns:
        int: Jumlah True items
    """
    return sum(1 for item in iterable if pred(item))


def batched(iterable, n):
    """
    Bagi iterable ke dalam batches dengan ukuran n.

    Args:
        iterable: Input iterable
        n: Ukuran batch

    Returns:
        iterator: Batch iterator
    """

    # Python 3.12+ punya itertools.batched, kita implement manual
    class BatchedIterator:
        def __init__(self, it, n):
            self.it = iter(it)
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            batch = list(python_itertools.islice(self.it, self.n))
            if not batch:
                raise StopIteration
            return batch

    return BatchedIterator(iterable, n)


def sliding_window(iterable, n):
    """
    Buat sliding windows dengan ukuran n.

    Args:
        iterable: Input iterable
        n: Ukuran window

    Returns:
        iterator: Sliding window iterator
    """

    # Implement manual sliding window
    class SlidingWindowIterator:
        def __init__(self, it, n):
            self.it = iter(it)
            self.n = n
            self.window = deque(maxlen=n)
            # Fill initial window
            for _ in range(n):
                try:
                    self.window.append(next(self.it))
                except StopIteration:
                    break

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.window) < self.n:
                raise StopIteration

            result = list(self.window)
            try:
                self.window.append(next(self.it))
            except StopIteration:
                pass

            return result

    return SlidingWindowIterator(iterable, n)


def pairwise(iterable):
    """
    Buat pairs dari consecutive items.

    Args:
        iterable: Input iterable

    Returns:
        iterator: Pairwise iterator
    """
    return python_itertools.pairwise(iterable)


def roundrobin(*iterables):
    """
    Round-robin schedule dari iterables.

    Args:
        *iterables: Input iterables

    Returns:
        iterator: Round-robin iterator
    """

    # Python tidak punya roundrobin bawaan, implement manual
    class RoundRobinIterator:
        def __init__(self, *iterables):
            self.iterables = [iter(it) for it in iterables]
            self.active = list(range(len(self.iterables)))

        def __iter__(self):
            return self

        def __next__(self):
            while self.active:
                for i in list(self.active):
                    try:
                        item = next(self.iterables[i])
                        return item
                    except StopIteration:
                        self.active.remove(i)
            raise StopIteration

    return RoundRobinIterator(*iterables)


def flatten(iterable):
    """
    Flatten nested iterable (satu level).

    Args:
        iterable: Nested iterable

    Returns:
        iterator: Flattened iterator
    """
    for item in iterable:
        if isinstance(item, (list, tuple, set)):
            for subitem in item:
                yield subitem
        else:
            yield item


def chunked(iterable, n):
    """
    Bagi iterable ke dalam chunks dengan ukuran n.

    Args:
        iterable: Input iterable
        n: Ukuran chunk

    Returns:
        iterator: Chunk iterator
    """
    iterator = iter(iterable)
    while True:
        chunk = list(python_itertools.islice(iterator, n))
        if not chunk:
            break
        yield chunk


def interleave(*iterables):
    """
    Interleave beberapa iterables.

    Args:
        *iterables: Input iterables

    Returns:
        iterator: Interleaved iterator
    """
    return roundrobin(*iterables)


# Daftar semua fungsi yang tersedia
__all__ = [
    "hitung",
    "siklus",
    "ulangi",
    "akumulasi",
    "rantai",
    "rantai_dari_iterable",
    "kompres",
    "teteskan",
    "filterfalse",
    "grupby",
    "islice",
    "perpanjang",
    "zip_longest",
    "produk",
    "permutasi",
    "kombinasi",
    "kombinasi_dengan_pengulangan",
    "ambil_while",
    "filter_tee",
    "konsumsi",
    "nth",
    "quantify",
    "batched",
    "sliding_window",
    "pairwise",
    "roundrobin",
    "flatten",
    "chunked",
    "interleave",
]
