# Modul JSON

Modul JSON menyediakan fungsi-fungsi untuk encoding dan decoding JSON, mengikuti standar modul json Python dengan nama fungsi dalam Bahasa Indonesia.

## Impor

```python
dari json impor loads, dumps, load, dump
// atau gunakan alias Indonesia
dari json impor baca_json, tulis_json, baca_dari_file, tulis_ke_file
// atau impor semua
dari json impor *
```

## Fungsi Parsing JSON

### loads() / baca_json()

Parse JSON string menjadi Python object.

**Sintaks:**
```python
loads(string_json, *, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
baca_json(string_json, *, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
```

**Parameter:**
- `string_json` (string): JSON string yang akan di-parse
- `encoding` (string, opsional): Encoding yang digunakan (deprecated)
- `cls` (class, opsional): Custom JSON decoder class
- `object_hook` (function, opsional): Function untuk custom object parsing
- `parse_float` (function, opsional): Function untuk parsing float
- `parse_int` (function, opsional): Function untuk parsing integer
- `parse_constant` (function, opsional): Function untuk parsing constants (NaN, Inf, -Inf)
- `object_pairs_hook` (function, opsional): Function untuk parsing object pairs

**Mengembalikan:**
- Python object: Hasil parsing JSON (dict, list, string, number, boolean, atau null)

**Contoh:**
```python
dari json import loads

// Parse JSON sederhana
json_str itu '{"nama": "Budi", "umur": 25}'
data itu loads(json_str)
tampilkan data["nama"]     // Output: Budi
tampilkan data["umur"]     // Output: 25

// Parse JSON array
json_array itu '[1, 2, 3, "hello", true]'
array_data itu loads(json_array)
tampilkan array_data       // Output: [1, 2, 3, "hello", True]

// Parse JSON nested
json_nested itu '{"user": {"id": 1, "name": "Alice"}, "roles": ["admin", "user"]}'
nested_data itu loads(json_nested)
tampilkan nested_data["user"]["name"]    // Output: Alice
tampilkan nested_data["roles"][0]        // Output: admin
```

**Error:**
- Melempar `JSONDecodeError` jika JSON string tidak valid

---

### load() / baca_dari_file()

Parse JSON dari file-like object.

**Sintaks:**
```python
load(file_object, *, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
baca_dari_file(file_object, *, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook)
```

**Parameter:**
- `file_object`: File-like object yang berisi JSON
- `cls` (class, opsional): Custom JSON decoder class
- `object_hook` (function, opsional): Function untuk custom object parsing
- `parse_float` (function, opsional): Function untuk parsing float
- `parse_int` (function, opsional): Function untuk parsing integer
- `parse_constant` (function, opsional): Function untuk parsing constants
- `object_pairs_hook` (function, opsional): Function untuk parsing object pairs

**Contoh:**
```python
dari json import load

// Asumsi file "data.json" berisi: {"nama": "Charlie", "umur": 30}
dengan open("data.json", "r") sebagai file
    data itu load(file)
    tampilkan data["nama"]
    tampilkan data["umur"]
selesai

// Parse dari string object (like file)
json_content it '{"product": "Laptop", "price": 8500000}'
import io
file_like it io.StringIO(json_content)
data itu load(file_like)
tampilkan data
```

## Fungsi Serialisasi JSON

### dumps() / tulis_json()

Convert Python object menjadi JSON string.

**Sintaks:**
```python
dumps(objek, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
tulis_json(objek, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
```

**Parameter:**
- `objek` (dict/list/string/number/boolean/None): Python object yang akan di-serialize
- `skipkeys` (boolean, opsional): Skip keys yang bukan string (default: False)
- `ensure_ascii` (boolean, opsional): Ensure output ASCII (default: True)
- `check_circular` (boolean, opsional): Check circular reference (default: True)
- `allow_nan` (boolean, opsional): Allow NaN, Inf, -Inf (default: True)
- `cls` (class, opsional): Custom JSON encoder class
- `indent` (integer, opsional): Number of spaces untuk indentasi
- `separators` (tuple, opsional): Tuple item separator dan key separator
- `default` (function, opsional): Function untuk object yang tidak bisa di-serialize
- `sort_keys` (boolean, opsional): Sort keys alphabetically (default: False)

**Mengembalikan:**
- String: JSON string yang telah di-serialize

