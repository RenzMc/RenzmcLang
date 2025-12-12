# Modul File I/O

Modul File I/O menyediakan fungsi-fungsi untuk operasi file I/O, mengikuti standar operasi file Python dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari fileio impor read_text, write_text, copy, move, delete
// atau gunakan alias Indonesia
dari fileio impor baca_teks, tulis_teks, salin, pindahkan, hapus
// atau impor semua
dari fileio impor *
```

## Fungsi Membaca File

### read_text() / baca_teks()

Baca file sebagai text.

**Sintaks:**
```python
read_text(path_file, encoding)
baca_teks(path_file, encoding)
```

**Parameter:**
- `path_file` (string): Path file yang akan dibaca
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Mengembalikan:**
- String: Konten file sebagai text

**Contoh:**
```python
dari fileio import baca_teks

// Baca file text sederhana
konten itu baca_teks("data.txt")
tampilkan konten

// Baca dengan encoding tertentu
konten_utf16 it baca_teks("data.txt", encoding="utf-16")
tampilkan konten_utf16

// Baca dan proses line by line
konten it baca_teks("artikel.txt")
baris-baris it pisah(konten, "\n")
tampilkan f"Jumlah baris: {panjang(baris-baris)}"
```

**Error:**
- Melempar `FileNotFoundError` jika file tidak ada
- Melempar `UnicodeDecodeError` jika encoding tidak cocok

---

### read_lines() / baca_baris()

Baca file sebagai list of lines.

**Sintaks:**
```python
read_lines(path_file, encoding)
baca_baris(path_file, encoding)
```

**Parameter:**
- `path_file` (string): Path file yang akan dibaca
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Mengembalikan:**
- List: List berisi setiap baris dari file

**Contoh:**
```python
dari fileio import baca_baris

// Baca semua baris
baris it baca_baris("data.txt")
tampilkan baris  // Output: ["baris1\n", "baris2\n", "baris3"]

// Hitung total baris
jumlah_baris it panjang(baris)
tampilkan f"Total baris: {jumlah_baris}"

// Proses setiap baris
untuk setiap baris_data dari baris
    // Hapus newline character
    baris_bersih it hapus_spasi(baris_data)
    tampilkan f"Baris: {baris_bersih}"
selesai

// Baca file CSV dengan parsing manual
csv_baris it baca_baris("data.csv")
untuk setiap baris_csv dari csv_baris
    kolom it pisah(hapus_spasi(baris_csv), ",")
    tampilkan kolom
selesai
```

---

### read_bytes() / baca_bytes()

Baca file sebagai bytes.

**Sintaks:**
```python
read_bytes(path_file)
baca_bytes(path_file)
```

**Parameter:**
- `path_file` (string): Path file yang akan dibaca

**Mengembalikan:**
- Bytes: Konten file sebagai bytes

**Contoh:**
```python
dari fileio import baca_bytes

// Baca file binary
data_gambar it baca_bytes("foto.jpg")
tampilkan f"Ukuran gambar: {panjang(data_gambar)} bytes"

// Baca dan proses binary data
data it baca_bytes("data.bin")
untuk i dari 0 hingga panjang(data) - 1
    tampilkan f"Byte {i}: {data[i]}"
selesai

// Simpan ke file baru (backup)
dari fileio import tulis_bytes
tulis_bytes("backup.bin", data)
```

---

### read_json() / baca_json()

Baca file JSON.

**Sintaks:**
```python
read_json(path_file, encoding)
baca_json(path_file, encoding)
```

**Parameter:**
- `path_file` (string): Path file JSON yang akan dibaca
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Mengembalikan:**
- Dictionary: Hasil parsing JSON

**Contoh:**
```python
dari fileio import baca_json

// Baca konfigurasi
config it baca_json("config.json")
tampilkan f"App name: {config['app_name']}"
tampilkan f"Version: {config['version']}"

// Baca data users
users it baca_json("users.json")
tampilkan f"Total users: {panjang(users)}"

untuk setiap user dari users
    tampilkan f"User: {user['name']} ({user['email']})"
selesai

// Baca dengan default value
coba
    settings it baca_json("settings.json")
    debug_mode it settings.get("debug", salah)
    port it settings.get("port", 8080)
kecuali Exception sebagai e
    tampilkan f"Error reading settings: {e}"
    // Gunakan default values
    debug_mode it salah
    port it 8080
