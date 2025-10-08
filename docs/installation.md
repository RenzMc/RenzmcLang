# 📦 Instalasi RenzmcLang

Panduan lengkap instalasi RenzmcLang di berbagai platform dan setup development environment.

## 🚀 Instalasi Cepat

### Dari PyPI (Direkomendasikan)

Cara termudah dan tercepat untuk menginstall RenzmcLang:

```bash
pip install renzmc
```

### Verifikasi Instalasi

Setelah instalasi, verifikasi dengan:

```bash
renzmc --version
```

Anda akan melihat output seperti:
```
RenzmcLang version 0.0.1
```

## 🔧 Instalasi dari Source

Untuk development atau ingin versi terbaru:

### 1. Clone Repository

```bash
git clone https://github.com/RenzMc/RenzmcLang.git
cd RenzmcLang
```

### 2. Install dalam Mode Development

```bash
pip install -e .
```

Mode development (`-e`) memungkinkan Anda mengedit source code dan perubahan langsung terlihat tanpa reinstall.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 💻 Setup Extension VSCode

Extension VSCode memberikan syntax highlighting, auto-completion, dan fitur lainnya untuk pengalaman coding yang lebih baik.

### Cara Install Extension

#### Metode 1: Install Manual (VSIX)

1. **Download File VSIX**
   - Kunjungi [GitHub Releases](https://github.com/RenzMc/renzmc-extension/releases)
   - Download file `renzmc-language-support-1.0.0.vsix`

2. **Install di VSCode**
   - Buka Visual Studio Code
   - Tekan `Ctrl+Shift+P` (Windows/Linux) atau `Cmd+Shift+P` (Mac)
   - Ketik: `Extensions: Install from VSIX...`
   - Pilih file `.vsix` yang sudah didownload
   - Klik "Install"

3. **Reload VSCode**
   - Jika diminta, reload VSCode
   - Extension siap digunakan!

#### Metode 2: Build dari Source

Jika ingin build sendiri:

```bash
# Clone repository extension
git clone https://github.com/RenzMc/renzmc-extension.git
cd renzmc-extension

# Install dependencies
npm install

# Package extension
npm install -g vsce
vsce package

# Install hasil package
code --install-extension renzmc-language-support-1.0.0.vsix
```

### Fitur Extension

Setelah terinstall, Anda akan mendapatkan:

✅ **Syntax Highlighting** - Warna untuk keywords, functions, strings, dll
✅ **Auto-Completion** - Auto-closing brackets dan quotes
✅ **Smart Indentation** - Auto-indent setelah keywords
✅ **File Icons** - Icon khusus untuk file `.rmc`
✅ **Code Snippets** - Template code siap pakai

### Verifikasi Extension

1. Buat file baru dengan ekstensi `.rmc`
2. Ketik kode RenzmcLang
3. Lihat syntax highlighting bekerja

```python
// File: test.rmc
tampilkan "Hello, World!"

fungsi tambah(a, b):
    hasil a + b
selesai
```

## 🐍 Requirements

### Minimum Requirements

- **Python**: 3.6 atau lebih baru
- **pip**: Package manager Python
- **OS**: Windows, Linux, atau macOS

### Optional Requirements

Untuk fitur tambahan:

- **Numba** (untuk JIT compiler):
  ```bash
  pip install numba
  ```

- **Requests** (untuk HTTP functions):
  ```bash
  pip install requests
  ```

- **Database drivers**:
  ```bash
  # SQLite (sudah built-in di Python)
  
  # MySQL
  pip install mysql-connector-python
  
  # PostgreSQL
  pip install psycopg2-binary
  
  # MongoDB
  pip install pymongo
  ```

## 🔍 Troubleshooting

### Problem: Command 'renzmc' not found

**Solusi:**
```bash
# Pastikan pip install berhasil
pip install --upgrade renzmc

# Atau gunakan python -m
python -m renzmc file.rmc
```

### Problem: Import Error saat menjalankan

**Solusi:**
```bash
# Install ulang dengan dependencies
pip install --force-reinstall renzmc
```

### Problem: Extension VSCode tidak muncul

**Solusi:**
1. Reload VSCode: `Ctrl+Shift+P` → "Reload Window"
2. Cek extension terinstall: `Ctrl+Shift+X`
3. Reinstall extension jika perlu

### Problem: Syntax highlighting tidak bekerja

**Solusi:**
1. Pastikan file berekstensi `.rmc` atau `.renzmc`
2. Klik kanan file → "Change Language Mode" → "RenzmcLang"
3. Reload VSCode

## 🧪 Testing Instalasi

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

### Test 2: Built-in Functions

```python
// test_builtin.rmc
angka itu [1, 2, 3, 4, 5]
tampilkan f"Panjang: {panjang(angka)}"
tampilkan f"Jumlah: {jumlah(angka)}"
tampilkan f"Rata-rata: {rata_rata(angka)}"
```

### Test 3: Python Integration

```python
// test_python.rmc
impor_python "math"

hasil itu panggil_python math.sqrt(16)
tampilkan f"Akar 16 = {hasil}"
```

## 📚 Langkah Selanjutnya

Setelah instalasi berhasil:

1. **[Sintaks Dasar](sintaks-dasar)** - Pelajari sintaks fundamental
2. **[Contoh Program](contoh)** - Jalankan contoh-contoh yang ada
3. **[Fungsi Built-in](fungsi-builtin)** - Eksplorasi fungsi bawaan

## 💡 Tips

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

3. **Install Development Tools**
   ```bash
   pip install pytest black flake8
   ```

## 🆘 Bantuan Lebih Lanjut

Jika masih ada masalah:

- **GitHub Issues**: [github.com/RenzMc/RenzmcLang/issues](https://github.com/RenzMc/RenzmcLang/issues)
- **Email**: renzaja11@gmail.com
- **Documentation**: Baca dokumentasi lengkap di website ini

---

**Instalasi selesai? Mari mulai coding! 🚀**