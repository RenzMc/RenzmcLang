# String Functions

This document covers all built-in string functions available in RenzMcLang. These functions are always available without importing any modules.

## Core String Functions

### huruf_besar()

Converts text to uppercase.

**Syntax:**
```python
huruf_besar(text)
```

**Parameters:**
- `text` (string): The text to convert to uppercase

**Returns:**
- String: Uppercase version of the input text

**Example:**
```python
teks itu "Hello World"
hasil itu huruf_besar(teks)
tampilkan hasil  // Output: "HELLO WORLD"
```

**Error:**
- Raises `TypeError` if argument is not a string

---

### huruf_kecil()

Converts text to lowercase.

**Syntax:**
```python
huruf_kecil(text)
```

**Parameters:**
- `text` (string): The text to convert to lowercase

**Returns:**
- String: Lowercase version of the input text

**Example:**
```python
teks itu "HELLO WORLD"
hasil itu huruf_kecil(teks)
tampilkan hasil  // Output: "hello world"
```

**Error:**
- Raises `TypeError` if argument is not a string

---

### potong()

Extracts a substring from text.

**Syntax:**
```python
potong(text, start, end)
```

**Parameters:**
- `text` (string): The source text
- `start` (integer): Starting index (inclusive)
- `end` (integer, optional): Ending index (exclusive). If omitted, extracts to the end

**Returns:**
- String: The extracted substring

**Examples:**
```python
teks itu "Hello World"
hasil1 itu potong(teks, 6)           // Output: "World"
hasil2 itu potong(teks, 0, 5)        // Output: "Hello"
hasil3 itu potong(teks, -5)          // Output: "World"
```

**Error:**
- Raises `TypeError` if first argument is not a string
- Raises `IndexError` if index is out of range

---

### gabung()

Joins multiple items into a single string with a separator.

**Syntax:**
```python
gabung(separator, item1, item2, ...)
```

**Parameters:**
- `separator` (string): The string to place between items
- `item1, item2, ...` (any): Items to join (automatically converted to strings)

**Returns:**
- String: The concatenated string

**Examples:**
```python
kata1 itu "Hello"
kata2 itu "World"
kata3 itu "2024"

hasil1 itu gabung(" ", kata1, kata2, kata3)    // Output: "Hello World 2024"
hasil2 itu gabung("-", "A", "B", "C")          // Output: "A-B-C"
hasil3 itu gabung("", 1, 2, 3)                 // Output: "123"
```

**Error:**
- Raises `TypeError` if separator is not a string

---

### pisah()

Splits text into a list of substrings.

**Syntax:**
```python
pisah(text, separator)
```

**Parameters:**
- `text` (string): The text to split
- `separator` (string, optional): The delimiter. If omitted, splits on whitespace

**Returns:**
- List: List of substrings

**Examples:**
```python
teks itu "Hello World Python"
hasil1 itu pisah(teks)                    // Output: ["Hello", "World", "Python"]
hasil2 itu pisah(teks, " ")              // Output: ["Hello", "World", "Python"]
hasil3 itu pisah("A,B,C", ",")           // Output: ["A", "B", "C"]
hasil4 itu pisah("A-B-C-D", "-")         // Output: ["A", "B", "C", "D"]
```

**Error:**
- Raises `TypeError` if first argument is not a string

---

### ganti()

Replaces occurrences of a substring with another substring.

**Syntax:**
```python
ganti(text, old, new)
```

**Parameters:**
- `text` (string): The source text
- `old` (string): Substring to replace
- `new` (string): Replacement substring

**Returns:**
- String: Text with replacements made

**Examples:**
```python
teks itu "Hello World World"
hasil1 itu ganti(teks, "World", "RenzMcLang")  // Output: "Hello RenzMcLang RenzMcLang"
hasil2 itu ganti("A-B-C", "-", " ")            // Output: "A B C"
hasil3 itu ganti("123", "2", "X")              // Output: "1X3"
```

**Error:**
- Raises `TypeError` if any argument is not a string

---

### mulai_dengan()

Checks if text starts with a specific prefix.

**Syntax:**
```python
mulai_dengan(text, prefix)
```

**Parameters:**
- `text` (string): The text to check
- `prefix` (string): The prefix to look for

**Returns:**
- Boolean: `benar` if text starts with prefix, `salah` otherwise

**Examples:**
```python
teks itu "Hello World"
hasil1 itu mulai_dengan(teks, "Hello")    // Output: benar
hasil2 itu mulai_dengan(teks, "World")    // Output: salah
hasil3 itu mulai_dengan("Python", "Py")   // Output: benar
```

**Error:**
- Raises `TypeError` if any argument is not a string

---

### akhir_dengan()

Checks if text ends with a specific suffix.

**Syntax:**
```python
akhir_dengan(text, suffix)
```

**Parameters:**
- `text` (string): The text to check
- `suffix` (string): The suffix to look for

**Returns:**
- Boolean: `benar` if text ends with suffix, `salah` otherwise

**Examples:**
```python
teks itu "Hello World"
hasil1 itu akhir_dengan(teks, "World")    // Output: benar
hasil2 itu akhir_dengan(teks, "Hello")    // Output: salah
hasil3 itu akhir_dengan("Python.py", ".py")  // Output: benar
```

**Error:**
- Raises `TypeError` if any argument is not a string

---

### berisi()

Checks if text contains a specific substring.

**Syntax:**
```python
berisi(text, substring)
```

**Parameters:**
- `text` (string): The text to search in
- `substring` (string): The substring to search for