selesai
```

---

### read_csv() / baca_csv()

Baca file CSV.

**Sintaks:**
```python
read_csv(path_file, delimiter, encoding)
baca_csv(path_file, delimiter, encoding)
```

**Parameter:**
- `path_file` (string): Path file CSV yang akan dibaca
- `delimiter` (string, opsional): Delimiter (default: ",")
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Mengembalikan:**
- List: List of rows (setiap row adalah list of strings)

**Contoh:**
```python
dari fileio import baca_csv

// Baca CSV standar
data it baca_csv("data.csv")
header it data[0]  // Baris pertama sebagai header
rows it data[1:]   // Data rows

tampilkan "Header:"
tampilkan header

tampilkan "Data:"
untuk setiap row dari rows
    tampilkan row
selesai

// Baca CSV dengan delimiter kustom
semicolon_data it baca_csv("data.csv", delimiter=";")
tampilkan semicolon_data

// Baca CSV dengan tab delimiter
tab_data it baca_csv("data.tsv", delimiter="\t")
tampilkan tab_data
```

## Fungsi Menulis File

### write_text() / tulis_teks()

Tulis text ke file.

**Sintaks:**
```python
write_text(path_file, konten, encoding)
tulis_teks(path_file, konten, encoding)
```

**Parameter:**
- `path_file` (string): Path file yang akan ditulis
- `konten` (string): Text konten yang akan ditulis
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Contoh:**
```python
dari fileio import tulis_teks

// Tulis text sederhana
tulis_teks("hello.txt", "Hello, World!")

// Tulis multi-line text
artikel it "Judul Artikel\n\nIni adalah paragraf pertama.\nIni adalah paragraf kedua."
tulis_teks("artikel.txt", artikel)

// Tulis dengan formatting
nama it "Budi Santoso"
umur it 25
bio it f"Nama: {nama}\nUmur: {umur}\nStatus: Aktif"
tulis_teks("profile.txt", bio)

// Append ke file (baca dulu, lalu tulis)
coba
    existing_konten it baca_teks("log.txt")
kecuali FileNotFoundError
    existing_konten it ""
selesai

log_baru it f"\n{waktu()}: User login"  // Asumsi ada fungsi waktu()
tulis_teks("log.txt", existing_konten + log_baru)
```

---

### write_lines() / tulis_baris()

Tulis list of lines ke file.

**Sintaks:**
```python
write_lines(path_file, baris-baris, encoding)
tulis_baris(path_file, baris-baris, encoding)
```

**Parameter:**
- `path_file` (string): Path file yang akan ditulis
- `baris-baris` (list): List of lines yang akan ditulis
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Contoh:**
```python
dari fileio import tulis_baris

// Tulis list sederhana
lines it ["Line 1\n", "Line 2\n", "Line 3"]
tulis_baris("output.txt", lines)

// Generate dan tulis lines
data_lines it []
untuk i dari 1 hingga 10
    tambah(data_lines, f"Data item {i}\n")
selesai
tulis_baris("data.txt", data_lines)

// Tulis CSV manual
csv_data it []
tambah(csv_data, "Name,Age,City\n")  // Header
tambah(csv_data, "Alice,25,Jakarta\n")
tambah(csv_data, "Bob,30,Bandung\n")
tambah(csv_data, "Charlie,28,Surabaya\n")
tulis_baris("manual.csv", csv_data)
```

---

### write_bytes() / tulis_bytes()

Tulis bytes ke file.

**Sintaks:**
```python
write_bytes(path_file, konten)
tulis_bytes(path_file, konten)
```

**Parameter:**
- `path_file` (string): Path file yang akan ditulis
- `konten` (bytes): Bytes konten yang akan ditulis

**Contoh:**
```python
dari fileio import tulis_bytes, baca_bytes

// Tulis binary data
binary_data it b"\x00\x01\x02\x03\x04\x05"
tulis_bytes("binary.bin", binary_data)

// Create simple image header (mock)
image_header it b"\x89PNG\r\n\x1a\n"
tulis_bytes("image.png", image_header)

// Copy dan modify bytes
original_data it baca_bytes("input.bin")
// Modify first byte
modified_data it bytes([0xFF] + list(original_data[1:]))
tulis_bytes("modified.bin", modified_data)
```

---

### write_json() / tulis_json()

Tulis data ke JSON file.

**Sintaks:**
```python
write_json(path_file, data, indent, encoding)
tulis_json(path_file, data, indent, encoding)
```

**Parameter:**
- `path_file` (string): Path file JSON yang akan ditulis
- `data` (dict): Data yang akan ditulis
- `indent` (integer, opsional): Indentasi untuk pretty printing
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Contoh:**
```python
dari fileio import tulis_json

