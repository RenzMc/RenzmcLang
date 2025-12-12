# Library String

## Overview

Library `string` menyediakan fungsi-fungsi lengkap untuk operasi string dengan nama fungsi dalam Bahasa Indonesia. Library ini mencakup case conversion, trimming, alignment, validation, manipulation, dan utility functions untuk text processing.

## Import Library

```python
dari renzmc.library.string impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.string impor huruf_besar, huruf_kecil, hapus_spasi, judul
```

## Case Conversion

### huruf_besar(teks)

Mengkonversi teks ke uppercase.

**Parameter:**
- `teks` (string): String untuk dikonversi

**Return:**
- `string`: Uppercase string

**Contoh:**
```python
text itu "Hello World"
upper_text itu huruf_besar(text)
tampilkan upper_text  // "HELLO WORLD"

// Konversi dengan mixed case
mixed itu "Python is Awesome!"
result itu huruf_besar(mixed)
tampilkan result  // "PYTHON IS AWESOME!"

// Konversi Indonesian text
indo_text itu "Belajar Pemrograman"
upper_indo itu huruf_besar(indo_text)
tampilkan upper_indo  // "BELAJAR PEMROGRAMAN"
```

### huruf_kecil(teks)

Mengkonversi teks ke lowercase.

**Parameter:**
- `teks` (string): String untuk dikonversi

**Return:**
- `string`: Lowercase string

**Contoh:**
```python
text itu "HELLO WORLD"
lower_text itu huruf_kecil(text)
tampilkan lower_text  // "hello world"

// Konversi dengan mixed case
mixed itu "PyThOn ProGrAmMinG"
result itu huruf_kecil(mixed)
tampilkan result  // "python programming"

// Konversi Indonesian text
indo_text itu "KOTA JAKARTA"
lower_indo itu huruf_kecil(indo_text)
tampilkan lower_indo  // "kota jakarta"
```

### huruf_besar_awal(teks)

Mengkonversi teks ke capitalize (huruf besar di awal).

**Parameter:**
- `teks` (string): String untuk dikonversi

**Return:**
- `string`: Capitalized string

**Contoh:**
```python
text itu "hello world"
capitalized_text itu huruf_besar_awal(text)
tampilkan capitalized_text  // "Hello world"

// Sentence capitalization
sentence itu "python is a programming language"
result itu huruf_besar_awal(sentence)
tampilkan result  // "Python is a programming language"

// Indonesian sentence
indo_sentence itu "indonesia adalah negara kepulauan"
result_indo itu huruf_besar_awal(indo_sentence)
tampilkan result_indo  // "Indonesia adalah negara kepulauan"
```

### judul(teks)

Mengkonversi teks ke title case.

**Parameter:**
- `teks` (string): String untuk dikonversi

**Return:**
- `string`: Title case string

**Contoh:**
```python
text itu "hello world from python"
title_text itu judul(text)
tampilkan title_text  // "Hello World From Python"

// Book title
book_title itu "the lord of the rings"
result itu judul(book_title)
tampilkan result  // "The Lord Of The Rings"

// Indonesian title
indo_title itu "sejarah nusantara"
result_indo itu judul(indo_title)
tampilkan result_indo  // "Sejarah Nusantara"
```

### swap_case(teks)

Menukar case (besar ke kecil, kecil ke besar).

**Parameter:**
- `teks` (string): String untuk di-swap case

**Return:**
- `string`: Swapped case string

**Contoh:**
```python
text itu "Hello World"
swapped_text itu swap_case(text)
tampilkan swapped_text  // "hELLO wORLD"

// Mixed case
mixed itu "PyThOn Is CoOl"
result itu swap_case(mixed)
tampilkan result  // "pYtHoN iS cOoL"

// Indonesian text
indo_text itu "KuCoT KaRtUn"
result_indo itu swap_case(indo_text)
tampilkan result_indo  // "kUcOt kArTuN"
```

## Whitespace Operations

### hapus_spasi(teks)

Menghapus whitespace di awal dan akhir string.

**Parameter:**
- `teks` (string): String untuk di-trim

