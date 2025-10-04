# Integrasi Python

## 🔌 Pengenalan

Salah satu fitur paling kuat dari RenzMcLang adalah integrasi yang mulus dengan Python. Anda dapat mengimpor dan menggunakan pustaka Python apa pun, mengakses objek Python, dan memanggil fungsi Python langsung dari kode RenzMcLang.

## 📑 Daftar Isi

- [Mengimpor Modul Python](#mengimpor-modul-python)
- [Memanggil Fungsi Python](#memanggil-fungsi-python)
- [Mengakses Objek Python](#mengakses-objek-python)
- [Menggunakan Pustaka Python](#menggunakan-pustaka-python)
- [Contoh Web Scraping](#contoh-web-scraping)
- [Contoh Analisis Data](#contoh-analisis-data)
- [Integrasi Database](#integrasi-database)
- [Praktik Terbaik](#praktik-terbaik)

---

## Mengimpor Modul Python

Gunakan `impor_python` untuk mengimpor modul Python:

```python
// Impor modul tunggal
impor_python "math"
impor_python "os"
impor_python "sys"

// Impor pustaka populer
impor_python "requests"
impor_python "json"
impor_python "datetime"
impor_python "sqlite3"
```

---

## Memanggil Fungsi Python

Gunakan `panggil_python` untuk memanggil fungsi Python:

```python
impor_python "math"

// Panggil fungsi Python
hasil itu panggil_python math.sqrt(16)
tampilkan hasil  // Output: 4.0

// Panggil dengan beberapa argumen
power itu panggil_python math.pow(2, 3)
tampilkan power  // Output: 8.0

// Akses konstanta
pi itu math.pi
tampilkan pi  // Output: 3.141592653589793
```

---

## Mengakses Objek Python

Akses properti dan metode objek Python:

```python
impor_python "datetime"

// Buat objek Python
sekarang itu panggil_python datetime.datetime.now()

// Akses properti
tahun itu sekarang.year
bulan itu sekarang.month
hari itu sekarang.day

tampilkan f"Tanggal: {hari}/{bulan}/{tahun}"

// Panggil metode
formatted itu panggil_python sekarang.strftime("%Y-%m-%d %H:%M:%S")
tampilkan formatted
```

---

## Menggunakan Pustaka Python

### Contoh 1: HTTP Requests

```python
impor_python "requests"

// Buat permintaan GET
response itu panggil_python requests.get("https://api.github.com")

// Akses properti respons
status itu response.status_code
text itu response.text

tampilkan f"Status: {status}"
tampilkan f"Panjang respons: {panjang(text)} karakter"

// Parse respons JSON
data itu panggil_python response.json()
tampilkan data
```

### Contoh 2: Operasi File

```python
impor_python "os"

// Dapatkan direktori saat ini
cwd itu panggil_python os.getcwd()
tampilkan f"Direktori saat ini: {cwd}"

// Daftar file
files itu panggil_python os.listdir(".")
tampilkan "File:"
untuk setiap file dari files
    tampilkan f"  - {file}"
selesai

// Periksa apakah path ada
exists itu panggil_python os.path.exists("data.txt")
tampilkan f"File ada: {exists}"
```

### Contoh 3: Pemrosesan JSON

```python
impor_python "json"

// Buat data
data itu {
    "nama": "Budi",
    "umur": 25,
    "hobi": ["coding", "gaming"]
}

// Konversi ke string JSON
json_str itu panggil_python json.dumps(data)
tampilkan json_str

// Parse string JSON
parsed itu panggil_python json.loads(json_str)
tampilkan parsed["nama"]
```

---

## Contoh Web Scraping

Contoh lengkap web scraping menggunakan requests:

```python
// Impor pustaka
impor_python "requests"

tampilkan "=== Contoh Web Scraping ==="
tampilkan ""

// Buat permintaan HTTP
tampilkan "Membuat permintaan ke example.com..."
response itu panggil_python requests.get("https://example.com")

// Dapatkan kode status
status itu response.status_code
tampilkan f"✓ Kode Status: {status}"

// Dapatkan teks respons
text itu response.text
text_length itu panjang(text)
tampilkan f"✓ Panjang Respons: {text_length} karakter"

// Dapatkan header
headers itu response.headers
tampilkan "✓ Header diterima"

tampilkan ""
tampilkan "✓ Web scraping berhasil diselesaikan!"
```

---

## Contoh Analisis Data

Menggunakan Python untuk analisis data:

```python
// Impor pustaka
impor_python "statistics"

tampilkan "=== Contoh Analisis Data ==="
tampilkan ""

// Data sampel
data itu [23, 45, 67, 89, 12, 34, 56, 78, 90]

// Hitung statistik
mean itu panggil_python statistics.mean(data)
median itu panggil_python statistics.median(data)
stdev itu panggil_python statistics.stdev(data)

tampilkan f"Rata-rata: {mean}"
tampilkan f"Median: {median}"
tampilkan f"Standar Deviasi: {stdev}"
```

---

## Integrasi Database

### Contoh SQLite

```python
impor_python "sqlite3"

// Hubungkan ke database
conn itu panggil_python sqlite3.connect("database.db")
cursor itu panggil_python conn.cursor()

// Buat tabel
panggil_python cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

// Masukkan data
panggil_python cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Budi", 25))
panggil_python conn.commit()

// Query data
panggil_python cursor.execute("SELECT * FROM users")
results itu panggil_python cursor.fetchall()

untuk setiap row dari results
    tampilkan f"ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}"
selesai

// Tutup koneksi
panggil_python conn.close()
```

---

## Praktik Terbaik

### 1. Impor di Bagian Atas

```python
// ✓ Baik: Impor di bagian atas
impor_python "requests"
impor_python "json"
impor_python "os"

// Kode Anda di sini...
```

### 2. Penanganan Error

```python
impor_python "requests"

coba
    response itu panggil_python requests.get("https://api.example.com")
    tampilkan response.status_code
tangkap Exception sebagai e:
    tampilkan f"Error: {e}"
selesai
```

### 3. Periksa Ketersediaan Modul

```python
coba
    impor_python "pandas"
    tampilkan "✓ Pandas tersedia"
tangkap ImportError:
    tampilkan "✗ Pandas tidak terinstal"
    tampilkan "Instal dengan: pip install pandas"
selesai
```

### 4. Gunakan Fungsi Bawaan Bila Memungkinkan

```python
// ✓ Baik: Gunakan fungsi bawaan RenzMcLang
data itu baca_file("data.txt")

// ✗ Kurang efisien: Gunakan Python
impor_python "builtins"
file itu panggil_python builtins.open("data.txt", "r")
data itu panggil_python file.read()
```

---

## Pustaka Python yang Tersedia

RenzMcLang dapat menggunakan SEMUA pustaka Python yang terinstal di sistem Anda:

### Pustaka Populer

- **Web**: `requests`, `urllib`, `beautifulsoup4`, `selenium`
- **Data**: `pandas`, `numpy`, `scipy`
- **Database**: `sqlite3`, `pymongo`, `psycopg2`, `mysql-connector`
- **API**: `flask`, `fastapi`, `django`
- **ML/AI**: `tensorflow`, `pytorch`, `scikit-learn`
- **Gambar**: `pillow`, `opencv-python`
- **Dan banyak lagi!**

### Menginstal Pustaka

```python
# Instal via pip
pip install requests
pip install pandas
pip install beautifulsoup4
```

---

## Ringkasan

Integrasi Python RenzMcLang menyediakan:

- ✅ Akses penuh ke ekosistem Python
- ✅ Impor modul Python apa pun
- ✅ Panggil fungsi Python dengan mulus
- ✅ Akses objek dan properti Python
- ✅ Gunakan pustaka populer (requests, pandas, dll.)
- ✅ Integrasi database (SQLite, MySQL, MongoDB)
- ✅ Web scraping dan panggilan API
- ✅ Analisis dan pemrosesan data

**Seluruh ekosistem Python ada di ujung jari Anda!** 🐍

---

Untuk contoh lebih lanjut, lihat direktori [examples/python_integration](../examples/python_integration/).

**Selamat Coding dengan Python + RenzMcLang! 🚀**