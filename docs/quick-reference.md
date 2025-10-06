# ⚡ Quick Reference - RenzMcLang latest version

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Cheat Sheet

### Variables & Data Types

```python
// Variables
nama itu "Budi"
umur itu 25
tinggi itu 175.5
is_student itu benar

// Lists
angka itu [1, 2, 3, 4, 5]
nama itu ["Budi", "Ani", "Citra"]

// Dictionaries
mahasiswa itu {
    "nama": "Budi",
    "umur": 25,
    "nim": "12345"
}

// Sets
unique itu {1, 2, 3, 4, 5}

// Tuples
koordinat itu (10, 20)
```

---

### Operators

```python
// Arithmetic
10 + 5    // Addition
10 - 5    // Subtraction
10 * 5    // Multiplication
10 / 5    // Division
10 // 3   // Floor division
10 % 3    // Modulus
2 ** 3    // Exponentiation

// Comparison
5 == 5    // Equal
5 != 3    // Not equal
5 > 3     // Greater than
5 < 3     // Less than
5 >= 5    // Greater or equal
5 <= 3    // Less or equal

// Logical
benar dan benar    // AND
benar atau salah   // OR
tidak benar        // NOT

// Membership
"a" dalam ["a", "b"]      // in
"d" tidak dalam ["a", "b"] // not in

// Bitwise
5 & 3     // AND
5 | 3     // OR
5 ^ 3     // XOR
~5        // NOT
5 << 1    // Left shift
5 >> 1    // Right shift
```

---

### Control Flow

```python
// If-else (both syntaxes supported)
jika kondisi
    // code
kalau_tidak_jika kondisi2  // Using underscore
    // code
kalau_tidak  // Using underscore
    // code
selesai

// Or using space
jika kondisi
    // code
kalau tidak jika kondisi2  // Using space
    // code
kalau tidak  // Using space
    // code
selesai

// Ternary
hasil itu "A" jika nilai >= 90 kalau tidak "B"

// Switch/case
cocok nilai
    kasus 1:
        // code
    kasus 2:
        // code
    bawaan:
        // code
selesai
```

---

### Loops

```python
// For loop (range)
untuk x dari 1 sampai 10
    tampilkan x
selesai

// For each
untuk setiap item dari daftar
    tampilkan item
selesai

// While loop
selama kondisi
    // code
selesai

// Break & Continue
untuk x dari 1 sampai 10
    jika x == 5
        berhenti  // break
    selesai
    jika x % 2 == 0
        lanjut    // continue
    selesai
    tampilkan x
selesai
```

---

### Functions

```python
// Basic function
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

// Function with return
fungsi tambah(a, b):
    hasil a + b
selesai

// Default parameters
fungsi sapa(nama, sapaan="Halo"):
    tampilkan f"{sapaan}, {nama}!"
selesai

// Lambda
kuadrat itu lambda dengan x -> x * x
tambah itu lambda dengan a, b -> a + b
```

---

### Classes (OOP)

```python
// Basic class
kelas Mahasiswa:
    konstruktor(nama, nim):
        diri.nama itu nama
        diri.nim itu nim
    selesai
    
    metode info():
        tampilkan f"Nama: {diri.nama}"
    selesai
selesai

// Inheritance
kelas MahasiswaS1 warisi Mahasiswa:
    konstruktor(nama, nim, jurusan):
        super().__init__(nama, nim)
        diri.jurusan itu jurusan
    selesai
selesai

// Create instance
mhs itu Mahasiswa("Budi", "12345")
mhs.info()
```

---

### String Operations

```python
// Basic
panjang(teks)              // Length
huruf_besar(teks)          // Uppercase
huruf_kecil(teks)          // Lowercase
huruf_kapital(teks)        // Capitalize

// Manipulation
potong(teks, 0, 5)         // Slice
ganti(teks, "old", "new")  // Replace
pisah(teks, ",")           // Split
gabung("-", list)          // Join
hapus_spasi(teks)          // Strip

// Search
cari(teks, "sub")          // Find
mulai_dengan(teks, "pre")  // Startswith
akhiri_dengan(teks, "suf") // Endswith

// Validation
adalah_angka(teks)         // Is digit
adalah_huruf(teks)         // Is alpha
adalah_alfanumerik(teks)   // Is alnum

// F-strings
pesan itu f"Nama: {nama}, Umur: {umur}"
```

