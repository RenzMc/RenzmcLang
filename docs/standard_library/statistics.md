# Statistics Module

The Statistics module provides comprehensive statistical analysis functionality following Python's statistics module standards with Indonesian function names.

## Import

```python
dari statistics impor *
// atau import specific functions
dari statistics impor mean, median, stdev, variance, mode
```

## Measures of Central Tendency

### mean() / rata_rata()
Calculates the arithmetic mean of numeric data.

**Syntax:**
```python
mean(data)
rata_rata(data)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values

**Returns:**
- Float: Arithmetic mean of the data

**Examples:**
```python
dari statistics impor mean, rata_rata

// Basic mean calculation
data1 = [1, 2, 3, 4, 5]
mean1 = mean(data1)
tampilkan mean1            // Output: 3.0

// Mean with decimal values
data2 = [1.5, 2.5, 3.5, 4.5]
mean2 = rata_rata(data2)
tampilkan mean2            // Output: 3.0

// Mean of negative numbers
data3 = [-5, 0, 5, 10]
mean3 = mean(data3)
tampilkan mean3            // Output: 2.5

// Mean test scores
scores = [85, 90, 78, 92, 88, 76, 95]
avg_score = rata_rata(scores)
tampilkan f"Average score: {avg_score:.1f}"
```

---

### median() / nilai_tengah()
Calculates the median (middle value) of numeric data.

**Syntax:**
```python
median(data)
nilai_tengah(data)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values

**Returns:**
- Float: Median value of the data

**Examples:**
```python
dari statistics impor median, nilai_tengah

// Odd number of values
data1 = [1, 3, 5, 7, 9]
median1 = median(data1)
tampilkan median1          // Output: 5

// Even number of values (average of middle two)
data2 = [1, 2, 3, 4, 5, 6]
median2 = nilai_tengah(data2)
tampilkan median2          // Output: 3.5

// Unsorted data
data3 = [9, 1, 5, 3, 7]
median3 = median(data3)    // Automatically sorts
tampilkan median3          // Output: 5

// Salary median
salaries = [45000, 50000, 52000, 48000, 55000, 60000, 75000]
median_salary = nilai_tengah(salaries)
tampilkan f"Median salary: ${median_salary}"
```

---

### mode() / modus()
Calculates the mode (most frequent value) of data.

**Syntax:**
```python
mode(data)
modus(data)
```

**Parameters:**
- `data` (sequence): Sequence of values

**Returns:**
- Any: Most frequent value(s)

**Examples:**
```python
dari statistics impor mode, modus

// Single mode
data1 = [1, 2, 2, 3, 4, 2, 5]
mode1 = mode(data1)
tampilkan mode1            // Output: 2

// String mode
data2 = ["apple", "banana", "apple", "orange", "apple"]
mode2 = modus(data2)
tampilkan mode2            // Output: "apple"

// Test grade mode
grades = ["A", "B", "C", "B", "B", "A", "B"]
common_grade = mode(grades)
tampilkan f"Most common grade: {common_grade}"
```

---

### multimode() / banyak_modus()
Returns all modes (most frequent values) of data.

**Syntax:**
```python
multimode(data)
banyak_modus(data)
```

**Parameters:**
- `data` (sequence): Sequence of values

**Returns:**
- List: List of all modes

**Examples:**
```python
dari statistics impor multimode, banyak_modus

// Multiple modes
data1 = [1, 1, 2, 2, 3, 4]
modes1 = multimode(data1)
tampilkan modes1           // Output: [1, 2]

// String modes
data2 = ["cat", "dog", "cat", "bird", "dog"]
modes2 = banyak_modus(data2)
tampilkan modes2           // Output: ["cat", "dog"]

// Survey responses
responses = ["yes", "no", "maybe", "yes", "no", "yes", "no"]
all_modes = multimode(responses)
tampilkan f"All modes: {all_modes}"
```

---

## Measures of Spread

### stdev() / deviasi_standar()
Calculates sample standard deviation.