**Returns:**
- Boolean: `benar` if substring is found, `salah` otherwise

**Examples:**
```python
teks itu "Hello World"
hasil1 itu berisi(teks, "World")     // Output: benar
hasil2 itu berisi(teks, "Python")    // Output: salah
hasil3 itu berisi("Python", "thon")  // Output: benar
```

**Error:**
- Raises `TypeError` if any argument is not a string

---

### hapus_spasi()

Removes whitespace from both ends of text.

**Syntax:**
```python
hapus_spasi(text)
```

**Parameters:**
- `text` (string): The text to trim

**Returns:**
- String: Text without leading/trailing whitespace

**Examples:**
```python
teks itu "   Hello World   "
hasil1 itu hapus_spasi(teks)     // Output: "Hello World"
hasil2 itu hapus_spasi("\tText\n")  // Output: "Text"
hasil3 itu hapus_spasi("NoSpace")  // Output: "NoSpace"
```

**Error:**
- Raises `TypeError` if argument is not a string

---

### format_teks()

Formats text using Python's format() method.

**Syntax:**
```python
format_teks(template, arg1, arg2, ...)
```

**Parameters:**
- `template` (string): Format string with placeholders
- `arg1, arg2, ...` (any): Values to substitute into placeholders

**Returns:**
- String: Formatted text

**Examples:**
```python
nama itu "John"
umur itu 25
hasil1 itu format_teks("Nama: {}, Umur: {}", nama, umur)  // Output: "Nama: John, Umur: 25"
hasil2 itu format_teks("Nilai: {value}", value=100)      // Output: "Nilai: 100"
hasil3 itu format_teks("{0} + {1} = {2}", 5, 3, 8)       // Output: "5 + 3 = 8"
```

**Error:**
- Raises `TypeError` if template is not a string
- Raises `ValueError` if format is invalid

## String Validation Functions

### adalah_huruf() / is_alpha()

Checks if text contains only alphabetic characters.

**Syntax:**
```python
adalah_huruf(text)  // atau is_alpha(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only letters, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_huruf("Hello")      // Output: benar
hasil2 itu adalah_huruf("Hello123")   // Output: salah
hasil3 itu adalah_huruf("ABC")        // Output: benar
hasil4 itu adalah_huruf("")           // Output: salah
```

---

### adalah_angka() / is_digit()

Checks if text contains only numeric characters.

**Syntax:**
```python
adalah_angka(text)  // atau is_digit(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only digits, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_angka("123")        // Output: benar
hasil2 itu adalah_angka("123.45")     // Output: salah
hasil3 itu adalah_angka("ABC")        // Output: salah
hasil4 itu adalah_angka("0123456789") // Output: benar
```

---

### adalah_alfanumerik() / is_alnum()

Checks if text contains only alphanumeric characters.

**Syntax:**
```python
adalah_alfanumerik(text)  // atau is_alnum(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only letters and digits, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_alfanumerik("Hello123")   // Output: benar
hasil2 itu adalah_alfanumerik("Hello")      // Output: benar
hasil3 itu adalah_alfanumerik("123")        // Output: benar
hasil4 itu adalah_alfanumerik("Hello-123")  // Output: salah
```

---

### adalah_huruf_kecil() / is_lower()

Checks if text contains only lowercase letters.

**Syntax:**
```python
adalah_huruf_kecil(text)  // atau is_lower(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only lowercase letters, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_huruf_kecil("hello")      // Output: benar
hasil2 itu adalah_huruf_kecil("Hello")      // Output: salah
hasil3 itu adalah_huruf_kecil("hello123")   // Output: salah
hasil4 itu adalah_huruf_kecil("abc")        // Output: benar
```

---

### adalah_huruf_besar() / is_upper()

Checks if text contains only uppercase letters.

**Syntax:**
```python
adalah_huruf_besar(text)  // atau is_upper(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only uppercase letters, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_huruf_besar("HELLO")      // Output: benar
hasil2 itu adalah_huruf_besar("Hello")      // Output: salah
hasil3 itu adalah_huruf_besar("HELLO123")   // Output: salah
hasil4 itu adalah_huruf_besar("ABC")        // Output: benar
```

---

### adalah_spasi() / is_space()

Checks if text contains only whitespace characters.

**Syntax:**
```python
adalah_spasi(text)  // atau is_space(text)
```

**Parameters:**
- `text` (string): The text to validate

**Returns:**
- Boolean: `benar` if text contains only whitespace, `salah` otherwise

**Examples:**
```python
hasil1 itu adalah_spasi(" ")          // Output: benar
hasil2 itu adalah_spasi("\t\n ")      // Output: benar
hasil3 itu adalah_spasi("Hello")      // Output: salah
hasil4 itu adalah_spasi("")           // Output: salah
```

## Usage Notes

1. **Function Aliases**: Many functions have both Indonesian and English names for convenience:
   - `adalah_huruf()` and `is_alpha()`
   - `adalah_angka()` and `is_digit()`
   - `adalah_alfanumerik()` and `is_alnum()`
   - `adalah_huruf_kecil()` and `is_lower()`
   - `adalah_huruf_besar()` and `is_upper()`
   - `adalah_spasi()` and `is_space()`

2. **Unicode Support**: All string functions support Unicode characters.

3. **Error Handling**: Functions validate input types and provide clear error messages in Indonesian.

4. **Performance**: These functions are optimized for common string operations and are directly mapped to Python's string methods.

5. **Immutability**: All string functions return new strings and do not modify the original text.