---

### List Operations

```python
// Basic
panjang(list)              // Length
tambah(list, item)         // Append
hapus(list, item)          // Remove
sisipkan(list, idx, item)  // Insert

// Sorting
urutkan(list)              // Sort
balik(list)                // Reverse

// Aggregation
jumlah(list)               // Sum
min(list)                  // Minimum
max(list)                  // Maximum

// Comprehension
[x * 2 untuk setiap x dari list]
[x untuk setiap x dari list jika x > 0]
```

---

### Dict Operations

```python
// Access
nilai itu dict["key"]
nilai itu dict.get("key", default)

// Modify
dict["key"] itu "value"
perbarui(dict, other_dict)

// Keys & Values
kunci(dict)                // Keys
nilai(dict)                // Values
items(dict)                // Items

// Check
"key" dalam dict           // Has key

// Comprehension
{k: v * 2 untuk setiap k, v dari dict.items()}
```

---

### File Operations

```python
// Read
content itu baca_file("file.txt")
lines itu baca_baris("file.txt")

// Write
tulis_file("file.txt", content)
tambah_file("file.txt", content)

// Check & Delete
ada_file("file.txt")
hapus_file("file.txt")

// Context manager
dengan buka("file.txt", "r") sebagai f
    content itu f.baca()
selesai
```

---

### JSON Operations

```python
// Parse
data itu json_parse(json_string)

// Stringify
json_str itu json_stringify(data)

// File I/O
data itu json_baca("data.json")
json_tulis("data.json", data)
```

---

### HTTP Operations (NEW in latest version!)

```python
// GET request
response itu http_get("https://api.example.com/users")
tampilkan response.status_code
data itu response.json()

// POST request
payload itu {"nama": "Budi", "email": "budi@example.com"}
response itu http_post("https://api.example.com/users", json=payload)

// PUT request
response itu http_put("https://api.example.com/users/1", json=data)

// DELETE request
response itu http_delete("https://api.example.com/users/1")

// With parameters
params itu {"page": 1, "limit": 10}
response itu http_get("https://api.example.com/users", params=params)

// With headers
headers itu {"Authorization": "Bearer token123"}
response itu http_get("https://api.example.com/data", headers=headers)

// Indonesian aliases
response itu ambil_http(url)      // GET
response itu kirim_http(url, ...)  // POST
response itu perbarui_http(url, ...) // PUT
response itu hapus_http(url)       // DELETE
```

---

### Math Operations

```python
// Basic
absolut(x)                 // Absolute value
bulat(x, digits)           // Round
pembulatan_atas(x)         // Ceil
pembulatan_bawah(x)        // Floor
pangkat(base, exp)         // Power
akar(x)                    // Square root

// Trigonometry
sinus(x)                   // Sin
cosinus(x)                 // Cos
tangen(x)                  // Tan

// Statistics
rata_rata(list)            // Mean
nilai_tengah(list)         // Median
modus(list)                // Mode
deviasi_standar(list)      // Std dev
variansi(list)             // Variance

// Random
acak()                     // Random 0-1
acak_bulat(min, max)       // Random int
pilih_acak(list)           // Random choice
```

---

### Error Handling

```python
// Try-catch
coba
    // code that might fail
tangkap ErrorType sebagai e
    // handle error
akhirnya
    // cleanup
selesai

// Raise error
raise Exception("Error message")

// Custom exception
kelas CustomError warisi Exception:
    konstruktor(message):
        diri.message itu message
    selesai
selesai
```

---

### Async/Await

```python
// Async function
async fungsi fetch_data(url):
    response itu await http_get(url)
    hasil response.json()
selesai

// Call async
data itu await fetch_data("https://api.example.com")

// Multiple async
async fungsi main():
    data1 itu await fetch_data(url1)
    data2 itu await fetch_data(url2)
selesai

await main()
```

---

### Comprehensions

```python
// List comprehension
[x * 2 untuk setiap x dari list]
[x untuk setiap x dari list jika x > 0]

// Dict comprehension
{k: v * 2 untuk setiap k, v dari dict.items()}
{x: x ** 2 untuk setiap x dari range(5)}

// Set comprehension
{x * 2 untuk setiap x dari list}

// Nested
[[i * j untuk setiap j dari range(3)] untuk setiap i dari range(3)]
```