**Syntax:**
```python
stdev(data, xbar)
deviasi_standar(data, xbar)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values
- `xbar` (float, optional): Pre-calculated mean

**Returns:**
- Float: Sample standard deviation

**Examples:**
```python
dari statistics impor stdev, deviasi_standar

// Basic standard deviation
data1 = [1, 2, 3, 4, 5]
std1 = stdev(data1)
tampilkan std1             // Output: ~1.58

// With pre-calculated mean
data2 = [10, 20, 30, 40, 50]
mean2 = mean(data2)
std2 = deviasi_standar(data2, mean2)
tampilkan std2

// Test score spread
scores = [85, 90, 78, 92, 88, 76, 95]
score_std = stdev(scores)
tampilkan f"Score standard deviation: {score_std:.2f}"
```

---

### pstdev() / deviasi_standar_populasi()
Calculates population standard deviation.

**Syntax:**
```python
pstdev(data, mu)
deviasi_standar_populasi(data, mu)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values
- `mu` (float, optional): Pre-calculated population mean

**Returns:**
- Float: Population standard deviation

**Examples:**
```python
dari statistics impor pstdev, deviasi_standar_populasi

// Population standard deviation
data1 = [1, 2, 3, 4, 5]
pop_std1 = pstdev(data1)
tampilkan pop_std1         // Output: ~1.41

// Compare with sample standard deviation
sample_std = stdev(data1)
tampilkan f"Sample std: {sample_std:.2f}, Population std: {pop_std1:.2f}"

// Complete population data
ages = [25, 30, 28, 35, 32, 29, 31, 27, 33, 30]
pop_age_std = deviasi_standar_populasi(ages)
tampilkan f"Population age std: {pop_age_std:.2f}"
```

---

### variance() / variansi()
Calculates sample variance.

**Syntax:**
```python
variance(data, xbar)
variansi(data, xbar)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values
- `xbar` (float, optional): Pre-calculated mean

**Returns:**
- Float: Sample variance

**Examples:**
```python
dari statistics impor variance, variansi

// Basic variance
data1 = [1, 2, 3, 4, 5]
var1 = variance(data1)
tampilkan var1             // Output: 2.5

// Test score variance
scores = [85, 90, 78, 92, 88, 76, 95]
score_var = variansi(scores)
tampilkan f"Score variance: {score_var:.2f}"

// Financial returns
returns = [0.05, 0.03, 0.07, -0.02, 0.04, 0.06]
returns_var = variance(returns)
tampilkan f"Returns variance: {returns_var:.4f}"
```

---

### pvariance() / variansi_populasi()
Calculates population variance.

**Syntax:**
```python
pvariance(data, mu)
variansi_populasi(data, mu)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values
- `mu` (float, optional): Pre-calculated population mean

**Returns:**
- Float: Population variance

**Examples:**
```python
dari statistics impor pvariance, variansi_populasi

// Population variance
data1 = [1, 2, 3, 4, 5]
pop_var1 = pvariance(data1)
tampilkan pop_var1         // Output: 2.0

// Complete dataset analysis
weights = [70, 75, 80, 85, 90, 72, 78, 82, 88, 76]
pop_weight_var = variansi_populasi(weights)
tampilkan f"Population weight variance: {pop_weight_var:.2f}"
```

---

## Advanced Statistical Functions

### geometric_mean() / rata_rata_geometrik()
Calculates geometric mean of positive numbers.

**Syntax:**
```python
geometric_mean(data)
rata_rata_geometrik(data)
```

**Parameters:**
- `data` (sequence): Sequence of positive numeric values

**Returns:**
- Float: Geometric mean

**Examples:**
```python
dari statistics impor geometric_mean, rata_rata_geometrik

// Basic geometric mean
data1 = [1, 4, 9]
gm1 = geometric_mean(data1)
tampilkan gm1              // Output: ~3.36

// Growth rates
growth_rates = [1.05, 1.10, 1.08, 1.12, 1.09]
avg_growth = rata_rata_geometrik(growth_rates)
tampilkan f"Average growth rate: {avg_growth:.4f}"

// Financial returns
returns = [1.05, 1.03, 1.07, 0.98, 1.04]
geometric_return = geometric_mean(returns)
tampilkan f"Geometric mean return: {geometric_return:.4f}"
```