// Tulis JSON sederhana
user_data it {"name": "David", "age": 30, "city": "Medan"}
tulis_json("user.json", user_data)

// Tulis dengan indentasi
config it {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": true,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    }
}
tulis_json("config.json", config, indent=2)

// Tulis array/list
products it [
    {"id": 1, "name": "Laptop", "price": 8500000},
    {"id": 2, "name": "Mouse", "price": 250000},
    {"id": 3, "name": "Keyboard", "price": 450000}
]
tulis_json("products.json", products, indent=4)
```

---

### write_csv() / tulis_csv()

Tulis data ke CSV file.

**Sintaks:**
```python
write_csv(path_file, rows, delimiter, encoding)
tulis_csv(path_file, rows, delimiter, encoding)
```

**Parameter:**
- `path_file` (string): Path file CSV yang akan ditulis
- `rows` (list): List of rows
- `delimiter` (string, opsional): Delimiter (default: ",")
- `encoding` (string, opsional): Encoding file (default: "utf-8")

**Contoh:**
```python
dari fileio import tulis_csv

// Tulis CSV sederhana
csv_data it [
    ["Name", "Age", "City"],
    ["Eva", "25", "Jakarta"],
    ["Frank", "30", "Bandung"],
    ["Grace", "28", "Surabaya"]
]
tulis_csv("users.csv", csv_data)

// Tulis dengan delimiter kustom
semicolon_data it [
    ["Product"; "Price"; "Stock"],
    ["Laptop"; "8500000"; "10"],
    ["Mouse"; "250000"; "50"],
    ["Keyboard"; "450000"; "25"]
]
tulis_csv("products.csv", semicolon_data, delimiter=";")

// Generate CSV dari data dinamis
sales_data it [["Date", "Product", "Amount", "Total"]]
// Add sample data
tambah(sales_data, ["2025-01-01", "Laptop", 2, 17000000])
tambah(sales_data, ["2025-01-02", "Mouse", 5, 1250000])
tambah(sales_data, ["2025-01-03", "Keyboard", 3, 1350000])
tulis_csv("sales_report.csv", sales_data)
```

## Operasi File

### copy() / salin()

Salin file dari source ke destination.

**Sintaks:**
```python
copy(source, destination)
salin(source, destination)
```

**Parameter:**
- `source` (string): Path file sumber
- `destination` (string): Path file tujuan

**Contoh:**
```python
dari fileio import salin

// Salin file
salin("data.txt", "backup/data.txt")

// Salin dengan nama baru
salin("config.json", "config_backup.json")

// Salin ke directory berbeda
salin("report.pdf", "archives/report_2025.pdf")
```

---

### move() / pindahkan()

Pindahkan file dari source ke destination.

**Sintaks:**
```python
move(source, destination)
pindahkan(source, destination)
```

**Parameter:**
- `source` (string): Path file sumber
- `destination` (string): Path file tujuan

**Contoh:**
```python
dari fileio import pindahkan

// Pindahkan file
pindahkan("temp.txt", "processed/temp.txt")

// Rename file
pindahkan("old_name.txt", "new_name.txt")

// Pindahkan ke directory lain
pindahkan("output.csv", "reports/monthly_report.csv")
```

---

### delete() / hapus()

Hapus file.

**Sintaks:**
```python
delete(path_file)
hapus(path_file)
```

**Parameter:**
- `path_file` (string): Path file yang akan dihapus

**Contoh:**
```python
dari fileio import hapus, ada

// Hapus file
hapus("temp_file.txt")

// Hapus dengan cek keberadaan
jika ada("old_data.csv")
    hapus("old_data.csv")
    tampilkan "File old_data.csv dihapus"
lainnya
    tampilkan "File old_data.csv tidak ditemukan"
selesai

// Cleanup temporary files
temp_files it ["temp1.txt", "temp2.dat", "temp3.bin"]
untuk setiap temp_file dari temp_files
    jika ada(temp_file)
        hapus(temp_file)
        tampilkan f"File {temp_file} dihapus"
    selesai
selesai
```

---

### exists() / ada()

Cek apakah file atau directory ada.

**Sintaks:**
```python
exists(path)
ada(path)
```

**Parameter:**
- `path` (string): Path yang akan dicek

**Mengembalikan:**
- Boolean: True jika ada, False jika tidak

**Contoh:**
```python
dari fileio import ada

// Cek file
jika ada("config.json")
    tampilkan "File config.json ada"
lainnya
    tampilkan "File config.json tidak ada"
selesai

// Cek directory
jika ada("data/")
    tampilkan "Directory data ada"
