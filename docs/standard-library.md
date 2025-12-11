# RenzMcLang Standard Library

## Table of Contents

1. [Introduction](#introduction)
2. [Import System](#import-system)
3. [Available Libraries](#available-libraries)
4. [Library Reference](#library-reference)
   - [math](#math)
   - [json](#json)
   - [http](#http)
   - [os](#os)
   - [datetime](#datetime)
   - [statistics](#statistics)
   - [random](#random)
   - [fileio](#fileio)
   - **[NEW] uuid](#uuid)**
   - **[NEW] base64](#base64)**
   - **[NEW] hashlib](#hashlib)**
   - **[NEW] urllib](#urllib)**
   - **[NEW] re (Regular Expressions)](#re-regular-expressions)**
   - **[NEW] string](#string)**
   - **[NEW] pathlib](#pathlib)**
   - **[NEW] itertools](#itertools)**
   - **[NEW] collections](#collections)**
5. [Migration Guide](#migration-guide)
6. [Examples](#examples)

---

## Introduction

RenzMcLang Standard Library menyediakan koleksi modul-modul esensial untuk pemrograman sehari-hari. Terinspirasi dari Python's standard library, dirancang dengan nama fungsi dalam Bahasa Indonesia dan mendukung alias Python untuk kompatibilitas.

### Key Features:
- **Bilingual Function Names**: Nama fungsi dalam Bahasa Indonesia + alias Python
- **Comprehensive Documentation**: Dokumentasi lengkap dengan contoh
- **Type Hints**: Support untuk type hints
- **Error Handling**: Error handling yang konsisten
- **Modular Design**: Arsitektur modular yang mudah diperluas

---

## Import System

RenzMcLang menyediakan dua cara untuk mengimport library:

### 1. Import Seluruh Library
```python
# Import seluruh library math
impor math

# Gunakan fungsi
hasil = math.sin(0.5)
hasil2 = math.sinus(0.5)  # Indonesian alias
```

### 2. Import Fungsi Spesifik
```python
# Import fungsi spesifik dari library math
dari math impor sin, cos, tan

# Import dengan alias
dari math impor sin sebagai sinus

# Gunakan fungsi langsung
hasil = sin(0.5)
```

### 3. Import Multiple Functions
```python
# Import banyak fungsi
dari statistics impor mean, median, stdev
dari json impor loads, dumps
```

---

## Available Libraries

### Core Libraries:
- **math**: Fungsi matematika dan konstanta
- **json**: JSON encoding/decoding
- **http**: HTTP client functionality
- **os**: Operating system interface
- **datetime**: Date dan time operations
- **statistics**: Statistical functions
- **random**: Random number generation
- **fileio**: File I/O operations

### Library Functions:
```python
# Dapatkan daftar semua available libraries
libraries = dapatkan_library()

# Dapatkan info tentang library spesifik
info = info_library('math')
```

---

## Library Reference

### math

Library untuk operasi matematika.

```python
# Constants
dari math impor pi, e, tau

# Basic Operations
dari math impor abs, sqrt, pow, round
hasil = akar(16)  # 4.0
hasil2 = pangkat(2, 3)  # 8.0

# Trigonometry
dari math impor sin, cos, tan, asin, acos, atan
sudut = pi / 4
hasil_sin = sin(sudut)

# Logarithms
dari math impor log, log10, log2
log_result = log(100, 10)  # 2.0

# Conversion
dari math impor degrees, radians
derajat = degrees(pi)  # 180.0

# Indonesian Aliases
dari math impor sinus, cosinus, tangen
hasil = sinus(0.5)
```

#### Available Functions:
- **Constants**: `pi`, `e`, `tau`, `inf`, `nan`
- **Basic**: `abs`, `sqrt`, `pow`, `round`, `ceil`, `floor`
- **Trigonometry**: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`
- **Logarithms**: `log`, `log10`, `log2`, `ln`
- **Conversion**: `degrees`, `radians`
- **Hyperbolic**: `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`
- **Special**: `factorial`, `gcd`, `lcm`

---

### json

Library untuk JSON encoding/decoding.

```python
dari json impor loads, dumps, load, dump

# Parse JSON string
json_str = '{"nama": "Budi", "umur": 25}'
data = loads(json_str)

# Convert object ke JSON
data = {"nama": "Budi", "umur": 25}
json_str = dumps(data, indent=2)

# Read dari file
data = load(open_file('data.json'))

# Write ke file
dump(data, open_file('output.json', 'w'), indent=2)
```

#### Available Functions:
- **Parsing**: `loads`, `load`
- **Encoding**: `dumps`, `dump`
- **Utilities**: `validate_json`, `format_json`, `minify_json`

---

### http

HTTP client untuk web requests.

```python
dari http impor get, post, put, delete, patch

# GET request
response = get('https://api.example.com/data')
if response.ok():
    data = response.json()
    print(f"Status: {response.status_code}")

# POST request
data = {"nama": "Budi", "email": "budi@example.com"}
response = post('https://api.example.com/users', json=data)

# PUT request
response = put('https://api.example.com/users/1', json={"nama": "Budi Updated"})

# DELETE request
response = delete('https://api.example.com/users/1')
```

#### Available Functions:
- **HTTP Methods**: `get`, `post`, `put`, `delete`, `patch`, `head`, `options`
- **Classes**: `HTTPResponse`, `HTTPSession`
- **Utilities**: `set_default_header`, `create_session`

---

### os

Operating system interface.

```python
dari os impor getcwd, chdir, listdir, mkdir, exists

# Current directory
cwd = getcwd()
print(f"Current directory: {cwd}")

# List files
files = list_dir('.')
print(f"Files: {files}")

# Create directory
buat_dir('data', exist_ok=True)

# Check if exists
if exists('file.txt'):
    print("File exists")

# Environment variables
dari os impor getenv, setenv
path = getenv('PATH', '')
atur_env('MY_VAR', 'hello')
```

#### Available Functions:
- **Path Operations**: `getcwd`, `chdir`, `listdir`, `exists`, `isfile`, `isdir`
- **File Operations**: `mkdir`, `makedirs`, `remove`, `rename`
- **Environment**: `getenv`, `setenv`, `unsetenv`, `environ`
- **Process**: `getpid`, `system`

---

### datetime

Date dan time operations.

```python
dari datetime impor datetime, timedelta, sekarang, hari_ini

# Current datetime
sekarang = sekarang()
print(f"Sekarang: {sekarang}")

# Current date
today = hari_ini()
print(f"Hari ini: {today}")

# Date arithmetic
dari datetime impor timedelta
besok = sekarang + timedelta(hari=1)
minggu_depan = sekarang + timedelta(minggu=1)

# Parse date string
dari datetime impor strptime
date_obj = strptime('01/01/2025', '%d/%m/%Y')
```

#### Available Functions:
- **Current Time**: `sekarang`, `hari_ini`, `utc_sekarang`
- **Parsing**: `strptime`, `parse_isoformat`
- **Classes**: `datetime`, `date`, `time`, `timedelta`

---

### statistics

Statistical functions.

```python
dari statistics impor mean, median, mode, stdev, variance

data = [1, 2, 3, 4, 5]

# Measures of central tendency
rata = mean(data)  # 3.0
tengah = median(data)  # 3
modus = mode(data)  # Error: no unique mode

# Measures of spread
deviasi = stdev(data)  # ~1.58
varian = variance(data)  # 2.5

# Additional statistics
dari statistics impor geometric_mean, harmonic_mean, quantiles
gm = geometric_mean([1, 4, 9])  # ~3.36
quartiles = quantiles(data, n=4)
```

#### Available Functions:
- **Central Tendency**: `mean`, `median`, `mode`, `multimode`
- **Spread**: `stdev`, `pstdev`, `variance`, `pvariance`
- **Other Means**: `geometric_mean`, `harmonic_mean`
- **Quantiles**: `quantiles`

---

### random

Random number generation.

```python
dari random impor random, randint, choice, shuffle

# Random float 0-1
angka = random()  # 0.123456789

# Random integer
dadu = randint(1, 6)  # 1-6

# Random choice
pilihan = choice(['a', 'b', 'c'])

# Shuffle list
items = [1, 2, 3, 4, 5]
shuffle(items)

# Multiple choices
pilihan = choices(['a', 'b', 'c'], k=3)

# Random sample
sample = sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3)
```

#### Available Functions:
- **Basic**: `random`, `randint`, `randrange`, `uniform`
- **Sequences**: `choice`, `choices`, `sample`, `shuffle`
- **Distributions**: `gauss`, `normalvariate`, `expovariate`

---

### fileio

File I/O operations.

```python
dari fileio impor read_text, write_text, read_json, write_json

# Read text file
content = read_text('data.txt')

# Write text file
write_text('output.txt', 'Hello World')

# Read JSON file
data = read_json('config.json')

# Write JSON file
write_json('output.json', {"key": "value"}, indent=2)

# Read lines
lines = read_lines('data.txt')

# Write lines
write_lines('output.txt', ['line1', 'line2'])

# File operations
dari fileio impor copy, move, delete, exists
copy('source.txt', 'backup.txt')
move('old.txt', 'new.txt')
delete('temp.txt')
```

#### Available Functions:
- **Reading**: `read_text`, `read_lines`, `read_bytes`, `read_json`, `read_csv`
- **Writing**: `write_text`, `write_lines`, `write_bytes`, `write_json`, `write_csv`
- **Operations**: `copy`, `move`, `delete`, `exists`, `size`
- **Directory**: `create_dir`, `remove_dir`, `list_dir`, `walk_dir`

---

## Migration Guide

### Dari Built-in Functions ke Standard Library

Beberapa fungsi yang sebelumnya built-in sekarang dipindahkan ke standard library:

#### Math Functions:
```python
# Sebelumnya (built-in)
hasil = sin(0.5)
hasil2 = akar(16)

# Sekarang (standard library)
dari math impor sin, akar
hasil = sin(0.5)
hasil2 = akar(16)
```

#### JSON Functions:
```python
# Sebelumnya (built-in)
data = teks_ke_json(json_str)
json_str = json_ke_teks(data)

# Sekarang (standard library)
dari json impor loads, dumps
data = loads(json_str)
json_str = dumps(data)
```

#### HTTP Functions:
```python
# Sebelumnya (built-in)
response = http_get('https://api.example.com')
response = ambil_http('https://api.example.com')

# Sekarang (standard library)
dari http impor get, ambil
response = get('https://api.example.com')
response = ambil('https://api.example.com')
```

#### File Functions:
```python
# Sebelumnya (built-in)
content = baca_file('data.txt')
tulis_file('output.txt', content)

# Sekarang (standard library)
dari fileio impor read_text, write_text
content = read_text('data.txt')
write_text('output.txt', content)
```

### Backward Compatibility

Untuk backward compatibility, beberapa built-in function tetap available dengan warning:

```python
# Built-in functions yang tetap available (deprecated)
tampilkan("Hello")  # print()
masukan("Name: ")   # input()
panjang("string")   # len()
jenis(value)        # type()
```

---

## Examples

### Example 1: Data Processing Pipeline

```python
// Import libraries yang diperlukan
dari json impor read_json, write_json
dari statistics impor mean, median, stdev
dari fileio impor read_text, write_text

// Baca data JSON
data = read_json('sales_data.json')

// Proses data
sales = data['sales']
rata_sales = mean(sales)
median_sales = median(sales)
std_sales = stdev(sales)

// Buat report
report = {
    "total_sales": len(sales),
    "average": rata_sales,
    "median": median_sales,
    "std_dev": std_sales
}

// Simpan hasil
write_json('sales_report.json', report, indent=2)
tampilkan(f"Report saved! Average: {rata_sales}")
```

### Example 2: Web API Client

```python
// Import HTTP dan JSON libraries
dari http impor get, post, create_session
dari json impor dumps

// Create session untuk persistent connection
session = buat_session()

// GET data
response = session.get('https://api.example.com/users')
if response.ok():
    users = response.json()
    tampilkan(f"Found {panjang(users)} users")

// POST new data
new_user = {
    "name": "Budi",
    "email": "budi@example.com",
    "age": 25
}

response = session.post('https://api.example.com/users', json=new_user)
if response.ok():
    tampilkan("User created successfully!")
    result = response.json()
    tampilkan(f"User ID: {result['id']}")
```

### Example 3: File Processing with Statistics

```python
// Import required libraries
dari fileio impor read_csv, write_json
dari statistics impor mean, median, stdev, quantiles
dari datetime impor sekarang

// Baca CSV data
rows = read_csv('data.csv', delimiter=';')

// Skip header dan extract numeric column
numeric_data = []
untuk setiap row dari rows[1:]:  // Skip header
    jika panjang(row) > 1:
        value = ke_angka(row[1])
        numeric_data.append(value)

// Hitung statistik
stats = {
    "count": panjang(numeric_data),
    "mean": mean(numeric_data),
    "median": median(numeric_data),
    "stdev": stdev(numeric_data),
    "quartiles": quantiles(numeric_data, n=4),
    "processed_at": str(sekarang())
}

// Simpan hasil
write_json('statistics.json', stats, indent=2)
tampilkan("Statistical analysis complete!")
```

### Example 4: Mathematical Calculations

```python
// Import math library
dari math impor pi, sin, cos, tan, sqrt, log, pangkat

// Trigonometry calculations
sudut = pi / 4  // 45 derajat
hasil_sin = sin(sudut)
hasil_cos = cos(sudut)
hasil_tan = tan(sudut)

// Mathematical operations
angka = 16
akar_kuadrat = sqrt(angka)
hasil_pangkat = pangkat(2, 8)  // 256
hasil_log = log(100, 10)  // 2.0

// Tampilkan hasil
tampilkan(f"Sin({sudut}) = {hasil_sin}")
tampilkan(f"Cos({sudut}) = {hasil_cos}")
tampilkan(f"Tan({sudut}) = {hasil_tan}")
tampilkan(f"Akar {angka} = {akar_kuadrat}")
tampilkan(f"2 pangkat 8 = {hasil_pangkat}")
tampilkan(f"Log 100 basis 10 = {hasil_log}")
```

---

## Tips and Best Practices

### 1. Use Specific Imports
```python
// Good: Import only what you need
dari math impor sin, cos, tan

// Avoid: Import entire library jika tidak perlu
impor math
```

### 2. Use Indonesian Names for Readability
```python
// Good: Indonesian names
dari statistics impor mean, median, stdev sebagai deviasi_standar

// Also Good: Mix with Indonesian
rata = mean(data)
tengah = median(data)
deviasi = deviasi_standar(data)
```

### 3. Handle Exceptions
```python
dari json impor loads, dumps

coba:
    data = loads(json_string)
tangkap JSONDecodeError sebagai e:
    tampilkan(f"Invalid JSON: {e}")
```

### 4. Use Context Managers for Files
```python
dari fileio impor open_text

dengan open_text('data.txt', 'r') sebagai f:
    content = f.read()
    // Process content
```

### 5. Check Response Status for HTTP
```python
dari http impor get

response = get('https://api.example.com/data')
jika response.ok():
    data = response.json()
kalau_tidak:
    tampilkan(f"Error: {response.status_code}")
```

---

## New Standard Libraries (Available in v1.0+)

### uuid
Library untuk generating UUID (Universally Unique Identifier).

```python
dari renzmc.library.uuid impor buat_uuid4, buat_uuid1, uuid_valid

# Generate UUID4 (random)
uuid_random itu buat_uuid4()

# Generate UUID1 (host+time)  
uuid_time itu buat_uuid1()

# Validate UUID
is_valid itu uuid_valid(uuid_random)
```

**Available Functions:**
- `buat_uuid4()` - Generate random UUID
- `buat_uuid1()` - Generate UUID based on host+time
- `buat_uuid3(namespace, name)` - Generate UUID from MD5 hash
- `buat_uuid5(namespace, name)` - Generate UUID from SHA-1 hash
- `uuid_valid(string)` - Validate UUID format
- `parse_uuid(string)` - Parse UUID string

### base64
Library untuk Base64 encoding dan decoding.

```python
dari renzmc.library.base64 impor encode_base64, decode_base64

# Encode string
encoded itu encode_base64("Hello RenzMcLang!")

# Decode Base64
decoded itu decode_base64(encoded)
```

**Available Functions:**
- `encode_base64(data)` - Encode ke Base64
- `decode_base64(encoded)` - Decode Base64
- `encode_base64_urlsafe(data)` - URL-safe encoding
- `decode_base64_urlsafe(encoded)` - URL-safe decoding
- `encode_base64_file(path)` - Encode file
- `decode_base64_ke_file(encoded, path)` - Decode ke file
- `base64_valid(data)` - Validate Base64 format

### hashlib
Library untuk hash functions dan cryptography.

```python
dari renzmc.library.hashlib impor hash_md5, hash_sha256, hmac_hash

# Hash strings
md5_hash itu hash_md5("secret data")
sha256_hash itu hash_sha256("important message")

# HMAC for security
signature itu hmac_hash("data", "secret_key")
```

**Available Functions:**
- `hash_md5(data)` - MD5 hash
- `hash_sha1(data)` - SHA1 hash
- `hash_sha256(data)` - SHA256 hash
- `hash_sha512(data)` - SHA512 hash
- `hash_file_md5(path)` - Hash file MD5
- `hmac_hash(data, key)` - HMAC signature
- `buat_salt(length)` - Generate random salt
- `hash_with_salt(data, salt)` - Hash dengan salt

### urllib
Library untuk URL handling dan manipulation.

```python
dari renzmc.library.urllib impor parse_url, gabung_url, encode_url

# Parse URL components
parsed itu parse_url("https://example.com/path?query=value")

# Join URLs
full_url itu gabung_url("https://api.com", "v1", "users")

# Encode parameters
encoded itu encode_url({"name": "John", "age": 25})
```

**Available Functions:**
- `parse_url(url)` - Parse URL components
- `buat_url(scheme, netloc, path, query)` - Build URL
- `encode_url(params)` - Encode URL parameters
- `decode_url(encoded)` - Decode URL parameters
- `gabung_url(base, *paths)` - Join multiple URLs
- `download_url(url, path)` - Download content from URL

### re (Regular Expressions)
Library untuk regular expression operations.

```python
dari renzmc.library.re impor validasi_email, extract_angka, cari_semua

# Validate email
is_valid_email itu validasi_email("user@example.com")

# Extract numbers from text
numbers itu extract_angka("Harga: Rp 150.000")

# Find all matches
matches itu cari_semua(r"\bword\b", text_content)
```

**Available Functions:**
- `validasi_email(email)` - Validate email format
- `validasi_telepon(phone)` - Validate Indonesian phone
- `validasi_url(url)` - Validate URL format
- `extract_email(text)` - Extract all emails
- `extract_url(text)` - Extract all URLs
- `extract_angka(text)` - Extract numbers
- `cari(pattern, string)` - Search pattern
- `cari_semua(pattern, string)` - Find all matches
- `ganti(pattern, replacement, string)` - Replace all

### string (Advanced)
Library untuk advanced string operations.

```python
dari renzmc.library.string impor acak_alphanumeric, caesar, rot13

# Generate random string
random_str itu acak_alphanumeric(10)

# Caesar cipher
encrypted itu caesar("Secret Message", 3)
decrypted itu caesar(encrypted, -3)

# ROT13 encoding
encoded itu rot13("Hidden text")
```

**Available Functions:**
- `acak_alphanumeric(length)` - Random alphanumeric string
- `acak_huruf(length)` - Random letters string
- `acak_angka(length)` - Random numbers string
- `caesar(text, shift)` - Caesar cipher
- `rot13(text)` - ROT13 encoding
- `hitung_vokal(text)` - Count vowels
- `hitung_konsonan(text)` - Count consonants
- `extract_angka(text)` - Extract numbers only
- `bersihkan_spasi(text)` - Clean whitespace

### pathlib
Library untuk object-oriented path manipulation.

```python
dari renzmc.library.pathlib impor Path, path_current, path_home

# Create path object
file_path itu Path("documents", "report.pdf")

# Get current/home directories
current_dir itu path_current()
home_dir itu path_home()

# Path operations
nama_file itu file_path.dapatkan_nama()  # "report.pdf"
extension itu file_path.dapatkan_extension()  # ".pdf"
parent_dir itu file_path.dapatkan_parent()  # "documents"
```

**Available Functions:**
- `Path(*segments)` - Path object constructor
- `path_current()` - Current working directory
- `path_home()` - Home directory
- `path_temp()` - Temporary directory
- `gabung_path(*paths)` - Join multiple paths
- `get_extension(path)` - Get file extension
- `get_filename(path)` - Get filename
- `get_basename(path)` - Get basename without extension

### itertools
Library untuk iterator operations dan utilities.

```python
dari renzmc.library.itertools impor hitung, siklus, permutasi, kombinasi

# Infinite counter
counter itu hitung(0, 2)  # 0, 2, 4, 6, 8, ...

# Cycle through list
cycler itu siklus([1, 2, 3])  # 1, 2, 3, 1, 2, 3, ...

# Generate permutations
perms itu permutasi([1, 2, 3])

# Generate combinations
combs itu kombinasi([1, 2, 3, 4], 2)
```

**Available Functions:**
- `hitung(start, step)` - Infinite counter
- `siklus(iterable)` - Cycle through iterable
- `ulangi(object, times)` - Repeat object
- `akumulasi(iterable, func)` - Accumulate results
- `rantai(*iterables)` - Chain multiple iterables
- `permutasi(iterable, r)` - Generate permutations
- `kombinasi(iterable, r)` - Generate combinations
- `islice(iterable, start, stop, step)` - Slice iterator
- `batched(iterable, n)` - Batch into groups

### collections
Library untuk advanced data structures.

```python
dari renzmc.library.collections impor Antrian, Tumpukan, Counter, buat_counter

# Queue (FIFO)
queue itu Antrian()
queue.masuk("item1")
item itu queue.keluar()

# Stack (LIFO)
stack itu Tumpukan()
stack.dorong("item1")
item itu stack.ambil()

# Counter (like multiset)
counter itu buat_counter(["a", "b", "a", "c"])
count_a itu counter.dapatkan("a")  # 2
```

**Available Functions:**
- `Antrian(iterable)` - Queue (FIFO) with enqueue/dequeue
- `Tumpukan(iterable)` - Stack (LIFO) with push/pop
- `Counter(iterable)` - Counter for counting elements
- `DefaultDict(factory)` - Dictionary with default values
- `OrderedDict()` - Dictionary that preserves insertion order
- `buat_antrian(iterable)` - Create queue
- `buat_tumpukan(iterable)` - Create stack
- `buat_counter(iterable)` - Create counter

---

## See Also

- [Built-in Functions](builtin-functions.md) - 180+ built-in functions lengkap
- [Syntax Basics](syntax-basics.md) - Basic syntax RenzMcLang
- [Advanced Features](advanced-features.md) - Advanced language features
- [Examples](examples.md) - More code examples
- [Installation](installation.md) - Installation guide

---

## Complete Library List

**Total Standard Libraries: 17**
1. math - Mathematics functions
2. json - JSON operations
3. http - HTTP client
4. os - Operating system interface
5. datetime - Date and time operations
6. statistics - Statistical functions
7. random - Random number generation
8. fileio - File I/O operations
9. **uuid** - UUID generation *(NEW)*
10. **base64** - Base64 encoding *(NEW)*
11. **hashlib** - Hash functions *(NEW)*
12. **urllib** - URL handling *(NEW)*
13. **re** - Regular expressions *(NEW)*
14. **string** - Advanced string operations *(NEW)*
15. **pathlib** - Path manipulation *(NEW)*
16. **itertools** - Iterator utilities *(NEW)*
17. **collections** - Advanced data structures *(NEW)*

**Total Functions: 180+** (95 core functions + 85+ standard library functions)