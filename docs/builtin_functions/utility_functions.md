# Utility Functions

This document covers all built-in utility functions available in RenzMcLang. These functions provide common utility operations including hashing, URL encoding/decoding, regular expressions, and Base64 encoding/decoding.

## Hashing Functions

### hash_teks()
Generates hash digest of text using specified algorithm.

**Syntax:**
```python
hash_teks(text, algorithm)
```

**Parameters:**
- `text` (string): Text to hash
- `algorithm` (string, optional): Hash algorithm (default: "sha256")
  - "md5": MD5 hash (32 characters)
  - "sha1": SHA-1 hash (40 characters)
  - "sha256": SHA-256 hash (64 characters) - default
  - "sha512": SHA-512 hash (128 characters)

**Returns:**
- String: Hexadecimal hash digest

**Examples:**
```python
// SHA-256 hashing (default)
password = "hello123"
hash1 = hash_teks(password)
tampilkan hash1              // Output: "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"

// MD5 hashing
hash2 = hash_teks(password, "md5")
tampilkan hash2              // Output: "0d202454fa902f84a640e4d021c5d1b9"

// SHA-1 hashing
hash3 = hash_teks(password, "sha1")
tampilkan hash3              // Output: "88d4266fd4e6338d13b845fcf289579d209c8978"

// SHA-512 hashing
hash4 = hash_teks(password, "sha512")
tampilkan hash4              // 128-character SHA-512 hash

// File integrity check
data = baca_file("data.txt")
file_hash = hash_teks(data, "sha256")
tampilkan f"File hash: {file_hash}"
```

**Error:**
- Raises `ValueError` if algorithm is not supported

---

## URL Encoding/Decoding Functions

### url_encode()
Encodes text for safe URL transmission.

**Syntax:**
```python
url_encode(text)
```

**Parameters:**
- `text` (string): Text to encode for URL

**Returns:**
- String: URL-encoded text

**Examples:**
```python
// Basic URL encoding
url_text = "hello world!"
encoded1 = url_encode(url_text)
tampilkan encoded1           // Output: "hello%20world%21"

// Encode special characters
url_text2 = "user@example.com"
encoded2 = url_encode(url_text2)
tampilkan encoded2           // Output: "user%40example.com"

// Encode query parameters
query = "search=python programming"
encoded3 = url_encode(query)
tampilkan encoded3           // Output: "search%3Dpython%20programming"

// Encode full URL
full_url = "https://example.com/search?q=hello world"
encoded4 = url_encode(full_url)
tampilkan encoded4           // Output: "https%3A//example.com/search%3Fq%3Dhello%20world"

// Build URL with encoded parameters
base_url = "https://api.example.com/users"
params = {"name": "John Doe", "city": "New York"}
encoded_params = url_encode(f"name={params['name']}&city={params['city']}")
full_url = base_url + "?" + encoded_params
tampilkan full_url           // Output: "https://api.example.com/users?name%3DJohn%20Doe%26city%3DNew%20York"
```

---

### url_decode()
Decodes URL-encoded text back to original.

**Syntax:**
```python
url_decode(text)
```

**Parameters:**
- `text` (string): URL-encoded text to decode

**Returns:**
- String: Decoded original text

**Examples:**
```python
// Basic URL decoding
encoded = "hello%20world%21"
decoded1 = url_decode(encoded)
tampilkan decoded1           // Output: "hello world!"

// Decode email
encoded2 = "user%40example.com"
decoded2 = url_decode(encoded2)
tampilkan decoded2           // Output: "user@example.com"

// Decode query parameters
encoded3 = "search%3Dpython%20programming"
decoded3 = url_decode(encoded3)
tampilkan decoded3           // Output: "search=python programming"

// Parse URL parameters
url_str = "name=John%20Doe&city=New%20York"
decoded_url = url_decode(url_str)
tampilkan decoded_url        // Output: "name=John Doe&city=New York"
```

---

## Regular Expression Functions

### regex_match()
Finds first match of pattern in text.

**Syntax:**
```python
regex_match(pattern, text)
```

**Parameters:**
- `pattern` (string): Regular expression pattern
- `text` (string): Text to search in

**Returns:**
- String or None: First matching substring or None if no match

