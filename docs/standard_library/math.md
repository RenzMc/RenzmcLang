# Modul Matematika

Modul Matematika menyediakan fungsi-fungsi matematika yang komprehensif mengikuti standar modul math Python dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari math impor *
// atau impor fungsi spesifik
dari math impor pi, sin, cos, sqrt
```

## Konstanta Matematika

### pi
Konstanta matematika π (3.141592653589793).

```python
dari math impor pi
tampilkan pi  // Output: 3.141592653589793

// Hitung keliling
jari_jari itu 10
keliling itu 2 * pi * jari_jari
tampilkan keliling  // Output: 62.83185307179586
```

### e
Konstanta matematika e (2.718281828459045).

```python
dari math impor e
tampilkan e  // Output: 2.718281828459045

// Hitung eksponensial
hasil itu e ** 2
tampilkan hasil  // Output: 7.38905609893065
```

### tau
Konstanta matematika τ (2π = 6.283185307179586).

```python
dari math impor tau
tampilkan tau  // Output: 6.283185307179586

// Rotasi penuh
sudut_penuh itu tau
tampilkan sudut_penuh
```

### inf
Tak terhingga positif.

```python
dari math impor inf
tampilkan inf  // Output: inf

// Periksa apakah nilai tak terhingga
dari math impor isinf
hasil itu isinf(inf)
tampilkan hasil  // Output: benar
```

### nan
Not a Number (NaN).

```python
dari math impor nan
tampilkan nan  // Output: nan

// Periksa apakah nilai NaN
dari math impor isnan
hasil itu isnan(nan)
tampilkan hasil  // Output: benar
```

## Operasi Dasar

### abs() / nilai_absolut()
Mengembalikan nilai absolut dari x.

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
dari math impor abs, nilai_absolut

hasil1 itu abs(-5.5)        // Output: 5.5
hasil2 itu abs(10)          // Output: 10
hasil3 itu nilai_absolut(-3) // Output: 3
```

---

### round()
Membulatkan x ke jumlah desimal tertentu.

**Sintaks:**
```python
round(x, digits)
```

**Parameter:**
- `x` (number): Angka yang akan dibulatkan
- `digits` (integer, opsional): Jumlah desimal (default: 0)

**Mengembalikan:**
- Number: Nilai yang dibulatkan

**Contoh:**
```python
dari math impor round

hasil1 itu round(3.14159, 2)   // Output: 3.14
hasil2 itu round(2.71828)      // Output: 3
hasil3 itu round(-2.7)         // Output: -3
```

---

### pow() / pangkat()
Menghitung basis dipangkatkan dengan eksponen.

**Sintaks:**
```python
pow(basis, eksponen)
pangkat(basis, eksponen)
```

**Parameter:**
- `basis` (number): Angka basis
- `eksponen` (number): Eksponen

**Mengembalikan:**
- Number: Basis^eksponen

**Contoh:**
```python
dari math impor pow, pangkat

hasil1 itu pow(2, 8)          // Output: 256.0
hasil2 itu pow(9, 0.5)        // Output: 3.0
hasil3 itu pangkat(5, 3)      // Output: 125.0
```

---

### sqrt() / akar()
Menghitung akar kuadrat dari x.

**Sintaks:**
```python
sqrt(x)
akar(x)
```

**Parameter:**
- `x` (number): Angka input (harus non-negatif)

**Mengembalikan:**
- Number: Akar kuadrat

**Contoh:**
```python
dari math impor sqrt, akar

hasil1 itu sqrt(16)           // Output: 4.0
hasil2 itu sqrt(2)            // Output: 1.4142135623730951
hasil3 itu akar(25)           // Output: 5.0
```

## Fungsi Trigonometri

### sin() / sinus()
Menghitung sinus dari x (dalam radian).

**Sintaks:**
```python
sin(x)
sinus(x)
```

**Parameter:**
- `x` (number): Sudut dalam radian

**Mengembalikan:**
- Number: Nilai sinus

**Contoh:**
```python
dari math impor sin, sinus, pi

hasil1 itu sin(0)              // Output: 0.0
hasil2 itu sin(pi/2)           // Output: 1.0
hasil3 itu sinus(pi)           // Output: 1.2246467991473532e-16 (≈ 0)
```

---

### cos() / cosinus()
Menghitung cosinus dari x (dalam radian).

**Sintaks:**
```python
cos(x)
cosinus(x)
```

**Parameter:**
- `x` (number): Sudut dalam radian

**Mengembalikan:**
- Number: Nilai cosinus

