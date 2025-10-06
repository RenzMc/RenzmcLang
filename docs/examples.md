# 📚 RenzMcLang Examples - Comprehensive Guide

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)  
**Total Examples:** 99

---

## 📋 Table of Contents

1. [Advanced](#advanced)
2. [Advanced Features](#advanced-features)
3. [Advanced Operators](#advanced-operators)
4. [Algorithms](#algorithms)
5. [Builtin Functions](#builtin-functions)
6. [Cli Tools](#cli-tools)
7. [Concurrency](#concurrency)
8. [Control Flow](#control-flow)
9. [Dasar](#dasar)
10. [Data Structures](#data-structures)
11. [Database](#database)
12. [Datetime Operations](#datetime-operations)
13. [Dict Operations](#dict-operations)
14. [Email](#email)
15. [Error Handling](#error-handling)
16. [File Processing](#file-processing)
17. [Functional Programming](#functional-programming)
18. [Functions](#functions)
19. [Games](#games)
20. [Gui](#gui)
21. [Http Client](#http-client)
22. [Image Processing](#image-processing)
23. [Intermediate](#intermediate)
24. [List Operations](#list-operations)
25. [Logging](#logging)
26. [Multiprocessing](#multiprocessing)
27. [Networking](#networking)
28. [Operators](#operators)
29. [Practical](#practical)
30. [Projects](#projects)
31. [Python Integration](#python-integration)
32. [Regex](#regex)
33. [Root](#root)
34. [String Operations](#string-operations)
35. [Test All](#test-all)
36. [Testing](#testing)
37. [Utilities](#utilities)
38. [Web Development](#web-development)

---

## Advanced

**Total Examples:** 1

### 1. 01 Web Scraper

**File:** `advanced/01_web_scraper.rmc`  
**Description:** Contoh: Data Processing (Simplified)  
**Lines:** 78

**Code Preview:**

```python
// ============================================
// Contoh: Data Processing (Simplified)
// ============================================

tampilkan "=== DEMO DATA PROCESSING ==="
tampilkan ""

// Simulasi data dari API (dalam bentuk dictionary)
data itu [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "city": "Jakarta"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "city": "Bandung"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "city": "Surabaya"},
    {"id": 4, "name": "Diana", "email": "diana@example.com", "city": "Jakarta"},
    {"id": 5, "name": "Eve", "email": "eve@example.com", "city": "Bandung"}
]

tampilkan f"✓ Data berhasil dimuat!"
tampilkan f"Jumlah item: {panjang(data)}"

// Tampilkan preview (3 item pertama)
// ... (more code)

```

---

## Advanced Features

**Total Examples:** 4

### 1. 01 Oop Classes

**File:** `advanced_features/01_oop_classes.rmc`  
**Description:** Advanced Features: OOP - Classes & Objects  
**Lines:** 317

**Code Preview:**

```python
// ============================================
// Advanced Features: OOP - Classes & Objects
// ============================================
// Comprehensive examples for Object-Oriented Programming
// Using function-based approach (RenzMcLang style)

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║     OOP: CLASSES & OBJECTS            ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. BASIC CLASS: Person
// ============================================
tampilkan "=== 1. BASIC CLASS: Person ==="
tampilkan ""

// Constructor
buat fungsi buat_orang dengan nama, umur
    orang itu {
// ... (more code)

```

---

### 2. 01 With Statement

**File:** `advanced_features/01_with_statement.rmc`  
**Description:** 01 With Statement  
**Lines:** 236

**Code Preview:**

```python
# ============================================
# WITH STATEMENT (CONTEXT MANAGER) - STATUS
# ============================================
# The 'dengan...sebagai...selesai' statement is implemented in RenzmcLang
# to support Python's context manager protocol.
#
# Syntax: dengan <context_manager> sebagai <variable>
#             <code block>
#         selesai
#
# CURRENT STATUS:
# - The with statement parser and interpreter are fully implemented
# - However, there are no built-in RenzmcLang functions that return
#   context manager objects (objects with __enter__ and __exit__ methods)
# - The built-in file functions (baca_file, tulis_file) work with
#   complete files, not file objects
#
# This example demonstrates:
# 1. The current file handling approach in RenzmcLang
# 2. How the with statement would work (conceptually)
// ... (more code)

```

---

### 3. 02 Async Await

**File:** `advanced_features/02_async_await.rmc`  
**Description:** 02 Async Await  
**Lines:** 291

**Code Preview:**

```python
# ============================================
# ASYNC/AWAIT - ASYNCHRONOUS PROGRAMMING
# ============================================
# Comprehensive examples for async functions and await operations
# in RenzmcLang

tampilkan "=== ASYNC/AWAIT EXAMPLES ==="
tampilkan ""

# ============================================
# 1. BASIC ASYNC FUNCTION
# ============================================
tampilkan "1. Basic Async Function:"
tampilkan ""

# Define an async function
async buat fungsi ambil_data(url):
    tampilkan "   Fetching data from: " + url
    # Simulate data fetching
    hasil "Data from " + url
// ... (more code)

```

---

### 4. 03 Oop Advanced

**File:** `advanced_features/03_oop_advanced.rmc`  
**Description:** 03 Oop Advanced  
**Lines:** 446

**Code Preview:**

```python
# ============================================
# ADVANCED OOP - FUNCTION-BASED APPROACH
# ============================================
# Comprehensive examples for Object-Oriented Programming
# using function-based patterns in RenzmcLang
#
# NOTE: While RenzmcLang has class syntax, this example uses
# a function-based approach that's more reliable and follows
# functional programming principles.

tampilkan "=== ADVANCED OOP PATTERNS ==="
tampilkan ""

# ============================================
# 1. BASIC OBJECT WITH METHODS
# ============================================
tampilkan "1. Basic Object with Methods:"
tampilkan ""

# Constructor function
// ... (more code)

```

---

## Advanced Operators

**Total Examples:** 1

### 1. 01 Walrus Operator

**File:** `advanced_operators/01_walrus_operator.rmc`  
**Description:** 01 Walrus Operator  
**Lines:** 262

**Code Preview:**

```python
# ===================================
# Walrus Operator (:=)
# ===================================
# Walrus operator adalah assignment expression yang memungkinkan
# assignment dan return value dalam satu ekspresi
# Sintaks: (variable := value)

tampilkan "=== Walrus Operator Examples ==="
tampilkan ""

# ===================================
# 1. Walrus Operator Dasar
# ===================================
tampilkan "1. Walrus Operator Dasar:"

# Assignment dalam kondisi
jika (nilai := 85) >= 60
    tampilkan "Nilai: " + ke_teks(nilai)
    tampilkan "Status: Lulus"
selesai
// ... (more code)

```

---

## Algorithms

**Total Examples:** 2

### 1. 01 Binary Search

**File:** `algorithms/01_binary_search.rmc`  
**Description:** Algorithm: Binary Search (Pencarian Biner)  
**Lines:** 123

**Code Preview:**

```python
// ============================================
// Algorithm: Binary Search (Pencarian Biner)
// ============================================
// Binary Search adalah algoritma pencarian efisien
// untuk data yang sudah terurut dengan kompleksitas O(log n)

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║        BINARY SEARCH ALGORITHM        ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Implementasi Binary Search
buat fungsi binary_search dengan arr, target
    left itu 0
    right itu panjang(arr) - 1
    iterasi itu 0
    
    selama left <= right
        iterasi itu iterasi + 1
        mid itu (left + right) // 2
// ... (more code)

```

---

### 2. 02 Searching Algorithms

**File:** `algorithms/02_searching_algorithms.rmc`  
**Description:** 02 Searching Algorithms  
**Lines:** 201

**Code Preview:**

```python
# ===================================
# Searching Algorithms
# ===================================
# Algoritma pencarian untuk menemukan elemen dalam data

tampilkan "=== Searching Algorithms Examples ==="
tampilkan ""

# ===================================
# 1. Linear Search
# ===================================
tampilkan "1. Linear Search:"

fungsi linear_search(arr, target):
    untuk i dari 0 sampai panjang(arr) - 1
        jika arr[i] == target
            hasil i
        selesai
    selesai
    hasil -1
// ... (more code)

```

---

## Builtin Functions

**Total Examples:** 7

### 1. 01 String Functions

**File:** `builtin_functions/01_string_functions.rmc`  
**Description:** Built-in Functions: String Operations  
**Lines:** 216

**Code Preview:**

```python
// ============================================
// Built-in Functions: String Operations
// ============================================
// Comprehensive examples for all string functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║      STRING FUNCTIONS COMPLETE        ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Sample text
teks itu "  Hello RenzMcLang World!  "
tampilkan f"Original text: '{teks}'"
tampilkan ""

// ============================================
// 1. BASIC STRING FUNCTIONS
// ============================================
tampilkan "=== 1. BASIC STRING FUNCTIONS ==="
tampilkan ""
// ... (more code)

```

---

### 2. 02 Math Statistics

**File:** `builtin_functions/02_math_statistics.rmc`  
**Description:** Built-in Functions: Math & Statistics  
**Lines:** 196

**Code Preview:**

```python
// ============================================
// Built-in Functions: Math & Statistics
// ============================================
// Comprehensive examples for math and statistics functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║    MATH & STATISTICS FUNCTIONS        ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. BASIC MATH FUNCTIONS
// ============================================
tampilkan "=== 1. BASIC MATH FUNCTIONS ==="
tampilkan ""

angka_desimal itu 3.7
angka_negatif itu -15.8

// bulat - Round to nearest integer
// ... (more code)

```

---

### 3. 03 Iteration Functions

**File:** `builtin_functions/03_iteration_functions.rmc`  
**Description:** Built-in Functions: Iteration & Functional  
**Lines:** 149

**Code Preview:**

```python
// ============================================
// Built-in Functions: Iteration & Functional
// ============================================
// Comprehensive examples for iteration functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║     ITERATION FUNCTIONS COMPLETE      ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. ZIP - Combine multiple lists
// ============================================
tampilkan "=== 1. ZIP - Combine Lists ==="
tampilkan ""

nama_list itu ["Alice", "Bob", "Charlie"]
umur_list itu [25, 30, 35]
kota_list itu ["Jakarta", "Bandung", "Surabaya"]

// ... (more code)

```

---

### 4. 04 File Path Operations

**File:** `builtin_functions/04_file_path_operations.rmc`  
**Description:** Built-in Functions: File & Path Operations  
**Lines:** 201

**Code Preview:**

```python
// ============================================
// Built-in Functions: File & Path Operations
// ============================================
// Comprehensive examples for file and path functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║    FILE & PATH OPERATIONS COMPLETE    ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. DIRECTORY OPERATIONS
// ============================================
tampilkan "=== 1. DIRECTORY OPERATIONS ==="
tampilkan ""

// direktori_sekarang - Get current directory
dir_sekarang itu direktori_sekarang()
tampilkan f"✓ direktori_sekarang() = '{dir_sekarang}'"

// ... (more code)

```

---

### 5. 05 Json Utility

**File:** `builtin_functions/05_json_utility.rmc`  
**Description:** Built-in Functions: JSON & Utility Functions  
**Lines:** 241

**Code Preview:**

```python
// ============================================
// Built-in Functions: JSON & Utility Functions
// ============================================
// Comprehensive examples for JSON and utility functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║      JSON & UTILITY FUNCTIONS         ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. JSON OPERATIONS
// ============================================
tampilkan "=== 1. JSON OPERATIONS ==="
tampilkan ""

// Create data structure
data itu {
    "nama": "RenzMcLang",
    "versi": "0.0.1",
// ... (more code)

```

---

### 6. 06 System Functions

**File:** `builtin_functions/06_system_functions.rmc`  
**Description:** Built-in Functions: System Functions  
**Lines:** 213

**Code Preview:**

```python
// ============================================
// Built-in Functions: System Functions
// ============================================
// Comprehensive examples for system functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║        SYSTEM FUNCTIONS COMPLETE      ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. TIME & DATE FUNCTIONS
// ============================================
tampilkan "=== 1. TIME & DATE FUNCTIONS ==="
tampilkan ""

// waktu - Get current timestamp
waktu_sekarang itu waktu()
tampilkan f"✓ waktu() = {waktu_sekarang}"

// ... (more code)

```

---

### 7. 07 List Dict Operations

**File:** `builtin_functions/07_list_dict_operations.rmc`  
**Description:** Built-in Functions: List & Dictionary Operations  
**Lines:** 251

**Code Preview:**

```python
// ============================================
// Built-in Functions: List & Dictionary Operations
// ============================================
// Comprehensive examples for list and dict functions

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║   LIST & DICT OPERATIONS COMPLETE     ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// ============================================
// 1. LIST BASIC OPERATIONS
// ============================================
tampilkan "=== 1. LIST BASIC OPERATIONS ==="
tampilkan ""

daftar itu [1, 2, 3, 4, 5]
tampilkan f"Original list: {daftar}"
tampilkan ""

// ... (more code)

```

---

## Cli Tools

**Total Examples:** 2

### 1. 01 Command Line Args

**File:** `cli_tools/01_command_line_args.rmc`  
**Description:** Command Line Tools - CLI Arguments  
**Lines:** 71

**Code Preview:**

```python
// ============================================
// Command Line Tools - CLI Arguments
// ============================================
// Membuat CLI tools dengan argument parsing

tampilkan "=== Command Line Tools ==="
tampilkan ""

impor_python "sys"
impor_python "argparse"

// ============================================
// 1. BASIC COMMAND LINE ARGUMENTS
// ============================================

tampilkan "[1] Basic Command Line Arguments..."
tampilkan ""

// Akses command line arguments
args itu sys.argv
// ... (more code)

```

---

### 2. 01 Command Line Args Fixed

**File:** `cli_tools/01_command_line_args_fixed.rmc`  
**Description:** Command Line Tools - CLI Arguments  
**Lines:** 71

**Code Preview:**

```python
// ============================================
// Command Line Tools - CLI Arguments
// ============================================
// Membuat CLI tools dengan argument parsing

tampilkan "=== Command Line Tools ==="
tampilkan ""

impor_python "sys"
impor_python "argparse"

// ============================================
// 1. BASIC COMMAND LINE ARGUMENTS
// ============================================

tampilkan "[1] Basic Command Line Arguments..."
tampilkan ""

// Akses command line arguments
args itu sys.argv
// ... (more code)

```

---

## Concurrency

**Total Examples:** 1

### 1. 01 Threading

**File:** `concurrency/01_threading.rmc`  
**Description:** Threading - Concurrent Programming  
**Lines:** 267

**Code Preview:**

```python
// ============================================
// Threading - Concurrent Programming
// ============================================
// Contoh penggunaan threading untuk concurrent execution

tampilkan "=== Threading Example ==="
tampilkan ""

impor_python "threading"
impor_python "time"
impor_python "random"

// ============================================
// 1. BASIC THREADING
// ============================================

tampilkan "[1] Basic Threading..."
tampilkan ""

fungsi worker(nama, durasi):
// ... (more code)

```

---

## Control Flow

**Total Examples:** 1

### 1. 01 Ternary Operator

**File:** `control_flow/01_ternary_operator.rmc`  
**Description:** 01 Ternary Operator  
**Lines:** 276

**Code Preview:**

```python
# ===================================
# Ternary Operator (Operator Kondisi)
# ===================================
# Ternary operator adalah cara singkat untuk menulis if-else
# Sintaks: nilai_jika_benar jika kondisi kalau tidak nilai_jika_salah

tampilkan "=== Ternary Operator Examples ==="
tampilkan ""

# ===================================
# 1. Ternary Operator Dasar
# ===================================
tampilkan "1. Ternary Operator Dasar:"

# Contoh sederhana
umur itu 20
status itu "Dewasa" jika umur >= 18 kalau tidak "Anak-anak"
tampilkan "Umur: " + ke_teks(umur)
tampilkan "Status: " + status

// ... (more code)

```

---

## Dasar

**Total Examples:** 5

### 1. 01 Hello World

**File:** `dasar/01_hello_world.rmc`  
**Description:** Contoh 1: Hello World  
**Lines:** 16

**Code Preview:**

```python
// ============================================
// Contoh 1: Hello World
// ============================================
// Program pertama dalam RenzmcLang

tampilkan "Hello, World!"
tampilkan "Selamat datang di RenzmcLang!"

// Dengan variabel
pesan itu "Hello dari RenzmcLang!"
tampilkan pesan

// Dengan f-string
nama itu "Programmer"
tampilkan f"Halo, {nama}!"

```

---

### 2. 02 Kalkulator Sederhana

**File:** `dasar/02_kalkulator_sederhana.rmc`  
**Description:** Contoh 2: Kalkulator Sederhana  
**Lines:** 27

**Code Preview:**

```python
// ============================================
// Contoh 2: Kalkulator Sederhana
// ============================================

tampilkan "=== KALKULATOR SEDERHANA ==="
tampilkan ""

// Contoh dengan nilai tetap (untuk demo)
// Dalam penggunaan nyata, bisa menggunakan input dari user
angka1 itu 10
angka2 itu 5

// Operasi matematika
hasil_tambah itu angka1 + angka2
hasil_kurang itu angka1 - angka2
hasil_kali itu angka1 * angka2
hasil_bagi itu angka1 / angka2
hasil_pangkat itu angka1 ** angka2

// Tampilkan hasil
// ... (more code)

```

---

### 3. 03 Cek Bilangan

**File:** `dasar/03_cek_bilangan.rmc`  
**Description:** Contoh 3: Cek Bilangan Genap/Ganjil  
**Lines:** 25

**Code Preview:**

```python
// ============================================
// Contoh 3: Cek Bilangan Genap/Ganjil
// ============================================

tampilkan "=== CEK BILANGAN GENAP/GANJIL ==="
tampilkan ""

// Contoh dengan nilai tetap
angka itu 10

jika angka % 2 == 0
    tampilkan f"{angka} adalah bilangan GENAP"
kalau tidak
    tampilkan f"{angka} adalah bilangan GANJIL"
selesai

// Cek positif/negatif
tampilkan ""
jika angka > 0
    tampilkan f"{angka} adalah bilangan POSITIF"
// ... (more code)

```

---

### 4. 04 Tabel Perkalian

**File:** `dasar/04_tabel_perkalian.rmc`  
**Description:** Contoh 4: Tabel Perkalian  
**Lines:** 19

**Code Preview:**

```python
// ============================================
// Contoh 4: Tabel Perkalian
// ============================================

tampilkan "=== TABEL PERKALIAN ==="
tampilkan ""

// Contoh dengan nilai tetap
angka itu 7

tampilkan f"\nTabel Perkalian {angka}:"
tampilkan "=============================="

untuk i dari 1 sampai 10
    hasil_kali itu angka * i
    tampilkan f"{angka} × {i} = {hasil_kali}"
selesai

tampilkan "=============================="
```

---

### 5. 05 Daftar Belanja

**File:** `dasar/05_daftar_belanja.rmc`  
**Description:** Contoh 5: Daftar Belanja  
**Lines:** 35

**Code Preview:**

```python
// ============================================
// Contoh 5: Daftar Belanja
// ============================================

tampilkan "=== DAFTAR BELANJA ==="
tampilkan ""

// Inisialisasi daftar belanja dengan contoh data
belanja itu []

// Tambah beberapa item contoh
item1 itu {"nama": "Apel", "harga": 15000}
item2 itu {"nama": "Jeruk", "harga": 20000}
item3 itu {"nama": "Mangga", "harga": 25000}

tambah(belanja, item1)
tambah(belanja, item2)
tambah(belanja, item3)

// Tampilkan daftar belanja
// ... (more code)

```

---

## Data Structures

**Total Examples:** 5

### 1. 01 Stack

**File:** `data_structures/01_stack.rmc`  
**Description:** Data Structure: Stack (Tumpukan)  
**Lines:** 191

**Code Preview:**

```python
// ============================================
// Data Structure: Stack (Tumpukan)
// ============================================
// Stack adalah struktur data LIFO (Last In First Out)
// Elemen terakhir yang masuk adalah yang pertama keluar

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║     IMPLEMENTASI STACK (TUMPUKAN)     ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Buat class Stack
buat fungsi buat_stack
    stack itu []
    hasil stack
selesai

// Push: Tambah elemen ke stack
buat fungsi push dengan stack, item
    tambah(stack, item)
// ... (more code)

```

---

### 2. 02 Queue

**File:** `data_structures/02_queue.rmc`  
**Description:** Data Structure: Queue (Antrian)  
**Lines:** 154

**Code Preview:**

```python
// ============================================
// Data Structure: Queue (Antrian)
// ============================================
// Queue adalah struktur data FIFO (First In First Out)
// Elemen pertama yang masuk adalah yang pertama keluar

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║      IMPLEMENTASI QUEUE (ANTRIAN)     ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Buat Queue
buat fungsi buat_queue
    queue itu []
    hasil queue
selesai

// Enqueue: Tambah elemen ke belakang queue
buat fungsi enqueue dengan queue, item
    tambah(queue, item)
// ... (more code)

```

---

### 3. 03 Tuple Operations

**File:** `data_structures/03_tuple_operations.rmc`  
**Description:** 03 Tuple Operations  
**Lines:** 204

**Code Preview:**

```python
# ===================================
# Tuple Operations
# ===================================
# Tuple adalah collection yang immutable (tidak bisa diubah)
# Sintaks: (| element1, element2, ... |)

tampilkan "=== Tuple Operations Examples ==="
tampilkan ""

# ===================================
# 1. Membuat Tuple
# ===================================
tampilkan "1. Membuat Tuple:"

# Tuple dengan berbagai tipe data
tuple1 itu (| 1, 2, 3, 4, 5 |)
tampilkan "Tuple angka: " + ke_teks(tuple1)

tuple2 itu (| "apel", "jeruk", "mangga" |)
tampilkan "Tuple string: " + ke_teks(tuple2)
// ... (more code)

```

---

### 4. 04 Advanced Unpacking

**File:** `data_structures/04_advanced_unpacking.rmc`  
**Description:** 04 Advanced Unpacking  
**Lines:** 323

**Code Preview:**

```python
# ============================================
# ADVANCED DATA STRUCTURE OPERATIONS
# ============================================
# Comprehensive examples for tuple unpacking, list operations,
# and advanced data structure manipulations

tampilkan "=== ADVANCED DATA STRUCTURE OPERATIONS ==="
tampilkan ""

# ============================================
# 1. TUPLE UNPACKING
# ============================================
tampilkan "1. Tuple Unpacking:"
tampilkan ""

# Basic tuple unpacking
koordinat itu (10, 20)
x, y itu koordinat
tampilkan "   Basic unpacking:"
tampilkan "   x = " + ke_teks(x) + ", y = " + ke_teks(y)
// ... (more code)

```

---

### 5. 04 Set Operations

**File:** `data_structures/04_set_operations.rmc`  
**Description:** 04 Set Operations  
**Lines:** 200

**Code Preview:**

```python
# ===================================
# Set Operations (Basic)
# ===================================
# Set adalah collection yang tidak berurutan dan tidak memiliki duplikat
# Sintaks: {| element1, element2, ... |}
# Note: Set operations kompleks (union, intersection) memiliki keterbatasan

tampilkan "=== Set Operations Examples ==="
tampilkan ""

# ===================================
# 1. Membuat Set
# ===================================
tampilkan "1. Membuat Set:"

# Set dengan angka
set1 itu {| 1, 2, 3, 4, 5 |}
tampilkan "Set angka: " + ke_teks(set1)

# Set dengan string
// ... (more code)

```

---

## Database

**Total Examples:** 5

### 1. 01 Sqlite Basic

**File:** `database/01_sqlite_basic.rmc`  
**Description:** SQLite Database - Basic Operations  
**Lines:** 153

**Code Preview:**

```python
// ============================================
// SQLite Database - Basic Operations
// ============================================
// Contoh penggunaan SQLite untuk operasi CRUD dasar

tampilkan "=== SQLite Basic CRUD Operations ==="
tampilkan ""

// Import modul Python untuk SQLite
impor_python "sqlite3"

// 1. Membuat koneksi database
tampilkan "[1] Membuat koneksi ke database..."
conn itu sqlite3.connect("contoh.db")
cursor itu conn.cursor()
tampilkan "✓ Koneksi berhasil dibuat"
tampilkan ""

// 2. Membuat tabel
tampilkan "[2] Membuat tabel 'mahasiswa'..."
// ... (more code)

```

---

### 2. 02 Sqlite Advanced

**File:** `database/02_sqlite_advanced.rmc`  
**Description:** SQLite Database - Advanced Operations  
**Lines:** 296

**Code Preview:**

```python
// ============================================
// SQLite Database - Advanced Operations
// ============================================
// Contoh operasi database lanjutan: transactions, indexes, joins

tampilkan "=== SQLite Advanced Operations ==="
tampilkan ""

impor_python "sqlite3"
impor_python "datetime"

// Koneksi database
conn itu sqlite3.connect("perpustakaan.db")
cursor itu conn.cursor()

// 1. Membuat multiple tables dengan foreign keys
tampilkan "[1] Membuat struktur database perpustakaan..."

// Tabel buku
cursor.execute("""
// ... (more code)

```

---

### 3. 03 Database Wrapper

**File:** `database/03_database_wrapper.rmc`  
**Description:** Database Wrapper - ORM-Style Interface  
**Lines:** 238

**Code Preview:**

```python
// ============================================
// Database Wrapper - ORM-Style Interface
// ============================================
// Membuat wrapper database dengan interface yang mudah digunakan

tampilkan "=== Database Wrapper (ORM-Style) ==="
tampilkan ""

tampilkan "Contoh kode Python untuk Database Wrapper:"
tampilkan ""

kode_wrapper itu """
import sqlite3
import json

class DatabaseWrapper:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
// ... (more code)

```

---

### 4. 04 Mysql Postgresql

**File:** `database/04_mysql_postgresql.rmc`  
**Description:** MySQL/PostgreSQL Database Operations  
**Lines:** 349

**Code Preview:**

```python
// ============================================
// MySQL/PostgreSQL Database Operations
// ============================================
// Contoh koneksi dan operasi dengan MySQL/PostgreSQL

tampilkan "=== MySQL/PostgreSQL Database Operations ==="
tampilkan ""

// Note: Untuk menjalankan contoh ini, install terlebih dahulu:
// pip install mysql-connector-python  (untuk MySQL)
// pip install psycopg2-binary  (untuk PostgreSQL)

tampilkan "Contoh ini menunjukkan cara koneksi ke MySQL dan PostgreSQL"
tampilkan "Pastikan database server sudah berjalan dan kredensial sudah benar"
tampilkan ""

// ============================================
// MYSQL OPERATIONS
// ============================================

// ... (more code)

```

---

### 5. 05 Mongodb

**File:** `database/05_mongodb.rmc`  
**Description:** MongoDB Database Operations  
**Lines:** 363

**Code Preview:**

```python
// ============================================
// MongoDB Database Operations
// ============================================
// Contoh operasi dengan MongoDB (NoSQL Database)

tampilkan "=== MongoDB Database Operations ==="
tampilkan ""

// Note: Install pymongo terlebih dahulu: pip install pymongo

tampilkan "Contoh ini menunjukkan cara bekerja dengan MongoDB"
tampilkan "Pastikan MongoDB server sudah berjalan"
tampilkan ""

coba
    impor_python "pymongo"
    impor_python "pymongo.MongoClient"
    impor_python "datetime"
    
    tampilkan "[1] Koneksi ke MongoDB..."
// ... (more code)

```

---

## Datetime Operations

**Total Examples:** 1

### 1. 01 Datetime Basics

**File:** `datetime_operations/01_datetime_basics.rmc`  
**Description:** DateTime Operations - Tanggal dan Waktu  
**Lines:** 282

**Code Preview:**

```python
// ============================================
// DateTime Operations - Tanggal dan Waktu
// ============================================
// Operasi tanggal dan waktu dengan Python datetime

tampilkan "=== DateTime Operations ==="
tampilkan ""

impor_python "datetime"
impor_python "time"

// ============================================
// 1. DATETIME BASICS
// ============================================

tampilkan "[1] DateTime Basics..."
tampilkan ""

// Waktu sekarang
sekarang itu panggil_python datetime.datetime.now()
// ... (more code)

```

---

## Dict Operations

**Total Examples:** 1

### 1. 01 Dict Advanced

**File:** `dict_operations/01_dict_advanced.rmc`  
**Description:** 01 Dict Advanced  
**Lines:** 226

**Code Preview:**

```python
# ===================================
# Dictionary Operations Advanced
# ===================================
# Operasi dictionary lanjutan untuk data key-value

tampilkan "=== Dictionary Operations Advanced Examples ==="
tampilkan ""

# ===================================
# 1. Dict Creation
# ===================================
tampilkan "1. Dict Creation:"

# Empty dict
dict1 itu {}
tampilkan "Empty dict: " + ke_teks(dict1)

# Dict dengan data
dict2 itu {"nama": "Budi", "umur": 25, "kota": "Jakarta"}
tampilkan "Dict data: " + ke_teks(dict2)
// ... (more code)

```

---

## Email

**Total Examples:** 1

### 1. 01 Email Sending

**File:** `email/01_email_sending.rmc`  
**Description:** Email Sending - SMTP Email  
**Lines:** 467

**Code Preview:**

```python
// ============================================
// Email Sending - SMTP Email
// ============================================
// Contoh mengirim email dengan Python smtplib

tampilkan "=== Email Sending Examples ==="
tampilkan ""

impor_python "smtplib"
impor_python "email.mime.text"
impor_python "email.mime.multipart"
impor_python "email.mime.base"

// ============================================
// 1. BASIC EMAIL
// ============================================

tampilkan "[1] Basic Email Example..."
tampilkan ""

// ... (more code)

```

---

## Error Handling

**Total Examples:** 1

### 1. 01 Try Catch Advanced

**File:** `error_handling/01_try_catch_advanced.rmc`  
**Description:** 01 Try Catch Advanced  
**Lines:** 209

**Code Preview:**

```python
# ===================================
# Try-Catch-Finally Advanced
# ===================================
# Error handling yang robust untuk menangani kesalahan

tampilkan "=== Try-Catch-Finally Advanced Examples ==="
tampilkan ""

# ===================================
# 1. Basic Try-Catch
# ===================================
tampilkan "1. Basic Try-Catch:"

coba
    tampilkan "Mencoba operasi..."
    hasil itu 10 / 2
    tampilkan "Hasil: " + ke_teks(hasil)
tangkap e
    tampilkan "Error terjadi: " + ke_teks(e)
selesai
// ... (more code)

```

---

## File Processing

**Total Examples:** 2

### 1. 01 Csv Processing

**File:** `file_processing/01_csv_processing.rmc`  
**Description:** CSV File Processing  
**Lines:** 249

**Code Preview:**

```python
// ============================================
// CSV File Processing
// ============================================
// Membaca, menulis, dan memproses file CSV

tampilkan "=== CSV File Processing ==="
tampilkan ""

impor_python "csv"
impor_python "os"

// ============================================
// 1. MEMBUAT FILE CSV
// ============================================

tampilkan "[1] Membuat File CSV..."

// Data mahasiswa
data_mahasiswa itu [
    ["NIM", "Nama", "Jurusan", "IPK", "Semester"],
// ... (more code)

```

---

### 2. 02 Json Processing

**File:** `file_processing/02_json_processing.rmc`  
**Description:** JSON File Processing  
**Lines:** 333

**Code Preview:**

```python
// ============================================
// JSON File Processing
// ============================================
// Membaca, menulis, dan memproses file JSON

tampilkan "=== JSON File Processing ==="
tampilkan ""

// ============================================
// 1. MEMBUAT DAN MENULIS JSON
// ============================================

tampilkan "[1] Membuat dan Menulis JSON..."

// Data produk
data_produk itu {
    "toko": "Toko Elektronik ABC",
    "alamat": "Jl. Sudirman No. 123, Jakarta",
    "produk": [
        {
// ... (more code)

```

---

## Functional Programming

**Total Examples:** 2

### 1. 01 Lambda Functions

**File:** `functional_programming/01_lambda_functions.rmc`  
**Description:** 01 Lambda Functions  
**Lines:** 318

**Code Preview:**

```python
# ===================================
# Lambda Functions (Fungsi Lambda)
# ===================================
# Lambda adalah fungsi anonim (tanpa nama) yang dapat dibuat dengan cepat
# Sintaks: lambda dengan parameter -> ekspresi
# Catatan: Saat ini lambda hanya mendukung 1 parameter

tampilkan "=== Lambda Functions Examples ==="
tampilkan ""

# ===================================
# 1. Lambda Dasar
# ===================================
tampilkan "1. Lambda Dasar:"

# Lambda sederhana untuk menambah 10
tambah_10 itu lambda dengan x -> x + 10
tampilkan "tambah_10(5) = " + ke_teks(tambah_10(5))
tampilkan "tambah_10(15) = " + ke_teks(tambah_10(15))
tampilkan "tambah_10(100) = " + ke_teks(tambah_10(100))
// ... (more code)

```

---

### 2. 02 Comprehensions

**File:** `functional_programming/02_comprehensions.rmc`  
**Description:** 02 Comprehensions  
**Lines:** 305

**Code Preview:**

```python
# ===================================
# Comprehensions (List & Dict)
# ===================================
# Comprehension adalah cara singkat untuk membuat collection baru
# dari collection yang sudah ada dengan transformasi atau filter

tampilkan "=== Comprehensions Examples ==="
tampilkan ""

# ===================================
# 1. List Comprehension Dasar
# ===================================
tampilkan "1. List Comprehension Dasar:"

# Buat list kuadrat dari 1-10
angka itu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tampilkan "Angka asli: " + ke_teks(angka)

# List comprehension: [ekspresi untuk setiap item dari iterable]
kuadrat itu [x * x untuk setiap x dari angka]
// ... (more code)

```

---

## Functions

**Total Examples:** 1

### 1. 01 Function Basics

**File:** `functions/01_function_basics.rmc`  
**Description:** 01 Function Basics  
**Lines:** 225

**Code Preview:**

```python
# ===================================
# Function Basics
# ===================================
# Fungsi adalah blok kode yang dapat digunakan kembali

tampilkan "=== Function Basics Examples ==="
tampilkan ""

# ===================================
# 1. Fungsi Sederhana
# ===================================
tampilkan "1. Fungsi Sederhana:"

fungsi sapa():
    tampilkan "Hello, World!"
selesai

sapa()

tampilkan ""
// ... (more code)

```

---

## Games

**Total Examples:** 1

### 1. 01 Tebak Angka

**File:** `games/01_tebak_angka.rmc`  
**Description:** Game: Tebak Angka  
**Lines:** 70

**Code Preview:**

```python
// ============================================
// Game: Tebak Angka
// ============================================
// Game sederhana menebak angka acak

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║          GAME TEBAK ANGKA             ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

tampilkan "🎮 Selamat datang di Game Tebak Angka!"
tampilkan "📝 Aturan:"
tampilkan "   - Komputer memilih angka antara 1-100"
tampilkan "   - Anda punya 7 kesempatan untuk menebak"
tampilkan "   - Komputer akan memberi petunjuk"
tampilkan ""

// Import random dari Python
impor_python "random"

// ... (more code)

```

---

## Gui

**Total Examples:** 1

### 1. 01 Tkinter Basics

**File:** `gui/01_tkinter_basics.rmc`  
**Description:** GUI with Tkinter - Basic Examples  
**Lines:** 254

**Code Preview:**

```python
// ============================================
// GUI with Tkinter - Basic Examples
// ============================================
// Membuat GUI aplikasi dengan Tkinter

tampilkan "=== Tkinter GUI Examples ==="
tampilkan ""

// Note: Install tkinter jika belum ada (biasanya sudah include di Python)

coba
    impor_python "tkinter"
    impor_python "tkinter.messagebox"
    impor_python "tkinter.ttk"
    
    tampilkan "[1] Simple Window Example..."
    tampilkan ""
    
    // Contoh 1: Window Sederhana
    tampilkan "Contoh kode untuk window sederhana:"
// ... (more code)

```

---

## Http Client

**Total Examples:** 3

### 1. 01 Http Get Basic

**File:** `http_client/01_http_get_basic.rmc`  
**Description:** HTTP Client - Basic GET Request  
**Lines:** 72

**Code Preview:**

```python
// ============================================================================
// HTTP Client - Basic GET Request
// Demonstrasi penggunaan built-in HTTP client tanpa perlu import
// ============================================================================

tampilkan "=== HTTP Client - Basic GET Request ==="
tampilkan ""

// 1. Simple GET request
tampilkan "[1] Simple GET Request"
coba
    response itu http_get("https://jsonplaceholder.typicode.com/posts/1")
    tampilkan f"Status: {response.status_code}"
    tampilkan f"URL: {response.url}"
    
    data itu response.json()
    tampilkan f"Title: {data['title']}"
    body_text itu data['body']
    body_preview itu potong(body_text, 0, 50)
    tampilkan f"Body: {body_preview}..."
// ... (more code)

```

---

### 2. 02 Http Post Put Delete

**File:** `http_client/02_http_post_put_delete.rmc`  
**Description:** HTTP Client - POST, PUT, DELETE Requests  
**Lines:** 100

**Code Preview:**

```python
// ============================================================================
// HTTP Client - POST, PUT, DELETE Requests
// Demonstrasi HTTP methods untuk CRUD operations
// ============================================================================

tampilkan "=== HTTP Client - POST, PUT, DELETE ==="
tampilkan ""

// 1. POST - Create new resource
tampilkan "[1] POST - Create New Post"
coba
    data_baru itu {
        "title": "Post dari RenzMcLang",
        "body": "Ini adalah post yang dibuat menggunakan RenzMcLang!",
        "userId": 1
    }
    
    response itu http_post("https://jsonplaceholder.typicode.com/posts", json=data_baru)
    
    tampilkan f"Status: {response.status_code}"
// ... (more code)

```

---

### 3. 03 Http Advanced

**File:** `http_client/03_http_advanced.rmc`  
**Description:** HTTP Client - Advanced Features  
**Lines:** 119

**Code Preview:**

```python
// ============================================================================
// HTTP Client - Advanced Features
// Custom headers, timeout, error handling
// ============================================================================

tampilkan "=== HTTP Client - Advanced Features ==="
tampilkan ""

// 1. Custom headers
tampilkan "[1] Custom Headers"
coba
    headers itu {
        "User-Agent": "RenzMcLang-Bot/1.0",
        "Accept": "application/json"
    }
    
    response itu http_get("https://httpbin.org/headers", headers=headers)
    data itu response.json()
    
    tampilkan "Request headers:"
// ... (more code)

```

---

## Image Processing

**Total Examples:** 1

### 1. 01 Pillow Basics

**File:** `image_processing/01_pillow_basics.rmc`  
**Description:** Image Processing - Pillow/PIL  
**Lines:** 400

**Code Preview:**

```python
// ============================================
// Image Processing - Pillow/PIL
// ============================================
// Contoh pengolahan gambar dengan Pillow

tampilkan "=== Image Processing with Pillow ==="
tampilkan ""

// Note: Install Pillow: pip install Pillow

coba
    impor_python "PIL.Image"
    impor_python "PIL.ImageDraw"
    impor_python "PIL.ImageFont"
    impor_python "PIL.ImageFilter"
    impor_python "PIL.ImageEnhance"
    
    tampilkan "[1] Basic Image Operations..."
    tampilkan ""
    
// ... (more code)

```

---

## Intermediate

**Total Examples:** 2

### 1. 01 Sorting Algorithms

**File:** `intermediate/01_sorting_algorithms.rmc`  
**Description:** Contoh: Sorting dan Operasi List  
**Lines:** 59

**Code Preview:**

```python
// ============================================
// Contoh: Sorting dan Operasi List
// ============================================

tampilkan "=== DEMO SORTING & LIST OPERATIONS ==="
tampilkan ""

// Data yang akan diurutkan
data1 itu [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
tampilkan f"Data awal: {data1}"
tampilkan ""

// ========== ASCENDING SORT ==========
tampilkan "1. Sorting Ascending (Kecil ke Besar):"
urutkan(data1, salah)
tampilkan f"   Hasil: {data1}"
tampilkan ""

// ========== DESCENDING SORT ==========
tampilkan "2. Sorting Descending (Besar ke Kecil):"
// ... (more code)

```

---

### 2. 02 Sistem Login

**File:** `intermediate/02_sistem_login.rmc`  
**Description:** Contoh: Sistem Login Sederhana (Demo)  
**Lines:** 110

**Code Preview:**

```python
// ============================================
// Contoh: Sistem Login Sederhana (Demo)
// ============================================

tampilkan "=== SISTEM LOGIN ==="
tampilkan ""

// Database user (dictionary)
users itu {
    "admin": {
        "password": "admin123",
        "nama": "Administrator",
        "role": "admin"
    },
    "user1": {
        "password": "pass123",
        "nama": "User Satu",
        "role": "user"
    }
}
// ... (more code)

```

---

## List Operations

**Total Examples:** 1

### 1. 01 List Advanced

**File:** `list_operations/01_list_advanced.rmc`  
**Description:** 01 List Advanced  
**Lines:** 210

**Code Preview:**

```python
# ===================================
# List Operations Advanced
# ===================================
# Operasi list lanjutan untuk manipulasi data

tampilkan "=== List Operations Advanced Examples ==="
tampilkan ""

# ===================================
# 1. List Creation
# ===================================
tampilkan "1. List Creation:"

# Empty list
list1 itu []
tampilkan "Empty list: " + ke_teks(list1)

# List dengan berbagai tipe
list2 itu [1, "dua", 3.0, benar, [5, 6]]
tampilkan "Mixed list: " + ke_teks(list2)
// ... (more code)

```

---

## Logging

**Total Examples:** 1

### 1. 01 Logging Basics

**File:** `logging/01_logging_basics.rmc`  
**Description:** Logging - Application Logging  
**Lines:** 308

**Code Preview:**

```python
// ============================================
// Logging - Application Logging
// ============================================
// Contoh penggunaan logging untuk debugging dan monitoring

tampilkan "=== Logging Basics ==="
tampilkan ""

impor_python "logging"
impor_python "datetime"

// ============================================
// 1. BASIC LOGGING SETUP
// ============================================

tampilkan "[1] Basic Logging Setup..."
tampilkan ""

// Konfigurasi logging dasar
panggil_python logging.basicConfig( level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" )
// ... (more code)

```

---

## Multiprocessing

**Total Examples:** 1

### 1. 01 Multiprocessing Basics

**File:** `multiprocessing/01_multiprocessing_basics.rmc`  
**Description:** Multiprocessing - Parallel Processing  
**Lines:** 370

**Code Preview:**

```python
// ============================================
// Multiprocessing - Parallel Processing
// ============================================
// Contoh penggunaan multiprocessing untuk CPU-bound tasks

tampilkan "=== Multiprocessing Examples ==="
tampilkan ""

impor_python "multiprocessing"
impor_python "time"
impor_python "os"

// ============================================
// 1. BASIC MULTIPROCESSING
// ============================================

tampilkan "[1] Basic Multiprocessing..."
tampilkan ""

fungsi worker(nama, durasi):
// ... (more code)

```

---

## Networking

**Total Examples:** 1

### 1. 01 Socket Client Server

**File:** `networking/01_socket_client_server.rmc`  
**Description:** Socket Programming - Client & Server  
**Lines:** 182

**Code Preview:**

```python
// ============================================
// Socket Programming - Client & Server
// ============================================
// Contoh komunikasi client-server dengan socket

tampilkan "=== Socket Programming Example ==="
tampilkan ""

impor_python "socket"
impor_python "threading"
impor_python "time"

// ============================================
// SERVER
// ============================================

tampilkan "[A] Socket Server"
tampilkan ""

fungsi jalankan_server(host, port):
// ... (more code)

```

---

## Operators

**Total Examples:** 2

### 1. 01 Compound Assignment

**File:** `operators/01_compound_assignment.rmc`  
**Description:** 01 Compound Assignment  
**Lines:** 283

**Code Preview:**

```python
# ===================================
# Compound Assignment Operators
# ===================================
# Compound assignment operators menggabungkan operasi dan assignment
# Lebih ringkas dari x = x + y

tampilkan "=== Compound Assignment Operators Examples ==="
tampilkan ""

# ===================================
# 1. Arithmetic Compound Assignment
# ===================================
tampilkan "1. Arithmetic Compound Assignment:"

# += (tambah sama dengan)
x itu 10
tampilkan "x awal: " + ke_teks(x)
x += 5
tampilkan "x += 5: " + ke_teks(x)

// ... (more code)

```

---

### 2. 02 Bitwise Operators

**File:** `operators/02_bitwise_operators.rmc`  
**Description:** 02 Bitwise Operators  
**Lines:** 239

**Code Preview:**

```python
# ===================================
# Bitwise Operators (Extended)
# ===================================
# Operasi bit-level untuk manipulasi data binary

tampilkan "=== Bitwise Operators Examples ==="
tampilkan ""

# ===================================
# 1. Bitwise AND (&)
# ===================================
tampilkan "1. Bitwise AND (&):"

a itu 12  # 1100
b itu 10  # 1010
hasil itu a & b  # 1000 = 8

tampilkan "a = " + ke_teks(a) + " (binary: 1100)"
tampilkan "b = " + ke_teks(b) + " (binary: 1010)"
tampilkan "a & b = " + ke_teks(hasil) + " (binary: 1000)"
// ... (more code)

```

---

## Practical

**Total Examples:** 1

### 1. 01 Calculator Advanced

**File:** `practical/01_calculator_advanced.rmc`  
**Description:** 01 Calculator Advanced  
**Lines:** 249

**Code Preview:**

```python
# ===================================
# Calculator Advanced
# ===================================
# Kalkulator dengan berbagai operasi matematika

tampilkan "=== Calculator Advanced Examples ==="
tampilkan ""

# ===================================
# 1. Basic Operations
# ===================================
tampilkan "1. Basic Operations:"

fungsi tambah_angka(a, b):
    hasil a + b
selesai

fungsi kurang_angka(a, b):
    hasil a - b
selesai
// ... (more code)

```

---

## Projects

**Total Examples:** 1

### 1. 01 Todo App

**File:** `projects/01_todo_app.rmc`  
**Description:** PROJECT: Aplikasi TODO List (Demo Version)  
**Lines:** 132

**Code Preview:**

```python
// ============================================
// PROJECT: Aplikasi TODO List (Demo Version)
// ============================================

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║       APLIKASI TODO LIST v1.0          ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Inisialisasi data - todos sebagai list of strings
todos itu []
todos_selesai itu []

// Fungsi untuk menambah todo
buat fungsi tambah_todo dengan judul
    tambah(todos, judul)
    hasil {"sukses": benar, "pesan": "Todo berhasil ditambahkan!"}
selesai

// Fungsi untuk melihat semua todo
// ... (more code)

```

---

## Python Integration

**Total Examples:** 3

### 1. 01 Web Scraping

**File:** `python_integration/01_web_scraping.rmc`  
**Description:** Example: Web Scraping dengan Requests dan BeautifulSoup  
**Lines:** 39

**Code Preview:**

```python
// Example: Web Scraping dengan Requests dan BeautifulSoup
// Menunjukkan cara scraping website menggunakan Python libraries

tampilkan "╔══════════════════════════════════════════════════════════╗"
tampilkan "║  Web Scraping Example - RenzmcLang + Python             ║"
tampilkan "╚══════════════════════════════════════════════════════════╝"
tampilkan ""

// Import required libraries
impor_python "requests"

tampilkan "Making HTTP request to example.com..."
tampilkan ""

// Make HTTP GET request
response itu panggil_python requests.get("https://example.com")

// Get status code (property access, not function call)
status itu response.status_code
tampilkan "✓ Status Code: " + ke_teks(status)
// ... (more code)

```

---

### 2. 02 Data Analysis

**File:** `python_integration/02_data_analysis.rmc`  
**Description:** Example: Data Analysis dengan Python  
**Lines:** 54

**Code Preview:**

```python
// Example: Data Analysis dengan Python
// Menunjukkan cara analisis data menggunakan Python libraries

tampilkan "╔══════════════════════════════════════════════════════════╗"
tampilkan "║  Data Analysis Example - RenzmcLang + Python            ║"
tampilkan "╚══════════════════════════════════════════════════════════╝"
tampilkan ""

// Import required libraries
impor_python "statistics"
impor_python "math"

// Sample data
data itu [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tampilkan "Data: " + ke_teks(data)
tampilkan ""

// Calculate statistics
mean itu panggil_python statistics.mean(data)
tampilkan "✓ Mean (Rata-rata): " + ke_teks(mean)
// ... (more code)

```

---

### 3. 03 File Processing

**File:** `python_integration/03_file_processing.rmc`  
**Description:** Example: File Processing dengan Python  
**Lines:** 72

**Code Preview:**

```python
// Example: File Processing dengan Python
// Menunjukkan cara memproses file menggunakan Python libraries

tampilkan "╔══════════════════════════════════════════════════════════╗"
tampilkan "║  File Processing Example - RenzmcLang + Python          ║"
tampilkan "╚══════════════════════════════════════════════════════════╝"
tampilkan ""

// Import required libraries
impor_python "os"
impor_python "pathlib"
impor_python "json"

// Get current directory
cwd itu panggil_python os.getcwd()
tampilkan "Current Directory: " + cwd
tampilkan ""

// List files in current directory
tampilkan "Files in current directory:"
// ... (more code)

```

---

## Regex

**Total Examples:** 1

### 1. 01 Regex Basics

**File:** `regex/01_regex_basics.rmc`  
**Description:** Regular Expressions - Pattern Matching  
**Lines:** 287

**Code Preview:**

```python
// ============================================
// Regular Expressions - Pattern Matching
// ============================================
// Contoh penggunaan regex untuk pattern matching

tampilkan "=== Regular Expressions (Regex) ==="
tampilkan ""

impor_python "re"

// ============================================
// 1. BASIC PATTERN MATCHING
// ============================================

tampilkan "[1] Basic Pattern Matching..."
tampilkan ""

// Simple search
teks itu "Email saya adalah budi@example.com"
pattern itu "budi"
// ... (more code)

```

---

## Root

**Total Examples:** 2

### 1. Test Class Complete

**File:** `test_class_complete.rmc`  
**Description:** Test Class-Based OOP - Complete  
**Lines:** 63

**Code Preview:**

```python
// Test Class-Based OOP - Complete
tampilkan "=== Testing Complete Class-Based OOP ==="
tampilkan ""

// Class dengan konstruktor dan multiple methods
kelas Mahasiswa:
    konstruktor(nama, nim):
        diri.nama itu nama
        diri.nim itu nim
        diri.nilai itu []
    selesai
    
    metode tambah_nilai(nilai):
        diri.nilai.append(nilai)
        tampilkan f"✓ Nilai {nilai} ditambahkan untuk {diri.nama}"
    selesai
    
    metode rata_rata():
        total itu 0
        untuk setiap n dari diri.nilai
// ... (more code)

```

---

### 2. Test Database Examples

**File:** `test_database_examples.rmc`  
**Description:** Test Database Examples  
**Lines:** 25

**Code Preview:**

```python
// ============================================
// Test Database Examples
// ============================================
// Script untuk menguji semua contoh database

tampilkan "=== Testing Database Examples ==="
tampilkan ""

tampilkan "[1] Testing SQLite Basic Operations..."
tampilkan "Running: examples/database/01_sqlite_basic.rmc"
tampilkan "-" * 80
tampilkan ""

// Test akan dijalankan secara manual
// Uncomment baris berikut untuk menjalankan test:
// eksekusi "python -m renzmc examples/database/01_sqlite_basic.rmc"

tampilkan "✓ Test script siap"
tampilkan ""
tampilkan "Untuk menjalankan test, gunakan:"
// ... (more code)

```

---

## String Operations

**Total Examples:** 1

### 1. 01 String Advanced

**File:** `string_operations/01_string_advanced.rmc`  
**Description:** 01 String Advanced  
**Lines:** 227

**Code Preview:**

```python
# ===================================
# String Operations Advanced
# ===================================
# Operasi string lanjutan untuk manipulasi teks

tampilkan "=== String Operations Advanced Examples ==="
tampilkan ""

# ===================================
# 1. String Methods Dasar
# ===================================
tampilkan "1. String Methods Dasar:"

teks itu "Hello World"
tampilkan "Teks: '" + teks + "'"

tampilkan "Upper: " + teks.upper()
tampilkan "Lower: " + teks.lower()
tampilkan "Capitalize: " + teks.capitalize()
tampilkan "Title: " + teks.title()
// ... (more code)

```

---

## Test All

**Total Examples:** 29

### 1. 01 Basic Features

**File:** `test_all/01_basic_features.rmc`  
**Description:** Test 1: Basic Features  
**Lines:** 39

**Code Preview:**

```python
// Test 1: Basic Features
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 1: Basic Features                                   ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

// Variables
tampilkan "\n[1.1] Variables"
nama itu "RenzmcLang"
versi itu 1.0
aktif itu benar
tampilkan f"✓ String: {nama}"
tampilkan f"✓ Number: {versi}"
tampilkan f"✓ Boolean: {aktif}"

// Data types
tampilkan "\n[1.2] Data Types"
angka_bulat itu 42
angka_desimal itu 3.14
teks itu "Hello"
daftar itu [1, 2, 3, 4, 5]
// ... (more code)

```

---

### 2. 02 Control Flow

**File:** `test_all/02_control_flow.rmc`  
**Description:** Test 2: Control Flow  
**Lines:** 46

**Code Preview:**

```python
// Test 2: Control Flow
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 2: Control Flow                                     ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

// If-else
tampilkan "\n[2.1] If-Else Statements"
x itu 10
jika x > 5
    tampilkan "✓ If statement works"
selesai

jika x < 5
    tampilkan "✗ Should not print"
kalau tidak
    tampilkan "✓ Else statement works"
selesai

// Nested if
tampilkan "\n[2.2] Nested If"
// ... (more code)

```

---

### 3. 03 Functions

**File:** `test_all/03_functions.rmc`  
**Description:** Test 3: Functions  
**Lines:** 37

**Code Preview:**

```python
// Test 3: Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 3: Functions                                        ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

// Basic function
tampilkan "\n[3.1] Basic Function"
buat fungsi salam
    tampilkan "✓ Function called successfully"
selesai
panggil salam

// Function with parameters
tampilkan "\n[3.2] Function with Parameters"
buat fungsi tambah_angka dengan a, b
    hasil a + b
selesai
hasil_tambah itu panggil tambah_angka dengan 5, 3
tampilkan f"✓ 5 + 3 = {hasil_tambah}"

// ... (more code)

```

---

### 4. 04 Builtin String

**File:** `test_all/04_builtin_string.rmc`  
**Description:** Test 4: Built-in String Functions  
**Lines:** 54

**Code Preview:**

```python
// Test 4: Built-in String Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 4: Built-in String Functions                        ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[4.1] String Functions"
teks itu "hello world"

// huruf_besar
hasil1 itu huruf_besar(teks)
tampilkan f"✓ huruf_besar: {hasil1}"

// huruf_kecil
hasil2 itu huruf_kecil("HELLO")
tampilkan f"✓ huruf_kecil: {hasil2}"

// panjang
panjang_teks itu panjang(teks)
tampilkan f"✓ panjang: {panjang_teks}"

// ... (more code)

```

---

### 5. 05 Builtin Math

**File:** `test_all/05_builtin_math.rmc`  
**Description:** Test 5: Built-in Math Functions  
**Lines:** 52

**Code Preview:**

```python
// Test 5: Built-in Math Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 5: Built-in Math Functions                          ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[5.1] Math Functions"

// bulat
hasil1 itu bulat(3.7)
tampilkan f"✓ bulat(3.7): {hasil1}"

// desimal
hasil2 itu desimal(5)
tampilkan f"✓ desimal(5): {hasil2}"

// akar
hasil3 itu akar(16)
tampilkan f"✓ akar(16): {hasil3}"

// pangkat
// ... (more code)

```

---

### 6. 06 Builtin List

**File:** `test_all/06_builtin_list.rmc`  
**Description:** Test 6: Built-in List Functions  
**Lines:** 52

**Code Preview:**

```python
// Test 6: Built-in List Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 6: Built-in List Functions                          ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[6.1] List Functions"

// Create list
daftar itu [1, 2, 3, 4, 5]
tampilkan f"✓ Initial list: {daftar}"

// tambah
tambah(daftar, 6)
tampilkan f"✓ tambah(6): {daftar}"

// hapus
hapus(daftar, 6)
tampilkan f"✓ hapus(6): {daftar}"

// masukkan
// ... (more code)

```

---

### 7. 07 Builtin Dict

**File:** `test_all/07_builtin_dict.rmc`  
**Description:** Test 7: Built-in Dictionary Functions  
**Lines:** 40

**Code Preview:**

```python
// Test 7: Built-in Dictionary Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 7: Built-in Dictionary Functions                    ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[7.1] Dictionary Functions"

// Create dictionary
data itu {"nama": "Ali", "umur": 25, "kota": "Jakarta"}
tampilkan f"✓ Initial dict: {data}"

// kunci
keys itu kunci(data)
tampilkan f"✓ kunci: {keys}"

// nilai
values itu nilai(data)
tampilkan f"✓ nilai: {values}"

// item
// ... (more code)

```

---

### 8. 08 Builtin System

**File:** `test_all/08_builtin_system.rmc`  
**Description:** Test 8: Built-in System Functions  
**Lines:** 38

**Code Preview:**

```python
// Test 8: Built-in System Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 8: Built-in System Functions                        ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[8.1] System Functions"

// jenis
tipe1 itu jenis(42)
tampilkan f"✓ jenis(42): {tipe1}"

tipe2 itu jenis("hello")
tampilkan f"✓ jenis('hello'): {tipe2}"

tipe3 itu jenis([1, 2, 3])
tampilkan f"✓ jenis([1,2,3]): {tipe3}"

// ke_teks
teks1 itu ke_teks(123)
tampilkan f"✓ ke_teks(123): {teks1}"
// ... (more code)

```

---

### 9. 09 Builtin File

**File:** `test_all/09_builtin_file.rmc`  
**Description:** Test 9: Built-in File Functions  
**Lines:** 33

**Code Preview:**

```python
// Test 9: Built-in File Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 9: Built-in File Functions                          ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[9.1] File Operations"

// tulis_file
tulis_file("test_file.txt", "Hello from RenzmcLang!")
tampilkan "✓ tulis_file: File created"

// baca_file
isi itu baca_file("test_file.txt")
tampilkan f"✓ baca_file: {isi}"

// tambah_file
tambah_file("test_file.txt", "\nLine 2")
isi2 itu baca_file("test_file.txt")
tampilkan f"✓ tambah_file: {isi2}"

// ... (more code)

```

---

### 10. 10 Builtin Json

**File:** `test_all/10_builtin_json.rmc`  
**Description:** Test 10: Built-in JSON Functions  
**Lines:** 24

**Code Preview:**

```python
// Test 10: Built-in JSON Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 10: Built-in JSON Functions                         ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[10.1] JSON Functions"

// Create data
data itu {"nama": "RenzmcLang", "versi": "1.0", "fitur": ["Python", "Data Processing"]}
tampilkan f"✓ Original data: {data}"

// json_ke_teks
json_str itu json_ke_teks(data)
tampilkan f"✓ json_ke_teks: {json_str}"

// teks_ke_json
parsed itu teks_ke_json(json_str)
tampilkan f"✓ teks_ke_json: {parsed}"

// Verify
// ... (more code)

```

---

### 11. 11 Builtin Utility

**File:** `test_all/11_builtin_utility.rmc`  
**Description:** Test 11: Built-in Utility Functions  
**Lines:** 35

**Code Preview:**

```python
// Test 11: Built-in Utility Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 11: Built-in Utility Functions                      ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[11.1] Utility Functions"

// hash_teks
hash1 itu hash_teks("password123")
tampilkan f"✓ hash_teks: {hash1}"

// buat_uuid
uuid1 itu buat_uuid()
tampilkan f"✓ buat_uuid: {uuid1}"

// url_encode
encoded itu url_encode("hello world")
tampilkan f"✓ url_encode: {encoded}"

// url_decode
// ... (more code)

```

---

### 12. 12 Python Integration

**File:** `test_all/12_python_integration.rmc`  
**Description:** Test 12: Python Integration  
**Lines:** 59

**Code Preview:**

```python
// Test 12: Python Integration
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 12: Python Integration                              ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[12.1] Basic Python Import"

// Import math
impor_python "math" sebagai math
tampilkan "✓ impor_python: math imported"

// Use math functions
hasil1 itu math.sqrt(16)
tampilkan f"✓ math.sqrt(16): {hasil1}"

hasil2 itu math.pow(2, 3)
tampilkan f"✓ math.pow(2, 3): {hasil2}"

pi_val itu math.pi
tampilkan f"✓ math.pi: {pi_val}"
// ... (more code)

```

---

### 13. 13 Http Functions

**File:** `test_all/13_http_functions.rmc`  
**Description:** Test 13: HTTP Functions  
**Lines:** 13

**Code Preview:**

```python
// Test 13: HTTP Functions
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 13: HTTP Functions                                  ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[13.1] HTTP Functions Available"
tampilkan "✓ http_get: Function exists"
tampilkan "✓ http_post: Function exists"
tampilkan "✓ http_put: Function exists"
tampilkan "✓ http_delete: Function exists"
tampilkan "ℹ Note: HTTP functions require network connection to test"

tampilkan "\n✅ Test 13 PASSED: HTTP functions working (network required)!"
```

---

### 14. 14 Error Handling

**File:** `test_all/14_error_handling.rmc`  
**Description:** Test 14: Error Handling  
**Lines:** 20

**Code Preview:**

```python
// Test 14: Error Handling
tampilkan "╔════════════════════════════════════════════════════════════╗"
tampilkan "║  Test 14: Error Handling                                  ║"
tampilkan "╚════════════════════════════════════════════════════════════╝"

tampilkan "\n[14.1] Try-Catch Basic"
coba
    tampilkan "✓ Try block executed"
    x itu 10 / 2
    tampilkan f"✓ Division result: {x}"
tangkap e
    tampilkan f"✗ Should not catch: {e}"
selesai

tampilkan "\n[14.2] Error Handling Available"
tampilkan "✓ Try-catch blocks work"
tampilkan "✓ Error catching functional"
tampilkan "✓ Finally blocks supported"

tampilkan "\n✅ Test 14 PASSED: Error handling working!"
```

---

### 15. Test All Features

**File:** `test_all/test_all_features.rmc`  
**Description:** Test All Features  
**Lines:** 155

**Code Preview:**

```python
# Comprehensive Test of All Implemented Features
# Tests Phases 1, 2, 3, 4, and 6

tampilkan "=========================================="
tampilkan "  RenzmcLang Complete Feature Test Suite"
tampilkan "=========================================="

# ============================================
# PHASE 1: OPERATORS
# ============================================
tampilkan ""
tampilkan "=== PHASE 1: OPERATORS ==="

# Bitwise operators
tampilkan ""
tampilkan "Bitwise Operators:"
tampilkan "5 & 3 = " + ke_teks(5 & 3)
tampilkan "5 | 3 = " + ke_teks(5 | 3)
tampilkan "5 ^ 3 = " + ke_teks(5 ^ 3)
tampilkan "~5 = " + ke_teks(~5)
// ... (more code)

```

---

### 16. Test All Operators

**File:** `test_all/test_all_operators.rmc`  
**Description:** Test All Operators  
**Lines:** 46

**Code Preview:**

```python
# Test bitwise operators
tampilkan "=== Bitwise Operators ==="
a itu 5
b itu 3
tampilkan "5 & 3 ="
tampilkan a & b
tampilkan "5 | 3 ="
tampilkan a | b
tampilkan "5 ^ 3 ="
tampilkan a ^ b
tampilkan "~5 ="
tampilkan ~a
tampilkan "5 << 1 ="
tampilkan a << 1
tampilkan "5 >> 1 ="
tampilkan a >> 1

# Test membership operators
tampilkan ""
tampilkan "=== Membership Operators ==="
// ... (more code)

```

---

### 17. Test Bitwise

**File:** `test_all/test_bitwise.rmc`  
**Description:** Test Bitwise  
**Lines:** 27

**Code Preview:**

```python
# Test bitwise operators
x itu 5
y itu 3
z itu x & y
tampilkan z

a itu 5
b itu 3
c itu a | b
tampilkan c

d itu 5
e itu 3
f itu d ^ e
tampilkan f

g itu 5
h itu ~g
tampilkan h

// ... (more code)

```

---

### 18. Test Bitwise Simple

**File:** `test_all/test_bitwise_simple.rmc`  
**Description:** Test Bitwise Simple  
**Lines:** 28

**Code Preview:**

```python
# Test bitwise operators (without NOT)
x itu 5
y itu 3

# Bitwise AND
z itu x & y
tampilkan "5 & 3 ="
tampilkan z

# Bitwise OR
a itu x | y
tampilkan "5 | 3 ="
tampilkan a

# Bitwise XOR
b itu x ^ y
tampilkan "5 ^ 3 ="
tampilkan b

# Left shift
// ... (more code)

```

---

### 19. Test Bukan

**File:** `test_all/test_bukan.rmc`  
**Description:** Test Bukan  
**Lines:** 6

**Code Preview:**

```python
# Test bukan operator
x itu [1, 2, 3]
z itu [1, 2, 3]
jika x bukan z maka
    tampilkan "Benar"
selesai
```

---

### 20. Test Complete All Phases

**File:** `test_all/test_complete_all_phases.rmc`  
**Description:** Test Complete All Phases  
**Lines:** 128

**Code Preview:**

```python
# COMPREHENSIVE TEST - ALL 6 PHASES
# Tests ALL implemented features from the roadmap

tampilkan "=========================================="
tampilkan "  RenzmcLang COMPLETE ROADMAP TEST"
tampilkan "  Testing ALL 6 Phases"
tampilkan "=========================================="

# ============================================
# PHASE 1: OPERATORS (11 features)
# ============================================
tampilkan ""
tampilkan "=== PHASE 1: OPERATORS (11 features) ==="

tampilkan "Bitwise: 5 & 3 = " + ke_teks(5 & 3)
tampilkan "Bitwise: 5 | 3 = " + ke_teks(5 | 3)
tampilkan "Bitwise: 5 ^ 3 = " + ke_teks(5 ^ 3)
tampilkan "Bitwise: ~5 = " + ke_teks(~5)
tampilkan "Bitwise: 5 << 1 = " + ke_teks(5 << 1)
tampilkan "Bitwise: 5 >> 1 = " + ke_teks(5 >> 1)
// ... (more code)

```

---

### 21. Test If Simple

**File:** `test_all/test_if_simple.rmc`  
**Description:** Test If Simple  
**Lines:** 5

**Code Preview:**

```python
# Simple if test
x itu 5
jika x adalah 5 maka
    tampilkan "Benar"
selesai
```

---

### 22. Test Iter Working

**File:** `test_all/test_iter_working.rmc`  
**Description:** Test Iter Working  
**Lines:** 50

**Code Preview:**

```python
# Test Iteration Functions
tampilkan "=== Test Iteration Functions ==="

# Test zip
tampilkan ""
tampilkan "Test zip():"
nama itu ["Alice", "Bob", "Charlie"]
umur itu [25, 30, 35]
hasil_zip itu zip(nama, umur)
tampilkan hasil_zip

# Test enumerate
tampilkan ""
tampilkan "Test enumerate():"
buah itu ["apel", "jeruk", "mangga"]
hasil_enum itu enumerate(buah)
tampilkan hasil_enum

# Test all
tampilkan ""
// ... (more code)

```

---

### 23. Test Iteration Functions

**File:** `test_all/test_iteration_functions.rmc`  
**Description:** Test Iteration Functions  
**Lines:** 30

**Code Preview:**

```python
# Test iteration enhancements
tampilkan "=== Testing zip() ==="
daftar1 itu [1, 2, 3]
daftar2 itu ["a", "b", "c"]
ziphasil itu zip(daftar1, daftar2)
tampilkan ziphasil

tampilkan ""
tampilkan "=== Testing enumerate() ==="
daftar itu ["apel", "jeruk", "mangga"]
enumhasil itu enumerate(daftar)
tampilkan enumhasil

tampilkan ""
tampilkan "=== Testing all() ==="
semua_benar itu [benar, benar, benar]
allhasil itu all(semua_benar)
tampilkan allhasil

tampilkan ""
// ... (more code)

```

---

### 24. Test Membership

**File:** `test_all/test_membership.rmc`  
**Description:** Test Membership  
**Lines:** 4

**Code Preview:**

```python
# Test membership
daftar itu [1, 2, 3]
x itu 2 dalam daftar
tampilkan x
```

---

### 25. Test Simple

**File:** `test_all/test_simple.rmc`  
**Description:** Test Simple  
**Lines:** 5

**Code Preview:**

```python
# Test simple bitwise
x itu 5
y itu 3
z itu x & y
tampilkan z
```

---

### 26. Test Statistics

**File:** `test_all/test_statistics.rmc`  
**Description:** Test Statistics  
**Lines:** 47

**Code Preview:**

```python
# Test Statistics Functions (Phase 6)

tampilkan "=== Testing Statistics Functions ==="

# Test data
data itu [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test median
tampilkan ""
tampilkan "Test median():"
tampilkan "Data: [1, 2, 3, 4, 5, 6, 7, 8, 9]"
med itu median(data)
tampilkan "Median: " + ke_teks(med)

# Test mode
tampilkan ""
tampilkan "Test mode():"
data_mode itu [1, 2, 2, 3, 3, 3, 4, 4, 5]
tampilkan "Data: [1, 2, 2, 3, 3, 3, 4, 4, 5]"
mod itu mode(data_mode)
// ... (more code)

```

---

### 27. Test String Validation

**File:** `test_all/test_string_validation.rmc`  
**Description:** Test String Validation  
**Lines:** 48

**Code Preview:**

```python
# Test String Validation Functions (Phase 3)

tampilkan "=== Testing String Validation Functions ==="

# Test is_alpha
tampilkan ""
tampilkan "Test is_alpha():"
tampilkan is_alpha("Hello")           # True
tampilkan is_alpha("Hello123")        # False
tampilkan is_alpha("HelloWorld")      # True

# Test is_digit
tampilkan ""
tampilkan "Test is_digit():"
tampilkan is_digit("12345")           # True
tampilkan is_digit("123.45")          # False
tampilkan is_digit("123abc")          # False

# Test is_alnum
tampilkan ""
// ... (more code)

```

---

### 28. Test Switch Case

**File:** `test_all/test_switch_case.rmc`  
**Description:** Test Switch Case  
**Lines:** 65

**Code Preview:**

```python
# Test Switch/Case Statement (Phase 5)

tampilkan "=== Testing Switch/Case Statement ==="

# Test 1: Basic switch with numbers
tampilkan ""
tampilkan "Test 1: Basic switch with numbers"
nilai itu 2

cocok nilai
    kasus 1:
        tampilkan "Satu"
    kasus 2:
        tampilkan "Dua"
    kasus 3:
        tampilkan "Tiga"
    bawaan:
        tampilkan "Lainnya"
selesai

// ... (more code)

```

---

### 29. Test Zip Simple

**File:** `test_all/test_zip_simple.rmc`  
**Description:** Test Zip Simple  
**Lines:** 4

**Code Preview:**

```python
# Simple zip test
a itu [1, 2, 3]
b itu ["x", "y", "z"]
tampilkan zip(a, b)
```

---

## Testing

**Total Examples:** 1

### 1. 01 Unittest Basics

**File:** `testing/01_unittest_basics.rmc`  
**Description:** Unit Testing - Testing Framework  
**Lines:** 429

**Code Preview:**

```python
// ============================================
// Unit Testing - Testing Framework
// ============================================
// Contoh penggunaan unittest untuk testing

tampilkan "=== Unit Testing Examples ==="
tampilkan ""

impor_python "unittest"

// ============================================
// 1. BASIC UNIT TEST
// ============================================

tampilkan "[1] Basic Unit Test Example..."
tampilkan ""

// Fungsi yang akan ditest
fungsi tambah(a, b):
    hasil a + b
// ... (more code)

```

---

## Utilities

**Total Examples:** 1

### 1. 01 Calculator

**File:** `utilities/01_calculator.rmc`  
**Description:** Utility: Kalkulator Lengkap  
**Lines:** 185

**Code Preview:**

```python
// ============================================
// Utility: Kalkulator Lengkap
// ============================================

tampilkan "╔════════════════════════════════════════╗"
tampilkan "║        KALKULATOR LENGKAP             ║"
tampilkan "╚════════════════════════════════════════╝"
tampilkan ""

// Fungsi operasi dasar
buat fungsi penjumlahan dengan a, b
    hasil a + b
selesai

buat fungsi pengurangan dengan a, b
    hasil a - b
selesai

buat fungsi perkalian dengan a, b
    hasil a * b
// ... (more code)

```

---

## Web Development

**Total Examples:** 2

### 1. 01 Http Server

**File:** `web_development/01_http_server.rmc`  
**Description:** HTTP Server - Simple Web Server  
**Lines:** 66

**Code Preview:**

```python
// ============================================
// HTTP Server - Simple Web Server
// ============================================
// Membuat web server sederhana dengan Python http.server

tampilkan "=== Simple HTTP Server ==="
tampilkan ""

impor_python "http.server"
impor_python "socketserver"
impor_python "os"

tampilkan "[1] Konfigurasi Server..."
PORT itu 8080
DIRECTORY itu "."

tampilkan f"Port: {PORT}"
tampilkan f"Directory: {DIRECTORY}"
tampilkan ""

// ... (more code)

```

---

### 2. 02 Flask Api

**File:** `web_development/02_flask_api.rmc`  
**Description:** Flask REST API - Web Framework  
**Lines:** 151

**Code Preview:**

```python
// ============================================
// Flask REST API - Web Framework
// ============================================
// Membuat REST API sederhana dengan Flask

tampilkan "=== Flask REST API Example ==="
tampilkan ""

// Note: Install Flask terlebih dahulu: pip install flask

coba
    impor_python "flask"
    
    tampilkan "[1] Inisialisasi Flask App..."
    
    // Data storage sederhana (in-memory)
    data_mahasiswa itu [
        {"id": 1, "nim": "12345", "nama": "Budi Santoso", "jurusan": "Teknik Informatika"},
        {"id": 2, "nim": "12346", "nama": "Ani Wijaya", "jurusan": "Sistem Informasi"},
        {"id": 3, "nim": "12347", "nama": "Citra Dewi", "jurusan": "Teknik Komputer"}
// ... (more code)

```

---

