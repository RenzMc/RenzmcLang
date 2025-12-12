# Library urllib

## Overview

Library `urllib` menyediakan fungsi-fungsi lengkap untuk URL handling dan manipulation dengan nama fungsi dalam Bahasa Indonesia. Library ini mencakup URL parsing, encoding/decoding, URL building, parameter handling, dan utility functions untuk web development.

## Import Library

```python
dari renzmc.library.urllib impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.urllib impor parse_url, buat_url, encode_url, gabung_url
```

## URL Parsing dan Building

### parse_url(url)

Mem-parse URL menjadi komponen-komponennya.

**Parameter:**
- `url` (string): URL string untuk di-parse

**Return:**
- `dict`: Komponen URL (scheme, netloc, path, params, query, fragment, username, password, hostname, port)

**Contoh:**
```python
// Basic URL parsing
url itu "https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section"
parsed itu parse_url(url)

tampilkan f"Scheme: {parsed['scheme']}"        // "https"
tampilkan f"Netloc: {parsed['netloc']}"        // "www.example.com:8080"
tampilkan f"Path: {parsed['path']}"            // "/path/to/page"
tampilkan f"Query: {parsed['query']}"          // "param1=value1&param2=value2"
tampilkan f"Fragment: {parsed['fragment']}"    // "section"
tampilkan f"Hostname: {parsed['hostname']}"    // "www.example.com"
tampilkan f"Port: {parsed['port']}"            // 8080

// URL dengan credentials
auth_url itu "ftp://user:pass@ftp.example.com/files/data.zip"
auth_parsed itu parse_url(auth_url)
tampilkan f"Username: {auth_parsed['username']}"  // "user"
tampilkan f"Password: {auth_parsed['password']}"  // "pass"

// Indonesian website URL
indo_url itu "https://katalog.perpusnas.go.id/search?q=indonesia&page=2"
indo_parsed itu parse_url(indo_url)
tampilkan f"Domain: {indo_parsed['hostname']}"     // "katalog.perpusnas.go.id"
tampilkan f"Path: {indo_parsed['path']}"           // "/search"
tampilkan f"Query: {indo_parsed['query']}"         // "q=indonesia&page=2"
```

### buat_url(scheme, netloc, path="", params="", query="", fragment=")

Membuat URL dari komponen-komponennya.

**Parameter:**
- `scheme` (string): Scheme (http, https, ftp, dll)
- `netloc` (string): Network location (domain:port)
- `path` (string): Path
- `params` (string): Parameters
- `query` (string): Query string
- `fragment` (string): Fragment

**Return:**
- `string`: URL lengkap

**Contoh:**
```python
// Basic URL building
url itu buat_url("https", "www.example.com", "/path/page", "", "param=value", "section")
tampilkan url  // "https://www.example.com/path/page?param=value#section"

// API endpoint
api_url itu buat_url(
    "https",
    "api.example.com",
    "/v1/users",
    "",
    "limit=10&offset=20",
    ""
)
tampilkan api_url  // "https://api.example.com/v1/users?limit=10&offset=20"

// Indonesian government service
gov_url itu buat_url(
    "https",
    "service.go.id",
    "/data/statistik",
    "",
    "tahun=2023&provinsi=DKI",
    ""
)
tampilkan gov_url  // "https://service.go.id/data/statistik?tahun=2023&provinsi=DKI"
```

## Encoding dan Decoding

### encode_url(params)

Meng-encode parameter ke URL-encoded string.

**Parameter:**
- `params` (dict/list): Dictionary atau list of tuples

**Return:**
- `string`: URL-encoded string

**Contoh:**
```python
// Encode dari dictionary
params itu {"name": "John Doe", "age": "30", "city": "Jakarta"}
encoded itu encode_url(params)
tampilkan encoded  // "name=John+Doe&age=30&city=Jakarta"

// Encode dari list of tuples (preserves order)
param_list itu [
    ("search", "buku indonesia"),
    ("category", "sastra"),
    ("year", "2023")
]
encoded_list itu encode_url(param_list)
tampilkan encoded_list  // "search=buku+indonesia&category=sastra&year=2023"

// Complex parameters
complex_params itu {
    "filter[category]": "books",
    "filter[year]": "2023",
    "sort": "title",
    "order": "asc"
}
encoded_complex itu encode_url(complex_params)
tampilkan encoded_complex
```

