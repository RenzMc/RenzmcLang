# Fungsi List Built-in (Terverifikasi)

🚨 **PENTING:** Hanya fungsi yang TERVERIFIKASI bekerja yang ditampilkan di sini.

---

## Fungsi List Dasar ✅

### panjang()

Menghitung jumlah elemen dalam list.

**Sintaks:**
```python
panjang(list)
```

**Parameter:**
- `list` (list): List yang akan dihitung panjangnya

**Mengembalikan:**
- Integer: Jumlah elemen dalam list

**Contoh:**
```python
angka it [1, 2, 3, 4, 5]
hasil it panjang(angka)
tampilkan hasil  // Output: 5
```

### tambah()

Menambahkan elemen ke akhir list.

**Sintaks:**
```python
tambah(list, elemen)
```

**Parameter:**
- `list` (list): List yang akan ditambahkan elemennya
- `elemen` (apa saja): Elemen yang akan ditambahkan

**Contoh:**
```python
buah it ["apel", "jeruk"]
tambah(buah, "mangga")
tampilkan buah  // Output: ["apel", "jeruk", "mangga"]
```

### hapus()

Menghapus elemen pertama yang ditemukan dalam list.

**Sintaks:**
```python
hapus(list, elemen)
```

**Parameter:**
- `list` (list): List yang akan dihapus elemennya
- `elemen` (apa saja): Elemen yang akan dihapus

**Contoh:**
```python
angka it [1, 2, 3, 4, 3]
hapus(angka, 3)
tampilkan angka  // Output: [1, 2, 4, 3]
```

### urutkan()

Mengurutkan elemen dalam list.

**Sintaks:**
```python
urutkan(list, descending)
```

**Parameter:**
- `list` (list): List yang akan diurutkan
- `descending` (boolean): `salah` untuk ascending, `benar` untuk descending

**Contoh:**
```python
angka it [3, 1, 4, 1, 5]
urutkan(angka, salah)  // Ascending
tampilkan angka  // Output: [1, 1, 3, 4, 5]

urutkan(angka, benar)   // Descending  
tampilkan angka  // Output: [5, 4, 3, 1, 1]
```

---

## Operasi List Dasar ✅

### Akses Elemen

**Sintaks:**
```python
elemen it list[index]
```

**Contoh:**
```python
buah it ["apel", "jeruk", "mangga"]
pertama it buah[0]      // Output: "apel"
terakhir it buah[-1]     // Output: "mangga"
```

### List Slicing

**Sintaks:**
```python
bagian it list[start:end]
```

**Contoh:**
```python
angka it [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// Basic slicing
potong1 it angka[2:5]    // Output: [2, 3, 4]
potong2 it angka[:5]     // Output: [0, 1, 2, 3, 4]
potong3 it angka[5:]     // Output: [5, 6, 7, 8, 9]
potong4 it angka[-3:]    // Output: [7, 8, 9]
```

### Pembuatan List

**Sintaks:**
```python
list_kosong it []
list_dengan_nilai it [item1, item2, item3]
```

**Contoh:**
```python
kosong it []                          // Output: []
angka it [1, 2, 3, 4, 5]              // Output: [1, 2, 3, 4, 5]
campuran it [1, "dua", 3.0, benar]    // Output: [1, "dua", 3.0, benar]
```

---

## Operasi Aritmatika ✅

### Penggabungan List

**Sintaks:**
```python
hasil it list1 + list2
```

**Contoh:**
```python
list1 it [1, 2, 3]
list2 it [4, 5, 6]
gabung it list1 + list2
tampilkan gabung  // Output: [1, 2, 3, 4, 5, 6]
```

### Pengulangan List

**Sintaks:**
```python
hasil it list * angka
```

**Contoh:**
```python
dasar it [1, 2]
ulang it dasar * 3
tampilkan ulang  // Output: [1, 2, 1, 2, 1, 2]
```

---

## Iteration ✅

### For Each Loop

**Sintaks:**
```python
untuk setiap item dari list
    // operasi dengan item
selesai
```

**Contoh:**
```python
buah it ["apel", "jeruk", "mangga"]
untuk setiap item dari buah
    tampilkan item
selesai
// Output:
// apel
// jeruk
// mangga
```

---

## 🚫 Fungsi yang TIDAK DIDUKUNG

Fungsi-fungsi berikut TIDAK bekerja di RenzMcLang:

- ❌ `append()` - Gunakan `tambah(list, item)`
- ❌ `remove()` - Gunakan `hapus(list, item)`
- ❌ `sort()` - Gunakan `urutkan(list, descending)`
- ❌ `pop()` - Gunakan Python integration
- ❌ `clear()` - Gunakan Python integration
- ❌ `copy()` - Gunakan Python integration
- ❌ `count()` - Gunakan Python integration
- ❌ `extend()` - Gunakan Python integration
- ❌ `index()` - Gunakan Python integration
- ❌ `insert()` - Gunakan Python integration
- ❌ `reverse()` - Gunakan Python integration
- ❌ List comprehensions - Tidak didukung
- ❌ Method chaining - Tidak didukung

---

## Alternatif: Python Integration

Untuk fungsi list yang lebih kompleks, gunakan integrasi Python:

```python
// Import list operations dari Python
impor_python "copy"

// Gunakan fungsi Python
data it [1, 2, 3]
salinan it panggil_python copy.deepcopy(data)
tampilkan salinan

// Atau evaluasi ekspresi Python langsung
hasil it evaluasi_python("[1, 2, 3] + [4, 5, 6]")
tampilkan hasil  // Output: [1, 2, 3, 4, 5, 6]
```

---

## Best Practices

### 1. Gunakan function-style untuk built-in functions
```python
// ✅ Benar
tambah(list, item)
hapus(list, item)
urutkan(list, salah)

// ❌ Salah - method tidak didukung
list.tambah(item)
list.hapus(item)
list.urutkan()
```

### 2. Iterasi yang benar
```python
// ✅ Benar
untuk setiap item dari daftar
    tampilkan item
selesai

// ❌ Salah - comprehension tidak didukung
hasil it [item * 2 untuk setiap item dari daftar]
```

### 3. Slicing yang aman
```python
// ✅ Benar
potong it list[1:5]

// ❌ Salah - tidak ada error checking otomatis
// Pastikan index valid
```

---

## Troubleshooting

### Error Umum:
1. **"Token tidak dikenal" dengan method-style**
   - Gunakan function-style: `tambah(list, item)` bukan `list.tambah(item)`

2. **"Index out of range"**
   - Pastikan index valid saat mengakses elemen
   - Gunakan `panjang(list)` untuk cek batas

3. **"Variabel tidak terdefinisi"**
   - Pastikan nama fungsi benar (lihat daftar di atas)

---

*Untuk informasi lebih lanjut, lihat [Iteration Functions](iteration_functions.md) dan [Python Integration](python_integration.md)*