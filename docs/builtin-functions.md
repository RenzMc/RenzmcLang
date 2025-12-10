# RenzMcLang Built-in Functions

## Overview

RenzMcLang v1.0 memisahkan fungsi menjadi dua kategori:

### 1. Core Built-in Functions (Always Available)
Fungsi fundamental yang tidak perlu diimport:
- Type conversion & basic operations
- I/O functions  
- Control flow utilities

### 2. Standard Library Functions (Requires Import)
Fungsi spesialisasi yang tersedia di standard library:
- Mathematics: di library `math`
- JSON: di library `json`
- HTTP: di library `http`
- File I/O: di library `fileio`
- Statistics: di library `statistics`
- OS operations: di library `os`
- DateTime: di library `datetime`
- Random: di library `random`

**Migration Notice**: Fungsi seperti `sin()`, `json_ke_teks()`, `http_get()`, dll sekarang berada di standard library. Lihat [Standard Library Guide](standard-library.md) untuk informasi lengkap.

---

## Core Built-in Functions

### Type Conversion Functions

#### `str(object)` / `teks(object)`
Convert object menjadi string.

```python
angka = 123
hasil = str(angka)      # "123"
hasil2 = teks(angka)    # "123"
```

#### `int(object)` / `bulat(object)`
Convert object menjadi integer.

```python
teks = "42"
hasil = int(teks)       # 42
hasil2 = bulat(teks)    # 42
```

#### `float(object)` / `desimal(object)`
Convert object menjadi float.

```python
teks = "3.14"
hasil = float(teks)     # 3.14
hasil2 = desimal(teks)  # 3.14
```

#### `bool(object)` / `boolean(object)`
Convert object menjadi boolean.

```python
nilai = bool(1)         # benar
nilai2 = boolean(0)     # salah
```

#### `list(object)` / `daftar(object)`
Convert object menjadi list.

```python
teks = "abc"
hasil = list(teks)      # ['a', 'b', 'c']
hasil2 = daftar(teks)   # ['a', 'b', 'c']
```

#### `dict(object)` / `kamus(object)`
Convert object menjadi dictionary.

```python
pairs = [('a', 1), ('b', 2)]
hasil = dict(pairs)     # {'a': 1, 'b': 2}
hasil2 = kamus(pairs)   # {'a': 1, 'b': 2}
```

#### `set(object)` / `himpunan(object)`
Convert object menjadi set.

```python
items = [1, 2, 2, 3]
hasil = set(items)      # {1, 2, 3}
hasil2 = himpunan(items) # {1, 2, 3}
```

#### `tuple(object)` / `tupel(object)`
Convert object menjadi tuple.

```python
items = [1, 2, 3]
hasil = tuple(items)    # (1, 2, 3)
hasil2 = tupel(items)   # (1, 2, 3)
```

### I/O Functions

#### `print(*objects)` / `tampilkan(*objects)`
Print objects ke console.

```python
tampilkan("Hello World")     # Hello World
print("Nama:", "Budi")       # Nama: Budi
```

#### `input(prompt)` / `masukan(prompt)`
Read input dari user.

```python
nama = input("Nama: ")       # Prompt: Nama: 
nama2 = masukan("Usia: ")    # Prompt: Usia: 
```

#### `len(object)` / `panjang(object)`
Dapatkan panjang object.

```python
teks = "Hello"
hasil = len(teks)           # 5
hasil2 = panjang(teks)      # 5
```

### Basic Operations

#### `sum(iterable)` / `jumlah(iterable)`
Jumlahkan semua elemen di iterable.

```python
angka = [1, 2, 3, 4, 5]
hasil = sum(angka)          # 15
hasil2 = jumlah(angka)      # 15
```

#### `min(iterable)` / `minimum(iterable)`
Cari nilai minimum.

```python
angka = [3, 1, 4, 2]
hasil = min(angka)          # 1
hasil2 = minimum(angka)     # 1
```

#### `max(iterable)` / `maksimum(iterable)`
Cari nilai maksimum.

```python
angka = [3, 1, 4, 2]
hasil = max(angka)          # 4
hasil2 = maksimum(angka)    # 4
```

#### `abs(number)` / `absolut(number)`
Nilai absolut dari number.

```python
nilai = abs(-5)             # 5
nilai2 = absolut(-5)        # 5
```

#### `round(number, digits=0)` / `bulat(number, digits=0)`
Bulatkan angka.

