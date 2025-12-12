# Fungsi Dictionary Built-in

Dokumen ini mencakup semua fungsi dictionary built-in yang tersedia di RenzMcLang. Fungsi-fungsi ini selalu tersedia tanpa perlu mengimpor modul apapun.

## Fungsi Akses Dictionary

### kunci()

Mendapatkan semua kunci dari dictionary.

**Sintaks:**
```python
kunci(dictionary)
```

**Parameter:**
- `dictionary` (dict): Dictionary yang akan diambil kuncinya

**Mengembalikan:**
- List: List berisi semua kunci dalam dictionary

**Contoh:**
```python
profil itu {
    "nama": "Budi",
    "umur": 25,
    "kota": "Jakarta"
}

semua_kunci itu kunci(profil)
tampilkan semua_kunci  // Output: ["nama", "umur", "kota"]

// Iterasi kunci
untuk setiap key dari kunci(profil)
    tampilkan f"Kunci: {key}"
selesai
```

**Error:**
- Melempar `TypeError` jika argumen bukan dictionary

---

### nilai()

Mendapatkan semua nilai dari dictionary.

**Sintaks:**
```python
nilai(dictionary)
```

**Parameter:**
- `dictionary` (dict): Dictionary yang akan diambil nilainya

**Mengembalikan:**
- List: List berisi semua nilai dalam dictionary

**Contoh:**
```python
harga_barang itu {
    "apel": 15000,
    "jeruk": 12000,
    "mangga": 20000
}

semua_nilai itu nilai(harga_barang)
tampilkan semua_nilai  // Output: [15000, 12000, 20000]

// Hitung total harga
total itu 0
untuk setiap harga dari nilai(harga_barang)
    total itu total + harga
selesai
tampilkan f"Total harga: {total}"
```

**Error:**
- Melempar `TypeError` jika argumen bukan dictionary

---

### item()

Mendapatkan semua pasangan kunci-nilai dari dictionary.

**Sintaks:**
```python
item(dictionary)
```

**Parameter:**
- `dictionary` (dict): Dictionary yang akan diambil item-nya

**Mengembalikan:**
- List: List berisi tuple (kunci, nilai)

**Contoh:**
```python
siswa itu {
    "nama": "Alice",
    "nilai": 85,
    "kelas": "XII"
}

semua_item itu item(siswa)
tampilkan semua_item  // Output: [("nama", "Alice"), ("nilai", 85), ("kelas", "XII")]

// Iterasi item
untuk setiap (key, value) dari item(siswa)
    tampilkan f"{key}: {value}"
selesai
```

**Error:**
- Melempar `TypeError` jika argumen bukan dictionary

## Fungsi Modifikasi Dictionary

### hapus_kunci()

Menghapus kunci dan nilainya dari dictionary.

**Sintaks:**
```python
hapus_kunci(dictionary, kunci)
```

**Parameter:**
- `dictionary` (dict): Dictionary yang akan dihapus kuncinya
- `kunci` (apa saja): Kunci yang akan dihapus

**Mengembalikan:**
- Dictionary: Dictionary yang telah dihapus kuncinya

**Contoh:**
```python
data_siswa itu {
    "nama": "Bob",
    "umur": 17,
    "alamat": "Surabaya",
    "telepon": "08123456789"
}

// Hapus kunci alamat
hapus_kunci(data_siswa, "alamat")
tampilkan data_siswa  // Output: {"nama": "Bob", "umur": 17, "telepon": "08123456789"}

// Hapus kunci telepon
hapus_kunci(data_siswa, "telepon")
tampilkan data_siswa  // Output: {"nama": "Bob", "umur": 17}
```

**Error:**
- Melempar `TypeError` jika argumen pertama bukan dictionary
- Melempar `KeyError` jika kunci tidak ditemukan dalam dictionary

## Contoh Praktis

### Database Sederhana

```python
// Simulasi database user
database_user itu {}

// Tambah user
database_user["user1"] itu {
    "nama": "Alice Johnson",
    "email": "alice@example.com",
    "umur": 28,
    "aktif": benar
}

database_user["user2"] itu {
    "nama": "Bob Smith",
    "email": "bob@example.com",
    "umur": 32,
    "aktif": benar
}

// Tampilkan semua user
tampilkan "Daftar User:"
untuk setiap user_id dari kunci(database_user)
    user_data itu database_user[user_id]
    tampilkan f"ID: {user_id}, Nama: {user_data['nama']}"
selesai

// Hapus user yang tidak aktif
database_user["user3"] itu {
    "nama": "Charlie Brown",
    "email": "charlie@example.com",
    "umur": 25,
    "aktif": salah
}

// Cari dan hapus user tidak aktif
user_id_aktif itu []
untuk setiap user_id dari kunci(database_user)
    jika database硍_user[user_id]["aktif"] == benar
        tambah(user_id_aktif, user_id)
    selesai
selesai

// Buat database baru hanya user aktif
database_aktif itu {}
untuk setiap user_id dari user_id_aktif
    database_aktif[user_id] itu database_user[user_id]
selesai

tampilkan f"User aktif: {kunci(database_aktif)}"
```

