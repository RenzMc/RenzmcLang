# DateTime Module

The DateTime module provides comprehensive date and time manipulation functionality following Python's datetime module standards with Indonesian function names.

## Import

```python
dari datetime impor *
// atau import specific functions
dari datetime impor datetime, date, time, timedelta, sekarang, hari_ini
```

## Core DateTime Classes

### datetime
Complete date and time object.

**Usage:**
```python
dari datetime impor datetime

// Current datetime
sekarang_dt = datetime.sekarang()
tampilkan sekarang_dt     // Output: "2024-01-15 14:30:25.123456"

// Create specific datetime
dt1 = datetime(2024, 1, 15, 14, 30, 0)
tampilkan dt1            // Output: "2024-01-15 14:30:00"

// Create datetime with timezone
dt2 = datetime(2024, 1, 15, 14, 30, 0, tzinfo=datetime.timezone.utc)
tampilkan dt2            // Output: "2024-01-15 14:30:00+00:00"

// Access components
tahun = dt1.tahun
bulan = dt1.bulan
hari = dt1.hari
jam = dt1.jam
menit = dt1.menit
detik = dt1.detik

tampilkan f"Tahun: {tahun}, Bulan: {bulan}, Hari: {hari}"
```

### date
Date object without time.

**Usage:**
```python
dari datetime impor date

// Current date
hari_ini_date = date.hari_ini()
tampilkan hari_ini_date   // Output: "2024-01-15"

// Create specific date
tanggal_lahir = date(1990, 5, 20)
tampilkan tanggal_lahir   // Output: "1990-05-20"

// Date operations
besok = hari_ini_date + datetime.timedelta(hari=1)
tampilkan besok           // Output: "2024-01-16"

kemarin = hari_ini_date - datetime.timedelta(hari=1)
tampilkan kemarin         // Output: "2024-01-14"
```

### time
Time object without date.

**Usage:**
```python
dari datetime impor time

// Create specific time
waktu_kerja = time(9, 0, 0)      // 09:00:00
waktu_istirahat = time(12, 30)   // 12:30:00
waktu_pulang = time(17, 30)      // 17:30:00

tampilkan waktu_kerja           // Output: "09:00:00"

// Create time with timezone
waktu_utc = time(14, 30, 0, tzinfo=datetime.timezone.utc)
tampilkan waktu_utc             // Output: "14:30:00+00:00"
```

### timedelta
Duration between two dates or times.

**Usage:**
```python
dari datetime impor timedelta

// Create timedelta
delta1 = timedelta(hari=7, jam=2, menit=30)
tampilkan delta1               // Output: "7 days, 2:30:00"

// Time arithmetic
sekarang = datetime.sekarang()
minggu_depan = sekarang + timedelta(hari=7)
tampilkan minggu_depan

// Calculate difference
date1 = date(2024, 1, 1)
date2 = date(2024, 1, 15)
selisih = date2 - date1
tampilkan selisih              // Output: "14 days, 0:00:00"
tampilkan selisih.hari         // Output: 14
```

## Current Time Functions

### sekarang()
Gets current local date and time.

**Syntax:**
```python
sekarang(tz)
```

**Parameters:**
- `tz` (timezone, optional): Specific timezone

**Returns:**
- datetime: Current date and time

**Examples:**
```python
dari datetime impor sekarang

// Basic current time
waktu_skrg = sekarang()
tampilkan waktu_skrg         // Output: "2024-01-15 14:30:25.123456"

// With timezone
waktu_utc = sekarang(datetime.timezone.utc)
tampilkan waktu_utc          // Output: "2024-01-15 07:30:25.123456+00:00"

// Indonesian alias
waktu_skrng = waktu_sekarang()
tampilkan waktu_skrng        // Same as sekarang()
```

---

### hari_ini()
Gets current local date.

**Syntax:**
```python
hari_ini()
```

**Returns:**
- date: Current date

**Examples:**
```python
dari datetime impor hari_ini

tanggal_skrg = hari_ini()
tampilkan tanggal_skrg       // Output: "2024-01-15"

// Indonesian alias
tanggal_skrng = tanggal_sekarang()
tampilkan tanggal_skrng      // Same as hari_ini()
```

---

### utc_sekarang()
Gets current UTC date and time.

**Syntax:**
```python
utc_sekarang()
```

**Returns:**
- datetime: Current UTC date and time

**Examples:**
```python
dari datetime impor utc_sekarang

waktu_utc = utc_sekarang()
tampilkan waktu_utc          // Output: "2024-01-15 07:30:25.123456"

// Indonesian alias
utc_waktu_skrng = utc_waktu_sekarang()
tampilkan utc_waktu_skrng    // Same as utc_sekarang()
```

---

## String Parsing Functions

