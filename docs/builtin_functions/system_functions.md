# Fungsi Sistem Built-in

Dokumen ini mencakup semua fungsi sistem built-in yang tersedia di RenzMcLang. Fungsi-fungsi ini menyediakan operasi tingkat sistem, penanganan file, operasi waktu, dan kemampuan eksekusi perintah.

## Fungsi Sistem Inti

### waktu()

Mengembalikan timestamp Unix saat ini.

**Sintaks:**
```python
waktu()
```

**Mengembalikan:**
- Float: Timestamp Unix saat ini dalam detik

**Contoh:**
```python
// Dapatkan timestamp saat ini
timestamp it waktu()
tampilkan timestamp         // Output: 1703123456.789 (contoh)

// Gunakan untuk operasi timing
start it waktu()
// Lakukan beberapa pekerjaan
end it waktu()
elapsed it end - start
tampilkan f"Waktu yang berlalu: {elapsed} detik"
```

---

### tidur()

Menjeda eksekusi untuk jumlah detik tertentu.

**Sintaks:**
```python
tidur(detik)
```

**Parameter:**
- `detik` (number): Jumlah detik untuk menjeda

**Contoh:**
```python
// Jeda 2 detik
tampilkan "Memulai..."
tidur(2)
tampilkan "Selesai!"

// Jeda setengah detik
tidur(0.5)

// Jeda dengan feedback pengguna
tampilkan "Memproses data..."
tidur(1)
tampilkan "Data diproses!"
```

---

### tanggal()

Mengembalikan tanggal dan waktu saat ini sebagai string yang diformat.

**Sintaks:**
```python
tanggal()
```

**Mengembalikan:**
- String: Tanggal dan waktu saat ini dalam format "YYYY-MM-DD HH:MM:SS"

**Contoh:**
```python
// Dapatkan tanggal dan waktu saat ini
sekarang it tanggal()
tampilkan sekarang           // Output: "2024-01-15 14:30:25"

// Gunakan dalam logging
log_message it f"[{tanggal()}] Aplikasi dimulai"
tampilkan log_message
```

---

### buat_uuid()

Menghasilkan UUID yang unik (Universally Unique Identifier).

**Sintaks:**
```python
buat_uuid()
```

**Mengembalikan:**
- String: String UUID dalam format standar

**Contoh:**
```python
// Hasilkan identifier unik
session_id it buat_uuid()
tampilkan session_id         // Output: "550e8400-e29b-41d4-a716-446655440000"

// Gunakan untuk filename unik
filename it f"data_{buat_uuid()}.json"
tampilkan filename          // Output: "data_550e8400-e29b-41d4-a716-446655440000.json"

// Gunakan untuk ID transaksi
transaction_id it buat_uuid()
tampilkan f"ID Transaksi: {transaction_id}"
```

## Operasi File

### buka() / open_file()

Membuka file untuk operasi membaca atau menulis.

**Sintaks:**
```python
buka(nama_file, mode)
open_file(nama_file, mode)
```

**Parameter:**
- `nama_file` (string): Path ke file
- `mode` (string, opsional): Mode buka file (default: "r")
  - "r": Mode baca (default)
  - "w": Mode tulis (menimpa file yang ada)
  - "a": Mode tambah
  - "r+": Mode baca dan tulis
  - "w+": Mode tulis dan baca
  - "a+": Mode tambah dan baca

**Mengembalikan:**
- File object: Handle file untuk operasi

**Contoh:**
```python
// Baca dari file
file it buka("data.txt")
content it file.baca()
file.tutup()
tampilkan content

// Tulis ke file
file it buka("output.txt", "w")
file.tulis("Hello, World!")
file.tutup()

// Tambah ke file
file it buka("log.txt", "a")
file.tulis(f"[{tanggal()}] Entri baru\n")
file.tutup()

// Menggunakan alias Inggris
file it open_file("config.json", "r")
config_data it file.baca()
file.tutup()

// Gaya context manager (jika didukung)
dengan buka("data.txt") sebagai file
    content it file.baca()
    tampilkan content
selesai
```