**Examples:**
```python
// Basic pattern matching
text = "The price is $123.45 for item A123."
match1 = regex_match(r"\$\d+\.\d+", text)
tampilkan match1             // Output: "$123.45"

// Find email addresses
email_text = "Contact us at admin@example.com or support@company.org"
match2 = regex_match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email_text)
tampilkan match2             // Output: "admin@example.com"

// Find phone numbers
phone_text = "Call me at 555-123-4567 or 555.987.6543"
match3 = regex_match(r"\d{3}[-.]\d{3}[-.]\d{4}", phone_text)
tampilkan match3             // Output: "555-123-4567"

// Find words starting with specific letter
word_text = "apple banana apricot cherry"
match4 = regex_match(r"\ba\w*", word_text)
tampilkan match4             // Output: "apple"

// No match found
no_match = regex_match(r"\d+", "hello world")
tampilkan no_match           // Output: None
```

---

### regex_replace()
Replaces all occurrences of pattern in text.

**Syntax:**
```python
regex_replace(pattern, replacement, text)
```

**Parameters:**
- `pattern` (string): Regular expression pattern to replace
- `replacement` (string): Replacement text
- `text` (string): Text to perform replacement on

**Returns:**
- String: Text with replacements applied

**Examples:**
```python
// Replace all digits
text = "Order #12345 costs $67.89"
cleaned1 = regex_replace(r"\d", "*", text)
tampilkan cleaned1           // Output: "Order #***** costs $**.**"

// Replace email addresses with placeholder
email_text = "Contact admin@example.com or support@company.org"
masked1 = regex_replace(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[REDACTED]", email_text)
tampilkan masked1            // Output: "Contact [REDACTED] or [REDACTED]"

// Remove HTML tags
html_text = "<p>This is <b>bold</b> text with <a href='#'>link</a></p>"
clean_html = regex_replace(r"<[^>]+>", "", html_text)
tampilkan clean_html         // Output: "This is bold text with link"

// Replace multiple spaces with single space
spaced_text = "This    has    multiple    spaces"
normalized = regex_replace(r"\s+", " ", spaced_text)
tampilkan normalized         // Output: "This has multiple spaces"

// Format phone numbers
phone_text = "Call 555-123-4567 or 555.987.6543"
formatted = regex_replace(r"(\d{3})[-.](\d{3})[-.](\d{4})", r"(\1) \2-\3", phone_text)
tampilkan formatted          // Output: "Call (555) 123-4567 or (555) 987-6543"
```

**Error:**
- Raises `ValueError` if regex pattern is invalid

---

## Base64 Encoding/Decoding Functions

### base64_encode()
Encodes text to Base64 format.

**Syntax:**
```python
base64_encode(text)
```

**Parameters:**
- `text` (string): Text to encode

**Returns:**
- String: Base64 encoded string

**Examples:**
```python
// Basic Base64 encoding
message = "Hello, World!"
encoded1 = base64_encode(message)
tampilkan encoded1           // Output: "SGVsbG8sIFdvcmxkIQ=="

// Encode longer text
long_text = "This is a longer message that will be encoded using Base64"
encoded2 = base64_encode(long_text)
tampilkan encoded2           // Output: Base64 encoded string

// Encode JSON data
json_data = '{"name": "John", "age": 25}'
encoded_json = base64_encode(json_data)
tampilkan encoded_json       // Output: Base64 encoded JSON

// Encode special characters
special = "Special chars: àáâãäåæçèéêë"
encoded_special = base64_encode(special)
tampilkan encoded_special    // Output: Base64 encoded string
```

---

### base64_decode()
Decodes Base64 encoded text back to original.

**Syntax:**
```python
base64_decode(text)
```

**Parameters:**
- `text` (string): Base64 encoded string to decode

**Returns:**
- String: Decoded original text

**Examples:**
```python
// Basic Base64 decoding
encoded = "SGVsbG8sIFdvcmxkIQ=="
decoded1 = base64_decode(encoded)
tampilkan decoded1           // Output: "Hello, World!"

// Decode JSON data
encoded_json = "eyJuYW1lIjogIkpvaG4iLCAiYWdlIjogMjV9"
decoded_json = base64_decode(encoded_json)
tampilkan decoded_json       // Output: '{"name": "John", "age": 25}'

// Decode special characters
encoded_special = "U3BlY2lhbCBjaGFyczogw6DHw6HDocOhw6XDhnOnw6f"
decoded_special = base64_decode(encoded_special)
tampilkan decoded_special    // Output: "Special chars: àáâãäåæçèéêë"

// Handle invalid Base64
coba
    invalid = "Invalid Base64!"
    decoded_invalid = base64_decode(invalid)
except ValueError sebagai e
    tampilkan f"Error: {e}"
selesai
```

**Error:**
- Raises `ValueError` if Base64 string is invalid

