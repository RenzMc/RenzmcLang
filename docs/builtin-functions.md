# Referensi Fungsi Bawaan

RenzMcLang menyediakan 118+ fungsi bawaan untuk tugas pemrograman umum. Semua fungsi tersedia tanpa perlu impor apapun.

## Daftar Isi

- [Fungsi Dasar](#fungsi-dasar)
- [Fungsi String](#fungsi-string)
- [Validasi String](#validasi-string)
- [Fungsi Matematika](#fungsi-matematika)
- [Statistik](#statistik)
- [Fungsi List](#fungsi-list)
- [Fungsi Iterasi](#fungsi-iterasi)
- [Fungsi Dictionary](#fungsi-dictionary)
- [Operasi File](#operasi-file)
- [Operasi Path](#operasi-path)
- [Fungsi Sistem](#fungsi-sistem)
- [JSON & Utilitas](#json--utilitas)
- [Fungsi HTTP](#fungsi-http)

---

## Fungsi Dasar

### `panjang(obj)`

Mendapatkan panjang dari sebuah objek

```python
// Contoh
data itu [1, 2, 3]
hasil itu panjang(data)
```

### `jenis(obj)`

Mendapatkan tipe dari sebuah objek

```python
// Contoh
data itu [1, 2, 3]
hasil itu jenis(data)
```

### `ke_teks(obj)`

Mengkonversi objek menjadi teks

```python
// Contoh
angka itu 123
hasil itu ke_teks(angka)
```

### `ke_angka(obj)`

Mengkonversi objek menjadi angka

```python
// Contoh
teks itu "123"
hasil itu ke_angka(teks)
```

### `ke_float(obj)`

Mengkonversi objek menjadi float

```python
// Contoh
teks itu "123.45"
hasil itu ke_float(teks)
```

### `ke_bool(obj)`

Mengkonversi objek menjadi boolean

```python
// Contoh
teks itu "True"
hasil itu ke_bool(teks)
```

### `ke_list(obj)`

Mengkonversi objek menjadi list

```python
// Contoh
teks itu "abc"
hasil itu ke_list(teks)  // ['a', 'b', 'c']
```

### `ke_tuple(obj)`

Mengkonversi objek menjadi tuple

```python
// Contoh
list itu [1, 2, 3]
hasil itu ke_tuple(list)  // (1, 2, 3)
```

### `ke_set(obj)`

Mengkonversi objek menjadi set

```python
// Contoh
list itu [1, 2, 2, 3]
hasil itu ke_set(list)  // {1, 2, 3}
```

### `ke_dict(obj)`

Mengkonversi objek menjadi dictionary

```python
// Contoh
list itu [["a", 1], ["b", 2]]
hasil itu ke_dict(list)  // {"a": 1, "b": 2}
```

### `cetak(obj)`

Mencetak objek ke konsol

```python
// Contoh
cetak("Hello World")
```

### `input(prompt)`

Mendapatkan input dari pengguna

```python
// Contoh
nama itu input("Masukkan nama: ")
```

### `input_angka(prompt)`

Mendapatkan input angka dari pengguna

```python
// Contoh
umur itu input_angka("Masukkan umur: ")
```

### `range(start, stop, step)`

Membuat range angka

```python
// Contoh
angka itu range(1, 10, 2)  // [1, 3, 5, 7, 9]
```

---

## Fungsi String

### `huruf_besar(text)`

Mengkonversi teks menjadi huruf besar

```python
// Contoh
teks itu "hello"
hasil itu huruf_besar(teks)  // "HELLO"
```

### `huruf_kecil(text)`

Mengkonversi teks menjadi huruf kecil

```python
// Contoh
teks itu "HELLO"
hasil itu huruf_kecil(teks)  // "hello"
```

### `kapital(text)`

Mengkapitalisasi teks

```python
// Contoh
teks itu "hello world"
hasil itu kapital(teks)  // "Hello World"
```

### `potong(text)`

Menghapus spasi di awal dan akhir teks

```python
// Contoh
teks itu "  hello  "
hasil itu potong(teks)  // "hello"
```

### `ganti(text, old, new)`

Mengganti teks

```python
// Contoh
teks itu "hello world"
hasil itu ganti(teks, "world", "dunia")  // "hello dunia"
```

### `pisah(text, separator)`

Memisahkan teks menjadi list

```python
// Contoh
teks itu "a,b,c"
hasil itu pisah(teks, ",")  // ["a", "b", "c"]
```

### `gabung(separator, items)`

Menggabungkan list menjadi teks

```python
// Contoh
list itu ["a", "b", "c"]
hasil itu gabung(",", list)  // "a,b,c"
```

### `awalan(text, prefix)`

Memeriksa apakah teks dimulai dengan awalan tertentu

```python
// Contoh
teks itu "hello world"
hasil itu awalan(teks, "hello")  // benar
```

### `akhiran(text, suffix)`

Memeriksa apakah teks diakhiri dengan akhiran tertentu

```python
// Contoh
teks itu "hello world"
hasil itu akhiran(teks, "world")  // benar
```

### `indeks(text, substring)`

Mendapatkan indeks substring dalam teks

```python
// Contoh
teks itu "hello world"
hasil itu indeks(teks, "world")  // 6
```

### `hitung(text, substring)`

Menghitung jumlah kemunculan substring dalam teks

```python
// Contoh
teks itu "hello hello"
hasil itu hitung(teks, "hello")  // 2
```

### `format(template, *args, **kwargs)`

Memformat teks dengan argumen

```python
// Contoh
template itu "Nama: {}, Umur: {}"
hasil itu format(template, "Budi", 25)  // "Nama: Budi, Umur: 25"
```

---

## Validasi String

### `adalah_alfabet(text)`

Memeriksa apakah teks hanya berisi huruf

```python
// Contoh
hasil itu adalah_alfabet("abc")  // benar
hasil itu adalah_alfabet("abc123")  // salah
```

### `adalah_alfanumerik(text)`

Memeriksa apakah teks hanya berisi huruf dan angka

```python
// Contoh
hasil itu adalah_alfanumerik("abc123")  // benar
hasil itu adalah_alfanumerik("abc_123")  // salah
```

### `adalah_angka(text)`

Memeriksa apakah teks hanya berisi angka

```python
// Contoh
hasil itu adalah_angka("123")  // benar
hasil itu adalah_angka("123a")  // salah
```

### `adalah_desimal(text)`

Memeriksa apakah teks adalah angka desimal

```python
// Contoh
hasil itu adalah_desimal("123.45")  // benar
hasil itu adalah_desimal("123")  // benar
hasil itu adalah_desimal("123a")  // salah
```

### `adalah_huruf_kecil(text)`

Memeriksa apakah teks hanya berisi huruf kecil

```python
// Contoh
hasil itu adalah_huruf_kecil("abc")  // benar
hasil itu adalah_huruf_kecil("Abc")  // salah
```

### `adalah_huruf_besar(text)`

Memeriksa apakah teks hanya berisi huruf besar

```python
// Contoh
hasil itu adalah_huruf_besar("ABC")  // benar
hasil itu adalah_huruf_besar("Abc")  // salah
```

### `adalah_spasi(text)`

Memeriksa apakah teks hanya berisi spasi

```python
// Contoh
hasil itu adalah_spasi("   ")  // benar
hasil itu adalah_spasi(" a ")  // salah
```

### `adalah_judul(text)`

Memeriksa apakah teks dalam format judul

```python
// Contoh
hasil itu adalah_judul("Hello World")  // benar
hasil itu adalah_judul("Hello world")  // salah
```

### `cocok_pola(text, pattern)`

Memeriksa apakah teks cocok dengan pola regex

```python
// Contoh
hasil itu cocok_pola("abc123", "[a-z]+[0-9]+")  // benar
```

---

## Fungsi Matematika

### `absolut(x)`

Mendapatkan nilai absolut

```python
// Contoh
hasil itu absolut(-5)  // 5
```

### `akar(x)`

Mendapatkan akar kuadrat

```python
// Contoh
hasil itu akar(16)  // 4.0
```

### `pangkat(x, y)`

Menghitung x pangkat y

```python
// Contoh
hasil itu pangkat(2, 3)  // 8
```

### `bulat(x)`

Membulatkan angka

```python
// Contoh
hasil itu bulat(3.7)  // 4
```

### `bulat_bawah(x)`

Membulatkan ke bawah

```python
// Contoh
hasil itu bulat_bawah(3.7)  // 3
```

### `bulat_atas(x)`

Membulatkan ke atas

```python
// Contoh
hasil itu bulat_atas(3.2)  // 4
```

### `sinus(x)`

Menghitung sinus

```python
// Contoh
hasil itu sinus(0)  // 0.0
```

### `kosinus(x)`

Menghitung kosinus

```python
// Contoh
hasil itu kosinus(0)  // 1.0
```

### `tangen(x)`

Menghitung tangen

```python
// Contoh
hasil itu tangen(0)  // 0.0
```

### `log(x, base)`

Menghitung logaritma

```python
// Contoh
hasil itu log(100, 10)  // 2.0
```

### `faktorial(x)`

Menghitung faktorial

```python
// Contoh
hasil itu faktorial(5)  // 120
```

### `acak()`

Mendapatkan angka acak antara 0 dan 1

```python
// Contoh
hasil itu acak()  // 0.123456789...
```

### `acak_int(min, max)`

Mendapatkan angka acak integer

```python
// Contoh
hasil itu acak_int(1, 10)  // 7
```

### `acak_pilih(items)`

Memilih item acak dari list

```python
// Contoh
hasil itu acak_pilih([1, 2, 3, 4, 5])  // 3
```

### `acak_urut(items)`

Mengacak urutan list

```python
// Contoh
hasil itu acak_urut([1, 2, 3, 4, 5])  // [3, 1, 5, 2, 4]
```

---

## Statistik

### `rata_rata(data)`

Menghitung rata-rata

```python
// Contoh
hasil itu rata_rata([1, 2, 3, 4, 5])  // 3.0
```

### `median(data)`

Menghitung nilai tengah

```python
// Contoh
hasil itu median([1, 2, 3, 4, 5])  // 3
```

### `modus(data)`

Menghitung nilai yang paling sering muncul

```python
// Contoh
hasil itu modus([1, 2, 2, 3, 4])  // 2
```

### `varians(data)`

Menghitung varians

```python
// Contoh
hasil itu varians([1, 2, 3, 4, 5])  // 2.5
```

### `std_deviasi(data)`

Menghitung standar deviasi

```python
// Contoh
hasil itu std_deviasi([1, 2, 3, 4, 5])  // 1.5811388300841898
```

### `minimum(data)`

Mendapatkan nilai minimum

```python
// Contoh
hasil itu minimum([5, 3, 8, 1, 2])  // 1
```

### `maksimum(data)`

Mendapatkan nilai maksimum

```python
// Contoh
hasil itu maksimum([5, 3, 8, 1, 2])  // 8
```

### `jumlah(data)`

Menjumlahkan semua nilai

```python
// Contoh
hasil itu jumlah([1, 2, 3, 4, 5])  // 15
```

### `produk(data)`

Mengalikan semua nilai

```python
// Contoh
hasil itu produk([1, 2, 3, 4, 5])  // 120
```

---

## Fungsi List

### `tambah(list, item)`

Menambahkan item ke list

```python
// Contoh
list itu [1, 2, 3]
tambah(list, 4)  // [1, 2, 3, 4]
```

### `hapus(list, item)`

Menghapus item dari list

```python
// Contoh
list itu [1, 2, 3, 4]
hapus(list, 3)  // [1, 2, 4]
```

### `sisipkan(list, index, item)`

Menyisipkan item pada indeks tertentu

```python
// Contoh
list itu [1, 2, 4]
sisipkan(list, 2, 3)  // [1, 2, 3, 4]
```

### `pop(list, index)`

Menghapus dan mengembalikan item pada indeks tertentu

```python
// Contoh
list itu [1, 2, 3, 4]
item itu pop(list, 2)  // item = 3, list = [1, 2, 4]
```

### `indeks_list(list, item)`

Mendapatkan indeks item dalam list

```python
// Contoh
list itu [1, 2, 3, 4]
hasil itu indeks_list(list, 3)  // 2
```

### `hitung_list(list, item)`

Menghitung jumlah kemunculan item dalam list

```python
// Contoh
list itu [1, 2, 2, 3, 4]
hasil itu hitung_list(list, 2)  // 2
```

### `urutkan(list)`

Mengurutkan list

```python
// Contoh
list itu [3, 1, 4, 2]
urutkan(list)  // [1, 2, 3, 4]
```

### `balikkan(list)`

Membalikkan urutan list

```python
// Contoh
list itu [1, 2, 3, 4]
balikkan(list)  // [4, 3, 2, 1]
```

### `salin(list)`

Menyalin list

```python
// Contoh
list1 itu [1, 2, 3]
list2 itu salin(list1)
```

### `bersihkan(list)`

Menghapus semua item dari list

```python
// Contoh
list itu [1, 2, 3]
bersihkan(list)  // []
```

### `gabung_list(list1, list2)`

Menggabungkan dua list

```python
// Contoh
list1 itu [1, 2]
list2 itu [3, 4]
hasil itu gabung_list(list1, list2)  // [1, 2, 3, 4]
```

### `potong_list(list, start, end)`

Memotong list

```python
// Contoh
list itu [1, 2, 3, 4, 5]
hasil itu potong_list(list, 1, 4)  // [2, 3, 4]
```

### `unik(list)`

Menghapus duplikat dari list

```python
// Contoh
list itu [1, 2, 2, 3, 4, 4]
hasil itu unik(list)  // [1, 2, 3, 4]
```

---

## Fungsi Iterasi

### `map(func, iterable)`

Menerapkan fungsi ke setiap item

```python
// Contoh
list itu [1, 2, 3]
hasil itu map(lambda x: x * 2, list)  // [2, 4, 6]
```

### `filter(func, iterable)`

Memfilter item berdasarkan fungsi

```python
// Contoh
list itu [1, 2, 3, 4, 5]
hasil itu filter(lambda x: x % 2 == 0, list)  // [2, 4]
```

### `reduce(func, iterable)`

Mengurangi list menjadi satu nilai

```python
// Contoh
list itu [1, 2, 3, 4]
hasil itu reduce(lambda x, y: x + y, list)  // 10
```

### `zip(iterable1, iterable2)`

Menggabungkan dua iterable

```python
// Contoh
list1 itu [1, 2, 3]
list2 itu ["a", "b", "c"]
hasil itu zip(list1, list2)  // [(1, "a"), (2, "b"), (3, "c")]
```

### `enumerate(iterable)`

Mengembalikan indeks dan nilai

```python
// Contoh
list itu ["a", "b", "c"]
hasil itu enumerate(list)  // [(0, "a"), (1, "b"), (2, "c")]
```

### `semua(iterable)`

Memeriksa apakah semua item bernilai benar

```python
// Contoh
hasil itu semua([True, True, True])  // benar
hasil itu semua([True, False, True])  // salah
```

### `ada(iterable)`

Memeriksa apakah ada item yang bernilai benar

```python
// Contoh
hasil itu ada([False, False, True])  // benar
hasil itu ada([False, False, False])  // salah
```

---

## Fungsi Dictionary

### `kunci(dict)`

Mendapatkan semua kunci dari dictionary

```python
// Contoh
dict itu {"a": 1, "b": 2}
hasil itu kunci(dict)  // ["a", "b"]
```

### `nilai(dict)`

Mendapatkan semua nilai dari dictionary

```python
// Contoh
dict itu {"a": 1, "b": 2}
hasil itu nilai(dict)  // [1, 2]
```

### `item(dict)`

Mendapatkan semua pasangan kunci-nilai

```python
// Contoh
dict itu {"a": 1, "b": 2}
hasil itu item(dict)  // [("a", 1), ("b", 2)]
```

### `ambil(dict, key, default)`

Mengambil nilai dengan kunci, dengan nilai default

```python
// Contoh
dict itu {"a": 1, "b": 2}
hasil itu ambil(dict, "c", 0)  // 0
```

### `hapus_kunci(dict, key)`

Menghapus kunci dari dictionary

```python
// Contoh
dict itu {"a": 1, "b": 2}
hapus_kunci(dict, "a")  // {"b": 2}
```

### `update_dict(dict1, dict2)`

Memperbarui dictionary dengan dictionary lain

```python
// Contoh
dict1 itu {"a": 1, "b": 2}
dict2 itu {"b": 3, "c": 4}
update_dict(dict1, dict2)  // {"a": 1, "b": 3, "c": 4}
```

### `bersihkan_dict(dict)`

Menghapus semua item dari dictionary

```python
// Contoh
dict itu {"a": 1, "b": 2}
bersihkan_dict(dict)  // {}
```

---

## Operasi File

### `baca_file(path)`

Membaca isi file

```python
// Contoh
isi itu baca_file("data.txt")
```

### `tulis_file(path, content)`

Menulis ke file

```python
// Contoh
tulis_file("data.txt", "Hello World")
```

### `tambah_file(path, content)`

Menambahkan ke file

```python
// Contoh
tambah_file("data.txt", "\nHello Again")
```

### `hapus_file(path)`

Menghapus file

```python
// Contoh
hapus_file("data.txt")
```

### `file_ada(path)`

Memeriksa apakah file ada

```python
// Contoh
hasil itu file_ada("data.txt")
```

### `buat_folder(path)`

Membuat folder

```python
// Contoh
buat_folder("data")
```

### `hapus_folder(path)`

Menghapus folder

```python
// Contoh
hapus_folder("data")
```

### `folder_ada(path)`

Memeriksa apakah folder ada

```python
// Contoh
hasil itu folder_ada("data")
```

### `daftar_file(path)`

Mendapatkan daftar file dalam folder

```python
// Contoh
files itu daftar_file(".")
```

---

## Operasi Path

### `gabung_path(path1, path2)`

Menggabungkan path

```python
// Contoh
path itu gabung_path("/home/user", "data.txt")  // "/home/user/data.txt"
```

### `ekstensi_file(path)`

Mendapatkan ekstensi file

```python
// Contoh
ext itu ekstensi_file("data.txt")  // ".txt"
```

### `nama_file(path)`

Mendapatkan nama file

```python
// Contoh
name itu nama_file("/home/user/data.txt")  // "data.txt"
```

### `direktori(path)`

Mendapatkan direktori dari path

```python
// Contoh
dir itu direktori("/home/user/data.txt")  // "/home/user"
```

### `path_absolut(path)`

Mendapatkan path absolut

```python
// Contoh
abs_path itu path_absolut("data.txt")  // "/home/user/data.txt"
```

---

## Fungsi Sistem

### `waktu()`

Mendapatkan waktu saat ini (detik sejak epoch)

```python
// Contoh
now itu waktu()
```

### `tidur(seconds)`

Menunda eksekusi

```python
// Contoh
tidur(2)  // Tunggu 2 detik
```

### `tanggal()`

Mendapatkan tanggal saat ini

```python
// Contoh
today itu tanggal()  // "2023-01-01"
```

### `waktu_lengkap()`

Mendapatkan waktu lengkap saat ini

```python
// Contoh
now itu waktu_lengkap()  // "2023-01-01 12:00:00"
```

### `lingkungan(name)`

Mendapatkan variabel lingkungan

```python
// Contoh
home itu lingkungan("HOME")
```

### `set_lingkungan(name, value)`

Mengatur variabel lingkungan

```python
// Contoh
set_lingkungan("DEBUG", "true")
```

### `jalankan(command)`

Menjalankan perintah shell

```python
// Contoh
output itu jalankan("ls -la")
```

### `keluar(code)`

Keluar dari program

```python
// Contoh
keluar(0)
```

---

## JSON & Utilitas

### `ke_json(obj)`

Mengkonversi objek ke JSON

```python
// Contoh
data itu {"name": "Budi", "age": 25}
json_str itu ke_json(data)
```

### `dari_json(json_str)`

Mengkonversi JSON ke objek

```python
// Contoh
json_str itu '{"name": "Budi", "age": 25}'
data itu dari_json(json_str)
```

### `ke_base64(text)`

Mengkonversi teks ke base64

```python
// Contoh
encoded itu ke_base64("Hello")
```

### `dari_base64(encoded)`

Mengkonversi base64 ke teks

```python
// Contoh
decoded itu dari_base64("SGVsbG8=")
```

### `hash_md5(text)`

Menghitung hash MD5

```python
// Contoh
hash itu hash_md5("Hello")
```

### `hash_sha256(text)`

Menghitung hash SHA256

```python
// Contoh
hash itu hash_sha256("Hello")
```

### `enkripsi(text, key)`

Mengenkripsi teks

```python
// Contoh
encrypted itu enkripsi("Hello", "secret")
```

### `dekripsi(encrypted, key)`

Mendekripsi teks

```python
// Contoh
decrypted itu dekripsi(encrypted, "secret")
```

---

## Fungsi HTTP

### `http_get(url, headers)`

Melakukan HTTP GET request

```python
// Contoh
response itu http_get("https://api.example.com")
```

### `http_post(url, data, headers)`

Melakukan HTTP POST request

```python
// Contoh
data itu {"name": "Budi", "age": 25}
response itu http_post("https://api.example.com", data)
```

### `http_put(url, data, headers)`

Melakukan HTTP PUT request

```python
// Contoh
data itu {"name": "Budi", "age": 26}
response itu http_put("https://api.example.com/user/1", data)
```

### `http_delete(url, headers)`

Melakukan HTTP DELETE request

```python
// Contoh
response itu http_delete("https://api.example.com/user/1")
```

### `unduh_file(url, path)`

Mengunduh file dari URL

```python
// Contoh
unduh_file("https://example.com/file.pdf", "file.pdf")
```

### `parse_url(url)`

Mengurai URL

```python
// Contoh
parts itu parse_url("https://example.com/path?query=value")
```

### `buat_url(scheme, host, path, query)`

Membuat URL

```python
// Contoh
url itu buat_url("https", "example.com", "/path", {"query": "value"})
```

---

**Selamat Coding dengan RenzMcLang! 🚀**