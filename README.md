# RenzMcLang 🚀
![RenzMcLanglogo](icon.png)

**Bahasa Pemrograman Berbasis Bahasa Indonesia yang Modern dan Powerful**

RenzMcLang adalah bahasa pemrograman yang menggunakan sintaks Bahasa Indonesia, dirancang untuk memudahkan pembelajaran pemrograman bagi penutur Bahasa Indonesia sambil tetap menyediakan fitur-fitur modern dan powerful.

[![Version](https://img.shields.io/badge/version-0.0.2-blue.svg)](https://github.com/RenzMc/RenzmcLang)
[![Python](https://img.shields.io/badge/python-3.6+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-renzmc-blue.svg)](https://pypi.org/project/renzmc/)

## ✨ Fitur Utama

### 🎯 Sintaks Bahasa Indonesia
- Keyword dalam Bahasa Indonesia yang intuitif
- Error messages yang helpful dalam Bahasa Indonesia
- Dokumentasi lengkap dalam Bahasa Indonesia

### 🔥 Fitur Modern
- **Lambda Functions** - Fungsi anonim untuk functional programming
- **Comprehensions** - List dan Dict comprehension untuk kode yang ringkas
- **Ternary Operator** - Kondisi inline yang elegant
- **OOP** - Object-Oriented Programming dengan class dan inheritance
- **Async/Await** - Pemrograman asynchronous
- **Error Handling** - Try-catch-finally yang robust
- **Type Hints** - Optional type annotations

### 🔌 Integrasi Python
- Import dan gunakan library Python
- Akses Python builtins
- Interoperability penuh dengan ekosistem Python

### 📦 Built-in Functions Lengkap
- String manipulation (143+ functions)
- Math & statistics
- File operations
- JSON utilities
- HTTP functions
- System operations
- Database operations
- Dan banyak lagi!

## 📥 Instalasi

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

## 🚀 Quick Start

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
kalau_tidak
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
status itu "Lulus" jika nilai >= 60 kalau tidak "Tidak Lulus"
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

### Functions

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

## 📚 Dokumentasi Lengkap

Lihat folder [docs/](docs/) untuk dokumentasi lengkap:

- [Panduan Instalasi](docs/installation.md)
- [Sintaks Dasar](docs/syntax-basics.md)
- [Built-in Functions](docs/builtin-functions.md)
- [OOP dan Advanced Features](docs/advanced-features.md)
- [Integrasi Python](docs/python-integration.md)
- [Contoh Program](docs/examples.md)

## 📖 Contoh Program

Lihat folder [examples/](examples/) untuk 80+ contoh program yang mencakup:

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

## 🎓 Tutorial

### 1. Instalasi dan Setup

```bash
# Install dari PyPI
pip install renzmc

# Verifikasi instalasi
renzmc --version

# Jalankan REPL (coming soon)
renzmc
```

### 2. Program Pertama

Buat file `hello.rmc`:

```python
tampilkan "Hello, World!"
tampilkan "Selamat datang di RenzMcLang!"
```

Jalankan:

```bash
renzmc hello.rmc
```

### 3. Program dengan Input

```python
tampilkan "Siapa nama Anda?"
nama itu input()
tampilkan "Halo, " + nama + "!"
```

### 4. Program Kalkulator

```python
tampilkan "=== Kalkulator Sederhana ==="
tampilkan "Masukkan angka pertama:"
a itu ke_angka(input())

tampilkan "Masukkan angka kedua:"
b itu ke_angka(input())

tampilkan "Pilih operasi (+, -, *, /):"
op itu input()

jika op == "+"
    hasil itu a + b
kalau_tidak_jika op == "-"
    hasil itu a - b
kalau_tidak_jika op == "*"
    hasil itu a * b
kalau_tidak_jika op == "/"
    hasil itu a / b
kalau_tidak
    tampilkan "Operasi tidak valid"
    keluar
selesai

tampilkan f"Hasil: {hasil}"
```

## 🔧 Pengembangan

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/RenzMc/RenzmcLang.git
cd RenzmcLang

# Install dalam mode development
pip install -e .

# Install development dependencies
pip install pytest black flake8
```

### Menjalankan Tests

```bash
# Test semua examples
python test_examples.py

# Test specific file
renzmc examples/test_all/test_all_features.rmc
```

### Struktur Project

```
RenzmcLang/
├── renzmc/              # Source code
│   ├── core/           # Lexer, Parser, Interpreter
│   ├── runtime/        # Runtime features
│   ├── builtins/       # Built-in functions
│   └── utils/          # Utilities
├── examples/           # 80+ contoh program
├── docs/              # Dokumentasi lengkap
├── tests/             # Unit tests
└── README.md          # File ini
```

## 🐛 Troubleshooting

### Import Error

```python
// ❌ Salah
impor sqlite3

// ✅ Benar
impor_python "sqlite3"
```

### Syntax Error

```python
// ❌ Salah
jika x bukan dalam list

// ✅ Benar
jika x tidak dalam list
```

### File Not Found

```python
// Pastikan path relatif benar
dengan buka("data.txt", "r") sebagai f
    # kode
selesai
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👥 Authors

- **RenzMc** - *Initial work* - [RenzMc](https://github.com/RenzMc)

## 📞 Contact

- GitHub: [@RenzMc](https://github.com/RenzMc)
- Email: renzaja11@gmail.com
---

**Made with ❤️ for Indonesian developers**

*"Coding in your native language, thinking in your native way"*

## 🎯 Use Cases

RenzMcLang cocok untuk:
- 📚 **Pembelajaran**: Belajar programming dengan bahasa Indonesia
- 🔬 **Prototyping**: Rapid application development
- 📊 **Data Processing**: Analisis dan transformasi data
- 🌐 **Web Development**: Backend API development
- 🗄️ **Database Operations**: Database management dan queries
- 🤖 **Automation**: Script automation dan task scheduling

## 💡 Tips & Best Practices

### Best Practices
1. Gunakan nama variabel yang deskriptif
2. Tambahkan komentar untuk kode kompleks
3. Manfaatkan built-in functions
4. Gunakan error handling yang proper
5. Test kode secara berkala

### Performance Tips
1. Gunakan comprehensions untuk operasi list
2. Manfaatkan built-in functions yang sudah dioptimasi
3. Hindari nested loops yang dalam
4. Gunakan generator untuk data besar
5. Profile kode untuk menemukan bottleneck

## 🔗 Links

- [Documentation](https://github.com/RenzMc/RenzmcLang/docs)
- [PyPI Package](https://pypi.org/project/renzmc/)
- [Issue Tracker](https://github.com/RenzMc/RenzmcLang/issues)
- [Changelog](CHANGELOG.md)

**Star ⭐ repository ini jika bermanfaat!**