### Sistem Inventori

```python
// Sistem inventori barang
inventori itu {
    "Laptop": {"jumlah": 10, "harga": 8500000},
    "Mouse": {"jumlah": 25, "harga": 150000},
    "Keyboard": {"jumlah": 15, "harga": 450000},
    "Monitor": {"jumlah": 8, "harga": 2500000}
}

// Hitung total nilai inventori
total_nilai itu 0
untuk setiap (barang, info) dari item(inventori)
    nilai_barang itu info["jumlah"] * info["harga"]
    total_nilai itu total_nilai + nilai_barang
    tampilkan f"{barang}: {info['jumlah']} unit x Rp {info['harga']} = Rp {nilai_barang}"
selesai

tampilkan f"Total nilai inventori: Rp {total_nilai}"

// Cari barang dengan stok terbanyak
stok_terbanyak itu 0
barang_terbanyak itu ""

untuk setiap (barang, info) dari item(inventori)
    jika info["jumlah"] > stok_terbanyak
        stok_terbanyak itu info["jumlah"]
        barang_terbanyak itu barang
    selesai
selesai

tampilkan f"Barang dengan stok terbanyak: {barang_terbanyak} ({stok_terbanyak} unit)"

// Hapus barang dengan stok 0
inventori["Printer"] itu {"jumlah": 0, "harga": 1200000}
barang_stok_kosong itu []

untuk setiap barang dari kunci(inventori)
    jika inventori[barang]["jumlah"] == 0
        tambah(barang_stok_kosong, barang)
    selesai
selesai

// Hapus barang stok kosong
untuk setiap barang dari barang_stok_kosong
    hapus_kunci(inventori, barang)
selesai

tampilkan f"Inventori setelah dibersihkan: {kunci(inventori)}"
```

### Konfigurasi Aplikasi

```python
// Konfigurasi default aplikasi
konfig_default itu {
    "database_host": "localhost",
    "database_port": 5432,
    "database_name": "myapp",
    "debug_mode": salah,
    "max_connections": 100,
    "timeout": 30
}

// Konfigurasi user (override default)
konfig_user itu {
    "database_host": "production-server.com",
    "debug_mode": benar,
    "max_connections": 200
}

// Gabungkan konfigurasi
konfig_final it salin(konfig_default)

// Override dengan konfigurasi user
untuk setiap (key, value) dari item(konfig_user)
    konfig_final[key] itu value
selesai

tampilkan "Konfigurasi Final:"
untuk setiap (key, value) dari item(konfig_final)
    tampilkan f"{key}: {value}"
selesai

// Validasi konfigurasi
validasi_errors itu []

// Cek host tidak kosong
jika konfig_final["database_host"] == ""
    tambah(validasi_errors, "Database host tidak boleh kosong")
selesai

// Cek port dalam range
port itu konfig_final["database_port"]
jika port < 1 atau port > 65535
    tambah(validasi_errors, "Database port harus antara 1-65535")
selesai

// Cek max_connections positif
jika konfig_final["max_connections"] <= 0
    tambah(validasi_errors, "Max connections harus positif")
selesai

jika panjang(validasi_errors) > 0
    tampilkan "Error validasi konfigurasi:"
    untuk setiap error dari validasi_errors
        tampilkan f"- {error}"
    selesai
lainnya
    tampilkan "Konfigurasi valid!"
selesai
```

### Analisis Data Statistik

