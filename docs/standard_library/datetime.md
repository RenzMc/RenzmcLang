# Modul DateTime

Modul DateTime menyediakan fungsi-fungsi untuk manipulasi tanggal dan waktu, mengikuti standar modul datetime Python dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari datetime impor datetime, timedelta, sekarang, hari_ini
// atau impor semua
dari datetime impor *
```

## Kelas DateTime

### datetime
Kelas untuk representasi tanggal dan waktu.

**Konstruktor:**
```python
datetime(tahun, bulan, hari, jam=0, menit=0, detik=0, mikrodetik=0, tzinfo=None)
```

**Parameter:**
- `tahun` (integer): Tahun (1-9999)
- `bulan` (integer): Bulan (1-12)
- `hari` (integer): Hari (1-31, tergantung bulan)
- `jam` (integer, opsional): Jam (0-23)
- `menit` (integer, opsional): Menit (0-59)
- `detik` (integer, opsional): Detik (0-59)
- `mikrodetik` (integer, opsional): Mikrodetik (0-999999)
- `tzinfo` (timezone, opsional): Informasi timezone

**Contoh:**
```python
dari datetime impor datetime

// Buat datetime object
dt1 itu datetime(2025, 1, 15, 14, 30, 45)
tampilkan dt1  // Output: 2025-01-15 14:30:45

// Buat datetime untuk hari ini
dt2 itu datetime(2025, 1, 15)
tampilkan dt2  // Output: 2025-01-15 00:00:00
```

---

### date
Kelas untuk representasi tanggal saja.

**Konstruktor:**
```python
date(tahun, bulan, hari)
```

**Contoh:**
```python
dari datetime impor date

tanggal itu date(2025, 1, 15)
tampilkan tanggal  // Output: 2025-01-15
```

---

### time
Kelas untuk representasi waktu saja.

**Konstruktor:**
```python
time(jam=0, menit=0, detik=0, mikrodetik=0, tzinfo=None)
```

**Contoh:**
```python
dari datetime impor time

waktu itu time(14, 30, 45)
tampilkan waktu  // Output: 14:30:45
```

---

### timedelta
Kelas untuk representasi durasi waktu.

**Konstruktor:**
```python
timedelta(hari=0, detik=0, mikrodetik=0, milidetik=0, menit=0, jam=0, minggu=0)
```

**Contoh:**
```python
dari datetime impor timedelta

// Durasi 3 hari 4 jam 30 menit
durasi itu timedelta(hari=3, jam=4, menit=30)
tampilkan durasi  // Output: 3 days, 4:30:00
```

## Fungsi Waktu Saat Ini

### sekarang() / waktu_sekarang()
Mendapatkan tanggal dan waktu saat ini.

**Sintaks:**
```python
sekarang(timezone)
waktu_sekarang(timezone)
```

**Parameter:**
- `timezone` (timezone, opsional): Timezone yang diinginkan

**Mengembalikan:**
- datetime object: Waktu saat ini

**Contoh:**
```python
dari datetime impor sekarang, waktu_sekarang

waktu_skg itu sekarang()
tampilkan f"Waktu sekarang: {waktu_skg}"

// Dengan timezone (jika tersedia)
waktu_jakarta itu sekarang(timezone.utc)
tampilkan f"Waktu UTC: {waktu_jakarta}"
```

---

### hari_ini() / tanggal_sekarang()
Mendapatkan tanggal hari ini.

**Sintaks:**
```python
hari_ini()
tanggal_sekarang()
```

**Mengembalikan:**
- date object: Tanggal hari ini

**Contoh:**
```python
dari datetime impor hari_ini

today itu hari_ini()
tampilkan f"Hari ini: {today}"
```

---

### utc_sekarang() / utc_waktu_sekarang()
Mendapatkan waktu saat ini dalam UTC.

**Sintaks:**
```python
utc_sekarang()
utc_waktu_sekarang()
```

**Mengembalikan:**
- datetime object: Waktu UTC saat ini

**Contoh:**
```python
dari datetime impor utc_sekarang

utc_time itu utc_sekarang()
tampilkan f"Waktu UTC: {utc_time}"
```

## Fungsi Parsing String

### parse_isoformat() / pars_format_iso()
Parsing string tanggal format ISO.

**Sintaks:**
```python
parse_isoformat(string_tanggal)
pars_format_iso(string_tanggal)
```

**Parameter:**
- `string_tanggal` (string): String tanggal format ISO (YYYY-MM-DD atau YYYY-MM-DDTHH:MM:SS)

**Mengembalikan:**
- datetime object: Tanggal yang diparsing

**Contoh:**
```python
dari datetime impor parse_isoformat

