# 🧪 Testing Examples

Folder ini berisi contoh-contoh testing dan validasi untuk berbagai fitur RenzmcLang.

## 📋 Daftar File

### 1. `test_class_complete.rmc`
**Deskripsi**: Testing lengkap untuk fitur OOP/Class
- Testing class definition
- Testing inheritance
- Testing methods dan properties
- Testing constructor

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/testing_examples/test_class_complete.rmc
```

**Yang Ditest**:
- ✅ Class creation
- ✅ Object instantiation
- ✅ Method calls
- ✅ Inheritance
- ✅ Polymorphism
- ✅ Encapsulation

### 2. `test_database_examples.rmc`
**Deskripsi**: Testing operasi database
- Testing koneksi database
- Testing CRUD operations
- Testing query execution
- Testing error handling

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/testing_examples/test_database_examples.rmc
```

**Yang Ditest**:
- ✅ Database connection
- ✅ CREATE operations
- ✅ READ operations
- ✅ UPDATE operations
- ✅ DELETE operations
- ✅ Transaction handling

### 3. `test_jit_compilation.rmc`
**Deskripsi**: Testing JIT compilation
- Testing JIT activation
- Testing compilation success
- Testing performance improvement
- Testing compiled function behavior

**Cara Menjalankan**:
```bash
python3 -m renzmc examples/testing_examples/test_jit_compilation.rmc
```

**Yang Ditest**:
- ✅ JIT compiler availability
- ✅ Function compilation
- ✅ Compiled function execution
- ✅ Performance metrics
- ✅ Type inference
- ✅ Error handling

## 🎯 Tujuan Testing

### Validasi Fitur
- Memastikan semua fitur bekerja dengan benar
- Mendeteksi bug dan error
- Validasi edge cases

### Regression Testing
- Memastikan update tidak merusak fitur existing
- Continuous integration
- Quality assurance

### Performance Testing
- Mengukur performa
- Benchmarking
- Optimasi

### Documentation
- Contoh penggunaan fitur
- Best practices
- Common patterns

## 🧪 Jenis Testing

### 1. Unit Testing
Testing individual components:
- Functions
- Classes
- Methods

### 2. Integration Testing
Testing interaksi antar komponen:
- Database integration
- Python integration
- External libraries

### 3. Performance Testing
Testing performa:
- JIT compilation
- Execution speed
- Memory usage

### 4. Feature Testing
Testing fitur lengkap:
- OOP features
- Type system
- Error handling

## 📊 Test Coverage

| Fitur | File Test | Status |
|-------|-----------|--------|
| OOP/Classes | test_class_complete.rmc | ✅ Complete |
| Database | test_database_examples.rmc | ✅ Complete |
| JIT Compilation | test_jit_compilation.rmc | ✅ Complete |

## 🚀 Cara Menjalankan Semua Test

### Menjalankan Satu Test
```bash
python3 -m renzmc examples/testing_examples/test_class_complete.rmc
```

### Menjalankan Semua Test (Manual)
```bash
# Test 1: Classes
python3 -m renzmc examples/testing_examples/test_class_complete.rmc

# Test 2: Database
python3 -m renzmc examples/testing_examples/test_database_examples.rmc

# Test 3: JIT
python3 -m renzmc examples/testing_examples/test_jit_compilation.rmc
```

### Menggunakan Script (Bash)
```bash
#!/bin/bash
for test in examples/testing_examples/*.rmc; do
    echo "Running $test..."
    python3 -m renzmc "$test"
    echo "---"
done
```

## ✅ Expected Results

### test_class_complete.rmc
```
✓ Class definition successful
✓ Object creation successful
✓ Method execution successful
✓ Inheritance working
✓ All tests passed
```

### test_database_examples.rmc
```
✓ Database connection successful
✓ CREATE operation successful
✓ READ operation successful
✓ UPDATE operation successful
✓ DELETE operation successful
✓ All tests passed
```

### test_jit_compilation.rmc
```
✓ JIT compiler available
✓ Function compiled successfully
✓ Compiled function executed
✓ Performance improvement detected
✓ All tests passed
```

## 🐛 Troubleshooting

### Test Gagal
1. **Periksa dependencies** - Pastikan semua library terinstall
2. **Periksa environment** - Python version, OS compatibility
3. **Baca error message** - Error message biasanya informatif
4. **Check logs** - Lihat log file untuk detail

### Common Issues

#### JIT Test Gagal
```
Error: numba not found
Solution: pip install numba
```

#### Database Test Gagal
```
Error: sqlite3 not found
Solution: Install sqlite3 atau gunakan database lain
```

#### Class Test Gagal
```
Error: Syntax error
Solution: Update RenzmcLang ke versi terbaru
```

## 📚 Referensi Testing

### Best Practices
1. **Test early, test often**
2. **Write clear test cases**
3. **Test edge cases**
4. **Document expected behavior**
5. **Automate testing**

### Testing Principles
- **Arrange-Act-Assert** pattern
- **Single responsibility** per test
- **Independent tests**
- **Repeatable results**
- **Fast execution**

## 🎓 Belajar dari Test

Test files ini juga berfungsi sebagai:
- **Tutorial** - Cara menggunakan fitur
- **Documentation** - Expected behavior
- **Examples** - Best practices
- **Reference** - Code patterns

## 🔄 Continuous Testing

### Development Workflow
1. Write code
2. Write tests
3. Run tests
4. Fix issues
5. Repeat

### CI/CD Integration
Test files ini dapat diintegrasikan dengan:
- GitHub Actions
- GitLab CI
- Jenkins
- Travis CI

## 📝 Menambahkan Test Baru

### Template Test File
```renzmc
// Test: [Feature Name]
// Description: [What this test does]

tampilkan "=== Testing [Feature] ==="

// Test Case 1
tampilkan "Test 1: [Description]"
// ... test code ...
tampilkan "✓ Test 1 passed"

// Test Case 2
tampilkan "Test 2: [Description]"
// ... test code ...
tampilkan "✓ Test 2 passed"

tampilkan "=== All tests passed ==="
```

### Naming Convention
- `test_[feature]_[aspect].rmc`
- Contoh: `test_http_client_get.rmc`

## 🤝 Kontribusi

Ingin menambahkan test?
1. Buat file test baru
2. Ikuti template di atas
3. Dokumentasikan test cases
4. Update README.md ini
5. Submit pull request

---

**Happy Testing! 🧪**

*Testing is not about finding bugs, it's about preventing them.*