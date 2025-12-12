# Fungsi List Built-in

Dokumen ini mencakup semua fungsi list built-in yang tersedia di RenzMcLang. Fungsi-fungsi ini selalu tersedia tanpa perlu mengimpor modul apapun.

## Fungsi Manipulasi List

### tambah()

Menambahkan item ke akhir list.

**Sintaks:**
```python
tambah(list, item)
```

**Parameter:**
- `list` (list): List yang akan ditambah item
- `item` (apa saja): Item yang akan ditambahkan

**Mengembalikan:**
- List: List yang telah ditambah item

**Contoh:**
```python
buah itu ["apel", "jeruk"]
tambah(buah, "mangga")
tampilkan buah  // Output: ["apel", "jeruk", "mangga"]

// Menambahkan angka
angka itu [1, 2, 3]
tambah(angka, 4)
tampilkan angka  // Output: [1, 2, 3, 4]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list

---

### hapus()

Menghapus item pertama yang ditemukan dalam list.

**Sintaks:**
```python
hapus(list, item)
```

**Parameter:**
- `list` (list): List yang akan dihapus item
- `item` (apa saja): Item yang akan dihapus

**Mengembalikan:**
- List: List yang telah dihapus item

**Contoh:**
```python
buah itu ["apel", "jeruk", "mangga", "jeruk"]
hapus(buah, "jeruk")
tampilkan buah  // Output: ["apel", "mangga", "jeruk"]

// Menghapus angka
angka itu [1, 2, 3, 2, 4]
hapus(angka, 2)
tampilkan angka  // Output: [1, 3, 2, 4]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list
- Melempar `ValueError` jika item tidak ditemukan dalam list

---

### hapus_pada()

Menghapus item pada indeks tertentu.

**Sintaks:**
```python
hapus_pada(list, indeks)
```

**Parameter:**
- `list` (list): List yang akan dihapus item
- `indeks` (integer): Indeks item yang akan dihapus

**Mengembalikan:**
- List: List yang telah dihapus item

**Contoh:**
```python
buah itu ["apel", "jeruk", "mangga", "pisang"]
hapus_pada(buah, 1)  // Hapus indeks 1 ("jeruk")
tampilkan buah  // Output: ["apel", "mangga", "pisang"]

// Indeks negatif
angka itu [10, 20, 30, 40]
hapus_pada(angka, -1)  // Hapus item terakhir
tampilkan angka  // Output: [10, 20, 30]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list
- Melempar `IndexError` jika indeks di luar jangkauan

---

### masukkan()

Menyisipkan item pada indeks tertentu.

**Sintaks:**
```python
masukkan(list, indeks, item)
```

**Parameter:**
- `list` (list): List yang akan disisipkan item
- `indeks` (integer): Indeks tempat penyisipan
- `item` (apa saja): Item yang akan disisipkan

**Mengembalikan:**
- List: List yang telah disisipkan item

**Contoh:**
```python
buah itu ["apel", "pisang"]
masukkan(buah, 1, "jeruk")  // Sisipkan pada indeks 1
tampilkan buah  // Output: ["apel", "jeruk", "pisang"]

// Sisipkan di awal
angka itu [2, 3, 4]
masukkan(angka, 0, 1)
tampilkan angka  // Output: [1, 2, 3, 4]

// Sisipkan di akhir
nama itu ["Alice", "Bob"]
masukkan(nama, 2, "Charlie")
tampilkan nama  // Output: ["Alice", "Bob", "Charlie"]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list
- Melempar `IndexError` jika indeks di luar jangkauan

---

### urutkan()

Mengurutkan item dalam list.

**Sintaks:**
```python
urutkan(list, terbalik)
```

**Parameter:**
- `list` (list): List yang akan diurutkan
- `terbalik` (boolean, opsional): `benar` untuk urutan terbalik, `salah` untuk urutan normal (default: `salah`)

**Mengembalikan:**
- List: List yang telah diurutkan

