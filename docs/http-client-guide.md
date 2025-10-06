# 🌐 HTTP Client Guide - RenzMcLang latest version

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)  
**Feature:** NEW in latest version!

---

## 🎯 Overview

RenzMcLang latest version menyediakan built-in HTTP client yang powerful dan mudah digunakan. Tidak perlu import Python libraries - semua fungsi HTTP tersedia langsung!

---

## 🚀 Quick Start

### Basic GET Request

```python
// Simple GET request
response itu http_get("https://jsonplaceholder.typicode.com/posts/1")

// Check status
tampilkan response.status_code  // 200

// Get JSON data
data itu response.json()
tampilkan data["title"]
```

### Basic POST Request

```python
// POST with JSON data
payload itu {
    "title": "Post Baru",
    "body": "Konten post",
    "userId": 1
}

response itu http_post("https://jsonplaceholder.typicode.com/posts", json=payload)
tampilkan response.status_code  // 201
```

---

## 📋 HTTP Methods

### 1. GET Request

#### Basic GET

```python
response itu http_get("https://api.example.com/users")
```

#### GET with Query Parameters

```python
params itu {
    "page": 1,
    "limit": 10,
    "sort": "name"
}

response itu http_get("https://api.example.com/users", params=params)
// URL: https://api.example.com/users?page=1&limit=10&sort=name
```

#### GET with Headers

```python
headers itu {
    "Authorization": "Bearer token123",
    "Accept": "application/json"
}

response itu http_get("https://api.example.com/data", headers=headers)
```

#### GET with Timeout

```python
// Timeout in seconds
response itu http_get("https://api.example.com/data", timeout=10)
```

#### Complete Example

```python
params itu {"category": "tech", "limit": 5}
headers itu {"Authorization": "Bearer token123"}

response itu http_get(
    "https://api.example.com/articles",
    params=params,
    headers=headers,
    timeout=15
)

jika response.ok()
    articles itu response.json()
    untuk setiap article dari articles
        tampilkan article["title"]
    selesai
selesai
```

### 2. POST Request

#### POST with JSON

```python
data itu {
    "nama": "Budi",
    "email": "budi@example.com",
    "umur": 25
}

response itu http_post("https://api.example.com/users", json=data)
```

#### POST with Form Data

```python
form_data itu {
    "username": "budi",
    "password": "secret123"
}

response itu http_post("https://api.example.com/login", data=form_data)
```

#### POST with Headers

```python
headers itu {
    "Authorization": "Bearer token123",
    "Content-Type": "application/json"
}

data itu {"message": "Hello"}

response itu http_post(
    "https://api.example.com/messages",
    json=data,
    headers=headers
)
```

### 3. PUT Request

#### Update Resource

```python
data_update itu {
    "nama": "Budi Updated",
    "email": "budi.new@example.com"
}

response itu http_put("https://api.example.com/users/1", json=data_update)
```

### 4. DELETE Request

#### Delete Resource

```python
response itu http_delete("https://api.example.com/users/1")

jika response.ok()
    tampilkan "User deleted successfully"
selesai
```

#### DELETE with Headers

```python
headers itu {"Authorization": "Bearer token123"}
response itu http_delete("https://api.example.com/users/1", headers=headers)
```

### 5. PATCH Request

#### Partial Update

```python
data_patch itu {
    "email": "newemail@example.com"
}

response itu http_patch("https://api.example.com/users/1", json=data_patch)
```

---

## 📦 Response Object

### Properties

```python
response itu http_get("https://api.example.com/data")

// Status code
tampilkan response.status_code  // 200, 404, 500, etc.

// URL
tampilkan response.url  // Final URL after redirects

// Response text
tampilkan response.text  // Raw response body

// Headers
tampilkan response.headers  // Dict of response headers
```

### Methods

#### `json()` - Parse JSON Response

```python
response itu http_get("https://api.example.com/users")
data itu response.json()  // Parse JSON to dict/list
```

#### `ok()` - Check Success

```python
response itu http_get("https://api.example.com/data")

jika response.ok()
    // Status code is 200-299
    tampilkan "Success!"
kalau_tidak
    tampilkan f"Error: {response.status_code}"
selesai
```

---

## 🔧 Configuration

### Set Default Headers

```python
// Set default headers for all requests
http_set_header("Authorization", "Bearer token123")
http_set_header("User-Agent", "MyApp/1.0")
http_set_header("Accept", "application/json")

// Now all requests will include these headers
response itu http_get("https://api.example.com/data")
```

