# 🚀 Advanced Features - RenzMcLang latest version

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Overview

RenzMcLang menyediakan fitur-fitur advanced yang powerful untuk development modern, termasuk OOP, Async/Await, Comprehensions, dan banyak lagi.

---

## 📋 Table of Contents

1. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
2. [Async/Await](#asyncawait)
3. [Comprehensions](#comprehensions)
4. [Lambda Functions](#lambda-functions)
5. [Decorators](#decorators)
6. [Context Managers](#context-managers)
7. [Generators](#generators)
8. [Error Handling](#error-handling)
9. [Pattern Matching](#pattern-matching)
10. [Type Hints](#type-hints)

---

## Object-Oriented Programming (OOP)

### 1. Classes and Objects

#### Basic Class Definition

```python
kelas Mahasiswa:
    konstruktor(nama, nim):
        diri.nama itu nama
        diri.nim itu nim
        diri.nilai itu []
    selesai
    
    metode tambah_nilai(nilai):
        diri.nilai.tambah(nilai)
    selesai
    
    metode rata_rata():
        jika panjang(diri.nilai) == 0
            hasil 0
        selesai
        hasil jumlah(diri.nilai) / panjang(diri.nilai)
    selesai
    
    metode info():
        tampilkan f"Nama: {diri.nama}"
        tampilkan f"NIM: {diri.nim}"
        tampilkan f"Rata-rata: {diri.rata_rata()}"
    selesai
selesai

// Create instance
mhs itu Mahasiswa("Budi", "12345")
mhs.tambah_nilai(85)
mhs.tambah_nilai(90)
mhs.tambah_nilai(88)
mhs.info()
```

### 2. Inheritance

```python
// Base class
kelas Orang:
    konstruktor(nama, umur):
        diri.nama itu nama
        diri.umur itu umur
    selesai
    
    metode perkenalan():
        tampilkan f"Nama: {diri.nama}, Umur: {diri.umur}"
    selesai
selesai

// Derived class
kelas Mahasiswa warisi Orang:
    konstruktor(nama, umur, nim):
        super().__init__(nama, umur)
        diri.nim itu nim
    selesai
    
    metode perkenalan():
        super().perkenalan()
        tampilkan f"NIM: {diri.nim}"
    selesai
selesai

// Usage
mhs itu Mahasiswa("Budi", 20, "12345")
mhs.perkenalan()
```

### 3. Properties

```python
kelas BankAccount:
    konstruktor(nama, saldo_awal):
        diri.nama itu nama
        diri._saldo itu saldo_awal
    selesai
    
    @properti
    metode saldo():
        hasil diri._saldo
    selesai
    
    metode setor(jumlah):
        jika jumlah > 0
            diri._saldo += jumlah
            tampilkan f"Setor: Rp {jumlah}"
        selesai
    selesai
    
    metode tarik(jumlah):
        jika jumlah > 0 dan jumlah <= diri._saldo
            diri._saldo -= jumlah
            tampilkan f"Tarik: Rp {jumlah}"
        kalau_tidak
            tampilkan "Saldo tidak cukup"
        selesai
    selesai
selesai

// Usage
akun itu BankAccount("Budi", 1000000)
tampilkan f"Saldo: Rp {akun.saldo}"
akun.setor(500000)
akun.tarik(200000)
```

### 4. Static Methods

```python
kelas MathUtils:
    @metode_statis
    metode tambah(a, b):
        hasil a + b
    selesai
    
    @metode_statis
    metode kali(a, b):
        hasil a * b
    selesai
selesai

// Usage (no instance needed)
hasil itu MathUtils.tambah(5, 3)
tampilkan hasil  // 8
```

### 5. Class Methods

```python
kelas Counter:
    jumlah itu 0
    
    @metode_kelas
    metode increment(cls):
        cls.jumlah += 1
    selesai
    
    @metode_kelas
    metode get_count(cls):
        hasil cls.jumlah
    selesai
selesai

// Usage
Counter.increment()
Counter.increment()
tampilkan Counter.get_count()  // 2
```

---

## Async/Await

### 1. Async Functions

```python
async fungsi fetch_data(url):
    tampilkan f"Fetching from {url}..."
    await tidur(2)  // Simulate delay
    hasil f"Data from {url}"
selesai

// Call async function
hasil itu await fetch_data("https://api.example.com")
tampilkan hasil
```

### 2. Multiple Async Operations

```python
async fungsi process_user(user_id):
    tampilkan f"Processing user {user_id}..."
    await tidur(1)
    hasil f"User {user_id} processed"
selesai

async fungsi main():
    // Sequential
    hasil1 itu await process_user(1)
    hasil2 itu await process_user(2)
    
    tampilkan hasil1
    tampilkan hasil2
selesai

await main()
```

### 3. Async with HTTP

```python
async fungsi fetch_users():
    response itu await http_get("https://jsonplaceholder.typicode.com/users")
    data itu response.json()
    
    untuk setiap user dari data
        tampilkan f"User: {user['name']}"
    selesai
selesai

await fetch_users()
```

---

## Comprehensions

### 1. List Comprehension

```python
// Basic list comprehension
angka itu [1, 2, 3, 4, 5]
kuadrat itu [x * x untuk setiap x dari angka]
// [1, 4, 9, 16, 25]

// With condition
genap itu [x untuk setiap x dari angka jika x % 2 == 0]
// [2, 4]

// Nested comprehension
matrix itu [[i * j untuk setiap j dari [1, 2, 3]] untuk setiap i dari [1, 2, 3]]
// [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### 2. Dict Comprehension

```python
// Basic dict comprehension
angka itu [1, 2, 3, 4, 5]
kuadrat_dict itu {x: x * x untuk setiap x dari angka}
// {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

// With condition
genap_dict itu {x: x * x untuk setiap x dari angka jika x % 2 == 0}
// {2: 4, 4: 16}

// From two lists
keys itu ["a", "b", "c"]
values itu [1, 2, 3]
dict_result itu {k: v untuk setiap k, v dari zip(keys, values)}
// {"a": 1, "b": 2, "c": 3}
```

### 3. Set Comprehension

```python
// Basic set comprehension
angka itu [1, 2, 2, 3, 3, 4]
unique itu {x untuk setiap x dari angka}
// {1, 2, 3, 4}

// With transformation
huruf itu ["a", "b", "c"]
upper_set itu {x.upper() untuk setiap x dari huruf}
// {"A", "B", "C"}
```

---

## Lambda Functions

### 1. Basic Lambda

```python
// Simple lambda
kuadrat itu lambda dengan x -> x * x
tampilkan kuadrat(5)  // 25

// Lambda with multiple parameters
tambah itu lambda dengan a, b -> a + b
tampilkan tambah(3, 4)  // 7
```

### 2. Lambda with Map

```python
angka itu [1, 2, 3, 4, 5]
kuadrat itu map(lambda dengan x -> x * x, angka)
tampilkan kuadrat  // [1, 4, 9, 16, 25]
```

### 3. Lambda with Filter

```python
angka itu [1, 2, 3, 4, 5, 6]
genap itu filter(lambda dengan x -> x % 2 == 0, angka)
tampilkan genap  // [2, 4, 6]
```

### 4. Lambda with Sort

```python
data itu [{"nama": "Budi", "umur": 25}, {"nama": "Ani", "umur": 22}]
sorted_data itu sorted(data, key=lambda dengan x -> x["umur"])
```

---

## Decorators

### 1. Function Decorators

```python
fungsi timer(func):
    fungsi wrapper(*args, **kwargs):
        start itu waktu_sekarang()
        hasil itu func(*args, **kwargs)
        end itu waktu_sekarang()
        tampilkan f"Execution time: {end - start}s"
        hasil hasil
    selesai
    hasil wrapper
selesai

@timer
fungsi slow_function():
    tidur(2)
    tampilkan "Done!"
selesai

slow_function()
```

### 2. Class Decorators

```python
@dekorator
kelas Singleton:
    _instance itu kosong
    
    konstruktor():
        jika Singleton._instance tidak kosong
            raise Exception("Singleton already exists")
        selesai
        Singleton._instance itu diri
    selesai
selesai
```

---

## Context Managers

### 1. File Context Manager

```python
// Automatic file closing
dengan buka("data.txt", "r") sebagai f
    content itu f.baca()
    tampilkan content
selesai
// File automatically closed
```

### 2. Custom Context Manager

```python
kelas DatabaseConnection:
    konstruktor(db_name):
        diri.db_name itu db_name
        diri.connection itu kosong
    selesai
    
    metode __enter__():
        diri.connection itu connect(diri.db_name)
        hasil diri.connection
    selesai
    
    metode __exit__(exc_type, exc_val, exc_tb):
        jika diri.connection
            diri.connection.close()
        selesai
    selesai
selesai

// Usage
dengan DatabaseConnection("mydb") sebagai conn
    // Use connection
    data itu conn.query("SELECT * FROM users")
selesai
// Connection automatically closed
```

---

## Generators

### 1. Basic Generator

```python
fungsi countdown(n):
    selama n > 0
        hasilkan n
        n -= 1
    selesai
selesai

// Usage
untuk setiap num dari countdown(5)
    tampilkan num
selesai
// Output: 5, 4, 3, 2, 1
```

### 2. Generator Expression

```python
// Generator expression (lazy evaluation)
gen itu (x * x untuk setiap x dari range(1000000))

// Only compute when needed
untuk setiap val dari gen
    jika val > 100
        berhenti
    selesai
    tampilkan val
selesai
```

### 3. Yield From

```python
fungsi flatten(nested_list):
    untuk setiap item dari nested_list
        jika jenis(item) == list
            hasil_dari flatten(item)
        kalau_tidak
            hasilkan item
        selesai
    selesai
selesai

// Usage
nested itu [1, [2, 3], [4, [5, 6]]]
flat itu list(flatten(nested))
tampilkan flat  // [1, 2, 3, 4, 5, 6]
```

---

## Error Handling

### 1. Try-Catch-Finally

```python
coba
    // Code that might raise error
    nilai itu ke_angka(input("Masukkan angka: "))
    hasil itu 100 / nilai
    tampilkan f"Hasil: {hasil}"
tangkap ZeroDivisionError sebagai e
    tampilkan "Error: Tidak bisa dibagi nol"
tangkap ValueError sebagai e
    tampilkan "Error: Input bukan angka"
tangkap Exception sebagai e
    tampilkan f"Error: {e}"
akhirnya
    tampilkan "Selesai"
selesai
```

### 2. Custom Exceptions

```python
kelas ValidationError warisi Exception:
    konstruktor(message):
        diri.message itu message
    selesai
selesai

fungsi validate_age(age):
    jika age < 0
        raise ValidationError("Umur tidak boleh negatif")
    selesai
    jika age > 150
        raise ValidationError("Umur tidak valid")
    selesai
    hasil benar
selesai

// Usage
coba
    validate_age(-5)
tangkap ValidationError sebagai e
    tampilkan f"Validation error: {e.message}"
selesai
```

### 3. Error Propagation

```python
fungsi read_config(path):
    coba
        content itu baca_file(path)
        config itu json_parse(content)
        hasil config
    tangkap FileNotFoundError
        tampilkan f"Config file not found: {path}"
        raise  // Re-raise the exception
    tangkap JSONDecodeError
        tampilkan "Invalid JSON format"
        raise
    selesai
selesai
```

---

## Pattern Matching

### 1. Switch/Case

```python
fungsi process_command(cmd):
    cocok cmd
        kasus "start":
            tampilkan "Starting..."
        kasus "stop":
            tampilkan "Stopping..."
        kasus "restart":
            tampilkan "Restarting..."
        bawaan:
            tampilkan "Unknown command"
    selesai
selesai

process_command("start")
```

### 2. Pattern Matching with Values

```python
fungsi describe_number(n):
    cocok n
        kasus 0:
            hasil "zero"
        kasus 1:
            hasil "one"
        kasus n jika n > 0:
            hasil "positive"
        kasus n jika n < 0:
            hasil "negative"
        bawaan:
            hasil "unknown"
    selesai
selesai
```

---

## Type Hints

RenzMcLang memiliki sistem type hints yang robust dengan dukungan untuk:
- Basic types (Integer, String, Float, Boolean)
- Union types (Integer | String)
- Optional types (String?)
- Generic types (List[Integer], Dict[String, Integer])

Untuk dokumentasi lengkap, lihat [Type System Documentation](type-system.md).

### 1. Function Type Hints

```python
fungsi tambah(a: Integer, b: Integer):
    hasil a + b
selesai

fungsi sapa(nama: String):
    hasil f"Hello, {nama}!"
selesai
```

### 2. Variable Type Hints

```python
nama: String itu "Budi"
umur: Integer itu 25
is_student: Boolean itu benar
nilai: List[Integer] itu [85, 90, 88]
```

### 3. Union and Optional Types

```python
// Union types
nilai: Integer | String itu 42
nilai itu "empat puluh dua"  // OK

// Optional types
nama: String? itu "Budi"
nama itu kosong  // OK

// Generic types
data: Dict[String, Integer] itu {"Budi": 85, "Ani": 90}
```

---

## 💡 Best Practices

### 1. OOP Best Practices

```python
// ✅ Good - Clear class structure
kelas User:
    konstruktor(username, email):
        diri.username itu username
        diri.email itu email
        diri._password itu kosong
    selesai
    
    metode set_password(password):
        // Hash password
        diri._password itu hash(password)
    selesai
    
    metode verify_password(password):
        hasil hash(password) == diri._password
    selesai
selesai

// ❌ Bad - Exposing internal state
kelas User:
    konstruktor(username, email, password):
        diri.username itu username
        diri.email itu email
        diri.password itu password  // Direct access
    selesai
selesai
```

### 2. Async Best Practices

```python
// ✅ Good - Proper async usage
async fungsi fetch_all_users():
    users itu await http_get("/api/users")
    hasil users.json()
selesai

// ❌ Bad - Blocking in async
async fungsi fetch_all_users():
    users itu http_get("/api/users")  // Missing await
    hasil users.json()
selesai
```

### 3. Error Handling Best Practices

```python
// ✅ Good - Specific error handling
coba
    data itu json_parse(content)
tangkap JSONDecodeError sebagai e
    tampilkan f"Invalid JSON: {e}"
tangkap FileNotFoundError sebagai e
    tampilkan f"File not found: {e}"
selesai

// ❌ Bad - Catching all errors
coba
    data itu json_parse(content)
tangkap Exception sebagai e
    tampilkan "Something went wrong"
selesai
```

---

## 📚 See Also

- [Syntax Basics](syntax-basics.md) - Basic syntax
- [Built-in Functions](builtin-functions.md) - Built-in functions
- [Examples](examples.md) - Code examples
- [Python Integration](python-integration.md) - Python integration

---

**Version: Latest**  
**Last Updated: 2025-10-04**