**Contoh:**
```python
// Urutan normal
angka itu [3, 1, 4, 1, 5, 9]
urutkan(angka)
tampilkan angka  // Output: [1, 1, 3, 4, 5, 9]

// Urutan terbalik
angka2 itu [3, 1, 4, 1, 5, 9]
urutkan(angka2, benar)
tampilkan angka2  // Output: [9, 5, 4, 3, 1, 1]

// Mengurutkan string
buah itu ["jeruk", "apel", "mangga"]
urutkan(buah)
tampilkan buah  // Output: ["apel", "jeruk", "mangga"]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list
- Melempar `TypeError` jika list berisi item yang tidak dapat dibandingkan

---

### balikkan()

Membalik urutan item dalam list.

**Sintaks:**
```python
balikkan(list)
```

**Parameter:**
- `list` (list): List yang akan dibalik urutannya

**Mengembalikan:**
- List: List yang telah dibalik urutannya

**Contoh:**
```python
angka itu [1, 2, 3, 4, 5]
balikkan(angka)
tampilkan angka  // Output: [5, 4, 3, 2, 1]

buah itu ["apel", "jeruk", "mangga"]
balikkan(buah)
tampilkan buah  // Output: ["mangga", "jeruk", "apel"]
```

**Error:**
- Melempar `TypeError` jika argumen bukan list

---

### extend()

Menambahkan semua item dari iterable ke akhir list.

**Sintaks:**
```python
extend(list, iterable)
```

**Parameter:**
- `list` (list): List yang akan ditambah item
- `iterable` (iterable): Iterable yang item-nya akan ditambahkan

**Mengembalikan:**
- List: List yang telah ditambah item

**Contoh:**
```python
// Extend dengan list lain
buah1 itu ["apel", "jeruk"]
buah2 itu ["mangga", "pisang"]
extend(buah1, buah2)
tampilkan buah1  // Output: ["apel", "jeruk", "mangga", "pisang"]

// Extend dengan tuple
angka itu [1, 2, 3]
extend(angka, (4, 5, 6))
tampilkan angka  // Output: [1, 2, 3, 4, 5, 6]

// Extend dengan string
huruf itu ["a", "b"]
extend(huruf, "cde")
tampilkan huruf  // Output: ["a", "b", "c", "d", "e"]
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list

## Fungsi Pencarian dan Informasi

### hitung()

Menghitung jumlah kemunculan item dalam list.

**Sintaks:**
```python
hitung(list, item)
```

**Parameter:**
- `list` (list): List yang akan dihitung item-nya
- `item` (apa saja): Item yang akan dihitung

**Mengembalikan:**
- Integer: Jumlah kemunculan item

**Contoh:**
```python
buah itu ["apel", "jeruk", "apel", "mangga", "apel"]
jumlah_apel itu hitung(buah, "apel")
tampilkan jumlah_apel  // Output: 3

angka itu [1, 2, 3, 2, 4, 2, 5]
jumlah_dua itu hitung(angka, 2)
tampilkan jumlah_dua  // Output: 3

// Item tidak ditemukan
jumlah_nol itu hitung(angka, 0)
tampilkan jumlah_nol  // Output: 0
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list

---

### indeks()

Mencari indeks pertama dari item dalam list.

**Sintaks:**
```python
indeks(list, item)
```

**Parameter:**
- `list` (list): List yang akan dicari
- `item` (apa saja): Item yang akan dicari indeksnya

**Mengembalikan:**
- Integer: Indeks pertama dari item

**Contoh:**
```python
buah itu ["apel", "jeruk", "mangga", "pisang"]
posisi_mangga itu indeks(buah, "mangga")
tampilkan posisi_mangga  // Output: 2

angka itu [10, 20, 30, 40, 50]
posisi_30 itu indeks(angka, 30)
tampilkan posisi_30  // Output: 2

// Item duplikat (mengembalikan yang pertama)
duplikat itu ["a", "b", "c", "b", "d"]
posisi_b itu indeks(duplikat, "b")
tampilkan posisi_b  // Output: 1
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan list
- Melempar `ValueError` jika item tidak ditemukan dalam list

## Fungsi Salin

### salin()

Membuat salinan shallow dari object.

**Sintaks:**
```python
salin(objek)
```

**Parameter:**
- `objek` (apa saja): Object yang akan disalin

**Mengembalikan:**
- Object: Salinan shallow dari objek

**Contoh:**
```python
// Salin list
asli itu [1, 2, 3]
salinan itu salin(asli)
tampilkan salinan  // Output: [1, 2, 3]

// Modifikasi salinan tidak mempengaruhi asli
tambah(salinan, 4)
tampilkan asli     // Output: [1, 2, 3] (tidak berubah)
tampilkan salinan  // Output: [1, 2, 3, 4] (berubah)
```

---

### salin_dalam()

Membuat salinan deep dari object.

**Sintaks:**
```python
salin_dalam(objek)
```

**Parameter:**
- `objek` (apa saja): Object yang akan disalin