**Contoh:**
```python
dari math impor cos, cosinus, pi

hasil1 itu cos(0)              // Output: 1.0
hasil2 itu cos(pi)             // Output: -1.0
hasil3 itu cosinus(pi/2)       // Output: 6.123233995736766e-17 (≈ 0)
```

---

### tan() / tangen()
Menghitung tangen dari x (dalam radian).

**Sintaks:**
```python
tan(x)
tangen(x)
```

**Parameter:**
- `x` (number): Sudut dalam radian

**Mengembalikan:**
- Number: Nilai tangen

**Contoh:**
```python
dari math impor tan, tangen, pi

hasil1 itu tan(0)              // Output: 0.0
hasil2 itu tan(pi/4)           // Output: 0.9999999999999999 (≈ 1)
hasil3 itu tangen(pi/6)        // Output: 0.5773502691896257
```

---

### asin()
Menghitung inverse sinus (arcsin) dari x.

**Sintaks:**
```python
asin(x)
```

**Parameter:**
- `x` (number): Nilai antara -1 dan 1

**Mengembalikan:**
- Number: Sudut dalam radian

**Contoh:**
```python
dari math impor asin

hasil1 itu asin(0)             // Output: 0.0
hasil2 itu asin(1)             // Output: 1.5707963267948966 (π/2)
hasil3 itu asin(0.5)           // Output: 0.5235987755982989 (π/6)
```

---

### acos()
Menghitung inverse cosinus (arccos) dari x.

**Sintaks:**
```python
acos(x)
```

**Parameter:**
- `x` (number): Nilai antara -1 dan 1

**Mengembalikan:**
- Number: Sudut dalam radian

**Contoh:**
```python
dari math impor acos

hasil1 itu acos(1)             // Output: 0.0
hasil2 itu acos(0)             // Output: 1.5707963267948966 (π/2)
hasil3 itu acos(-1)            // Output: 3.141592653589793 (π)
```

---

### atan()
Menghitung inverse tangen (arctan) dari x.

**Sintaks:**
```python
atan(x)
```

**Parameter:**
- `x` (number): Angka real apa saja

**Mengembalikan:**
- Number: Sudut dalam radian

**Contoh:**
```python
dari math impor atan

hasil1 itu atan(0)             // Output: 0.0
hasil2 itu atan(1)             // Output: 0.7853981633974483 (π/4)
hasil3 itu atan(1000)          // Output: 1.5697963271282298 (≈ π/2)
```

---

### atan2()
Menghitung arctangen dari y/x, mempertimbangkan kuadran.

**Sintaks:**
```python
atan2(y, x)
```

**Parameter:**
- `y` (number): Koordinat Y
- `x` (number): Koordinat X

**Mengembalikan:**
- Number: Sudut dalam radian

**Contoh:**
```python
dari math impor atan2

hasil1 itu atan2(1, 1)         // Output: 0.7853981633974483 (π/4)
hasil2 itu atan2(1, 0)         // Output: 1.5707963267948966 (π/2)
hasil3 itu atan2(0, 1)         // Output: 0.0
```

## Fungsi Logaritma

### log() / logaritma()
Menghitung logaritma dari x dengan basis tertentu.

**Sintaks:**
```python
log(x, basis)
logaritma(x, basis)
```

**Parameter:**
- `x` (number): Angka positif
- `basis` (number, opsional): Basis (default: e untuk log natural)

**Mengembalikan:**
- Number: Nilai logaritma

**Contoh:**
```python
dari math impor log, logaritma, e

hasil1 itu log(100)            // Output: 4.605170185988092 (log natural)
hasil2 itu log(100, 10)        // Output: 2.0 (log basis 10)
hasil3 itu logaritma(e)        // Output: 1.0
```

---

### log10()
Menghitung logaritma basis 10 dari x.

**Sintaks:**
```python
log10(x)
```

**Parameter:**
- `x` (number): Angka positif

**Mengembalikan:**
- Number: Logaritma basis 10

**Contoh:**
```python
dari math impor log10

hasil1 itu log10(1000)         // Output: 3.0
hasil2 itu log10(100)          // Output: 2.0
hasil3 itu log10(1)            // Output: 0.0
```

---

### log2()
Menghitung logaritma basis 2 dari x.

**Sintaks:**
```python
log2(x)
```

**Parameter:**
- `x` (number): Angka positif

**Mengembalikan:**
- Number: Logaritma basis 2

**Contoh:**
```python
dari math impor log2

hasil1 itu log2(8)             // Output: 3.0
hasil2 itu log2(16)            // Output: 4.0
hasil3 itu log2(1)             // Output: 0.0
```

---

### ln() / logaritma_natural()
Menghitung logaritma natural (basis e) dari x.

