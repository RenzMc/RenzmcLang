# Fungsi Tipe Built-in

Dokumen ini mencakup semua fungsi tipe built-in yang tersedia di RenzMcLang. Fungsi-fungsi ini selalu tersedia tanpa perlu mengimpor modul apapun dan menyediakan konversi tipe, pengecekan tipe, dan operasi tipe dasar.

## Fungsi Konversi Tipe

### str() / teks()

Mengubah objek apapun menjadi string.

**Sintaks:**
```python
str(objek)
teks(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diubah menjadi string

**Mengembalikan:**
- String: Representasi string dari objek

**Contoh:**
```python
// Konversi dasar
hasil1 it str(123)              // Output: "123"
hasil2 it teks(45.67)           // Output: "45.67"
hasil3 it str(benar)            // Output: "True"
hasil4 it teks(salah)           // Output: "False"

// Objek kompleks
hasil5 it str([1, 2, 3])        // Output: "[1, 2, 3]"
hasil6 it teks({"a": 1})        // Output: "{'a': 1}"
```

---

### int() / bilangan_bulat()

Mengubah objek menjadi integer.

**Sintaks:**
```python
int(objek, basis)
bilangan_bulat(objek, basis)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diubah menjadi integer
- `basis` (integer, opsional): Basis bilangan untuk konversi string (default: 10)

**Mengembalikan:**
- Integer: Representasi integer dari objek

**Contoh:**
```python
// Dari angka
hasil1 it int(123.45)           // Output: 123
hasil2 it bilangan_bulat(-67.8) // Output: -67

// Dari string
hasil3 it int("123")            // Output: 123
hasil4 it int("-456")           // Output: -456

// Dari basis berbeda
hasil5 it int("101", 2)         // Output: 5 (biner)
hasil6 it int("FF", 16)         // Output: 255 (heksadesimal)
hasil7 it int("10", 8)          // Output: 8 (oktal)

// Dari boolean
hasil8 it int(benar)            // Output: 1
hasil9 it int(salah)            // Output: 0
```

---

### float() / bilangan_desimal()

Mengubah objek menjadi bilangan desimal.

**Sintaks:**
```python
float(objek)
bilangan_desimal(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diubah menjadi float

**Mengembalikan:**
- Float: Representasi float dari objek

**Contoh:**
```python
// Dari integer
hasil1 it float(123)            // Output: 123.0
hasil2 it bilangan_desimal(-45) // Output: -45.0

// Dari string
hasil3 it float("123.45")       // Output: 123.45
hasil4 it float("-67.89")       // Output: -67.89
hasil5 it float("3.14e-2")      // Output: 0.0314

// Dari notasi ilmiah
hasil6 it float("1e3")          // Output: 1000.0
hasil7 it float("2.5E-1")       // Output: 0.25

