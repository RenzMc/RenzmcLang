# Library Regular Expression (re)

## Overview

Library `re` menyediakan fungsi-fungsi untuk operasi regular expression dengan nama fungsi dalam Bahasa Indonesia. Library ini mendukung pattern matching, searching, splitting, replacement, dan validasi teks dengan regex patterns.

## Import Library

```python
dari renzmc.library.re impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.re impor cocok, cari, cari_semua, ganti, validasi_email
```

## Fungsi Matching Dasar

### cocok(pattern, string, flags=0)

Mengecek apakah pattern cocok di awal string.

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dicocokkan
- `flags` (int): Regex flags (opsional)

**Return:**
- `Match object`: Jika cocok, `None` jika tidak

**Contoh:**
```python
// Basic match
result itu cocok(r"Hello", "Hello World")
jika result:
    tampilkan "Pattern cocok di awal"
    tampilkan result.group()  // "Hello"

// No match
result2 itu cocok(r"World", "Hello World")
jika tidak result2:
    tampilkan "Pattern tidak cocok di awal"

// With groups
result3 itu cocok(r"(\w+) (\w+)", "John Doe")
jika result3:
    tampilkan result3.group(1)  // "John"
    tampilkan result3.group(2)  // "Doe"
```

### cari(pattern, string, flags=0)

Mencari pattern dalam string (bukan hanya di awal).

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dicari
- `flags` (int): Regex flags (opsional)

**Return:**
- `Match object`: Jika ditemukan, `None` jika tidak

**Contoh:**
```python
// Search anywhere in string
result itu cari(r"World", "Hello World")
jika result:
    tampilkan "Pattern ditemukan"
    tampilkan result.group()  // "World"

// Search with groups
text itu "Email: user@example.com"
result2 itu cari(r"(\w+)@(\w+\.\w+)", text)
jika result2:
    tampilkan f"Username: {result2.group(1)}"  // "user"
    tampilkan f"Domain: {result2.group(2)}"    // "example.com"

// Case insensitive search
result3 itu cari(r"hello", "Hello World", IGNORECASE)
jika result3:
    tampilkan "Case insensitive match found"
```

### full_cocok(pattern, string, flags=0)

Mengecek apakah seluruh string cocok dengan pattern.

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dicocokkan
- `flags` (int): Regex flags (opsional)

**Return:**
- `Match object`: Jika cocok sempurna, `None` jika tidak

**Contoh:**
```python
// Exact match
result itu full_cocok(r"\d{4}", "1234")
jika result:
    tampilkan "Exact 4 digits match"

// No exact match
result2 itu full_cocok(r"\d{4}", "12345")
jika tidak result2:
    tampilkan "Not exact 4 digits"

// Email validation
email_pattern itu r"[\w\.-]+@[\w\.-]+\.\w+"
result3 itu full_cocok(email_pattern, "user@example.com")
jika result3:
    tampilkan "Valid email format"
```

## Fungsi Pencarian Multiple

### cari_semua(pattern, string, flags=0)

Mencari semua pattern dalam string.

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dicari
- `flags` (int): Regex flags (opsional)

**Return:**
- `list`: List semua matches

**Contoh:**
```python
// Find all numbers
text itu "Prices: 10, 25, 100, 500"
numbers itu cari_semua(r"\d+", text)
tampilkan numbers  // ["10", "25", "100", "500"]

// Find all words
words itu cari_semua(r"\b\w+\b", "Hello world from Python")
tampilkan words  // ["Hello", "world", "from", "Python"]

// Find all emails
email_text itu "Contact: user1@site.com, user2@domain.org"
emails itu cari_semua(r"[\w\.-]+@[\w\.-]+\.\w+", email_text)
tampilkan emails  // ["user1@site.com", "user2@domain.org"]

// With groups (returns tuples)
emails_with_groups itu cari_semua(r"(\w+)@([\w\.-]+)", email_text)
tampilkan emails_with_groups  // [("user1", "site.com"), ("user2", "domain.org")]
```

### cari_iterasi(pattern, string, flags=0)

Mencari pattern dengan iterator (memory efficient untuk large strings).

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dicari
- `flags` (int): Regex flags (opsional)

