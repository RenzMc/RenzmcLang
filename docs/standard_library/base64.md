# Library Base64

## Overview

Library `base64` menyediakan fungsi-fungsi untuk encoding dan decoding data dalam format Base64. Library ini sangat berguna untuk mengubah data biner menjadi teks yang dapat dikirim melalui media yang hanya mendukung teks.

## Import Library

```python
dari renzmc.library.base64 impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.base64 impor encode_base64, decode_base64
```

## Fungsi-fungsi Tersedia

### encode_base64(data)

Mengencode string atau bytes menjadi format Base64.

**Parameter:**
- `data` (string/bytes): Data yang akan di-encode

**Return:**
- `string`: String Base64 yang sudah di-encode

**Contoh:**
```python
// Encode string
teks itu "Hello, World!"
hasil itu encode_base64(teks)
tampilkan hasil  // Output: "SGVsbG8sIFdvcmxkIQ=="

// Encode bytes langsung
data_bytes itu b"Data biner"
hasil_bytes itu encode_base64(data_bytes)
tampilkan hasil_bytes
```

### decode_base64(encoded_data)

Mengdecode string Base64 kembali ke bentuk aslinya.

**Parameter:**
- `encoded_data` (string): String Base64 yang akan di-decode

**Return:**
- `string`: Data asli yang sudah di-decode

**Contoh:**
```python
// Decode string
encoded itu "SGVsbG8sIFdvcmxkIQ=="
hasil itu decode_base64(encoded)
tampilkan hasil  // Output: "Hello, World!"

// Error handling
coba
    hasil itu decode_base64("invalid_base64")
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### encode_base64_bytes(data)

Mengencode data menjadi Base64 dalam format bytes.

**Parameter:**
- `data` (string/bytes): Data yang akan di-encode

**Return:**
- `bytes`: Bytes Base64 yang sudah di-encode

**Contoh:**
```python
teks itu "Hello, World!"
hasil_bytes itu encode_base64_bytes(teks)
tampilkan hasil_bytes  // Output: b"SGVsbG8sIFdvcmxkIQ=="
```

### decode_base64_bytes(encoded_data)

Mengdecode Base64 bytes kembali ke bentuk bytes asli.

**Parameter:**
- `encoded_data` (bytes/string): Base64 bytes yang akan di-decode

**Return:**
- `bytes`: Bytes asli yang sudah di-decode

**Contoh:**
```python
encoded_bytes itu b"SGVsbG8sIFdvcmxkIQ=="
hasil_bytes itu decode_base64_bytes(encoded_bytes)
tampilkan hasil_bytes  // Output: b"Hello, World!"
```

### encode_base64_urlsafe(data)

Mengencode data menjadi URL-safe Base64 (tanpa karakter + dan /).

**Parameter:**
- `data` (string/bytes): Data yang akan di-encode

**Return:**
- `string`: String URL-safe Base64

**Contoh:**
```python
teks itu "Hello, World!"
hasil itu encode_base64_urlsafe(teks)
tampilkan hasil  // Output: "SGVsbG8sIFdvcmxkIQ"
```

### decode_base64_urlsafe(encoded_data)

Mengdecode URL-safe Base64 string.

**Parameter:**
- `encoded_data` (string): URL-safe Base64 string

**Return:**
- `string`: Data asli yang sudah di-decode

**Contoh:**
```python
encoded itu "SGVsbG8sIFdvcmxkIQ"
hasil itu decode_base64_urlsafe(encoded)
tampilkan hasil  // Output: "Hello, World!"
```

### encode_base64_file(file_path)

Mengencode seluruh isi file menjadi Base64.

**Parameter:**
- `file_path` (string): Path ke file yang akan di-encode

**Return:**
- `string`: Base64 dari isi file

**Contoh:**
```python
coba
    hasil itu encode_base64_file("data.txt")
    tampilkan f"File encoded: {potong(hasil, 0, 50)}..."
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### decode_base64_ke_file(encoded_data, file_path)

Mengdecode Base64 dan menyimpannya ke file.

**Parameter:**
- `encoded_data` (string): Base64 yang akan di-decode
- `file_path` (string): Path untuk menyimpan file hasil

**Contoh:**
```python
encoded itu "SGVsbG8sIFdvcmxkIQ=="
coba
    decode_base64_ke_file(encoded, "hasil.txt")
    tampilkan "File berhasil disimpan!"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### base64_valid(encoded_data)

Memeriksa apakah string merupakan Base64 yang valid.

**Parameter:**
- `encoded_data` (string): String yang akan dicek

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
// Cek Base64 valid
valid1 itu base64_valid("SGVsbG8sIFdvcmxkIQ==")
tampilkan valid1  // Output: True

// Cek Base64 tidak valid
valid2 itu base64_valid("invalid_string!")
tampilkan valid2  // Output: False
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.base64 impor *

tampilkan "=== Demo Base64 Library ==="

// 1. Encode dan decode string sederhana
teks_asli itu "Ini adalah contoh teks untuk di-encode ke Base64"
encoded itu encode_base64(teks_asli)
decoded itu decode_base64(encoded)

tampilkan f"Teks asli: {teks_asli}"
tampilkan f"Encoded: {encoded}"
tampilkan f"Decoded: {decoded}"
tampilkan f"Valid: {base64_valid(encoded)}"
tampilkan ""

// 2. URL-safe Base64 untuk URL
data_url itu "user:password"
encoded_url itu encode_base64_urlsafe(data_url)
tampilkan f"URL-safe Base64: {encoded_url}"

// 3. File operations
coba
    // Buat file test
    tampilkan "Test file" >> test.txt
    
    // Encode file
    file_encoded itu encode_base64_file("test.txt")
    tampilkan f"File encoded: {potong(file_encoded, 0, 30)}..."
    
    // Decode ke file baru
    decode_base64_ke_file(file_encoded, "test_decoded.txt")
    
    // Baca file hasil
    isi_file itu baca("test_decoded.txt")
    tampilkan f"Isi file decoded: {isi_file}"
tangkap e
    tampilkan f"Error file operations: {e}"
selesai

tampilkan "=== Demo Selesai ==="
```

## Use Cases Umum

1. **Email Attachments**: Mengencode file lampiran untuk email
2. **Data Transmission**: Mengirim data biner melalui API yang hanya menerima teks
3. **URL Parameters**: Menyimpan data dalam URL parameter dengan aman
4. **Configuration Storage**: Menyimpan konfigurasi biner dalam format teks
5. **Cryptography**: Base encoding untuk enkripsi dan hashing

## Error Handling

Semua fungsi decoding akan melempar exception jika:
- Input tidak valid sebagai Base64
- File tidak ditemukan (untuk operasi file)
- Terjadi kesalahan I/O

Gunakan blok `coba...tangkap...selesai` untuk menangani error dengan baik.

## Performa Tips

- Gunakan `encode_base64_bytes` dan `decode_base64_bytes` untuk data biner besar
- Untuk file besar, pertimbangkan untuk memproses dalam chunks
- URL-safe Base64 sedikit lebih lambat dari Base64 standar