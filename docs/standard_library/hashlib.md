# Library Hashlib

## Overview

Library `hashlib` menyediakan fungsi-fungsi untuk hashing data dengan berbagai algoritma kriptografi. Library ini mendukung algoritma seperti MD5, SHA family, BLAKE2, SHA3, serta fitur tambahan seperti HMAC, salted hashing, dan file hashing.

## Import Library

```python
dari renzmc.library.hashlib impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.hashlib impor hash_md5, hash_sha256, hash_file_sha256
```

## Fungsi Hash Dasar

### hash_md5(data)

Generate MD5 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: MD5 hash hexadecimal string (32 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_md5_result itu hash_md5(teks)
tampilkan hash_md5_result  // Output: "ed076287532e86365e841e92bfc50d8c"

// Hash bytes langsung
data_bytes itu b"Data biner"
hash_bytes itu hash_md5(data_bytes)
tampilkan hash_bytes
```

### hash_sha1(data)

Generate SHA1 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA1 hash hexadecimal string (40 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha1_result itu hash_sha1(teks)
tampilkan hash_sha1_result  // Output: "0a4d55a8d778e5022fab701977c5d840bbc486d0"
```

### hash_sha224(data)

Generate SHA224 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA224 hash hexadecimal string (56 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha224_result itu hash_sha224(teks)
tampilkan hash_sha224_result
```

### hash_sha256(data)

Generate SHA256 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA256 hash hexadecimal string (64 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha256_result itu hash_sha256(teks)
tampilkan hash_sha256_result  // Output: "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
```

### hash_sha384(data)

Generate SHA384 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA384 hash hexadecimal string (96 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha384_result itu hash_sha384(teks)
tampilkan hash_sha384_result
```

### hash_sha512(data)

Generate SHA512 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA512 hash hexadecimal string (128 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha512_result itu hash_sha512(teks)
tampilkan hash_sha512_result
```

## Algoritma BLAKE2

### hash_blake2b(data, digest_size=64)

Generate BLAKE2b hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash
- `digest_size` (int): Ukuran digest (default 64, max 64)

**Return:**
- `string`: BLAKE2b hash hexadecimal string

**Contoh:**
```python
teks itu "Hello, World!"
hash_blake2b_result itu hash_blake2b(teks)
tampilkan hash_blake2b_result

// Custom digest size
hash_custom itu hash_blake2b(teks, digest_size=32)
tampilkan hash_custom
```

### hash_blake2s(data, digest_size=32)

Generate BLAKE2s hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash
- `digest_size` (int): Ukuran digest (default 32, max 32)

**Return:**
- `string`: BLAKE2s hash hexadecimal string

**Contoh:**
```python
teks itu "Hello, World!"
hash_blake2s_result itu hash_blake2s(teks)
tampilkan hash_blake2s_result
```

## Algoritma SHA3

### hash_sha3_224(data)

Generate SHA3-224 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA3-224 hash hexadecimal string (56 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha3_224_result itu hash_sha3_224(teks)
tampilkan hash_sha3_224_result
```

### hash_sha3_256(data)

Generate SHA3-256 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA3-256 hash hexadecimal string (64 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha3_256_result itu hash_sha3_256(teks)
tampilkan hash_sha3_256_result
```

### hash_sha3_384(data)

Generate SHA3-384 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA3-384 hash hexadecimal string (96 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha3_384_result itu hash_sha3_384(teks)
tampilkan hash_sha3_384_result
```

### hash_sha3_512(data)

Generate SHA3-512 hash dari data.

**Parameter:**
- `data` (string/bytes): Data yang akan di-hash

**Return:**
- `string`: SHA3-512 hash hexadecimal string (128 karakter)

**Contoh:**
```python
teks itu "Hello, World!"
hash_sha3_512_result itu hash_sha3_512(teks)
tampilkan hash_sha3_512_result
```

## File Hashing

### hash_file_md5(file_path)

Generate MD5 hash dari file.

**Parameter:**
- `file_path` (string): Path ke file

**Return:**
- `string`: MD5 hash hexadecimal string

**Contoh:**
```python
coba
    file_hash itu hash_file_md5("data.txt")
    tampilkan f"MD5 hash file: {file_hash}"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### hash_file_sha256(file_path)

Generate SHA256 hash dari file.

**Parameter:**
- `file_path` (string): Path ke file

**Return:**
- `string`: SHA256 hash hexadecimal string

**Contoh:**
```python
coba
    file_hash itu hash_file_sha256("document.pdf")
    tampilkan f"SHA256 hash file: {file_hash}"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### hash_file_chunked(file_path, algorithm="sha256", chunk_size=8192)

Generate hash dari file dengan chunked reading (efisien untuk file besar).

**Parameter:**
- `file_path` (string): Path ke file
- `algorithm` (string): Algoritma hash ('md5', 'sha1', 'sha256', dll)
- `chunk_size` (int): Ukuran chunk untuk dibaca (default 8192 bytes)

**Return:**
- `string`: Hash hexadecimal string

**Contoh:**
```python
// Hash file besar dengan chunks
coba
    hash_file itu hash_file_chunked("large_video.mp4", "sha256", 65536)
    tampilkan f"Hash file besar: {hash_file}"
    
    // Gunakan algoritma berbeda
    hash_md5_file itu hash_file_chunked("data.bin", "md5")
    tampilkan f"MD5 hash: {hash_md5_file}"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

## HMAC dan Salted Hashing

### hmac_hash(data, key, algorithm="sha256")

Generate HMAC hash menggunakan secret key.

**Parameter:**
- `data` (string/bytes): Data untuk di-hash
- `key` (string/bytes): Secret key
- `algorithm` (string): Algoritma hash ('md5', 'sha1', 'sha256', dll)

**Return:**
- `string`: HMAC hexadecimal string

**Contoh:**
```python
data itu "Important message"
secret_key itu "my_secret_key"

// Generate HMAC
hmac_result itu hmac_hash(data, secret_key)
tampilkan f"HMAC SHA256: {hmac_result}"

// Gunakan algoritma berbeda
hmac_md5 itu hmac_hash(data, secret_key, "md5")
tampilkan f"HMAC MD5: {hmac_md5}"

// Verifikasi integritas data
hmac_verify itu hmac_hash(data, secret_key)
data_modified itu "Important message!"
hmac_invalid itu hmac_hash(data_modified, secret_key)

tampilkan f"Original valid: {hmac_verify == hmac_result}"
tampilkan f"Modified invalid: {hmac_invalid != hmac_result}"
```

### buat_salt(length=32)

Generate random salt untuk hashing.

**Parameter:**
- `length` (int): Panjang salt dalam bytes (default 32)

**Return:**
- `string`: Salt sebagai hexadecimal string

**Contoh:**
```python
// Buat salt default (32 bytes)
salt1 itu buat_salt()
tampilkan f"Salt 1: {salt1}"

// Buat salt custom length
salt2 itu buat_salt(16)
tampilkan f"Salt 2: {salt2}"

// Salt selalu berbeda
salt3 itu buat_salt()
tampilkan f"Salt 3: {salt3}"
tampilkan f"Salt unique: {salt1 != salt2 dan salt2 != salt3}"
```

### hash_with_salt(data, salt=None, algorithm="sha256")

Generate hash dengan salt.

**Parameter:**
- `data` (string/bytes): Data untuk di-hash
- `salt` (string): Salt (jika None, akan dibuat random)
- `algorithm` (string): Algoritma hash

**Return:**
- `tuple`: (hash, salt)

**Contoh:**
```python
password itu "user_password_123"

// Hash dengan salt otomatis
hash_result, salt_used itu hash_with_salt(password)
tampilkan f"Hash: {hash_result}"
tampilkan f"Salt: {salt_used}"

// Hash dengan salt tertentu
custom_salt itu "a1b2c3d4e5f6"
hash_custom, salt_returned itu hash_with_salt(password, custom_salt)
tampilkan f"Hash custom: {hash_custom}"
tampilkan f"Salt returned: {salt_returned}"

// Hash sama akan berbeda dengan salt berbeda
hash1, salt1 itu hash_with_salt(password)
hash2, salt2 itu hash_with_salt(password)
tampilkan f"Hashes different: {hash1 != hash2}"
```

### verify_hash_with_salt(data, hash_value, salt, algorithm="sha256")

Verify hash dengan salt.

**Parameter:**
- `data` (string): Original data
- `hash_value` (string): Hash untuk diverifikasi
- `salt` (string): Salt yang digunakan
- `algorithm` (string): Algoritma hash

**Return:**
- `boolean`: True jika hash cocok

**Contoh:**
```python
password itu "secret_password"

// Hash password
stored_hash, salt itu hash_with_salt(password)
tampilkan f"Stored hash: {stored_hash}"
tampilkan f"Salt: {salt}"

// Verifikasi password benar
is_valid itu verify_hash_with_salt(password, stored_hash, salt)
tampilkan f"Password valid: {is_valid}"

// Verifikasi password salah
wrong_password itu "wrong_password"
is_invalid itu verify_hash_with_salt(wrong_password, stored_hash, salt)
tampilkan f"Password invalid: {is_invalid}"
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.hashlib impor *

tampilkan "=== Demo Hashlib Library ==="

// 1. Berbagai algoritma hash
tampilkan "\n1. Algorithm Comparison:"
data itu "Hello, RenzMcLang!"

hashes itu {
    "MD5": hash_md5(data),
    "SHA1": hash_sha1(data),
    "SHA256": hash_sha256(data),
    "SHA512": hash_sha512(data),
    "BLAKE2b": hash_blake2b(data),
    "SHA3-256": hash_sha3_256(data)
}

untuk algo, hash_value dalam hashes.items():
    tampilkan f"{algo}: {potong(hash_value, 0, 20)}... ({panjang(hash_value)} chars)"

// 2. File hashing
tampilkan "\n2. File Hashing:"
coba
    // Buat test file
    "Test content for hashing" >> test_file.txt
    
    // Hash file
    file_hash_md5 itu hash_file_md5("test_file.txt")
    file_hash_sha256 itu hash_file_sha256("test_file.txt")
    
    tampilkan f"File MD5: {file_hash_md5}"
    tampilkan f"File SHA256: {file_hash_sha256}"
    
    // Hash dengan chunks
    chunked_hash itu hash_file_chunked("test_file.txt", "sha1")
    tampilkan f"Chunked SHA1: {chunked_hash}"
tangkap e
    tampilkan f"File error: {e}"
selesai

// 3. HMAC untuk integritas data
tampilkan "\n3. HMAC for Data Integrity:"
message itu "Secure transaction data"
secret_key itu "transaction_key_2024"

hmac_signature itu hmac_hash(message, secret_key)
tampilkan f"HMAC signature: {hmac_signature}"

// Simulasi verifikasi
received_message itu "Secure transaction data"
is_valid_transaction itu verify_hash_with_salt(received_message, hmac_signature, secret_key)
tampilkan f"Transaction valid: {is_valid_transaction}"

// 4. Password hashing dengan salt
tampilkan "\n4. Password Security:"
user_password itu "MySecurePassword123!"

// Hash password untuk penyimpanan
stored_hash, stored_salt itu hash_with_salt(user_password, algorithm="sha256")
tampilkan f"Password stored (hash): {potong(stored_hash, 0, 20)}...")
tampilkan f"Password stored (salt): {stored_salt}"

// Login verification
login_attempt itu "MySecurePassword123!"
login_success itu verify_hash_with_salt(login_attempt, stored_hash, stored_salt)
tampilkan f"Login successful: {login_success}"

// Wrong password attempt
wrong_login itu "WrongPassword"
login_fail itu verify_hash_with_salt(wrong_login, stored_hash, stored_salt)
tampilkan f"Login failed: {login_fail}"

// 5. Hash comparison untuk deduplication
tampilkan "\n5. Data Deduplication:"
file_contents itu [
    "Content A",
    "Content B", 
    "Content A",  // Duplicate
    "Content C"
]

hash_map itu {}
untuk idx, content dalam enumerate(file_contents):
    content_hash itu hash_sha256(content)
    jika content_hash dalam hash_map
        duplicate_idx itu hash_map[content_hash]
        tampilkan f"File {idx} duplicate dengan file {duplicate_idx}"
    lainnya
        hash_map[content_hash] = idx
        tampilkan f"File {idx} unique: {potong(content_hash, 0, 10)}..."
    selesai

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **Password Storage**: Hash dengan salt untuk keamanan password
2. **Data Integrity**: HMAC untuk verifikasi integritas data
3. **File Verification**: Hash file untuk mendeteksi korupsi
4. **Data Deduplication**: Identifikasi data duplikat dengan hash
5. **Digital Signatures**: Foundation untuk signature schemes
6. **Checksum**: Verifikasi download dan transfer file
7. **Blockchain**: Hash chaining untuk immutability
8. **Caching**: Hash keys untuk efficient lookup

## Security Considerations

- **MD5 dan SHA1**: Tidak disarankan untuk keamanan (collision vulnerable)
- **SHA256**: Minimum yang direkomendasikan untuk keamanan
- **SHA512**: Lebih aman untuk critical applications
- **Salt**: Selalu gunakan salt untuk password hashing
- **HMAC**: Gunakan untuk integrity verification, bukan hash biasa
- **Random Salt**: Gunakan `buat_salt()` untuk salt yang cryptographically secure

## Performa Tips

- SHA256 umumnya memberikan balance kecepatan/keamanan yang baik
- BLAKE2 seringkali lebih cepat dari SHA family
- Gunakan `hash_file_chunked()` untuk file besar (>100MB)
- Salt default 32 bytes (256 bits) cukup untuk keamanan
- HMAC sedikit lebih lambat dari hash biasa karena secret key

## Error Handling

Semua fungsi file hashing akan melempar exception jika:
- File tidak ditemukan (`FileNotFoundError`)
- Tidak ada akses read (`PermissionError`)
- Algoritma tidak didukung (`ValueError`)
- Error I/O lainnya (`ValueError`)

Gunakan blok `coba...tangkap...selesai` untuk handling yang baik.