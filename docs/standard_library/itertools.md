# Library Itertools

## Overview

Library `itertools` menyediakan fungsi-fungsi untuk operasi iterator yang efisien dan memory-friendly. Library ini mengimplementasikan iterator pattern untuk pengolahan data streams, kombinasi, permutasi, dan operasi sequence lainnya tanpa memuat seluruh data ke memory.

## Import Library

```python
dari renzmc.library.itertools impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.itertools impor hitung, siklus, produk, permutasi
```

## Iterator Infinit

### hitung(start=0, step=1)

Membuat iterator yang menghitung dari nilai start dengan step tertentu secara infinit.

**Parameter:**
- `start` (number): Nilai awal (default 0)
- `step` (number): Step increment (default 1)

**Return:**
- `iterator`: Count iterator infinit

**Contoh:**
```python
// Count dari 0
counter itu hitung()
untuk i dalam range(5):
    nilai itu next(counter)
    tampilkan nilai  // Output: 0, 1, 2, 3, 4

// Count dari 10 dengan step 2
counter2 itu hitung(10, 2)
untuk i dalam range(5):
    nilai itu next(counter2)
    tampilkan nilai  // Output: 10, 12, 14, 16, 18
```

### siklus(iterable)

Membuat iterator yang mengulang iterable secara infinit.

**Parameter:**
- `iterable`: Iterable untuk diulang

**Return:**
- `iterator`: Cycle iterator infinit

**Contoh:**
```python
// Cycle list
colors itu ["merah", "hijau", "biru"]
color_cycle itu siklus(colors)

untuk i dalam range(7):
    color itu next(color_cycle)
    tampilkan color  // Output: merah, hijau, biru, merah, hijau, biru, merah

// Cycle string
alphabet_cycle itu siklus("ABC")
untuk i dalam range(5):
    char itu next(alphabet_cycle)
    tampilkan char  // Output: A, B, C, A, B
```

### ulangi(object, times=None)

Mengulang object sebanyak times (infinit jika None).

**Parameter:**
- `object`: Object untuk diulang
- `times` (int): Jumlah pengulangan (None untuk infinit)

**Return:**
- `iterator`: Repeat iterator

**Contoh:**
```python
// Ulangi 3 kali
repeat_three itu ulangi("Hello", 3)
untuk item dalam repeat_three:
    tampilkan item  // Output: Hello, Hello, Hello

// Ulangi infinit (gunakan dengan care!)
repeat_infinit itu ulangi(42)
untuk i dalam range(5):
    nilai itu next(repeat_infinit)
    tampilkan nilai  // Output: 42, 42, 42, 42, 42
```

## Iterator Akumulasi

### akumulasi(iterable, func=lambda x, y: x + y)

Membuat iterator yang mengakumulasi hasil dengan fungsi tertentu.

**Parameter:**
- `iterable`: Iterable input
- `func` (function): Fungsi akumulasi (default penjumlahan)

**Return:**
- `iterator`: Accumulate iterator

**Contoh:**
```python
// Akumulasi penjumlahan
numbers itu [1, 2, 3, 4, 5]
sum_acc itu akumulasi(numbers)
list_sum itu list(sum_acc)  // [1, 3, 6, 10, 15]

// Akumulasi perkalian
mult_acc itu akumulasi(numbers, lambda x, y: x * y)
list_mult itu list(mult_acc)  // [1, 2, 6, 24, 120]

// Akumulasi maksimum
max_acc itu akumulasi(numbers, max)
list_max itu list(max_acc)  // [1, 2, 3, 4, 5]
```

## Iterator Chaining dan Filtering

### rantai(*iterables)

Menggabungkan beberapa iterables menjadi satu iterator.

**Parameter:**
- `*iterables`: Iterables untuk digabungkan

**Return:**
- `iterator`: Chained iterator

**Contoh:**
```python
// Chain lists
list1 itu [1, 2, 3]
list2 itu [4, 5, 6]
list3 itu [7, 8, 9]

chained itu rantai(list1, list2, list3)
result itu list(chained)  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Chain berbagai tipe
mixed_chain itu rantai([1, 2], "AB", (3, 4))
tampilkan list(mixed_chain)  // [1, 2, 'A', 'B', 3, 4]
```

### rantai_dari_iterable(iterable)

Menggabungkan iterable dari iterable.

**Parameter:**
- `iterable`: Iterable yang berisi iterables

**Return:**
- `iterator`: Chained iterator