### decode_url(encoded_string)

Meng-decode URL-encoded string.

**Parameter:**
- `encoded_string` (string): URL-encoded string

**Return:**
- `dict`: Parameters sebagai dictionary

**Contoh:**
```python
// Decode query string
query itu "name=John+Doe&age=30&city=Jakarta"
decoded itu decode_url(query)

tampilkan f"Name: {decoded['name']}"    // "John Doe"
tampilkan f"Age: {decoded['age']}"      // "30"
tampilkan f"City: {decoded['city']}"    // "Jakarta"

// Decode Indonesian content
indo_query itu "judul=laskar+pelangi&penulis=andi+hirata"
decoded_indo itu decode_url(indo_query)
tampilkan f"Judul: {decoded_indo['judul']}"       // "laskar pelangi"
tampilkan f"Penulis: {decoded_indo['penulis']}"   // "andi hirata"
```

### encode_component(component)

Meng-encode URL component (khusus untuk path, query, dll).

**Parameter:**
- `component` (string): String component untuk di-encode

**Return:**
- `string`: URL-encoded component

**Contoh:**
```python
// Encode path component
path itu "/files/buku indonesia.pdf"
encoded_path itu encode_component(path)
tampilkan encoded_path  // "/files/buku%20indonesia.pdf"

// Encode Indonesian text
indo_text itu "katalog perpustakaan nasional"
encoded_text itu encode_component(indo_text)
tampilkan encoded_text  // "katalog%20perpustakaan%20nasional"

// Encode special characters
special itu "hello world! @#$%"
encoded_special itu encode_component(special)
tampilkan encoded_special  // "hello%20world%21%20%40%23%24%25"
```

### decode_component(encoded_component)

Meng-decode URL component.

**Parameter:**
- `encoded_component` (string): URL-encoded component

**Return:**
- `string`: Decoded component

**Contoh:**
```python
// Decode path component
encoded_path itu "/files/buku%20indonesia.pdf"
decoded_path itu decode_component(encoded_path)
tampilkan decoded_path  // "/files/buku indonesia.pdf"

// Decode Indonesian text
encoded_text itu "katalog%20perpustakaan%20nasional"
decoded_text itu decode_component(encoded_text)
tampilkan decoded_text  // "katalog perpustakaan nasional"
```

## URL Manipulation

### gabung_url(base_url, *paths)

Menggabungkan base URL dengan path-path menggunakan proper URL joining.

**Parameter:**
- `base_url` (string): Base URL
- `*paths` (string): Path-path untuk digabungkan

**Return:**
- `string`: URL lengkap

**Contoh:**
```python
// Basic URL joining
base itu "https://api.example.com"
full_url itu gabung_url(base, "v1", "users", "123")
tampilkan full_url  // "https://api.example.com/v1/users/123"

// Join dengan trailing slash
base2 itu "https://cdn.example.com/"
image_url itu gabung_url(base2, "images", "books", "cover.jpg")
tampilkan image_url  // "https://cdn.example.com/images/books/cover.jpg"

// Indonesian site
indo_base itu "https://perpusnas.go.id"
search_url itu gabung_url(indo_base, "search", "books", "indonesia")
tampilkan search_url  // "https://perpusnas.go.id/search/books/indonesia"

// Multiple path joining
paths itu ["api", "v2", "data", "statistik", "provinsi"]
final_url itu gabung_url("https://data.go.id", *paths)
tampilkan final_url  // "https://data.go.id/api/v2/data/statistik/provinsi"
```

## URL Component Extraction

### dapatkan_scheme(url)

Mendapatkan scheme dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: URL scheme

**Contoh:**
```python
scheme1 itu dapatkan_scheme("https://example.com")
tampilkan scheme1  // "https"

scheme2 itu dapatkan_scheme("ftp://files.example.com")
tampilkan scheme2  // "ftp"

scheme3 itu dapatkan_scheme("mailto:user@example.com")
tampilkan scheme3  // "mailto"
```

### dapatkan_domain(url)