// Parse date only
tanggal itu parse_isoformat("2025-01-15")
tampilkan f"Tanggal: {tanggal}"

// Parse datetime
dt itu parse_isoformat("2025-01-15T14:30:45")
tampilkan f"Datetime: {dt}"
```

---

### strptime() / pars_string_waktu()
Parsing string tanggal dengan format tertentu.

**Sintaks:**
```python
strptime(string_tanggal, format_string)
pars_string_waktu(string_tanggal, format_string)
```

**Parameter:**
- `string_tanggal` (string): String tanggal yang akan diparsing
- `format_string` (string): Format string sesuai standar Python

**Mengembalikan:**
- datetime object: Tanggal yang diparsing

**Contoh:**
```python
dari datetime impor strptime

// Format DD/MM/YYYY
dt1 itu strptime("15/01/2025", "%d/%m/%Y")
tampilkan f"Format DD/MM/YYYY: {dt1}"

// Format dengan nama hari
dt2 itu strptime("Senin, 15 Januari 2025", "%A, %d %B %Y")
tampilkan f"Format lengkap: {dt2}"

// Format waktu
dt3 itu strptime("15-01-2025 14:30:45", "%d-%m-%Y %H:%M:%S")
tampilkan f"Dengan waktu: {dt3}"
```

## Fungsi Utilitas Waktu

### waktu() / waktu_epoch()
Mendapatkan waktu saat ini dalam detik sejak epoch.

**Sintaks:**
```python
waktu()
waktu_epoch()
```

**Mengembalikan:**
- Float: Waktu dalam detik sejak epoch (1 Januari 1970)

**Contoh:**
```python
dari datetime impor waktu, waktu_epoch

epoch_time itu waktu()
tampilkan f"Waktu epoch: {epoch_time}"

// Menghitung waktu eksekusi
start itu waktu()
// ... lakukan operasi ...
end itu waktu()
tampilkan f"Waktu eksekusi: {end - start} detik"
```

---

### sleep() / tidur()
Menunda eksekusi selama jumlah detik tertentu.

**Sintaks:**
```python
sleep(detik)
tidur(detik)
```

**Parameter:**
- `detik` (float): Jumlah detik untuk menunda

**Contoh:**
```python
dari datetime impor sleep, tidur

tampilkan "Mulai eksekusi"
sleep(2.5)  // Tunda 2.5 detik
tampilkan "Selesai setelah 2.5 detik"

// Menggunakan alias Indonesia
tampilkan "Tidur sebentar..."
tidur(1)    // Tunda 1 detik
tampilkan "Bangun!"
```

## Konstanta

### MINYEAR / tahun_minimum
Tahun minimum yang didukung (1).

```python
dari datetime impor MINYEAR, tahun_minimum

tampilkan f"Tahun minimum: {MINYEAR}"
tampilkan f"Tahun minimum (Indonesia): {tahun_minimum}"
```

---

### MAXYEAR / tahun_maksimum
Tahun maksimum yang didukung (9999).

```python
dari datetime impor MAXYEAR, tahun_maksimum

tampilkan f"Tahun maksimum: {MAXYEAR}"
tampilkan f"Tahun maksimum (Indonesia): {tahun_maksimum}"
```

## Operasi DateTime

### Penambahan dan Pengurangan

```python
dari datetime impor datetime, timedelta, sekarang

// Dapatkan waktu sekarang
skrng itu sekarang()

// Tambah 5 hari
lima_hari_lagi itu skrng + timedelta(hari=5)
tampilkan f"5 hari lagi: {lima_hari_lagi}"

// Kurangi 2 minggu
dua_minggu_lalu itu skrng - timedelta(minggu=2)
tampilkan f"2 minggu lalu: {dua_minggu_lalu}"

// Tambah 3 jam 30 menit
tambahan_waktu itu skrng + timedelta(jam=3, menit=30)
tampilkan f"3 jam 30 menit lagi: {tambahan_waktu}"
```

### Perbandingan

```python
dari datetime impor datetime

waktu1 itu datetime(2025, 1, 15, 10, 0, 0)
waktu2 itu datetime(2025, 1, 15, 14, 30, 0)

jika waktu1 < waktu2
    tampilkan "Waktu1 lebih awal dari Waktu2"
selesai

jika waktu1 == waktu2
    tampilkan "Waktu1 sama dengan Waktu2"
lainnya
    tampilkan "Waktu1 tidak sama dengan Waktu2"
selesai
```

### Format String

```python
dari datetime impor datetime, sekarang