**Sintaks:**
```python
ln(x)
logaritma_natural(x)
```

**Parameter:**
- `x` (number): Angka positif

**Mengembalikan:**
- Number: Logaritma natural

**Contoh:**
```python
dari math impor ln, logaritma_natural, e

hasil1 itu ln(e)               // Output: 1.0
hasil2 itu ln(e ** 2)          // Output: 2.0
hasil3 itu logaritma_natural(1) // Output: 0.0
```

## Fungsi Konversi Sudut

### degrees() / derajat()
Mengkonversi radian ke derajat.

**Sintaks:**
```python
degrees(x)
derajat(x)
```

**Parameter:**
- `x` (number): Sudut dalam radian

**Mengembalikan:**
- Number: Sudut dalam derajat

**Contoh:**
```python
dari math impor degrees, derajat, pi

hasil1 itu degrees(pi)         // Output: 180.0
hasil2 itu degrees(pi/2)       // Output: 90.0
hasil3 itu derajat(0)          // Output: 0.0
```

---

### radians() / radian()
Mengkonversi derajat ke radian.

**Sintaks:**
```python
radians(x)
radian(x)
```

**Parameter:**
- `x` (number): Sudut dalam derajat

**Mengembalikan:**
- Number: Sudut dalam radian

**Contoh:**
```python
dari math impor radians, radian

hasil1 itu radians(180)        // Output: 3.141592653589793
hasil2 itu radians(90)         // Output: 1.5707963267948966
hasil3 itu radian(45)          // Output: 0.7853981633974483
```

## Fungsi Khusus

### factorial() / faktorial()
Menghitung faktorial dari n (n!).

**Sintaks:**
```python
factorial(n)
faktorial(n)
```

**Parameter:**
- `n` (integer): Integer non-negatif

**Mengembalikan:**
- Integer: Nilai faktorial

**Contoh:**
```python
dari math impor factorial, faktorial

hasil1 itu factorial(5)        // Output: 120
hasil2 itu factorial(0)        // Output: 1
hasil3 itu faktorial(10)       // Output: 3628800
```

---

### gcd()
Menghitung faktor persekutuan terbesar dari a dan b.

**Sintaks:**
```python
gcd(a, b)
```

**Parameter:**
- `a` (integer): Integer pertama
- `b` (integer): Integer kedua

**Mengembalikan:**
- Integer: Faktor persekutuan terbesar

**Contoh:**
```python
dari math impor gcd

hasil1 itu gcd(48, 18)         // Output: 6
hasil2 itu gcd(100, 25)        // Output: 25
hasil3 itu gcd(17, 13)         // Output: 1
```

---

### lcm()
Menghitung kelipatan persekutuan terkecil dari a dan b.

**Sintaks:**
```python
lcm(a, b)
```

**Parameter:**
- `a` (integer): Integer pertama
- `b` (integer): Integer kedua

**Mengembalikan:**
- Integer: Kelipatan persekutuan terkecil

**Contoh:**
```python
dari math impor lcm

hasil1 itu lcm(4, 6)           // Output: 12
hasil2 itu lcm(5, 7)           // Output: 35
hasil3 itu lcm(10, 15)         // Output: 30
```

---

### ceil() / pembulatan_atas()
Membulatkan x ke integer terdekat ke atas.

**Sintaks:**
```python
ceil(x)
pembulatan_atas(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Integer: Nilai yang dibulatkan ke atas

**Contoh:**
```python
dari math impor ceil, pembulatan_atas