Mendapatkan domain/hostname dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: Domain hostname

**Contoh:**
```python
domain1 itu dapatkan_domain("https://www.example.com/path")
tampilkan domain1  // "www.example.com"

domain2 itu dapatkan_domain("https://api.service.gov.id/v1/data")
tampilkan domain2  // "api.service.gov.id"

domain3 itu dapatkan_domain("ftp://files.server.net:21/files")
tampilkan domain3  // "files.server.net"
```

### dapatkan_path(url)

Mendapatkan path dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: URL path

**Contoh:**
```python
path1 itu dapatkan_path("https://example.com/api/users")
tampilkan path1  // "/api/users"

path2 itu dapatkan_path("https://perpusnas.go.id/search/books/indonesia")
tampilkan path2  // "/search/books/indonesia"

path3 itu dapatkan_path("https://cdn.example.com/files/data.json")
tampilkan path3  // "/files/data.json"
```

### dapatkan_query(url)

Mendapatkan query string dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: Query string

**Contoh:**
```python
query1 itu dapatkan_query("https://example.com/search?q=python&lang=en")
tampilkan query1  // "q=python&lang=en"

query2 itu dapatkan_query("https://api.data.go.id/v1/statistik?tahun=2023&provinsi=DKI")
tampilkan query2  // "tahun=2023&provinsi=DKI"
```

## Query String Operations

### parse_query(query_string)

Meng-parse query string menjadi dictionary.

**Parameter:**
- `query_string` (string): Query string untuk di-parse

**Return:**
- `dict`: Parsed query parameters

**Contoh:**
```python
// Parse basic query
query itu "name=John&age=30&city=Jakarta"
parsed itu parse_query(query)

tampilkan f"Name: {parsed['name']}"    // "John"
tampilkan f"Age: {parsed['age']}"      // "30"
tampilkan f"City: {parsed['city']}"    // "Jakarta"

// Parse Indonesian query
indo_query itu "judul=laskar+pelangi&penulis=andi+hirata&tahun=2005"
parsed_indo itu parse_query(indo_query)

tampilkan f"Judul: {parsed_indo['judul']}"     // "laskar pelangi"
tampilkan f"Penulis: {parsed_indo['penulis']}" // "andi hirata"
tampilkan f"Tahun: {parsed_indo['tahun']}"     // "2005"
```

### buat_query(params)

Membuat query string dari parameters.

**Parameter:**
- `params` (dict): Parameters dictionary

**Return:**
- `string`: Query string

**Contoh:**
```python
// Basic query building
params itu {"search": "buku indonesia", "limit": "10", "page": "1"}
query_string itu buat_query(params)
tampilkan query_string  // "search=buku+indonesia&limit=10&page=1"

// API parameters
api_params itu {
    "api_key": "abc123",
    "format": "json",
    "language": "id"
}
api_query itu buat_query(api_params)
tampilkan api_query  // "api_key=abc123&format=json&language=id"
```

## URL Validation dan Utilities

### url_valid(url)

Mengecek apakah URL valid.

**Parameter:**
- `url` (string): URL untuk dicek

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
// Valid URLs
valid1 itu url_valid("https://www.example.com")
valid2 itu url_valid("ftp://files.server.org")
valid3 itu url_valid("https://api.service.gov.id/v1/data")

// Invalid URLs
invalid1 itu url_valid("not-a-url")
invalid2 itu url_valid("http://")
invalid3 itu url_valid("://missing-scheme.com")

tampilkan f"Valid 1: {valid1}")
tampilkan f"Valid 2: {valid2}")
tampilkan f"Valid 3: {valid3}")
tampilkan f"Invalid 1: {invalid1}")
tampilkan f"Invalid 2: {invalid2}")
tampilkan f"Invalid 3: {invalid3}")
```

### dapatkan_extension(url)

Mendapatkan file extension dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: File extension

**Contoh:**
```python
ext1 itu dapatkan_extension("https://example.com/files/document.pdf")
tampilkan ext1  // ".pdf"

ext2 itu dapatkan_extension("https://cdn.site.org/images/cover.jpg")
tampilkan ext2  // ".jpg"