**Return:**
- `string`: Trimmed string

**Contoh:**
```python
text itu "   Hello World   "
trimmed_text itu hapus_spasi(text)
tampilkan f"'{trimmed_text}'"  // 'Hello World'

// Multiple whitespace
messy itu "  \t\n  Python Programming  \n\t  "
clean itu hapus_spasi(messy)
tampilkan f"'{clean}'"  // 'Python Programming'

// Indonesian text
indo_text itu "   Bahasa Indonesia   "
clean_indo itu hapus_spasi(indo_text)
tampilkan f"'{clean_indo}'"  // 'Bahasa Indonesia'
```

### hapus_spasi_kiri(teks)

Menghapus whitespace di awal string.

**Parameter:**
- `teks` (string): String untuk di-ltrim

**Return:**
- `string`: Left trimmed string

**Contoh:**
```python
text itu "   Hello World   "
left_trimmed itu hapus_spasi_kiri(text)
tampilkan f"'{left_trimmed}'"  // 'Hello World   '

// Indonesian text
indo_text itu "   Selamat datang   "
left_clean itu hapus_spasi_kiri(indo_text)
tampilkan f"'{left_clean}'"  // 'Selamat datang   '
```

### hapus_spasi_kanan(teks)

Menghapus whitespace di akhir string.

**Parameter:**
- `teks` (string): String untuk di-rtrim

**Return:**
- `string`: Right trimmed string

**Contoh:**
```python
text itu "   Hello World   "
right_trimmed itu hapus_spasi_kanan(text)
tampilkan f"'{right_trimmed}'"  // '   Hello World'

// Indonesian text
indo_text itu "   Terima kasih   "
right_clean itu hapus_spasi_kanan(indo_text)
tampilkan f"'{right_clean}'"  // '   Terima kasih'
```

## String Alignment

### tengah(teks, lebar, fillchar=" ")

Mengatur string ke tengah dengan karakter pengisi.

**Parameter:**
- `teks` (string): String untuk di-center
- `lebar` (int): Lebar total
- `fillchar` (string): Karakter pengisi (default space)

**Return:**
- `string`: Centered string

**Contoh:**
```python
text itu "Hello"
centered itu tengah(text, 10)
tampilkan f"'{centered}'"  // '   Hello  '

// Dengan custom fill character
centered2 itu tengah(text, 10, "*")
tampilkan f"'{centered2}'"  // '***Hello**'

// Indonesian text
indo_text itu "Jakarta"
centered_indo itu tengah(indo_text, 15, "-")
tampilkan f"'{centered_indo}'"  // '-----Jakarta----'
```

### kiri(teks, lebar, fillchar=" ")

Mengatur string ke kiri dengan karakter pengisi.

**Parameter:**
- `teks` (string): String untuk di-left align
- `lebar` (int): Lebar total
- `fillchar` (string): Karakter pengisi (default space)

**Return:**
- `string`: Left aligned string

**Contoh:**
```python
text itu "Hello"
left_aligned itu kiri(text, 10)
tampilkan f"'{left_aligned}'"  // 'Hello     '

// Dengan custom fill character
left2 itu kiri(text, 10, ".")
tampilkan f"'{left2}'"  // 'Hello.....'

// Indonesian text
indo_text itu "Data"
left_indo itu kiri(indo_text, 8, "_")
tampilkan f"'{left_indo}'"  // 'Data____'
```

### kanan(teks, lebar, fillchar=" ")

Mengatur string ke kanan dengan karakter pengisi.

**Parameter:**
- `teks` (string): String untuk di-right align
- `lebar` (int): Lebar total
- `fillchar` (string): Karakter pengisi (default space)

**Return:**
- `string`: Right aligned string

**Contoh:**
```python
text itu "Hello"
right_aligned itu kanan(text, 10)
tampilkan f"'{right_aligned}'"  // '     Hello'

// Dengan custom fill character
right2 itu kanan(text, 10, "0")
tampilkan f"'{right2}'"  // '00000Hello'

// Indonesian text
indo_text itu "Total"
right_indo itu kanan(indo_text, 8, "=")
tampilkan f"'{right_indo}'"  // '====Total'
```

