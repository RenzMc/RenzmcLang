# Fungsi String Built-in (Terverifikasi)

🚨 **PENTING:** Hanya fungsi yang TERVERIFIKASI bekerja yang ditampilkan di sini.

---

## Fungsi String Dasar ✅

### panjang()

Menghitung jumlah karakter dalam string.

**Sintaks:**
```python
panjang(teks)
```

**Parameter:**
- `teks` (string): String yang akan dihitung panjangnya

**Mengembalikan:**
- Integer: Jumlah karakter dalam string

**Contoh:**
```python
teks it "Hello World"
hasil it panjang(teks)
tampilkan hasil  // Output: 11
```

### huruf_besar()

Mengubah teks menjadi huruf kapital.

**Sintaks:**
```python
huruf_besar(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan diubah menjadi huruf kapital

**Mengembalikan:**
- String: Versi huruf kapital dari teks input

**Contoh:**
```python
teks it "Hello World"
hasil it huruf_besar(teks)
tampilkan hasil  // Output: "HELLO WORLD"
```

### huruf_kecil()

Mengubah teks menjadi huruf kecil.

**Sintaks:**
```python
huruf_kecil(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan diubah menjadi huruf kecil

**Mengembalikan:**
- String: Versi huruf kecil dari teks input

**Contoh:**
```python
teks it "Hello World"
hasil it huruf_kecil(teks)
tampilkan hasil  // Output: "hello world"
```

---

## Fungsi Konversi ✅

### str() / ke_teks()

Mengubah objek apapun menjadi string.

**Sintaks:**
```python
str(objek)
ke_teks(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diubah menjadi string

**Mengembalikan:**
- String: Representasi string dari objek

**Contoh:**
```python
// Konversi dasar
hasil1 it str(123)              // Output: "123"
hasil2 it ke_teks(45.67)         // Output: "45.67"
hasil3 it str(benar)             // Output: "True"
hasil4 it ke_teks(salah)          // Output: "False"
```

---

## Operasi String Dasar ✅

### Penggabungan String

**Sintaks:**
```python
hasil it string1 + string2
```

**Contoh:**
```python
nama_depan it "John"
nama_belakang it "Doe"
nama_lengkap it nama_depan + " " + nama_belakang
tampilkan nama_lengkap  // Output: "John Doe"
```

### Pengulangan String

**Sintaks:**
```python
hasil it string * angka
```

**Contoh:**
```python
garis it "=" * 10
tampilkan garis  // Output: "=========="
```

### Akses Karakter

**Sintaks:**
```python
karakter it string[index]
```

**Contoh:**
```python
teks it "Hello"
pertama it teks[0]      // Output: "H"
terakhir it teks[-1]     // Output: "o"
```

---

## F-String Interpolation ✅

### Format String

**Sintaks:**
```python
pesan it f"Text {variabel} more text"
```

**Contoh:**
```python
nama it "Budi"
umur it 25
pesan it f"Nama saya {nama}, umur {umur} tahun"
tampilkan pesan  // Output: "Nama saya Budi, umur 25 tahun"
```

---

## 🚫 Fungsi yang TIDAK DIDUKUNG

Fungsi-fungsi berikut TIDAK bekerja di RenzMcLang:

- ❌ `split()` - Gunakan Python integration
- ❌ `join()` - Gunakan Python integration  
- ❌ `replace()` - Gunakan Python integration
- ❌ `find()` / `index()` - Gunakan Python integration
- ❌ `startswith()` / `endswith()` - Gunakan Python integration
- ❌ `strip()` / `lstrip()` / `rstrip()` - Gunakan Python integration
- ❌ Semua fungsi string lanjutan lainnya

---

## Alternatif: Python Integration

Untuk fungsi string yang lebih kompleks, gunakan integrasi Python:

```python
// Import string module Python
impor_python "string"

// Gunakan fungsi Python
hasil it panggil_python " ".join(["Hello", "World"])
tampilkan hasil  // Output: "Hello World"

// Atau evaluasi ekspresi Python langsung
hasil it evaluasi_python("'Hello World'.split()")
tampilkan hasil  // Output: ["Hello", "World"]
```

---

## Best Practices

### 1. Gunakan F-string untuk formatting
```python
// ✅ Baik
nama it "Budi"
pesan it f"Halo {nama}"

// ❌ Hindari string concatenation kompleks
pesan it "Halo " + nama
```

### 2. Gunakan fungsi yang tersedia
```python
// ✅ Gunakan fungsi built-in
teks it huruf_besar("hello")

// ❌ Jangan coba fungsi yang tidak ada
// hasil it teks.upper()  // ERROR: fungsi tidak ada
```

---

## Troubleshooting

### Error Umum:
1. **"Variabel tidak terdefinisi"**
   - Pastikan nama fungsi benar
   - Cek daftar fungsi yang didukung di atas

2. **"Token tidak dikenal"**
   - Pastikan tidak menggunakan method-style: `string.method()`
   - Gunakan function-style: `function(string)`

---

*Untuk informasi lebih lanjut, lihat [Type Functions](type_functions.md) dan [Python Integration](python_integration.md)*