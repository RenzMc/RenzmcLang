# Fitur Lanjutan RenzMcLang (Terverifikasi)

## 🚨 PENTING: Hanya fitur yang TERVERIFIKASI yang ditampilkan

Dokumen ini hanya berisi fitur-fitur lanjutan yang telah diuji dan dikonfirmasi bekerja di RenzMcLang. Banyak "fitur lanjutan" yang didokumentasikan di tempat lain ternyata tidak diimplementasikan.

---

## Table of Contents

1. [Import System Lanjutan](#import-system-lanjutan)
2. [Lambda Functions](#lambda-functions)
3. [Error Handling](#error-handling)
4. [Object-Oriented Programming](#object-oriented-programming)
5. [Python Integration](#python-integration)

---

## Import System Lanjutan ✅

RenzMcLang memiliki sistem import yang powerful dan sudah terverifikasi bekerja dengan baik.

### 1. Wildcard Import (Import All)

**Sintaks:** `dari module impor *`

**Deskripsi:** Import semua item publik dari module.

**Contoh:**
```python
// math_utils.rmc
buat fungsi tambah dengan a, b
    hasil a + b
selesai

buat fungsi kali dengan a, b
    hasil a * b
selesai

PI itu 3.14159

// main.rmc
dari math_utils impor *

// Semua fungsi dan variabel publik bisa digunakan
hasil1 itu panggil tambah dengan 10, 5
tampilkan hasil1  // Output: 15

hasil2 itu panggil kali dengan 4, 6
tampilkan hasil2  // Output: 24

tampilkan PI      // Output: 3.14159
```

### 2. Import Multiple Items

**Contoh:**
```python
// Import beberapa fungsi sekaligus
dari math_utils impor tambah, kali, bagi

// Gunakan fungsi yang diimpor
hasil1 it panggil tambah dengan 10, 5      // 15
hasil2 it panggil kali dengan 4, 7         // 28
hasil3 it panggil bagi dengan 20, 4        // 5.0
```

### 3. Import Constants

**Contoh:**
```python
// constants.rmc
APP_NAME it "MyApp"
VERSION it "1.0.0"
MAX_USERS it 100

// main.rmc
dari constants impor APP_NAME, VERSION, MAX_USERS

tampilkan f"{APP_NAME} v{VERSION}"  // Output: MyApp v1.0.0
tampilkan f"Max users: {MAX_USERS}"  // Output: Max users: 100
```

---

## Lambda Functions ✅

Lambda functions adalah fungsi anonim yang singkat dan berguna.

### Sintaks Dasar

```python
// Sintaks: lambda dengan parameter -> ekspresi
kuadrat it lambda dengan x -> x * x
tambah it lambda dengan a, b -> a + b
```

### Penggunaan Lambda

```python
// Lambda untuk operasi sederhana
kuadrat it lambda dengan x -> x * x
hasil it panggil kuadrat dengan 5
tampilkan hasil  // Output: 25

// Lambda dengan multiple parameters
tambah it lambda dengan a, b -> a + b
total it panggil tambah dengan 10, 3
tampilkan total  // Output: 13
```

---

## Error Handling ✅

RenzMcLang mendukung error handling dengan sintaks yang intuitif.

### 1. Try-Catch Dasar

```python
// Try-catch sederhana
coba
    // Kode yang mungkin error
    hasil it 10 / 0
tangkap error
    tampilkan f"Terjadi error: {error}"
selesai
```

### 2. Try-Catch-Finally

```python
// Dengan finally block
coba
    file it buka("data.txt", "r")
    // Baca file
tangkap error
    tampilkan "Error membaca file"
akhirnya
    tampilkan "Cleanup resources"
selesai
```

---

## Object-Oriented Programming ✅

RenzMcLang menggunakan pendekatan function-based untuk OOP yang praktis dan efektif.

### 1. Class dengan Constructor

```python
// Constructor function
buat fungsi buat_Person dengan nama, umur:
    person it {
        "nama": nama,
        "umur": umur,
        "active": benar
    }
    hasil person
selesai

// Method function
buat fungsi Person_info dengan self:
    hasil f"{self['nama']} ({self['umur']} tahun)"
selesai

// Gunakan class
orang it panggil buat_Person dengan "Budi", 25
info it panggil Person_info dengan orang
tampilkan info  // Output: Budi (25 tahun)
```

### 2. Inheritance

```python
// Child class constructor
buat fungsi buat_Student dengan nama, umur, jurusan:
    student it {
        "nama": nama,
        "umur": umur,
        "jurusan": jurusan,
        "type": "Student",
        "nilai": []
    }
    hasil student
selesai
```

---

## Python Integration ✅

RenzMcLang memiliki integrasi yang kuat dengan Python ecosystem.

### 1. Import Python Modules

```python
// Import library Python
impor_python "math"
impor_python "datetime"
impor_python "requests"
impor_python "json"
```

### 2. Gunakan Python Functions

```python
// Math operations
hasil it panggil_python math.sqrt(16)
tampilkan hasil  // Output: 4.0

pi it panggil_python math.pi
tampilkan f"Pi: {pi}"
```

---

## 🚫 FITUR YANG TIDAK DIDUKUNG

Fitur-fitur berikut TIDAK bekerja di RenzMcLang saat ini:

1. **❌ Async/Await** - `fungsi async` tidak dikenali parser
2. **❌ List/Dict Comprehensions** - Sintaks `[x for x in list]` tidak didukung
3. **❌ Decorators** - `@decorator` syntax bermasalah
4. **❌ Pattern Matching** - `cocok` hanya untuk switch-case sederhana
5. **❌ Type Hints** - Sintaks type annotation tidak didukung
6. **❌ Generators** - `yield` keyword tidak dikenali
7. **❌ Context Managers** - `dengan` statement terbatas untuk file

---

## Best Practices

### 1. Error Handling
```python
// SELALU gunakan try-catch untuk operasi yang bisa gagal
coba
    data it baca_file("config.json")
tangkap error
    tampilkan f"Gagal baca config: {error}"
    data it {}  // Default value
selesai
```

### 2. OOP Patterns
```python
// Gunakan convention untuk encapsulation
buat fungsi buat_Class dengan params:
    obj it {
        "_private": "private data",  // Prefix _ untuk private
        "public": "public data"
    }
    hasil obj
selesai
```

---

## Troubleshooting

### Error Umum dan Solusi

1. **"Token tidak dikenal"**
   - Cek sintaks yang digunakan
   - Pastikan tidak menggunakan fitur yang tidak didukung

2. **"Variabel tidak terdefinisi"**
   - Pastikan variabel dideklarasikan dengan `itu`
   - Jangan gunakan `adalah`

---

## Conclusion

RenzMcLang memiliki fitur lanjutan yang solid:
- ✅ Import system yang powerful
- ✅ Lambda functions
- ✅ Error handling yang robust
- ✅ OOP yang praktis
- ✅ Python integration yang lengkap

Fokus pada fitur yang benar-benar bekerja akan memberikan pengalaman development yang lebih baik!

---

*Untuk informasi lebih lanjut, lihat [Built-in Functions](builtin_functions/)*