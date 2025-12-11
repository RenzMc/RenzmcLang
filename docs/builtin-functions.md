# RenzMcLang Built-in Functions

## Overview

RenzMcLang v1.0 menyediakan **180+ built-in functions** yang terorganisir dalam dua kategori:

### 1. Core Built-in Functions (Always Available)
Fungsi fundamental yang tidak perlu diimport:
- Type conversion & basic operations
- I/O functions  
- Control flow utilities
- String manipulation (50+ functions)
- Math & statistics (40+ functions)
- File operations (30+ functions)

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
- **NEW**: UUID: di library `uuid`
- **NEW**: Base64: di library `base64`
- **NEW**: Hashlib: di library `hashlib`
- **NEW**: Urllib: di library `urllib`
- **NEW**: Regex: di library `re`
- **NEW**: String: di library `string`
- **NEW**: Pathlib: di library `pathlib`
- **NEW**: Itertools: di library `itertools`
- **NEW**: Collections: di library `collections`

---

## Core Built-in Functions (Total: 95+ Functions)

### Type Conversion Functions (8 functions)

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
hasil = bool(1)         # True
hasil2 = boolean(0)     # False
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

#### `tuple(object)` / `tupel(object)`
Convert object menjadi tuple.

```python
daftar = [1, 2, 3]
hasil = tuple(daftar)   # (1, 2, 3)
hasil2 = tupel(daftar)  # (1, 2, 3)
```

#### `set(object)` / `himpunan(object)`
Convert object menjadi set.

```python
daftar = [1, 2, 2, 3]
hasil = set(daftar)     # {1, 2, 3}
hasil2 = himpunan(daftar) # {1, 2, 3}
```

### Input/Output Functions (12 functions)

#### `tampilkan(*args)` / `print(*args)`
Menampilkan output ke console.

```python
tampilkan "Hello World"
tampilkan "Nilai:", 42, "Status:", True
```

#### `input(prompt)` / `masukan(prompt)`
Menerima input dari user.

```python
nama = input("Masukkan nama: ")
umur = masukan("Masukkan umur: ")
```

#### `baca_file(nama_file)` / `read_file(nama_file)`
Membaca isi file.

```python
konten = baca_file("data.txt")
teks = read_file("config.json")
```

#### `tulis_file(nama_file, konten)` / `write_file(nama_file, konten)`
Menulis ke file.

```python
tulis_file("output.txt", "Hello World")
write_file("data.json", json_string)
```

#### `tambah_file(nama_file, konten)` / `append_file(nama_file, konten)`
Menambah konten ke file.

```python
tambah_file("log.txt", "Error message\n")
append_file("data.csv", "new,row,data")
```

#### `hapus_file(nama_file)` / `delete_file(nama_file)`
Menghapus file.

```python
hapus_file("temp.txt")
delete_file("old_data.csv")
```

#### `file_ada(nama_file)` / `file_exists(nama_file)`
Cek apakah file ada.

```python
if file_ada("config.json"):
    config = baca_file("config.json")
```

#### `buat_dir(nama_dir)` / `create_dir(nama_dir)`
Membuat direktori.

```python
buat_dir("uploads")
create_dir("logs/errors")
```

#### `hapus_dir(nama_dir)` / `delete_dir(nama_dir)`
Menghapus direktori.

```python
hapus_dir("temp")
delete_dir("old_logs")
```

#### `daftar_file(path)` / `list_files(path)`
Menampilkan daftar file dalam direktori.

```python
files = daftar_file("/home/user")
documents = list_files("./documents")
```

#### `dapatkan_ukuran_file(nama_file)` / `get_file_size(nama_file)`
Mendapatkan ukuran file dalam bytes.

```python
size = dapatkan_ukuran_file("large_file.dat")
bytes = get_file_size("image.jpg")
```

#### `copy_file(sumber, tujuan)` / `copy_file(sumber, tujuan)`
Menyalin file.

```python
copy_file("source.txt", "backup.txt")
```