## Fungsi Eksekusi Perintah

### jalankan_perintah()

Menjalankan perintah sistem dengan kontrol keamanan.

**Sintaks:**
```python
jalankan_perintah(perintah, shell, capture_output)
```

**Parameter:**
- `perintah` (string): Perintah untuk dieksekusi
- `shell` (boolean, opsional): Gunakan shell untuk eksekusi (default: benar)
- `capture_output` (boolean, opsional): Tangkap output perintah (default: benar)

**Mengembalikan:**
- Dict: Hasil berisi:
  - "stdout": Output standar
  - "stderr": Error standar
  - "returncode": Kode keluar

**Contoh:**
```python
// Jalankan perintah aman
result it jalankan_perintah("ls -la")
tampilkan result["stdout"]

// Periksa hasil perintah
result it jalankan_perintah("echo 'Hello World'")
tampilkan result["stdout"]    // Output: "Hello World\n"
tampilkan result["returncode"] // Output: 0

// Tangani error perintah
result it jalankan_perintah("cat nonexistent.txt")
tampilkan result["stderr"]    // Pesan error
tampilkan result["returncode"] // Kode keluar bukan nol

// Jalankan perintah dengan shell kustom
result it jalankan_perintah("python --version", shell=benar)
tampilkan result["stdout"]    // Info versi Python
```

## Fungsi Keamanan

### atur_sandbox()

Mengaktifkan atau menonaktifkan mode sandbox untuk eksekusi perintah.

**Sintaks:**
```python
atur_sandbox(diaktifkan)
```

**Parameter:**
- `diaktifkan` (boolean, opsional): Aktifkan sandbox (default: benar)

**Mengembalikan:**
- Boolean: Status sandbox saat ini

**Contoh:**
```python
// Aktifkan sandbox
status it atur_sandbox(benar)
tampilkan status            // Output: benar

// Nonaktifkan sandbox
status it atur_sandbox(salah)
tampilkan status            // Output: salah

// Periksa status saat ini
is_sandboxed it atur_sandbox()
tampilkan f"Sandbox diaktifkan: {is_sandboxed}"
```

---

### tambah_perintah_aman()

Menambahkan perintah ke daftar perintah aman.

**Sintaks:**
```python
tambah_perintah_aman(perintah)
```

**Parameter:**
- `perintah` (string): Perintah untuk ditambahkan ke daftar aman

**Mengembalikan:**
- Boolean: True jika berhasil ditambahkan

**Contoh:**
```python
// Tambah perintah aman kustom
tambah_perintah_aman("python")
tambah_perintah_aman("node")
tambah_perintah_aman("npm")

// Sekarang perintah ini dapat dieksekusi dalam mode sandbox
atur_sandbox(benar)
result it jalankan_perintah("python --version")
tampilkan result["stdout"]
```

---

### hapus_perintah_aman()

Menghapus perintah dari daftar perintah aman.

**Sintaks:**
```python
hapus_perintah_aman(perintah)
```

**Parameter:**
- `perintah` (string): Perintah untuk dihapus dari daftar aman

**Mengembalikan:**
- Boolean: True jika berhasil dihapus, False jika tidak ditemukan

**Contoh:**
```python
// Hapus perintah dari daftar aman
success it hapus_perintah_aman("python")
tampilkan success            // Output: benar

// Coba hapus perintah yang tidak ada
success it hapus_perintah_aman("nonexistent")
tampilkan success            // Output: salah
```

## Operasi Informasi Sistem

### Daftar Perintah Aman