**Return:**
- `iterator`: Iterator untuk matches

**Contoh:**
```python
// Find all numbers with iterator
text itu "Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
matches itu cari_iterasi(r"\d+", text)

numbers_list itu []
untuk match dalam matches:
    numbers_list.tambah(match.group())

tampilkan numbers_list  // ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

// Process large text efficiently
large_text itu "Word1 word2 word3 word4 word5" * 1000
word_iterator itu cari_iterasi(r"\b\w+\b", large_text)

count itu 0
untuk word dalam word_iterator:
    count += 1
    jika count > 10:  // Process only first 10
        break

tampilkan f"Processed {count} words"
```

## Fungsi Splitting dan Replacement

### bagi(pattern, string, maxsplit=0, flags=0)

Membagi string berdasarkan pattern.

**Parameter:**
- `pattern` (string): Regex pattern
- `string` (string): String untuk dibagi
- `maxsplit` (int): Maximum split (0 untuk unlimited)
- `flags` (int): Regex flags (opsional)

**Return:**
- `list`: List hasil split

**Contoh:**
```python
// Split by whitespace
text itu "Hello   world   from   Python"
words itu bagi(r"\s+", text)
tampilkan words  // ["Hello", "world", "from", "Python"]

// Split by punctuation
sentence itu "Hello, world! How are you?"
parts itu bagi(r"[,.!?]\s*", sentence)
tampilkan parts  // ["Hello", "world", "How", "are", "you", ""]

// Split with maxsplit
data itu "field1,field2,field3,field4"
limited itu bagi(r",", data, maxsplit=2)
tampilkan limited  // ["field1", "field2", "field3,field4"]

// Split by multiple characters
mixed itu "apple;banana|cherry,orange"
fruits itu bagi(r"[;,|]", mixed)
tampilkan fruits  // ["apple", "banana", "cherry", "orange"]
```

### ganti(pattern, replacement, string, count=0, flags=0)

Mengganti pattern dengan replacement string.

**Parameter:**
- `pattern` (string): Regex pattern
- `replacement` (string): String replacement
- `string` (string): String untuk diganti
- `count` (int): Maximum replacement (0 untuk unlimited)
- `flags` (int): Regex flags (opsional)

**Return:**
- `string`: String hasil replacement

**Contoh:**
```python
// Replace all numbers
text itu "Phone: 123-456-7890"
result itu ganti(r"\d", "*", text)
tampilkan result  // "Phone: ***-***-****"

// Replace with count limit
text2 itu "word1 word2 word3 word4"
result2 itu ganti(r"word\d", "REPLACED", text2, count=2)
tampilkan result2  // "REPLACED REPLACED word3 word4"

// Replace whitespace with single space
messy itu "Too    many   spaces"
clean itu ganti(r"\s+", " ", messy)
tampilkan clean  // "Too many spaces"

// Replace with backreferences
html_text itu "<b>Bold</b> and <i>Italic</i>"
no_html itu ganti(r"<(\w+)>(.*?)</\1>", r"\2", html_text)
tampilkan no_html  // "Bold and Italic"
```

### ganti_dengan_fungsi(pattern, replacement_func, string, count=0, flags=0)

Mengganti pattern dengan fungsi.

**Parameter:**
- `pattern` (string): Regex pattern
- `replacement_func` (function): Function untuk replacement
- `string` (string): String untuk diganti
- `count` (int): Maximum replacement (0 untuk unlimited)
- `flags` (int): Regex flags (opsional)

**Return:**
- `string`: String hasil replacement

**Contoh:**
```python
// Uppercase all words
def uppercase_match(match):
    return match.group().upper()

text itu "hello world from python"
result itu ganti_dengan_fungsi(r"\b\w+\b", uppercase_match, text)
tampilkan result  // "HELLO WORLD FROM PYTHON"

// Double all numbers
def double_number(match):
    num = int(match.group())
    return str(num * 2)

numbers itu "Values: 10, 20, 30"
result2 itu ganti_dengan_fungsi(r"\d+", double_number, numbers)
tampilkan result2  // "Values: 20, 40, 60"

// Add prefix to emails
def add_prefix(match):
    email = match.group()
    return f"mailto:{email}"

email_text itu "Contact: user@site.com"
result3 itu ganti_dengan_fungsi(r"[\w\.-]+@[\w\.-]+\.\w+", add_prefix, email_text)
tampilkan result3  // "Contact: mailto:user@site.com"
```

