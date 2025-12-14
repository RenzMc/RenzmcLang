# Instalasi RenzMcLang

Panduan lengkap instalasi RenzMcLang di berbagai platform.

## Instalasi Cepat

### Dari PyPI (Direkomendasikan)

```bash
pip install renzmc
```

### Verifikasi Instalasi

```bash
renzmc --version
```

## Instalasi dari Source

### 1. Clone Repository

```bash
git clone https://github.com/RenzMc/RenzmcLang.git
cd RenzMcLang
```

### 2. Install dalam Mode Development

```bash
pip install -e .
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Testing Instalasi

### Test 1: Hello World

Buat file `test.rmc`:

```python
tampilkan "Hello, World!"
```

Jalankan:

```bash
renzmc test.rmc
```

Output:

```
Hello, World!
```

### Test 2: Program Sederhana

```python
// test_builtin.rmc
angka itu [1, 2, 3, 4, 5]
tampilkan f"Panjang: {panjang(angka)}"
tampilkan f"Jumlah: {min(angka)}"
tampilkan f"Rata-rata: {rata_rata(angka)}"
```

### Test 3: Fungsi

```python
// test_function.rmc
fungsi sapa(nama):
    tampilkan f"Hello, {nama}!"
selesai

sapa("Budi")
```

## Requirements

### Minimum Requirements

- **Python**: 3.6 atau lebih baru
- **pip**: Package manager Python
- **OS**: Windows, Linux, atau macOS

### Optional Requirements

- **Numba** (untuk JIT compiler):
  ```bash
  pip install numba
  ```

- **Requests** (untuk HTTP functions):
  ```bash
  pip install requests
  ```

## Troubleshooting

### Problem: Command 'renzmc' not found

**Solusi:**
```bash
# Pastikan pip install berhasil
pip install --upgrade renzmc

# Atau gunakan python -m
python -m renzmc file.rmc
```

### Problem: Import Error

**Solusi:**
```bash
# Install ulang dengan dependencies
pip install --force-reinstall renzmc
```

## Tips

1. **Gunakan Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install renzmc
   ```

2. **Update Berkala**
   ```bash
   pip install --upgrade renzmc
   ```

---

**Instalasi selesai? Mari mulai coding!**