### zfill(teks, lebar)

Menambahkan nol di sebelah kiri string.

**Parameter:**
- `teks` (string): String untuk di-zfill
- `lebar` (int): Lebar total

**Return:**
- `string`: Zero-filled string

**Contoh:**
```python
text itu "42"
zero_filled itu zfill(text, 5)
tampilkan zero_filled  // "00042"

// Numbers dengan negative
negative itu "-7"
zero_negative itu zfill(negative, 4)
tampilkan zero_negative  // "-007"

// Indonesian format
nip itu "12345"
nip_formatted itu zfill(nip, 10)
tampilkan nip_formatted  // "0000012345"
```

## Prefix dan Suffix Operations

### hapus_prefix(teks, prefix)

Menghapus prefix dari string.

**Parameter:**
- `teks` (string): String asli
- `prefix` (string): Prefix yang akan dihapus

**Return:**
- `string`: String tanpa prefix

**Contoh:**
```python
text itu "HelloWorld"
no_prefix itu hapus_prefix(text, "Hello")
tampilkan no_prefix  // "World"

// Multiple prefixes
filename itu "document_final_v2.pdf"
no_doc itu hapus_prefix(filename, "document_")
tampilkan no_doc  // "final_v2.pdf"

// Indonesian
indo_text itu "PreIndoText"
no_pre itu hapus_prefix(indo_text, "Pre")
tampilkan no_pre  // "IndoText"
```

### hapus_suffix(teks, suffix)

Menghapus suffix dari string.

**Parameter:**
- `teks` (string): String asli
- `suffix` (string): Suffix yang akan dihapus

**Return:**
- `string`: String tanpa suffix

**Contoh:**
```python
text itu "HelloWorld"
no_suffix itu hapus_suffix(text, "World")
tampilkan no_suffix  // "Hello"

// File extensions
filename itu "report.pdf"
no_ext itu hapus_suffix(filename, ".pdf")
tampilkan no_ext  // "report"

// Indonesian
indo_text itu "TextIndoPost"
no_post itu hapus_suffix(indo_text, "Post")
tampilkan no_post  // "TextIndo"
```

## String Validation

### is_alpha(teks)

Mengecek apakah string hanya berisi huruf.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika hanya huruf

**Contoh:**
```python
alpha1 itu is_alpha("Hello")
tampilkan alpha1  // True

alpha2 itu is_alpha("Hello123")
tampilkan alpha2  // False

// Indonesian text
alpha3 itu is_alpha("Bahasa")
tampilkan alpha3  // True

alpha4 itu is_alpha("Bahasa123")
tampilkan alpha4  // False
```

### is_digit(teks)

Mengecek apakah string hanya berisi digit.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika hanya digit

**Contoh:**
```python
digit1 itu is_digit("12345")
tampilkan digit1  // True

digit2 itu is_digit("12a34")
tampilkan digit2  // False

// Phone number validation
phone itu "08123456789"
is_phone_digit itu is_digit(phone)
tampilkan is_phone_digit  // True
```

### is_alnum(teks)

Mengecek apakah string berisi huruf dan digit saja.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika hanya huruf dan digit

**Contoh:**
```python
alnum1 itu is_alnum("Hello123")
tampilkan alnum1  // True

alnum2 itu is_alnum("Hello 123")
tampilkan alnum2  // False

// Username validation
username itu "user123"
is_valid_username itu is_alnum(username)
tampilkan is_valid_username  // True
```

### is_space(teks)

Mengecek apakah string hanya berisi whitespace.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika hanya whitespace

**Contoh:**
```python
space1 itu is_space("   ")
tampilkan space1  // True

space2 itu is_space("\t\n ")
tampilkan space2  // True

space3 itu is_space(" Hello ")
tampilkan space3  // False
```

### is_lower(teks)

Mengecek apakah string lowercase.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika lowercase