**Contoh:**
```python
// Chain dari list of lists
lists itu [[1, 2], [3, 4], [5, 6]]
chained itu rantai_dari_iterable(lists)
result itu list(chained)  // [1, 2, 3, 4, 5, 6]

// Chain dari generator
def get_lists():
    hasil [i, i+1] untuk i dalam range(0, 6, 2)

chained_gen itu rantai_dari_iterable(get_lists())
tampilkan list(chained_gen)  // [0, 1, 2, 3, 4, 5]
```

### kompres(data, selectors)

Memfilter data dengan selectors (hanya items yang selectors-nya True).

**Parameter:**
- `data`: Data iterable
- `selectors`: Selector iterable (boolean)

**Return:**
- `iterator`: Compressed iterator

**Contoh:**
```python
data itu ["A", "B", "C", "D", "E"]
selectors itu [True, False, True, False, True]

compressed itu kompres(data, selectors)
result itu list(compressed)  // ["A", "C", "E"]

// Filter numbers > 5
numbers itu [2, 7, 3, 8, 1, 9]
selectors_num itu [n > 5 untuk n dalam numbers]
filtered_numbers itu list(kompres(numbers, selectors_num))  // [7, 8, 9]
```

### filterfalse(predicate, iterable)

Memfilter items yang predicate-nya False.

**Parameter:**
- `predicate` (function): Fungsi predicate
- `iterable`: Input iterable

**Return:**
- `iterator`: Filterfalse iterator

**Contoh:**
```python
// Filter bilangan genap (keep ganjil)
numbers itu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers itu list(filterfalse(lambda x: x % 2 == 0, numbers))
tampilkan odd_numbers  // [1, 3, 5, 7, 9]

// Filter string kosong
strings itu ["hello", "", "world", "", "python"]
non_empty itu list(filterfalse(lambda s: s == "", strings))
tampilkan non_empty  // ["hello", "world", "python"]
```

### ambil_while(predicate, iterable)

Mengambil items selama predicate True.

**Parameter:**
- `predicate` (function): Fungsi predicate
- `iterable`: Input iterable

**Return:**
- `iterator`: Takewhile iterator

**Contoh:**
```python
// Ambil numbers < 5
numbers itu [1, 2, 3, 4, 5, 6, 7, 8]
small_numbers itu list(ambil_while(lambda x: x < 5, numbers))
tampilkan small_numbers  // [1, 2, 3, 4]

// Ambil strings dengan panjang < 4
strings itu ["a", "ab", "abc", "abcd", "abcde"]
short_strings itu list(ambil_while(lambda s: panjang(s) < 4, strings))
tampilkan short_strings  // ["a", "ab", "abc"]
```

## Iterator Slicing dan Grouping

### islice(iterable, start, stop=None, step=1)

Slice iterator seperti list slicing (memory efficient).

**Parameter:**
- `iterable`: Input iterable
- `start` (int): Start index
- `stop` (int): Stop index (None untuk sampai akhir)
- `step` (int): Step (default 1)

**Return:**
- `iterator`: Isliced iterator

**Contoh:**
```python
// Slice dari index 2 sampai 8
numbers itu range(10)
sliced itu islice(numbers, 2, 8)
result itu list(sliced)  // [2, 3, 4, 5, 6, 7]

// Step slicing
step_slice itu islice(numbers, 0, 10, 2)
step_result itu list(step_slice)  // [0, 2, 4, 6, 8]

// Dari index tertentu sampai akhir
end_slice itu islice(numbers, 5)
end_result itu list(end_slice)  // [5, 6, 7, 8, 9]
```

### grupby(iterable, key=None)

Group consecutive items yang sama.

**Parameter:**
- `iterable`: Input iterable
- `key` (function): Key function untuk grouping

**Return:**
- `iterator`: Groupby iterator

**Contoh:**
```python
// Group consecutive identical items
data itu [1, 1, 2, 2, 2, 3, 1, 1]
untuk key, group dalam grupby(data):
    tampilkan f"Key {key}: {list(group)}"
// Output:
// Key 1: [1, 1]
// Key 2: [2, 2, 2]  
// Key 3: [3]
// Key 1: [1, 1]

// Group dengan key function
words itu ["apple", "apricot", "banana", "blueberry", "cherry"]
untuk key, group dalam grupby(words, lambda w: w[0]):
    tampilkan f"{key}: {list(group)}"
// Output:
// a: ['apple', 'apricot']
// b: ['banana', 'blueberry']
// c: ['cherry']
```