### parse_isoformat()
Parses ISO format date string.

**Syntax:**
```python
parse_isoformat(date_string)
```

**Parameters:**
- `date_string` (string): ISO format date string

**Returns:**
- datetime: Parsed datetime object

**Examples:**
```python
dari datetime impor parse_isoformat

// Basic ISO format
dt1 = parse_isoformat("2024-01-15T14:30:25")
tampilkan dt1               // Output: "2024-01-15 14:30:25"

// With microseconds
dt2 = parse_isoformat("2024-01-15T14:30:25.123456")
tampilkan dt2               // Output: "2024-01-15 14:30:25.123456"

// With timezone
dt3 = parse_isoformat("2024-01-15T14:30:25+00:00")
tampilkan dt3               // Output: "2024-01-15 14:30:25+00:00"

// Indonesian alias
dt4 = pars_format_iso("2024-01-15T14:30:25")
tampilkan dt4               // Same as parse_isoformat()
```

---

### strptime()
Parses date string with custom format.

**Syntax:**
```python
strptime(date_string, format_string)
```

**Parameters:**
- `date_string` (string): Date string to parse
- `format_string` (string): Format pattern

**Returns:**
- datetime: Parsed datetime object

**Examples:**
```python
dari datetime impor strptime

// DD/MM/YYYY format
dt1 = strptime("15/01/2024", "%d/%m/%Y")
tampilkan dt1               // Output: "2024-01-15 00:00:00"

// MM-DD-YYYY HH:MM format
dt2 = strptime("01-15-2024 14:30", "%m-%d-%Y %H:%M")
tampilkan dt2               // Output: "2024-01-15 14:30:00"

// Full format
dt3 = strptime("Monday, January 15, 2024 02:30 PM", "%A, %B %d, %Y %I:%M %p")
tampilkan dt3               // Output: "2024-01-15 14:30:00"

// Indonesian date format
dt4 = strptime("15 Januari 2024", "%d %B %Y")
tampilkan dt4               // Output: "2024-01-15 00:00:00"

// Indonesian alias
dt5 = pars_string_waktu("15/01/2024", "%d/%m/%Y")
tampilkan dt5               // Same as strptime()
```

---

## Time Functions

### waktu()
Gets current Unix timestamp.

**Syntax:**
```python
waktu()
```

**Returns:**
- Float: Seconds since Unix epoch

**Examples:**
```python
dari datetime impor waktu

timestamp = waktu()
tampilkan timestamp         // Output: 1705312225.123456 (example)

// Indonesian alias
timestamp_id = waktu_epoch()
tampilkan timestamp_id      // Same as waktu()
```

---

### sleep() / tidur()
Pauses execution for specified seconds.

**Syntax:**
```python
sleep(detik)
tidur(detik)
```

**Parameters:**
- `detik` (float): Number of seconds to sleep

**Examples:**
```python
dari datetime impor sleep, tidur

// Sleep for 2 seconds
tampilkan "Starting..."
sleep(2)
tampilkan "Done!"

// Sleep for half a second
tampilkan "Processing..."
tidur(0.5)
tampilkan "Complete!"
```

---

## Constants

### MINYEAR / tahun_minimum
Minimum year value supported (1).

```python
dari datetime impor MINYEAR, tahun_minimum

tampilkan MINYEAR            // Output: 1
tampilkan tahun_minimum      // Output: 1
```

### MAXYEAR / tahun_maksimum
Maximum year value supported (9999).

```python
dari datetime impor MAXYEAR, tahun_maksimum

tampilkan MAXYEAR            // Output: 9999
tampilkan tahun_maksimum     // Output: 9999
```

---

## Advanced Usage Examples

### Date Calculations

```python
dari datetime impor datetime, timedelta, hari_ini

// Calculate age
fungsi hitung_umur(tanggal_lahir):
    hari_ini_date = hari_ini()
    umur = hari_ini_date.tahun - tanggal_lahir.tahun
    
    // Adjust if birthday hasn't occurred this year
    jika (hari_ini_date.bulan, hari_ini_date.hari) < (tanggal_lahir.bulan, tanggal_lahir.hari)
        umur = umur - 1
    selesai
    
    hasil umur
selesai

// Usage
lahir = date(1990, 5, 20)
umur_saya = hitung_umur(lahir)
tampilkan f"Umur: {umur_saya} tahun"
```

### Working Days Calculator

```python
dari datetime impor datetime, timedelta

fungsi hitung_hari_kerja(start_date, end_date):
    current = start_date
    hari_kerja = 0
    
    selama current <= end_date
        // Monday=0, Sunday=6 in Python
        jika current.weekday() < 5  // Monday to Friday
            hari_kerja = hari_kerja + 1
        selesai
        current = current + timedelta(hari=1)
    selesai
    
    hasil hari_kerja
selesai

// Usage
mulai = date(2024, 1, 1)  // Monday
akhir = date(2024, 1, 31) // Wednesday
total_hari_kerja = hitung_hari_kerja(mulai, akhir)
tampilkan f"Hari kerja di Januari 2024: {total_hari_kerja}"
```