**Contoh:**
```python
lower1 itu is_lower("hello")
tampilkan lower1  // True

lower2 itu is_lower("Hello")
tampilkan lower2  // False

// Indonesian
lower3 itu is_lower("jakarta")
tampilkan lower3  // True
```

### is_upper(teks)

Mengecek apakah string uppercase.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika uppercase

**Contoh:**
```python
upper1 itu is_upper("HELLO")
tampilkan upper1  // True

upper2 itu is_upper("Hello")
tampilkan upper2  // False

// Indonesian
upper3 itu is_upper("JAKARTA")
tampilkan upper3  // True
```

### is_title(teks)

Mengecek apakah string title case.

**Parameter:**
- `teks` (string): String untuk dicek

**Return:**
- `boolean`: True jika title case

**Contoh:**
```python
title1 itu is_title("Hello World")
tampilkan title1  // True

title2 itu is_title("Hello world")
tampilkan title2  // False

// Indonesian
title3 itu is_title("Sejarah Nusantara")
tampilkan title3  // True
```

## Character Sets Constants

### huruf_vokal()

Mendapatkan string huruf vokal.

**Return:**
- `string`: "aiueoAIUEO"

**Contoh:**
```python
vokal itu huruf_vokal()
tampilkan vokal  // "aiueoAIUEO"

// Hitung vokal dalam text
text itu "Indonesia"
count itu sum(1 untuk char dalam text jika char dalam vokal)
tampilkan f"Jumlah vokal: {count}"  // 4
```

### huruf_konsonan()

Mendapatkan string huruf konsonan.

**Return:**
- `string`: "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

**Contoh:**
```python
konsonan itu huruf_konsonan()
tampilkan konsonan  // "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

// Hitung konsonan dalam text
text itu "Python"
konsonan_set itu huruf_konsonan()
count itu sum(1 untuk char dalam text jika char dalam konsonan_set)
tampilkan f"Jumlah konsonan: {count}"  // 5
```

### angka()

Mendapatkan string angka.

**Return:**
- `string`: "0123456789"

**Contoh:**
```python
digits itu angka()
tampilkan digits  // "0123456789"

// Extract numbers dari text
text itu "Harga: Rp 50.000"
numbers itu [char untuk char dalam text jika char dalam digits]
tampilkan f"Angka: {''.join(numbers)}"  // "50000"
```

### huruf_besar_all()

Mendapatkan string semua huruf besar.

**Return:**
- `string`: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

**Contoh:**
```python
uppercase_all itu huruf_besar_all()
tampilkan uppercase_all  // "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

### huruf_kecil_all()

Mendapatkan string semua huruf kecil.

**Return:**
- `string`: "abcdefghijklmnopqrstuvwxyz"

**Contoh:**
```python
lowercase_all itu huruf_kecil_all()
tampilkan lowercase_all  // "abcdefghijklmnopqrstuvwxyz"
```

### huruf_all()

Mendapatkan string semua huruf.

**Return:**
- `string`: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

**Contoh:**
```python
all_letters itu huruf_all()
tampilkan f"Total huruf: {panjang(all_letters)}"  // 52
```

### punctuation()

Mendapatkan string punctuation characters.

**Return:**
- `string`: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

**Contoh:**
```python
punct itu punctuation()
tampilkan punct  // '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

// Cek punctuation dalam text
text itu "Hello, world!"
punct_count itu sum(1 untuk char dalam text jika char dalam punct)
tampilkan f"Punctuation count: {punct_count}"  // 2
```

### whitespace()

Mendapatkan string whitespace characters.

**Return:**
- `string`: " \t\n\r\x0b\x0c"

**Contoh:**
```python
ws itu whitespace()
tampilkan f"Whitespace chars: {panjang(ws)}"  // 6
```

### printable()

Mendapatkan string printable characters.

**Return:**
- `string`: Semua printable characters

**Contoh:**
```python
printable_chars itu printable()
tampilkan f"Printable chars: {panjang(printable_chars)}"  // 100
```

## Random String Generation

### acak_huruf(length=10)

Mengenerate random string huruf.

**Parameter:**
- `length` (int): Panjang string (default 10)

**Return:**
- `string`: Random huruf string

**Contoh:**
```python
random1 itu acak_huruf()
tampilkan random1  // Contoh: "KjHgNmLpQr"