ext3 itu dapatkan_extension("https://api.data.go.id/v1/statistik.json")
tampilkan ext3  // ".json"

// No extension
ext4 itu dapatkan_extension("https://example.com/path/to/file")
tampilkan f"No extension: {ext4 == ''}")
```

### dapatkan_filename(url)

Mendapatkan filename dari URL.

**Parameter:**
- `url` (string): URL input

**Return:**
- `string`: Filename

**Contoh:**
```python
filename1 itu dapatkan_filename("https://example.com/files/report.pdf")
tampilkan filename1  // "report.pdf"

filename2 itu dapatkan_filename("https://cdn.images.com/cover-book.jpg")
tampilkan filename2  // "cover-book.jpg"

filename3 itu dapatkan_filename("https://data.gov.id/datasets/statistik-2023.csv")
tampilkan filename3  // "statistik-2023.csv"

// Path without file
filename4 itu dapatkan_filename("https://example.com/path/to/")
tampilkan f"No filename: {filename4 == ''}")
```

### escape_url(url)

Meng-escape URL untuk keamanan.

**Parameter:**
- `url` (string): URL untuk di-escape

**Return:**
- `string`: Escaped URL

**Contoh:**
```python
// URL dengan special characters
unsafe_url itu "https://example.com/search?q=hello world&path=/my folder/file.txt"
escaped_url itu escape_url(unsafe_url)
tampilkan escaped_url
// "https://example.com/search?q=hello%20world&path=/my%20folder/file.txt"

// Indonesian content
indo_url itu "https://perpusnas.go.id/search?q=buku indonesia&kategori=sastra"
escaped_indo itu escape_url(indo_url)
tampilkan escaped_indo
// "https://perpusnas.go.id/search?q=buku%20indonesia&kategori=sastra"
```

### download_url(url, destination="")

Mengunduh file dari URL (simplified implementation).

**Parameter:**
- `url` (string): URL untuk didownload
- `destination` (string): Path tujuan (opsional)

**Return:**
- `string`: Path file yang didownload atau content

**Contoh:**
```python
// Download ke memory (simplified)
coba
    content itu download_url("https://api.example.com/data.json")
    tampilkan f"Downloaded: {potong(content, 0, 100)}..."
tangkap e
    tampilkan f"Download failed: {e}")
selesai

// Download ke file
coba
    file_path itu download_url("https://example.com/data.txt", "downloaded_data.txt")
    tampilkan f"Downloaded to: {file_path}")
tangkap e
    tampilkan f"Download failed: {e}")
selesai
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.urllib impor *

tampilkan "=== Demo urllib Library ===")

// 1. URL parsing
tampilkan "\n1. URL Parsing:")
sample_url itu "https://api.example.com:8080/v1/users?limit=10&page=2&sort=name#results"
parsed itu parse_url(sample_url)

tampilkan f"URL: {sample_url}")
tampilkan f"Scheme: {parsed['scheme']}")
tampilkan f"Host: {parsed['hostname']}")
tampilkan f"Port: {parsed['port']}")
tampilkan f"Path: {parsed['path']}")
tampilkan f"Query: {parsed['query']}")
tampilkan f"Fragment: {parsed['fragment']}")

// 2. URL building
tampilkan "\n2. URL Building:")
api_base itu "https://data.go.id"
endpoint itu "/v1/statistik"
params itu {"tahun": "2023", "provinsi": "DKI", "kategori": "pendidikan"}

query_string itu buat_query(params)
full_url itu gabung_url(api_base, endpoint) + "?" + query_string
tampilkan f"Built URL: {full_url}")

// 3. Encoding dan decoding
tampilkan "\n3. Encoding dan Decoding:")
indonesian_data itu {
    "judul": "Laskar Pelangi",
    "penulis": "Andrea Hirata",
    "penerbit": "Bentang Pustaka",
    "tahun": "2005"
}

encoded_params itu encode_url(indonesian_data)
tampilkan f"Encoded: {encoded_params}")

decoded_params itu decode_url(encoded_params)
tampilkan f"Decoded title: {decoded_params['judul']}")
tampilkan f"Decoded author: {decoded_params['penulis']}")

