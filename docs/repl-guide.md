# 🖥️ REPL Guide - RenzMcLang v0.0.4

**Last Updated:** 2025-10-04  
**Version:** 0.0.4  
**Feature:** NEW in v0.0.4!

---

## 🎯 What is REPL?

REPL (Read-Eval-Print Loop) adalah interactive shell yang memungkinkan Anda menjalankan kode RenzMcLang secara langsung dan melihat hasilnya secara real-time. Ini sangat berguna untuk:

- 🧪 Testing kode dengan cepat
- 📚 Belajar bahasa pemrograman
- 🔍 Debugging dan eksplorasi
- 💡 Eksperimen dengan fitur baru

---

## 🚀 Getting Started

### Starting REPL

```bash
# Start REPL
rmc

# Or
renzmc
```

### Welcome Screen

```
╔════════════════════════════════════════════════════════════════╗
║           RenzMcLang Interactive Shell (REPL)                 ║
║                    Version 0.0.4                               ║
╚════════════════════════════════════════════════════════════════╝

Selamat datang di RenzMcLang REPL!
Ketik 'bantuan' untuk melihat perintah yang tersedia
Ketik 'keluar' atau tekan Ctrl+D untuk keluar

>>>
```

---

## 📋 Basic Usage

### 1. Simple Expressions

```python
>>> 2 + 2
4

>>> 10 * 5
50

>>> "Hello" + " " + "World"
Hello World
```

### 2. Variables

```python
>>> nama itu "Budi"
>>> umur itu 25
>>> tampilkan f"Nama: {nama}, Umur: {umur}"
Nama: Budi, Umur: 25

>>> x itu 10
>>> y itu 20
>>> z itu x + y
>>> tampilkan z
30
```

### 3. Lists and Dicts

```python
>>> angka itu [1, 2, 3, 4, 5]
>>> tampilkan angka
[1, 2, 3, 4, 5]

>>> mahasiswa itu {"nama": "Budi", "umur": 25}
>>> tampilkan mahasiswa["nama"]
Budi
```

---

## 🎮 REPL Commands

### `bantuan` - Show Help

Menampilkan daftar perintah yang tersedia.

```python
>>> bantuan

📚 Perintah REPL:
  bantuan      - Tampilkan pesan bantuan ini
  keluar       - Keluar dari REPL
  bersih       - Bersihkan layar
  riwayat      - Tampilkan riwayat perintah
  reset        - Reset interpreter (hapus semua variabel)
  variabel     - Tampilkan semua variabel yang ada

💡 Tips:
  - Gunakan 'selesai' untuk mengakhiri blok multiline
  - Tekan Enter dua kali untuk mengeksekusi blok multiline
  - Gunakan f-string untuk string interpolation: f"Nilai: {x}"
```

### `keluar` - Exit REPL

Keluar dari REPL.

```python
>>> keluar
Keluar dari REPL...
```

**Alternatif:**
- Ketik `exit` atau `quit`
- Tekan `Ctrl+D` (Linux/Mac) atau `Ctrl+Z` (Windows)

### `bersih` - Clear Screen

Membersihkan layar terminal.

```python
>>> bersih
# Screen cleared, banner shown again
```

### `riwayat` - Show History

Menampilkan riwayat perintah yang telah dijalankan.

```python
>>> riwayat

📜 Riwayat Perintah:
  1. x itu 10
  2. y itu 20
  3. tampilkan x + y
  4. nama itu "Budi"
```

### `reset` - Reset Interpreter

Menghapus semua variabel dan mereset interpreter.

```python
>>> x itu 10
>>> y itu 20
>>> reset
✅ Interpreter direset (semua variabel dihapus)

>>> tampilkan x
❌ Error: 'x' tidak didefinisikan
```

### `variabel` - Show Variables

Menampilkan semua variabel yang telah didefinisikan.

```python
>>> x itu 10
>>> nama itu "Budi"
>>> angka itu [1, 2, 3]
>>> variabel

📦 Variabel yang Didefinisikan:
  x = 10
  nama = Budi
  angka = [1, 2, 3]
```

---