random2 itu acak_huruf(5)
tampilkan random2  // Contoh: "XyZaB"

// Random Indonesian-style string
random3 itu acak_huruf(8)
tampilkan random3  // Contoh: "AbCdEfGh"
```

### acak_angka(length=10)

Menggenerate random string angka.

**Parameter:**
- `length` (int): Panjang string (default 10)

**Return:**
- `string`: Random angka string

**Contoh:**
```python
random1 itu acak_angka()
tampilkan random1  // Contoh: "1234567890"

random2 itu acak_angka(6)
tampilkan random2  // Contoh: "837429"

// Generate random PIN
pin itu acak_angka(4)
tampilkan f"PIN: {pin}"  // Contoh: "8274"
```

### acak_alphanumeric(length=10)

Menggenerate random string alphanumeric.

**Parameter:**
- `length` (int): Panjang string (default 10)

**Return:**
- `string`: Random alphanumeric string

**Contoh:**
```python
random1 itu acak_alphanumeric()
tampilkan random1  // Contoh: "A1b2C3d4E5"

random2 itu acak_alphanumeric(8)
tampilkan random2  // Contoh: "xY7zP3qR"

// Generate random password
password itu acak_alphanumeric(12)
tampilkan f"Password: {password}"  // Contoh: "K8jH2mN5pQ1s"
```

## Text Manipulation

### balik_kata(kata)

Membalikkan kata.

**Parameter:**
- `kata` (string): Kata untuk dibalik

**Return:**
- `string`: Kata yang dibalik

**Contoh:**
```python
word itu "hello"
reversed_word itu balik_kata(word)
tampilkan reversed_word  // "olleh"

// Indonesian
indo_word itu "kasur"
reversed_indo itu balik_kata(indo_word)
tampilkan reversed_indo  // "rusak"
```

### balik_kalimat(kalimat)

Membalikkan kalimat.

**Parameter:**
- `kalimat` (string): Kalimat untuk dibalik

**Return:**
- `string`: Kalimat yang dibalik

**Contoh:**
```python
sentence itu "Hello World"
reversed_sentence itu balik_kalimat(sentence)
tampilkan reversed_sentence  // "dlroW olleH"

// Indonesian
indo_sentence itu "Belajar Python"
reversed_indo itu balik_kalimat(indo_sentence)
tampilkan reversed_indo  // "nohtyP rajaleB"
```

### hitung_vokal(teks)

Menghitung jumlah huruf vokal.

**Parameter:**
- `teks` (string): Teks untuk dihitung

**Return:**
- `int`: Jumlah vokal

**Contoh:**
```python
text itu "Hello World"
vowel_count itu hitung_vokal(text)
tampilkan vowel_count  // 3

// Indonesian
indo_text itu "Indonesia"
vowel_count_indo itu hitung_vokal(indo_text)
tampilkan vowel_count_indo  // 4
```

### hitung_konsonan(teks)

Menghitung jumlah huruf konsonan.

**Parameter:**
- `teks` (string): Teks untuk dihitung

**Return:**
- `int`: Jumlah konsonan

**Contoh:**
```python
text itu "Hello World"
consonant_count itu hitung_konsonan(text)
tampilkan consonant_count  // 7

// Indonesian
indo_text itu "Bahasa"
consonant_count_indo itu hitung_konsonan(indo_text)
tampilkan consonant_count_indo  // 3
```

### hitung_kata(teks)

Menghitung jumlah kata.

**Parameter:**
- `teks` (string): Teks untuk dihitung

**Return:**
- `int`: Jumlah kata

**Contoh:**
```python
text itu "Hello World from Python"
word_count itu hitung_kata(text)
tampilkan word_count  // 4