### Set Default Timeout

```python
// Set default timeout (in seconds)
http_set_timeout(30)

// Now all requests will use 30 second timeout
response itu http_get("https://api.example.com/data")
```

---

## 🇮🇩 Indonesian Aliases

### Available Aliases

```python
// GET
response itu ambil_http("https://api.example.com/data")

// POST
response itu kirim_http("https://api.example.com/users", json=data)

// PUT
response itu perbarui_http("https://api.example.com/users/1", json=data)

// DELETE
response itu hapus_http("https://api.example.com/users/1")
```

### Example with Aliases

```python
// Ambil data
response itu ambil_http("https://jsonplaceholder.typicode.com/users")
users itu response.json()

// Kirim data baru
user_baru itu {"name": "Budi", "email": "budi@example.com"}
response itu kirim_http("https://jsonplaceholder.typicode.com/users", json=user_baru)

// Perbarui data
user_update itu {"name": "Budi Updated"}
response itu perbarui_http("https://jsonplaceholder.typicode.com/users/1", json=user_update)

// Hapus data
response itu hapus_http("https://jsonplaceholder.typicode.com/users/1")
```

---

## 🎯 Common Use Cases

### 1. REST API Client

```python
kelas APIClient:
    konstruktor(base_url, token):
        diri.base_url itu base_url
        http_set_header("Authorization", f"Bearer {token}")
    selesai
    
    metode get(endpoint):
        url itu diri.base_url + endpoint
        response itu http_get(url)
        hasil response.json()
    selesai
    
    metode post(endpoint, data):
        url itu diri.base_url + endpoint
        response itu http_post(url, json=data)
        hasil response.json()
    selesai
    
    metode put(endpoint, data):
        url itu diri.base_url + endpoint
        response itu http_put(url, json=data)
        hasil response.json()
    selesai
    
    metode delete(endpoint):
        url itu diri.base_url + endpoint
        response itu http_delete(url)
        hasil response.ok()
    selesai
selesai

// Usage
client itu APIClient("https://api.example.com", "token123")
users itu client.get("/users")
new_user itu client.post("/users", {"name": "Budi"})
```

### 2. Data Fetching

```python
fungsi fetch_github_user(username):
    url itu f"https://api.github.com/users/{username}"
    
    coba
        response itu http_get(url, timeout=10)
        
        jika response.ok()
            data itu response.json()
            hasil {
                "name": data["name"],
                "bio": data["bio"],
                "repos": data["public_repos"],
                "followers": data["followers"]
            }
        kalau_tidak
            tampilkan f"Error: {response.status_code}"
            hasil kosong
        selesai
    tangkap Exception sebagai e
        tampilkan f"Request failed: {e}"
        hasil kosong
    selesai
selesai

// Usage
user_info itu fetch_github_user("github")
jika user_info
    tampilkan f"Name: {user_info['name']}"
    tampilkan f"Repos: {user_info['repos']}"
selesai
```

### 3. Form Submission

```python
fungsi submit_form(url, form_data):
    headers itu {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response itu http_post(url, data=form_data, headers=headers)
    
    jika response.ok()
        tampilkan "Form submitted successfully"
        hasil benar
    kalau_tidak
        tampilkan f"Form submission failed: {response.status_code}"
        hasil salah
    selesai
selesai

// Usage
form itu {
    "username": "budi",
    "email": "budi@example.com",
    "message": "Hello!"
}

submit_form("https://example.com/contact", form)
```

### 4. File Download

```python
fungsi download_file(url, filename):
    coba
        response itu http_get(url, timeout=60)
        
        jika response.ok()
            tulis_file(filename, response.text)
            tampilkan f"File downloaded: {filename}"
            hasil benar
        kalau_tidak
            tampilkan f"Download failed: {response.status_code}"
            hasil salah
        selesai
    tangkap Exception sebagai e
        tampilkan f"Download error: {e}"
        hasil salah
    selesai
selesai

// Usage
download_file("https://example.com/data.json", "data.json")
```

### 5. API Pagination

```python
fungsi fetch_all_pages(base_url):
    all_data itu []
    page itu 1
    
    selama benar
        params itu {"page": page, "limit": 10}
        response itu http_get(base_url, params=params)
        
        jika tidak response.ok()
            berhenti
        selesai
        
        data itu response.json()
        jika panjang(data) == 0
            berhenti
        selesai
        
        all_data.extend(data)
        page += 1
    selesai
    
    hasil all_data
selesai

// Usage
all_users itu fetch_all_pages("https://api.example.com/users")
tampilkan f"Total users: {panjang(all_users)}"
```