lainnya
    tampilkan "Directory data tidak ada"
selesai

// Cek sebelum operasi file
filename it "important_data.txt"
jika tidak ada(filename)
    // Buat file baru
    dari fileio import tulis_teks
    tulis_teks(filename, "Initial data")
    tampilkan f"File {filename} dibuat"
lainnya
    tampilkan f"File {filename} sudah ada"
selesai
```

---

### size() / ukuran()

Dapatkan ukuran file dalam bytes.

**Sintaks:**
```python
size(path_file)
ukuran(path_file)
```

**Parameter:**
- `path_file` (string): Path file

**Mengembalikan:**
- Integer: Ukuran file dalam bytes

**Contoh:**
```python
dari fileio import ukuran, ada

// Dapatkan ukuran file
jika ada("data.txt")
    file_size it ukuran("data.txt")
    tampilkan f"Ukuran file: {file_size} bytes"
    
    // Konversi ke KB
    size_kb it file_size / 1024
    tampilkan f"Ukuran file: {size_kb:.2f} KB"
selesai

// Monitor file sizes
files it ["data1.txt", "data2.txt", "data3.txt"]
total_size it 0
untuk setiap file dari files
    jika ada(file)
        file_size it ukuran(file)
        total_size it total_size + file_size
        tampilkan f"{file}: {file_size} bytes"
    selesai
selesai
tampilkan f"Total ukuran: {total_size} bytes"
```

---

### is_file() / adalah_file()

Cek apakah path adalah file.

**Sintaks:**
```python
is_file(path)
adalah_file(path)
```

**Parameter:**
- `path` (string): Path yang akan dicek

**Mengembalikan:**
- Boolean: True jika file, False jika tidak

**Contoh:**
```python
dari fileio import adalah_file

// Cek apakah path adalah file
jika adalah_file("data.txt")
    tampilkan "data.txt adalah file"
lainnya
    tampilkan "data.txt bukan file"
selesai

// Filter files dari directory listing
all_items it ["data.txt", "logs", "config.json", "temp"]
files it []
untuk setiap item dari all_items
    jika adalah_file(item)
        tambah(files, item)
    selesai
selesai
tampilkan f"Files: {files}"
```

---

### is_dir() / adalah_dir()

Cek apakah path adalah directory.

**Sintaks:**
```python
is_dir(path)
adalah_dir(path)
```

**Parameter:**
- `path` (string): Path yang akan dicek

**Mengembalikan:**
- Boolean: True jika directory, False jika tidak

**Contoh:**
```python
dari fileio import adalah_dir

// Cek apakah path adalah directory
jika adalah_dir("data/")
    tampilkan "data adalah directory"
lainnya
    tampilkan "data bukan directory"
selesai

// Filter directories
items it ["data", "file.txt", "logs", "config.json"]
directories it []
untuk setiap item dari items
    jika adalah_dir(item)
        tambah(directories, item)
    selesai
selesai
tampilkan f"Directories: {directories}"
```

## Operasi Directory

### create_dir() / buat_dir()

Buat directory.

**Sintaks:**
```python
create_dir(path_dir, exist_ok)
buat_dir(path_dir, exist_ok)
```

**Parameter:**
- `path_dir` (string): Path directory yang akan dibuat
- `exist_ok` (boolean, opsional): Tidak error jika directory sudah ada (default: True)

**Contoh:**
```python
dari fileio import buat_dir

// Buat directory sederhana
buat_dir("data")

// Buat nested directory
buat_dir("data/processed/2025")

// Buat dengan error handling
coba
    buat_dir("logs", exist_ok=salah)  // Akan error jika sudah ada
    tampilkan "Directory logs dibuat"
kecuali Exception sebagai e
    tampilkan f"Error: {e}"
selesai

// Buat struktur directory lengkap
directories it [
    "data",
    "data/input",
    "data/output", 
    "data/temp",
    "logs",
    "config"
]
untuk setiap dir dari directories
    buat_dir(dir)
    tampilkan f"Directory {dir} dibuat"
selesai
```

---

### remove_dir() / hapus_dir()

Hapus directory dan semua isinya.

**Sintaks:**
```python
remove_dir(path_dir, ignore_errors)
hapus_dir(path_dir, ignore_errors)
```

**Parameter:**
- `path_dir` (string): Path directory yang akan dihapus
- `ignore_errors` (boolean, opsional): Abaikan error saat penghapusan (default: False)

**Contoh:**
```python
dari fileio import hapus_dir, adalah_dir

// Hapus directory
hapus_dir("temp")