// Indonesian
indo_text itu "Belajar pemrograman itu menyenangkan"
word_count_indo itu hitung_kata(indo_text)
tampilkan word_count_indo  // 5
```

### extract_angka(teks)

Mengekstrak angka dari teks.

**Parameter:**
- `teks` (string): Teks untuk diekstrak

**Return:**
- `list`: List angka yang ditemukan

**Contoh:**
```python
text itu "Price: Rp 50.000, Discount: 10%"
numbers itu extract_angka(text)
tampilkan numbers  // ["50", "000", "10"]

// Indonesian
indo_text itu "No. 001, Tahun 2023"
numbers_indo itu extract_angka(indo_text)
tampilkan numbers_indo  // ["001", "2023"]
```

### extract_huruf(teks)

Mengekstrak huruf dari teks.

**Parameter:**
- `teks` (string): Teks untuk diekstrak

**Return:**
- `string`: String huruf saja

**Contoh:**
```python
text itu "Hello123World"
letters itu extract_huruf(text)
tampilkan letters  // "HelloWorld"

// Indonesian
indo_text itu "Jakarta12345"
letters_indo itu extract_huruf(indo_text)
tampilkan letters_indo  // "Jakarta"
```

### bersihkan_spasi(teks)

Membersihkan spasi berlebih dalam teks.

**Parameter:**
- `teks` (string): Teks untuk dibersihkan

**Return:**
- `string`: Teks tanpa spasi berlebih

**Contoh:**
```python
messy_text itu "Hello    World   from   Python"
clean_text itu bersihkan_spasi(messy_text)
tampilkan clean_text  // "Hello World from Python"

// Indonesian
messy_indo itu "Indonesia    adalah    negara    kepulauan"
clean_indo itu bersihkan_spasi(messy_indo)
tampilkan clean_indo  // "Indonesia adalah negara kepulauan"
```

## Cipher Functions

### rot13(teks)

Mengencode/decode teks dengan ROT13 cipher.

**Parameter:**
- `teks` (string): Teks untuk di-encode

**Return:**
- `string`: ROT13 encoded text

**Contoh:**
```python
text itu "Hello World"
rot13_text itu rot13(text)
tampilkan rot13_text  // "Uryyb Jbeyq"

// Decode balik
decoded itu rot13(rot13_text)
tampilkan decoded  // "Hello World"

// Indonesian
indo_text itu "Belajar"
rot13_indo itu rot13(indo_text)
tampilkan rot13_indo  // "Orywne"
```

### caesar(teks, shift=3)

Mengencode teks dengan Caesar cipher.

**Parameter:**
- `teks` (string): Teks untuk di-encode
- `shift` (int): Jumlah pergeseran (default 3)

**Return:**
- `string`: Caesar encoded text

**Contoh:**
```python
text itu "Hello"
caesar_text itu caesar(text)
tampilkan caesar_text  // "Khoor"

// Custom shift
caesar_custom itu caesar(text, 5)
tampilkan caesar_custom  // "Mjqqt"

// Indonesian
indo_text itu "Pagi"
caesar_indo itu caesar(indo_text, 3)
tampilkan caesar_indo  // "Sdjl"
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.string impor *

tampilkan "=== Demo String Library ==="

// 1. Case conversion
tampilkan "\n1. Case Conversion:"
original itu "Hello World from RenzMcLang"
upper_text itu huruf_besar(original)
lower_text itu huruf_kecil(original)
capitalized itu huruf_besar_awal(original)
title_text itu judul(original)
swapped itu swap_case(original)

tampilkan f"Original: {original}"
tampilkan f"Uppercase: {upper_text}"
tampilkan f"Lowercase: {lower_text}"
tampilkan f"Capitalized: {capitalized}"
tampilkan f"Title: {title_text}"
tampilkan f"Swapped: {swapped}"

// 2. Whitespace operations
tampilkan "\n2. Whitespace Operations:"
messy itu "   \t\n   Python Programming   \n\t  "
clean itu hapus_spasi(messy)
left_clean itu hapus_spasi_kiri(messy)
right_clean itu hapus_spasi_kanan(messy)

tampilkan f"Original: '{messy}'"
tampilkan f"Trimmed: '{clean}'"
tampilkan f"Left trimmed: '{left_clean}'"
tampilkan f"Right trimmed: '{right_clean}'"

