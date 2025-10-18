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

### Built-in Functions Lengkap
- String manipulation (148+ functions)
- Math & statistics - Operasi matematika lengkap
- File operations - Read, write, manipulasi file
- JSON utilities - Parse dan generate JSON
- HTTP functions - HTTP client built-in
- System operations - Akses sistem operasi
- Database operations - SQLite, MySQL, PostgreSQL, MongoDB
- Crypto operations - Enkripsi dan hashing
- Date/Time - Manipulasi tanggal dan waktu
- Dan banyak lagi!

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
Lihat folder [docs/](docs/) untuk dokumentasi lengkap:

#### Panduan Dasar
- [Panduan Instalasi](docs/installation.md) - Cara install dan setup RenzmcLang
- [Sintaks Dasar](docs/syntax-basics.md) - Pelajari sintaks dasar bahasa
- [Quick Reference](docs/quick-reference.md) - Cheat sheet untuk referensi cepat

#### Fitur & Fungsi
- [Built-in Functions](docs/builtin-functions.md) - 184+ fungsi built-in lengkap
- [Advanced Features](docs/advanced-features.md) - OOP, async/await, decorators, dll
- [JIT Compiler](docs/jit-compiler.md) - Kompilasi JIT untuk performa maksimal
- [Type System](docs/type-system.md) - Sistem tipe opsional dengan validasi runtime

#### Integrasi & Tools
- [Integrasi Python](docs/python-integration.md) - Gunakan library Python di RenzmcLang
- [HTTP Client Guide](docs/http-client-guide.md) - HTTP client built-in untuk API calls
- [Contoh Program](docs/examples.md) - 80+ contoh program siap pakai

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

## Authors

- **RenzMc** - *Initial work* - [RenzMc](https://github.com/RenzMc)

## Contact

- GitHub: [@RenzMc](https://github.com/RenzMc)
- Email: renzaja11@gmail.com
---

**Made with love for Indonesian developers**

*"Coding in your native language, thinking in your native way"*

## Use Cases

RenzMcLang cocok untuk:
- Pembelajaran: Belajar programming dengan bahasa Indonesia
- Prototyping: Rapid application development
- Data Processing: Analisis dan transformasi data dengan JIT acceleration
- Web Development: Backend API development
- Database Operations: Database management dan queries
- Automation: Script automation dan task scheduling
- Scientific Computing: Komputasi numerik dengan JIT compiler
- Algorithm Implementation: Implementasi algoritma dengan performa tinggi
- Game Logic: Game logic dengan type safety
- Mathematical Modeling: Pemodelan matematika dengan JIT optimization

## Tips & Best Practices

### Best Practices
1. Gunakan nama variabel yang deskriptif
2. Tambahkan komentar untuk kode kompleks
3. Manfaatkan built-in functions
4. Gunakan error handling yang proper
5. Test kode secara berkala
6. Gunakan type hints untuk fungsi publik
7. Manfaatkan JIT compiler untuk operasi numerik intensif

### Performance Tips
1. Leverage JIT Compiler - Fungsi numerik dengan loop akan otomatis dioptimasi
2. Use Type Hints - Membantu JIT compiler mengoptimasi lebih baik
3. Gunakan comprehensions untuk operasi list
4. Manfaatkan built-in functions yang sudah dioptimasi
5. Hindari nested loops yang dalam (atau biarkan JIT mengoptimasi)
6. Gunakan generator untuk data besar
7. Profile kode untuk menemukan bottleneck
8. Pisahkan operasi numerik ke fungsi terpisah untuk JIT optimization

### JIT Optimization Tips
1. Keep Functions Pure - Fungsi tanpa side effects lebih mudah dioptimasi
2. Use Numeric Types - Integer dan Float mendapat benefit terbesar
3. Minimize External Calls - Fungsi self-contained lebih cepat dikompilasi
4. Let It Warm Up - Biarkan fungsi dipanggil 10+ kali untuk trigger JIT
5. Check Compilation - Fungsi dengan loop dan operasi kompleks akan dikompilasi

## Links

- [Documentation](https://github.com/RenzMc/RenzmcLang/docs)
- [PyPI Package](https://pypi.org/project/renzmc/)
- [Issue Tracker](https://github.com/RenzMc/RenzmcLang/issues)
- [Changelog](CHANGELOG.md)

**Star repository ini jika bermanfaat!**