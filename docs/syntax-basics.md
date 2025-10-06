# 📖 Syntax Basics - RenzMcLang latest version

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Overview

RenzMcLang menggunakan sintaks Bahasa Indonesia yang intuitif dan mudah dipahami. Panduan ini mencakup semua dasar sintaks yang perlu Anda ketahui.

---

## 📋 Table of Contents

1. [Comments](#comments)
2. [Variables](#variables)
3. [Data Types](#data-types)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Loops](#loops)
7. [Functions](#functions)
8. [Input/Output](#inputoutput)
9. [Multiline Support](#multiline-support)

---

## Comments

### Single Line Comments
```python
// Ini adalah komentar satu baris
tampilkan "Hello"  // Komentar di akhir baris
```

### Multi-line Comments
```python
/*
Ini adalah komentar
multi-baris
*/
```

---

## Variables

### Variable Declaration

```python
// Menggunakan keyword 'itu'
nama itu "Budi"
umur itu 25
tinggi itu 175.5
is_student itu benar

// Menggunakan keyword 'adalah'
x adalah 10
y adalah 20
```

### Variable Naming Rules

✅ **Valid:**
```python
nama itu "Budi"
nama_lengkap itu "Budi Santoso"
umur_2024 itu 25
_private itu "secret"
```

❌ **Invalid:**
```python
2nama itu "Budi"      // Tidak boleh dimulai dengan angka
nama-lengkap itu "X"  // Tidak boleh menggunakan dash
jika itu "test"       // Tidak boleh menggunakan keyword
```

### Variable Assignment

```python
// Simple assignment
x itu 10

// Multiple assignment
a itu b itu c itu 0

// Swap values
x itu 5
y itu 10
temp itu x
x itu y
y itu temp
```

---

## Data Types

### 1. Numbers

#### Integer (Bilangan Bulat)
```python
angka_positif itu 42
angka_negatif itu -17
angka_besar itu 1000000
```

#### Float (Bilangan Desimal)
```python
pi itu 3.14159
suhu itu -5.5
tinggi itu 175.8
```

### 2. Strings (Teks)

#### String Declaration
```python
// Single quotes
nama itu 'Budi'

// Double quotes
pesan itu "Hello, World!"

// Multi-line string
alamat itu """
Jalan Merdeka No. 123
Jakarta Pusat
Indonesia
"""
```

#### String Operations
```python
// Concatenation
nama_depan itu "Budi"
nama_belakang itu "Santoso"
nama_lengkap itu nama_depan + " " + nama_belakang

// String repetition
garis itu "=" * 50

// String indexing
teks itu "Hello"
huruf_pertama itu teks[0]  // "H"
huruf_terakhir itu teks[-1]  // "o"

// String slicing
kata itu "Programming"
bagian itu kata[0:4]  // "Prog"
```

#### F-Strings (String Interpolation)
```python
nama itu "Budi"
umur itu 25

// F-string
pesan itu f"Nama saya {nama}, umur {umur} tahun"
tampilkan pesan  // Output: Nama saya Budi, umur 25 tahun

// With expressions
harga itu 100000
pajak itu 0.1
total itu f"Total: Rp {harga * (1 + pajak)}"
```

### 3. Booleans

```python
// Boolean values
benar_value itu benar
salah_value itu salah

// Boolean from comparison
is_adult itu umur >= 18
is_student itu benar
has_license itu salah
```

### 4. Lists (Daftar)

```python
// Empty list
daftar_kosong itu []

// List with values
angka itu [1, 2, 3, 4, 5]
nama itu ["Budi", "Ani", "Citra"]
campuran itu [1, "dua", 3.0, benar]

// List operations
angka.tambah(6)           // Add element
angka.hapus(3)            // Remove element
panjang itu panjang(angka)  // Get length
pertama itu angka[0]      // Access element
terakhir itu angka[-1]    // Last element
```

### 5. Dictionaries (Kamus)

```python
// Empty dictionary
kamus_kosong itu {}

// Dictionary with values
mahasiswa itu {
    "nama": "Budi",
    "umur": 25,
    "jurusan": "Informatika"
}

// Access values
nama itu mahasiswa["nama"]
umur itu mahasiswa["umur"]

// Add/update values
mahasiswa["email"] itu "budi@example.com"
mahasiswa["umur"] itu 26

// Check key existence
jika "nama" dalam mahasiswa
    tampilkan "Nama ada"
selesai
```

### 6. Sets (Himpunan)

```python
// Empty set
himpunan_kosong itu set()

// Set with values
angka itu {1, 2, 3, 4, 5}
huruf itu {"a", "b", "c"}

// Set operations
angka.tambah(6)           // Add element
angka.hapus(3)            // Remove element
panjang itu panjang(angka)  // Get length
```

### 7. Tuples

```python
// Tuple declaration
koordinat itu (10, 20)
rgb itu (255, 128, 0)

// Tuple unpacking
x, y itu koordinat
r, g, b itu rgb

// Access elements
pertama itu koordinat[0]
kedua itu koordinat[1]
```

---

## Operators

### 1. Arithmetic Operators

```python
// Addition
hasil itu 10 + 5  // 15

// Subtraction
hasil itu 10 - 5  // 5

// Multiplication
hasil itu 10 * 5  // 50

// Division
hasil itu 10 / 5  // 2.0

// Floor Division
hasil itu 10 // 3  // 3

// Modulus
hasil itu 10 % 3  // 1

// Exponentiation
hasil itu 2 ** 3  // 8
```

### 2. Comparison Operators

```python
// Equal to
hasil itu 5 == 5  // benar

// Not equal to
hasil itu 5 != 3  // benar

// Greater than
hasil itu 5 > 3  // benar

// Less than
hasil itu 5 < 3  // salah

// Greater than or equal
hasil itu 5 >= 5  // benar

// Less than or equal
hasil itu 5 <= 3  // salah
```

### 3. Logical Operators

```python
// AND
hasil itu benar dan benar  // benar
hasil itu benar dan salah  // salah

// OR
hasil itu benar atau salah  // benar
hasil itu salah atau salah  // salah

// NOT
hasil itu tidak benar  // salah
hasil itu tidak salah  // benar
```

### 4. Assignment Operators

```python
// Simple assignment
x itu 10

// Compound assignment
x += 5   // x = x + 5
x -= 3   // x = x - 3
x *= 2   // x = x * 2
x /= 4   // x = x / 4
x %= 3   // x = x % 3
x **= 2  // x = x ** 2
```

### 5. Membership Operators

```python
// in
hasil itu "a" dalam ["a", "b", "c"]  // benar
hasil itu 5 dalam [1, 2, 3]          // salah

// not in
hasil itu "d" tidak dalam ["a", "b", "c"]  // benar
```

### 6. Bitwise Operators

```python
// AND
hasil itu 5 & 3  // 1

// OR
hasil itu 5 | 3  // 7

// XOR
hasil itu 5 ^ 3  // 6

// NOT
hasil itu ~5  // -6

// Left shift
hasil itu 5 << 1  // 10

// Right shift
hasil itu 5 >> 1  // 2
```

---

## Control Flow

### 1. If Statement

```python
// Simple if
jika umur >= 18
    tampilkan "Dewasa"
selesai

// If-else
jika nilai >= 60
    tampilkan "Lulus"
kalau_tidak
    tampilkan "Tidak Lulus"
selesai

// If-elif-else
jika nilai >= 90
    tampilkan "A"
kalau_tidak_jika nilai >= 80
    tampilkan "B"
kalau_tidak_jika nilai >= 70
    tampilkan "C"
kalau_tidak
    tampilkan "D"
selesai
```

### 2. Ternary Operator

```python
// Inline if-else
status itu "Lulus" jika nilai >= 60 kalau tidak "Tidak Lulus"

// With expressions
max_value itu a jika a > b kalau tidak b
```

### 3. Switch/Case Statement

```python
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
```

---

## Loops

### 1. For Loop

#### Range-based For Loop
```python
// Loop from 1 to 10
untuk x dari 1 sampai 10
    tampilkan x
selesai

// Loop with step
untuk x dari 0 sampai 20 dengan langkah 2
    tampilkan x
selesai
```

#### For Each Loop
```python
// Iterate over list
buah itu ["apel", "jeruk", "mangga"]
untuk setiap item dari buah
    tampilkan item
selesai

// Iterate over dictionary
mahasiswa itu {"nama": "Budi", "umur": 25}
untuk setiap key dari mahasiswa
    tampilkan f"{key}: {mahasiswa[key]}"
selesai
```

### 2. While Loop

```python
// Simple while loop
counter itu 0
selama counter < 5
    tampilkan counter
    counter += 1
selesai

// While with condition
input_valid itu salah
selama tidak input_valid
    nilai itu input("Masukkan angka: ")
    jika nilai.isdigit()
        input_valid itu benar
    selesai
selesai
```

### 3. Loop Control

#### Break
```python
// Exit loop early
untuk x dari 1 sampai 10
    jika x == 5
        berhenti
    selesai
    tampilkan x
selesai
```

#### Continue
```python
// Skip iteration
untuk x dari 1 sampai 10
    jika x % 2 == 0
        lanjut
    selesai
    tampilkan x  // Only odd numbers
selesai
```

---

## Functions

### 1. Function Declaration

```python
// Simple function
fungsi sapa():
    tampilkan "Hello!"
selesai

// Call function
sapa()
```

### 2. Function with Parameters

```python
// Function with parameters
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

// Call with argument
sapa("Budi")
```

### 3. Function with Return Value

```python
// Function with return
fungsi tambah(a, b):
    hasil a + b
selesai

// Use return value
total itu tambah(5, 3)
tampilkan total  // 8
```

### 4. Function with Default Parameters

```python
// Default parameters
fungsi sapa(nama, sapaan="Halo"):
    tampilkan f"{sapaan}, {nama}!"
selesai

// Call with default
sapa("Budi")  // Output: Halo, Budi!

// Call with custom
sapa("Budi", "Selamat pagi")  // Output: Selamat pagi, Budi!
```

### 5. Lambda Functions

```python
// Lambda function
kuadrat itu lambda dengan x -> x * x

// Use lambda
hasil itu kuadrat(5)  // 25

// Lambda with multiple parameters
tambah itu lambda dengan a, b -> a + b
total itu tambah(3, 4)  // 7
```

---

## Input/Output

### 1. Output (Print)

```python
// Simple print
tampilkan "Hello, World!"

// Print multiple values
tampilkan "Nama:", nama, "Umur:", umur

// Print with f-string
tampilkan f"Nama: {nama}, Umur: {umur}"

// Multiline print with parentheses
tampilkan(
    "This is a",
    "multiline",
    "print statement"
)
```

### 2. Input

```python
// Get user input
nama itu input("Masukkan nama: ")

// Convert to number
umur itu ke_angka(input("Masukkan umur: "))

// Convert to integer
nilai itu ke_bulat(input("Masukkan nilai: "))
```

### 3. File I/O

```python
// Write to file
dengan buka("data.txt", "w") sebagai f
    f.tulis("Hello, World!")
selesai

// Read from file
dengan buka("data.txt", "r") sebagai f
    content itu f.baca()
    tampilkan content
selesai

// Append to file
dengan buka("data.txt", "a") sebagai f
    f.tulis("\nBaris baru")
selesai
```

---

## Multiline Support

RenzMcLang supports multiline syntax for better code readability, especially when dealing with long function calls or complex data structures.

### 1. Multiline Function Calls

```python
// Function calls can span multiple lines
text itu "hello world"
hasil itu text.replace(
    "world",
    "python"
)

// Python integration with multiline
impor_python "builtins"
hasil2 itu panggil_python builtins.str(
    "hello world"
)
```

### 2. Multiline Print Statements

```python
// Print with parentheses for multiline
tampilkan(
    "Line 1",
    "Line 2",
    "Line 3"
)
```

### 3. Multiline Data Structures

```python
// Multiline lists
items itu [
    "item1",
    "item2",
    "item3",
    "item4"
]

// Multiline dictionaries
person itu {
    "name": "John",
    "age": 30,
    "city": "Jakarta",
    "email": "john@example.com"
}

// Multiline sets
numbers itu {
    1,
    2,
    3,
    4,
    5
}
```

### 4. Else Clause Variations

```python
// Both syntaxes are supported
jika nilai >= 60
    tampilkan "Lulus"
kalau_tidak  // Using underscore
    tampilkan "Tidak Lulus"
selesai

// Or using two words
jika nilai >= 60
    tampilkan "Lulus"
kalau tidak  // Using space
    tampilkan "Tidak Lulus"
selesai
```

### 5. Best Practices for Multiline

```python
// ✅ Good - Clear and readable
hasil itu text.format(
    title="Document",
    content="Content here",
    author="John Doe"
)

// ✅ Good - Consistent indentation
data itu {
    "user": {
        "name": "John",
        "email": "john@example.com"
    },
    "settings": {
        "theme": "dark",
        "language": "id"
    }
}

// ❌ Bad - Inconsistent formatting
hasil itu text.format(title="Document",
content="Content",author="John")
```

---

## 💡 Best Practices

### 1. Naming Conventions

```python
// ✅ Good
nama_lengkap itu "Budi Santoso"
total_harga itu 100000
is_valid itu benar

// ❌ Bad
n itu "Budi"
x itu 100000
flag itu benar
```

### 2. Code Organization

```python
// ✅ Good - Clear and organized
fungsi hitung_total(harga, pajak):
    subtotal itu harga
    pajak_amount itu harga * pajak
    total itu subtotal + pajak_amount
    hasil total
selesai

// ❌ Bad - Unclear
fungsi h(x, y):
    hasil x + x * y
selesai
```

### 3. Comments

```python
// ✅ Good - Helpful comments
// Hitung total harga dengan pajak 10%
total itu harga * 1.1

// ❌ Bad - Obvious comments
// Tambah 1 ke x
x itu x + 1
```

---

## 📚 Next Steps

After learning the basics:

1. **Advanced Features:** Learn [Advanced Features](advanced-features.md)
2. **Built-in Functions:** Explore [Built-in Functions](builtin-functions.md)
3. **Examples:** Try [Examples](examples.md)
4. **Python Integration:** See [Python Integration](python-integration.md)

---

**Happy Coding! 🚀**