**Contoh:**
```python
dari json import dumps

// Serialisasi dictionary sederhana
data itu {"nama": "Diana", "umur": 28, "aktif": benar}
json_str itu dumps(data)
tampilkan json_str  // Output: {"nama": "Diana", "umur": 28, "aktif": true}

// Dengan indentasi
json_pretty it dumps(data, indent=2)
tampilkan json_pretty
// Output:
// {
//   "nama": "Diana",
//   "umur": 28,
//   "aktif": true
// }

// Sort keys alphabetically
json_sorted it dumps(data, indent=2, sort_keys=benar)
tampilkan json_sorted

// Serialisasi list
angka itu [1, 2, 3, 4, 5]
json_list it dumps(angka)
tampilkan json_list  // Output: [1, 2, 3, 4, 5]

// Serialisasi complex object
complex_data it {
    "users": [
        {"id": 1, "name": "Alice", "scores": [85, 90, 78]},
        {"id": 2, "name": "Bob", "scores": [92, 88, 95]}
    ],
    "metadata": {
        "total": 2,
        "average_score": 88.0
    }
}
json_complex it dumps(complex_data, indent=2, sort_keys=benar)
tampilkan json_complex
```

---

### dump() / tulis_ke_file()

Write JSON object ke file-like object.

**Sintaks:**
```python
dump(objek, file_object, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
tulis_ke_file(objek, file_object, *, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys)
```

**Parameter:**
- `objek` (dict/list/string/number/boolean/None): Python object yang akan di-serialize
- `file_object`: File-like object untuk write output
- `skipkeys` (boolean, opsional): Skip keys yang bukan string (default: False)
- `ensure_ascii` (boolean, opsional): Ensure output ASCII (default: True)
- `check_circular` (boolean, opsional): Check circular reference (default: True)
- `allow_nan` (boolean, opsional): Allow NaN, Inf, -Inf (default: True)
- `cls` (class, opsional): Custom JSON encoder class
- `indent` (integer, opsional): Number of spaces untuk indentasi
- `separators` (tuple, opsional): Tuple item separator dan key separator
- `default` (function, opsional): Function untuk object yang tidak bisa di-serialize
- `sort_keys` (boolean, opsional): Sort keys alphabetically (default: False)

**Contoh:**
```python
dari json import dump

// Write ke file
data itu {"nama": "Eva", "pekerjaan": "Developer", "skills": ["Python", "JavaScript"]}
dengan open("profile.json", "w") sebagai file
    dump(data, file, indent=2)
selesai

// Write dengan options
config itu {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": false,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}
dengan open("config.json", "w") sebagai file
    dump(config, file, indent=4, sort_keys=benar, ensure_ascii=salah)
selesai
```

## Fungsi Utilitas

### format_json()

Format JSON string dengan indentasi yang rapi.

**Sintaks:**
```python
format_json(objek, indent)
```

**Parameter:**
- `objek` (dict/list/string/number/boolean/None): Python object yang akan di-format
- `indent` (integer, opsional): Number of spaces untuk indentasi (default: 2)

**Mengembalikan:**
- String: JSON string yang sudah di-format

**Contoh:**
```python
dari json import format_json

data itu {"user": "Frank", "age": 35, "city": "Bandung"}
formatted it format_json(data, indent=4)
tampilkan formatted
```

---

### validate_json()

Validasi apakah string adalah JSON yang valid.

**Sintaks:**
```python
validate_json(string_json)
```

**Parameter:**
- `string_json` (string): String yang akan divalidasi

**Mengembalikan:**
- Boolean: True jika valid, False jika tidak

**Contoh:**
```python
dari json import validate_json

valid_json itu '{"nama": "Grace", "umur": 25}'
invalid_json it '{"nama": "Grace", "umur": 25'  // Kurung tutup kurang

tampilkan validate_json(valid_json)      // Output: benar
tampilkan validate_json(invalid_json)    // Output: salah
```

---

### minify_json()

Convert object menjadi JSON string yang minimal (tanpa spasi).

**Sintaks:**
```python
minify_json(objek)
```

**Parameter:**
- `objek` (dict/list/string/number/boolean/None): Python object yang akan di-minify

**Mengembalikan:**
- String: Minified JSON string

**Contoh:**
```python
dari json import minify_json

data it {"key1": "value1", "key2": "value2", "number": 123}
minified it minify_json(data)
tampilkan minified  // Output: {"key1":"value1","key2":"value2","number":123}
```

## Kelas

### JSONDecoder / parser_json

Custom JSON decoder dengan additional functionality.

**Contoh:**
```python
dari json import JSONDecoder

// Buat custom decoder
decoder itu JSONDecoder(object_hook=lambda d: {k.upper(): v untuk k, v di d.items()})
json_str it '{"nama": "Henry", "umur": 30}'
data itu decoder.decode(json_str)
tampilkan data  // Output: {'NAMA': 'Henry', 'UMUR': 30}
```

