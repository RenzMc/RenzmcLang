# Panduan Instalasi

## 📦 Menginstal RenzMcLang

RenzMcLang adalah bahasa pemrograman berbasis Python dengan sintaks Bahasa Indonesia. Ikuti langkah-langkah berikut untuk menginstalnya di sistem Anda.

### Prasyarat

- Python 3.8 atau lebih tinggi
- pip (pengelola paket Python)

### Metode Instalasi

#### Metode 1: Instal dari PyPI (Direkomendasikan)

```bash
pip install renzmc
```

#### Metode 2: Instal dari Sumber

```bash
# Klon repositori
git clone https://github.com/yourusername/RenzMcLang.git
cd RenzMcLang

# Instal dependensi
pip install -r requirements.txt

# Instal paket
pip install -e .
```

### Verifikasi Instalasi

Setelah instalasi, verifikasi bahwa RenzMcLang terinstal dengan benar:

```bash
rmc --version
```

Anda akan melihat output seperti:
```
RenzmcLang 1.0.0
```

### Menjalankan Program Pertama Anda

Buat file bernama `hello.rmc`:

```python
tampilkan "Hello, World!"
```

Jalankan:

```bash
rmc hello.rmc
```

Output:
```
Hello, World!
```

### Mode Interaktif (REPL)

Mulai interpreter interaktif:

```bash
rmc
```

Anda akan melihat:

```
RenzmcLang 1.0.0 - Bahasa pemrograman berbasis Bahasa Indonesia
Ketik 'keluar' untuk keluar dari interpreter.

>>> 
```

Coba beberapa perintah:

```python
>>> tampilkan "Halo!"
Halo!
>>> angka itu 42
>>> tampilkan angka
42
>>> keluar
```

### Opsi Baris Perintah

RenzMcLang mendukung beberapa opsi baris perintah:

```bash
# Jalankan file
rmc script.rmc

# Jalankan kode secara langsung
rmc -c "tampilkan 'Hello'"

# Tampilkan versi
rmc --version

# Mode interaktif (default ketika tidak ada argumen)
rmc
```

### Dependensi

RenzMcLang membutuhkan paket Python berikut:

- `aiohttp>=3.8.1` - Untuk operasi HTTP asinkron
- `requests>=2.27.1` - Untuk permintaan HTTP
- `cryptography>=36.0.0` - Untuk fitur enkripsi
- `python-dateutil>=2.8.2` - Untuk operasi tanggal/waktu
- `pytz>=2021.3` - Untuk dukungan zona waktu
- `pyyaml>=6.0` - Untuk penguraian YAML
- `ujson>=5.1.0` - Untuk operasi JSON cepat
- `regex>=2022.1.18` - Untuk dukungan regex lanjutan

Semua ini otomatis diinstal saat Anda menginstal RenzMcLang melalui pip.

### Pemecahan Masalah

#### "rmc: command not found"

Jika Anda mendapatkan error ini, pastikan direktori skrip Python ada di PATH Anda:

**Linux/macOS:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Windows:**
Tambahkan `%APPDATA%\Python\Scripts` ke variabel lingkungan PATH Anda.

#### Error Impor

Jika Anda mengalami error impor, instal ulang dependensi:

```bash
pip install --upgrade -r requirements.txt
```

#### Error Izin

Pada Linux/macOS, Anda mungkin perlu menggunakan `pip install --user`:

```bash
pip install --user renzmc
```

### Menghapus Instalasi

Untuk menghapus instalasi RenzMcLang:

```bash
pip uninstall renzmc
```

### Langkah Selanjutnya

- Baca panduan [Dasar-dasar Sintaks](syntax-basics.md)
- Jelajahi [Fungsi Bawaan](builtin-functions.md)
- Lihat [Contoh](examples.md)
- Pelajari tentang [Integrasi Python](python-integration.md)

---

**Butuh Bantuan?** Kunjungi [repositori GitHub](https://github.com/yourusername/RenzMcLang) kami atau buka issue.