## Fungsi Compilation dan Utilities

### kompile(pattern, flags=0)

Mengompilasi regex pattern untuk penggunaan berulang.

**Parameter:**
- `pattern` (string): Regex pattern
- `flags` (int): Regex flags (opsional)

**Return:**
- `Pattern object`: Compiled pattern

**Contoh:**
```python
// Compile pattern untuk performance
email_pattern itu kompile(r"[\w\.-]+@[\w\.-]+\.\w+")

// Gunakan berulang kali
texts itu [
    "Contact: user@site.com",
    "Email: admin@domain.org",
    "Send to: info@company.net"
]

untuk text dalam texts:
    match itu email_pattern.cari(text)
    jika match:
        tampilkan f"Found: {match.group()}"

// Compile dengan flags
word_pattern itu kompile(r"\b\w+\b", IGNORECASE)
text itu "Hello World"
match2 itu word_pattern.cari(text)
tampilkan match2.group()  // "Hello"
```

### escape(pattern)

Meng-escape semua karakter non-alphanumeric dalam pattern.

**Parameter:**
- `pattern` (string): String untuk di-escape

**Return:**
- `string`: Escaped pattern

**Contoh:**
```python
// Escape special characters
special itu "C:\\Program Files\\MyApp\&quot;
escaped itu escape(special)
tampilkan escaped  // "C:\\\\Program Files\\\\MyApp\\\&quot;

// Escape user input untuk regex
user_input itu "[test] (pattern) + more"
safe_pattern itu escape(user_input)
tampilkan safe_pattern  // "\\\[test\\] \\(pattern\\) \\+ more"

// Gunakan dalam regex
text itu "This is [test] (pattern) + more"
pattern itu f"{safe_pattern}.*"
match itu cari(pattern, text)
jika match:
    tampilkan "Found escaped pattern"
```

## Fungsi Group dan Position

### dapatkan_grup(match, group_num=0)

Mendapatkan grup tertentu dari match object.

**Parameter:**
- `match` (Match object): Match object
- `group_num` (int): Nomor grup (default 0)

**Return:**
- `string`: Group content

**Contoh:**
```python
match itu cocok(r"(\w+) (\w+) (\w+)", "John Doe Smith")
jika match:
    first_name itu dapatkan_grup(match, 1)
    last_name itu dapatkan_grup(match, 2)
    full_match itu dapatkan_grup(match, 0)
    
    tampilkan f"First: {first_name}"   // "John"
    tampilkan f"Last: {last_name}"     // "Doe"
    tampilkan f"Full: {full_match}"    // "John Doe Smith"
```

### dapatkan_semua_grup(match)

Mendapatkan semua grup dari match object.

**Parameter:**
- `match` (Match object): Match object

**Return:**
- `tuple`: Semua groups

**Contoh:**
```python
match itu cocok(r"(\d{4})-(\d{2})-(\d{2})", "2023-12-25")
jika match:
    all_groups itu dapatkan_semua_grup(match)
    tampilkan all_groups  // ("2023", "12", "25")
    
    year, month, day = all_groups
    tampilkan f"Year: {year}, Month: {month}, Day: {day}"
```

### dapatkan_nama_grup(match, name)

Mendapatkan grup berdasarkan nama dari match object.

**Parameter:**
- `match` (Match object): Match object
- `name` (string): Nama grup

**Return:**
- `string`: Group content

**Contoh:**
```python
pattern itu r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match itu cocok(pattern, "2023-12-25")

jika match:
    year itu dapatkan_nama_grup(match, "year")
    month itu dapatkan_nama_grup(match, "month")
    day itu dapatkan_nama_grup(match, "day")
    
    tampilkan f"Date: {day}/{month}/{year}"
```

### dapatkan_posisi(match)

Mendapatkan posisi match dalam string.

**Parameter:**
- `match` (Match object): Match object

**Return:**
- `tuple`: (start, end) positions

