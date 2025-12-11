# HTTP Module

The HTTP module provides comprehensive HTTP client functionality following Python's requests library standards with Indonesian function names.

## Import

```python
dari http impor *
// atau import specific functions
dari http impor get, post, put, delete
// atau import classes
dari http impor HTTPResponse, HTTPSession
```

## HTTP Methods

### get() / ambil()
Performs an HTTP GET request to retrieve data.

**Syntax:**
```python
get(url, params, headers, timeout)
ambil(url, params, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `params` (dict, optional): Query parameters to append to URL
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object containing the result

**Examples:**
```python
dari http impor get, ambil

// Basic GET request
response1 = get("https://api.example.com/users")
data1 = response1.json()

// GET with query parameters
response2 = get("https://api.example.com/users", params={"page": 1, "limit": 10})
data2 = response2.json()

// GET with headers and timeout
headers = {"Authorization": "Bearer token123"}
response3 = get("https://api.example.com/protected", headers=headers, timeout=10)
```

---

### post() / kirim()
Performs an HTTP POST request to send data.

**Syntax:**
```python
post(url, data, json, headers, timeout)
kirim(url, data, json, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `data` (dict/string/bytes, optional): Form data to send
- `json` (dict, optional): JSON data to send
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object containing the result

**Examples:**
```python
dari http impor post, kirim

// POST JSON data
response1 = post("https://api.example.com/users", json={"name": "Budi", "age": 25})
user1 = response1.json()

// POST form data
response2 = post("https://api.example.com/login", data={"username": "admin", "password": "secret"})
result2 = response2.text

// POST with custom headers
headers = {"Content-Type": "application/json"}
response3 = kirim("https://api.example.com/data", json={"key": "value"}, headers=headers)
```

---

### put() / perbarui()
Performs an HTTP PUT request to update data.

**Syntax:**
```python
put(url, data, json, headers, timeout)
perbarui(url, data, json, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `data` (dict/string/bytes, optional): Form data to send
- `json` (dict, optional): JSON data to send
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object containing the result

**Examples:**
```python
dari http impor put, perbarui

// PUT JSON data to update user
response1 = put("https://api.example.com/users/1", json={"name": "Budi Updated"})
updated_user1 = response1.json()

// PUT form data
response2 = put("https://api.example.com/items/1", data={"name": "Updated Item", "price": 100})
result2 = response2.text

// PUT with Indonesian alias
response3 = perbarui("https://api.example.com/users/123", json={"status": "active"})
```

---

### delete() / hapus()
Performs an HTTP DELETE request to remove data.

**Syntax:**
```python
delete(url, headers, timeout)
hapus(url, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object containing the result

**Examples:**
```python
dari http impor delete, hapus

// DELETE a resource
response1 = delete("https://api.example.com/users/1")
success1 = response1.ok()

// DELETE with authentication headers
headers = {"Authorization": "Bearer token123"}
response2 = delete("https://api.example.com/items/456", headers=headers)

// DELETE with Indonesian alias
response3 = hapus("https://api.example.com/temp/789")
```

---

### patch() / tambal()
Performs an HTTP PATCH request to partially update data.

**Syntax:**
```python
patch(url, data, json, headers, timeout)
tambal(url, data, json, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `data` (dict/string/bytes, optional): Form data to send
- `json` (dict, optional): JSON data to send
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object containing the result

**Examples:**
```python
dari http impor patch, tambal

// PATCH partial update
response1 = patch("https://api.example.com/users/1", json={"age": 26})
updated_user1 = response1.json()

// PATCH with Indonesian alias
response2 = tambal("https://api.example.com/profile", json={"bio": "Updated bio"})
```

---

### head() / kepala()
Performs an HTTP HEAD request to retrieve headers only.

**Syntax:**
```python
head(url, headers, timeout)
kepala(url, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object with headers only

**Examples:**
```python
dari http impor head, kepala

// HEAD request to check resource
response1 = head("https://api.example.com/users")
content_type1 = response1.headers["Content-Type"]
content_length1 = response1.headers["Content-Length"]

// HEAD with Indonesian alias
response2 = kepala("https://example.com")
server_info2 = response2.headers
```

---

### options() / opsi()
Performs an HTTP OPTIONS request to retrieve allowed methods.

**Syntax:**
```python
options(url, headers, timeout)
opsi(url, headers, timeout)
```

**Parameters:**
- `url` (string): Target URL
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (integer, optional): Request timeout in seconds (default: 30)

**Returns:**
- HTTPResponse: Response object with allowed methods

**Examples:**
```python
dari http impor options, opsi

// OPTIONS request to check allowed methods
response1 = options("https://api.example.com/users")
allowed_methods1 = response1.headers["Allow"]

// OPTIONS with Indonesian alias
response2 = opsi("https://api.example.com/data")
supported_methods2 = response2.headers
```

## Response Object

The HTTP functions return an HTTPResponse object with the following properties and methods:

### Properties

#### url
The final URL after redirects.

```python
response = get("https://api.example.com")
final_url = response.url
tampilkan final_url
```

#### status_code
HTTP status code of the response.

```python
response = get("https://api.example.com")
code = response.status_code
tampilkan code  // Output: 200
```

#### headers
Dictionary of response headers.

```python
response = get("https://api.example.com")
content_type = response.headers["Content-Type"]
server = response.headers["Server"]
```

### Methods

#### text
Returns the response body as a string.

```python
response = get("https://api.example.com/data")
content = response.text
tampilkan content
```

#### json()
Parses the response body as JSON and returns a dictionary.

```python
response = get("https://api.example.com/users")
data = response.json()
names = data["users"]
```

#### content()
Returns the response body as bytes.

```python
response = get("https://example.com/image.jpg")
image_data = response.content()
// Save to file
file_handler = buka_file("image.jpg", "wb")
file_handler.tulis(image_data)
file_handler.tutup()
```

#### ok()
Returns `benar` if the request was successful (status code 200-299), `salah` otherwise.

```python
response = get("https://api.example.com/users")
jika response.ok()
    tampilkan "Request successful"
lainnya
    tampilkan "Request failed"
selesai
```

#### raise_for_status()
Raises an exception if the status code indicates an error.

```python
response = get("https://api.example.com/users")
response.raise_for_status()  // Will raise HTTPError if status >= 400
```

## Session Management

### HTTPSession
Creates a session for connection pooling and persistent connections.

**Syntax:**
```python
session = HTTPSession()
```

**Methods:**
- `get(url, **kwargs)`
- `post(url, **kwargs)`
- `put(url, **kwargs)`
- `delete(url, **kwargs)`
- `patch(url, **kwargs)`

**Examples:**
```python
dari http impor HTTPSession, buat_sesi

// Create session
session = HTTPSession()
// atau
session = buat_sesi()

// Set session defaults
session.headers["Authorization"] = "Bearer token123"
session.timeout = 15

// Multiple requests with same session
response1 = session.get("https://api.example.com/users")
response2 = session.post("https://api.example.com/data", json={"key": "value"})
response3 = session.put("https://api.example.com/items/1", json={"name": "Updated"})
```

## Utility Functions

### set_default_header() / atur_header_default()
Sets a default header for all HTTP requests.

**Syntax:**
```python
set_default_header(key, value)
atur_header_default(key, value)
```

**Parameters:**
- `key` (string): Header name
- `value` (string): Header value

**Examples:**
```python
dari http impor set_default_header, atur_header_default

// Set default authorization
set_default_header("Authorization", "Bearer token123")

// Set default user agent
atur_header_default("User-Agent", "MyApp/1.0")

// All subsequent requests will include these headers
response = get("https://api.example.com/data")
```

### set_default_timeout() / atur_timeout_default()
Sets a default timeout for all HTTP requests.

**Syntax:**
```python
set_default_timeout(timeout)
atur_timeout_default(timeout)
```

**Parameters:**
- `timeout` (integer): Timeout in seconds

**Examples:**
```python
dari http impor set_default_timeout, atur_timeout_default

// Set default timeout to 10 seconds
set_default_timeout(10)

// Set default timeout with Indonesian alias
atur_timeout_default(15)

// All subsequent requests will use this timeout
response = get("https://api.example.com/data")
```

### create_session() / buat_sesi()
Creates a new HTTP session object.

**Syntax:**
```python
create_session()
buat_sesi()
```

**Returns:**
- HTTPSession: New session object

**Examples:**
```python
dari http impor create_session, buat_sesi

session1 = create_session()
session2 = buat_sesi()
```

## Error Handling

### HTTPError
Exception raised for HTTP request failures.

**Properties:**
- `message`: Error message
- `status_code`: HTTP status code (if available)

**Examples:**
```python
dari http impor get, HTTPError

coba
    response = get("https://invalid-url.example.com")
    response.raise_for_status()
tangkap HTTPError sebagai e
    tampilkan "HTTP Error:", e.message
    jika e.status_code
        tampilkan "Status Code:", e.status_code
selesai
```

## Complete Examples

### REST API Client
```python
dari http impor get, post, put, delete, set_default_header
dari json impor dumps, loads

// Set authentication
set_default_header("Authorization", "Bearer api-token")

// Base API URL
base_url = "https://jsonplaceholder.typicode.com"

// GET all users
response = get(base_url + "/users")
users = response.json()
tampilkan "Total users:", panjang(users)

// POST new user
new_user = {"name": "John Doe", "email": "john@example.com"}
response = post(base_url + "/users", json=new_user)
created_user = response.json()
tampilkan "Created user ID:", created_user["id"]

// PUT update user
updated_user = {"name": "John Updated"}
response = put(base_url + "/users/1", json=updated_user)
tampilkan "Update status:", response.status_code

// DELETE user
response = delete(base_url + "/users/1")
tampilkan "Delete successful:", response.ok()
```

### File Download
```python
dari http impor get
dari os impor path_exists

// Download image
image_url = "https://picsum.photos/800/600"
response = get(image_url)

jika response.ok()
    image_data = response.content()
    filename = "downloaded_image.jpg"
    
    // Save file
    file_handler = buka_file(filename, "wb")
    file_handler.tulis(image_data)
    file_handler.tutup()
    
    tampilkan "Image downloaded as:", filename
lainnya
    tampilkan "Failed to download image"
selesai
```

### Session-based Requests
```python
dari http impor HTTPSession, set_default_header

// Create session with authentication
session = HTTPSession()
session.headers["Authorization"] = "Bearer session-token"
session.timeout = 20

// Multiple requests
response1 = session.get("https://api.example.com/profile")
response2 = session.post("https://api.example.com/posts", json={"title": "New Post"})
response3 = session.put("https://api.example.com/settings", json={"theme": "dark"})

// Check all requests
requests = [response1, response2, response3]
untuk setiap response dari requests
    tampilkan "URL:", response.url, "Status:", response.status_code
selesai
```

## Usage Notes

1. **SSL/TLS**: The module automatically handles SSL/TLS connections but doesn't verify certificates by default for compatibility.

2. **Redirects**: HTTP requests follow redirects by default.

3. **Timeout**: Default timeout is 30 seconds but can be customized per request or globally.

4. **Indonesian Aliases**: All main functions have Indonesian aliases:
   - `ambil()` for `get()`
   - `kirim()` for `post()`
   - `perbarui()` for `put()`
   - `hapus()` for `delete()`
   - `tambal()` for `patch()`
   - `kepala()` for `head()`
   - `opsi()` for `options()`

5. **Content Types**: The module automatically sets appropriate Content-Type headers based on data type.

6. **Error Handling**: Always check `response.ok()` or use `response.raise_for_status()` for proper error handling.

7. **Session Usage**: Use sessions for multiple requests to the same domain for better performance.