## 🔄 Multiline Input

REPL mendukung input multiline untuk fungsi, class, dan control flow.

### Functions

```python
>>> fungsi tambah(a, b):
...     hasil a + b
... selesai
>>> tampilkan tambah(5, 3)
8
```

### Classes

```python
>>> kelas Mahasiswa:
...     konstruktor(nama, nim):
...         diri.nama itu nama
...         diri.nim itu nim
...     selesai
...     
...     metode info():
...         tampilkan f"Nama: {diri.nama}, NIM: {diri.nim}"
...     selesai
... selesai
>>> mhs itu Mahasiswa("Budi", "12345")
>>> mhs.info()
Nama: Budi, NIM: 12345
```

### Control Flow

```python
>>> untuk x dari 1 sampai 5
...     tampilkan x * 2
... selesai
2
4
6
8
10
```

### If Statements

```python
>>> nilai itu 85
>>> jika nilai >= 80
...     tampilkan "A"
... kalau_tidak_jika nilai >= 70
...     tampilkan "B"
... kalau_tidak
...     tampilkan "C"
... selesai
A
```

---

## 💡 Advanced Usage

### 1. Testing Functions

```python
>>> fungsi faktorial(n):
...     jika n <= 1
...         hasil 1
...     selesai
...     hasil n * faktorial(n - 1)
... selesai

>>> tampilkan faktorial(5)
120

>>> tampilkan faktorial(10)
3628800
```

### 2. Working with Lists

```python
>>> angka itu [1, 2, 3, 4, 5]
>>> kuadrat itu [x * x untuk setiap x dari angka]
>>> tampilkan kuadrat
[1, 4, 9, 16, 25]

>>> genap itu [x untuk setiap x dari angka jika x % 2 == 0]
>>> tampilkan genap
[2, 4]
```

### 3. HTTP Requests

```python
>>> response itu http_get("https://jsonplaceholder.typicode.com/posts/1")
>>> tampilkan response.status_code
200

>>> data itu response.json()
>>> tampilkan data["title"]
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

### 4. File Operations

```python
>>> tulis_file("test.txt", "Hello, World!")
>>> content itu baca_file("test.txt")
>>> tampilkan content
Hello, World!
```

### 5. Lambda Functions

```python
>>> kuadrat itu lambda dengan x -> x * x
>>> tampilkan kuadrat(5)
25

>>> tambah itu lambda dengan a, b -> a + b
>>> tampilkan tambah(10, 20)
30
```

### 6. Data Processing

```python
>>> data itu [
...     {"nama": "Budi", "nilai": 85},
...     {"nama": "Ani", "nilai": 90},
...     {"nama": "Citra", "nilai": 88}
... ]

>>> rata itu rata_rata([d["nilai"] untuk setiap d dari data])
>>> tampilkan f"Rata-rata: {rata}"
Rata-rata: 87.66666666666667

>>> lulus itu [d untuk setiap d dari data jika d["nilai"] >= 85]
>>> tampilkan lulus
[{'nama': 'Budi', 'nilai': 85}, {'nama': 'Ani', 'nilai': 90}, {'nama': 'Citra', 'nilai': 88}]
```

---

## 🎯 Use Cases

### 1. Quick Calculations

```python
>>> // Calculate compound interest
>>> principal itu 1000000
>>> rate itu 0.05
>>> time itu 5
>>> amount itu principal * (1 + rate) ** time
>>> tampilkan f"Amount after {time} years: Rp {amount:,.2f}"
Amount after 5 years: Rp 1,276,281.56
```

### 2. String Manipulation

```python
>>> teks itu "  Hello World  "
>>> bersih itu hapus_spasi(teks)
>>> besar itu huruf_besar(bersih)
>>> tampilkan besar
HELLO WORLD

>>> kata itu pisah(besar, " ")
>>> tampilkan kata
['HELLO', 'WORLD']
```

### 3. Data Analysis

```python
>>> nilai itu [85, 90, 78, 92, 88, 95, 82]
>>> tampilkan f"Rata-rata: {rata_rata(nilai)}"
Rata-rata: 87.14285714285714

