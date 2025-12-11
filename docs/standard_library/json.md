# JSON Module

The JSON module provides comprehensive JSON (JavaScript Object Notation) encoding and decoding functionality following Python's json module standards with Indonesian function names.

## Import

```python
dari json impor *
// atau import specific functions
dari json impor loads, dumps, load, dump
// atau import classes
dari json impor JSONDecoder, JSONEncoder
```

## Core JSON Functions

### loads() / baca_json()
Parses a JSON string and converts it to a Python object.

**Syntax:**
```python
loads(json_string, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
baca_json(json_string, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
```

**Parameters:**
- `json_string` (string): JSON string to parse
- `encoding` (string, optional): Text encoding (deprecated)
- `cls` (class, optional): Custom JSON decoder class
- `object_hook` (function, optional): Function for custom object parsing
- `parse_float` (function, optional): Function for parsing float values
- `parse_int` (function, optional): Function for parsing integer values
- `parse_constant` (function, optional): Function for parsing constants (NaN, Inf, -Inf)
- `object_pairs_hook` (function, optional): Function for parsing object pairs

**Returns:**
- Python object: Dictionary, list, string, number, boolean, or None

**Examples:**
```python
dari json impor loads, baca_json

// Basic JSON parsing
json_str1 = '{"nama": "Budi", "umur": 25, "aktif": true}'
data1 = loads(json_str1)
tampilkan data1["nama"]      // Output: "Budi"
tampilkan data1["umur"]      // Output: 25
tampilkan data1["aktif"]     // Output: benar

// Parse JSON array
json_str2 = '[1, 2, 3, 4, 5]'
data2 = baca_json(json_str2)
tampilkan data2              // Output: [1, 2, 3, 4, 5]

// Parse nested JSON
json_str3 = '{"user": {"id": 1, "name": "John"}, "items": ["a", "b", "c"]}'
data3 = loads(json_str3)
tampilkan data3["user"]["name"]  // Output: "John"
tampilkan data3["items"][0]      // Output: "a"

// Parse with custom object hook
fungsi custom_hook(obj):
    obj["processed"] = benar
    hasil obj
selesai

data4 = loads('{"key": "value"}', object_hook=custom_hook)
tampilkan data4["processed"]   // Output: benar
```

---

### dumps() / tulis_json()
Converts a Python object to a JSON string.

**Syntax:**
```python
dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
tulis_json(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
```

**Parameters:**
- `obj` (object): Python object to serialize
- `skipkeys` (boolean, optional): Skip non-string keys (default: salah)
- `ensure_ascii` (boolean, optional): Ensure ASCII output (default: benar)
- `check_circular` (boolean, optional): Check for circular references (default: benar)
- `allow_nan` (boolean, optional): Allow NaN, Inf, -Inf values (default: benar)
- `cls` (class, optional): Custom JSON encoder class
- `indent` (integer, optional): Number of spaces for indentation (default: None)
- `separators` (tuple, optional): Tuple of (item_separator, key_separator)
- `default` (function, optional): Function for non-serializable objects
- `sort_keys` (boolean, optional): Sort keys alphabetically (default: salah)

**Returns:**
- String: JSON representation of the object

**Examples:**
```python
dari json impor dumps, tulis_json

// Basic object serialization
data1 = {"nama": "Budi", "umur": 25, "aktif": benar}
json_str1 = dumps(data1)
tampilkan json_str1          // Output: {"nama": "Budi", "umur": 25, "aktif": true}

// Formatted JSON with indentation
json_str2 = tulis_json(data1, indent=2)
tampilkan json_str2
// Output:
// {
//   "nama": "Budi",
//   "umur": 25,
//   "aktif": true
// }

// Sort keys and pretty print
data3 = {"z": 1, "a": 2, "m": 3}
json_str3 = dumps(data3, indent=4, sort_keys=benar)
tampilkan json_str3
// Output:
// {
//     "a": 2,
//     "m": 3,
//     "z": 1
// }

// Minified JSON
json_str4 = tulis_json(data3, separators=(",", ":"))
tampilkan json_str4          // Output: {"z":1,"a":2,"m":3}

// Serialize list
data5 = [1, 2, 3, "hello", benar]
json_str5 = dumps(data5)
tampilkan json_str5          // Output: [1, 2, 3, "hello", true]

// Handle non-ASCII characters
data6 = {"pesan": "Halo Dunia"}
json_str6 = dumps(data6, ensure_ascii=salah)
tampilkan json_str6          // Output: {"pesan": "Halo Dunia"}
```

---

### load() / baca_dari_file()
Parses JSON from a file-like object.