---

### JSONEncoder / encoder_json

Custom JSON encoder dengan additional functionality.

**Contoh:**
```python
dari json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data it {"items": {1, 2, 3}, "name": "Iris"}
json_str it dumps(data, cls=CustomEncoder)
tampilkan json_str  // Output: {"items": [1, 2, 3], "name": "Iris"}
```

---

### JSONDecodeError / error_json

Exception yang di-raised saat JSON parsing gagal.

**Contoh:**
```python
dari json import loads, JSONDecodeError

coba
    data it loads('{"invalid": json}')
kecuali JSONDecodeError sebagai e
    tampilkan f"JSON Error: {e}"
selesai
```

## Contoh Praktis

### Configuration Manager

```python
dari json import load, dump, validate_json

buat fungsi load_config dengan filename
    coba
        dengan open(filename, "r") sebagai file
            config it load(file)
            hasil config
    kecuali FileNotFoundError
        tampilkan f"File {filename} tidak ditemukan"
        hasil {}
    kecuali Exception sebagai e
        tampilkan f"Error loading config: {e}"
        hasil {}
    selesai
selesai

buat fungsi save_config dengan config, filename
    coba
        dengan open(filename, "w") sebagai file
            dump(config, file, indent=2, sort_keys=benar)
        tampilkan f"Config disimpan ke {filename}"
        hasil benar
    kecuali Exception sebagai e
        tampilkan f"Error saving config: {e}"
        hasil salah
    selesai
selesai

// Penggunaan
config it load_config("app_config.json")
config["app_name"] it "MyRenzMcApp"
config["version"] it "1.0.0"
config["debug"] it benar

save_config(config, "app_config.json")
```

### Data Export/Import

```python
dari json import dumps, loads, format_json

buat fungsi export_data_ke_json dengan data
    // Add metadata
    export_data it {
        "timestamp": waktu(),  // Asumsi ada fungsi waktu()
        "version": "1.0",
        "data": data
    }
    
    json_string it format_json(export_data, indent=2)
    hasil json_string
selesai

buat fungsi import_dari_json dengan json_string
    coba
        parsed_data it loads(json_string)
        
        // Validate structure
        jika "data" dalam parsed_data
            hasil parsed_data["data"]
        lainnya
            hasil parsed_data
        selesai
    kecuali Exception sebagai e
        tampilkan f"Error importing JSON: {e}"
        hasil {}
    selesai
selesai

// Data export
users it [
    {"id": 1, "name": "Jack", "email": "jack@example.com"},
    {"id": 2, "name": "Kate", "email": "kate@example.com"}
]

json_export it export_data_ke_json(users)
tampilkan "Data exported:"
tampilkan json_export

// Data import
imported_data it import_dari_json(json_export)
tampilkan f"Imported {panjang(imported_data)} users"
```

### API Response Parser

```python
dari json import loads, validate_json

buat fungsi parse_api_response dengan response_text
    // Validate JSON format
    jika tidak validate_json(response_text)
        hasil {"error": "Invalid JSON format", "success": salah}
    selesai
    
    coba
        data it loads(response_text)
        
        // Standard API response format
        response it {
            "success": benar,
            "data": data.get("data", data),
            "message": data.get("message", "Success"),
            "status_code": data.get("status", 200)
        }
        
        hasil response
    kecuali Exception sebagai e
        hasil {"error": f"Parsing error: {e}", "success": salah}
    selesai
selesai

// Mock API response
api_response it '{
    "status": 200,
    "message": "Users retrieved successfully",
    "data": [
        {"id": 1, "name": "Liam", "role": "admin"},
        {"id": 2, "name": "Mia", "role": "user"}
    ],
    "total": 2
}'

parsed it parse_api_response(api_response)
jika parsed["success"]
    tampilkan f"API Success: {parsed['message']}"
    tampilkan f"Users: {panjang(parsed['data'])}")
lainnya
    tampilkan f"API Error: {parsed['error']}"
selesai
```

### Database JSON Backup