// Hapus dengan error handling
coba
    hapus_dir("logs", ignore_errors=salah)
    tampilkan "Directory logs dihapus"
kecuali Exception sebagai e
    tampilkan f"Error: {e}"
selesai

// Cleanup temporary directories
temp_dirs it ["temp1", "temp2", "temp3"]
untuk setiap temp_dir dari temp_dirs
    jika adalah_dir(temp_dir)
        hapus_dir(temp_dir, ignore_errors=benar)
        tampilkan f"Directory {temp_dir} dihapus"
    selesai
selesai
```

---

### list_dir() / daftar_dir()

Daftar file dan directory dalam directory.

**Sintaks:**
```python
list_dir(path_dir)
daftar_dir(path_dir)
```

**Parameter:**
- `path_dir` (string, opsional): Path directory (default: current directory)

**Mengembalikan:**
- List: List nama file dan directory

**Contoh:**
```python
dari fileio import daftar_dir, adalah_file, adalah_dir

// Daftar current directory
items it daftar_dir(".")
tampilkan items

// Daftar directory tertentu
data_items it daftar_dir("data")
tampilkan f"Isi directory data: {data_items}"

// Filter files dan directories
files it []
directories it []
untuk setiap item dari data_items
    full_path it "data/" + item
    jika adalah_file(full_path)
        tambah(files, item)
    selesai
    jika adalah_dir(full_path)
        tambah(directories, item)
    selesai
selesai
tampilkan f"Files: {files}"
tampilkan f"Directories: {directories}"

// Recursive listing
buat fungsi list_recursive dengan path
    items it daftar_dir(path)
    untuk setiap item dari items
        full_path it path + "/" + item
        tampilkan full_path
        jika adalah_dir(full_path)
            list_recursive(full_path)
        selesai
    selesai
selesai

list_recursive("data")
```

---

### walk_dir() / jelajahi_dir()

Jelajahi directory tree secara rekursif.

**Sintaks:**
```python
walk_dir(path_dir)
jelajahi_dir(path_dir)
```

**Parameter:**
- `path_dir` (string): Root directory

**Mengembalikan:**
- Generator: Menghasilkan tuple (dirpath, dirnames, filenames)

**Contoh:**
```python
dari fileio import jelajahi_dir

// Jelajahi directory
untuk setiap (dirpath, dirnames, filenames) dari jelajahi_dir("data")
    tampilkan f"Directory: {dirpath}"
    
    // Tampilkan subdirectories
    tampilkan "  Subdirectories:"
    untuk setiap dirname dari dirnames
        tampilkan f"    {dirname}"
    selesai
    
    // Tampilkan files
    tampilkan "  Files:"
    untuk setiap filename dari filenames
        tampilkan f"    {filename}"
    selesai
selesai

// Hitung total files
total_files it 0
untuk setiap (dirpath, dirnames, filenames) dari jelajahi_dir(".")
    total_files it total_files + panjang(filenames)
selesai
tampilkan f"Total files: {total_files}"

// Cari file dengan ekstensi tertentu
txt_files it []
untuk setiap (dirpath, dirnames, filenames) dari jelajahi_dir(".")
    untuk setiap filename dari filenames
        jika akhir_dengan(filename, ".txt")
            full_path it dirpath + "/" + filename
            tambah(txt_files, full_path)
        selesai
    selesai
selesai
tampilkan f"Text files: {txt_files}"
```

## Context Manager

### open_text() / buka_teks()

Buka text file dengan mode tertentu.

**Sintaks:**
```python
open_text(path_file, mode, encoding)
buka_teks(path_file, mode, encoding)
```

**Parameter:**
- `path_file` (string): Path file
- `mode` (string, opsional): Mode file ('r', 'w', 'a', etc.) (default: 'r')
- `encoding` (string, opsional): Encoding file (default: 'utf-8')

**Mengembalikan:**
- TextIOWrapper: File object

**Contoh:**
```python
dari fileio import buka_teks

// Buka dan baca file
dengan buka_teks("data.txt", "r") sebagai file
    konten it file.read()
    tampilkan konten
selesai

// Buka dan tulis file
dengan buka_teks("output.txt", "w") sebagai file
    file.write("Hello from context manager")
    file.write("\nThis is line 2")
selesai

// Append ke file
dengan buka_teks("log.txt", "a") sebagai file
    file.write(f"\n{waktu()}: New log entry")
selesai

// Process line by line
dengan buka_teks("large_file.txt", "r") sebagai file
    line_count it 0
    untuk setiap line dari file
        line_count it line_count + 1
        jika line_count % 1000 == 0
            tampilkan f"Processed {line_count} lines"
        selesai
    selesai