**Mengembalikan:**
- Object: Salinan deep dari objek

**Contoh:**
```python
// Salin list bersarang
asli_bersarang itu [[1, 2], [3, 4]]
salinan_dalam itu salin_dalam(asli_bersarang)
tampilkan salinan_dalam  // Output: [[1, 2], [3, 4]]

// Modifikasi salinan deep tidak mempengaruhi asli
tambah(salinan_dalam[0], 99)
tampilkan asli_bersarang     // Output: [[1, 2], [3, 4]] (tidak berubah)
tampilkan salinan_dalam  // Output: [[1, 2, 99], [3, 4]] (berubah)
```

## Contoh Praktis

### Daftar Belanja

```python
// Buat daftar belanja
daftar_belanja itu []

// Tambah item
tambah(daftar_belanja, "susu")
tambah(daftar_belanja, "roti")
tambah(daftar_belanja, "telur")
tampilkan daftar_belanja  // Output: ["susu", "roti", "telur"]

// Sisipkan item di tengah
masukkan(daftar_belanja, 1, "keju")
tampilkan daftar_belanja  // Output: ["susu", "keju", "roti", "telur"]

// Hapus item yang tidak perlu
hapus(daftar_belanja, "telur")
tampilkan daftar_belanja  // Output: ["susu", "keju", "roti"]

// Urutkan alphabetically
urutkan(daftar_belanja)
tampilkan daftar_belanja  // Output: ["keju", "roti", "susu"]
```

### Analisis Data

```python
// Data skor siswa
skor itu [85, 92, 78, 95, 88, 76, 89, 93]

// Hitung jumlah siswa
jumlah_siswa itu panjang(skor)
tampilkan f"Jumlah siswa: {jumlah_siswa}"

// Cari skor tertinggi dan terendah
urutkan(skor)
skor_terendah itu skor[0]
skor_tertinggi itu skor[-1]
tampilkan f"Skor terendah: {skor_terendah}"
tampilkan f"Skor tertinggi: {skor_tertinggi}"

// Hitung rata-rata
total itu 0
untuk setiap nilai dari skor
    total itu total + nilai
selesai
rata_rata itu total / jumlah_siswa
tampilkan f"Rata-rata: {rata_rata}"

// Hitung siswa di atas rata-rata
atas_rata_rata itu 0
untuk setiap nilai dari skor
    jika nilai > rata_rata
        atas_rata_rata itu atas_rata_rata + 1
    selesai
selesai
tampilkan f"Siswa di atas rata-rata: {atas_rata_rata}"
```

### Queue (Antrian)

```python
// Implementasi queue sederhana
buat fungsi buat_queue
    hasil []
selesai

buat fungsi enqueue dengan queue, item
    tambah(queue, item)
selesai

buat fungsi dequeue dengan queue
    jika panjang(queue) > 0
        hasil queue[0]
        hapus_pada(queue, 0)
    lainnya
        hasil "Queue kosong"
    selesai
selesai

buat fungsi is_empty dengan queue
    hasil panjang(queue) == 0
selesai

// Penggunaan
antrian itu buat_queue()
enqueue(antrian, "Alice")
enqueue(antrian, "Bob")
enqueue(antrian, "Charlie")

tampilkan f"Antrian: {antrian}"

// Layani pelanggan
pertama itu dequeue(antrian)
tampilkan f"Dilayani: {pertama}"
tampilkan f"Sisa antrian: {antrian}"

kedua itu dequeue(antrian)
tampilkan f"Dilayani: {kedua}"
tampilkan f"Sisa antrian: {antrian}"

tampilkan f"Queue kosong? {is_empty(antrian)}"
```

## Catatan Penggunaan

1. **Modifikasi In-place**: Sebagian besar fungsi modifikasi list dilakukan in-place (mengubah list asli).

2. **Return Value**: Fungsi modifikasi mengembalikan list yang telah dimodifikasi untuk chaining.

3. **Indeks Negatif**: Mendukung indeks negatif untuk mengakses item dari belakang.

4. **Type Safety**: Fungsi memvalidasi tipe input dan memberikan pesan error dalam bahasa Indonesia.

5. **Shallow vs Deep Copy**: 
   - `salin()` membuat shallow copy (objek bersarang masih mereferensi yang sama)
   - `salin_dalam()` membuat deep copy (semua objek bersarang juga disalin)

6. **Performance**: Fungsi-fungsi ini dioptimasi untuk performa dan langsung dipetakan ke method list Python.