**Syntax:**
```python
load(file_object, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
baca_dari_file(file_object, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
```

**Parameters:**
- `file_object`: File-like object containing JSON data
- `cls` (class, optional): Custom JSON decoder class
- `object_hook` (function, optional): Function for custom object parsing
- `parse_float` (function, optional): Function for parsing float values
- `parse_int` (function, optional): Function for parsing integer values
- `parse_constant` (function, optional): Function for parsing constants
- `object_pairs_hook` (function, optional): Function for parsing object pairs

**Returns:**
- Python object: Parsed JSON data

**Examples:**
```python
dari json impor load, baca_dari_file

// Read from file (assuming data.json exists)
file_handler = buka_file("data.json", "r")
data1 = load(file_handler)
file_handler.tutup()
tampilkan data1

// Indonesian alias
file_handler2 = buka_file("config.json", "r")
config = baca_dari_file(file_handler2)
file_handler2.tutup()
tampilkan config["settings"]
```

---

### dump() / tulis_ke_file()
Writes a Python object as JSON to a file-like object.

**Syntax:**
```python
dump(obj, file_object, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
tulis_ke_file(obj, file_object, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
```

**Parameters:**
- `obj` (object): Python object to serialize
- `file_object`: File-like object to write JSON to
- `skipkeys` (boolean, optional): Skip non-string keys (default: salah)
- `ensure_ascii` (boolean, optional): Ensure ASCII output (default: benar)
- `check_circular` (boolean, optional): Check for circular references (default: benar)
- `allow_nan` (boolean, optional): Allow NaN, Inf, -Inf values (default: benar)
- `cls` (class, optional): Custom JSON encoder class
- `indent` (integer, optional): Number of spaces for indentation
- `separators` (tuple, optional): Tuple of separators
- `default` (function, optional): Function for non-serializable objects
- `sort_keys` (boolean, optional): Sort keys alphabetically (default: salah)

**Returns:**
- None

**Examples:**
```python
dari json impor dump, tulis_ke_file

// Write to file with formatting
data = {"nama": "Budi", "umur": 25, "hobi": ["membaca", "coding"]}

file_handler = buka_file("output.json", "w")
dump(data, file_handler, indent=2, sort_keys=benar)
file_handler.tutup()

// Indonesian alias
data2 = {"config": {"theme": "dark", "language": "id"}}
file_handler2 = buka_file("config.json", "w")
tulis_ke_file(data2, file_handler2, indent=4)
file_handler2.tutup()
```

## Utility Functions

### format_json()
Formats a Python object as a pretty-printed JSON string.

**Syntax:**
```python
format_json(obj, indent)
```

**Parameters:**
- `obj` (object): Python object to format
- `indent` (integer, optional): Number of spaces for indentation (default: 2)

**Returns:**
- String: Formatted JSON string

**Examples:**
```python
dari json impor format_json

data = {"user": {"name": "John", "age": 30}, "active": benar}
formatted = format_json(data, indent=4)
tampilkan formatted
// Output:
// {
//     "active": true,
//     "user": {
//         "age": 30,
//         "name": "John"
//     }
// }
```

---

### validate_json()
Validates whether a string is valid JSON.

**Syntax:**
```python
validate_json(json_string)
```

**Parameters:**
- `json_string` (string): String to validate

**Returns:**
- Boolean: `benar` if valid JSON, `salah` otherwise

**Examples:**
```python
dari json impor validate_json

// Valid JSON
valid1 = validate_json('{"name": "John"}')
tampilkan valid1              // Output: benar

valid2 = validate_json('[1, 2, 3]')
tampilkan valid2              // Output: benar

// Invalid JSON
invalid1 = validate_json('{name: John}')
tampilkan invalid1            // Output: salah

invalid2 = validate_json('{"missing": "quote}')
tampilkan invalid2            // Output: salah
```

---

### minify_json()
Converts an object to a minified JSON string (no whitespace).

**Syntax:**
```python
minify_json(obj)
```

**Parameters:**
- `obj` (object): Python object to minify

**Returns:**
- String: Minified JSON string

**Examples:**
```python
dari json impor minify_json

data = {"name": "John", "age": 30, "items": [1, 2, 3]}
minified = minify_json(data)
tampilkan minified            // Output: {"name":"John","age":30,"items":[1,2,3]}
```

## Classes

### JSONDecoder
Custom JSON decoder class with additional functionality.

**Syntax:**
```python
decoder = JSONDecoder(**kwargs)
```

**Parameters:**
- `**kwargs`: Additional keyword arguments