selesai
```

---

### open_binary() / buka_binary()

Buka binary file dengan mode tertentu.

**Sintaks:**
```python
open_binary(path_file, mode)
buka_binary(path_file, mode)
```

**Parameter:**
- `path_file` (string): Path file
- `mode` (string, opsional): Mode file ('rb', 'wb', 'ab', etc.) (default: 'rb')

**Mengembalikan:**
- BufferedReader/BufferedWriter: Binary file object

**Contoh:**
```python
dari fileio import buka_binary

// Baca binary file
dengan buka_binary("image.png", "rb") sebagai file
    header it file.read(8)  // Read first 8 bytes
    tampilkan f"Header: {header}"
selesai

// Tulis binary file
data it b"\x00\x01\x02\x03\x04\x05"
dengan buka_binary("output.bin", "wb") sebagai file
    file.write(data)
selesai

// Copy binary file
dengan buka_binary("input.bin", "rb") sebagai source
    dengan buka_binary("output.bin", "wb") sebagai destination
        destination.write(source.read())
    selesai
selesai
```

## Fungsi Utilitas Path

### get_extension() / dapatkan_ekstensi()

Dapatkan file extension.

**Sintaks:**
```python
get_extension(path_file)
dapatkan_ekstensi(path_file)
```

**Parameter:**
- `path_file` (string): Path file

**Mengembalikan:**
- String: File extension (termasuk dot)

**Contoh:**
```python
dari fileio import dapatkan_ekstensi

// Dapatkan ekstensi file
ext1 it dapatkan_ekstensi("data.txt")      // Output: ".txt"
ext2 it dapatkan_ekstensi("image.jpg")     // Output: ".jpg"
ext3 it dapatkan_ekstensi("archive.tar.gz") // Output: ".gz"
ext4 it dapatkan_ekstensi("no_extension")  // Output: ""

tampilkan ext1
tampilkan ext2
tampilkan ext3
tampilkan ext4

// Filter files by extension
files it ["data.txt", "image.jpg", "config.json", "script.py"]
txt_files it []
untuk setiap file dari files
    jika dapatkan_ekstensi(file) == ".txt"
        tambah(txt_files, file)
    selesai
selesai
tampilkan f"Text files: {txt_files}"
```

---

### get_basename() / dapatkan_nama_file()

Dapatkan filename tanpa path.

**Sintaks:**
```python
get_basename(path_file)
dapatkan_nama_file(path_file)
```

**Parameter:**
- `path_file` (string): Path file

**Mengembalikan:**
- String: Filename saja

**Contoh:**
```python
dari fileio import dapatkan_nama_file