```python
dari json import dump, load

buat fungsi backup_table_ke_json dengan table_data, filename
    coba
        dengan open(filename, "w") sebagai file
            dump(table_data, file, indent=2, ensure_ascii=salah)
        
        tampilkan f"Backup berhasil disimpan ke {filename}"
        hasil benar
    kecuali Exception sebagai e
        tampilkan f"Backup gagal: {e}"
        hasil salah
    selesai
selesai

buat fungsi restore_table_dari_json dengan filename
    coba
        dengan open(filename, "r") sebagai file
            table_data it load(file)
        
        tampilkan f"Restore berhasil dari {filename}"
        tampilkan f"Jumlah records: {panjang(table_data)}"
        hasil table_data
    kecuali FileNotFoundError
        tampilkan f"File backup {filename} tidak ditemukan"
        hasil []
    kecuali Exception sebagai e
        tampilkan f"Restore gagal: {e}"
        hasil []
    selesai
selesai

// Mock database table
users_table it [
    {"id": 1, "username": "noah", "email": "noah@example.com", "created_at": "2025-01-01"},
    {"id": 2, "username": "olivia", "email": "olivia@example.com", "created_at": "2025-01-02"},
    {"id": 3, "username": "peter", "email": "peter@example.com", "created_at": "2025-01-03"}
]

// Backup
backup_table_ke_json(users_table, "users_backup.json")

// Restore (simulasi)
restored_users it restore_table_dari_json("users_backup.json")
tampilkan f"Restored {panjang(restored_users)} users"
```

### JSON Schema Validator

```python
dari json import loads, validate_json

buat fungsi validate_json_schema dengan json_data, schema
    // Validasi basic JSON format
    jika tidak validate_json(json_data)
        hasil {"valid": salah, "error": "Invalid JSON format"}
    selesai
    
    coba
        data it loads(json_data)
        errors it []
        
        // Check required fields
        jika "required" dalam schema
            untuk setiap field dari schema["required"]
                jika field tidak dalam data
                    tambah(errors, f"Field required '{field}' tidak ada")
                selesai
            selesai
        selesai
        
        // Check field types
        jika "properties" dalam schema
            untuk setiap (field, field_schema) dari item(schema["properties"])
                jika field dalam data
                    expected_type it field_schema.get("type")
                    actual_value it data[field]
                    
                    jika expected_type == "string" dan jenis(actual_value) != "str"
                        tambah(errors, f"Field '{field}' harus string")
                    selesai
                    
                    jika expected_type == "number" dan jenis(actual_value) not in ["int", "float"]
                        tambah(errors, f"Field '{field}' harus number")
                    selesai
                    
                    jika expected_type == "boolean" dan jenis(actual_value) != "bool"
                        tambah(errors, f"Field '{field}' harus boolean")
                    selesai
                selesai
            selesai
        selesai
        
        jika panjang(errors) > 0
            hasil {"valid": salah, "errors": errors}
        lainnya
            hasil {"valid": benar, "data": data}
        selesai
        
    kecuali Exception sebagai e
        hasil {"valid": salah, "error": f"Validation error: {e}"}
    selesai
selesai

// Schema definition
user_schema it {
    "type": "object",
    "required": ["nama", "email", "umur"],
    "properties": {
        "nama": {"type": "string"},
        "email": {"type": "string"},
        "umur": {"type": "number"},
        "aktif": {"type": "boolean"}
    }
}

// Test data
valid_user it '{"nama": "Quinn", "email": "quinn@example.com", "umur": 25, "aktif": true}'
invalid_user it '{"nama": "Rachel", "umur": "thirty"}'  // Email missing, umur bukan number

validation1 it validate_json_schema(valid_user, user_schema)
tampilkan validation1

validation2 it validate_json_schema(invalid_user, user_schema)
tampilkan validation2
```

## Catatan Penggunaan

1. **Impor Diperlukan**: Semua fungsi JSON harus diimpor dari modul json.

2. **Alias Indonesia**: Fungsi memiliki alias Indonesia:
   - `baca_json()` untuk `loads()`
   - `tulis_json()` untuk `dumps()`
   - `baca_dari_file()` untuk `load()`
   - `tulis_ke_file()` untuk `dump()`
   - `parser_json()` untuk `JSONDecoder`
   - `encoder_json()` untuk `JSONEncoder`
   - `error_json()` untuk `JSONDecodeError`

3. **Tipe Data Support**: JSON support tipe data: object (dict), array (list), string, number, boolean, null.

4. **Unicode**: Set `ensure_ascii=False` untuk support karakter Unicode dalam output.

5. **Performance**: Untuk data besar, gunakan `separators=(",", ":")` untuk output yang lebih compact.

6. **Error Handling**: Selalu gunakan try-catch untuk menangani `JSONDecodeError`.

7. **Circular Reference**: Defaultnya cek circular reference, set `check_circular=False` untuk performa.

8. **Custom Types**: Gunakan custom encoder untuk tipe data yang tidak didukung secara default.

9. **File Operations**: Gunakan `load()`/`dump()` untuk operasi file, `loads()`/`dumps()` untuk string.

10. **Validation**: Gunakan `validate_json()` untuk quick validation tanpa parsing penuh.