// Dari boolean
hasil8 it float(benar)          // Output: 1.0
hasil9 it float(salah)          // Output: 0.0
```

---

### bool() / boolean()

Mengubah objek menjadi boolean.

**Sintaks:**
```python
bool(objek)
boolean(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diubah menjadi boolean

**Mengembalikan:**
- Boolean: Representasi boolean dari objek

**Aturan Truthiness:**
- Angka: 0 dan 0.0 adalah `salah`, lainnya `benar`
- String: String kosong "" adalah `salah`, lainnya `benar`
- Koleksi: List [], dict {}, set (), tuple () kosong adalah `salah`, lainnya `benar`
- None: Selalu `salah`
- Nilai string: "true", "1", "yes", "ya", "benar" (case insensitive) adalah `benar`

**Contoh:**
```python
// Dari angka
hasil1 it bool(0)               // Output: salah
hasil2 it bool(123)             // Output: benar
hasil3 it boolean(0.0)          // Output: salah
hasil4 it bool(-45.6)           // Output: benar

// Dari string
hasil5 it bool("")              // Output: salah
hasil6 it bool("hello")         // Output: benar
hasil7 it boolean("false")      // Output: salah
hasil8 it bool("benar")         // Output: benar
hasil9 it bool("ya")            // Output: benar

// Dari koleksi
hasil10 it bool([])             // Output: salah
hasil11 it bool([1, 2, 3])      // Output: benar
hasil12 it bool({})             // Output: salah
hasil13 it bool({"a": 1})       // Output: benar
hasil14 it boolean(())          // Output: salah
hasil15 it bool((1, 2))         // Output: benar
```

---

### list() / daftar()

Mengubah iterable menjadi list.

**Sintaks:**
```python
list(iterable)
daftar(iterable)
```

**Parameter:**
- `iterable` (iterable, opsional): Objek yang akan diubah menjadi list

**Mengembalikan:**
- List: List baru yang berisi elemen-elemen

**Contoh:**
```python
// Dari koleksi lain
hasil1 it list((1, 2, 3))       // Output: [1, 2, 3]
hasil2 it daftar({1, 2, 3})     // Output: [1, 2, 3] (urutan mungkin berbeda)
hasil3 it list("hello")         // Output: ["h", "e", "l", "l", "o"]

// Dari range
hasil4 it list(range(5))        // Output: [0, 1, 2, 3, 4]

// Dari dictionary (hanya keys)
hasil5 it daftar({"a": 1, "b": 2}) // Output: ["a", "b"] (urutan mungkin berbeda)

// List kosong
hasil6 it list()                // Output: []
```

---

### dict() / kamus()

Membuat dictionary dari argumen atau iterable.

**Sintaks:**
```python
dict(iterable)
dict(**kwargs)
kamus(iterable)
kamus(**kwargs)
```

**Parameter:**
- `iterable` (iterable, opsional): Iterable dari pasangan key-value
- `**kwargs`: Argumen keyword sebagai pasangan key-value

**Mengembalikan:**
- Dictionary: Dictionary baru

**Contoh:**
```python
// Dari argumen keyword
hasil1 it dict(a=1, b=2, c=3)   // Output: {"a": 1, "b": 2, "c": 3}
hasil2 it kamus(name="John", age=25) // Output: {"name": "John", "age": 25}

// Dari list of tuples
hasil3 it dict([("a", 1), ("b", 2), ("c", 3)]) // Output: {"a": 1, "b": 2, "c": 3}

// Dari dictionary lain
hasil4 it dict({"x": 10, "y": 20}) // Output: {"x": 10, "y": 20}

// Dictionary kosong
hasil5 it dict()                // Output: {}
```

---

### set() / himpunan()

Mengubah iterable menjadi set.

**Sintaks:**
```python
set(iterable)
himpunan(iterable)
```

**Parameter:**
- `iterable` (iterable, opsional): Objek yang akan diubah menjadi set

**Mengembalikan:**
- Set: Set baru yang berisi elemen unik

**Contoh:**
```python
// Dari list (menghapus duplikat)
hasil1 it set([1, 2, 2, 3, 3, 3]) // Output: {1, 2, 3}
hasil2 it himpunan(["a", "b", "a"]) // Output: {"a", "b"}

// Dari string
hasil3 it set("hello")          // Output: {"h", "e", "l", "o"}

// Dari tuple
hasil4 it set((1, 2, 3, 2, 1))  // Output: {1, 2, 3}

// Set kosong
hasil5 it set()                 // Output: set()
```

---

### tuple() / tupel()

Mengubah iterable menjadi tuple.

**Sintaks:**
```python
tuple(iterable)
tupel(iterable)
```

**Parameter:**
- `iterable` (iterable, opsional): Objek yang akan diubah menjadi tuple

**Mengembalikan:**
- Tuple: Tuple baru yang berisi elemen-elemen

**Contoh:**
```python
// Dari list
hasil1 it tuple([1, 2, 3])      // Output: (1, 2, 3)
hasil2 it tupel(["a", "b"])     // Output: ("a", "b")

// Dari string
hasil3 it tuple("hi")           // Output: ("h", "i")

// Dari set
hasil4 it tuple({1, 2, 3})      // Output: (1, 2, 3) (urutan mungkin berbeda)

// Tuple kosong
hasil5 it tuple()               // Output: ()
```

## Fungsi Informasi Tipe

### jenis() / type()

Mengembalikan nama tipe dari objek.

**Sintaks:**
```python
jenis(objek)
type(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang akan diambil informasi tipenya

**Mengembalikan:**
- String: Nama tipe dari objek

**Contoh:**
```python
// Tipe dasar
hasil1 it jenis(123)            // Output: "int"
hasil2 it jenis(45.67)          // Output: "float"
hasil3 it jenis("hello")        // Output: "str"
hasil4 it jenis(benar)          // Output: "bool"

// Koleksi
hasil5 it jenis([1, 2, 3])      // Output: "list"
hasil6 it jenis({"a": 1})       // Output: "dict"
hasil7 it jenis({1, 2, 3})      // Output: "set"
hasil8 it jenis((1, 2, 3))      // Output: "tuple"

// Fungsi dan kelas
fungsi_test it lambda x -> x + 1
hasil9 it jenis(fungsi_test)    // Output: "function"
hasil10 it jenis(RenzMcLang)    // Output: "type" (untuk kelas)
```

---

### panjang() / len()

Mengembalikan panjang dari objek.

**Sintaks:**
```python
panjang(objek)
len(objek)
```

**Parameter:**
- `objek` (apa saja): Objek yang memiliki panjang (string, list, tuple, dict, set)

**Mengembalikan:**
- Integer: Panjang dari objek

**Contoh:**
```python
// Panjang string
hasil1 it panjang("hello")      // Output: 5
hasil2 it len("RenzMcLang")     // Output: 10

// Panjang list
hasil3 it panjang([1, 2, 3, 4, 5]) // Output: 5
hasil4 it len([])               // Output: 0

// Panjang dictionary (jumlah keys)
hasil5 it panjang({"a": 1, "b": 2, "c": 3}) // Output: 3
hasil6 it len({})               // Output: 0

// Panjang set
hasil7 it panjang({1, 2, 3})     // Output: 3

// Panjang tuple
hasil8 it len((1, 2, 3, 4))      // Output: 4
```

---

### ke_angka()

Mengubah string menjadi angka, mencoba integer terlebih dahulu lalu float.

**Sintaks:**
```python
ke_angka(objek)
```

**Parameter:**
- `objek` (string): String yang akan diubah menjadi angka

**Mengembalikan:**
- Integer atau Float: Representasi numerik

**Contoh:**
```python
// Konversi integer
hasil1 it ke_angka("123")       // Output: 123
hasil2 it ke_angka("-456")      // Output: -456

// Konversi float
hasil3 it ke_angka("123.45")    // Output: 123.45
hasil4 it ke_angka("-67.89")    // Output: -67.89

// Notasi ilmiah
hasil5 it ke_angka("1e3")       // Output: 1000.0
hasil6 it ke_angka("2.5E-1")    // Output: 0.25

// Kasus error
// hasil7 it ke_angka("abc")      // Melempar ValueError
// hasil8 it ke_angka("")         // Melempar ValueError
```

## Fungsi Matematika Tipe

### sum() / jumlah_sum()

Jumlah dari semua item dalam iterable.

**Sintaks:**
```python
sum(iterable, start)
jumlah_sum(iterable, start)
```

**Parameter:**
- `iterable`: Iterable dari angka
- `start` (number, opsional): Nilai awal (default: 0)

**Mengembalikan:**
- Number: Jumlah dari semua item

**Contoh:**
```python
// Penjumlahan dasar
hasil1 it sum([1, 2, 3, 4, 5])   // Output: 15
hasil2 it jumlah_sum([10, 20, 30]) // Output: 60

// Dengan nilai awal
hasil3 it sum([1, 2, 3], 10)     // Output: 16
hasil4 it jumlah_sum([5, 5], 100) // Output: 110

// Dengan floats
hasil5 it sum([1.5, 2.5, 3.0])   // Output: 7.0

// Iterable kosong
hasil6 it sum([])                // Output: 0
hasil7 it sum([], 5)             // Output: 5
```

---

### min() / minimum_min()

Mengembalikan item terkecil dalam iterable.

**Sintaks:**
```python
min(iterable)
min(arg1, arg2, ...)
minimum_min(iterable)
minimum_min(arg1, arg2, ...)
```

**Parameter:**
- `iterable`: Iterable dari item yang dapat dibandingkan
- `arg1, arg2, ...`: Item individual untuk dibandingkan

**Mengembalikan:**
- Any: Item terkecil

**Contoh:**
```python
// Dari iterable
hasil1 it min([5, 3, 8, 1, 9])   // Output: 1
hasil2 it minimum_min([10, 20, 5, 15]) // Output: 5

// Dari argumen
hasil3 it min(5, 3, 8, 1, 9)     // Output: 1
hasil4 it minimum_min("apple", "banana", "cherry") // Output: "apple"

// Dengan strings (leksikografis)
hasil5 it min(["dog", "cat", "elephant"]) // Output: "cat"

// Dengan floats
hasil6 it min([3.14, 2.71, 1.41]) // Output: 1.41
```

---

### max() / maksimum_max()

Mengembalikan item terbesar dalam iterable.

**Sintaks:**
```python
max(iterable)
max(arg1, arg2, ...)
maksimum_max(iterable)
maksimum_max(arg1, arg2, ...)
```

**Parameter:**
- `iterable`: Iterable dari item yang dapat dibandingkan
- `arg1, arg2, ...`: Item individual untuk dibandingkan

**Mengembalikan:**
- Any: Item terbesar

**Contoh:**
```python
// Dari iterable
hasil1 it max([5, 3, 8, 1, 9])   // Output: 9
hasil2 it maksimum_max([10, 20, 5, 15]) // Output: 20

// Dari argumen
hasil3 it max(5, 3, 8, 1, 9)     // Output: 9
hasil4 it maksimum_max("apple", "banana", "cherry") // Output: "cherry"

// Dengan strings (leksikografis)
hasil5 it max(["dog", "cat", "elephant"]) // Output: "elephant"

// Dengan floats
hasil6 it max([3.14, 2.71, 1.41]) // Output: 3.14
```

---

### abs() / nilai_absolut()

Mengembalikan nilai absolut dari angka.

**Sintaks:**
```python
abs(x)
nilai_absolut(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Number: Nilai absolut

**Contoh:**
```python
// Integer
hasil1 it abs(-5)               // Output: 5
hasil2 it nilai_absolut(10)     // Output: 10

// Float
hasil3 it abs(-3.14)            // Output: 3.14
hasil4 it nilai_absolut(2.71)   // Output: 2.71

// Nol
hasil5 it abs(0)                // Output: 0
```

---

### round() / bulatkan()

Membulatkan angka ke jumlah desimal tertentu.

**Sintaks:**
```python
round(angka, ndigits)
bulatkan(angka, ndigits)
```

**Parameter:**
- `angka` (number): Angka yang akan dibulatkan
- `ndigits` (integer, opsional): Jumlah desimal (default: 0)

**Mengembalikan:**
- Number: Nilai yang dibulatkan

**Contoh:**
```python
// Bulatkan ke integer terdekat
hasil1 it round(3.14159)        // Output: 3
hasil2 it bulatkan(2.71828)     // Output: 3
hasil3 it round(-2.7)           // Output: -3

// Bulatkan ke desimal spesifik
hasil4 it round(3.14159, 2)     // Output: 3.14
hasil5 it bulatkan(2.71828, 3)  // Output: 2.718
hasil6 it round(1.5, 0)         // Output: 2

// Bulatkan angka negatif
hasil7 it round(-3.14159, 2)    // Output: -3.14
```

---

### pow() / pangkat_pow()

Membangkitkan basis ke pangkat exp, opsional dengan modulus.

**Sintaks:**
```python
pow(basis, exp, mod)
pangkat_pow(basis, exp, mod)
```

**Parameter:**
- `basis` (number): Angka basis
- `exp` (number): Eksponen
- `mod` (number, opsional): Modulus untuk eksponensial modular

**Mengembalikan:**
- Number: Basis dipangkatkan exp (mod mod, jika disediakan)

**Contoh:**
```python
// Eksponensial dasar
hasil1 it pow(2, 8)             // Output: 256
hasil2 it pangkat_pow(3, 3)     // Output: 27
hasil3 it pow(9, 0.5)           // Output: 3.0

// Dengan eksponen pecahan
hasil4 it pow(16, 0.25)         // Output: 2.0
hasil5 it pangkat_pow(27, 1/3)  // Output: 3.0

// Dengan modulus
hasil6 it pow(2, 8, 100)        // Output: 56 (256 % 100)
hasil7 it pangkat_pow(3, 4, 50) // Output: 31 (81 % 50)

// Eksponen negatif
hasil8 it pow(2, -3)            // Output: 0.125
```

## Fungsi Input/Output Tipe

### input() / masukan()

Membaca input dari pengguna.

**Sintaks:**
```python
input(prompt)
masukan(prompt)
```

**Parameter:**
- `prompt` (string, opsional): Prompt yang ditampilkan ke pengguna

**Mengembalikan:**
- String: Input pengguna

**Contoh:**
```python
// Input dasar
nama it input("Masukkan nama: ")
tampilkan "Hello, " + nama

// Alias Indonesia
umur it masukan("Berapa umur Anda: ")
tampilkan "Umur Anda: " + umur

// Tanpa prompt
password it input()
tampilkan "Password received"
```

---

### print() / cetak()

Menampilkan output teks ke konsol.

**Sintaks:**
```python
print(*args, sep, end)
cetak(*args, sep, end)
```

**Parameter:**
- `*args`: Item yang akan dicetak
- `sep` (string, opsional): Pemisah antar item (default: " ")
- `end` (string, opsional): String yang ditambahkan setelah item terakhir (default: "\n")

**Mengembalikan:**
- None

**Contoh:**
```python
// Pencetakan dasar
print("Hello, World!")
cetak("Halo, Dunia!")

// Multiple items
print("Nama:", "John", "Umur:", 25)

// Pemisah kustom
print("A", "B", "C", sep="-")   // Output: A-B-C

// End kustom
print("Loading", end="...")
print(" done")                  // Output: Loading...done

// Alias Indonesia
cetak("Total:", 100, "items")
```

## Catatan Penggunaan

1. **Alias Fungsi**: Banyak fungsi memiliki nama Indonesia dan Inggris:
   - `jenis()` dan `type()`
   - `panjang()` dan `len()`
   - `teks()` dan `str()`
   - `bilangan_bulat()` dan `int()`
   - `bilangan_desimal()` dan `float()`
   - `boolean()` dan `bool()`
   - `daftar()` dan `list()`
   - `kamus()` dan `dict()`
   - `himpunan()` dan `set()`
   - `tupel()` dan `tuple()`
   - `masukan()` dan `input()`
   - `cetak()` dan `print()`

2. **Konversi Tipe**: Fungsi konversi melempar exception yang sesuai untuk input tidak valid.

3. **Konversi Boolean**: Fungsi `bool()` mengikuti aturan truthiness Python dengan tambahan dukungan untuk string boolean Indonesia.

4. **Konversi Angka**: `ke_angka()` mencoba konversi integer terlebih dahulu, lalu konversi float.

5. **Input/Output**: `input()` dan `print()` bekerja persis seperti counterpart Python mereka.

6. **Operasi Koleksi**: Fungsi konversi tipe membuat salinan baru, tidak mengubah objek asli.