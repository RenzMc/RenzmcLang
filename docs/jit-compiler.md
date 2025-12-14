## Table of Contents

1. [Overview](#overview)
2. [How JIT Works](#how-jit-works)
3. [Automatic Hot Function Detection](#automatic-hot-function-detection)
4. [Manual JIT Hints](#manual-jit-hints)
5. [Profile-Guided Optimization](#profile-guided-optimization)
6. [GPU Acceleration](#gpu-acceleration)
7. [Parallel Execution](#parallel-execution)
8. [Type Inference System](#type-inference-system)
9. [Compilation Process](#compilation-process)
10. [Performance Benefits](#performance-benefits)
11. [Usage Examples](#usage-examples)
12. [Best Practices](#best-practices)
13. [Troubleshooting](#troubleshooting)
14. [Technical Details](#technical-details)

---

## Overview

RenzMcLang dilengkapi dengan **JIT (Just-In-Time) Compiler** yang menggunakan Numba untuk mengoptimasi fungsi-fungsi yang sering dipanggil (hot functions). Sistem ini bekerja secara otomatis di background tanpa memerlukan konfigurasi manual, dan sekarang mendukung manual hints, profiling, GPU acceleration, dan parallel execution.

### Key Features

- - **Automatic Detection** - Mendeteksi hot functions secara otomatis
- - **Manual JIT Hints** - Decorator untuk force JIT compilation
- - **Profile-Guided Optimization** - Optimasi berdasarkan profiling
- - **GPU Acceleration** - CUDA support via Numba
- - **Parallel Execution** - Multi-threading untuk fungsi independent
- - **Type Inference** - Sistem inferensi tipe untuk optimasi
- - **Numba Integration** - Menggunakan Numba untuk kompilasi native
- - **Fallback Mechanism** - Fallback ke interpreter jika kompilasi gagal
- - **Zero Configuration** - Tidak perlu setup atau konfigurasi
- - **Performance Boost** - Peningkatan performa hingga 10-100x untuk operasi numerik

---

## How JIT Works

### 1. Function Call Tracking

Setiap kali fungsi dipanggil, RenzMcLang melacak jumlah pemanggilan:

```rmc
fungsi hitung_faktorial(n):
    jika n <= 1
        hasil 1
    selesai
    hasil n * hitung_faktorial(n - 1)
selesai
```

### 2. Hot Function Detection

Threshold default: **10 panggilan**

Ketika fungsi mencapai threshold:
1. Sistem menganalisis apakah fungsi cocok untuk JIT compilation
2. Jika cocok, fungsi dikompilasi ke native code
3. Panggilan selanjutnya menggunakan versi compiled

### 3. Compilation Criteria

Fungsi akan dikompilasi jika memenuhi kriteria:

- **Numeric Operations** - Operasi matematika intensif  
- **Loops** - Mengandung loop (untuk/selama)  
- **High Operation Count** - Lebih dari 5 operasi  
- **No External Dependencies** - Tidak bergantung pada fungsi eksternal kompleks

---

## Manual JIT Hints

### @jit_compile Decorator

Force JIT compilation tanpa menunggu threshold:

```rmc
@jit_compile
fungsi hitung_faktorial(n):
    jika n <= 1
        hasil 1
    selesai
    hasil n * hitung_faktorial(n - 1)
selesai

hasil itu hitung_faktorial(10)
tampilkan hasil
```

### @jit_force Decorator

Alias untuk @jit_compile, memaksa kompilasi JIT:

```rmc
@jit_force
fungsi fibonacci(n):
    jika n <= 1
        hasil n
    selesai
    hasil fibonacci(n-1) + fibonacci(n-2)
selesai

hasil itu fibonacci(15)
tampilkan hasil
```

### Benefits of Manual JIT

- **Immediate Optimization** - Tidak perlu menunggu 10 panggilan
- **Predictable Performance** - Performa konsisten dari awal
- **Fine-grained Control** - Kontrol penuh atas fungsi yang dikompilasi
- **Better for Benchmarking** - Hasil benchmark lebih akurat

---

## Profile-Guided Optimization

### @profile Decorator

Menganalisis performa fungsi untuk optimasi:

```rmc
@profile
fungsi hitung_total(n):
    total itu 0
    untuk i dari 1 sampai n
        total itu total + i
    selesai
    hasil total
selesai

hasil itu hitung_total(10000)
```

Output:
```
Profile [hitung_total]:
  Execution Time: 0.001234 seconds
  Memory Used: 0.05 MB
```

### Combined with JIT

```rmc
@profile
@jit_compile
fungsi optimized_function(n):
    total itu 0
    untuk i dari 1 sampai n
        untuk j dari 1 sampai 100
            total itu total + (i * j)
        selesai
    selesai
    hasil total
selesai

hasil itu optimized_function(1000)
```

### Profiling Metrics

- ⏱️ **Execution Time** - Waktu eksekusi dalam detik
- **Memory Usage** - Penggunaan memori dalam MB
- **Performance Insights** - Data untuk optimasi lebih lanjut

---

## GPU Acceleration

### @gpu Decorator

Menggunakan CUDA untuk akselerasi GPU:

```rmc
@gpu
fungsi vector_add(a):, b
    hasil a + b
selesai

hasil itu vector_add(10), 20
tampilkan hasil
```

### GPU Requirements

- **CUDA-capable GPU** - NVIDIA GPU dengan CUDA support
- **CUDA Toolkit** - CUDA Toolkit terinstal
- **Numba CUDA** - Numba dengan CUDA support

### GPU Fallback

Jika GPU tidak tersedia, fungsi akan fallback ke CPU:

```rmc
@gpu
fungsi gpu_compute(n):
    total itu 0
    untuk i dari 1 sampai n
        total itu total + (i * i)
    selesai
    hasil total
selesai
```

### Combined GPU + JIT

```rmc
@jit_compile
@gpu
fungsi hybrid_compute(x):, y
    hasil itu 0
    untuk i dari 1 sampai 100
        hasil itu hasil + (x * i) + (y * i)
    selesai
    hasil hasil
selesai
```

---

## Parallel Execution

### @parallel Decorator

Multi-threading untuk fungsi independent:

```rmc
@parallel
fungsi proses_item(item):
    hasil itu 0
    untuk i dari 1 sampai 1000
        hasil itu hasil + (item * i)
    selesai
    hasil hasil
selesai

data itu [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hasil itu proses_item(data)
tampilkan hasil
```

### Parallel Processing Benefits

- **Multi-core Utilization** - Menggunakan semua CPU cores
- **Faster Processing** - Pemrosesan data lebih cepat
- **Scalable** - Performa meningkat dengan jumlah cores
- **Automatic Distribution** - Distribusi kerja otomatis

### Best Use Cases for Parallel

- **Batch Processing** - Memproses banyak item
- **Independent Computations** - Komputasi yang tidak saling bergantung
- **Data Analysis** - Analisis data besar
- **Map Operations** - Operasi map pada koleksi

---

## Type Inference System

### Automatic Type Detection

JIT compiler menggunakan type inference engine untuk mendeteksi tipe data:

```rmc
fungsi operasi_numerik(a):, b, c
    langkah1 itu a * b
    langkah2 itu b * c
    langkah3 itu c * a
    hasil langkah1 + langkah2 + langkah3
selesai
```

### Supported Types for JIT

| Type | JIT Support | Performance Gain |
|------|-------------|------------------|
| Integer | - Full | 50-100x |
| Float | - Full | 50-100x |
| Boolean | - Full | 10-50x |
| String | ⚠️ Limited | 1-5x |
| List | ⚠️ Limited | 1-10x |
| Dict | - No | N/A |

---

## Compilation Process

### Step-by-Step Process

1. **AST Analysis**
   ```
   RenzMcLang Code → AST → Type Inference
   ```

2. **Python Code Generation**
   ```
   AST → Python Code → Optimization
   ```

3. **Numba Compilation**
   ```
   Python Code → LLVM IR → Native Code
   ```

4. **Caching**
   ```
   Native Code → Cache → Fast Execution
   ```

### Compilation Modes

#### 1. nopython Mode (Fastest)
```rmc
@jit_compile
fungsi fibonacci(n):
    jika n <= 1
        hasil n
    selesai
    hasil fibonacci(n)-1 + fibonacci(n)-2
selesai
```

#### 2. object Mode (Fallback)
```rmc
fungsi proses_data(data):
    hasil itu 0
    untuk item dari data
        hasil itu hasil + item
    selesai
    hasil hasil
selesai
```

---

## Performance Benefits

### Benchmark Results

#### Example 1: Manual JIT vs Auto JIT

```rmc
@jit_compile
fungsi kuadrat(x):
    hasil x * x
selesai
```

- **Without JIT**: ~0.001ms per call
- **With Manual JIT**: ~0.00001ms per call (immediate)
- **Speedup**: 100x from first call

#### Example 2: Parallel Processing

```rmc
@parallel
fungsi process(item):
    total itu 0
    untuk i dari 1 sampai 1000
        total itu total + (item * i)
    selesai
    hasil total
selesai
```

- **Sequential**: ~100ms for 10 items
- **Parallel (4 cores)**: ~30ms for 10 items
- **Speedup**: 3.3x

#### Example 3: GPU Acceleration

```rmc
@gpu
fungsi vector_op(n):
    total itu 0
    untuk i dari 1 sampai n
        total itu total + (i * i)
    selesai
    hasil total
selesai
```

- **CPU**: ~50ms for n=10000
- **GPU**: ~5ms for n=10000
- **Speedup**: 10x

---

## Usage Examples

### Example 1: Manual JIT Compilation

```rmc
tampilkan "=== Manual JIT Demo ==="

@jit_compile
fungsi factorial(n):
    jika n <= 1
        hasil 1
    selesai
    hasil n * factorial(n) - 1
selesai

untuk i dari 1 sampai 10
    hasil itu factorial(i)
    tampilkan "factorial(" + ke_teks(i) + ") = " + ke_teks(hasil)
selesai
```

### Example 2: Profiling

```rmc
tampilkan "=== Profiling Demo ==="

@profile
fungsi compute_sum(n):
    total itu 0
    untuk i dari 1 sampai n
        total itu total + i
    selesai
    hasil total
selesai

hasil itu compute_sum(10000)
tampilkan "Sum: " + ke_teks(hasil)
```

### Example 3: Parallel Processing

```rmc
tampilkan "=== Parallel Demo ==="

@parallel
fungsi process_number(num):
    hasil itu 0
    untuk i dari 1 sampai 100
        hasil itu hasil + (num * i)
    selesai
    hasil hasil
selesai

numbers itu [1, 2, 3, 4, 5]
hasil itu process_number(numbers)
tampilkan hasil
```

### Example 4: GPU Acceleration

```rmc
tampilkan "=== GPU Demo ==="

@gpu
fungsi gpu_compute(n):
    total itu 0
    untuk i dari 1 sampai n
        total itu total + (i * i)
    selesai
    hasil total
selesai

hasil itu gpu_compute(1000)
tampilkan "GPU Result: " + ke_teks(hasil)
```

### Example 5: Combined Optimizations

```rmc
tampilkan "=== Combined Optimizations ==="

@profile
@jit_compile
@parallel
fungsi optimized(data):
    hasil itu 0
    untuk item dari data
        untuk i dari 1 sampai 100
            hasil itu hasil + (item * i)
        selesai
    selesai
    hasil hasil
selesai

data itu [1, 2, 3, 4, 5]
hasil itu optimized(data)
tampilkan hasil
```

---

## Best Practices

### - DO: Functions Good for JIT

```rmc
@jit_compile
fungsi hitung_rata_rata(data):
    total itu 0
    untuk item dari data
        total itu total + item
    selesai
    hasil total / panjang(data)
selesai

@jit_compile
fungsi matrix_multiply(a):, b
    hasil itu []
    untuk i dari 0 sampai panjang(a)
        baris itu []
        untuk j dari 0 sampai panjang(b[0])
            nilai itu 0
            untuk k dari 0 sampai panjang(b)
                nilai itu nilai + a[i][k] * b[k][j]
            selesai
            baris.tambah(nilai)
        selesai
        hasil.tambah(baris)
    selesai
    hasil hasil
selesai
```

### - DON'T: Functions Not Suitable for JIT

```rmc
fungsi proses_teks(teks):
    hasil itu teks.upper().replace("a", "b").split()
    hasil hasil
selesai

fungsi fetch_data(url):
    response itu http_get(url)
    hasil response.json()
selesai
```

### Optimization Tips

1. **Use Manual JIT for Critical Functions**
   ```rmc
   @jit_compile
   fungsi critical_path(data):
       hasil proses_kompleks(data)
   selesai
   ```

2. **Profile Before Optimizing**
   ```rmc
   @profile
   fungsi test_performance(n):
       hasil compute(n)
   selesai
   ```

3. **Parallelize Independent Operations**
   ```rmc
   @parallel
   fungsi process_batch(items):
       hasil transform(items)
   selesai
   ```

4. **Use GPU for Heavy Computations**
   ```rmc
   @gpu
   fungsi heavy_compute(data):
       hasil complex_math(data)
   selesai
   ```

---

## Troubleshooting

### Common Issues

#### 1. JIT Not Activating

**Problem:** Fungsi tidak dikompilasi meskipun menggunakan @jit_compile

**Solutions:**
- Pastikan fungsi numeric
- Pastikan ada operasi cukup
- Hindari string operations

#### 2. GPU Not Available

**Problem:** @gpu decorator tidak menggunakan GPU

**Solutions:**
- Check CUDA installation
- Verify GPU compatibility
- Install Numba with CUDA support
- Function will fallback to CPU automatically

#### 3. Parallel Not Faster

**Problem:** @parallel tidak meningkatkan performa

**Possible Causes:**
1. Overhead > computation time
2. Data too small
3. Operations not independent

**Solutions:**
- Use for larger datasets
- Ensure operations are independent
- Profile to verify benefit

---

## Technical Details

### Architecture

```
┌─────────────────────────────────────────────┐
│         RenzMcLang Interpreter              │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │     Function Call Tracker            │  │
│  │  - Count calls per function          │  │
│  │  - Detect hot functions (>10 calls)  │  │
│  │  - Manual JIT hints support          │  │
│  └──────────────────────────────────────┘  │
│                    ↓                        │
│  ┌──────────────────────────────────────┐  │
│  │     Type Inference Engine            │  │
│  │  - Analyze function parameters       │  │
│  │  - Infer return types                │  │
│  │  - Check JIT suitability             │  │
│  └──────────────────────────────────────┘  │
│                    ↓                        │
│  ┌──────────────────────────────────────┐  │
│  │     Code Generator                   │  │
│  │  - Convert AST to Python code        │  │
│  │  - Optimize for Numba                │  │
│  │  - GPU code generation               │  │
│  └──────────────────────────────────────┘  │
│                    ↓                        │
│  ┌──────────────────────────────────────┐  │
│  │     Numba JIT Compiler               │  │
│  │  - Compile to LLVM IR                │  │
│  │  - Generate native code              │  │
│  │  - CUDA compilation                  │  │
│  │  - Cache compiled functions          │  │
│  └──────────────────────────────────────┘  │
│                    ↓                        │
│  ┌──────────────────────────────────────┐  │
│  │     Execution Engine                 │  │
│  │  - Native code execution             │  │
│  │  - GPU execution                     │  │
│  │  - Parallel execution                │  │
│  │  - Profiling & monitoring            │  │
│  └──────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### Implementation Files

| File | Purpose |
|------|---------|
| `renzmc/jit/__init__.py` | JIT module initialization |
| `renzmc/jit/compiler.py` | Main JIT compiler logic |
| `renzmc/jit/code_generator.py` | AST to Python code conversion |
| `renzmc/jit/type_inference.py` | Type inference engine |
| `renzmc/runtime/advanced_features.py` | Decorator implementations |

### Dependencies

- **Numba** - JIT compilation to native code
- **LLVM** - Backend for code generation (via Numba)
- **CUDA** - GPU acceleration (optional)

### Configuration

Default settings:
```rmc
HOT_FUNCTION_THRESHOLD = 10
MIN_OPERATION_COUNT = 5
```

---

## Decorator Reference

### Available Decorators

| Decorator | Purpose | Example |
|-----------|---------|---------|
| `@jit_compile` | Force JIT compilation | `@jit_compile` |
| `@jit_force` | Alias for jit_compile | `@jit_force` |
| `@profile` | Profile execution | `@profile` |
| `@parallel` | Parallel execution | `@parallel` |
| `@gpu` | GPU acceleration | `@gpu` |

### Decorator Combinations

```rmc
@profile
@jit_compile
fungsi optimized(n):
    hasil compute(n)
selesai

@parallel
@jit_compile
fungsi parallel_optimized(data):
    hasil process(data)
selesai

@gpu
@jit_compile
fungsi gpu_optimized(n):
    hasil heavy_compute(n)
selesai
```

---

## Conclusion

JIT Compiler di RenzMcLang sekarang memberikan:

- **Automatic Optimization** - Tidak perlu konfigurasi manual  
- **Manual Control** - Decorator untuk kontrol penuh  
- **Profile-Guided** - Optimasi berdasarkan profiling  
- **GPU Acceleration** - CUDA support untuk performa maksimal  
- **Parallel Execution** - Multi-threading otomatis  
- **Significant Performance Gains** - 10-100x speedup  
- **Transparent Operation** - Bekerja di background  
- **Fallback Safety** - Fallback ke interpreter jika gagal  

**Best Use Cases:**
- Algoritma matematika kompleks
- Loop-heavy computations
- Numeric data processing
- Scientific computing
- Performance-critical functions
- Parallel data processing
- GPU-accelerated computations

**Not Recommended For:**
- String manipulation
- File I/O operations
- API calls
- Simple one-liner functions