# Referensi Cepat

## 🚀 Lembar Contekan RenzMcLang

Panduan referensi cepat untuk sintaks dan fitur RenzMcLang.

---

## 📝 Komentar

```renzmc
// Komentar satu baris
```

---

## 🔢 Variabel

```renzmc
nama itu "Budi"              // String
umur itu 25                  // Integer
tinggi itu 175.5             // Float
aktif itu benar              // Boolean
```

---

## 📤 Output

```renzmc
tampilkan "Hello"            // Tampilkan
cetak "Hello"                // Cetak
tulis "Hello"                // Tulis
tunjukkan "Hello"            // Tunjukkan
```

---

## 🔤 Format String

```renzmc
nama itu "Budi"
tampilkan f"Halo, {nama}!"   // F-string
```

---

## ➕ Operator

### Aritmatika
```renzmc
a + b        // Penjumlahan
a - b        // Pengurangan
a * b        // Perkalian
a / b        // Pembagian
a % b        // Modulo
a ** b       // Pangkat
a // b       // Pembagian bulat
```

### Perbandingan
```renzmc
a == b       // Sama dengan
a != b       // Tidak sama dengan
a > b        // Lebih besar dari
a < b        // Lebih kecil dari
a >= b       // Lebih besar atau sama dengan
a <= b       // Lebih kecil atau sama dengan
```

### Logika
```renzmc
a dan b      // AND
a atau b     // OR
tidak a      // NOT
```

### Penugasan Gabungan
```renzmc
x += 5       // x = x + 5
x -= 3       // x = x - 3
x *= 2       // x = x * 2
x /= 4       // x = x / 4
```

### Bitwise
```renzmc
a & b        // AND
a | b        // OR
a ^ b        // XOR
~a           // NOT
a << 1       // Geser kiri
a >> 1       // Geser kanan
```

---

## 🔀 Alur Kontrol

### If-Else
```renzmc
jika kondisi
    // kode
kalau tidak jika kondisi2
    // kode
kalau tidak
    // kode
selesai
```

### Ternary
```renzmc
hasil itu "A" jika x > 5 kalau tidak "B"
```

### Switch-Case
```renzmc
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

## 🔁 Perulangan

### Perulangan For
```renzmc
untuk i dari 1 sampai 10
    tampilkan i
selesai
```

### Perulangan For Each
```renzmc
untuk setiap item dari daftar
    tampilkan item
selesai
```

### Perulangan While
```renzmc
selama kondisi
    // kode
selesai
```

### Kontrol Perulangan
```renzmc
lanjut       // Continue
berhenti     // Break
```

---

## 📦 Fungsi

### Fungsi Dasar
```renzmc
fungsi nama(param1, param2):
    // kode
    kembali hasil
selesai
```

### Fungsi Lambda
```renzmc
kuadrat itu lambda x: x * x
```

### Pemanggilan Fungsi
```renzmc
hasil itu nama(arg1, arg2)
```

---

## 📊 Struktur Data

### List
```renzmc
daftar itu [1, 2, 3, 4, 5]
daftar[0]                    // Akses
daftar[0:2]                  // Slice
```

### Dictionary
```renzmc
data itu {
    "key1": "value1",
    "key2": "value2"
}
data["key1"]                 // Akses
```

### Set
```renzmc
himpunan itu {1, 2, 3, 4, 5}
```

### Tuple
```renzmc
tuple itu (1, 2, 3)
```

---

## 🎨 Comprehensions

### List Comprehension
```renzmc
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
```

### Dict Comprehension
```renzmc
dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5]}
```

---

## 🛡️ Penanganan Error

```renzmc
coba
    // kode
tangkap ErrorType sebagai e:
    // tangani error
akhirnya
    // pembersihan