---

### harmonic_mean() / rata_rata_harmonik()
Calculates harmonic mean of positive numbers.

**Syntax:**
```python
harmonic_mean(data, weights)
rata_rata_harmonik(data, weights)
```

**Parameters:**
- `data` (sequence): Sequence of positive numeric values
- `weights` (sequence, optional): Weights for weighted harmonic mean

**Returns:**
- Float: Harmonic mean

**Examples:**
```python
dari statistics impor harmonic_mean, rata_rata_harmonik

// Basic harmonic mean
data1 = [1, 2, 4]
hm1 = harmonic_mean(data1)
tampilkan hm1              // Output: ~1.71

// Weighted harmonic mean
data2 = [10, 20, 30]
weights2 = [1, 2, 3]
hm2 = rata_rata_harmonik(data2, weights2)
tampilkan hm2

// Speed calculations
speeds = [60, 50, 40]  // km/h
avg_speed = harmonic_mean(speeds)
tampilkan f"Average speed: {avg_speed:.2f} km/h"
```

---

### quantiles() / kuantil()
Divides data into equal intervals.

**Syntax:**
```python
quantiles(data, n)
kuantil(data, n)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values
- `n` (integer): Number of equal intervals (default: 4 for quartiles)

**Returns:**
- List: List of quantile values

**Examples:**
```python
dari statistics impor quantiles, kuantil

// Quartiles (default, n=4)
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quartiles1 = quantiles(data1)
tampilkan quartiles1       // Output: [3.0, 5.5, 8.0]

// Quintiles (n=5)
quintiles1 = kuantil(data1, n=5)
tampilkan quintiles1       // Output: [2.8, 4.6, 6.4, 8.2]

// Percentiles (n=100)
data2 = rentang(1, 101)    // 1 to 100
percentiles = quantiles(data2, n=10)  // Deciles
tampilkan percentiles

// Test score percentiles
scores = [65, 70, 75, 80, 85, 90, 95, 100]
score_quartiles = kuantil(scores, n=4)
tampilkan f"Score quartiles: {score_quartiles}"
```

---

## Custom Statistical Functions

### range_data() / rentang_data()
Calculates the range (max - min) of data.

**Syntax:**
```python
range_data(data)
rentang_data(data)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values

**Returns:**
- Float: Range of the data

**Examples:**
```python
dari statistics impor rentang_data

data1 = [1, 2, 3, 4, 5]
range1 = rentang_data(data1)
tampilkan range1           // Output: 4.0

data2 = [10, 25, 15, 30, 20]
range2 = range_data(data2)
tampilkan range2           // Output: 20.0

// Temperature range
temperatures = [18, 25, 22, 28, 20, 24, 19, 26]
temp_range = rentang_data(temperatures)
tampilkan f"Temperature range: {temp_range}°C"
```

---

### cv() / koefisien_variasi()
Calculates coefficient of variation.

**Syntax:**
```python
cv(data)
koefisien_variasi(data)
```

**Parameters:**
- `data` (sequence): Sequence of numeric values

**Returns:**
- Float: Coefficient of variation

**Examples:**
```python
dari statistics impor cv, koefisien_variasi

// Basic CV
data1 = [10, 12, 11, 13, 9]
cv1 = cv(data1)
tampilkan cv1              // Output: ~0.14

// Compare variability of two datasets
data_a = [100, 102, 98, 101, 99]
data_b = [50, 150, 75, 125, 100]

cv_a = koefisien_variasi(data_a)
cv_b = koefisien_variasi(data_b)

tampilkan f"CV A: {cv_a:.3f}, CV B: {cv_b:.3f}"
tampilkan "Dataset B has higher relative variability"
```

---