### zip_longest(*iterables, fillvalue=None)

Zip iterables dengan panjang berbeda, isi dengan fillvalue.

**Parameter:**
- `*iterables`: Iterables untuk di-zip
- `fillvalue`: Nilai untuk pengisi (default None)

**Return:**
- `iterator`: Zipped longest iterator

**Contoh:**
```python
// Zip lists dengan panjang berbeda
list1 itu [1, 2, 3]
list2 itu ["A", "B"]
list3 itu ["X", "Y", "Z", "W"]

zipped itu zip_longest(list1, list2, list3, fillvalue="?")
result itu list(zipped)
// [(1, 'A', 'X'), (2, 'B', 'Y'), (3, '?', 'Z'), ('?', '?', 'W')]

// Zip dengan fillvalue 0
numbers1 itu [1, 2, 3]
numbers2 itu [10, 20]
math_zipped itu list(zip_longest(numbers1, numbers2, fillvalue=0))
tampilkan math_zipped  // [(1, 10), (2, 20), (3, 0)]
```

## Kombinasi dan Permutasi

### produk(*iterables, repeat=1)

Cartesian product dari iterables.

**Parameter:**
- `*iterables`: Input iterables
- `repeat` (int): Jumlah repeat (default 1)

**Return:**
- `iterator`: Product iterator

**Contoh:**
```python
// Product dari dua lists
colors itu ["merah", "biru"]
sizes itu ["S", "M", "L"]

color_size_prod itu list(produk(colors, sizes))
tampilkan color_size_prod
// [('merah', 'S'), ('merah', 'M'), ('merah', 'L'), 
//  ('biru', 'S'), ('biru', 'M'), ('biru', 'L')]

// Product dengan repeat
dice_rolls itu list(produk([1, 2, 3, 4, 5, 6], repeat=2))
tampilkan f"Total combinations: {panjang(dice_rolls)}"  // 36
tampilkan f"First few: {dice_rolls[:5]}"
```

### permutasi(iterable, r=None)

Generate permutasi dari iterable.

**Parameter:**
- `iterable`: Input iterable
- `r` (int): Panjang permutasi (default panjang iterable)

**Return:**
- `iterator`: Permutation iterator

**Contoh:**
```python
// Permutasi semua elements
items itu ["A", "B", "C"]
all_perm itu list(permutasi(items))
tampilkan f"Total permutations: {panjang(all_perm)}"  // 6
tampilkan all_perm
// [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), 
//  ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

// Permutasi dengan panjang tertentu
perm2 itu list(permutasi(items, 2))
tampilkan f"2-permutations: {perm2}"
// [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

### kombinasi(iterable, r)

Generate kombinasi dari iterable (tanpa pengulangan).

**Parameter:**
- `iterable`: Input iterable
- `r` (int): Panjang kombinasi

**Return:**
- `iterator`: Combination iterator

**Contoh:**
```python
// Kombinasi 2 elements
items itu ["A", "B", "C", "D"]
comb2 itu list(kombinasi(items, 2))
tampilkan f"2-combinations: {comb2}"
// [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

// Kombinasi 3 elements
comb3 itu list(kombinasi(items, 3))
tampilkan f"3-combinations: {comb3}"
// [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
```

### kombinasi_dengan_pengulangan(iterable, r)

Generate kombinasi dengan pengulangan.

**Parameter:**
- `iterable`: Input iterable
- `r` (int): Panjang kombinasi

**Return:**
- `iterator`: Combination with replacement iterator

**Contoh:**
```python
// Kombinasi dengan pengulangan
colors itu ["merah", "hijau", "biru"]
comb_rep itu list(kombinasi_dengan_pengulangan(colors, 2))
tampilkan comb_rep
// [('merah', 'merah'), ('merah', 'hijau'), ('merah', 'biru'),
//  ('hijau', 'hijau'), ('hijau', 'biru'), ('biru', 'biru')]
```

## Fungsi Utilitas Lanjutan

### sliding_window(iterable, n)

Membuat sliding window dari size n.

**Parameter:**
- `iterable`: Input iterable
- `n` (int): Window size

**Return:**
- `iterator`: Sliding window iterator

**Contoh:**
```python
// Sliding window size 3
numbers itu [1, 2, 3, 4, 5, 6]
windows itu list(sliding_window(numbers, 3))
tampilkan windows  // [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