```python
nilai = round(3.14159, 2)   # 3.14
nilai2 = bulat(3.14159, 2)  # 3.14
```

#### `pow(base, exp)` / `pangkat(base, exp)`
Hitung pangkat.

```python
hasil = pow(2, 3)           # 8
hasil2 = pangkat(2, 3)      # 8
```

### Control Flow Functions

#### `range(stop)` / `rentang(stop)`
Generate sequence angka.

```python
// range(stop)
untuk setiap i dari range(5):
    tampilkan i  // 0, 1, 2, 3, 4

// range(start, stop)
untuk setiap i dari rentang(2, 8):
    tampilkan i  // 2, 3, 4, 5, 6, 7

// range(start, stop, step)
untuk setiap i dari rentang(0, 10, 2):
    tampilkan i  // 0, 2, 4, 6, 8
```

#### `enumerate(iterable)` / `enumerasi(iterable)`
Tambahkan index ke setiap elemen.

```python
items = ['apel', 'jeruk', 'mangga']
indexed = enumerate(items)
tampilkan indexed  // [(0, 'apel'), (1, 'jeruk'), (2, 'mangga')]

// Dalam loop
untuk setiap item dari enumerasi(items):
    tampilkan f"Index {item[0]}: {item[1]}"
```

#### `zip(*iterables)` / `zip_iter(*iterables)`
Gabungkan beberapa iterables.

```python
nama = ['Alice', 'Bob', 'Charlie']
umur = [25, 30, 35]
kota = ['Jakarta', 'Bandung', 'Surabaya']

hasil = zip(nama, umur, kota)
tampilkan hasil
// [('Alice', 25, 'Jakarta'), ('Bob', 30, 'Bandung'), ('Charlie', 35, 'Surabaya')]
```

#### `all(iterable)` / `semua(iterable)`
Cek apakah semua elemen truthy.

```python
values = [benar, benar, benar]
hasil = all(values)          # benar
hasil2 = semua(values)       # benar

values2 = [benar, salah, benar]
hasil3 = all(values2)        # salah
```

#### `any(iterable)` / `ada(iterable)`
Cek apakah ada elemen yang truthy.

```python
values = [salah, salah, benar]
hasil = any(values)          # benar
hasil2 = ada(values)         # benar
```

### Information Functions

#### `type(object)` / `jenis(object)`
Dapatkan tipe object.

```python
nilai = 123
tipe = type(nilai)           # "int"
tipe2 = jenis(nilai)         # "int"
```

#### `isinstance(object, class)` / `adalah_instance(object, class)`
Cek apakah object instance dari class tertentu.

```python
nilai = "hello"
hasil = isinstance(nilai, str)           # benar
hasil2 = adalah_instance(nilai, str)     # benar
```

---

## Deprecated Functions (Moved to Standard Library)

Fungsi-fungsi berikut sudah tidak available sebagai built-in dan telah dipindahkan ke standard library:

### Mathematics (Sekarang di library `math`)
```python
// ❌ Deprecated (Built-in)
sin(0.5), cos(0.5), tan(0.5)
sqrt(16), akar(16)
log(100, 10), logaritma(100, 10)
pi, e, tau

// ✅ New way (Standard Library)
dari math impor sin, cos, tan, sqrt, log, pi
sin(0.5), cos(0.5), tan(0.5)
sqrt(16)
log(100, 10)
pi
```

### JSON (Sekarang di library `json`)
```python
// ❌ Deprecated (Built-in)
teks_ke_json(json_str)
json_ke_teks(data)
baca_json('file.json')
tulis_json('file.json', data)

// ✅ New way (Standard Library)
dari json impor loads, dumps, load, dump
loads(json_str)
dumps(data)
load(open_file('file.json'))
dump(data, open_file('file.json', 'w'))
```

### HTTP (Sekarang di library `http`)
```python
// ❌ Deprecated (Built-in)
http_get('https://api.example.com')
http_post('https://api.example.com', json=data)
ambil_http('https://api.example.com')

// ✅ New way (Standard Library)
dari http impor get, post, ambil
get('https://api.example.com')
post('https://api.example.com', json=data)
ambil('https://api.example.com')
```

### File Operations (Sekarang di library `fileio`)
```python
// ❌ Deprecated (Built-in)
baca_file('data.txt')
tulis_file('output.txt', content)
baca_json('config.json')
tulis_json('output.json', data)

// ✅ New way (Standard Library)
dari fileio impor read_text, write_text, read_json, write_json
read_text('data.txt')
write_text('output.txt', content)
read_json('config.json')
write_json('output.json', data)
```