---

### Python Integration

```python
// Import module
impor_python "math"
impor_python "numpy" sebagai np

// Import specific
dari_python "math" impor sqrt, pi

// Call Python function
hasil itu panggil_python math.sqrt(16)
array itu panggil_python np.array([1, 2, 3])

// Use Python library
impor_python "requests"
response itu panggil_python requests.get(url)
```

---

### REPL Commands (NEW in latest version!)

```bash
# Start REPL
rmc

# REPL commands
>>> bantuan      # Show help
>>> keluar       # Exit REPL
>>> bersih       # Clear screen
>>> riwayat      # Show history
>>> reset        # Reset interpreter
>>> variabel     # Show all variables
```

---

### Type Conversion

```python
// To string
ke_teks(value)
str(value)

// To number
ke_angka(value)
float(value)

// To integer
ke_bulat(value)
int(value)

// To boolean
ke_boolean(value)
bool(value)

// To list
ke_list(value)
list(value)
```

---

### Iteration Functions

```python
// Map
map(lambda dengan x -> x * 2, list)

// Filter
filter(lambda dengan x -> x > 0, list)

// Reduce
reduce(lambda dengan a, b -> a + b, list)

// Zip
zip(list1, list2)

// Enumerate
enumerate(list)

// Range
range(10)
range(1, 11)
range(0, 20, 2)
```

---

### Common Patterns

#### 1. Read and Process File
```python
dengan buka("data.txt", "r") sebagai f
    untuk setiap line dari f
        processed itu line.strip()
        tampilkan processed
    selesai
selesai
```

#### 2. API Request with Error Handling
```python
coba
    response itu http_get("https://api.example.com/data")
    jika response.ok()
        data itu response.json()
        // process data
    kalau_tidak
        tampilkan f"Error: {response.status_code}"
    selesai
tangkap Exception sebagai e
    tampilkan f"Request failed: {e}"
selesai
```

#### 3. List Processing
```python
// Filter and transform
angka itu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap itu [x untuk setiap x dari angka jika x % 2 == 0]
kuadrat itu [x ** 2 untuk setiap x dari genap]
tampilkan kuadrat  // [4, 16, 36, 64, 100]
```

#### 4. Dictionary Manipulation
```python
// Merge dictionaries
dict1 itu {"a": 1, "b": 2}
dict2 itu {"c": 3, "d": 4}
merged itu {**dict1, **dict2}

// Filter dictionary
filtered itu {k: v untuk setiap k, v dari dict.items() jika v > 10}
```

#### 5. Class with Properties
```python
kelas User:
    konstruktor(nama):
        diri._nama itu nama
    selesai
    
    @properti
    metode nama():
        hasil diri._nama
    selesai
    
    @nama.setter
    metode nama(value):
        diri._nama itu value
    selesai
selesai
```

---

## 🔑 Keywords

```
jika, kalau, maka, tidak, lainnya, selesai, akhir
selama, ulangi, kali, untuk, setiap, dari, sampai
lanjut, berhenti, lewati
coba, tangkap, akhirnya
cocok, kasus, bawaan
simpan, ke, dalam, itu, adalah, bukan
tampilkan, tunjukkan, tanya
buat, fungsi, dengan, parameter
panggil, jalankan, kembali, hasil, kembalikan
kelas, metode, konstruktor, warisi
gunakan, impor, impor_python, panggil_python
modul, paket
lambda, fungsi_cepat
async, asinkron, await, tunggu
yield, hasilkan, hasil_bertahap, hasil_dari
dekorator, properti, metode_statis, metode_kelas
sebagai, jenis_data, generator
dan, atau, benar, salah
self, ini, diri
```

---

## 📚 Quick Links

- [Installation](installation.md)
- [Syntax Basics](syntax-basics.md)
- [Built-in Functions](builtin-functions.md)
- [Advanced Features](advanced-features.md)
- [Python Integration](python-integration.md)
- [Examples](examples.md)

---

**Version: Latest**  
**Last Updated: 2025-10-04**

**New in latest version:**
- ✨ REPL (Interactive Shell)
- 🌐 Built-in HTTP Client
- 📦 7 new HTTP functions
- 🚀 No imports needed for HTTP!