// Moving average
def moving_average(data, window):
    windows itu sliding_window(data, window)
    hasil [sum(window)/window untuk window dalam windows]
    return hasil

data itu [1, 2, 3, 4, 5, 6, 7, 8]
avg3 itu moving_average(data, 3)
tampilkan avg3  // [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
```

### pairwise(iterable)

Membuat pairs dari consecutive elements.

**Parameter:**
- `iterable`: Input iterable

**Return:**
- `iterator`: Pairwise iterator

**Contoh:**
```python
// Pairwise consecutive
numbers itu [1, 2, 3, 4, 5]
pairs itu list(pairwise(numbers))
tampilkan pairs  // [(1, 2), (2, 3), (3, 4), (4, 5)]

// Differences between consecutive
def consecutive_differences(data):
    pairs itu pairwise(data)
    hasil [b - a untuk a, b dalam pairs]
    return hasil

diffs itu consecutive_differences([10, 15, 12, 18, 20])
tampilkan diffs  // [5, -3, 6, 2]
```

### batched(iterable, n)

Batch iterable menjadi chunks of size n.

**Parameter:**
- `iterable`: Input iterable
- `n` (int): Batch size

**Return:**
- `iterator`: Batched iterator

**Contoh:**
```python
// Batch size 3
items itu [1, 2, 3, 4, 5, 6, 7, 8, 9]
batches itu list(batched(items, 3))
tampilkan batches  // [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

// Process large data in batches
large_data itu range(100)
batch_size itu 10
batch_count itu 0

untuk batch dalam batched(large_data, batch_size):
    batch_count += 1
    tampilkan f"Batch {batch_count}: {batch}"
```

### chunked(iterable, n)

Chunk iterable into lists of size n.

**Parameter:**
- `iterable`: Input iterable
- `n` (int): Chunk size

**Return:**
- `iterator`: Chunked iterator

**Contoh:**
```python
// Chunk data
data itu ["A", "B", "C", "D", "E", "F", "G"]
chunks itu list(chunked(data, 3))
tampilkan chunks  // [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]

// Process file line by line in chunks
lines itu ["line1", "line2", "line3", "line4", "line5"]
untuk chunk dalam chunked(lines, 2):
    tampilkan f"Processing: {chunk}"
```

### flatten(iterable)

Flatten nested iterables.

**Parameter:**
- `iterable`: Input iterable

**Return:**
- `iterator`: Flattened iterator

**Contoh:**
```python
// Flatten nested lists
nested itu [[1, 2], [3, [4, 5]], [6]]
flattened itu list(flatten(nested))
tampilkan flattened  // [1, 2, 3, [4, 5], 6]

// Flatten mixed types
mixed itu [1, [2, 3], "AB", (4, 5)]
flat_mixed itu list(flatten(mixed))
tampilkan flat_mixed  // [1, 2, 3, 'A', 'B', 4, 5]
```

### roundrobin(*iterables)

Interleave iterables secara公平.

**Parameter:**
- `*iterables`: Input iterables

**Return:**
- `iterator`: Round robin iterator

**Contoh:**
```python
// Round robin dari 3 lists
list1 itu [1, 4, 7]
list2 itu [2, 5, 8]
list3 itu [3, 6, 9]

interleaved itu list(roundrobin(list1, list2, list3))
tampilkan interleaved  // [1, 2, 3, 4, 5, 6, 7, 8, 9]

// Different lengths
short itu [1, 2]
long itu ["A", "B", "C", "D"]
result itu list(roundrobin(short, long))
tampilkan result  // [1, 'A', 2, 'B', 'C', 'D']
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.itertools impor *

tampilkan "=== Demo Itertools Library ==="

// 1. Infinite iterators
tampilkan "\n1. Infinite Iterators:"
counter itu hitung(10, 5)
count_list itu [next(counter) untuk i dalam range(5)]
tampilkan f"Count from 10 by 5: {count_list}"

cycle_colors itu siklus(["merah", "hijau", "biru"])
color_sample itu [next(cycle_colors) untuk i dalam range(6)]
tampilkan f"Color cycle: {color_sample}"

// 2. Accumulation
tampilkan "\n2. Accumulation:"
numbers itu [2, 3, 4, 5]
sum_acc itu list(akumulasi(numbers))
prod_acc itu list(akumulasi(numbers, lambda x, y: x * y))
tampilkan f"Sum accumulate: {sum_acc}"
tampilkan f"Product accumulate: {prod_acc}"