**Examples:**
```python
dari json impor JSONDecoder

decoder = JSONDecoder(object_hook=lambda x: {**x, "decoded": benar})
data = decoder.decode('{"test": "value"}')
tampilkan data["decoded"]      // Output: benar
```

---

### JSONEncoder
Custom JSON encoder class with additional functionality.

**Syntax:**
```python
encoder = JSONEncoder(**kwargs)
```

**Parameters:**
- `**kwargs`: Additional keyword arguments

**Examples:**
```python
dari json impor JSONEncoder

encoder = JSONEncoder(indent=2)
data = {"name": "John", "age": 30}
json_str = encoder.encode(data)
tampilkan json_str
```

## Exception Handling

### JSONDecodeError
Exception raised when JSON parsing fails.

**Properties:**
- `msg`: Error message
- `doc`: JSON document that caused the error
- `pos`: Position in the document where the error occurred

**Examples:**
```python
dari json impor loads, JSONDecodeError

coba
    data = loads('{"invalid": json}')
tangkap JSONDecodeError sebagai e
    tampilkan "JSON Error:", e.msg
    tampilkan "Position:", e.pos
selesai
```

## Complete Examples

### API Data Processing
```python
dari json impor loads, dumps, format_json
dari http impor get

// Fetch data from API
response = get("https://jsonplaceholder.typicode.com/users")
users = response.json()

// Process data
processed_users = []
untuk setiap user dari users
    new_user = {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "company": user["company"]["name"]
    }
    processed_users.tambah(new_user)
selesai

// Convert to formatted JSON
json_output = format_json(processed_users, indent=2)
tampilkan json_output

// Save to file
file_handler = buka_file("processed_users.json", "w")
file_handler.tulis(json_output)
file_handler.tutup()
```

### Configuration Management
```python
dari json impor load, dump, validate_json

// Default configuration
default_config = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0",
        "debug": salah
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "features": {
        "auth": benar,
        "logging": benar,
        "cache": salah
    }
}

// Save default config
file_handler = buka_file("config.json", "w")
dump(default_config, file_handler, indent=4, sort_keys=benar)
file_handler.tutup()

// Load and validate config
file_handler = buka_file("config.json", "r")
config_data = file_handler.baca()
file_handler.tutup()

jika validate_json(config_data)
    config = load(config_data)
    tampilkan "Configuration loaded successfully"
    tampilkan "App name:", config["app"]["name"]
    tampilkan "Database host:", config["database"]["host"]
lainnya
    tampilkan "Invalid configuration file"
selesai
```

### Data Validation and Cleaning
```python
dari json impor loads, validate_json, format_json

// Raw JSON strings (from user input, API, etc.)
raw_data = [
    '{"name": "John", "age": 25}',
    '{"name": "Jane", "age": 30}',
    '{"invalid": json}',
    '{"name": "Bob", "age": 35}'
]

// Process and validate data
valid_data = []
invalid_count = 0

untuk setiap item dari raw_data
    jika validate_json(item)
        data = loads(item)
        // Ensure required fields
        jika "name" di data dan "age" di data
            valid_data.tambah(data)
        lainnya
            invalid_count = invalid_count + 1
    lainnya
        invalid_count = invalid_count + 1
selesai

tampilkan "Valid entries:", panjang(valid_data)
tampilkan "Invalid entries:", invalid_count

// Export cleaned data
cleaned_json = format_json(valid_data, indent=2)
file_handler = buka_file("cleaned_data.json", "w")
file_handler.tulis(cleaned_json)
file_handler.tutup()
```

## Usage Notes

1. **Indonesian Aliases**: All main functions have Indonesian aliases:
   - `baca_json()` for `loads()`
   - `tulis_json()` for `dumps()`
   - `baca_dari_file()` for `load()`
   - `tulis_ke_file()` for `dump()`

2. **Type Support**: JSON supports the following types:
   - Objects: `{}` (Python dict)
   - Arrays: `[]` (Python list)
   - Strings: `""` (Python str)
   - Numbers: (Python int and float)
   - Booleans: `true`, `false` (Python bool)
   - Null: `null` (Python None)

3. **Unicode Support**: Set `ensure_ascii=salah` to preserve Unicode characters.

4. **Error Handling**: Always wrap JSON operations in try-catch blocks for production code.

5. **Performance**: Use `load()`/`dump()` for file operations instead of reading entire files into memory.

6. **Validation**: Use `validate_json()` to check JSON validity before parsing.

7. **Formatting**: Use `format_json()` for consistent, readable JSON output.

8. **Minification**: Use `minify_json()` for compact JSON transmission.