### z_score() / nilai_z()
Calculates z-score for a value in a dataset.

**Syntax:**
```python
z_score(x, data)
nilai_z(x, data)
```

**Parameters:**
- `x` (number): Value to calculate z-score for
- `data` (sequence): Reference dataset

**Returns:**
- Float: Z-score value

**Examples:**
```python
dari statistics impor z_score, nilai_z

// Basic z-score
data1 = [1, 2, 3, 4, 5]
z1 = z_score(4, data1)
tampilkan z1               // Output: ~1.26

// Student performance
class_scores = [75, 80, 85, 90, 95, 78, 82, 88, 92, 77]
student_score = 88

student_z = nilai_z(student_score, class_scores)
tampilkan f"Student z-score: {student_z:.2f}"

// Quality control measurements
measurements = [10.1, 9.9, 10.0, 10.2, 9.8, 10.1, 9.9]
target_measurement = 10.15

measurement_z = z_score(target_measurement, measurements)
tampilkan f"Measurement z-score: {measurement_z:.2f}"
```

---

## Advanced Usage Examples

### Complete Statistical Analysis

```python
dari statistics impor (
    mean, median, stdev, variance, 
    geometric_mean, quantiles, cv, z_score
)

fungsi analisis_statistik_lengkap(data, nama="Data"):
    tampilkan f"=== Analisis Statistik {nama} ==="
    
    // Central tendency
    rata = mean(data)
    tengah = median(data)
    
    tampilkan f"Rata-rata: {rata:.2f}"
    tampilkan f"Median: {tengah:.2f}"
    
    // Spread
    std_dev = stdev(data)
    vari = variance(data)
    data_range = max(data) - min(data)
    coeff_var = cv(data)
    
    tampilkan f"Standar deviasi: {std_dev:.2f}"
    tampilkan f"Variansi: {vari:.2f}"
    tampilkan f"Range: {data_range:.2f}"
    tampilkan f"Koefisien variasi: {coeff_var:.3f}"
    
    // Quantiles
    quartiles = quantiles(data)
    tampilkan f"Quartiles: Q1={quartiles[0]:.2f}, Q2={quartiles[1]:.2f}, Q3={quartiles[2]:.2f}"
    
    // Z-scores for outliers
    outliers = []
    untuk value dari data
        z = abs(z_score(value, data))
        jika z > 2  // Outlier threshold
            tambah(outliers, value)
        selesai
    selesai
    
    jika outliers
        tampilkan f"Outliers (z > 2): {outliers}"
    lainnya
        tampilkan "No outliers detected"
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

// Usage
test_scores = [85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 83]
analysis = analisis_statistik_lengkap(test_scores, "Test Scores")
```

### Comparing Two Datasets

```python
dari statistics impor mean, stdev, cv

fungsi bandingkan_dataset(data1, data2, nama1="Dataset 1", nama2="Dataset 2"):
    tampilkan f"=== Perbandingan {nama1} vs {nama2} ==="
    
    // Basic statistics
    mean1 = mean(data1)
    mean2 = mean(data2)
    std1 = stdev(data1)
    std2 = stdev(data2)
    
    tampilkan f"{nama1}: Mean={mean1:.2f}, Std={std1:.2f}"
    tampilkan f"{nama2}: Mean={mean2:.2f}, Std={std2:.2f}"
    
    // Relative comparison
    mean_diff = mean2 - mean1
    std_ratio = std2 / std1
    
    tampilkan f"Mean difference: {mean_diff:.2f}"
    tampilkan f"Std ratio: {std_ratio:.2f}"
    
    // Coefficient of variation
    cv1 = cv(data1)
    cv2 = cv(data2)
    
    tampilkan f"CV {nama1}: {cv1:.3f}"
    tampilkan f"CV {nama2}: {cv2:.3f}"
    
    jika cv1 < cv2
        tampilkan f"{nama1} has more consistent (lower relative variability)"
    lainnya
        tampilkan f"{nama2} has more consistent (lower relative variability)"
    selesai
selesai

// Usage
product_a = [10.2, 10.5, 10.1, 10.3, 10.4, 10.2, 10.6]
product_b = [10.8, 10.2, 11.1, 9.9, 10.5, 10.7, 10.0]

bandingkan_dataset(product_a, product_b, "Product A", "Product B")
```