### Statistics (Sekarang di library `statistics`)
```python
// ❌ Deprecated (Built-in)
rata_rata(data)
median(data)
stdev(data)
variance(data)

// ✅ New way (Standard Library)
dari statistics impor mean, median, stdev, variance
mean(data)
median(data)
stdev(data)
variance(data)
```

### Random (Sekarang di library `random`)
```python
// ❌ Deprecated (Built-in)
acak()           // 0-1 random
acak_bulat(1, 6)  // random integer 1-6
pilih_acak(items)

// ✅ New way (Standard Library)
dari random impor random, randint, choice
random()         // 0-1 random
randint(1, 6)    // random integer 1-6
choice(items)
```

### OS Operations (Sekarang di library `os`)
```python
// ❌ Deprecated (Built-in)
dapatkan_dir_sekarang()
ubah_dir('/path')
daftar_dir('.')
buat_dir('new_dir')

// ✅ New way (Standard Library)
dari os impor getcwd, chdir, listdir, mkdir
getcwd()
chdir('/path')
listdir('.')
mkdir('new_dir')
```

---

## Standard Library Migration Examples

### Example 1: Mathematical Calculations

```python
// Old way (deprecated)
hasil = sin(pi / 4)
akar_16 = akar(16)
log_100 = logaritma(100, 10)

// New way (standard library)
dari math impor sin, pi, sqrt, log
hasil = sin(pi / 4)
akar_16 = sqrt(16)
log_100 = log(100, 10)
```

### Example 2: HTTP API Client

```python
// Old way (deprecated)
response = http_get('https://api.example.com/data')
jika response.status_code == 200:
    data = response.json()

// New way (standard library)
dari http impor get
response = get('https://api.example.com/data')
jika response.ok():
    data = response.json()
```

### Example 3: File Processing

```python
// Old way (deprecated)
content = baca_file('data.txt')
config = baca_json('config.json')
tulis_json('output.json', processed_data, indent=2)

// New way (standard library)
dari fileio impor read_text, read_json, write_json
content = read_text('data.txt')
config = read_json('config.json')
write_json('output.json', processed_data, indent=2)
```

### Example 4: Data Analysis

```python
// Old way (deprecated)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rata = rata_rata(data)
median = nilai_tengah(data)
std_dev = deviasi_standar(data)

// New way (standard library)
dari statistics impor mean, median, stdev
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rata = mean(data)
median = median(data)
std_dev = stdev(data)
```

---

## Library Management Functions

RenzMcLang menyediakan fungsi untuk mengelola standard library:

### `dapatkan_library()` / `get_libraries()`
Dapatkan daftar semua available libraries.

```python
libraries = dapatkan_library()
tampilkan(libraries)
// ['math', 'json', 'http', 'os', 'datetime', 'statistics', 'random', 'fileio']
```

### `impor_library(library_name)` / `import_library(library_name)`
Import library secara dinamis.

```python
math_lib = impor_library('math')
hasil = math_lib.sin(0.5)
```

### `info_library(library_name)`
Dapatkan informasi tentang library.

```python
info = info_library('math')
tampilkan(info)
// {
//   "name": "math",
//   "functions": ["sin", "cos", "tan", ...],
//   "constants": ["pi", "e", ...],
//   "version": "1.0.0"
// }
```

---

## Best Practices

### 1. Use Specific Imports
```python
// Good
dari math impor sin, cos, tan

// Avoid (unless banyak fungsi yang dibutuhkan)
impor math
```

### 2. Use Indonesian Names for Readability
```python
// Good
dari statistics impor mean, median, stdev
rata = mean(data)
tengah = median(data)
deviasi = stdev(data)
```

### 3. Combine Built-in and Library Functions
```python
dari math impor sqrt
dari statistics impor mean

data = [1, 4, 9, 16, 25]
rata_rata = mean(data)      // Library function
panjang_data = len(data)    // Built-in function
std_dev = sqrt(rata_rata)   // Combined
```

### 4. Handle Import Errors
```python
coba:
    dari math impor sin, cos
tangkap ImportError sebagai e:
    tampilkan(f"Error import math: {e}")
```

---

## See Also

- [Standard Library Guide](standard-library.md) - Dokumentasi lengkap standard library
- [Syntax Basics](syntax-basics.md) - Basic syntax RenzMcLang
- [Examples](examples.md) - More code examples
- [Installation](installation.md) - Installation guide