selesai
```

---

## 🔌 Integrasi Python

### Import Modul
```renzmc
impor_python "requests"
impor_python "json"
```

### Panggil Fungsi Python
```renzmc
hasil itu panggil_python math.sqrt(16)
```

### Akses Objek Python
```renzmc
status itu response.status_code
```

---

## 📚 Fungsi Bawaan

### Fungsi String
```renzmc
panjang(text)                // Panjang
huruf_besar(text)            // Huruf besar
huruf_kecil(text)            // Huruf kecil
pisah(text, sep)             // Pisah
gabung(sep, items)           // Gabung
ganti(text, old, new)        // Ganti
```

### Fungsi Matematika
```renzmc
akar(x)                      // Akar kuadrat
pangkat(x, y)                // Pangkat
absolut(x)                   // Absolut
bulat(x)                     // Bulatkan
```

### Fungsi List
```renzmc
tambah(list, item)           // Tambah
hapus(list, item)            // Hapus
urutkan(list)                // Urutkan
balikkan(list)               // Balikkan
minimum(list)                // Minimum
maksimum(list)               // Maksimum
jumlah(list)                 // Jumlah
rata_rata(list)              // Rata-rata
```

### Fungsi Iterasi
```renzmc
map(func, list)              // Map
filter(func, list)           // Filter
zip(list1, list2)            // Zip
enumerate(list)              // Enumerate
```

### Fungsi File
```renzmc
baca_file(path)              // Baca file
tulis_file(path, content)    // Tulis file
hapus_file(path)             // Hapus file
```

### Fungsi Sistem
```renzmc
waktu()                      // Waktu saat ini
tidur(seconds)               // Tidur
acak()                       // Acak
```

---

## 🎯 OOP (Berbasis Fungsi)

### Konstruktor
```renzmc
buat fungsi buat_orang dengan nama, umur
    orang itu {
        "nama": nama,
        "umur": umur
    }
    hasil orang
selesai
```

### Metode
```renzmc
buat fungsi perkenalan dengan orang
    hasil f"Halo, {orang['nama']}"
selesai
```

### Penggunaan
```renzmc
orang1 itu panggil buat_orang dengan "Budi", 25
pesan itu panggil perkenalan dengan orang1
```

---

## ⚡ Async/Await

```renzmc
impor_python "asyncio"

async fungsi fetch_data(url):
    await panggil_python asyncio.sleep(1)
    hasil f"Data dari {url}"
selesai

async fungsi main():
    data itu await fetch_data("https://api.com")
    tampilkan data
selesai

panggil_python asyncio.run(main())
```

---

## 🎨 Context Manager

```renzmc
dengan buka("file.txt", "r") sebagai f:
    content itu f.read()
    tampilkan content
selesai
```

---

## 🔑 Kata Kunci

### Alur Kontrol
- `jika` / `kalau` - if
- `kalau tidak` - else
- `kalau tidak jika` - elif
- `selesai` - end
- `selama` - while
- `untuk` - for
- `dari` - from
- `sampai` - to
- `lanjut` - continue
- `berhenti` - break

### Fungsi
- `fungsi` - function
- `kembali` - return
- `lambda` - lambda
- `async` - async
- `await` - await

### OOP
- `buat fungsi` - create function
- `dengan` - with
- `panggil` - call

### Penanganan Error
- `coba` - try
- `tangkap` - catch
- `akhirnya` - finally
- `sebagai` - as

### Integrasi Python
- `impor_python` - import Python module
- `panggil_python` - call Python function

### Nilai
- `benar` - true
- `salah` - false
- `itu` - is/equals

### Operator
- `dan` - and
- `atau` - or
- `tidak` - not
- `dalam` - in

---

## 📖 Ekstensi File

- `.rmc` - File sumber RenzMcLang

---

## 🚀 Baris Perintah

```bash
# Jalankan file
rmc script.rmc

# Jalankan kode langsung
rmc -c "tampilkan 'Hello'"

# Tampilkan versi
rmc --version

# Mode interaktif
rmc
```

---

## 💡 Tips

1. **Gunakan f-string** untuk format string
2. **Gunakan comprehensions** untuk kode yang ringkas
3. **Gunakan fungsi bawaan** bila tersedia
4. **Tangani error** dengan try-catch
5. **Impor pustaka Python** untuk fungsionalitas tambahan

---

## 📚 Sumber Lainnya

- [Panduan Instalasi](installation.md)
- [Dasar-dasar Sintaks](syntax-basics.md)
- [Fungsi Bawaan](builtin-functions.md)
- [Fitur Lanjutan](advanced-features.md)
- [Integrasi Python](python-integration.md)
- [Contoh](examples.md)

---

**Referensi Cepat v1.0 - RenzMcLang**

**Selamat Coding! 🚀**