**Contoh:**
```python
text itu "Error at line 10, column 25"
match itu cari(r"line \d+", text)

jika match:
    start_pos, end_pos itu dapatkan_posisi(match)
    tampilkan f"Found at position {start_pos}-{end_pos}"
    tampilkan f"Matched text: {text[start_pos:end_pos]}"
```

## Fungsi Validasi Spesifik

### validasi_email(email)

Memvalidasi format email.

**Parameter:**
- `email` (string): Email untuk divalidasi

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
emails itu [
    "user@example.com",
    "invalid.email",
    "user@domain.co.uk",
    "user@.com",
    "user.name@company.org"
]

untuk email dalam emails:
    jika validasi_email(email):
        tampilkan f"✓ Valid: {email}"
    lainnya:
        tampilkan f"✗ Invalid: {email}"
```

### validasi_telepon(phone)

Memvalidasi format nomor telepon Indonesia.

**Parameter:**
- `phone` (string): Nomor telepon untuk divalidasi

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
phones itu [
    "08123456789",
    "+628123456789",
    "021-1234567",
    "0812-3456-7890",
    "123456789",
    "081234567890123"
]

untuk phone dalam phones:
    jika validasi_telepon(phone):
        tampilkan f"✓ Valid: {phone}"
    lainnya:
        tampilkan f"✗ Invalid: {phone}"
```

### validasi_url(url)

Memvalidasi format URL.

**Parameter:**
- `url` (string): URL untuk divalidasi

**Return:**
- `boolean`: True jika valid, False jika tidak

**Contoh:**
```python
urls itu [
    "https://www.example.com",
    "http://site.org/path",
    "ftp://files.server.net",
    "www.invalid.com",
    "not-a-url",
    "https://subdomain.example.co.uk/path?query=value"
]

untuk url dalam urls:
    jika validasi_url(url):
        tampilkan f"✓ Valid: {url}"
    lainnya:
        tampilkan f"✗ Invalid: {url}"
```

## Fungsi Ekstraksi Spesifik

### extract_email(text)

Mengekstrak semua email dari text.

**Parameter:**
- `text` (string): Text untuk diekstrak

**Return:**
- `list`: List email yang ditemukan

**Contoh:**
```python
text itu "Contact: admin@site.com, support@company.org, info@help.net"
emails itu extract_email(text)
tampilkan emails  // ["admin@site.com", "support@company.org", "info@help.net"]
```

### extract_url(text)

Mengekstrak semua URL dari text.

**Parameter:**
- `text` (string): Text untuk diekstrak

**Return:**
- `list`: List URL yang ditemukan

**Contoh:**
```python
text itu "Visit https://example.com or http://site.org for more info"
urls itu extract_url(text)
tampilkan urls  // ["https://example.com", "http://site.org"]
```

### extract_angka(text)

Mengekstrak semua angka dari text.

**Parameter:**
- `text` (string): Text untuk diekstrak

**Return:**
- `list`: List angka yang ditemukan

**Contoh:**
```python
text itu "Prices: $10.50, $25.75, $100.00"
numbers itu extract_angka(text)
tampilkan numbers  // ["10", "50", "25", "75", "100", "00"]
```

### extract_kata(text)

Mengekstrak semua kata dari text.

**Parameter:**
- `text` (string): Text untuk diekstrak

**Return:**
- `list`: List kata yang ditemukan

**Contoh:**
```python
text itu "Hello world! How are you today?"
words itu extract_kata(text)
tampilkan words  // ["Hello", "world", "How", "are", "you", "today"]
```

## Regex Flags

### Constants

- `IGNORECASE`: Case insensitive matching
- `MULTILINE`: Multi-line mode (^ dan $ match line boundaries)
- `DOTALL`: Dot matches all characters including newline
- `VERBOSE`: Allow verbose regex patterns
- `ASCII`: Make \w, \W, \b, \B ASCII-only
- `LOCALE`: Make \w, \W, \b, \B locale-dependent

