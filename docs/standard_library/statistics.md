# Modul Statistik

Modul Statistik menyediakan fungsionalitas analisis statistik komprehensif mengikuti standar modul statistics Python dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari statistics impor *
// atau impor fungsi spesifik
dari statistics impor mean, median, stdev, variance, mode
```

## Ukuran Tendensi Sentral

### mean() / rata_rata()

Menghitung rata-rata aritmatika dari data numerik.

**Sintaks:**
```python
mean(data)
rata_rata(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik

**Mengembalikan:**
- Float: Rata-rata aritmatika dari data

**Contoh:**
```python
dari statistics impor mean, rata_rata

// Perhitungan rata-rata dasar
data1 it [1, 2, 3, 4, 5]
mean1 it mean(data1)
tampilkan mean1            // Output: 3.0

// Rata-rata dengan nilai desimal
data2 it [1.5, 2.5, 3.5, 4.5]
mean2 it rata_rata(data2)
tampilkan mean2            // Output: 3.0

// Rata-rata angka negatif
data3 it [-5, 0, 5, 10]
mean3 it mean(data3)
tampilkan mean3            // Output: 2.5

// Rata-rata nilai tes
scores it [85, 90, 78, 92, 88, 76, 95]
avg_score it rata_rata(scores)
tampilkan f"Nilai rata-rata: {avg_score:.1f}"
```

---

### median() / nilai_tengah()

Menghitung median (nilai tengah) dari data numerik.

**Sintaks:**
```python
median(data)
nilai_tengah(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik

**Mengembalikan:**
- Float: Nilai median dari data

**Contoh:**
```python
dari statistics impor median, nilai_tengah

// Jumlah nilai ganjil
data1 it [1, 3, 5, 7, 9]
median1 it median(data1)
tampilkan median1          // Output: 5

// Jumlah nilai genap (rata-rata dua tengah)
data2 it [1, 2, 3, 4, 5, 6]
median2 it nilai_tengah(data2)
tampilkan median2          // Output: 3.5

// Data tidak terurut
data3 it [9, 1, 5, 3, 7]
median3 it median(data3)    // Otomatis mengurutkan
tampilkan median3          // Output: 5

// Median gaji
salaries it [45000, 50000, 52000, 48000, 55000, 60000, 75000]
median_salary it nilai_tengah(salaries)
tampilkan f"Median gaji: ${median_salary}"
```

---

### mode() / modus()

Menghitung modus (nilai yang paling sering) dari data.

**Sintaks:**
```python
mode(data)
modus(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai

**Mengembalikan:**
- Any: Nilai yang paling sering

**Contoh:**
```python
dari statistics impor mode, modus

// Modus tunggal
data1 it [1, 2, 2, 3, 4, 2, 5]
mode1 it mode(data1)
tampilkan mode1            // Output: 2

// Modus string
data2 it ["apple", "banana", "apple", "orange", "apple"]
mode2 it modus(data2)
tampilkan mode2            // Output: "apple"

// Modus nilai tes
grades it ["A", "B", "C", "B", "B", "A", "B"]
common_grade it mode(grades)
tampilkan f"Nilai yang paling umum: {common_grade}"
```

---

### multimode() / banyak_modus()

Mengembalikan semua modus (nilai yang paling sering) dari data.

**Sintaks:**
```python
multimode(data)
banyak_modus(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai

**Mengembalikan:**
- List: List dari semua modus

**Contoh:**
```python
dari statistics impor multimode, banyak_modus

// Modus ganda
data1 it [1, 1, 2, 2, 3, 4]
modes1 it multimode(data1)
tampilkan modes1           // Output: [1, 2]

// Modus string
data2 it ["cat", "dog", "cat", "bird", "dog"]
modes2 it banyak_modus(data2)
tampilkan modes2           // Output: ["cat", "dog"]

// Respons survei
responses it ["yes", "no", "maybe", "yes", "no", "yes", "no"]
all_modes it multimode(responses)
tampilkan f"Semua modus: {all_modes}"
```

## Ukuran Sebaran

### stdev() / deviasi_standar()

Menghitung standar deviasi sampel.

**Sintaks:**
```python
stdev(data, xbar)
deviasi_standar(data, xbar)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik
- `xbar` (float, opsional): Rata-rata yang dihitung sebelumnya

**Mengembalikan:**
- Float: Standar deviasi sampel

**Contoh:**
```python
dari statistics impor stdev, deviasi_standar

// Standar deviasi dasar
data1 it [1, 2, 3, 4, 5]
std1 it stdev(data1)
tampilkan std1             // Output: ~1.58

// Dengan rata-rata yang dihitung sebelumnya
data2 it [10, 20, 30, 40, 50]
mean2 it mean(data2)
std2 it deviasi_standar(data2, mean2)
tampilkan std2

// Sebaran nilai tes
scores it [85, 90, 78, 92, 88, 76, 95]
score_std it stdev(scores)
tampilkan f"Standar deviasi nilai: {score_std:.2f}"
```

---

### pstdev() / deviasi_standar_populasi()

Menghitung standar deviasi populasi.

**Sintaks:**
```python
pstdev(data, mu)
deviasi_standar_populasi(data, mu)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik
- `mu` (float, opsional): Rata-rata populasi yang dihitung sebelumnya

**Mengembalikan:**
- Float: Standar deviasi populasi

**Contoh:**
```python
dari statistics impor pstdev, deviasi_standar_populasi

// Standar deviasi populasi
data1 it [1, 2, 3, 4, 5]
pop_std1 it pstdev(data1)
tampilkan pop_std1         // Output: ~1.41

// Bandingkan dengan standar deviasi sampel
sample_std it stdev(data1)
tampilkan f"Std sampel: {sample_std:.2f}, Std populasi: {pop_std1:.2f}"

// Data populasi lengkap
ages it [25, 30, 28, 35, 32, 29, 31, 27, 33, 30]
pop_age_std it deviasi_standar_populasi(ages)
tampilkan f"Std umur populasi: {pop_age_std:.2f}"
```

---

### variance() / variansi()

Menghitung variansi sampel.

**Sintaks:**
```python
variance(data, xbar)
variansi(data, xbar)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik
- `xbar` (float, opsional): Rata-rata yang dihitung sebelumnya

**Mengembalikan:**
- Float: Variansi sampel

**Contoh:**
```python
dari statistics impor variance, variansi

// Variansi dasar
data1 it [1, 2, 3, 4, 5]
var1 it variance(data1)
tampilkan var1             // Output: 2.5

// Variansi nilai tes
scores it [85, 90, 78, 92, 88, 76, 95]
score_var it variansi(scores)
tampilkan f"Variansi nilai: {score_var:.2f}"

// Return finansial
returns it [0.05, 0.03, 0.07, -0.02, 0.04, 0.06]
returns_var it variance(returns)
tampilkan f"Variansi return: {returns_var:.4f}"
```

---

### pvariance() / variansi_populasi()

Menghitung variansi populasi.

**Sintaks:**
```python
pvariance(data, mu)
variansi_populasi(data, mu)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik
- `mu` (float, opsional): Rata-rata populasi yang dihitung sebelumnya

**Mengembalikan:**
- Float: Variansi populasi

**Contoh:**
```python
dari statistics impor pvariance, variansi_populasi

// Variansi populasi
data1 it [1, 2, 3, 4, 5]
pop_var1 it pvariance(data1)
tampilkan pop_var1         // Output: 2.0

// Analisis dataset lengkap
weights it [70, 75, 80, 85, 90, 72, 78, 82, 88, 76]
pop_weight_var it variansi_populasi(weights)
tampilkan f"Variansi bobot populasi: {pop_weight_var:.2f}"
```

## Fungsi Statistik Lanjutan

### geometric_mean() / rata_rata_geometrik()

Menghitung rata-rata geometrik dari angka positif.

**Sintaks:**
```python
geometric_mean(data)
rata_rata_geometrik(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik positif

**Mengembalikan:**
- Float: Rata-rata geometrik

**Contoh:**
```python
dari statistics impor geometric_mean, rata_rata_geometrik

// Rata-rata geometrik dasar
data1 it [1, 4, 9]
gm1 it geometric_mean(data1)
tampilkan gm1              // Output: ~3.36

// Laju pertumbuhan
growth_rates it [1.05, 1.10, 1.08, 1.12, 1.09]
avg_growth it rata_rata_geometrik(growth_rates)
tampilkan f"Laju pertumbuhan rata-rata: {avg_growth:.4f}"

// Return finansial
returns it [1.05, 1.03, 1.07, 0.98, 1.04]
geometric_return it geometric_mean(returns)
tampilkan f"Return rata-rata geometrik: {geometric_return:.4f}"
```

---

### harmonic_mean() / rata_rata_harmonik()

Menghitung rata-rata harmonik dari angka positif.

**Sintaks:**
```python
harmonic_mean(data, weights)
rata_rata_harmonik(data, weights)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik positif
- `weights` (sequence, opsional): Bobot untuk rata-rata harmonik tertimbang

**Mengembalikan:**
- Float: Rata-rata harmonik

**Contoh:**
```python
dari statistics impor harmonic_mean, rata_rata_harmonik

// Rata-rata harmonik dasar
data1 it [1, 2, 4]
hm1 it harmonic_mean(data1)
tampilkan hm1              // Output: ~1.71

// Rata-rata harmonik tertimbang
data2 it [10, 20, 30]
weights2 it [1, 2, 3]
hm2 it rata_rata_harmonik(data2, weights2)
tampilkan hm2

// Perhitungan kecepatan
speeds it [60, 50, 40]  // km/jam
avg_speed it harmonic_mean(speeds)
tampilkan f"Kecepatan rata-rata: {avg_speed:.2f} km/jam"
```

---

### quantiles() / kuantil()

Membagi data menjadi interval yang sama.

**Sintaks:**
```python
quantiles(data, n)
kuantil(data, n)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik
- `n` (integer): Jumlah interval yang sama (default: 4 untuk kuartil)

**Mengembalikan:**
- List: List nilai kuantil

**Contoh:**
```python
dari statistics impor quantiles, kuantil

// Kuartil (default, n=4)
data1 it [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quartiles1 it quantiles(data1)
tampilkan quartiles1       // Output: [3.0, 5.5, 8.0]

// Kuintil (n=5)
quintiles1 it kuantil(data1, n=5)
tampilkan quintiles1       // Output: [2.8, 4.6, 6.4, 8.2]

// Persentil (n=100)
data2 it rentang(1, 101)    // 1 to 100
percentiles it quantiles(data2, n=10)  // Desil
tampilkan percentiles

// Kuartil nilai tes
scores it [65, 70, 75, 80, 85, 90, 95, 100]
score_quartiles it kuantil(scores, n=4)
tampilkan f"Kuartil nilai: {score_quartiles}"
```

## Fungsi Statistik Kustom

### range_data() / rentang_data()

Menghitung rentang (maks - min) dari data.

**Sintaks:**
```python
range_data(data)
rentang_data(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik

**Mengembalikan:**
- Float: Rentang dari data

**Contoh:**
```python
dari statistics impor rentang_data

data1 it [1, 2, 3, 4, 5]
range1 it rentang_data(data1)
tampilkan range1           // Output: 4.0

data2 it [10, 25, 15, 30, 20]
range2 it range_data(data2)
tampilkan range2           // Output: 20.0

// Rentang suhu
temperatures it [18, 25, 22, 28, 20, 24, 19, 26]
temp_range it rentang_data(temperatures)
tampilkan f"Rentang suhu: {temp_range}°C"
```

---

### cv() / koefisien_variasi()

Menghitung koefisien variasi.

**Sintaks:**
```python
cv(data)
koefisien_variasi(data)
```

**Parameter:**
- `data` (sequence): Sequence nilai numerik

**Mengembalikan:**
- Float: Koefisien variasi

**Contoh:**
```python
dari statistics impor cv, koefisien_variasi

// CV dasar
data1 it [10, 12, 11, 13, 9]
cv1 it cv(data1)
tampilkan cv1              // Output: ~0.14

// Bandingkan variabilitas dua dataset
data_a it [100, 102, 98, 101, 99]
data_b it [50, 150, 75, 125, 100]

cv_a it koefisien_variasi(data_a)
cv_b it koefisien_variasi(data_b)

tampilkan f"CV A: {cv_a:.3f}, CV B: {cv_b:.3f}"
tampilkan "Dataset B memiliki variabilitas relatif lebih tinggi"
```

---

### z_score() / nilai_z()

Menghitung z-score untuk nilai dalam dataset.

**Sintaks:**
```python
z_score(x, data)
nilai_z(x, data)
```

**Parameter:**
- `x` (number): Nilai untuk menghitung z-score
- `data` (sequence): Dataset referensi

**Mengembalikan:**
- Float: Nilai z-score

**Contoh:**
```python
dari statistics impor z_score, nilai_z

// Z-score dasar
data1 it [1, 2, 3, 4, 5]
z1 it z_score(4, data1)
tampilkan z1               // Output: ~1.26

// Performa siswa
class_scores it [75, 80, 85, 90, 95, 78, 82, 88, 92, 77]
student_score it 88

student_z it nilai_z(student_score, class_scores)
tampilkan f"Z-score siswa: {student_z:.2f}"

// Pengukuran kontrol kualitas
measurements it [10.1, 9.9, 10.0, 10.2, 9.8, 10.1, 9.9]
target_measurement it 10.15

measurement_z it z_score(target_measurement, measurements)
tampilkan f"Z-score pengukuran: {measurement_z:.2f}"
```

## Contoh Penggunaan Lanjutan

### Analisis Statistik Lengkap

```python
dari statistics impor (
    mean, median, stdev, variance, 
    geometric_mean, quantiles, cv, z_score
)

fungsi analisis_statistik_lengkap(data, nama="Data"):
    tampilkan f"=== Analisis Statistik {nama} ==="
    
    // Tendensi sentral
    rata it mean(data)
    tengah it median(data)
    
    tampilkan f"Rata-rata: {rata:.2f}"
    tampilkan f"Median: {tengah:.2f}"
    
    // Sebaran
    std_dev it stdev(data)
    vari it variance(data)
    data_range it max(data) - min(data)
    coeff_var it cv(data)
    
    tampilkan f"Standar deviasi: {std_dev:.2f}"
    tampilkan f"Variansi: {vari:.2f}"
    tampilkan f"Range: {data_range:.2f}"
    tampilkan f"Koefisien variasi: {coeff_var:.3f}"
    
    // Kuantil
    quartiles it quantiles(data)
    tampilkan f"Kuartil: Q1={quartiles[0]:.2f}, Q2={quartiles[1]:.2f}, Q3={quartiles[2]:.2f}"
    
    // Z-scores untuk outliers
    outliers it []
    untuk value dari data
        z it abs(z_score(value, data))
        jika z > 2  // Threshold outlier
            tambah(outliers, value)
        selesai
    selesai
    
    jika outliers
        tampilkan f"Outliers (z > 2): {outliers}"
    lainnya
        tampilkan "Tidak ada outliers yang terdeteksi"
    selesai
    
    hasil {
        "mean": rata,
        "median": tengah,
        "stdev": std_dev,
        "variance": vari,
        "range": data_range,
        "cv": coeff_var,
        "quartiles": quartiles,
        "outliers": outliers
    }
selesai

// Penggunaan
test_scores it [85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 83]
analysis it analisis_statistik_lengkap(test_scores, "Nilai Tes")
```

### Membandingkan Dua Dataset

```python
dari statistics impor mean, stdev, cv

fungsi bandingkan_dataset(data1, data2, nama1="Dataset 1", nama2="Dataset 2"):
    tampilkan f"=== Perbandingan {nama1} vs {nama2} ==="
    
    // Statistik dasar
    mean1 it mean(data1)
    mean2 it mean(data2)
    std1 it stdev(data1)
    std2 it stdev(data2)
    
    tampilkan f"{nama1}: Mean={mean1:.2f}, Std={std1:.2f}"
    tampilkan f"{nama2}: Mean={mean2:.2f}, Std={std2:.2f}"
    
    // Perbandingan relatif
    mean_diff it mean2 - mean1
    std_ratio it std2 / std1
    
    tampilkan f"Perbedaan mean: {mean_diff:.2f}"
    tampilkan f"Rasio std: {std_ratio:.2f}"
    
    // Koefisien variasi
    cv1 it cv(data1)
    cv2 it cv(data2)
    
    tampilkan f"CV {nama1}: {cv1:.3f}"
    tampilkan f"CV {nama2}: {cv2:.3f}"
    
    jika cv1 < cv2
        tampilkan f"{nama1} lebih konsisten (variabilitas relatif lebih rendah)"
    lainnya
        tampilkan f"{nama2} lebih konsisten (variabilitas relatif lebih rendah)"
    selesai
selesai

// Penggunaan
product_a it [10.2, 10.5, 10.1, 10.3, 10.4, 10.2, 10.6]
product_b it [10.8, 10.2, 11.1, 9.9, 10.5, 10.7, 10.0]

bandingkan_dataset(product_a, product_b, "Produk A", "Produk B")
```

### Analisis Kontrol Kualitas

```python
dari statistics impor mean, stdev, z_score

fungsi analisis_kualitas(measurements, spec_mean, spec_tolerance=2):
    """Analisis kontrol kualitas dengan spesifikasi"""
    
    tampilkan "=== Analisis Kontrol Kualitas ==="
    
    // Kapabilitas proses
    process_mean it mean(measurements)
    process_std it stdev(measurements)
    
    tampilkan f"Mean proses: {process_mean:.3f}"
    tampilkan f"Std proses: {process_std:.3f}"
    tampilkan f"Target spec: {spec_mean:.3f}"
    tampilkan f"Toleransi spec: ±{spec_tolerance:.3f}"
    
    // Indeks kapabilitas proses
    cp it spec_tolerance / (3 * process_std)
    cpk it min((spec_mean + spec_tolerance - process_mean) / (3 * process_std),
              (process_mean - (spec_mean - spec_tolerance)) / (3 * process_std))
    
    tampilkan f"Cp (Process Capability): {cp:.2f}"
    tampilkan f"Cpk (Process Capability Index): {cpk:.2f}"
    
    // Item di luar spec
    oos_lower it []
    oos_upper it []
    
    untuk measurement dari measurements
        jika measurement < spec_mean - spec_tolerance
            tambah(oos_lower, measurement)
        selesai
        jika measurement > spec_mean + spec_tolerance
            tambah(oos_upper, measurement)
        selesai
    selesai
    
    total_oos it panjang(oos_lower) + panjang(oos_upper)
    percent_oos it (total_oos / panjang(measurements)) * 100
    
    tampilkan f"Item di luar spec: {total_oos}/{panjang(measurements)} ({percent_oos:.1f}%)"
    
    jika oos_lower
        tampilkan f"Di bawah spec: {oos_lower}"
    selesai
    jika oos_upper
        tampilkan f"Di atas spec: {oos_upper}"
    selesai
    
    // Penilaian kualitas
    jika cp >= 1.33 dan cpk >= 1.33
        tampilkan "Proses mampu dan terpusat"
    lainnya jika cp >= 1.33
        tampilkan "Proses mampu tapi tidak terpusat"
    lainnya jika cpk >= 1.33
        tampilkan "Proses terpusat tapi tidak mampu"
    lainnya
        tampilkan "Proses perlu perbaikan"
    selesai
selesai

// Penggunaan
measurements it [10.02, 9.98, 10.05, 10.01, 9.99, 10.03, 10.00, 9.97, 10.04, 9.96]
analisis_kualitas(measurements, spec_mean=10.0, spec_tolerance=0.05)
```

## Catatan Performa

- **Dataset besar**: Gunakan `fmean()` untuk perhitungan rata-rata lebih cepat dengan dataset besar
- **Efisiensi memori**: Fungsi bekerja dengan iterator, tidak hanya list
- **Presisi**: Menggunakan aritmatika presisi tinggi untuk akurasi lebih baik
- **Kasus edge**: Menangani data kosong dan kasus nilai tunggal dengan tepat

## Penanganan Error

```python
dari statistics impor StatisticsError, mean

coba
    empty_mean it mean([])
except StatisticsError
    tampilkan "Error: Tidak dapat menghitung rata-rata data kosong"
selesai

// Handle mean nol untuk koefisien variasi
data_with_zero it [0, 0, 0]
coba
    cv_zero it cv(data_with_zero)
except ValueError
    tampilkan "Error: Mean adalah nol, tidak dapat menghitung koefisien variasi"
selesai
```

## Praktik Terbaik

1. **Validasi data**: Pastikan data numerik dan tidak kosong sebelum perhitungan
2. **Pilih ukuran yang tepat**: Gunakan median untuk data miring, mean untuk data simetris
3. **Sampel vs Populasi**: Gunakan `stdev()` untuk sampel, `pstdev()` untuk populasi lengkap
4. **Deteksi outlier**: Gunakan z-scores atau metode IQR untuk mengidentifikasi outlier
5. **Signifikansi statistik**: Pertimbangkan ukuran sampel saat menginterpretasi hasil