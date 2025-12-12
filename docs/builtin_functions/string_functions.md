# Fungsi String Built-in

Dokumen ini mencakup semua fungsi string built-in yang tersedia di RenzMcLang. Fungsi-fungsi ini selalu tersedia tanpa perlu mengimpor modul apapun.

## Fungsi String Dasar

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
teks itu "Hello World"
hasil itu huruf_besar(teks)
tampilkan hasil  // Output: "HELLO WORLD"
```

**Error:**
- Melempar `TypeError` jika argumen bukan string

---

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
teks itu "HELLO WORLD"
hasil itu huruf_kecil(teks)
tampilkan hasil  // Output: "hello world"
```

**Error:**
- Melempar `TypeError` jika argumen bukan string

---

### potong()

Mengambil substring dari teks.

**Sintaks:**
```python
potong(teks, mulai, akhir)
```

**Parameter:**
- `teks` (string): Teks sumber
- `mulai` (integer): Indeks awal (inklusif)
- `akhir` (integer, opsional): Indeks akhir (eksklusif). Jika dihilangkan, mengambil sampai akhir

**Mengembalikan:**
- String: Substring yang diambil

**Contoh:**
```python
teks itu "Hello World"
hasil1 itu potong(teks, 6)           // Output: "World"
hasil2 itu potong(teks, 0, 5)        // Output: "Hello"
hasil3 itu potong(teks, -5)          // Output: "World"
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan string
- Melempar `IndexError` jika indeks di luar jangkauan

---

### gabung()

Menggabungkan beberapa item menjadi satu string dengan pemisah.

**Sintaks:**
```python
gabung(pemisah, item1, item2, ...)
```

**Parameter:**
- `pemisah` (string): String yang ditempatkan di antara item
- `item1, item2, ...` (apa saja): Item yang akan digabung (otomatis dikonversi ke string)

**Mengembalikan:**
- String: String yang telah digabung

**Contoh:**
```python
kata1 itu "Hello"
kata2 itu "World"
kata3 itu "2024"

hasil1 itu gabung(" ", kata1, kata2, kata3)    // Output: "Hello World 2024"
hasil2 itu gabung("-", "A", "B", "C")          // Output: "A-B-C"
hasil3 itu gabung("", 1, 2, 3)                 // Output: "123"
```

**Error:**
- Melempar `TypeError` jika pemisah bukan string

---

### pisah()

Memisahkan teks menjadi list substring.

**Sintaks:**
```python
pisah(teks, pemisah)
```

**Parameter:**
- `teks` (string): Teks yang akan dipisah
- `pemisah` (string, opsional): Pembatas. Jika dihilangkan, memisah berdasarkan whitespace

**Mengembalikan:**
- List: List substring

**Contoh:**
```python
teks itu "Hello World Python"
hasil1 itu pisah(teks)                    // Output: ["Hello", "World", "Python"]
hasil2 itu pisah(teks, " ")              // Output: ["Hello", "World", "Python"]
hasil3 itu pisah("A,B,C", ",")           // Output: ["A", "B", "C"]
hasil4 itu pisah("A-B-C-D", "-")         // Output: ["A", "B", "C", "D"]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan string

---

### ganti()

Mengganti kemunculan substring dengan substring lain.

**Sintaks:**
```python
ganti(teks, lama, baru)
```

**Parameter:**
- `teks` (string): Teks sumber
- `lama` (string): Substring yang akan diganti
- `baru` (string): Substring pengganti

**Mengembalikan:**
- String: Teks dengan penggantian yang telah dilakukan

**Contoh:**
```python
teks itu "Hello World World"
hasil1 itu ganti(teks, "World", "RenzMcLang")  // Output: "Hello RenzMcLang RenzMcLang"
hasil2 itu ganti("A-B-C", "-", " ")            // Output: "A B C"
hasil3 itu ganti("123", "2", "X")              // Output: "1X3"
```

**Error:**
- Melempar `TypeError` jika ada argumen yang bukan string

---