**Contoh:**
```python
// Case insensitive
result1 itu cari(r"hello", "Hello World", IGNORECASE)

// Multi-line
text itu "First line\nSecond line\nThird line"
result2 itu cari(r"^Second", text, MULTILINE)

// Dotall untuk multiline matching
html itu "<div>Content\nwith newlines</div>"
result3 itu cari(r"<div>.*</div>", html, DOTALL)

// Verbose pattern untuk readability
pattern_verbose itu kompile(r"""
    \b          # Word boundary
    \w+         # One or more word characters
    \s          # Whitespace
    \w+         # Another word
    \b          # Word boundary
""", VERBOSE)

result4 itu pattern_verbose.cari("Hello world")
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.re impor *

tampilkan "=== Demo Regular Expression Library ==="

// 1. Basic matching
tampilkan "\n1. Basic Matching:"
match_result itu cocok(r"Hello", "Hello World")
jika match_result:
    tampilkan f"Match found: {match_result.group()}"

search_result itu cari(r"World", "Hello World")
jika search_result:
    tampilkan f"Search found: {search_result.group()}"

// 2. Group extraction
tampilkan "\n2. Group Extraction:"
text itu "John Doe, age: 30, city: Jakarta"
pattern itu r"(\w+) (\w+), age: (\d+), city: (\w+)"

match itu cocok(pattern, text)
jika match:
    name_parts itu dapatkan_semua_grup(match)
    tampilkan f"Name parts: {name_parts}"
    tampilkan f"First name: {dapatkan_grup(match, 1)}"

// 3. Find all matches
tampilkan "\n3. Find All Matches:"
data_text itu "Products: apple, banana, orange, grape, mango"
fruits itu cari_semua(r"\b\w+\b", data_text)
tampilkan f"Fruits: {fruits}"

// Find numbers
number_text itu "Count: 10, 20, 30, 40, 50"
numbers itu cari_semua(r"\d+", number_text)
tampilkan f"Numbers: {numbers}"

// 4. Splitting
tampilkan "\n4. Splitting:"
messy_text itu "apple,banana;cherry|orange"
fruits_list itu bagi(r"[,;|]", messy_text)
tampilkan f"Split fruits: {fruits_list}"

// Split by whitespace
sentence itu "Too    many   spaces"
words_list itu bagi(r"\s+", sentence)
tampilkan f"Words: {words_list}"

// 5. Replacement
tampilkan "\n5. Replacement:"
original itu "Phone: 123-456-7890"
masked itu ganti(r"\d", "*", original)
tampilkan f"Masked: {masked}"

// Uppercase words
def make_upper(match):
    return match.group().upper()

text itu "hello world from python"
uppercased itu ganti_dengan_fungsi(r"\b\w+\b", make_upper, text)
tampilkan f"Uppercased: {uppercased}"

// 6. Validation
tampilkan "\n6. Validation:"
test_emails itu [
    "valid@email.com",
    "invalid.email",
    "user@domain.co.uk",
    "user@.com"
]

untuk email dalam test_emails:
    status itu "Valid" jika validasi_email(email) lainnya "Invalid"
    tampilkan f"{email}: {status}"

// 7. Extraction
tampilkan "\n7. Extraction:"
contact_text itu "Contacts: admin@site.com, user@domain.org, support@help.net"
extracted_emails itu extract_email(contact_text)
tampilkan f"Extracted emails: {extracted_emails}"

url_text itu "Visit https://example.com and http://site.org"
extracted_urls itu extract_url(url_text)
tampilkan f"Extracted URLs: {extracted_urls}"

// 8. Advanced patterns
tampilkan "\n8. Advanced Patterns:"

// Named groups
log_pattern itu r"(?P<level>\w+): (?P<message>.*)"
log_text itu "ERROR: Database connection failed"
log_match itu cari(log_pattern, log_text)

jika log_match:
    level itu dapatkan_nama_grup(log_match, "level")
    message itu dapatkan_nama_grup(log_match, "message")
    tampilkan f"Log Level: {level}, Message: {message}"

// Lookahead dan lookbehind
password_text itu "Password123 (valid), Pass (invalid)"
password_pattern itu r"(?=.+\d)[A-Za-z\d]{8,}"
valid_passwords itu cari_semua(password_pattern, password_text)
tampilkan f"Valid passwords: {valid_passwords}"

// 9. Compiled patterns untuk performance
tampilkan "\n9. Compiled Patterns:"

// Compile email pattern
email_compiled itu kompile(r"[\w\.-]+@[\w\.-]+\.\w+", IGNORECASE)

emails_text itu [
    "Contact: USER@SITE.COM",
    "Email: admin@domain.org", 
    "Send to: info@company.NET"
]

untuk text dalam emails_text:
    match itu email_compiled.cari(text)
    jika match:
        tampilkan f"Found: {match.group()}"

// 10. Real-world data processing
tampilkan "\n10. Real-world Example:"

// Process log file content
log_content itu """
2023-12-25 10:00:00 INFO: Application started
2023-12-25 10:01:15 ERROR: Database connection failed  
2023-12-25 10:02:30 WARN: Retrying connection
2023-12-25 10:03:00 INFO: Connection established
"""

// Extract log entries
log_pattern itu r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+): (.*)"
log_entries itu cari_semua(log_pattern, log_content)

tampilkan "Log entries:"
untuk entry dalam log_entries:
    timestamp, level, message = entry
    tampilkan f"  [{timestamp}] {level}: {message}")

// Count by level
error_count itu panjang(cari_semua(r"ERROR: .*", log_content))
info_count itu panjang(cari_semua(r"INFO: .*", log_content))
warn_count itu panjang(cari_semua(r"WARN: .*", log_content))

tampilkan f"\nSummary: {info_count} info, {warn_count} warnings, {error_count} errors"

// 11. Indonesian text processing
tampilkan "\n11. Indonesian Text Processing:"
indo_text itu "Jakarta adalah ibu kota Indonesia. Bandung adalah kota kembang."

// Find Indonesian cities (simple example)
cities itu cari_semua(r"\b(Jakarta|Bandung|Surabaya|Medan|Yogyakarta)\b", indo_text)
tampilkan f"Kota yang ditemukan: {cities}"

// Extract words with Indonesian characters
indonesian_words itu cari_semua(r"\b[a-zA-Z]+\b", indo_text)
tampilkan f"Kata-kata: {indonesian_words}"

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **Data Validation**: Email, phone, URL, format validation
2. **Text Processing**: Cleaning dan normalisasi text
3. **Log Analysis**: Parsing dan extracting log information
4. **Web Scraping**: Extracting data dari HTML/text
5. **Data Extraction**: Pulling structured data dari unstructured text
6. **Input Validation**: Form validation di applications
7. **Search and Replace**: Batch text processing
8. **Pattern Recognition**: Identifying patterns dalam large datasets

## Performance Tips

- Gunakan `kompile()` untuk patterns yang digunakan berulang kali
- Gunakan `cari_iterasi()` untuk large text processing
- Specific patterns lebih cepat dari generic ones
- Hindari backtracking berlebihan dalam complex patterns
- Gunakan appropriate flags untuk optimasi matching

## Security Considerations

- **ReDoS Attacks**: Hindari patterns yang bisa cause exponential backtracking
- **Input Validation**: Selalu validate regex patterns dari user input
- **Memory Usage**: Berhati-hati dengan `cari_semua()` pada large texts
- **Time Complexity**: Complex patterns bisa sangat slow

## Common Patterns

### Email Validation
```python
email_pattern itu r"[\w\.-]+@[\w\.-]+\.\w+"
```

### Phone Number (Indonesia)
```python
phone_pattern itu r"(\+62|08)[\d-]{8,12}"
```

### URL Validation
```python
url_pattern itu r"https?://[\w\.-]+\.[a-zA-Z]{2,}"
```

### Indonesian Postal Code
```python
postal_pattern itu r"\d{5}"
```

### Indonesian ID Card (NIK)
```python
nik_pattern itu r"\d{16}"
```

## Error Handling

- Gunakan `coba...tangkap...selesai` untuk regex operations
- `ValueError` untuk invalid regex patterns
- Handle `None` returns dari `cocok()` dan `cari()`
- Validate pattern strings sebelum compilation

## Best Practices

1. Gunakan descriptive variable names untuk patterns
2. Comment complex regex patterns
3. Test patterns dengan various input cases
4. Use raw strings (r"...") untuk regex patterns
5. Consider performance untuk large-scale text processing
6. Use specific patterns daripada overly generic ones
7. Document regex patterns untuk team collaboration