### String Manipulation Functions (25+ functions)

#### `panjang(string)` / `len(string)`
Mendapatkan panjang string.

```python
panjang = panjang("Hello World")  # 11
length = len("RenzMcLang")       # 10
```

#### `huruf_besar(string)` / `upper(string)`
Mengubah ke uppercase.

```python
hasil = huruf_besar("hello")     # "HELLO"
upper_text = upper("World")      # "WORLD"
```

#### `huruf_kecil(string)` / `lower(string)`
Mengubah ke lowercase.

```python
hasil = huruf_kecil("HELLO")     # "hello"
lower_text = lower("World")      # "world"
```

#### `potong(string, awal, akhir)` / `slice(string, awal, akhir)`
Memotong string.

```python
hasil = potong("Hello World", 0, 5)  # "Hello"
sliced = slice("RenzMcLang", 4, 9)    # "McLang"
```

#### `ganti(string, lama, baru)` / `replace(string, lama, baru)`
Mengganti substring.

```python
hasil = ganti("Hello World", "World", "RenzMcLang")  # "Hello RenzMcLang"
replaced = replace("abc abc", "abc", "xyz")          # "xyz xyz"
```

#### `pisah(string, pemisah)` / `split(string, pemisah)`
Memisah string menjadi list.

```python
hasil = pisah("a,b,c", ",")      # ["a", "b", "c"]
words = split("Hello World", " ") # ["Hello", "World"]
```

#### `gabung(pemisah, list_string)` / `join(pemisah, list_string)`
Menggabung list menjadi string.

```python
hasil = gabung(",", ["a", "b", "c"])  # "a,b,c"
joined = join(" ", ["Hello", "World"]) # "Hello World"
```

#### `hapus_spasi(string)` / `strip(string)`
Menghapus whitespace di awal dan akhir.

```python
hasil = hapus_spasi("  hello  ")  # "hello"
cleaned = strip("  world  ")      # "world"
```

#### `mulai_dengan(string, prefix)` / `startswith(string, prefix)`
Cek apakah string diawali dengan prefix.

```python
hasil = mulai_dengan("hello", "he")   # True
starts = startswith("world", "wo")    # True
```

#### `akhir_dengan(string, suffix)` / `endswith(string, suffix)`
Cek apakah string diakhiri dengan suffix.

```python
hasil = akhir_dengan("hello", "lo")   # True
ends = endswith("world", "ld")        # True
```

#### `berisi(string, substring)` / `contains(string, substring)`
Cek apakah string mengandung substring.

```python
hasil = berisi("hello", "ell")    # True
contains_word = contains("world", "orl")  # True
```

#### `find(string, substring)` / `cari(string, substring)`
Mencari posisi substring.

```python
posisi = find("hello", "ell")     # 1
index = cari("world", "orl")      # 1
```

#### `hitung(string, substring)` / `count(string, substring)`
Menghitung jumlah substring.

```python
jumlah = hitung("hello hello", "hello")  # 2
count_word = count("a,b,a,b", "a")       # 2
```

#### `adalah_huruf(string)` / `is_alpha(string)`
Cek apakah string hanya huruf.

```python
hasil = adalah_huruf("abc")       # True
is_alpha_text = is_alpha("123")  # False
```

#### `adalah_angka(string)` / `is_digit(string)`
Cek apakah string hanya angka.

```python
hasil = adalah_angka("123")       # True
is_digit_text = is_digit("abc")   # False
```

#### `adalah_alfanumerik(string)` / `is_alnum(string)`
Cek apakah string alphanumeric.

```python
hasil = adalah_alfanumerik("abc123")   # True
is_alnum_text = is_alnum("abc!")       # False
```

### Mathematical Functions (30+ functions)

#### `abs(nilai)` / `mutlak(nilai)`
Nilai absolut.

```python
hasil = abs(-5)         # 5
mutlak_nilai = mutlak(-10) # 10
```

#### `round(nilai, desimal)` / `bulatkan(nilai, desimal)`
Membulatkan angka.