// 4. Component encoding
tampilkan "\n4. Component Encoding:")
path_with_spaces itu "/katalog buku/indonesia/sastra modern.pdf"
encoded_path itu encode_component(path_with_spaces)
tampilkan f"Original path: {path_with_spaces}")
tampilkan f"Encoded path: {encoded_path}")

decoded_path itu decode_component(encoded_path)
tampilkan f"Decoded back: {decoded_path}")

// 5. URL manipulation
tampilkan "\n5. URL Manipulation:")
base_urls itu [
    "https://api.example.com",
    "https://cdn.example.com/",
    "https://service.gov.id"
]

untuk base dalam base_urls:
    user_url itu gabung_url(base, "v2", "users", "profile")
    tampilkan f"From {base}: {user_url}")

// 6. Query operations
tampilkan "\n6. Query Operations:")
search_query itu "q=pemrograman python&lang=id&page=1&per_page=20"
parsed_query itu parse_query(search_query)

tampilkan f"Original query: {search_query}")
tampilkan "Parsed parameters:")
untuk key, value dalam parsed_query.items():
    tampilkan f"  {key}: {value}")

// Rebuild dengan modifications
new_params itu parsed_query
new_params["page"] = "2"
new_query itu buat_query(new_params)
tampilkan f"Modified query: {new_query}")

// 7. URL validation
tampilkan "\n7. URL Validation:")
test_urls itu [
    "https://www.example.com",
    "ftp://files.server.org",
    "invalid-url",
    "http://",
    "https://perpusnas.go.id/search",
    "not-a-url-at-all"
]

untuk test_url dalam test_urls:
    is_valid itu url_valid(test_url)
    status itu "✓ Valid" jika is_valid lainnya "✗ Invalid"
    tampilkan f"{test_url}: {status}")

// 8. File operations
tampilkan "\n8. File Operations:")
file_urls itu [
    "https://example.com/documents/report.pdf",
    "https://cdn.images.com/cover-book.jpg",
    "https://data.gov.id/datasets/statistik-2023.csv",
    "https://site.org/path/to/folder/"
]

untuk file_url dalam file_urls:
    filename itu dapatkan_filename(file_url)
    extension itu dapatkan_extension(file_url)
    tampilkan f"URL: {file_url}")
    tampilkan f"  Filename: {filename or '(none)'}")
    tampilkan f"  Extension: {extension or '(none)'}")

// 9. Indonesian web services
tampilkan "\n9. Indonesian Web Services:")

// Perpustakaan Nasional
perpus_url itu gabung_url(
    "https://katalog.perpusnas.go.id",
    "search"
) + "?" + encode_url({"q": "sejarah indonesia", "page": "2"})

tampilkan f"Perpusnas URL: {perpus_url}")

// Data Portal Indonesia
data_portal itu gabung_url(
    "https://data.go.id",
    "data",
    "statistik"
) + "?" + encode_url({"tahun": "2023", "provinsi": "Jawa Barat"})

tampilkan f"Data Portal URL: {data_portal}")

// BPBD API
bpbd_url itu buat_url(
    "https",
    "bnpb-inacaws.bmkg.go.id",
    "api",
    "",
    "wilayah=jakarta&format=json",
    ""
)
tampilkan f"BPBD URL: {bpbd_url}")

// 10. URL security
tampilkan "\n10. URL Security:")
unsafe_urls itu [
    "https://example.com/search?q=hello world&type=pdf",
    "https://site.org/path/my folder/file.txt",
    "https://api.service.com/data?name=John Doe&city=New York"
]

untuk unsafe dalam unsafe_urls:
    safe_url itu escape_url(unsafe)
    tampilkan f"Unsafe:  {unsafe}")
    tampilkan f"Safe:    {safe_url}")
    tampilkan "")

// 11. Advanced URL operations
tampilkan "\n11. Advanced Operations:")

// URL normalization
urls_to_normalize itu [
    "HTTP://Example.COM/Path",
    "https://example.com/path/",
    "https://example.com/path//to//file"
]

tampilkan "URL normalization:")
untuk url dalam urls_to_normalize:
    normalized_url itu huruf_kecil(url)
    // Remove double slashes (simplified)
    normalized_url itu normalized_url.ganti("//", "/")
    tampilkan f"  Original: {url}")
    tampilkan f"  Normalized: {normalized_url}")