### mulai_dengan()

Memeriksa apakah teks diawali dengan prefix tertentu.

**Sintaks:**
```python
mulai_dengan(teks, prefix)
```

**Parameter:**
- `teks` (string): Teks yang akan diperiksa
- `prefix` (string): Prefix yang dicari

**Mengembalikan:**
- Boolean: `benar` jika teks diawali prefix, `salah` jika tidak

**Contoh:**
```python
teks itu "Hello World"
hasil1 itu mulai_dengan(teks, "Hello")    // Output: benar
hasil2 itu mulai_dengan(teks, "World")    // Output: salah
hasil3 itu mulai_dengan("Python", "Py")   // Output: benar
```

**Error:**
- Melempar `TypeError` jika ada argumen yang bukan string

---

### akhir_dengan()

Memeriksa apakah teks diakhiri dengan suffix tertentu.

**Sintaks:**
```python
akhir_dengan(teks, suffix)
```

**Parameter:**
- `teks` (string): Teks yang akan diperiksa
- `suffix` (string): Suffix yang dicari

**Mengembalikan:**
- Boolean: `benar` jika teks diakhiri suffix, `salah` jika tidak

**Contoh:**
```python
teks itu "Hello World"
hasil1 itu akhir_dengan(teks, "World")    // Output: benar
hasil2 itu akhir_dengan(teks, "Hello")    // Output: salah
hasil3 itu akhir_dengan("Python.py", ".py")  // Output: benar
```

**Error:**
- Melempar `TypeError` jika ada argumen yang bukan string

---

### berisi()

Memeriksa apakah teks mengandung substring tertentu.

**Sintaks:**
```python
berisi(teks, substring)
```

**Parameter:**
- `teks` (string): Teks tempat pencarian
- `substring` (string): Substring yang dicari

**Mengembalikan:**
- Boolean: `benar` jika substring ditemukan, `salah` jika tidak

**Contoh:**
```python
teks itu "Hello World"
hasil1 itu berisi(teks, "World")     // Output: benar
hasil2 itu berisi(teks, "Python")    // Output: salah
hasil3 itu berisi("Python", "thon")  // Output: benar
```

**Error:**
- Melempar `TypeError` jika ada argumen yang bukan string

---

### hapus_spasi()

Menghapus whitespace dari kedua ujung teks.