>>> tampilkan f"Median: {nilai_tengah(nilai)}"
Median: 88

>>> tampilkan f"Min: {min(nilai)}, Max: {max(nilai)}"
Min: 78, Max: 95
```

### 4. API Testing

```python
>>> // Test API endpoint
>>> response itu http_get("https://api.github.com/users/github")
>>> jika response.ok()
...     user itu response.json()
...     tampilkan f"Name: {user['name']}"
...     tampilkan f"Bio: {user['bio']}"
...     tampilkan f"Repos: {user['public_repos']}"
... selesai
Name: GitHub
Bio: How people build software.
Repos: 350
```

### 5. Learning OOP

```python
>>> kelas BankAccount:
...     konstruktor(nama, saldo):
...         diri.nama itu nama
...         diri.saldo itu saldo
...     selesai
...     
...     metode setor(jumlah):
...         diri.saldo += jumlah
...         tampilkan f"Setor: Rp {jumlah}"
...     selesai
...     
...     metode info():
...         tampilkan f"Nama: {diri.nama}, Saldo: Rp {diri.saldo}"
...     selesai
... selesai

>>> akun itu BankAccount("Budi", 1000000)
>>> akun.info()
Nama: Budi, Saldo: Rp 1000000

>>> akun.setor(500000)
Setor: Rp 500000

>>> akun.info()
Nama: Budi, Saldo: Rp 1500000
```

---

## ⚡ Tips & Tricks

### 1. Use Tab Completion (if available)

```python
>>> tam<TAB>
tampilkan
```

### 2. Multi-line Editing

```python
>>> fungsi long_function():
...     # Press Enter to continue
...     x itu 10
...     y itu 20
...     hasil x + y
... selesai
```

### 3. Quick Variable Inspection

```python
>>> data itu {"a": 1, "b": 2, "c": 3}
>>> variabel
📦 Variabel yang Didefinisikan:
  data = {'a': 1, 'b': 2, 'c': 3}
```

### 4. Error Recovery

```python
>>> x itu 10 / 0
❌ Error: division by zero

>>> # REPL continues, you can keep working
>>> x itu 10 / 2
>>> tampilkan x
5.0
```

### 5. Import and Test Libraries

```python
>>> impor_python "math"
>>> tampilkan panggil_python math.pi
3.141592653589793

>>> tampilkan panggil_python math.sqrt(16)
4.0
```

---

## 🐛 Troubleshooting

### Issue 1: Multiline Not Working

**Problem:** Multiline input tidak terdeteksi

**Solution:** Pastikan menggunakan keyword yang benar (`fungsi`, `kelas`, `jika`, dll.) dan akhiri dengan `selesai`

### Issue 2: Variable Not Found

**Problem:** Variable tidak ditemukan setelah didefinisikan

**Solution:** Gunakan perintah `variabel` untuk melihat semua variabel yang ada

### Issue 3: REPL Hangs

**Problem:** REPL tidak merespon

**Solution:** Tekan `Ctrl+C` untuk interrupt, atau `Ctrl+D` untuk exit

### Issue 4: Clear History

**Problem:** Ingin menghapus history

**Solution:** Gunakan perintah `reset` untuk mereset interpreter dan menghapus semua variabel

---

## 📚 See Also

- [Quick Reference](quick-reference.md) - Quick syntax reference
- [Syntax Basics](syntax-basics.md) - Basic syntax guide
- [Built-in Functions](builtin-functions.md) - All built-in functions
- [Examples](examples.md) - Code examples

---

## 🎓 Learning Path

### Beginner
1. Start REPL: `rmc`
2. Try simple expressions: `2 + 2`
3. Create variables: `x itu 10`
4. Use built-in functions: `tampilkan(x)`

### Intermediate
1. Define functions
2. Work with lists and dicts
3. Use comprehensions
4. Try HTTP requests

### Advanced
1. Create classes
2. Use async/await
3. Integrate Python libraries
4. Build complex applications

---

**Version: 0.0.4**  
**Last Updated: 2025-10-04**

**REPL is a powerful tool for learning and testing RenzMcLang. Happy coding! 🚀**