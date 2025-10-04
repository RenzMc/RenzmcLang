# Fitur Lanjutan

## 🚀 Pengenalan

RenzMcLang mendukung fitur pemrograman lanjutan termasuk Pemrograman Berorientasi Objek (OOP), pemrograman asinkron, dekorator, dan lainnya. Panduan ini mencakup semua fitur lanjutan dengan contoh yang berfungsi.

## 📑 Daftar Isi

- [Pemrograman Berorientasi Objek (OOP)](#pemrograman-berorientasi-objek-oop)
- [Fungsi Lambda](#fungsi-lambda)
- [List & Dictionary Comprehensions](#list--dictionary-comprehensions)
- [Async/Await](#asyncawait)
- [Dekorator](#dekorator)
- [Penanganan Error](#penanganan-error)
- [Context Managers (Pernyataan With)](#context-managers-pernyataan-with)
- [Generator](#generator)
- [Operator Lanjutan](#operator-lanjutan)

---

## Pemrograman Berorientasi Objek (OOP)

### Struktur Kelas Dasar

RenzMcLang menggunakan pendekatan berbasis fungsi untuk OOP:

```python
// Fungsi konstruktor
buat fungsi buat_orang dengan nama, umur
    orang itu {
        "nama": nama,
        "umur": umur
    }
    hasil orang
selesai

// Fungsi metode
buat fungsi perkenalan dengan orang
    hasil f"Halo, nama saya {orang['nama']}, umur {orang['umur']} tahun"
selesai

// Buat objek
orang1 itu panggil buat_orang dengan "Alice", 25

// Panggil metode
pesan itu panggil perkenalan dengan orang1
tampilkan pesan
```

### Kelas dengan Properti

```python
// Kelas Bank Account
buat fungsi buat_bank_account dengan pemilik, saldo_awal
    account itu {
        "pemilik": pemilik,
        "saldo": saldo_awal,
        "transaksi": []
    }
    hasil account
selesai

// Metode deposit
buat fungsi deposit dengan account, jumlah
    account["saldo"] itu account["saldo"] + jumlah
    tambah(account["transaksi"], f"Deposit: +Rp {jumlah}")
    tampilkan f"✓ Deposit Rp {jumlah} berhasil"
selesai

// Metode withdraw
buat fungsi withdraw dengan account, jumlah
    jika jumlah > account["saldo"]
        tampilkan "✗ Saldo tidak cukup"
        hasil salah
    selesai
    
    account["saldo"] itu account["saldo"] - jumlah
    tambah(account["transaksi"], f"Withdraw: -Rp {jumlah}")
    tampilkan f"✓ Withdraw Rp {jumlah} berhasil"
    hasil benar
selesai

// Penggunaan
akun itu panggil buat_bank_account dengan "Budi", 1000000
panggil deposit dengan akun, 500000
panggil withdraw dengan akun, 200000
```

### Pola Pewarisan

```python
// Kelas dasar: Animal
buat fungsi buat_animal dengan nama, jenis
    animal itu {
        "nama": nama,
        "jenis": jenis
    }
    hasil animal
selesai

// Kelas turunan: Dog (memperluas Animal)
buat fungsi buat_dog dengan nama, ras
    // Panggil konstruktor induk
    dog itu panggil buat_animal dengan nama, "Anjing"
    // Tambahkan properti khusus
    dog["ras"] itu ras
    hasil dog
selesai

// Metode untuk Dog
buat fungsi gonggong dengan dog
    tampilkan f"{dog['nama']} berkata: Woof! Woof!"
selesai

// Penggunaan
anjing itu panggil buat_dog dengan "Buddy", "Golden Retriever"
panggil gonggong dengan anjing
```

---

## Fungsi Lambda

Fungsi lambda adalah fungsi anonim untuk operasi cepat:

```python
// Lambda sederhana
kuadrat itu lambda x: x * x
tampilkan kuadrat(5)  // Output: 25

// Lambda dengan beberapa parameter
tambah itu lambda x, y: x + y
tampilkan tambah(3, 4)  // Output: 7

// Lambda dengan kondisi
is_genap itu lambda x: x % 2 == 0
tampilkan is_genap(4)  // Output: benar

// Menggunakan lambda dengan map
angka itu [1, 2, 3, 4, 5]
kuadrat_list itu map(lambda x: x * x, angka)
tampilkan kuadrat_list  // Output: [1, 4, 9, 16, 25]
```

---

## List & Dictionary Comprehensions

### List Comprehension

```python
// List comprehension dasar
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
// Output: [1, 4, 9, 16, 25]

// Dengan kondisi
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
// Output: [2, 4, 6]

// Comprehension bersarang
matrix itu [[i * j untuk j dari [1, 2, 3]] untuk i dari [1, 2, 3]]
// Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Dictionary Comprehension

```python
// Dict comprehension dasar
kuadrat_dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5]}
// Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

// Dengan kondisi
genap_dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0}
// Output: {2: 4, 4: 16, 6: 36}
```

---

## Async/Await

Pemrograman asinkron untuk operasi konkuren:

```python
// Impor pustaka async
impor_python "asyncio"

// Fungsi async
async fungsi fetch_data(url):
    tampilkan f"Mengambil {url}..."
    await panggil_python asyncio.sleep(1)
    hasil f"Data dari {url}"
selesai

// Fungsi async utama
async fungsi main():
    data1 itu await fetch_data("https://api1.com")
    data2 itu await fetch_data("https://api2.com")
    tampilkan data1
    tampilkan data2
selesai

// Jalankan fungsi async
panggil_python asyncio.run(main())
```

---

## Dekorator

Dekorator memodifikasi perilaku fungsi:

```python
// Dekorator timer
buat fungsi timer_decorator dengan func
    buat fungsi wrapper(*args):
        start itu waktu()
        result itu panggil func dengan *args
        end itu waktu()
        tampilkan f"Waktu eksekusi: {end - start} detik"
        hasil result
    selesai
    hasil wrapper
selesai

// Terapkan dekorator
@timer_decorator
fungsi slow_function():
    tidur(2)
    tampilkan "Fungsi selesai"
selesai
```

---

## Penanganan Error

Penanganan error komprehensif dengan try-catch-finally:

```python
// Try-catch dasar
coba
    hasil itu 10 / 0
tangkap ZeroDivisionError sebagai e:
    tampilkan "Error: Tidak bisa membagi dengan nol!"
selesai

// Try-catch-finally
coba
    file itu baca_file("data.txt")
    tampilkan file
tangkap FileNotFoundError:
    tampilkan "File tidak ditemukan"
tangkap Exception sebagai e:
    tampilkan f"Error: {e}"
akhirnya
    tampilkan "Pembersihan selesai"
selesai
```

---

## Context Managers (Pernyataan With)

Manajemen sumber daya otomatis:

```python
// Penanganan file dengan context manager
dengan buka("data.txt", "r") sebagai f:
    content itu f.read()
    tampilkan content
selesai
// File otomatis ditutup

// Multiple context managers
dengan buka("input.txt", "r") sebagai f_in, buka("output.txt", "w") sebagai f_out:
    data itu f_in.read()
    f_out.write(data)
selesai
```

---

## Generator

Iterasi yang efisien memori:

```python
// Fungsi generator
fungsi countdown(n):
    selama n > 0
        yield n
        n -= 1
    selesai
selesai

// Gunakan generator
untuk setiap num dari countdown(5)
    tampilkan num
selesai
```

---

## Operator Lanjutan

### Operator Walrus (:=)

```python
// Ekspresi penugasan
jika (n := panjang(data)) > 10
    tampilkan f"Data memiliki {n} item"
selesai
```

### Operator Bitwise

```python
a itu 5   // 0101 dalam biner
b itu 3   // 0011 dalam biner

tampilkan a & b    // AND: 1 (0001)
tampilkan a | b    // OR: 7 (0111)
tampilkan a ^ b    // XOR: 6 (0110)
tampilkan ~a       // NOT: -6
tampilkan a << 1   // Geser kiri: 10 (1010)
tampilkan a >> 1  // Geser kanan: 2 (0010)
```

---

## Ringkasan

RenzMcLang mendukung semua fitur pemrograman modern:

- ✅ Pemrograman Berorientasi Objek (berbasis fungsi)
- ✅ Fungsi lambda dan pemrograman fungsional
- ✅ List dan dictionary comprehensions
- ✅ Async/await untuk pemrograman konkuren
- ✅ Dekorator untuk modifikasi fungsi
- ✅ Penanganan error komprehensif
- ✅ Context manager untuk manajemen sumber daya
- ✅ Generator untuk efisiensi memori
- ✅ Operator lanjutan (walrus, bitwise)

Untuk contoh lebih lanjut, lihat direktori [examples](../examples/).

---

**Selamat Coding Lanjutan dengan RenzMcLang! 🚀**