**Sintaks:**
```python
hapus_spasi(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan dibersihkan

**Mengembalikan:**
- String: Teks tanpa whitespace di awal dan akhir

**Contoh:**
```python
teks itu "   Hello World   "
hasil1 itu hapus_spasi(teks)     // Output: "Hello World"
hasil2 itu hapus_spasi("\tText\n")  // Output: "Text"
hasil3 itu hapus_spasi("NoSpace")  // Output: "NoSpace"
```

**Error:**
- Melempar `TypeError` jika argumen bukan string

---

### format_teks()

Memformat teks menggunakan method format() Python.

**Sintaks:**
```python
format_teks(template, arg1, arg2, ...)
```

**Parameter:**
- `template` (string): String format dengan placeholder
- `arg1, arg2, ...` (apa saja): Nilai yang akan disubstitusikan ke placeholder

**Mengembalikan:**
- String: Teks yang telah diformat

**Contoh:**
```python
nama itu "John"
umur itu 25
hasil1 itu format_teks("Nama: {}, Umur: {}", nama, umur)  // Output: "Nama: John, Umur: 25"
hasil2 itu format_teks("Nilai: {value}", value=100)      // Output: "Nilai: 100"
hasil3 itu format_teks("{0} + {1} = {2}", 5, 3, 8)       // Output: "5 + 3 = 8"
```

**Error:**
- Melempar `TypeError` jika template bukan string
- Melempar `ValueError` jika format tidak valid

## Fungsi Validasi String

### adalah_huruf() / is_alpha()

Memeriksa apakah teks hanya mengandung karakter alfabet.

**Sintaks:**
```python
adalah_huruf(teks)  // atau is_alpha(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung huruf, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_huruf("Hello")      // Output: benar
hasil2 itu adalah_huruf("Hello123")   // Output: salah
hasil3 itu adalah_huruf("ABC")        // Output: benar
hasil4 itu adalah_huruf("")           // Output: salah
```

---

### adalah_angka() / is_digit()

Memeriksa apakah teks hanya mengandung karakter numerik.

**Sintaks:**
```python
adalah_angka(teks)  // atau is_digit(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung digit, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_angka("123")        // Output: benar
hasil2 itu adalah_angka("123.45")     // Output: salah
hasil3 itu adalah_angka("ABC")        // Output: salah
hasil4 itu adalah_angka("0123456789") // Output: benar
```

---

### adalah_alfanumerik() / is_alnum()

Memeriksa apakah teks hanya mengandung karakter alfanumerik.

**Sintaks:**
```python
adalah_alfanumerik(teks)  // atau is_alnum(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung huruf dan digit, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_alfanumerik("Hello123")   // Output: benar
hasil2 itu adalah_alfanumerik("Hello")      // Output: benar
hasil3 itu adalah_alfanumerik("123")        // Output: benar
hasil4 itu adalah_alfanumerik("Hello-123")  // Output: salah
```

---

### adalah_huruf_kecil() / is_lower()

Memeriksa apakah teks hanya mengandung huruf kecil.

**Sintaks:**
```python
adalah_huruf_kecil(teks)  // atau is_lower(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung huruf kecil, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_huruf_kecil("hello")      // Output: benar
hasil2 itu adalah_huruf_kecil("Hello")      // Output: salah
hasil3 itu adalah_huruf_kecil("hello123")   // Output: salah
hasil4 itu adalah_huruf_kecil("abc")        // Output: benar
```

---

### adalah_huruf_besar() / is_upper()

Memeriksa apakah teks hanya mengandung huruf besar.

**Sintaks:**
```python
adalah_huruf_besar(teks)  // atau is_upper(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung huruf besar, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_huruf_besar("HELLO")      // Output: benar
hasil2 itu adalah_huruf_besar("Hello")      // Output: salah
hasil3 itu adalah_huruf_besar("HELLO123")   // Output: salah
hasil4 itu adalah_huruf_besar("ABC")        // Output: benar
```

---

### adalah_spasi() / is_space()

Memeriksa apakah teks hanya mengandung karakter whitespace.

**Sintaks:**
```python
adalah_spasi(teks)  // atau is_space(teks)
```

**Parameter:**
- `teks` (string): Teks yang akan divalidasi

**Mengembalikan:**
- Boolean: `benar` jika teks hanya mengandung whitespace, `salah` jika tidak

**Contoh:**
```python
hasil1 itu adalah_spasi(" ")          // Output: benar
hasil2 itu adalah_spasi("\t\n ")      // Output: benar
hasil3 itu adalah_spasi("Hello")      // Output: salah
hasil4 itu adalah_spasi("")           // Output: salah
```

## Catatan Penggunaan

1. **Alias Fungsi**: Banyak fungsi memiliki nama Indonesia dan Inggris untuk kemudahan:
   - `adalah_huruf()` dan `is_alpha()`
   - `adalah_angka()` dan `is_digit()`
   - `adalah_alfanumerik()` dan `is_alnum()`
   - `adalah_huruf_kecil()` dan `is_lower()`
   - `adalah_huruf_besar()` dan `is_upper()`
   - `adalah_spasi()` dan `is_space()`

2. **Dukungan Unicode**: Semua fungsi string mendukung karakter Unicode.

3. **Penanganan Error**: Fungsi memvalidasi tipe input dan memberikan pesan error yang jelas dalam bahasa Indonesia.

4. **Performa**: Fungsi-fungsi ini dioptimasi untuk operasi string umum dan langsung dipetakan ke method string Python.

5. **Imutabilitas**: Semua fungsi string mengembalikan string baru dan tidak memodifikasi teks asli.