// Dapatkan filename
name1 it dapatkan_nama_file("/home/user/data.txt")     // Output: "data.txt"
name2 it dapatkan_nama_file("C:\\Windows\\system32\&quot;) // Output: "system32"
name3 it dapatkan_nama_file("relative/path/file.json") // Output: "file.json"
name4 it dapatkan_nama_file("simple.txt")              // Output: "simple.txt"

tampilkan name1
tampilkan name2
tampilkan name3
tampilkan name4
```

---

### get_stem() / dapatkan_stem()

Dapatkan filename tanpa extension.

**Sintaks:**
```python
get_stem(path_file)
dapatkan_stem(path_file)
```

**Parameter:**
- `path_file` (string): Path file

**Mengembalikan:**
- String: Filename tanpa extension

**Contoh:**
```python
dari fileio import dapatkan_stem

// Dapatkan filename tanpa extension
stem1 it dapatkan_stem("data.txt")           // Output: "data"
stem2 it dapatkan_stem("report.final.pdf")   // Output: "report.final"
stem3 it dapatkan_stem("archive.tar.gz")     // Output: "archive.tar"
stem4 it dapatkan_stem("no_extension")       // Output: "no_extension"

tampilkan stem1
tampilkan stem2
tampilkan stem3
tampilkan stem4

// Generate backup filename
original_file it "important_data.txt"
stem it dapatkan_stem(original_file)
backup_file it stem + "_backup.txt"
tampilkan f"Backup file: {backup_file}"
```

---

### get_parent() / dapatkan_induk()

Dapatkan parent directory.

**Sintaks:**
```python
get_parent(path_file)
dapatkan_induk(path_file)
```

**Parameter:**
- `path_file` (string): Path file

**Mengembalikan:**
- String: Parent directory path

**Contoh:**
```python
dari fileio import dapatkan_induk

// Dapatkan parent directory
parent1 it dapatkan_induk("/home/user/data.txt")     // Output: "/home/user"
parent2 it dapatkan_induk("C:\\Windows\\system32\&quot;) // Output: "C:\\Windows"
parent3 it dapatkan_induk("relative/path/file.json") // Output: "relative/path"
parent4 it dapatkan_induk("simple.txt")              // Output: "."

tampilkan parent1
tampilkan parent2
tampilkan parent3
tampilkan parent4
```

---

### join_paths() / gabungkan_path()

Gabungkan path components.

**Sintaks:**
```python
join_paths(*paths)
gabungkan_path(*paths)
```

**Parameter:**
- `*paths` (string): Path components

**Mengembalikan:**
- String: Joined path

**Contoh:**
```python
dari fileio import gabungkan_path

// Gabungkan path
path1 it gabungkan_path("/home", "user", "data.txt")  // Output: "/home/user/data.txt"
path2 it gabungkan_path("data", "processed", "2025")   // Output: "data/processed/2025"
path3 it gabungkan_path("config", "app.json")         // Output: "config/app.json"

tampilkan path1
tampilkan path2
tampilkan path3

// Dynamic path construction
base_dir it "/home/user/project"
data_dir it gabungkan_path(base_dir, "data")
config_file it gabungkan_path(base_dir, "config", "settings.json")
log_file it gabungkan_path(base_dir, "logs", "app.log")

tampilkan data_dir
tampilkan config_file
tampilkan log_file
```

---

### absolute_path() / path_absolut()

Dapatkan absolute path.

**Sintaks:**
```python
absolute_path(relative_path)
path_absolut(relative_path)
```

**Parameter:**
- `relative_path` (string): Relative path

**Mengembalikan:**
- String: Absolute path

**Contoh:**
```python
dari fileio import path_absolut

// Convert relative ke absolute
abs_path1 it path_absolut("data.txt")
abs_path2 it path_absolut("../config.json")
abs_path3 it path_absolut("./logs/app.log")

tampilkan f"Absolute path: {abs_path1}"
tampilkan f"Absolute path: {abs_path2}"
tampilkan f"Absolute path: {abs_path3}"

// Normalize paths
messy_path it "data/../config/./settings.json"
normalized it path_absolut(messy_path)
tampilkan f"Normalized: {normalized}"
```

## Contoh Praktis

### File Manager Sederhana

```python
dari fileio import *

buat fungsi organize_files dengan source_dir, target_dir
    // Buat target directory structure
    buat_dir(gabungkan_path(target_dir, "documents"))
    buat_dir(gabungkan_path(target_dir, "images"))
    buat_dir(gabungkan_path(target_dir, "configs"))
    
    // Jelajahi source directory
    untuk setiap (dirpath, dirnames, filenames) dari jelajahi_dir(source_dir)
        untuk setiap filename dari filenames
            source_path it gabungkan_path(dirpath, filename)
            extension it dapatkan_ekstensi(filename)
            
            // Tentukan target directory
            jika extension di [".txt", ".doc", ".pdf"]
                target_subdir it "documents"
            selesai
            jika extension di [".jpg", ".png", ".gif", ".bmp"]
                target_subdir it "images"
            selesai
            jika extension di [".json", ".xml", ".yaml"]
                target_subdir it "configs"
            selesai
            lainnya
                target_subdir it "others"
            selesai
            
            // Pindahkan file
            target_path it gabungkan_path(target_dir, target_subdir, filename)
            pindahkan(source_path, target_path)
            tampilkan f"Moved {filename} to {target_subdir}"
        selesai
    selesai
selesai

// Penggunaan
organize_files("messy_files", "organized")
```

### Log File Processor

```python
dari fileio import baca_baris, tulis_teks, dapatkan_ekstensi

buat fungsi process_log_file dengan input_file, output_file
    // Baca semua baris
    lines it baca_baris(input_file)
    
    // Process lines
    processed_lines it []
    error_count it 0
    warning_count it 0
    
    untuk setiap line dari lines
        clean_line it hapus_spasi(line)
        
        // Filter empty lines
        jika panjang(clean_line) > 0
            // Count log levels
            jika berisi(huruf_kecil(clean_line), "error")
                error_count it error_count + 1
            selesai
            jika berisi(huruf_kecil(clean_line), "warning")
                warning_count it warning_count + 1
            selesai
            
            tambah(processed_lines, clean_line)
        selesai
    selesai
    
    // Generate report
    report it f"Log Processing Report\n"
    report it report + f"Input file: {input_file}\n"
    report it report + f"Total lines processed: {panjang(processed_lines)}\n"
    report it report + f"Errors found: {error_count}\n"
    report it report + f"Warnings found: {warning_count}\n"
    report it report + "\nProcessed Log:\n"
    
    // Add processed lines
    untuk setiap line dari processed_lines
        report it report + line + "\n"
    selesai
    
    // Write output
    tulis_teks(output_file, report)
    tampilkan f"Log processing completed. Results saved to {output_file}"
selesai

// Penggunaan
process_log_file("app.log", "processed_log.txt")
```

### Configuration Backup System

```python
dari fileio import baca_json, tulis_json, ada, salin, buat_dir
dari datetime import sekarang

buat fungsi backup_config dengan config_file, backup_dir
    // Pastikan config file ada
    jika tidak ada(config_file)
        tampilkan f"Config file {config_file} tidak ada"
        hasil salah
    selesai
    
    // Buat backup directory
    buat_dir(backup_dir)
    
    // Baca config
    coba
        config it baca_json(config_file)
    kecuali Exception sebagai e
        tampilkan f"Error reading config: {e}"
        hasil salah
    selesai
    
    // Generate backup filename dengan timestamp
    current_time it sekarang()
    timestamp it ganti(str(current_time), ":", "-")  // Ganti colon dengan dash
    backup_filename it f"config_backup_{timestamp}.json"
    backup_path it gabungkan_path(backup_dir, backup_filename)
    
    // Add backup metadata
    backup_config it {
        "original_file": config_file,
        "backup_time": str(current_time),
        "config_data": config
    }
    
    // Write backup
    coba
        tulis_json(backup_path, backup_config, indent=2)
        tampilkan f"Config backed up to {backup_path}"
        
        // Also copy original file
        original_backup it gabungkan_path(backup_dir, dapatkan_nama_file(config_file))
        salin(config_file, original_backup)
        
        hasil benar
    kecuali Exception sebagai e
        tampilkan f"Error creating backup: {e}"
        hasil salah
    selesai
selesai

// Penggunaan
backup_config("app_config.json", "backups")
```

### Data Export System

```python
dari fileio import tulis_csv, tulis_json, tulis_teks, gabungkan_path
dari datetime import sekarang

buat fungsi export_data dengan data, export_dir, format_type
    // Buat export directory
    buat_dir(export_dir)
    
    // Generate filename dengan timestamp
    timestamp it ganti(str(sekarang()), ":", "-")
    
    // Export based on format
    jika format_type == "csv"
        filename it f"data_export_{timestamp}.csv"
        filepath it gabungkan_path(export_dir, filename)
        
        // Convert data ke CSV format
        csv_data it []
        // Add header
        jika panjang(data) > 0 dan jenis(data[0]) == "dict"
            header it kunci(data[0])
            tambah(csv_data, header)
            
            // Add rows
            untuk setiap row dari data
                row_data it []
                untuk setiap key dari header
                    tambah(row_data, str(row.get(key, "")))
                selesai
                tambah(csv_data, row_data)
            selesai
        lainnya
            // Simple list data
            tambah(csv_data, ["value"])
            untuk setiap item dari data
                tambah(csv_data, [str(item)])
            selesai
        selesai
        
        tulis_csv(filepath, csv_data)
        tampilkan f"Data exported to CSV: {filepath}"
        
    selesai
    
    jika format_type == "json"
        filename it f"data_export_{timestamp}.json"
        filepath it gabungkan_path(export_dir, filename)
        
        export_data it {
            "export_time": str(sekarang()),
            "total_records": panjang(data),
            "data": data
        }
        
        tulis_json(filepath, export_data, indent=2)
        tampilkan f"Data exported to JSON: {filepath}"
        
    selesai
    
    jika format_type == "txt"
        filename it f"data_export_{timestamp}.txt"
        filepath it gabungkan_path(export_dir, filename)
        
        // Generate text report
        report it f"Data Export Report\n"
        report it report + f"Generated: {sekarang()}\n"
        report it report + f"Total Records: {panjang(data)}\n"
        report it report + "\nData:\n"
        
        untuk setiap i, item dari enumerate(data)
            report it report + f"{i + 1}. {item}\n"
        selesai
        
        tulis_teks(filepath, report)
        tampilkan f"Data exported to TXT: {filepath}"
        
    selesai
    
    hasil filepath
selesai

// Sample data
user_data it [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 28}
]

// Export ke berbagai format
export_data(user_data, "exports", "csv")
export_data(user_data, "exports", "json")
export_data(user_data, "exports", "txt")
```