// 3. Chaining dan filtering
tampilkan "\n3. Chaining dan Filtering:"
data_sets itu [[1, 2], [3, 4], [5, 6]]
chained_data itu list(rantai_dari_iterable(data_sets))
tampilkan f"Chained: {chained_data}"

filtered_data itu list(filterfalse(lambda x: x <= 3, chained_data))
tampilkan f"Filtered > 3: {filtered_data}"

// 4. Slicing
tampilkan "\n4. Slicing:"
large_range itu range(20)
sliced_data itu list(islice(large_range, 5, 15, 2))
tampilkan f"Slice 5-15 step 2: {sliced_data}"

// 5. Grouping
tampilkan "\n5. Grouping:"
words itu ["apple", "apricot", "banana", "blueberry", "cherry", "cranberry"]
untuk first_letter, group dalam grupby(words, lambda w: w[0]):
    tampilkan f"{first_letter.upper()}: {list(group)}"

// 6. Combinations dan Permutasi
tampilkan "\n6. Combinations dan Permutasi:"
colors itu ["merah", "hijau", "biru"]
comb2 itu list(kombinasi(colors, 2))
perm3 itu list(permutasi(colors))
tampilkan f"2-combinations: {comb2}"
tampilkan f"3-permutations: {perm3}"

// 7. Advanced utilities
tampilkan "\n7. Advanced Utilities:"
series itu [1, 2, 3, 4, 5, 6, 7, 8]
windows itu list(sliding_window(series, 3))
tampilkan f"Sliding windows: {windows}"

pairs itu list(pairwise(series))
tampilkan f"Pairs: {pairs}"

batches itu list(batched(series, 4))
tampilkan f"Batches: {batches}"

// 8. Real-world example - Data processing
tampilkan "\n8. Data Processing Example:"
// Process sensor data
sensor_readings itu [23.5, 24.1, 22.8, 25.2, 24.8, 23.9, 24.5, 25.1, 24.3]

// Moving average dengan sliding window
windows_data itu list(sliding_window(sensor_readings, 3))
moving_avg itu [sum(window)/3 untuk window dalam windows_data]
tampilkan f"Moving averages: {[round(avg, 1) untuk avg dalam moving_avg]}"

// Group by temperature range
temp_ranges itu []
untuk reading dalam sensor_readings:
    jika reading < 24:
        temp_ranges.tambah("rendah")
    lainnya jika reading < 25:
        temp_ranges.tambah("sedang")  
    lainnya:
        temp_ranges.tambah("tinggi")

untuk range_type, group dalam grupby(sorted(temp_ranges)):
    tampilkan f"Range {range_type}: {panjang(list(group))} readings"

// 9. Cartesian product untuk combinations
tampilkan "\n9. Product Combinations:"
sizes itu ["S", "M", "L"]
colors itu ["merah", "biru", "hijau"]
styles itu ["kasual", "formal"]

produk kombinasi itu list(produk(sizes, colors, styles))[:5]
tampilkan f"First 5 combinations: {kombinasi}"
tampilkan f"Total combinations: {panjang(list(produk(sizes, colors, styles)))}"

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **Data Processing**: Stream processing untuk large datasets
2. **Combination Generation**: Password generation, feature combinations
3. **Time Series Analysis**: Moving averages, sliding windows
4. **Batch Processing**: Process data in chunks for memory efficiency
5. **Infinite Sequences**: Generate streams without memory limits
6. **Data Transformation**: Map/filter/reduce operations
7. **Combinatorial Problems**: Generate all possibilities systematically
8. **Parallel Processing**: Prepare data batches for parallel execution

## Performa Tips

- Gunakan iterators untuk large data (memory efficient)
- `islice` lebih efisien daripada slicing list besar
- `batched` dan `chunked` untuk processing data dalam batches
- `sliding_window` dan `pairwise` untuk time series analysis
- Infinite iterators baik untuk generator patterns
- `filterfalse` kadang lebih intuitif daripada filter dengan negasi

## Memory Considerations

- Semua iterators lazy evaluation (tidak memuat semua data ke memory)
- Perfect untuk processing streams dan large datasets
- Gunakan `list()` hanya jika benar-benar dibutuhkan
- Beberapa functions seperti `grupby` butuh sorted data untuk optimal

## Error Handling

- Iterator akan raise `StopIteration` saat exhausted
- Pastikan predicate functions tidak raise exceptions
- Gunakan try-except untuk iterator operations yang mungkin gagal
- Empty iterables menghasilkan empty iterator (tidak error)