```python
hasil = round(3.7)       # 4
bulatkan_nilai = bulatkan(3.14159, 2) # 3.14
```

#### `ceil(nilai)` / `atap(nilai)`
Pembulatan ke atas.

```python
hasil = ceil(3.2)        # 4
atap_nilai = atap(5.1)   # 6
```

#### `floor(nilai)` / `lantai(nilai)`
Pembulatan ke bawah.

```python
hasil = floor(3.8)       # 3
lantai_nilai = lantai(5.9) # 5
```

#### `pow(basis, eksponen)` / `pangkat(basis, eksponen)`
Perpangkatan.

```python
hasil = pow(2, 3)        # 8
pangkat_nilai = pangkat(5, 2) # 25
```

#### `sqrt(nilai)` / `akar(nilai)`
Akar kuadrat.

```python
hasil = sqrt(16)         # 4.0
akar_nilai = akar(25)    # 5.0
```

#### `sin(sudut)` / `sinus(sudut)`
Sinus sudut (radian).

```python
hasil = sin(0.5)         # 0.4794255386
sinus_nilai = sinus(1.0) # 0.8414709848
```

#### `cos(sudut)` / `cosinus(sudut)`
Cosinus sudut (radian).

```python
hasil = cos(0.5)         # 0.877582562
cosinus_nilai = cosinus(1.0) # 0.540302306
```

#### `tan(sudut)` / `tangen(sudut)`
Tangen sudut (radian).

```python
hasil = tan(0.5)         # 0.5463024898
tangen_nilai = tangen(1.0) # 1.557407725
```

#### `min(iterable)` / `minimum(iterable)`
Nilai minimum.

```python
hasil = min([1, 5, 3])    # 1
minimum_nilai = minimum([10, 5, 8]) # 5
```

#### `max(iterable)` / `maksimum(iterable)`
Nilai maksimum.

```python
hasil = max([1, 5, 3])    # 5
maksimum_nilai = maksimum([10, 5, 8]) # 10
```

#### `sum(iterable)` / `jumlah(iterable)`
Jumlah semua elemen.

```python
hasil = sum([1, 2, 3])    # 6
jumlah_nilai = jumlah([10, 20, 30]) # 60
```

#### `mean(iterable)` / `rata_rata(iterable)`
Rata-rata.

```python
hasil = mean([1, 2, 3])    # 2.0
rata_rata_nilai = rata_rata([10, 20, 30]) # 20.0
```

#### `median(iterable)` / `median_nilai(iterable)`
Nilai median.

```python
hasil = median([1, 3, 2])  # 2
median_nilai = median_nilai([1, 2, 3, 4]) # 2.5
```

### List & Dictionary Operations (20+ functions)

#### `tambah(list, item)` / `append(list, item)`
Menambah item ke list.

```python
daftar = [1, 2, 3]
tambah(daftar, 4)      # [1, 2, 3, 4]
append(daftar, 5)      # [1, 2, 3, 4, 5]
```

#### `hapus(list, index)` / `remove(list, index)`
Menghapus item dari list.

```python
daftar = [1, 2, 3]
hapus(daftar, 1)       # [1, 3]
remove(daftar, 0)       # [2, 3]
```

#### `urutkan(list)` / `sort(list)`
Mengurutkan list.

```python
daftar = [3, 1, 2]
urutkan(daftar)        # [1, 2, 3]
sort(daftar)           # [1, 2, 3]
```

#### `balik(list)` / `reverse(list)`
Membalik urutan list.

```python
daftar = [1, 2, 3]
balik(daftar)          # [3, 2, 1]
reverse(daftar)        # [3, 2, 1]
```

---

## Standard Library Functions (Total: 85+ Functions)

### UUID Library (9 functions) - `dari renzmc.library.uuid impor *`

```python
dari renzmc.library.uuid impor buat_uuid4, buat_uuid1, uuid_valid

# Generate UUID
uuid4 = buat_uuid4()           # Random UUID
uuid1 = buat_uuid1()           # Host+time UUID
valid = uuid_valid(uuid4)      # True/False
```

