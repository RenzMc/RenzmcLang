# Modul HTTP

Modul HTTP menyediakan fungsi-fungsi untuk melakukan HTTP requests, mengikuti standar requests library dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari http impor get, post, put, delete, patch
// atau impor semua
dari http impor *
// atau gunakan alias Indonesia
dari http impor ambil, kirim, perbarui, hapus
```

## Fungsi HTTP Utama

### get() / ambil()

Melakukan HTTP GET request untuk mengambil data.

**Sintaks:**
```python
get(url, params, headers, timeout)
ambil(url, params, headers, timeout)
```

**Parameter:**
- `url` (string): URL untuk request
- `params` (dict, opsional): Query parameters
- `headers` (dict, opsional): Additional headers
- `timeout` (integer, opsional): Request timeout dalam detik (default: 30)

**Mengembalikan:**
- HTTPResponse object: Response dari server

**Contoh:**
```python
dari http import get

// GET sederhana
response itu get("https://api.example.com/users")
tampilkan f"Status: {response.status_code}"
tampilkan f"Data: {response.text}"

// GET dengan parameters
response itu get("https://api.example.com/users", params={
    "page": 1,
    "limit": 10
})
data itu response.json()
tampilkan data

// GET dengan headers kustom
response itu get("https://api.example.com/data", headers={
    "Authorization": "Bearer token123",
    "Accept": "application/json"
})
```

---

### post() / kirim()

Melakukan HTTP POST request untuk mengirim data.

**Sintaks:**
```python
post(url, data, json, headers, timeout)
kirim(url, data, json, headers, timeout)
```

**Parameter:**
- `url` (string): URL untuk request
- `data` (string/bytes/dict, opsional): Data untuk POST (form data)
- `json` (dict, opsional): JSON data untuk POST
- `headers` (dict, opsional): Additional headers
- `timeout` (integer, opsional): Request timeout dalam detik (default: 30)

**Mengembalikan:**
- HTTPResponse object: Response dari server

**Contoh:**
```python
dari http import post

// POST dengan JSON data
response itu post("https://api.example.com/users", json={
    "nama": "Budi Santoso",
    "email": "budi@example.com",
    "umur": 25
})
user_baru itu response.json()
tampilkan f"User dibuat: {user_baru}"

// POST dengan form data
response itu post("https://api.example.com/login", data={
    "username": "budi",
    "password": "secret123"
})
tampilkan f"Login status: {response.status_code}"

// POST dengan raw data
response itu post("https://api.example.com/webhook", 
    data='{"event": "user_created", "user_id": 123}',
    headers={"Content-Type": "application/json"}
)
```

---

### put() / perbarui()

Melakukan HTTP PUT request untuk memperbarui data.

**Sintaks:**
```python
put(url, data, json, headers, timeout)
perbarui(url, data, json, headers, timeout)
```

**Parameter:**
- `url` (string): URL untuk request
- `data` (string/bytes/dict, opsional): Data untuk PUT
- `json` (dict, opsional): JSON data untuk PUT
- `headers` (dict, opsional): Additional headers
- `timeout` (integer, opsional): Request timeout dalam detik (default: 30)

**Contoh:**
```python
dari http import put

// PUT dengan JSON data
response itu put("https://api.example.com/users/123", json={
    "nama": "Budi Updated",
    "email": "budi.updated@example.com"
})
user_updated itu response.json()
tampilkan f"User diperbarui: {user_updated}"

// PUT dengan form data
response itu put("https://api.example.com/profile/123", data={
    "nama_lengkap": "Budi Santoso",
    "bio": "Software Developer"
})
```

---

### delete() / hapus()

Melakukan HTTP DELETE request untuk menghapus data.

**Sintaks:**
```python
delete(url, headers, timeout)
hapus(url, headers, timeout)
```

**Parameter:**
- `url` (string): URL untuk request
- `headers` (dict, opsional): Additional headers
- `timeout` (integer, opsional): Request timeout dalam detik (default: 30)

**Contoh:**
```python
dari http import delete

// DELETE user
response itu delete("https://api.example.com/users/123")
tampilkan f"Delete status: {response.status_code}"

// DELETE dengan headers
response itu delete("https://api.example.com/posts/456", headers={
    "Authorization": "Bearer token123"
})
```

---

### patch() / tambal()

Melakukan HTTP PATCH request untuk memperbarui sebagian data.

**Sintaks:**
```python
patch(url, data, json, headers, timeout)
tambal(url, data, json, headers, timeout)
```

**Contoh:**
```python
dari http import patch