### Quality Control Analysis

```python
dari statistics impor mean, stdev, z_score

fungsi analisis_kualitas(measurements, spec_mean, spec_tolerance=2):
    """Analisis kontrol kualitas dengan spesifikasi"""
    
    tampilkan "=== Analisis Kontrol Kualitas ==="
    
    // Process capability
    process_mean = mean(measurements)
    process_std = stdev(measurements)
    
    tampilkan f"Process mean: {process_mean:.3f}"
    tampilkan f"Process std: {process_std:.3f}"
    tampilkan f"Spec target: {spec_mean:.3f}"
    tampilkan f"Spec tolerance: ±{spec_tolerance:.3f}"
    
    // Process capability index
    cp = spec_tolerance / (3 * process_std)
    cpk = min((spec_mean + spec_tolerance - process_mean) / (3 * process_std),
              (process_mean - (spec_mean - spec_tolerance)) / (3 * process_std))
    
    tampilkan f"Cp (Process Capability): {cp:.2f}"
    tampilkan f"Cpk (Process Capability Index): {cpk:.2f}"
    
    // Out of spec items
    oos_lower = []
    oos_upper = []
    
    untuk measurement dari measurements
        jika measurement < spec_mean - spec_tolerance
            tambah(oos_lower, measurement)
        selesai
        jika measurement > spec_mean + spec_tolerance
            tambah(oos_upper, measurement)
        selesai
    selesai
    
    total_oos = panjang(oos_lower) + panjang(oos_upper)
    percent_oos = (total_oos / panjang(measurements)) * 100
    
    tampilkan f"Items out of spec: {total_oos}/{panjang(measurements)} ({percent_oos:.1f}%)"
    
    jika oos_lower
        tampilkan f"Below spec: {oos_lower}"
    selesai
    jika oos_upper
        tampilkan f"Above spec: {oos_upper}"
    selesai
    
    // Quality assessment
    jika cp >= 1.33 dan cpk >= 1.33
        tampilkan "✅ Process is capable and centered"
    lainnya jika cp >= 1.33
        tampilkan "⚠️ Process is capable but not centered"
    lainnya jika cpk >= 1.33
        tampilkan "⚠️ Process is centered but not capable"
    lainnya
        tampilkan "❌ Process needs improvement"
    selesai
selesai

// Usage
measurements = [10.02, 9.98, 10.05, 10.01, 9.99, 10.03, 10.00, 9.97, 10.04, 9.96]
analisis_kualitas(measurements, spec_mean=10.0, spec_tolerance=0.05)
```

## Performance Notes

- **Large datasets**: Use `fmean()` for faster mean calculation with large datasets
- **Memory efficiency**: Functions work with iterators, not just lists
- **Precision**: Uses high-precision arithmetic for better accuracy
- **Edge cases**: Handles empty data and single-value cases appropriately

## Error Handling

```python
dari statistics impor StatisticsError, mean

coba
    empty_mean = mean([])
except StatisticsError
    tampilkan "Error: Cannot calculate mean of empty data"
selesai

// Handle zero mean for coefficient of variation
data_with_zero = [0, 0, 0]
coba
    cv_zero = cv(data_with_zero)
except ValueError
    tampilkan "Error: Mean is zero, cannot calculate coefficient of variation"
selesai
```

## Best Practices

1. **Data validation**: Ensure data is numeric and non-empty before calculations
2. **Choose appropriate measure**: Use median for skewed data, mean for symmetric data
3. **Sample vs Population**: Use `stdev()` for samples, `pstdev()` for complete populations
4. **Outlier detection**: Use z-scores or IQR method to identify outliers
5. **Statistical significance**: Consider sample size when interpreting results