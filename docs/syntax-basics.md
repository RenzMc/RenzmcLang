# Dasar-dasar Sintaks

## 🎯 Pengenalan

RenzMcLang adalah bahasa pemrograman dengan sintaks Bahasa Indonesia yang dikompilasi ke Python. Panduan ini mencakup sintaks dan fitur dasar.

## 📝 Komentar

Komentar adalah baris yang diabaikan oleh interpreter:

```python
// Ini adalah komentar satu baris

tampilkan "Hello"  // Komentar setelah kode
```

## 🔢 Variabel dan Tipe Data

### Deklarasi Variabel

Variabel dideklarasikan menggunakan kata kunci `itu`:

```python
nama itu "Budi"
umur itu 25
tinggi itu 175.5
aktif itu benar
```

### Tipe Data

```python
// Angka (integer dan float)
angka_bulat itu 42
angka_desimal itu 3.14

// String
teks itu "Hello, World!"
teks2 itu 'Single quotes juga bisa'

// Boolean
benar_value itu benar  // true
salah_value itu salah  // false

// List
daftar itu [1, 2, 3, 4, 5]
nama_list itu ["Ali", "Budi", "Citra"]

// Dictionary
data itu {
    "nama": "Budi",
    "umur": 25,
    "kota": "Jakarta"
}
```

### Format String (F-Strings)

```python
nama itu "Budi"
umur itu 25

tampilkan f"Nama saya {nama} dan umur saya {umur} tahun"
// Output: Nama saya Budi dan umur saya 25 tahun

// Dengan ekspresi
tampilkan f"Tahun depan saya akan berumur {umur + 1} tahun"
```

## 📤 Output

### Pernyataan Print

Beberapa kata kunci untuk mencetak:

```python
tampilkan "Hello"  // display
cetak "Hello"     // print
tulis "Hello"     // write
tunjukkan "Hello" // show
```

## ➕ Operator

### Operator Aritmatika

```python
a itu 10
b itu 3

tambah itu a + b      // 13
kurang itu a - b      // 7
kali itu a * b        // 30
bagi itu a / b        // 3.333...
sisa itu a % b        // 1 (modulo)
pangkat itu a ** b     // 1000 (power)
bagi_bulat itu a // b  // 3 (floor division)
```

### Operator Perbandingan

```python
a itu 10
b itu 5

a == b  // Sama dengan (salah)
a != b  // Tidak sama dengan (benar)
a > b   // Lebih besar dari (benar)
a < b   // Lebih kecil dari (salah)
a >= b  // Lebih besar atau sama dengan (benar)
a <= b  // Lebih kecil atau sama dengan (salah)
```

### Operator Logika

```python
a itu benar
b itu salah

a dan b   // AND (salah)
a atau b  // OR (benar)
tidak a   // NOT (salah)
```

### Operator Penugasan Gabungan

```python
x itu 10

x += 5   // x = x + 5 (15)
x -= 3   // x = x - 3 (12)
x *= 2   // x = x * 2 (24)
x /= 4   // x = x / 4 (6.0)
```

### Operator Bitwise

```python
a itu 5   // 0101 dalam biner
b itu 3   // 0011 dalam biner

a & b    // Bitwise AND (1)
a | b    // Bitwise OR (7)
a ^ b    // Bitwise XOR (6)
~a       // Bitwise NOT (-6)
a << 1   // Left shift (10)
a >> 1  // Right shift (2)
```

## 🔀 Alur Kontrol

### Pernyataan If-Else

```python
angka itu 10

jika angka > 0
    tampilkan "Positif"
kalau tidak jika angka < 0
    tampilkan "Negatif"
kalau tidak
    tampilkan "Nol"
selesai
```

Alternatif kata kunci `kalau`:

```python
kalau angka % 2 == 0
    tampilkan "Genap"
kalau tidak
    tampilkan "Ganjil"
selesai
```

### Operator Ternary

```python
umur itu 20
status itu "Dewasa" jika umur >= 18 kalau tidak "Anak-anak"
tampilkan status  // Output: Dewasa
```

### Switch-Case (Match)

```python
hari itu 3

cocok hari
    kasus 1:
        tampilkan "Senin"
    kasus 2:
        tampilkan "Selasa"
    kasus 3:
        tampilkan "Rabu"
    bawaan:
        tampilkan "Hari lain"
selesai
```

## 🔁 Perulangan

### Perulangan For (Range)

```python
// Loop dari 1 sampai 10
untuk i dari 1 sampai 10
    tampilkan i
selesai
```

### Perulangan For Each

```python
buah itu ["Apel", "Jeruk", "Mangga"]

untuk setiap item dari buah
    tampilkan item
selesai
```

### Perulangan While

```python
counter itu 0

selama counter < 5
    tampilkan counter
    counter += 1
selesai
```

### Kontrol Perulangan

```python
untuk i dari 1 sampai 10
    jika i == 3
        lanjut  // Lompat ke iterasi berikutnya (continue)
    selesai
    
    jika i == 8
        berhenti  // Keluar dari loop (break)
    selesai
    
    tampilkan i
selesai
```

## 📦 Fungsi

### Definisi Fungsi

```python
fungsi sapa(nama):
    tampilkan f"Halo, {nama}!"
selesai

// Memanggil fungsi
sapa("Budi")
```

### Fungsi dengan Nilai Kembali

```python
fungsi tambah(a, b):
    kembali a + b
selesai

hasil itu tambah(5, 3)
tampilkan hasil  // Output: 8
```

### Fungsi dengan Parameter Default

```python
fungsi sapa_dengan_gelar(nama, gelar="Bapak"):
    tampilkan f"{gelar} {nama}"
selesai

sapa_dengan_gelar("Budi")              // Output: Bapak Budi
sapa_dengan_gelar("Ani", "Ibu")      // Output: Ibu Ani
```

### Fungsi Lambda

```python
kuadrat itu lambda x: x * x
tampilkan kuadrat(5)  // Output: 25

// Lambda dengan beberapa parameter
tambah itu lambda x, y: x + y
tampilkan tambah(3, 4)  // Output: 7
```

## 🎨 Operasi List dan Dictionary

### Operasi List

```python
angka itu [1, 2, 3]

// Akses elemen
tampilkan angka[0]  // Output: 1

// Slicing
tampilkan angka[0:2]  // Output: [1, 2]

// Modifikasi
angka[0] itu 10
tampilkan angka  // Output: [10, 2, 3]
```

### Operasi Dictionary

```python
mahasiswa itu {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

// Akses nilai
tampilkan mahasiswa["nama"]  // Output: Budi

// Tambah/modifikasi
mahasiswa["ipk"] itu 3.8
```

### List Comprehension

```python
// Membuat list kuadrat
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
tampilkan kuadrat  // Output: [1, 4, 9, 16, 25]

// Dengan kondisi
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
tampilkan genap  // Output: [2, 4, 6]
```

## 🛡️ Penanganan Error

```python
coba
    angka itu 10 / 0
tangkap ZeroDivisionError sebagai e:
    tampilkan "Error: Tidak bisa membagi dengan nol!"
akhirnya
    tampilkan "Selesai"
selesai
```

## 📚 Langkah Selanjutnya

- Pelajari tentang [Fungsi Bawaan](builtin-functions.md)
- Jelajahi [Fitur Lanjutan](advanced-features.md)
- Lihat [Integrasi Python](python-integration.md)
- Lihat [Contoh](examples.md) untuk kode praktis

---

**Selamat Coding dengan RenzMcLang! 🚀**