// URL comparison
url1 itu "https://example.com/path?param=value"
url2 itu "https://EXAMPLE.COM/path?param=value")

parsed1 itu parse_url(url1)
parsed2 itu parse_url(url2))

same_scheme itu parsed1["scheme"] == parsed2["scheme"]
same_host itu huruf_kecil(parsed1["hostname"]) == huruf_kecil(parsed2["hostname"])
same_path itu parsed1["path"] == parsed2["path"]

tampilkan f"\nURL Comparison:")
tampilkan f"URL 1: {url1}")
tampilkan f"URL 2: {url2}")
tampilkan f"Same scheme: {same_scheme}")
tampilkan f"Same host: {same_host}")
tampilkan f"Same path: {same_path}")

// 12. Real-world API example
tampilkan "\n12. Real-world API Example:")

// Build complex API request
api_config itu {
    "base_url": "https://api.example.com",
    "version": "v2",
    "endpoint": "users",
    "params": {
        "limit": "50",
        "offset": "0",
        "sort": "name",
        "order": "asc",
        "fields": "id,name,email,created_at"
    }
}

// Build URL
api_url itu gabung_url(
    api_config["base_url"],
    api_config["version"],
    api_config["endpoint"]
)

query_string itu buat_query(api_config["params"])
final_api_url itu api_url + "?" + query_string

tampilkan f"API URL: {final_api_url}")

// Parse dan validate
jika url_valid(final_api_url):
    parsed_api itu parse_url(final_api_url)
    tampilkan f"API Host: {parsed_api['hostname']}")
    tampilkan f"API Path: {parsed_api['path']}")
    
    params_parsed itu parse_query(parsed_api["query"])
    tampilkan "API Parameters:")
    untuk key, value dalam params_parsed.items():
        tampilkan f"  {key}: {value}")
lainnya:
    tampilkan "Invalid API URL!")

tampilkan "\n=== Demo Selesai ===")
```

## Use Cases Umum

1. **Web Development**: Building dan parsing URLs untuk web applications
2. **API Integration**: Constructing API endpoints dan query parameters
3. **Data Scraping**: Parsing URLs dari web pages dan normalizing
4. **URL Shortening**: Parsing dan manipulating URL components
5. **Security**: Validating dan sanitizing URLs dari user input
6. **CDN Integration**: Building CDN URLs untuk asset management
7. **SEO**: Creating clean dan canonical URLs
8. **Indonesian Services**: Integration dengan Indonesian government APIs

## Security Considerations

- Selalu validasi URLs dari user input dengan `url_valid()`
- Gunakan `escape_url()` untuk URLs yang mengandung special characters
- Hati-hati dengan file extensions dari untrusted sources
- Sanitize query parameters sebelum database operations
- Use HTTPS untuk sensitive data transmission

## Performance Tips

- Gunakan `gabung_url()` untuk consistent URL joining
- Cache parsed URLs untuk repeated operations
- Use dictionary untuk parameter building (lebih efisien)
- Validate URLs early dalam request processing
- Avoid repeated parsing dari same URL

## Error Handling

- Gunakan `coba...tangkap...selesai` untuk URL operations
- `ValueError` untuk invalid URL formats
- Handle network errors untuk download operations
- Validate parameters sebelum URL building
- Graceful fallback untuk malformed URLs

## Indonesian Context Support

Library ini dirancang untuk dukungan penuh konteks Indonesia:
- Examples dengan Indonesian government services
- Support untuk Indonesian text encoding/decoding
- Integration patterns untuk Indonesian APIs
- Cultural context dalam URL examples
- Indonesian domain examples (.go.id, .sch.id, dll)

## Best Practices

1. Gunakan `parse_url()` untuk URL decomposition
2. Build URLs dengan `buat_url()` untuk consistency
3. Encode parameters dengan `encode_url()` untuk safety
4. Validate URLs dengan `url_valid()` sebelum processing
5. Use proper URL joining dengan `gabung_url()`
6. Handle Indonesian characters dengan proper encoding
7. Sanitize user-provided URLs sebelum usage