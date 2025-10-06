# ⚡ JIT Compilation Examples

Folder ini berisi contoh-contoh penggunaan JIT (Just-In-Time) Compilation di RenzmcLang untuk meningkatkan performa eksekusi kode.

## 📋 Daftar File

### 1. `jit_simple_demo.rmc`
**Deskripsi**: Demo sederhana JIT compilation
- Pengenalan dasar JIT
- Cara mengaktifkan JIT
- Perbandingan performa dengan/tanpa JIT

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_simple_demo.rmc
```

### 2. `jit_demo.rmc`
**Deskripsi**: Demo lengkap fitur JIT
- Berbagai use case JIT
- Optimasi fungsi matematika
- Optimasi loop

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_demo.rmc
```

### 3. `jit_complete_advanced.rmc`
**Deskripsi**: Contoh JIT advanced lengkap
- Teknik optimasi lanjutan
- Multiple function compilation
- Complex algorithms dengan JIT

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_complete_advanced.rmc
```

### 4. `jit_manual_hints.rmc`
**Deskripsi**: Menggunakan type hints manual untuk JIT
- Cara memberikan hint tipe data
- Optimasi dengan type hints
- Best practices

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_manual_hints.rmc
```

### 5. `jit_performance_test.rmc`
**Deskripsi**: Testing performa JIT
- Benchmark berbagai operasi
- Mengukur speedup
- Analisis performa

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_performance_test.rmc
```

### 6. `jit_performance_benchmark.rmc`
**Deskripsi**: Benchmark komprehensif JIT
- Multiple test cases
- Statistical analysis
- Detailed performance metrics

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_performance_benchmark.rmc
```

### 7. `jit_profiling.rmc`
**Deskripsi**: Profiling kode dengan JIT
- Cara melakukan profiling
- Mengidentifikasi bottleneck
- Optimasi berdasarkan profiling

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_profiling.rmc
```

### 8. `jit_parallel_execution.rmc`
**Deskripsi**: Eksekusi paralel dengan JIT
- Parallel processing
- Multi-threading dengan JIT
- Optimasi untuk multi-core

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_parallel_execution.rmc
```

### 9. `jit_gpu_acceleration.rmc`
**Deskripsi**: GPU acceleration dengan JIT
- Menggunakan GPU untuk komputasi
- CUDA integration
- Massive parallel processing

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/jit_gpu_acceleration.rmc
```

**Note**: Memerlukan GPU dan CUDA toolkit

### 10. `verify_jit_active.rmc`
**Deskripsi**: Verifikasi JIT aktif
- Cara mengecek status JIT
- Debugging JIT compilation
- Troubleshooting

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/jit_examples/verify_jit_active.rmc
```

## 🎯 Konsep yang Diajarkan

### JIT Compilation Basics
- Apa itu JIT compilation
- Kapan menggunakan JIT
- Trade-offs JIT vs interpreted

### Performance Optimization
- Mengidentifikasi kode yang perlu dioptimasi
- Mengukur performa
- Benchmarking techniques

### Type Hints
- Pentingnya type hints untuk JIT
- Cara memberikan type hints
- Type inference

### Advanced Techniques
- GPU acceleration
- Parallel execution
- Profiling dan debugging

## 📊 Performa yang Diharapkan

Dengan JIT compilation, Anda dapat mengharapkan:
- **2-10x** speedup untuk operasi numerik
- **5-50x** speedup untuk loop intensif
- **10-100x** speedup dengan GPU acceleration

## ⚙️ Requirements

### Dasar
- Python 3.8+
- RenzmcLang installed
- numba package (untuk JIT)

### Optional (untuk GPU)
- CUDA toolkit
- NVIDIA GPU
- numba dengan CUDA support

### Instalasi Dependencies
```bash
pip install numba
# Untuk GPU support:
pip install numba[cuda]
```

## 🚀 Quick Start

1. **Mulai dengan simple demo**:
```bash
python3 -m renzmc examples/jit_examples/jit_simple_demo.rmc
```

2. **Verifikasi JIT aktif**:
```bash
python3 -m renzmc examples/jit_examples/verify_jit_active.rmc
```

3. **Test performa**:
```bash
python3 -m renzmc examples/jit_examples/jit_performance_test.rmc
```

## 💡 Tips Optimasi

1. **Gunakan type hints** - Membantu JIT compiler mengoptimasi kode
2. **Hindari dynamic typing** - Gunakan tipe data konsisten
3. **Loop optimization** - JIT sangat efektif untuk loop
4. **Numeric operations** - JIT terbaik untuk operasi matematika
5. **Profile first** - Ukur sebelum optimasi

## ⚠️ Limitations

- JIT tidak selalu lebih cepat untuk kode sederhana
- Compilation overhead untuk first run
- Tidak semua kode bisa di-JIT compile
- Memory overhead untuk compiled code

## 📚 Referensi

- [RenzmcLang JIT Documentation](../../docs/jit-compiler.md)
- [Numba Documentation](https://numba.pydata.org/)
- [Performance Optimization Guide](../../docs/performance-optimization.md)

## 🎓 Urutan Belajar

1. `jit_simple_demo.rmc` - Mulai di sini
2. `verify_jit_active.rmc` - Verifikasi setup
3. `jit_demo.rmc` - Contoh lengkap
4. `jit_manual_hints.rmc` - Type hints
5. `jit_performance_test.rmc` - Benchmarking
6. `jit_profiling.rmc` - Profiling
7. `jit_complete_advanced.rmc` - Advanced techniques
8. `jit_parallel_execution.rmc` - Parallel processing
9. `jit_gpu_acceleration.rmc` - GPU (optional)

---

**Happy Optimizing! ⚡**