**Available Functions:**
- `buat_uuid1()` - UUID berdasarkan host dan waktu
- `buat_uuid3(namespace, name)` - UUID berdasarkan MD5 hash
- `buat_uuid4()` - UUID random
- `buat_uuid5(namespace, name)` - UUID berdasarkan SHA-1 hash
- `parse_uuid(string)` - Parse UUID string
- `uuid_valid(string)` - Validasi UUID
- `dapatkan_namespace_dns()` - DNS namespace
- `dapatkan_namespace_url()` - URL namespace
- `dapatkan_namespace_oid()` - OID namespace

### Base64 Library (8 functions) - `dari renzmc.library.base64 impor *`

```python
dari renzmc.library.base64 impor encode_base64, decode_base64

# Encode/Decode
encoded = encode_base64("Hello World")     # "SGVsbG8gV29ybGQ="
decoded = decode_base64(encoded)          # "Hello World"
```

**Available Functions:**
- `encode_base64(data)` - Encode ke Base64
- `decode_base64(encoded_data)` - Decode Base64
- `encode_base64_urlsafe(data)` - URL-safe encoding
- `decode_base64_urlsafe(encoded_data)` - URL-safe decoding
- `encode_base64_file(path)` - Encode file
- `decode_base64_ke_file(encoded, path)` - Decode ke file
- `base64_valid(data)` - Validasi Base64

### Hashlib Library (18 functions) - `dari renzmc.library.hashlib impor *`

```python
dari renzmc.library.hashlib impor hash_md5, hash_sha256, hmac_hash

# Hash functions
md5_hash = hash_md5("data")           # MD5 hash
sha256_hash = hash_sha256("data")     # SHA256 hash
hmac_sig = hmac_hash("data", "key")   # HMAC signature
```

**Available Functions:**
- `hash_md5(data)` - MD5 hash
- `hash_sha1(data)` - SHA1 hash  
- `hash_sha224(data)` - SHA224 hash
- `hash_sha256(data)` - SHA256 hash
- `hash_sha384(data)` - SHA384 hash
- `hash_sha512(data)` - SHA512 hash
- `hash_blake2b(data)` - BLAKE2b hash
- `hash_blake2s(data)` - BLAKE2s hash
- `hash_sha3_224(data)` - SHA3-224 hash
- `hash_sha3_256(data)` - SHA3-256 hash
- `hash_sha3_384(data)` - SHA3-384 hash
- `hash_sha3_512(data)` - SHA3-512 hash
- `hash_file_md5(path)` - MD5 hash file
- `hash_file_sha256(path)` - SHA256 hash file
- `hmac_hash(data, key)` - HMAC hash
- `buat_salt(length)` - Generate random salt
- `hash_with_salt(data, salt)` - Hash dengan salt

### Urllib Library (15 functions) - `dari renzmc.library.urllib impor *`

```python
dari renzmc.library.urllib impor parse_url, gabung_url, encode_url

# URL operations
parsed = parse_url("https://example.com/path?query=value")
joined = gabung_url("https://api.com", "v1", "users")
encoded = encode_url({"name": "John", "age": 25})
```

**Available Functions:**
- `parse_url(url)` - Parse URL components
- `buat_url(scheme, netloc, path, query, fragment)` - Build URL
- `encode_url(params)` - Encode parameters
- `decode_url(encoded)` - Decode URL-encoded string
- `encode_component(component)` - Encode URL component
- `decode_component(encoded)` - Decode component
- `gabung_url(base, *paths)` - Join URLs
- `dapatkan_scheme(url)` - Get URL scheme
- `dapatkan_domain(url)` - Get domain
- `dapatkan_path(url)` - Get path
- `dapatkan_query(url)` - Get query string
- `parse_query(query)` - Parse query string
- `buat_query(params)` - Build query string
- `url_valid(url)` - Validate URL
- `download_url(url, path)` - Download URL content