// 3. Alignment
tampilkan "\n3. Alignment:"
text itu "Hello"
centered itu tengah(text, 15, "-")
left_aligned itu kiri(text, 15, "=")
right_aligned itu kanan(text, 15, "*")
zero_padded itu zfill("42", 6)

tampilkan f"Centered: '{centered}'"
tampilkan f"Left aligned: '{left_aligned}'"
tampilkan f"Right aligned: '{right_aligned}'"
tampilkan f"Zero padded: '{zero_padded}'"

// 4. Prefix dan suffix
tampilkan "\n4. Prefix dan Suffix:"
filename itu "document_final_v2.pdf"
no_prefix itu hapus_prefix(filename, "document_")
no_suffix itu hapus_suffix(no_prefix, "_v2.pdf")

tampilkan f"Original: {filename}"
tampilkan f"Tanpa prefix: {no_prefix}"
tampilkan f"Tanpa suffix: {no_suffix}"

// 5. Validation
tampilkan "\n5. String Validation:"
test_strings itu ["Hello", "12345", "Hello123", "   "]

untuk test_str dalam test_strings:
    alpha itu is_alpha(test_str)
    digit itu is_digit(test_str)
    alnum itu is_alnum(test_str)
    space itu is_space(test_str)
    
    tampilkan f"'{test_str}': Alpha={alpha}, Digit={digit}, Alnum={alnum}, Space={space}"

// 6. Character sets
tampilkan "\n6. Character Sets:"
tampilkan f"Vokal: {huruf_vokal()}"
tampilkan f"Konsonan: {potong(huruf_konsonan(), 0, 20)}..."
tampilkan f"Angka: {angka()}"
tampilkan f"Punctuation: {punctuation()}"

// 7. Random generation
tampilkan "\n7. Random String Generation:"
random_letters itu acak_huruf(8)
random_digits itu acak_angka(6)
random_alnum itu acak_alphanumeric(10)

tampilkan f"Random letters: {random_letters}"
tampilkan f"Random digits: {random_digits}"
tampilkan f"Random alphanumeric: {random_alnum}"

// 8. Text manipulation
tampilkan "\n8. Text Manipulation:"
word itu "programming"
reversed_word itu balik_kata(word)

sentence itu "Programming is fun and educational"
reversed_sentence itu balik_kalimat(sentence)

indonesian_text itu "Bahasa Indonesia adalah indah"
vowel_count itu hitung_vokal(indonesian_text)
consonant_count itu hitung_konsonan(indonesian_text)
word_count itu hitung_kata(indonesian_text)

tampilkan f"Reversed word: {reversed_word}"
tampilkan f"Reversed sentence: {reversed_sentence}"
tampilkan f"Indonesian text: '{indonesian_text}'"
tampilkan f"Vowels: {vowel_count}, Consonants: {consonant_count}, Words: {word_count}"

// 9. Extraction
tampilkan "\n9. Data Extraction:"
data_text itu "Order #12345, Amount: Rp 50.000, Customer: ID67890"
numbers itu extract_angka(data_text)
letters itu extract_huruf(data_text)

tampilkan f"Original: {data_text}"
tampilkan f"Extracted numbers: {numbers}"
tampilkan f"Extracted letters: {letters}"

// 10. Text cleaning
tampilkan "\n10. Text Cleaning:"
messy_text itu "This    is    a    very    messy    text   with   extra   spaces"
clean_text itu bersihkan_spasi(messy_text)

tampilkan f"Original: '{messy_text}'")
tampilkan f"Cleaned: '{clean_text}'")

// 11. Cipher operations
tampilkan "\n11. Cipher Operations:"
secret_message itu "This is a secret message"
rot13_encoded itu rot13(secret_message)
caesar_encoded itu caesar(secret_message, 5)

tampilkan f"Original: {secret_message}")
tampilkan f"ROT13: {rot13_encoded}")
tampilkan f"Caesar (shift 5): {caesar_encoded}")