// PATCH dengan JSON data
response itu patch("https://api.example.com/users/123", json={
    "status": "active"
})
user_patched itu response.json()
tampilkan f"User dipatch: {user_patched}"
```

---

### head() / kepala()

Melakukan HTTP HEAD request untuk mengambil headers saja.

**Sintaks:**
```python
head(url, headers, timeout)
kepala(url, headers, timeout)
```

**Contoh:**
```python
dari http import head

// HEAD request
response itu head("https://api.example.com/users/123")
tampilkan f"Headers: {response.headers}"
tampilkan f"Status: {response.status_code}"
```

---

### options() / opsi()

Melakukan HTTP OPTIONS request untuk mengecek available methods.

**Sintaks:**
```python
options(url, headers, timeout)
opsi(url, headers, timeout)
```

**Contoh:**
```python
dari http import options

// OPTIONS request
response itu options("https://api.example.com/users")
tampilkan f"Allowed methods: {response.headers.get('Allow', 'Unknown')}"
```

## Kelas HTTPResponse

### Properti

- `url` (string): URL dari response
- `status_code` (integer): HTTP status code
- `headers` (dict): Response headers
- `text` (string): Response body sebagai string

### Metode

- `json()`: Parse response body sebagai JSON
- `content()`: Response body sebagai bytes
- `ok()`: Cek apakah request berhasil (status 200-299)
- `raise_for_status()`: Raise exception jika error

**Contoh Penggunaan:**
```python
dari http import get

response itu get("https://api.example.com/users")

// Cek status
jika response.ok()
    tampilkan "Request berhasil!"
    
    // Ambil data sebagai JSON
    data itu response.json()
    tampilkan f"Jumlah users: {panjang(data)}"
    
    // Tampilkan headers
    tampilkan f"Content-Type: {response.headers['Content-Type']}"
    
    // Ambil raw content
    raw_content itu response.content()
    tampilkan f"Content length: {panjang(raw_content)}"
lainnya
    tampilkan f"Error: {response.status_code}"
    response.raise_for_status()  // Akan raise exception
selesai
```

## Kelas HTTPSession

Digunakan untuk connection pooling dan persistent connections.

**Contoh:**
```python
dari http import create_session

// Buat session
session itu create_session()

// Set headers dan timeout untuk session
session.headers["Authorization"] itu "Bearer token123"
session.timeout it 60

// Gunakan session untuk multiple requests
response1 itu session.get("https://api.example.com/users")
response2 itu session.post("https://api.example.com/data", json={"key": "value"})

// Session akan reuse connection untuk performa lebih baik
```

## Fungsi Utilitas

### set_default_header() / atur_header_default()

Mengatur default header untuk semua requests.

**Sintaks:**
```python
set_default_header(key, value)
atur_header_default(key, value)
```

**Contoh:**
```python
dari http import set_default_header, get

// Set default authorization
set_default_header("Authorization", "Bearer token123")

// Semua request akan include header ini
response itu get("https://api.example.com/protected")
```

---

### set_default_timeout() / atur_timeout_default()

Mengatur default timeout untuk semua requests.

**Sintaks:**
```python
set_default_timeout(timeout)
atur_timeout_default(timeout)
```

**Contoh:**
```python
dari http import set_default_timeout, get

// Set default timeout 60 detik
set_default_timeout(60)

// Semua request akan timeout setelah 60 detik
response itu get("https://api.example.com/slow-endpoint")
```

---

### create_session() / buat_sesi()

Membuat HTTP session object.

**Sintaks:**
```python
create_session()
buat_sesi()
```

**Mengembalikan:**
- HTTPSession object: Session untuk multiple requests

## Contoh Praktis

### API Client

```python
dari http import get, post, create_session

buat fungsi get_user dengan user_id
    response itu get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    jika response.ok()
        hasil response.json()
    lainnya
        hasil {"error": "User tidak ditemukan"}
    selesai
selesai

buat fungsi create_post dengan title, body, user_id
    response itu post("https://jsonplaceholder.typicode.com/posts", json={
        "title": title,
        "body": body,
        "userId": user_id
    })
    
    jika response.ok()
        hasil response.json()
    lainnya
        hasil {"error": "Gagal membuat post"}
    selesai
selesai

// Penggunaan
user itu get_user(1)
tampilkan f"User: {user['name']} ({user['email']})"

post_baru itu create_post("Judul Baru", "Ini konten post", 1)
tampilkan f"Post dibuat dengan ID: {post_baru['id']}"
```

### Webhook Sender

```python
dari http import post, set_default_header

// Konfigurasi webhook
webhook_url itu "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
set_default_header("Content-Type", "application/json")