### Regular Expression Library (25 functions) - `dari renzmc.library.re impor *`

```python
dari renzmc.library.re impor validasi_email, extract_angka, cari_semua

# Regex operations
is_email = validasi_email("user@example.com")    # True
numbers = extract_angka("Harga: Rp 150.000")     # ["150", "000"]
matches = cari_semua(r"\bword\b", text)         # Find all words
```

**Available Functions:**
- `cocok(pattern, string)` - Match at start
- `cari(pattern, string)` - Search in string
- `cari_semua(pattern, string)` - Find all matches
- `ganti(pattern, replacement, string)` - Replace all
- `bagi(pattern, string)` - Split by pattern
- `kompile(pattern)` - Compile regex
- `escape(pattern)` - Escape special chars
- `validasi_email(email)` - Validate email
- `validasi_telepon(phone)` - Validate phone
- `validasi_url(url)` - Validate URL
- `extract_email(text)` - Extract emails
- `extract_url(text)` - Extract URLs
- `extract_angka(text)` - Extract numbers
- `extract_kata(text)` - Extract words

### String Library (30+ functions) - `dari renzmc.library.string impor *`

```python
dari renzmc.library.string impor acak_alphanumeric, caesar, rot13

# Advanced string operations
random_str = acak_alphanumeric(10)        # "aB3xY9zL2m"
encrypted = caesar("Hello", 3)           # "Khoor"
rot13_text = rot13("Secret")             # "Frperg"
vowels = hitung_vokal("Hello World")     # 3
```

**Available Functions:**
- `huruf_besar(text)` - Uppercase
- `huruf_kecil(text)` - Lowercase
- `judul(text)` - Title case
- `swap_case(text)` - Swap case
- `hapus_spasi(text)` - Trim whitespace
- `tengah(text, width, fill)` - Center text
- `kiri(text, width, fill)` - Left align
- `kanan(text, width, fill)` - Right align
- `is_alpha(text)` - Check alphabetic
- `is_digit(text)` - Check numeric
- `is_alnum(text)` - Check alphanumeric
- `acak_huruf(length)` - Random letters
- `acak_angka(length)` - Random numbers
- `acak_alphanumeric(length)` - Random alphanumeric
- `hitung_vokal(text)` - Count vowels
- `hitung_konsonan(text)` - Count consonants
- `hitung_kata(text)` - Count words
- `extract_angka(text)` - Extract numbers
- `extract_huruf(text)` - Extract letters
- `bersihkan_spasi(text)` - Clean whitespace
- `caesar(text, shift)` - Caesar cipher
- `rot13(text)` - ROT13 cipher

### Pathlib Library (20+ functions) - `dari renzmc.library.pathlib impor *`

```python
dari renzmc.library.pathlib impor Path, path_current, path_home

# Path operations
current = path_current()                    # Current directory
home = path_home()                          # Home directory
path = Path("docs", "file.txt")             # Path object
nama_file = path.dapatkan_nama()            # "file.txt"
extension = path.dapatkan_extension()       # ".txt"
parent = path.dapatkan_parent()             # "docs"
```

**Available Functions:**
- `Path(*segments)` - Path object
- `path_current()` - Current directory
- `path_home()` - Home directory
- `path_temp()` - Temp directory
- `gabung_path(*paths)` - Join paths
- `path_absolute(path)` - Absolute path
- `path_relatif(path, start)` - Relative path
- `expand_user(path)` - Expand ~ to home
- `split_path(path)` - Split path
- `split_ext(path)` - Split extension
- `get_extension(path)` - Get extension
- `get_filename(path)` - Get filename
- `get_basename(path)` - Get basename
- `get_directory(path)` - Get directory

### Itertools Library (25+ functions) - `dari renzmc.library.itertools impor *`