waktu_skg itu sekarang()

// Format standar
tampilkan f"Tanggal: {waktu_skg.strftime('%d/%m/%Y')}"
tampilkan f"Waktu: {waktu_skg.strftime('%H:%M:%S')}"

// Format lengkap
tampilkan f"Lengkap: {waktu_skg.strftime('%A, %d %B %Y %H:%M:%S')}"

// Format ISO
tampilkan f"ISO: {waktu_skg.isoformat()}"
```

## Contoh Praktis

### Kalkulator Usia

```python
dari datetime impor datetime, hari_ini

buat fungsi hitung_usia dengan tanggal_lahir
    hari_ini_dt itu hari_ini()
    usia_tahun itu hari_ini_dt.tahun - tanggal_lahir.tahun
    
    // Periksa apakah sudah ulang tahun tahun ini
    jika (hari_ini_dt.bulan, hari_ini_dt.hari) < (tanggal_lahir.bulan, tanggal_lahir.hari)
        usia_tahun itu usia_tahun - 1
    selesai
    
    hasil usia_tahun
selesai

lahir itu datetime(1990, 5, 15).date()
usia itu hitung_usia(lahir)
tampilkan f"Usia: {usia} tahun"
```

### Penghitung Mundur

```python
dari datetime impor datetime, sekarang, sleep

buat fungsi countdown dengan detik
    selama detik > 0
        tampilkan f"Countdown: {detik}"
        sleep(1)
        detik itu detik - 1
    selesai
    tampilkan "Waktu habis!"
selesai

// Mulai countdown 10 detik
countdown(10)
```

### Deadline Calculator

```python
dari datetime import datetime, timedelta, sekarang

buat fungsi hitung_deadline dengan hari_kerja
    hari_kerja_per_minggu itu 5
    minggu itu hari_kerja // hari_kerja_per_minggu
    sisa_hari itu hari_kerja % hari_kerja_per_minggu
    
    start itu sekarang()
    
    // Tambah minggu penuh
    deadline itu start + timedelta(minggu=minggu)
    
    // Tambah hari kerja sisa
    hari_terhitung itu 0
    selama hari_terhitung < sisa_hari
        deadline itu deadline + timedelta(hari=1)
        
        // Lewati akhir pekan (Sabtu=5, Minggu=6)
        jika deadline.weekday() >= 5
            deadline itu deadline + timedelta(hari=1)
        lainnya
            hari_terhitung itu hari_terhitung + 1
        selesai
    selesai
    
    hasil deadline
selesai

deadline_kerja itu hitung_deadline(7)  // 7 hari kerja
tampilkan f"Deadline 7 hari kerja: {deadline_kerja}"
```

## Format String Umum

| Kode | Deskripsi | Contoh |
|------|-----------|--------|
| `%Y` | Tahun 4 digit | 2025 |
| `%y` | Tahun 2 digit | 25 |
| `%m` | Bulan (01-12) | 01 |
| `%B` | Nama bulan lengkap | Januari |
| `%b` | Nama bulan singkat | Jan |
| `%d` | Hari (01-31) | 15 |
| `%A` | Nama hari lengkap | Senin |
| `%a` | Nama hari singkat | Sen |
| `%H` | Jam (00-23) | 14 |
| `%I` | Jam (01-12) | 02 |
| `%M` | Menit (00-59) | 30 |
| `%S` | Detik (00-59) | 45 |
| `%f` | Mikrodetik | 123456 |
| `%p` | AM/PM | PM |

## Catatan Penggunaan

1. **Impor Diperlukan**: Semua fungsi datetime harus diimpor dari modul datetime.

2. **Alias Indonesia**: Banyak fungsi memiliki alias Indonesia:
   - `waktu_sekarang()` untuk `sekarang()`
   - `tanggal_sekarang()` untuk `hari_ini()`
   - `utc_waktu_sekarang()` untuk `utc_sekarang()`
   - `pars_format_iso()` untuk `parse_isoformat()`
   - `pars_string_waktu()` untuk `strptime()`
   - `waktu_epoch()` untuk `waktu()`
   - `tidur()` untuk `sleep()`
   - `tahun_minimum` untuk `MINYEAR`
   - `tahun_maksimum` untuk `MAXYEAR`

3. **Timezone**: Fungsi timezone memerlukan instalasi pytz atau library timezone lainnya.

4. **Format String**: Gunakan format string Python standar untuk parsing dan formatting.

5. **Imutabilitas**: datetime objects tidak dapat diubah, operasi selalu mengembalikan object baru.

6. **Precision**: datetime mendukung precision hingga mikrodetik.