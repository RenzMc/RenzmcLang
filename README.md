# RenzMcLang

![RenzMcLanglogo](icon.png)

**Bahasa Pemrograman Berbasis Bahasa Indonesia yang Modern dan Powerful**

RenzMcLang adalah bahasa pemrograman yang menggunakan sintaks Bahasa Indonesia, dirancang untuk memudahkan pembelajaran pemrograman bagi penutur Bahasa Indonesia sambil tetap menyediakan fitur-fitur modern dan powerful.

[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-renzmc-blue.svg)](https://pypi.org/project/renzmc/)

## Fitur Utama

### Sintaks Bahasa Indonesia
- Keyword dalam Bahasa Indonesia yang intuitif
- Error messages yang helpful dalam Bahasa Indonesia
- Dokumentasi lengkap dalam Bahasa Indonesia

### Fitur Modern

#### JIT Compiler (Just-In-Time Compilation)
- Automatic Hot Function Detection - Deteksi otomatis fungsi yang sering dipanggil
- Numba Integration - Kompilasi ke native code menggunakan Numba
- 10-100x Performance Boost - Peningkatan performa signifikan untuk operasi numerik
- Zero Configuration - Bekerja otomatis tanpa setup
- Smart Type Inference - Sistem inferensi tipe untuk optimasi maksimal
- Fallback Safety - Fallback ke interpreter jika kompilasi gagal

#### Robust Type System
- Optional Type Hints - Type annotations opsional untuk variabel dan fungsi
- Runtime Type Validation - Validasi tipe saat runtime
- Bilingual Type Names - Dukungan nama tipe Indonesia dan Inggris
- Backward Compatible - 100% kompatibel dengan kode tanpa type hints
- Smart Type Inference - Inferensi tipe otomatis
- Clear Error Messages - Pesan error tipe yang jelas dan helpful

#### Advanced Programming Features
- Lambda Functions - Fungsi anonim untuk functional programming
- Comprehensions - List dan Dict comprehension untuk kode yang ringkas
- Ternary Operator - Kondisi inline yang elegant
- OOP - Object-Oriented Programming dengan class dan inheritance
- Async/Await - Pemrograman asynchronous
- Error Handling - Try-catch-finally yang robust
- Pattern Matching - Switch-case untuk control flow yang elegant
- Decorators - Function dan class decorators
- Generators - Yield untuk lazy evaluation
- Context Managers - With statement untuk resource management

### Integrasi Python
- Import dan gunakan library Python
- Akses Python builtins
- Interoperability penuh dengan ekosistem Python
- Call Python functions dari RenzMcLang
- Seamless data type conversion

### Built-in Functions Lengkap - 180+ Functions

#### Core Functions (95+ selalu tersedia):
- **Type Conversion** (8 functions): `str()`, `int()`, `float()`, `bool()`, `list()`, `dict()`, `tuple()`, `set()`
- **Input/Output** (12 functions): `tampilkan()`, `input()`, `baca_file()`, `tulis_file()`, `hapus_file()`, dll
- **String Manipulation** (25+ functions): `panjang()`, `huruf_besar()`, `huruf_kecil()`, `potong()`, `ganti()`, dll
- **Mathematics** (30+ functions): `abs()`, `round()`, `pow()`, `sqrt()`, `sin()`, `cos()`, `tan()`, `min()`, `max()`, dll
- **List & Dictionary** (20+ functions): `tambah()`, `hapus()`, `urutkan()`, `balik()`, dll

#### Standard Library Functions (85+ dengan import):
- **UUID** (9 functions): `buat_uuid4()`, `buat_uuid1()`, `uuid_valid()`, dll
- **Base64** (8 functions): `encode_base64()`, `decode_base64()`, dll
- **Hashlib** (18 functions): `hash_md5()`, `hash_sha256()`, `hash_sha512()`, `hmac_hash()`, dll
- **Urllib** (15 functions): `parse_url()`, `encode_url()`, `gabung_url()`, dll
- **Regular Expression** (25 functions): `validasi_email()`, `extract_angka()`, `cari_semua()`, dll
- **String Advanced** (30+ functions): `acak_alphanumeric()`, `caesar()`, `rot13()`, dll
- **Pathlib** (20+ functions): `Path()`, `path_current()`, `parse_url()`, dll
- **Itertools** (25+ functions): `hitung()`, `siklus()`, `permutasi()`, `kombinasi()`, dll
- **Collections** (20+ functions): `Antrian()`, `Tumpukan()`, `Counter()`, dll

**Total: 180+ fungsi dalam Bahasa Indonesia!**

[EXAMPLE WEBSITE YG PAKE BAHASA PEMROGRAMAN RENZMC](https://github.com/RenzMc/renzmc-website)

Bahasa pemrograman **RenzmcLang** sekarang sudah punya ekstensi VSCode - cek di [GitHub Renzmc Extension](https://github.com/RenzMc/renzmc-extension/tree/main)

## Instalasi

### Dari PyPI (Recommended)

```bash
pip install renzmc
```

### Dari Source

```bash
git clone https://github.com/RenzMc/RenzmcLang.git
cd RenzmcLang
pip install -e .
```

### Verifikasi Instalasi

```bash
renzmc --version
```

Atau jalankan contoh program:

```bash
renzmc examples/dasar/01_hello_world.rmc
```

## Quick Start

### Hello World

```python
tampilkan "Hello, World!"
```

### Variabel dan Tipe Data

```python
# Deklarasi variabel
nama itu "Budi"
umur itu 25
tinggi itu 175.5
is_student itu benar

# List
hobi itu ["membaca", "coding", "gaming"]

# Dictionary
profil itu {
    "nama": "Budi",
    "umur": 25,
    "kota": "Jakarta"
}
```

### Control Flow

```python
# If-else
jika umur >= 18
    tampilkan "Dewasa"
lainnya
    tampilkan "Anak-anak"
selesai

# Switch-case
cocok nilai
    kasus 1:
        tampilkan "Satu"
    kasus 2:
        tampilkan "Dua"
    bawaan:
        tampilkan "Lainnya"
selesai

# Ternary operator
status itu "Lulus" jika nilai >= 60 lainnya "Tidak Lulus"
```

### Loops

```python
# For loop
untuk x dari 1 sampai 10
    tampilkan x
selesai

# For each
untuk setiap item dari daftar
    tampilkan item
selesai

# While loop
selama kondisi
    # kode
selesai
```

```python
# Deklarasi fungsi
fungsi tambah(a, b):
    hasil a + b
selesai

# Lambda function
kuadrat itu lambda dengan x -> x * x

# Panggil fungsi
hasil itu tambah(5, 3)
tampilkan hasil  # Output: 8
```

### Comprehensions

```python
# List comprehension
kuadrat itu [x * x untuk setiap x dari angka]

# Dengan filter
genap itu [x untuk setiap x dari angka jika x % 2 == 0]

# Dict comprehension
kuadrat_dict itu {x: x * x untuk setiap x dari angka}
```

### OOP

```python
# Definisi class
kelas Mahasiswa:
    konstruktor(nama, nim):
        diri.nama itu nama
        diri.nim itu nim
    selesai
    
    metode perkenalan():
        tampilkan "Nama: " + diri.nama
        tampilkan "NIM: " + diri.nim
    selesai
selesai

# Buat instance
mhs itu Mahasiswa("Budi", "12345")
mhs.perkenalan()
```

### Python Integration

```python
// Import library Python
impor_python "requests"
impor_python "json"

// Gunakan library Python
response itu panggil_python requests.get("https://api.example.com/data")
data itu panggil_python json.loads(response.text)
tampilkan data
```

## Dokumentasi Lengkap

### Dokumentasi Online
Kunjungi [renzmc-docs.vercel.app](https://renzmc-docs.vercel.app/) untuk dokumentasi lengkap dan interaktif.

### Dokumentasi Lokal
Lihat folder [docs/](docs/) untuk dokumentasi lengkap

## Contoh Program

Lihat folder [examples/](examples/) untuk 130+ contoh program yang mencakup:

- **Dasar** - Hello World, kalkulator, loops
- **Intermediate** - Sorting algorithms, sistem login
- **Advanced** - Web scraping, OOP, async/await
- **Database** - SQLite, MySQL, PostgreSQL, MongoDB
- **Web Development** - HTTP server, REST API
- **Data Processing** - CSV, JSON, file operations
- **Dan banyak lagi!**

### Menjalankan Contoh

```bash
# Contoh dasar
renzmc examples/dasar/01_hello_world.rmc

# Contoh database
renzmc examples/database/01_sqlite_basic.rmc

# Contoh web scraping
renzmc examples/python_integration/01_web_scraping.rmc
```

**Made with love for Indonesian developers**

*"Coding in your native language, thinking in your native way"*

## Links

- [Documentation](https://github.com/RenzMc/RenzmcLang/docs)
- [PyPI Package](https://pypi.org/project/renzmc/)
- [Issue Tracker](https://github.com/RenzMc/RenzmcLang/issues)
- [Changelog](CHANGELOG.md)

**Star repository ini jika bermanfaat!**