```python
// Data penjualan per bulan
penjualan itu {
    "Januari": 15000000,
    "Februari": 18500000,
    "Maret": 22000000,
    "April": 19500000,
    "Mei": 25000000,
    "Juni": 28000000
}

// Statistik dasar
nilai_penjualan itu nilai(penjualan)
bulan_penjualan itu kunci(penjualan)

// Total penjualan
total itu 0
untuk setiap nilai dari nilai_penjualan
    total itu total + nilai
selesai
tampilkan f"Total penjualan: Rp {total}"

// Rata-rata penjualan
rata_rata itu total / panjang(nilai_penjualan)
tampilkan f"Rata-rata penjualan: Rp {rata_rata}"

// Penjualan tertinggi
penjualan_tertinggi it max(nilai_penjualan)
indeks_tertinggi it indeks(nilai_penjualan, penjualan_tertinggi)
bulan_tertinggi it bulan_penjualan[indeks_tertinggi]
tampilkan f"Penjualan tertinggi: {bulan_tertinggi} (Rp {penjualan_tertinggi})"

// Penjualan terendah
penjualan_terendah it min(nilai_penjualan)
indeks_terendah it indeks(nilai_penjualan, penjualan_terendah)
bulan_terendah it bulan_penjualan[indeks_terendah]
tampilkan f"Penjualan terendah: {bulan_terendah} (Rp {penjualan_terendah})"

// Cari bulan dengan penjualan di atas rata-rata
bulan_diatas_rata it []
untuk setiap (bulan, nilai) dari item(penjualan)
    jika nilai > rata_rata
        tambah(bulan_diatas_rata, bulan)
    selesai
selesai

tampilkan f"Bulan dengan penjualan di atas rata-rata: {bulan_diatas_rata}"

// Persentase kenaikan dari bulan sebelumnya
kenaikan_persen it {}
bulan_list it kunci(penjualan)
untuk i dari 1 sampai panjang(bulan_list) - 1
    bulan_sekarang it bulan_list[i]
    bulan_sebelumnya it bulan_list[i-1]
    nilai_sekarang it penjualan[bulan_sekarang]
    nilai_sebelumnya it penjualan[bulan_sebelumnya]
    
    persentase it ((nilai_sekarang - nilai_sebelumnya) / nilai_sebelumnya) * 100
    kenaikan_persen[bulan_sekarang] it persentase
selesai

tampilkan "Persentase kenaikan penjualan:"
untuk setiap (bulan, persen) dari item(kenaikan_persen)
    tampilkan f"{bulan}: {persen:.2f}%"
selesai
```

### Cache Manager

```python
// Sistem cache sederhana
cache it {}
cache_max_size it 100
cache_ttl it 300  // 5 menit dalam detik

buat fungsi simpan_cache dengan key, value
    // Hapus cache lama jika penuh
    jika panjang(kunci(cache)) >= cache_max_size
        // Hapus 10% cache tertua
        hapus_count it cache_max_size // 10
        cache_keys it kunci(cache)
        
        untuk i dari 0 sampai hapus_count - 1
            jika i < panjang(cache_keys)
                hapus_kunci(cache, cache_keys[i])
            selesai
        selesai
    selesai
    
    // Simpan dengan timestamp
    cache[key] it {
        "value": value,
        "timestamp": waktu()  // waktu() fungsi untuk mendapatkan epoch time
    }
selesai

buat fungsi ambil_cache dengan key
    jika key dalam cache
        cache_item it cache[key]
        usia it waktu() - cache_item["timestamp"]
        
        jika usia < cache_ttl
            hasil cache_item["value"]
        lainnya
            hapus_kunci(cache, key)
            hasil "Cache expired"
        selesai
    lainnya
        hasil "Cache miss"
    selesai
selesai

buat fungsi clear_cache_expired
    cache_keys it kunci(cache)
    expired_keys it []
    
    untuk setiap key dari cache_keys
        cache_item it cache[key]
        usia it waktu() - cache_item["timestamp"]
        
        jika usia >= cache_ttl
            tambah(expired_keys, key)
        selesai
    selesai
    
    untuk setiap key dari expired_keys
        hapus_kunci(cache, key)
    selesai
    
    tampilkan f"Dihapus {panjang(expired_keys)} cache expired"
selesai

// Penggunaan cache
simpan_cache("user:123", {"nama": "Alice", "umur": 28})
simpan_cache("product:456", {"nama": "Laptop", "harga": 8500000})
simpan_cache("settings:theme", "dark")

user_data it ambil_cache("user:123")
tampilkan f"Data user: {user_data}"

product_data it ambil_cache("product:999")  // Tidak ada
tampilkan f"Data product: {product_data}"

tampilkan f"Cache keys: {kunci(cache)}"
clear_cache_expired()
```

## Catatan Penggunaan

1. **Return Type**: Fungsi `kunci()`, `nilai()`, dan `item()` mengembalikan list, bukan view object seperti Python.

2. **Modifikasi In-place**: Fungsi `hapus_kunci()` memodifikasi dictionary asli.

3. **Order Preservation**: Order kunci dipertahankan (Python 3.7+).

4. **Type Safety**: Fungsi memvalidasi tipe input dan memberikan pesan error dalam bahasa Indonesia.

5. **Key Uniqueness**: Dictionary tidak boleh memiliki kunci duplikat.

6. **Hashable Keys**: Kunci harus berupa objek yang dapat di-hash (string, number, tuple).

7. **Performance**: Fungsi-fungsi ini dioptimasi untuk performa dan langsung dipetakan ke method dict Python.

8. **Memory Usage**: Gunakan fungsi ini dengan bijak untuk dictionary yang sangat besar.