// 12. Indonesian text processing
tampilkan "\n12. Indonesian Text Processing:")
indonesian_sentences itu [
    "jakarta adalah ibu kota indonesia",
    "belajar pemrograman itu sangat menyenangkan",
    "nasi goreng adalah makanan favorit saya"
]

untuk sentence dalam indonesian_sentences:
    title_case itu judul(sentence)
    word_count itu hitung_kata(sentence)
    char_count itu panjang(hapus_spasi(sentence))
    
    tampilkan f"Original: '{sentence}'")
    tampilkan f"Title case: '{title_case}'")
    tampilkan f"Words: {word_count}, Characters: {char_count}")

// 13. Practical examples
tampilkan "\n13. Practical Examples:")

// Format nomor telepon
phone itu "08123456789"
formatted_phone itu hapus_spasi(kiri(phone + " ", 15, "*"))
tampilkan f"Phone formatted: '{formatted_phone}'")

// Generate random password
password itu acak_alphanumeric(12)
tampilkan f"Generated password: {password}")

// Validate Indonesian NIK (simplified)
nik itu "3201011234567890"
jika panjang(nik) == 16 dan is_digit(nik):
    tampilkan "Valid NIK format")
lainnya:
    tampilkan "Invalid NIK format")

// Extract kode pos dari alamat
address itu "Jl. Merdeka No. 123, Jakarta Pusat 10110"
postal_codes itu extract_angka(address)
jika postal_codes:
    postal_code itu postal_codes[-1]  // Ambil yang terakhir
    tampilkan f"Postal code: {postal_code}")

// 14. String analysis
tampilkan "\n14. String Analysis:")
analysis_text itu "Programming in RenzMcLang is enjoyable and productive!"

total_chars itu panjang(analysis_text)
no_spaces itu panjang(bersihkan_spasi(analysis_text))
vowels itu hitung_vokal(analysis_text)
consonants itu hitung_konsonan(analysis_text)
words itu hitung_kata(analysis_text)
digits_count itu panjang(extract_angka(analysis_text))

tampilkan f"Text: '{analysis_text}'")
tampilkan f"Total characters: {total_chars}")
tampilkan f"Characters without spaces: {no_spaces}")
tampilkan f"Vowels: {vowels}")
tampilkan f"Consonants: {consonants}")
tampilkan f"Words: {words}")
tampilkan f"Digits: {digits_count}")

tampilkan "\n=== Demo Selesai ===")
```

## Use Cases Umum

1. **Text Processing**: Cleaning dan normalisasi text
2. **Data Validation**: Validasi input forms dan user data
3. **String Formatting**: Output formatting untuk reports dan displays
4. **Password Generation**: Generate secure random passwords
5. **Text Analysis**: Count characters, words, dan patterns
6. **Data Extraction**: Extract specific patterns dari text
7. **Localization**: Handle Indonesian text processing
8. **Security**: Simple cipher operations untuk basic encoding

## Performance Tips

- Gunakan `hapus_spasi()` untuk text normalization
- `acak_alphanumeric()` efficient untuk password generation
- `bersihkan_spasi()` untuk cleanup user input
- `hitung_kata()` lebih cepat dari manual splitting
- Constants seperti `huruf_vokal()` di-cache untuk performance

## Indonesian Language Support

Library ini dirancang dengan dukungan penuh Bahasa Indonesia:
- Function names dalam Bahasa Indonesia
- Examples dengan konteks Indonesia
- Support untuk Indonesian text processing
- Validation patterns untuk Indonesian data
- Cultural context dalam examples

## Security Considerations

- `caesar()` dan `rot13()` bukan untuk security purposes
- Gunakan `acak_alphanumeric()` untuk temporary passwords
- Always validate user input dengan validation functions
- Hash sensitive data sebelum storage

## Best Practices

1. Gunakan `hapus_spasi()` untuk input normalization
2. Validate text dengan appropriate `is_*` functions
3. Use `bersihkan_spasi()` untuk user-generated content
4. Generate passwords dengan `acak_alphanumeric()`
5. Extract data dengan specific `extract_*` functions
6. Use Indonesian function names untuk better readability