---

## Advanced Usage Examples

### Password Security System

```python
// Secure password hashing
fungsi hash_password(password, salt=""):
    // Combine password with salt
    salted_password = password + salt
    // Hash with SHA-256
    hashed = hash_teks(salted_password, "sha256")
    hasil hashed
selesai

// User authentication
fungsi authenticate_user(stored_hash, provided_password, salt=""):
    computed_hash = hash_password(provided_password, salt)
    hasil stored_hash == computed_hash
selesai

// Usage
user_password = "mySecretPass123!"
salt = "user_salt_2024"
stored_hash = hash_password(user_password, salt)

// Login attempt
login_password = "mySecretPass123!"
is_valid = authenticate_user(stored_hash, login_password, salt)
tampilkan f"Login valid: {is_valid}"
```

### URL Parameter Parser

```python
// Parse URL parameters
fungsi parse_url_params(encoded_params):
    params = {}
    
    // Decode the parameters
    decoded = url_decode(encoded_params)
    
    // Split into individual parameters
    pairs = pisah(decoded, "&")
    
    // Process each parameter
    untuk setiap pair dari pairs
        jika "=" di pair
            key_value = pisah(pair, "=")
            key = url_decode(key_value[0])
            value = url_decode(key_value[1])
            params[key] = value
        selesai
    selesai
    
    hasil params
selesai

// Usage
url_string = "name=John%20Doe&email=admin%40example.com&age=25"
parsed_params = parse_url_params(url_string)
tampilkan parsed_params
// Output: {"name": "John Doe", "email": "admin@example.com", "age": "25"}
```

### Text Processing Pipeline

```python
// Complete text processing
fungsi clean_and_secure_text(text):
    // Remove HTML tags
    clean_text = regex_replace(r"<[^>]+>", "", text)
    
    // Normalize whitespace
    normalized = regex_replace(r"\s+", " ", clean_text)
    
    // Remove special characters except basic punctuation
    safe_text = regex_replace(r"[^\w\s.,!?]", "", normalized)
    
    // Generate checksum for integrity
    checksum = hash_teks(safe_text, "md5")
    
    hasil {
        "cleaned_text": safe_text,
        "checksum": checksum,
        "original_length": panjang(text),
        "cleaned_length": panjang(safe_text)
    }
selesai

// Usage
messy_text = "<p>Hello <b>World</b>! @#$% Contact me@john@example.com</p>"
result = clean_and_secure_text(messy_text)

tampilkan "Cleaned text:", result["cleaned_text"]
tampilkan "Checksum:", result["checksum"]
tampilkan "Length reduction:", result["original_length"] - result["cleaned_length"]
```

### Secure Data Transmission

```python
// Secure data package
fungsi create_secure_package(data):
    // Convert to JSON
    json_data = json.dumps(data)
    
    // Encode in Base64
    encoded_data = base64_encode(json_data)
    
    // Create checksum
    checksum = hash_teks(encoded_data, "sha256")
    
    // Create package
    package = {
        "data": encoded_data,
        "checksum": checksum,
        "timestamp": waktu()
    }
    
    hasil package
selesai

// Verify and extract package
fungsi extract_secure_package(package):
    // Verify checksum
    computed_checksum = hash_teks(package["data"], "sha256")
    
    jika computed_checksum != package["checksum"]
        tampilkan "Package integrity check failed!"
        hasil None
    selesai
    
    // Decode data
    try
        json_data = base64_decode(package["data"])
        extracted_data = json.loads(json_data)
        tampilkan "Package verified and extracted successfully"
        hasil extracted_data
    except Exception sebagai e
        tampilkan f"Failed to extract package: {e}"
        hasil None
    selesai
selesai

// Usage
sensitive_data = {"username": "admin", "password": "secret123", "role": "admin"}
secure_package = create_secure_package(sensitive_data)

// Transmit or store secure_package...
// Later, extract and verify
extracted = extract_secure_package(secure_package)
tampilkan extracted
```

## Performance Notes

- **Hash Functions**: SHA-256 provides good balance of security and speed
- **URL Encoding**: Use for web form data and URL parameters
- **Regular Expressions**: Can be computationally expensive for large texts
- **Base64**: Increases data size by approximately 33%

## Security Considerations

1. **Hash Security**: Use SHA-256 or stronger for security applications
2. **Input Validation**: Always validate user input before regex operations
3. **Base64**: Not encryption, only encoding - don't use for sensitive data
4. **URL Safety**: Always encode user input before including in URLs