```python
dari renzmc.library.itertools impor hitung, siklus, permutasi, kombinasi

# Iterator operations
counter = hitung(0, 2)                      # 0, 2, 4, 6, 8, ...
cycle = siklus([1, 2, 3])                  # 1, 2, 3, 1, 2, 3, ...
perms = permutasi([1, 2, 3])                # All permutations
combs = kombinasi([1, 2, 3, 4], 2)         # All combinations
```

**Available Functions:**
- `hitung(start, step)` - Count iterator
- `siklus(iterable)` - Cycle iterator
- `ulangi(object, times)` - Repeat iterator
- `akumulasi(iterable, func)` - Accumulate
- `rantai(*iterables)` - Chain iterables
- `kompres(data, selectors)` - Compress
- `islice(iterable, start, stop, step)` - Slice iterator
- `zip_longest(*iterables, fillvalue)` - Zip with fill
- `produk(*iterables)` - Cartesian product
- `permutasi(iterable, r)` - Permutations
- `kombinasi(iterable, r)` - Combinations
- `kombinasi_dengan_pengulangan(iterable, r)` - Combinations with replacement
- `ambil_while(predicate, iterable)` - Take while
- `filterfalse(predicate, iterable)` - Filter false
- `grupby(iterable, key)` - Group by
- `batched(iterable, n)` - Batch into groups
- `chunked(iterable, n)` - Chunk iterator
- `sliding_window(iterable, n)` - Sliding windows
- `pairwise(iterable)` - Pairwise combinations
- `roundrobin(*iterables)` - Round-robin schedule
- `flatten(iterable)` - Flatten nested iterable
- `interleave(*iterables)` - Interleave iterables

### Collections Library (20+ functions) - `dari renzmc.library.collections impor *`

```python
dari renzmc.library.collections impor Antrian, Tumpukan, Counter, buat_counter

# Data structures
queue = Antrian()                            # Queue (FIFO)
stack = Tumpukan()                           # Stack (LIFO)
counter = buat_counter(["a", "b", "a"])      # Counter: {"a": 2, "b": 1}

# Queue operations
queue.masuk("item1")                        # Enqueue
item = queue.keluar()                       # Dequeue

# Stack operations
stack.dorong("item1")                       # Push
item = stack.ambil()                        # Pop
```

**Available Functions:**
- `Antrian(iterable)` - Queue class (FIFO)
- `Tumpukan(iterable)` - Stack class (LIFO)
- `DefaultDict(factory)` - Default dictionary
- `OrderedDict(*args)` - Ordered dictionary
- `Counter(iterable)` - Counter class
- `RantaiMap(*maps)` - Chain map
- `NamedTuple(name, fields)` - Named tuple factory
- `buat_antrian(iterable)` - Create queue
- `buat_tumpukan(iterable)` - Create stack
- `buat_defaultdict(factory)` - Create defaultdict
- `buat_ordered_dict(*args)` - Create ordered dict
- `buat_counter(iterable)` - Create counter
- `buat_chain_map(*maps)` - Create chain map
- `deque_siklus(iterable, maxlen)` - Cyclic deque
- `heapify(list)` - Convert to heap
- `heappush(heap, item)` - Push to heap
- `heappop(heap)` - Pop from heap
- `nlargest(n, iterable)` - N largest items
- `nsmallest(n, iterable)` - N smallest items

---

## Total Functions Summary

### Core Built-in Functions: 95+ Functions
- Type Conversion: 8 functions
- Input/Output: 12 functions  
- String Manipulation: 25+ functions
- Mathematics: 30+ functions
- List & Dictionary: 20+ functions

### Standard Library Functions: 85+ Functions
- UUID: 9 functions
- Base64: 8 functions
- Hashlib: 18 functions
- Urllib: 15 functions
- Regular Expression: 25 functions
- String: 30+ functions
- Pathlib: 20+ functions
- Itertools: 25+ functions
- Collections: 20+ functions

### **GRAND TOTAL: 180+ Functions**

Semua functions ini tersedia dalam **Bahasa Indonesia** dan dapat digunakan langsung atau dengan import library yang sesuai!
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