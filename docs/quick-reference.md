# Quick Reference - RenzMcLang

Referensi cepat untuk sintaks dan fitur utama RenzMcLang.

## Variabel & Tipe Data

```python
// Variabel
nama itu "Budi"
umur itu 25
tinggi itu 175.5
is_student itu benar

// List
angka itu [1, 2, 3, 4, 5]

// Dictionary
mahasiswa itu {
    "nama": "Budi",
    "umur": 25,
    "nim": "12345"
}

// Set
unique itu {1, 2, 3, 4, 5}

// Tuple
koordinat itu (10, 20)
```

## Operator Aritmatika

```python
// Aritmatika
10 + 5    // Penjumlahan
10 - 5    // Pengurangan
10 * 5    // Perkalian
10 / 5    // Pembagian
10 // 3   // Pembagian lantai
10 % 3    // Modulus
2 ** 3    // Perpangkatan
```

## Alur Kontrol

```python
// If-else
jika umur >= 18
    tampilkan "Dewasa"
lainnya
    tampilkan "Anak-anak"
selesai

// For loop
untuk x dari 1 sampai 5
    tampilkan x
selesai

// While loop
counter itu 0
selama counter < 3
    tampilkan counter
    counter itu counter + 1
selesai
```

## Fungsi

```python
// Fungsi dasar
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

// Fungsi dengan pengembalian
fungsi jumlahkan(a, b):
    hasil a + b
selesai

// Panggil fungsi
sapa("Budi")
hasil itu jumlahkan(5, 3)
tampilkan hasil
```

## Operasi String

```python
// Dasar
teks itu "Hello World"
panjang(teks)              // Panjang
huruf_besar(teks)          // Huruf besar
huruf_kecil(teks)          // Huruf kecil

// Manipulasi
potong(teks, 0, 5)         // Potong
ganti(teks, "old", "new")  // Ganti
pisah(teks, ",")           // Pisah
```

## Operasi List

```python
// Dasar
list itu [1, 2, 3, 4, 5]
panjang(list)              // Panjang
tambah(list, 6)            // Tambah
hapus(list, 3)             // Hapus

// Pengurutan
urutkan(list)              // Urutkan di tempat

// Agregasi
min(list)                  // Minimum
max(list)                  // Maksimum
rata_rata(list)            // Rata-rata
```

## Import System

```python
// Import dari modul
dari math impor sqrt, pi
dari string_utils impor format_text sebagai fmt

// Import seluruh modul
impor helpers sebagai h

// WILDCARD IMPORT
dari utils impor *
```

## Operasi File

```python
// Baca
content itu baca_file("data.txt")

// Tulis
tulis_file("output.txt", "Hello")

// Periksa
ada_file("data.txt")
```

## Operasi JSON

```python
// Parse
data itu json_parse('{"nama": "Budi"}')

// Stringify
json_str itu json_stringify(data)

// File I/O
data itu json_baca("data.json")
json_tulis("output.json", data)
```

## Konversi Tipe

```python
// Ke string
ke_teks(value)

// Ke angka
ke_angka(value)

// Ke integer
ke_bulat(value)

// Ke boolean
ke_boolean(value)
```

## Fungsi Built-in

```python
// Matematika
absolut(x)
bulat(x, digits)
pangkat(base, exp)
akar(x)

// Statistik
rata_rata(list)
nilai_tengah(list)
modus(list)

// Acak
acak()
acak_bulat(min, max)
pilih_acak(list)
```

## Penanganan Kesalahan

```python
// Try-catch
coba
    // kode yang mungkin gagal
tangkap Exception sebagai e
    tampilkan f"Error: {e}"
selesai
```

## Kata Kunci Utama

```
jika, maka, tidak, lainnya, selesai
untuk, setiap, dari, sampai
selama
fungsi, hasil
kelas, metode, konstruktor
impor, dari
tampilkan
coba, tangkap
benar, salah
dan, atau
```

---

**Version**: Latest  
**Updated**: 2025-12-14