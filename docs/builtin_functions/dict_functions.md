# Dictionary Functions

This document covers all built-in dictionary functions available in RenzMcLang. These functions are always available without importing any modules and provide comprehensive dictionary manipulation capabilities.

## Core Dictionary Functions

### kunci()
Returns all keys from a dictionary as a list.

**Syntax:**
```python
kunci(dictionary)
```

**Parameters:**
- `dictionary` (dict): The dictionary to extract keys from

**Returns:**
- List: List of all keys in the dictionary

**Examples:**
```python
// Basic key extraction
profil = {"nama": "John", "umur": 25, "kota": "Jakarta"}
daftar_kunci = kunci(profil)
tampilkan daftar_kunci         // Output: ["nama", "umur", "kota"]

// Mixed key types
data = {1: "satu", "dua": 2, 3.0: "tiga"}
keys = kunci(data)
tampilkan keys                 // Output: [1, "dua", 3.0]

// Empty dictionary
kosong = {}
empty_keys = kunci(kosong)
tampilkan empty_keys           // Output: []

// Nested dictionary
nested = {"user": {"id": 1}, "config": {"debug": benar}}
top_keys = kunci(nested)
tampilkan top_keys             // Output: ["user", "config"]
```

---

### nilai()
Returns all values from a dictionary as a list.

**Syntax:**
```python
nilai(dictionary)
```

**Parameters:**
- `dictionary` (dict): The dictionary to extract values from

**Returns:**
- List: List of all values in the dictionary

**Examples:**
```python
// Basic value extraction
profil = {"nama": "John", "umur": 25, "kota": "Jakarta"}
daftar_nilai = nilai(profil)
tampilkan daftar_nilai         // Output: ["John", 25, "Jakarta"]

// Mixed value types
data = {"int": 42, "str": "hello", "bool": benar, "list": [1, 2, 3]}
values = nilai(data)
tampilkan values               // Output: [42, "hello", benar, [1, 2, 3]]

// Empty dictionary
kosong = {}
empty_values = nilai(kosong)
tampilkan empty_values         // Output: []

// Dictionary with None values
data_none = {"a": 1, "b": None, "c": "test"}
values_none = nilai(data_none)
tampilkan values_none          // Output: [1, None, "test"]
```

---

### item()
Returns all key-value pairs from a dictionary as a list of tuples.

**Syntax:**
```python
item(dictionary)
```

**Parameters:**
- `dictionary` (dict): The dictionary to extract items from

**Returns:**
- List: List of (key, value) tuples

**Examples:**
```python
// Basic item extraction
profil = {"nama": "John", "umur": 25, "kota": "Jakarta"}
daftar_item = item(profil)
tampilkan daftar_item          // Output: [("nama", "John"), ("umur", 25), ("kota", "Jakarta")]

// Iterate through items
data = {"apple": 3, "banana": 5, "cherry": 2}
items = item(data)
untuk setiap (key, val) dari items
    tampilkan f"{key}: {val}"
selesai
// Output:
// apple: 3
// banana: 5
// cherry: 2

// Mixed key and value types
data = {1: "satu", "dua": 2, 3.0: [1, 2, 3]}
mixed_items = item(data)
tampilkan mixed_items          // Output: [(1, "satu"), ("dua", 2), (3.0, [1, 2, 3])]

// Empty dictionary
kosong = {}
empty_items = item(kosong)
tampilkan empty_items          // Output: []
```

---

### hapus_kunci()
Removes a specific key from a dictionary.

**Syntax:**
```python
hapus_kunci(dictionary, key)
```

**Parameters:**
- `dictionary` (dict): The dictionary to remove from
- `key` (any): The key to remove

**Returns:**
- Dict: The modified dictionary (in-place operation)

**Examples:**
```python
// Basic key removal
data = {"nama": "John", "umur": 25, "kota": "Jakarta"}
hasil = hapus_kunci(data, "umur")
tampilkan data                 // Output: {"nama": "John", "kota": "Jakarta"}
tampilkan hasil                // Output: {"nama": "John", "kota": "Jakarta"}

// Remove numeric key
numbers = {1: "satu", 2: "dua", 3: "tiga"}
hapus_kunci(numbers, 2)
tampilkan numbers              // Output: {1: "satu", 3: "tiga"}

// Remove string key
config = {"debug": benar, "port": 8080, "host": "localhost"}
hapus_kunci(config, "debug")
tampilkan config               // Output: {"port": 8080, "host": "localhost"}

// Attempt to remove non-existent key
data = {"a": 1, "b": 2}
coba hapus_kunci(data, "c")    // Error: Kunci 'c' tidak ditemukan dalam dictionary
```

**Error:**
- Raises `KeyError` if the key is not found in the dictionary

## Advanced Dictionary Operations

### Common Patterns

```python
// Dictionary iteration patterns
data = {"apple": 3, "banana": 5, "cherry": 2}

// Iterate using kunci()
untuk setiap key dari kunci(data)
    value = data[key]
    tampilkan f"{key}: {value}"
selesai

// Iterate using nilai() 
untuk setiap value dari nilai(data)
    tampilkan f"Value: {value}"
selesai

// Iterate using item()
untuk setiap (key, value) dari item(data)
    tampilkan f"{key} => {value}"
selesai

// Dictionary filtering
scores = {"math": 90, "english": 85, "science": 95}
passed_keys = []
untuk setiap (subject, score) dari item(scores)
    jika score >= 90
        tambah(passed_keys, subject)
    selesai
selesai
tampilkan passed_keys          // Output: ["math", "science"]
```

### Dictionary Transformations

```python
// Transform keys to uppercase
data = {"name": "John", "age": 25}
upper_keys = {}
untuk setiap (key, value) dari item(data)
    new_key = huruf_besar(key)
    upper_keys[new_key] = value
selesai
tampilkan upper_keys           // Output: {"NAME": "John", "AGE": 25}

// Filter dictionary values
numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
even_numbers = {}
untuk setiap (key, value) dari item(numbers)
    jika value % 2 == 0
        even_numbers[key] = value
    selesai
selesai
tampilkan even_numbers         // Output: {"b": 2, "d": 4}

// Merge dictionaries using kunci() and nilai()
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {}
untuk setiap key dari kunci(dict1)
    merged[key] = dict1[key]
selesai
untuk setiap key dari kunci(dict2)
    merged[key] = dict2[key]
selesai
tampilkan merged               // Output: {"a": 1, "b": 2, "c": 3, "d": 4}
```

## Performance Notes

- **kunci()**: Returns a new list, O(n) complexity where n is number of keys
- **nilai()**: Returns a new list, O(n) complexity where n is number of values  
- **item()**: Returns a new list of tuples, O(n) complexity
- **hapus_kunci()**: Modifies dictionary in-place, O(1) average case for hash table operations

## Best Practices

1. **Use item() for iteration**: Most efficient way to iterate through key-value pairs
2. **Avoid unnecessary conversions**: Access dictionary directly when you don't need lists
3. **Check key existence**: Use `di` operator before calling `hapus_kunci()` to avoid KeyError
4. **Memory efficiency**: Large dictionaries may consume significant memory when converted to lists