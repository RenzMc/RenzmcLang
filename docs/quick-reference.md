# ⚡ Referensi Cepat - RenzMcLang versi terbaru

**Terakhir Diperbarui:** 2025-10-08  
[![Versi PyPI](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Lembar Contekan

### Variabel & Tipe Data

```python
// Variabel
nama itu "Budi"
umur itu 25
tinggi itu 175.5
is_student itu benar

// List
angka itu [1, 2, 3, 4, 5]
nama itu ["Budi", "Ani", "Citra"]

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

---

### Operator

```python
// Aritmatika
10 + 5    // Penjumlahan
10 - 5    // Pengurangan
10 * 5    // Perkalian
10 / 5    // Pembagian
10 // 3   // Pembagian lantai
10 % 3    // Modulus
2 ** 3    // Perpangkatan

// Perbandingan
5 == 5    // Sama dengan
5 != 3    // Tidak sama dengan
5 > 3     // Lebih besar dari
5 < 3     // Kurang dari
5 >= 5    // Lebih besar atau sama dengan
5 <= 3    // Kurang dari atau sama dengan

// Logika
benar dan benar    // AND
benar atau salah   // OR
tidak benar        // NOT

// Keanggotaan
"a" dalam ["a", "b"]      // in
"d" tidak dalam ["a", "b"] // not in

// Bitwise
5 & 3     // AND
5 | 3     // OR
5 ^ 3     // XOR
~5        // NOT
5 << 1    // Geser kiri
5 >> 1    // Geser kanan
```

---

### Alur Kontrol

```python
// If-else (kedua sintaks didukung)
jika kondisi
    // kode
lainnya jika kondisi2  // Menggunakan garis bawah
    // kode
lainnya  // Menggunakan garis bawah
    // kode
selesai

// Atau menggunakan spasi
jika kondisi
    // kode
kalau tidak jika kondisi2  // Menggunakan spasi
    // kode
kalau tidak  // Menggunakan spasi
    // kode
selesai

// Ternary
hasil itu "A" jika nilai >= 90 kalau tidak "B"

// Switch/case
cocok nilai
    kasus 1:
        // kode
    kasus 2:
        // kode
    bawaan:
        // kode
selesai
```

---

### Perulangan

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
    // kode
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

### Fungsi

```python
// Fungsi dasar
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

// Fungsi dengan pengembalian
fungsi tambah(a, b):
    hasil a + b
selesai

// Parameter default
fungsi sapa(nama, sapaan="Halo"):
    tampilkan f"{sapaan}, {nama}!"
selesai

// Lambda
kuadrat itu lambda dengan x -> x * x
tambah itu lambda dengan a, b -> a + b
```

---

### Kelas (OOP)

```python
// Kelas dasar
kelas Mahasiswa:
    konstruktor(nama, nim):
        diri.nama itu nama
        diri.nim itu nim
    selesai
    
    metode info():
        tampilkan f"Nama: {diri.nama}"
    selesai
selesai

// Pewarisan
kelas MahasiswaS1 warisi Mahasiswa:
    konstruktor(nama, nim, jurusan):
        super().__init__(nama, nim)
        diri.jurusan itu jurusan
    selesai
selesai

// Buat instance
mhs itu Mahasiswa("Budi", "12345")
mhs.info()
```

---

### Operasi String

```python
// Dasar
panjang(teks)              // Panjang
huruf_besar(teks)          // Huruf besar
huruf_kecil(teks)          // Huruf kecil
huruf_kapital(teks)        // Kapitalisasi

// Manipulasi
potong(teks, 0, 5)         // Potong
ganti(teks, "old", "new")  // Ganti
pisah(teks, ",")           // Pisah
gabung("-", list)          // Gabung
hapus_spasi(teks)          // Hapus spasi

// Pencarian
cari(teks, "sub")          // Cari
mulai_dengan(teks, "pre")  // Mulai dengan
akhiri_dengan(teks, "suf") // Akhiri dengan

// Validasi
adalah_angka(teks)         // Apakah angka
adalah_huruf(teks)         // Apakah huruf
adalah_alfanumerik(teks)   // Apakah alfanumerik

// F-string
pesan itu f"Nama: {nama}, Umur: {umur}"
```

---


### Import System (NEW) 🚀

```python
// Import satu item
dari module impor item

// Import banyak item
dari module impor item1, item2, item3

// Import dengan alias
dari module impor item sebagai alias

// Import dari nested module
dari folder.module impor item

// Import biasa (seluruh module)
impor module sebagai alias

// Contoh penggunaan
dari math_utils impor jumlah, perkalian
dari string_utils impor format_text sebagai fmt
impor helpers as h
```

---

### Operasi List

```python
// Dasar
panjang(list)              // Panjang
tambah(list, item)         // Tambah
hapus(list, item)          // Hapus
masukkan(list, idx, item)  // Sisipkan

// Pengurutan
urutkan(list, terbalik)    // Urutkan di tempat
sorted(list, reverse)      // Kembalikan salinan terurut
balikkan(list)             // Balikkan di tempat
terbalik(list)             // Kembalikan salinan terbalik

// Agregasi
jumlah(list)               // Jumlah
min(list)                  // Minimum
max(list)                  // Maksimum

// Comprehension
[x * 2 untuk setiap x dari list]
[x untuk setiap x dari list jika x > 0]
```

---

### Operasi Dict

```python
// Akses
nilai itu dict["key"]
nilai itu dict.get("key", default)

// Modifikasi
dict["key"] itu "value"
perbarui(dict, other_dict)

// Kunci & Nilai
kunci(dict)                // Kunci
nilai(dict)                // Nilai
items(dict)                // Item

// Periksa
"key" dalam dict           // Memiliki kunci

// Comprehension
{k: v * 2 untuk setiap k, v dari dict.items()}
```

---

### Operasi File

```python
// Baca
content itu baca_file("file.txt")
lines itu baca_baris("file.txt")

// Tulis
tulis_file("file.txt", content)
tambah_file("file.txt", content)

// Periksa & Hapus
ada_file("file.txt")
hapus_file("file.txt")

// Manajer konteks
dengan buka("file.txt", "r") sebagai f
    content itu f.baca()
selesai
```

---

### Operasi JSON

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

### Operasi HTTP (BARU di versi terbaru!)

```python
// Permintaan GET
response itu http_get("https://api.example.com/users")
tampilkan response.status_code
data itu response.json()

// Permintaan POST
payload itu {"nama": "Budi", "email": "budi@example.com"}
response itu http_post("https://api.example.com/users", json=payload)

// Permintaan PUT
response itu http_put("https://api.example.com/users/1", json=data)

// Permintaan DELETE
response itu http_delete("https://api.example.com/users/1")

// Dengan parameter
params itu {"page": 1, "limit": 10}
response itu http_get("https://api.example.com/users", params=params)

// Dengan header
headers itu {"Authorization": "Bearer token123"}
response itu http_get("https://api.example.com/data", headers=headers)

// Alias bahasa Indonesia
response itu ambil_http(url)      // GET
response itu kirim_http(url, ...)  // POST
response itu perbarui_http(url, ...) // PUT
response itu hapus_http(url)       // DELETE
```

---

### Operasi Matematika

```python
// Dasar
absolut(x)                 // Nilai absolut
bulat(x, digits)           // Bulatkan
pembulatan_atas(x)         // Pembulatan ke atas
pembulatan_bawah(x)        // Pembulatan ke bawah
pangkat(base, exp)         // Pangkat
akar(x)                    // Akar kuadrat

// Trigonometri
sinus(x)                   // Sin
cosinus(x)                 // Cos
tangen(x)                  // Tan

// Statistik
rata_rata(list)            // Rata-rata
nilai_tengah(list)         // Median
modus(list)                // Modus
deviasi_standar(list)      // Deviasi standar
variansi(list)             // Variansi

// Acak
acak()                     // Acak 0-1
acak_bulat(min, max)       // Bilangan bulat acak
pilih_acak(list)           // Pilihan acak
```

---

### Penanganan Kesalahan

```python
// Try-catch
coba
    // kode yang mungkin gagal
tangkap ErrorType sebagai e
    // tangani kesalahan
akhirnya
    // pembersihan
selesai

// Raise error
raise Exception("Pesan kesalahan")

// Pengecualian kustom
kelas CustomError warisi Exception:
    konstruktor(message):
        diri.message itu message
    selesai
selesai
```

---

### Async/Await

```python
// Fungsi async
async fungsi fetch_data(url):
    response itu await http_get(url)
    hasil response.json()
selesai

// Panggil async
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

// Bersarang
[[i * j untuk setiap j dari range(3)] untuk setiap i dari range(3)]
```

---

### Integrasi Python

```python
// Impor modul
impor_python "math"
impor_python "numpy" sebagai np

// Impor spesifik
dari_python "math" impor sqrt, pi

// Panggil fungsi Python
hasil itu panggil_python math.sqrt(16)
array itu panggil_python np.array([1, 2, 3])

// Gunakan library Python
impor_python "requests"
response itu panggil_python requests.get(url)
```

---

### Perintah REPL (BARU di versi terbaru!)

```bash
# Mulai REPL
rmc

# Perintah REPL
>>> bantuan      # Tampilkan bantuan
>>> keluar       # Keluar dari REPL
>>> bersih       # Bersihkan layar
>>> riwayat      # Tampilkan riwayat
>>> reset        # Reset interpreter
>>> variabel     # Tampilkan semua variabel
```

---

### Konversi Tipe

```python
// Ke string
ke_teks(value)
str(value)

// Ke angka
ke_angka(value)
float(value)

// Ke integer
ke_bulat(value)
int(value)

// Ke boolean
ke_boolean(value)
bool(value)

// Ke list
ke_list(value)
list(value)
```

---

### Fungsi Iterasi

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

### Pola Umum

#### 1. Baca dan Proses File
```python
dengan buka("data.txt", "r") sebagai f
    untuk setiap line dari f
        processed itu line.strip()
        tampilkan processed
    selesai
selesai
```

#### 2. Permintaan API dengan Penanganan Kesalahan
```python
coba
    response itu http_get("https://api.example.com/data")
    jika response.ok()
        data itu response.json()
        // proses data
    lainnya
        tampilkan f"Error: {response.status_code}"
    selesai
tangkap Exception sebagai e
    tampilkan f"Permintaan gagal: {e}"
selesai
```

#### 3. Pemrosesan List
```python
// Filter dan transformasi
angka itu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap itu [x untuk setiap x dari angka jika x % 2 == 0]
kuadrat itu [x ** 2 untuk setiap x dari genap]
tampilkan kuadrat  // [4, 16, 36, 64, 100]
```

#### 4. Manipulasi Dictionary
```python
// Gabungkan dictionary
dict1 itu {"a": 1, "b": 2}
dict2 itu {"c": 3, "d": 4}
merged itu {**dict1, **dict2}

// Filter dictionary
filtered itu {k: v untuk setiap k, v dari dict.items() jika v > 10}
```

#### 5. Kelas dengan Properti
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

## 🔑 Kata Kunci

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
gunakan, impor, dari, impor_python, panggil_python
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

## 📚 Tautan Cepat

- [Instalasi](installation.md)
- [Dasar-dasar Sintaks](syntax-basics.md)
- [Fungsi Bawaan](builtin-functions.md)
- [Fitur Lanjutan](advanced-features.md)
- [Integrasi Python](python-integration.md)
- [Contoh](examples.md)

---

**Versi: Terbaru**  
**Terakhir Diperbarui: 2025-10-08**

**Baru di versi terbaru:**
   - 🚀 Sistem Import OOP baru (dari...impor)
   - 📦 Import dari nested modules
   - 🏷️ Import dengan alias
   - 📚 Module caching untuk performa
- ✨ REPL (Shell Interaktif)
- 🌐 HTTP Client Bawaan
- 📦 7 fungsi HTTP baru
- 🚀 Tidak perlu impor untuk HTTP!