### Timezone Handling

```python
dari datetime impor datetime, timezone, timedelta

// Create timezone with offset
wib = timezone(timedelta(jam=7))     // WIB (UTC+7)
wita = timezone(timedelta(jam=8))    // WITA (UTC+8)
wit = timezone(timedelta(jam=9))     // WIT (UTC+9)

// Convert between timezones
utc_time = datetime.now(timezone.utc)
wib_time = utc_time.astimezone(wib)
wita_time = utc_time.astimezone(wita)
wit_time = utc_time.astimezone(wit)

tampilkan f"UTC: {utc_time}"
tampilkan f"WIB: {wib_time}"
tampilkan f"WITA: {wita_time}"
tampilkan f"WIT: {wit_time}"
```

### Date Formatting and Display

```python
dari datetime impor datetime, hari_ini

fungsi format_tanggal_indonesia(dt):
    hari_nama = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_nama = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                  "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    hari_idx = dt.weekday()
    bulan_idx = dt.bulan - 1
    
    hasil f"{hari_nama[hari_idx]}, {dt.hari} {bulan_nama[bulan_idx]} {dt.tahun}"
selesai

// Usage
sekarang_date = hari_ini()
formatted_date = format_tanggal_indonesia(sekarang_date)
tampilkan formatted_date    // Output: "Senin, 15 Januari 2024"
```

### Event Scheduler

```python
dari datetime impor datetime, timedelta, sekarang, sleep

fungsi jadwal_event(event_time, callback):
    sekarang_time = sekarang()
    
    jika event_time > sekarang_time
        tunggu = event_time - sekarang_time
        detik_tunggu = tunggu.total_seconds()
        
        tampilkan f"Event dijadwalkan dalam {detik_tunggu} detik"
        sleep(detik_tunggu)
        
        tampilkan "Menjalankan event..."
        callback()
    lainnya
        tampilkan "Event waktu sudah lewat"
    selesai
selesai

fungsi event_callback():
    tampilkan "Event berhasil dijalankan!"
    tampilkan f"Waktu eksekusi: {sekarang()}"
selesai

// Schedule event for 10 seconds from now
waktu_event = sekarang() + timedelta(detik=10)
jadwal_event(waktu_event, event_callback)
```

### Performance Timing

```python
dari datetime impor waktu

fungsi ukur_waktu_eksekusi(func, *args):
    start_time = waktu()
    result = func(*args)
    end_time = waktu()
    
    execution_time = end_time - start_time
    tampilkan f"Waktu eksekusi: {execution_time:.4f} detik"
    
    hasil result
selesai

// Test function
fungsi fibonacci(n):
    jika n <= 1
        hasil n
    selesai
    hasil fibonacci(n-1) + fibonacci(n-2)
selesai

// Usage
result = ukur_waktu_eksekusi(fibonacci, 35)
tampilkan f"Fibonacci(35) = {result}"
```

## Date Format Codes

Common format codes for `strptime()`:

- `%Y`: 4-digit year (2024)
- `%y`: 2-digit year (24)
- `%m`: Month as number (01-12)
- `%B`: Full month name (January)
- `%b`: Abbreviated month name (Jan)
- `%d`: Day of month (01-31)
- `%A`: Full weekday name (Monday)
- `%a`: Abbreviated weekday name (Mon)
- `%H`: Hour (24-hour clock, 00-23)
- `%I`: Hour (12-hour clock, 01-12)
- `%M`: Minute (00-59)
- `%S`: Second (00-59)
- `%p`: AM/PM
- `%f`: Microseconds

## Time Constants and Properties

```python
dari datetime impor datetime, time, date

// datetime properties
dt = datetime.sekarang()
tampilkan dt.tahun           // Year
tampilkan dt.bulan           // Month (1-12)
tampilkan dt.hari            // Day (1-31)
tampilkan dt.jam             // Hour (0-23)
tampilkan dt.menit           // Minute (0-59)
tampilkan dt.detik           // Second (0-59)
tampilkan dt.microsecond     // Microsecond (0-999999)
tampilkan dt.weekday()       // Day of week (0=Monday, 6=Sunday)

// date properties
d = date.hari_ini()
tampilkan d.tahun
tampilkan d.bulan
tampilkan d.hari
tampilkan d.weekday()

// time properties
t = time(14, 30, 45, 123456)
tampilkan t.jam
tampilkan t.menit
tampilkan t.detik
tampilkan t.microsecond
```