Secara default, perintah berikut aman untuk dieksekusi dalam mode sandbox:
- `ls` - Tampilkan konten direktori
- `cat` - Tampilkan konten file
- `echo` - Tampilkan pesan
- `pwd` - Cetak direktori kerja
- `date` - Tampilkan tanggal dan waktu
- `whoami` - Tampilkan pengguna saat ini
- `uname` - Tampilkan informasi sistem
- `grep` - Cari pola teks
- `find` - Cari file
- `wc` - Hitung kata
- `head` - Tampilkan baris pertama
- `tail` - Tampilkan baris terakhir
- `sort` - Urutkan baris
- `uniq` - Hapus baris duplikat

## Contoh Penggunaan Lanjutan

### Pipeline Pemrosesan File

```python
// Proses multiple file dengan timing
start_time it waktu()

files it ["data1.txt", "data2.txt", "data3.txt"]
results it []

untuk setiap filename dari files
    tampilkan f"Memproses {filename}..."
    
    file it buka(filename, "r")
    content it file.baca()
    file.tutup()
    
    // Proses konten
    processed it huruf_besar(content)
    results.append(processed)
    
    tidur(0.1)  // Jeda singkat
selesai

end_time it waktu()
elapsed it end_time - start_time

tampilkan f"Diproses {panjang(files)} file dalam {elapsed} detik"
```

### Monitoring Sistem

```python
// Buat fungsi monitoring sistem
fungsi monitor_system():
    timestamp it waktu()
    date_str it tanggal()
    session_id it buat_uuid()
    
    tampilkan f"=== Monitor Sistem ==="
    tampilkan f"Waktu: {date_str}"
    tampilkan f"Timestamp: {timestamp}"
    tampilkan f"Sesi: {session_id}"
    
    // Dapatkan info sistem
    hasil whoami it jalankan_perintah("whoami")
    tampilkan f"Pengguna: {hasil['stdout'].strip()}"
    
    hasil uname it jalankan_perintah("uname -a")
    tampilkan f"Sistem: {hasil['stdout'].strip()}"
selesai

// Jalankan monitoring
monitor_system()
```

### Operasi File Aman

```python
// Backup file aman dengan UUID
fungsi backup_file(filepath):
    // Validasi file ada
    coba
        original it buka(filepath, "r")
        content it original.baca()
        original.tutup()
    except
        tampilkan "Error: File tidak ditemukan atau tidak dapat dibaca"
        hasil salah
    selesai
    
    // Buat backup dengan UUID
    backup_name it f"backup_{buat_uuid()}_{filepath}"
    backup it buka(backup_name, "w")
    backup.tulis(content)
    backup.tutup()
    
    tampilkan f"Backup dibuat: {backup_name}"
    hasil benar
selesai

// Penggunaan
backup_file("important.txt")
```

## Pertimbangan Keamanan

1. **Mode Sandbox**: Selalu aktifkan mode sandbox untuk kode tidak tepercaya
2. **Validasi Perintah**: Hanya eksekusi perintah dari daftar aman
3. **Izin File**: Pastikan izin file yang benar sebelum operasi
4. **Perlindungan Timeout**: Perintah memiliki timeout 30 detik built-in
5. **Validasi Input**: Validasi path file dan input perintah

## Penanganan Error

```python
// Eksekusi perintah aman dengan penanganan error
fungsi safe_execute(command):
    coba
        result it jalankan_perintah(command)
        tampilkan "Perintah dieksekusi berhasil"
        tampilkan f"Kode keluar: {result['returncode']}"
        
        jika result['returncode'] == 0
            tampilkan "Output:"
            tampilkan result['stdout']
        lainnya
            tampilkan "Output error:"
            tampilkan result['stderr']
        selesai
        
    except SecurityError sebagai e
        tampilkan f"Error keamanan: {e.message}"
    except TimeoutError
        tampilkan "Perintah timeout"
    except Exception sebagai e
        tampilkan f"Error tak terduga: {e}"
    selesai
selesai

// Penggunaan
safe_execute("ls -la")
```