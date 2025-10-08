# 📖 Dasar-dasar Sintaks - RenzMcLang versi terbaru

**Terakhir Diperbarui:** 2025-10-08  
[![Versi PyPI](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Ikhtisar

RenzMcLang menggunakan sintaks Bahasa Indonesia yang intuitif dan mudah dipahami. Panduan ini mencakup semua dasar sintaks yang perlu Anda ketahui.

---

## 📋 Daftar Isi

1. [Komentar](#komentar)
2. [Variabel](#variabel)
3. [Tipe Data](#tipe-data)
4. [Operator](#operator)
5. [Alur Kontrol](#alur-kontrol)
6. [Perulangan](#perulangan)
7. [Fungsi](#fungsi)
8. [Input/Output](#inputoutput)
9. [Dukungan Multi-baris](#dukungan-multi-baris)

---

## Komentar

### Komentar Satu Baris
```python
// Ini adalah komentar satu baris
tampilkan "Hello"  // Komentar di akhir baris
```

### Komentar Multi-baris
```python
/*
Ini adalah komentar
multi-baris
*/
```

---

## Variabel

### Deklarasi Variabel

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

### Aturan Penamaan Variabel

✅ **Valid:**
```python
nama itu "Budi"
nama_lengkap itu "Budi Santoso"
umur_2024 itu 25
_private itu "secret"
```

❌ **Tidak Valid:**
```python
2nama itu "Budi"      // Tidak boleh dimulai dengan angka
nama-lengkap itu "X"  // Tidak boleh menggunakan dash
jika itu "test"       // Tidak boleh menggunakan keyword
```

### Penugasan Variabel

```python
// Penugasan sederhana
x itu 10

// Penugasan ganda
a itu b itu c itu 0

// Tukar nilai
x itu 5
y itu 10
temp itu x
x itu y
y itu temp
```

---

## Tipe Data

### 1. Angka

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

### 2. String (Teks)

#### Deklarasi String
```python
// Tanda kutip tunggal
nama itu 'Budi'

// Tanda kutip ganda
pesan itu "Hello, World!"

// String multi-baris
alamat itu """
Jalan Merdeka No. 123
Jakarta Pusat
Indonesia
"""
```

#### Operasi String
```python
// Penggabungan
nama_depan itu "Budi"
nama_belakang itu "Santoso"
nama_lengkap itu nama_depan + " " + nama_belakang

// Pengulangan string
garis itu "=" * 50

// Pengindeksan string
teks itu "Hello"
huruf_pertama itu teks[0]  // "H"
huruf_terakhir itu teks[-1]  // "o"

// Pemotongan string
kata itu "Programming"
bagian itu kata[0:4]  // "Prog"
```

#### F-String (Interpolasi String)
```python
nama itu "Budi"
umur itu 25

// F-string
pesan itu f"Nama saya {nama}, umur {umur} tahun"
tampilkan pesan  // Output: Nama saya Budi, umur 25 tahun

// Dengan ekspresi
harga itu 100000
pajak itu 0.1
total itu f"Total: Rp {harga * (1 + pajak)}"
```

### 3. Boolean

```python
// Nilai boolean
benar_value itu benar
salah_value itu salah

// Boolean dari perbandingan
is_adult itu umur >= 18
is_student itu benar
has_license itu salah
```

### 4. List (Daftar)

```python
// List kosong
daftar_kosong itu []

// List dengan nilai
angka itu [1, 2, 3, 4, 5]
nama itu ["Budi", "Ani", "Citra"]
campuran itu [1, "dua", 3.0, benar]

// Operasi list
angka.tambah(6)           // Tambah elemen
angka.hapus(3)            // Hapus elemen
panjang itu panjang(angka)  // Dapatkan panjang
pertama itu angka[0]      // Akses elemen
terakhir itu angka[-1]    // Elemen terakhir
```

### 5. Dictionary (Kamus)

```python
// Kamus kosong
kamus_kosong itu {}

// Kamus dengan nilai
mahasiswa itu {
    "nama": "Budi",
    "umur": 25,
    "jurusan": "Informatika"
}

// Akses nilai
nama itu mahasiswa["nama"]
umur itu mahasiswa["umur"]

// Tambah/perbarui nilai
mahasiswa["email"] itu "budi@example.com"
mahasiswa["umur"] itu 26

// Periksa keberadaan kunci
jika "nama" dalam mahasiswa
    tampilkan "Nama ada"
selesai
```

### 6. Set (Himpunan)

```python
// Set kosong
himpunan_kosong itu set()

// Set dengan nilai
angka itu {1, 2, 3, 4, 5}
huruf itu {"a", "b", "c"}

// Operasi set
angka.tambah(6)           // Tambah elemen
angka.hapus(3)            // Hapus elemen
panjang itu panjang(angka)  // Dapatkan panjang
```

### 7. Tuple

```python
// Deklarasi tuple
koordinat itu (10, 20)
rgb itu (255, 128, 0)

// Pembongkaran tuple
x, y itu koordinat
r, g, b itu rgb

// Akses elemen
pertama itu koordinat[0]
kedua itu koordinat[1]
```

---

## Operator

### 1. Operator Aritmatika

```python
// Penjumlahan
hasil itu 10 + 5  // 15

// Pengurangan
hasil itu 10 - 5  // 5

// Perkalian
hasil itu 10 * 5  // 50

// Pembagian
hasil itu 10 / 5  // 2.0

// Pembagian Lantai
hasil itu 10 // 3  // 3

// Modulus
hasil itu 10 % 3  // 1

// Perpangkatan
hasil itu 2 ** 3  // 8
```

### 2. Operator Perbandingan

```python
// Sama dengan
hasil itu 5 == 5  // benar

// Tidak sama dengan
hasil itu 5 != 3  // benar

// Lebih besar dari
hasil itu 5 > 3  // benar

// Kurang dari
hasil itu 5 < 3  // salah

// Lebih besar dari atau sama dengan
hasil itu 5 >= 5  // benar

// Kurang dari atau sama dengan
hasil itu 5 <= 3  // salah
```

### 3. Operator Logika

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

### 4. Operator Penugasan

```python
// Penugasan sederhana
x itu 10

// Penugasan gabungan
x += 5   // x = x + 5
x -= 3   // x = x - 3
x *= 2   // x = x * 2
x /= 4   // x = x / 4
x %= 3   // x = x % 3
x **= 2  // x = x ** 2
```

### 5. Operator Keanggotaan

```python
// in
hasil itu "a" dalam ["a", "b", "c"]  // benar
hasil itu 5 dalam [1, 2, 3]          // salah

// not in
hasil itu "d" tidak dalam ["a", "b", "c"]  // benar
```

### 6. Operator Bitwise

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

## Alur Kontrol

### 1. Pernyataan If

```python
// If sederhana
jika umur >= 18
    tampilkan "Dewasa"
selesai

// If-else
jika nilai >= 60
    tampilkan "Lulus"
lainnya
    tampilkan "Tidak Lulus"
selesai

// If-elif-else
jika nilai >= 90
    tampilkan "A"
lainnya jika nilai >= 80
    tampilkan "B"
lainnya jika nilai >= 70
    tampilkan "C"
lainnya
    tampilkan "D"
selesai
```

### 2. Operator Ternary

```python
// If-else inline
status itu "Lulus" jika nilai >= 60 kalau tidak "Tidak Lulus"

// Dengan ekspresi
max_value itu a jika a > b kalau tidak b
```

### 3. Pernyataan Switch/Case

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

## Perulangan

### 1. Perulangan For

#### Perulangan For Berbasis Rentang
```python
// Perulangan dari 1 sampai 10
untuk x dari 1 sampai 10
    tampilkan x
selesai

// Perulangan dengan langkah
untuk x dari 0 sampai 20 dengan langkah 2
    tampilkan x
selesai
```

#### Perulangan For Each
```python
// Iterasi melalui list
buah itu ["apel", "jeruk", "mangga"]
untuk setiap item dari buah
    tampilkan item
selesai

// Iterasi melalui dictionary
mahasiswa itu {"nama": "Budi", "umur": 25}
untuk setiap key dari mahasiswa
    tampilkan f"{key}: {mahasiswa[key]}"
selesai
```

### 2. Perulangan While

```python
// Perulangan while sederhana
counter itu 0
selama counter < 5
    tampilkan counter
    counter += 1
selesai

// While dengan kondisi
input_valid itu salah
selama tidak input_valid
    nilai itu input("Masukkan angka: ")
    jika nilai.isdigit()
        input_valid itu benar
    selesai
selesai
```

### 3. Kontrol Perulangan

#### Break
```python
// Keluar dari perulangan lebih awal
untuk x dari 1 sampai 10
    jika x == 5
        berhenti
    selesai
    tampilkan x
selesai
```

#### Continue
```python
// Lewati iterasi
untuk x dari 1 sampai 10
    jika x % 2 == 0
        lanjut
    selesai
    tampilkan x  // Hanya angka ganjil
selesai
```

---

## Fungsi

### 1. Deklarasi Fungsi

```python
// Fungsi sederhana
fungsi sapa():
    tampilkan "Hello!"
selesai

// Panggil fungsi
sapa()
```

### 2. Fungsi dengan Parameter

```python
// Fungsi dengan parameter
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

// Panggil dengan argumen
sapa("Budi")
```

### 3. Fungsi dengan Nilai Pengembalian

```python
// Fungsi dengan pengembalian
fungsi tambah(a, b):
    hasil a + b
selesai

// Gunakan nilai pengembalian
total itu tambah(5, 3)
tampilkan total  // 8
```

### 4. Fungsi dengan Parameter Default

```python
// Parameter default
fungsi sapa(nama, sapaan="Halo"):
    tampilkan f"{sapaan}, {nama}!"
selesai

// Panggil dengan default
sapa("Budi")  // Output: Halo, Budi!

// Panggil dengan kustom
sapa("Budi", "Selamat pagi")  // Output: Selamat pagi, Budi!
```

### 5. Fungsi Lambda

```python
// Fungsi lambda
kuadrat itu lambda dengan x -> x * x

// Gunakan lambda
hasil itu kuadrat(5)  // 25

// Lambda dengan beberapa parameter
tambah itu lambda dengan a, b -> a + b
total itu tambah(3, 4)  // 7
```

---

## Input/Output

### 1. Output (Tampilkan)

```python
// Tampilkan sederhana
tampilkan "Hello, World!"

// Tampilkan beberapa nilai
tampilkan "Nama:", nama, "Umur:", umur

// Tampilkan dengan f-string
tampilkan f"Nama: {nama}, Umur: {umur}"

// Tampilkan multi-baris dengan tanda kurung
tampilkan(
    "Ini adalah",
    "pernyataan tampilkan",
    "multi-baris"
)
```

### 2. Input

```python
// Dapatkan input pengguna
nama itu input("Masukkan nama: ")

// Konversi ke angka
umur itu ke_angka(input("Masukkan umur: "))

// Konversi ke integer
nilai itu ke_bulat(input("Masukkan nilai: "))
```

### 3. File I/O

```python
// Tulis ke file
dengan buka("data.txt", "w") sebagai f
    f.tulis("Hello, World!")
selesai

// Baca dari file
dengan buka("data.txt", "r") sebagai f
    content itu f.baca()
    tampilkan content
selesai

// Tambahkan ke file
dengan buka("data.txt", "a") sebagai f
    f.tulis("\nBaris baru")
selesai
```

---

## Dukungan Multi-baris

RenzMcLang mendukung sintaks multi-baris untuk keterbacaan kode yang lebih baik, terutama ketika berurusan dengan pemanggilan fungsi yang panjang atau struktur data yang kompleks.

### 1. Pemanggilan Fungsi Multi-baris

```python
// Pemanggilan fungsi dapat mencakup beberapa baris
text itu "hello world"
hasil itu text.replace(
    "world",
    "python"
)

// Integrasi Python dengan multi-baris
impor_python "builtins"
hasil2 itu panggil_python builtins.str(
    "hello world"
)
```

### 2. Pernyataan Tampilkan Multi-baris

```python
// Tampilkan dengan tanda kurung untuk multi-baris
tampilkan(
    "Baris 1",
    "Baris 2",
    "Baris 3"
)
```

### 3. Struktur Data Multi-baris

```python
// List multi-baris
items itu [
    "item1",
    "item2",
    "item3",
    "item4"
]

// Dictionary multi-baris
person itu {
    "name": "John",
    "age": 30,
    "city": "Jakarta",
    "email": "john@example.com"
}

// Set multi-baris
numbers itu {
    1,
    2,
    3,
    4,
    5
}
```

### 4. Variasi Klausa Else

```python
// Kedua sintaks didukung
jika nilai >= 60
    tampilkan "Lulus"
lainnya  // Menggunakan garis bawah
    tampilkan "Tidak Lulus"
selesai

// Atau menggunakan dua kata
jika nilai >= 60
    tampilkan "Lulus"
kalau tidak  // Menggunakan spasi
    tampilkan "Tidak Lulus"
selesai
```

### 5. Praktik Terbaik untuk Multi-baris

```python
// ✅ Baik - Jelas dan mudah dibaca
hasil itu text.format(
    title="Document",
    content="Content here",
    author="John Doe"
)

// ✅ Baik - Indentasi konsisten
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

// ❌ Buruk - Pemformatan tidak konsisten
hasil itu text.format(title="Document",
content="Content",author="John")
```

---

## 💡 Praktik Terbaik

### 1. Konvensi Penamaan

```python
// ✅ Baik
nama_lengkap itu "Budi Santoso"
total_harga itu 100000
is_valid itu benar

// ❌ Buruk
n itu "Budi"
x itu 100000
flag itu benar
```

### 2. Organisasi Kode

```python
// ✅ Baik - Jelas dan terorganisir
fungsi hitung_total(harga, pajak):
    subtotal itu harga
    pajak_amount itu harga * pajak
    total itu subtotal + pajak_amount
    hasil total
selesai

// ❌ Buruk - Tidak jelas
fungsi h(x, y):
    hasil x + x * y
selesai
```

### 3. Komentar

```python
// ✅ Baik - Komentar yang membantu
// Hitung total harga dengan pajak 10%
total itu harga * 1.1

// ❌ Buruk - Komentar yang jelas
// Tambah 1 ke x
x itu x + 1
```

---

## 📚 Langkah Selanjutnya

Setelah mempelajari dasar-dasar:

1. **Fitur Lanjutan:** Pelajari [Fitur Lanjutan](advanced-features.md)
2. **Fungsi Bawaan:** Jelajahi [Fungsi Bawaan](builtin-functions.md)
3. **Contoh:** Coba [Contoh](examples.md)
4. **Integrasi Python:** Lihat [Integrasi Python](python-integration.md)

---

**Selamat Coding! 🚀**