buat fungsi kirim_notifikasi dengan message, channel
    payload it {
        "text": message,
        "channel": channel,
        "username": "RenzMcBot"
    }
    
    response itu post(webhook_url, json=payload)
    
    jika response.ok()
        tampilkan "Notifikasi terkirim!"
    lainnya
        tampilkan f"Gagal mengirim notifikasi: {response.status_code}"
    selesai
selesai

// Penggunaan
kirim_notifikasi("Hello from RenzMcLang!", "#general")
kirim_notifikasi("Task completed successfully!", "#notifications")
```

### REST API Wrapper

```python
dari http import create_session

buat fungsi buat_api_client dengan base_url, api_key
    session itu create_session()
    session.headers["Authorization"] it f"Bearer {api_key}"
    session.headers["Content-Type"] it "application/json"
    
    api_client it {
        "session": session,
        "base_url": base_url
    }
    hasil api_client
selesai

buat fungsi api_get dengan client, endpoint
    url it client["base_url"] + endpoint
    response it client["session"].get(url)
    
    jika response.ok()
        hasil response.json()
    lainnya
        hasil {"error": f"API Error: {response.status_code}"}
    selesai
selesai

buat fungsi api_post dengan client, endpoint, data
    url it client["base_url"] + endpoint
    response it client["session"].post(url, json=data)
    
    jika response.ok()
        hasil response.json()
    lainnya
        hasil {"error": f"API Error: {response.status_code}"}
    selesai
selesai

// Penggunaan
api itu buat_api_client("https://api.example.com/v1", "secret-api-key")

users itu api_get(api, "/users")
tampilkan f"Users: {users}"

user_baru itu api_post(api, "/users", {
    "name": "John Doe",
    "email": "john@example.com"
})
tampilkan f"User created: {user_baru}"
```

### File Downloader

```python
dari http import get
dari fileio import tulis_file  // Asumsi ada fungsi fileio

buat fungsi download_file dengan url, filename
    tampilkan f"Mengunduh {url}..."
    
    response itu get(url)
    
    jika response.ok()
        // Simpan ke file
        file_content itu response.content()
        tulis_file(filename, file_content)
        tampilkan f"File disimpan sebagai {filename}"
        
        // Tampilkan info
        file_size it panjang(file_content)
        tampilkan f"Ukuran file: {file_size} bytes"
    lainnya
        tampilkan f"Gagal mengunduh: {response.status_code}"
    selesai
selesai

// Penggunaan
download_file("https://example.com/data.json", "downloaded_data.json")
download_file("https://example.com/image.png", "downloaded_image.png")
```

## Error Handling

```python
dari http import get, HTTPError

buat fungsi safe_get dengan url
    coba
        response itu get(url, timeout=10)
        response.raise_for_status()  // Raise exception untuk status error
        
        // Cek apakah response JSON valid
        coba
            data itu response.json()
            hasil {"success": benar, "data": data}
        kecuali
            hasil {"success": benar, "data": response.text}
        selesai
        
    kecuali HTTPError sebagai e
        hasil {"success": salah, "error": f"HTTP Error: {e}"}
    kecuali Exception sebagai e
        hasil {"success": salah, "error": f"Network Error: {e}"}
    selesai
selesai

// Penggunaan
result itu safe_get("https://api.example.com/data")
jika result["success"]
    tampilkan f"Data: {result['data']}"
lainnya
    tampilkan f"Error: {result['error']}"
selesai
```

## Catatan Penggunaan

1. **Impor Diperlukan**: Semua fungsi HTTP harus diimpor dari modul http.

2. **Alias Indonesia**: Fungsi memiliki alias Indonesia:
   - `ambil()` untuk `get()`
   - `kirim()` untuk `post()`
   - `perbarui()` untuk `put()`
   - `hapus()` untuk `delete()`
   - `tambal()` untuk `patch()`
   - `kepala()` untuk `head()`
   - `opsi()` untuk `options()`

3. **SSL**: Modul ini menggunakan SSL context yang tidak verify certificates untuk compatibility. Gunakan dengan hati-hati di production.

4. **Timeout**: Default timeout adalah 30 detik, dapat diubah dengan `set_default_timeout()`.

5. **Headers**: Default User-Agent diset ke "RenzMcLang-HTTP/1.0".

6. **Response Object**: Response menyimpan content dalam memory, hati-hati dengan response yang sangat besar.

7. **Session**: Gunakan session untuk multiple requests ke domain yang sama untuk performa lebih baik.

8. **Error Handling**: Selalu cek `response.ok()` atau gunakan `response.raise_for_status()` untuk error handling.