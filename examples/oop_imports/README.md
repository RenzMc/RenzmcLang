# Contoh Sistem Import OOP

Direktori ini berisi contoh lengkap yang menunjukkan sistem import bergaya Python milik RenzMcLang untuk kelas dan fungsi yang tersebar di berbagai folder.

## Struktur Direktori

```
oop_imports/
├── Ren/
│   └── renz.rmc          # Modul dengan kelas Person, Calculator, BankAccount
├── Utils/
│   └── helpers.rmc       # Modul dengan kelas Logger, Validator dan fungsi utilitas
├── 01_basic_import.rmc   # Import dasar tunggal dan multiple
├── 02_multiple_imports.rmc  # Import dari beberapa modul
├── 03_import_with_alias.rmc # Menggunakan alias pada import
└── 04_complex_example.rmc   # Contoh aplikasi dunia nyata

```

## Sintaks Import

### Import Dasar

```rmc
from Ren.renz import buat_Person, Person_perkenalan
```

### Import dengan Alias

```rmc
from Ren.renz import buat_Person as create_person
```

### Import Banyak Sekaligus

```rmc
from Ren.renz import buat_Person, buat_Calculator, buat_BankAccount
```

### Import dari Modul Nested

```rmc
from Utils.helpers import format_currency, buat_Logger
```

## Menjalankan Contoh

```bash
# Jalankan contoh import dasar
renzmc examples/oop_imports/01_basic_import.rmc

# Jalankan contoh multiple imports
renzmc examples/oop_imports/02_multiple_imports.rmc

# Jalankan contoh import dengan alias
renzmc examples/oop_imports/03_import_with_alias.rmc

# Jalankan contoh aplikasi kompleks
renzmc examples/oop_imports/04_complex_example.rmc
```

## Fitur yang Ditunjukkan

1. **Import lintas-folder**: Mengimpor kelas dari direktori yang berbeda.
2. **Path modul bertingkat (nested)**: Menggunakan notasi titik (mis. `Ren.renz`).
3. **Import banyak sekaligus**: Mengimpor beberapa item dalam satu pernyataan.
4. **Alias untuk import**: Mengganti nama import untuk menghindari konflik.
5. **Polapola dunia nyata**: Aplikasi lengkap yang memakai beberapa modul.

## Struktur Modul

### Ren/renz.rmc

Berisi:

* Kelas `Person` (konstruktor, metode)
* Kelas `Calculator` (operasi aritmetika)
* Kelas `BankAccount` (operasi perbankan)
* Fungsi utilitas

### Utils/helpers.rmc

Berisi:

* Kelas `Logger` (fungsi logging)
* Kelas `Validator` (metode validasi)
* Fungsi utilitas formatting

## Catatan

* Semua konstruktor kelas mengikuti konvensi penamaan `buat_ClassName`.
* Semua metode mengikuti konvensi `ClassName_methodName`.
* Pola ini memungkinkan pemrograman gaya OOP yang rapi di RenzMcLang.
* Sistem import mendukung ekstensi file `.rmc` dan `.renzmc`.