hasil1 itu ceil(3.2)           // Output: 4
hasil2 itu ceil(3.8)           // Output: 4
hasil3 itu pembulatan_atas(-2.3) // Output: -2
```

---

### floor() / pembulatan_bawah()
Membulatkan x ke integer terdekat ke bawah.

**Sintaks:**
```python
floor(x)
pembulatan_bawah(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Integer: Nilai yang dibulatkan ke bawah

**Contoh:**
```python
dari math impor floor, pembulatan_bawah

hasil1 itu floor(3.2)          // Output: 3
hasil2 itu floor(3.8)          // Output: 3
hasil3 itu pembulatan_bawah(-2.3) // Output: -3
```

---

### trunc()
Menghapus bagian desimal dari x.

**Sintaks:**
```python
trunc(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Integer: Nilai yang dipotong

**Contoh:**
```python
dari math impor trunc

hasil1 itu trunc(3.2)          // Output: 3
hasil2 itu trunc(3.8)          // Output: 3
hasil3 itu trunc(-2.3)         // Output: -2
```

## Fungsi Utilitas

### fsum() / jumlah_presisi()
Melakukan penjumlahan presisi tinggi dari iterable.

**Sintaks:**
```python
fsum(iterable)
jumlah_presisi(iterable)
```

**Parameter:**
- `iterable`: Iterable angka

**Mengembalikan:**
- Number: Jumlah yang presisi

**Contoh:**
```python
dari math impor fsum, jumlah_presisi

angka itu [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
hasil1 itu fsum(angka)         // Output: 1.0
hasil2 itu jumlah_presisi([1, 2, 3, 4, 5]) // Output: 15.0
```

---

### isfinite()
Memeriksa apakah x adalah angka finite.

**Sintaks:**
```python
isfinite(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Boolean: `benar` jika finite, `salah` jika tidak

**Contoh:**
```python
dari math impor isfinite, inf, nan

hasil1 itu isfinite(123)       // Output: benar
hasil2 itu isfinite(inf)       // Output: salah
hasil3 itu isfinite(nan)       // Output: salah
```

---

### isinf()
Memeriksa apakah x adalah tak terhingga.

**Sintaks:**
```python
isinf(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Boolean: `benar` jika tak terhingga, `salah` jika tidak

**Contoh:**
```python
dari math impor isinf, inf

hasil1 itu isinf(inf)          // Output: benar
hasil2 itu isinf(123)          // Output: salah
hasil3 itu isinf(-inf)         // Output: benar
```

---

### isnan()
Memeriksa apakah x adalah NaN (Not a Number).

**Sintaks:**
```python
isnan(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Boolean: `benar` jika NaN, `salah` jika tidak

**Contoh:**
```python
dari math impor isnan, nan

hasil1 itu isnan(nan)          // Output: benar
hasil2 itu isnan(123)          // Output: salah
hasil3 itu isnan(0)            // Output: salah
```

---

### copysign()
Menyalin tanda dari y ke x.

**Sintaks:**
```python
copysign(x, y)
```

**Parameter:**
- `x` (number): Magnitudo
- `y` (number): Sumber tanda

**Mengembalikan:**
- Number: x dengan tanda dari y

**Contoh:**
```python
dari math impor copysign

hasil1 itu copysign(5, -3)     // Output: -5.0
hasil2 itu copysign(-5, 3)     // Output: 5.0
hasil3 itu copysign(5, 0)      // Output: 5.0
```

---

### frexp()
Mengembalikan mantissa dan eksponen dari x.

**Sintaks:**
```python
frexp(x)
```

**Parameter:**
- `x` (number): Angka input

**Mengembalikan:**
- Tuple: (mantissa, eksponen)

**Contoh:**
```python
dari math impor frexp

hasil1 itu frexp(8)            // Output: (0.5, 4)
hasil2 itu frexp(0.75)         // Output: (0.75, 0)
```

---

### ldexp()
Menghitung x * (2**i).

**Sintaks:**
```python
ldexp(x, i)
```

**Parameter:**
- `x` (number): Mantissa
- `i` (integer): Eksponen

**Mengembalikan:**
- Number: x * (2**i)

**Contoh:**
```python
dari math impor ldexp

hasil1 itu ldexp(0.5, 4)       // Output: 8.0
hasil2 itu ldexp(1, 3)         // Output: 8.0
hasil3 itu ldexp(2, 0)         // Output: 2.0
```

## Catatan Penggunaan

1. **Impor Diperlukan**: Semua fungsi matematika harus diimpor dari modul math.

2. **Alias Indonesia**: Banyak fungsi memiliki alias Indonesia untuk kemudahan:
   - `nilai_absolut()` untuk `abs()`
   - `pangkat()` untuk `pow()`
   - `akar()` untuk `sqrt()`
   - `sinus()` untuk `sin()`
   - `cosinus()` untuk `cos()`
   - `tangen()` untuk `tan()`
   - `logaritma()` untuk `log()`
   - `logaritma_natural()` untuk `ln()`
   - `derajat()` untuk `degrees()`
   - `radian()` untuk `radians()`
   - `faktorial()` untuk `factorial()`
   - `pembulatan_atas()` untuk `ceil()`
   - `pembulatan_bawah()` untuk `floor()`
   - `jumlah_presisi()` untuk `fsum()`

3. **Satuan Sudut**: Fungsi trigonometri menggunakan radian secara default. Gunakan `degrees()`/`radians()` untuk konversi.

4. **Presisi**: Fungsi menggunakan aritmatika floating-point presisi ganda.

5. **Penanganan Error**: Fungsi akan melempar exception yang sesuai untuk input tidak valid (misalnya angka negatif untuk akar kuadrat).