### 6. Webhook Handler

```python
fungsi send_webhook(webhook_url, message):
    payload itu {
        "text": message,
        "timestamp": waktu_sekarang()
    }
    
    coba
        response itu http_post(webhook_url, json=payload, timeout=5)
        hasil response.ok()
    tangkap Exception sebagai e
        tampilkan f"Webhook failed: {e}"
        hasil salah
    selesai
selesai

// Usage
webhook_url itu "https://hooks.slack.com/services/xxx/yyy/zzz"
send_webhook(webhook_url, "Deployment successful!")
```

---

## 🛡️ Error Handling

### Basic Error Handling

```python
coba
    response itu http_get("https://api.example.com/data")
    
    jika response.ok()
        data itu response.json()
        // Process data
    kalau_tidak
        tampilkan f"HTTP Error: {response.status_code}"
    selesai
tangkap Exception sebagai e
    tampilkan f"Request failed: {e}"
selesai
```

### Timeout Handling

```python
coba
    response itu http_get("https://slow-api.example.com", timeout=5)
    data itu response.json()
tangkap TimeoutError sebagai e
    tampilkan "Request timeout after 5 seconds"
tangkap Exception sebagai e
    tampilkan f"Error: {e}"
selesai
```

### Connection Error Handling

```python
coba
    response itu http_get("https://invalid-domain.example.com")
tangkap ConnectionError sebagai e
    tampilkan "Failed to connect to server"
tangkap Exception sebagai e
    tampilkan f"Error: {e}"
selesai
```

### Retry Logic

```python
fungsi fetch_with_retry(url, max_retries=3):
    untuk attempt dari range(max_retries)
        coba
            response itu http_get(url, timeout=10)
            jika response.ok()
                hasil response.json()
            selesai
        tangkap Exception sebagai e
            tampilkan f"Attempt {attempt + 1} failed: {e}"
            jika attempt < max_retries - 1
                tidur(2)  // Wait before retry
            selesai
        selesai
    selesai
    
    hasil kosong
selesai

// Usage
data itu fetch_with_retry("https://api.example.com/data")
```

---

## 💡 Best Practices

### 1. Always Check Response Status

```python
// ✅ Good
response itu http_get(url)
jika response.ok()
    data itu response.json()
kalau_tidak
    tampilkan f"Error: {response.status_code}"
selesai

// ❌ Bad
response itu http_get(url)
data itu response.json()  // Might fail if not 200
```

### 2. Use Timeouts

```python
// ✅ Good
response itu http_get(url, timeout=10)

// ❌ Bad
response itu http_get(url)  // Might hang forever
```

### 3. Handle Errors

```python
// ✅ Good
coba
    response itu http_get(url)
    data itu response.json()
tangkap Exception sebagai e
    tampilkan f"Error: {e}"
selesai

// ❌ Bad
response itu http_get(url)
data itu response.json()  // No error handling
```

### 4. Set Default Headers

```python
// ✅ Good - Set once
http_set_header("Authorization", "Bearer token")
http_set_header("User-Agent", "MyApp/1.0")

// ❌ Bad - Repeat in every request
response itu http_get(url, headers={"Authorization": "Bearer token"})
```

### 5. Use Appropriate HTTP Methods

```python
// ✅ Good
response itu http_get(url)        // For fetching
response itu http_post(url, ...)  // For creating
response itu http_put(url, ...)   // For updating
response itu http_delete(url)     // For deleting

// ❌ Bad
response itu http_get(url + "?action=delete")  // Use DELETE instead
```

---

## 📚 See Also

- [Quick Reference](quick-reference.md) - Quick syntax reference
- [Built-in Functions](builtin-functions.md) - All built-in functions
- [Examples](examples.md) - Code examples
- [Python Integration](python-integration.md) - Python integration

---

## 🎓 Learning Path

### Beginner
1. Simple GET request
2. Check response status
3. Parse JSON response
4. Basic error handling

### Intermediate
1. POST with JSON data
2. Use query parameters
3. Set custom headers
4. Handle timeouts

### Advanced
1. Build API client class
2. Implement retry logic
3. Handle pagination
4. Create webhook handlers

---

**Version: Latest**  
**Last Updated: 2025-10-04**

**Built-in HTTP client makes web development easier than ever! 🚀**