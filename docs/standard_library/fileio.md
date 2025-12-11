# File I/O Module

The File I/O module provides comprehensive file and directory operations functionality following Python's file operations standards with Indonesian function names.

## Import

```python
dari fileio impor *
// atau import specific functions
dari fileio impor read_text, write_text, copy, delete, exists
```

## File Reading Functions

### read_text() / baca_teks()
Reads file content as text.

**Syntax:**
```python
read_text(file_path, encoding)
baca_teks(file_path, encoding)
```

**Parameters:**
- `file_path` (string): Path to the file to read
- `encoding` (string, optional): File encoding (default: "utf-8")

**Returns:**
- String: File content as text

**Examples:**
```python
dari fileio impor read_text, baca_teks

// Read basic text file
content1 = read_text("data.txt")
tampilkan content1

// Read with specific encoding
content2 = baca_teks("data_utf8.txt", "utf-8")
tampilkan content2

// Read configuration file
config_content = read_text("config.ini")
tampilkan config_content

// Handle file not found
coba
    content = read_text("nonexistent.txt")
except FileNotFoundError
    tampilkan "File not found!"
selesai
```

---

### read_lines() / baca_baris()
Reads file content as a list of lines.

**Syntax:**
```python
read_lines(file_path, encoding)
baca_baris(file_path, encoding)
```

**Parameters:**
- `file_path` (string): Path to the file to read
- `encoding` (string, optional): File encoding (default: "utf-8")

**Returns:**
- List: List of lines from the file

**Examples:**
```python
dari fileio impor read_lines, baca_baris

// Read file as lines
lines1 = read_lines("data.txt")
tampilkan lines1           // Output: ["line 1\n", "line 2\n", "line 3"]

// Process each line
lines2 = baca_baris("names.txt")
untuk line dari lines2
    clean_line = line.strip()  // Remove whitespace
    tampilkan f"Name: {clean_line}"
selesai

// Count lines
all_lines = read_lines("document.txt")
line_count = panjang(all_lines)
tampilkan f"Total lines: {line_count}"

// Filter lines containing specific text
log_lines = baca_baris("app.log")
error_lines = []
untuk line dari log_lines
    jika "ERROR" di line
        tambah(error_lines, line.strip())
    selesai
selesai
tampilkan f"Found {panjang(error_lines)} errors"
```

---

### read_bytes() / baca_bytes()
Reads file content as bytes.

**Syntax:**
```python
read_bytes(file_path)
baca_bytes(file_path)
```

**Parameters:**
- `file_path` (string): Path to the file to read

**Returns:**
- Bytes: File content as bytes

**Examples:**
```python
dari fileio impor read_bytes, baca_bytes

// Read image file
image_data = read_bytes("photo.jpg")
tampilkan f"Image size: {panjang(image_data)} bytes"

// Read binary data
binary_data = baca_bytes("data.bin")
tampilkan f"Binary data: {binary_data[:10]}"  // First 10 bytes

// Read PDF file
pdf_content = read_bytes("document.pdf")
tampilkan f"PDF size: {panjang(pdf_content)} bytes"

// Calculate file hash (using utility functions)
dari builtin_functions impor hash_teks
file_hash = hash_teks(binary_data, "md5")
tampilkan f"File MD5: {file_hash}"
```

---

### read_json() / baca_json()
Reads and parses JSON file.

**Syntax:**
```python
read_json(file_path, encoding)
baca_json(file_path, encoding)
```

**Parameters:**
- `file_path` (string): Path to the JSON file
- `encoding` (string, optional): File encoding (default: "utf-8")

**Returns:**
- Dictionary: Parsed JSON data

**Examples:**
```python
dari fileio impor read_json, baca_json

// Read configuration
config = read_json("config.json")
tampilkan config["database_url"]
tampilkan config["port"]

// Read user data
users = baca_json("users.json")
untuk user dari users
    tampilkan f"User: {user['name']}, Age: {user['age']}"
selesai

// Read API response
api_data = read_json("api_response.json")
tampilkan api_data["status"]
tampilkan api_data["data"]["total"]

// Handle JSON parsing errors
coba
    data = baca_json("invalid.json")
except Exception sebagai e
    tampilkan f"JSON parsing error: {e}"
selesai
```

---

### read_csv() / baca_csv()
Reads CSV file as list of rows.

**Syntax:**
```python
read_csv(file_path, delimiter, encoding)
baca_csv(file_path, delimiter, encoding)
```

**Parameters:**
- `file_path` (string): Path to the CSV file
- `delimiter` (string, optional): Field delimiter (default: ",")
- `encoding` (string, optional): File encoding (default: "utf-8")

**Returns:**
- List: List of rows (each row is a list of strings)

**Examples:**
```python
dari fileio impor read_csv, baca_csv

// Read standard CSV
data1 = read_csv("data.csv")
tampilkan data1[0]          // First row
tampilkan data1[1][2]       // Third column of second row

// Read semicolon-delimited CSV
data2 = baca_csv("data.csv", delimiter=";")
tampilkan data2

// Process CSV data
rows = read_csv("students.csv")
headers = rows[0]           // Assuming first row is headers
tampilkan "Headers:", headers

untuk i dari rentang(1, panjang(rows))
    row = rows[i]
    tampilkan f"Student: {row[0]}, Grade: {row[1]}"
selesai

// Read tab-separated data
tsv_data = baca_csv("data.tsv", delimiter="\t")
tampilkan tsv_data
```

---

## File Writing Functions

### write_text() / tulis_teks()
Writes text content to a file.

**Syntax:**
```python
write_text(file_path, content, encoding)
tulis_teks(file_path, content, encoding)
```

**Parameters:**
- `file_path` (string): Path to the file to write
- `content` (string): Text content to write
- `encoding` (string, optional): File encoding (default: "utf-8")

**Examples:**
```python
dari fileio impor write_text, tulis_teks

// Write simple text
write_text("output.txt", "Hello, RenzMcLang!")
tampilkan "Text written to output.txt"

// Write multi-line content
content = "Line 1\nLine 2\nLine 3"
tulis_teks("multiline.txt", content)

// Write with specific encoding
write_text("utf8_file.txt", "Unicode: ñáéíóú", "utf-8")

// Write log file
log_message = f"[{tanggal()}] Application started"
tulis_teks("app.log", log_message, "utf-8")

// Append to file
dengan open_text("log.txt", "a") sebagai file
    file.tulis(f"[{tanggal()}] New log entry\n")
selesai
```

---

### write_lines() / tulis_baris()
Writes a list of lines to a file.

**Syntax:**
```python
write_lines(file_path, lines, encoding)
tulis_baris(file_path, lines, encoding)
```

**Parameters:**
- `file_path` (string): Path to the file to write
- `lines` (list): List of strings to write
- `encoding` (string, optional): File encoding (default: "utf-8")

**Examples:**
```python
dari fileio impor write_lines, tulis_baris

// Write list of lines
data = ["First line\n", "Second line\n", "Third line"]
write_lines("output.txt", data)

// Write generated data
numbers = []
untuk i di rentang(1, 11)
    tambah(numbers, f"Number {i}\n")
selesai
tulis_baris("numbers.txt", numbers)

// Write CSV data without CSV module
csv_data = ["Name,Age,City\n", "John,25,NYC\n", "Jane,30,LA\n"]
write_lines("simple.csv", csv_data)
```

---

### write_bytes() / tulis_bytes()
Writes bytes content to a file.

**Syntax:**
```python
write_bytes(file_path, content)
tulis_bytes(file_path, content)
```

**Parameters:**
- `file_path` (string): Path to the file to write
- `content` (bytes): Bytes content to write

**Examples:**
```python
dari fileio impor write_bytes, tulis_bytes

// Write binary data
binary_data = b"\x00\x01\x02\x03\x04"
write_bytes("output.bin", binary_data)

// Write image data
image_bytes = read_bytes("input.jpg")
tulis_bytes("backup.jpg", image_bytes)

// Create simple binary file
header = b"BINARY\x01\x00"
data = b"Hello Binary World"
tulis_bytes("simple.bin", header + data)
```

---

### write_json() / tulis_json()
Writes data to JSON file.

**Syntax:**
```python
write_json(file_path, data, indent, encoding)
tulis_json(file_path, data, indent, encoding)
```

**Parameters:**
- `file_path` (string): Path to the JSON file
- `data` (dictionary): Data to write
- `indent` (integer, optional): Indentation for pretty printing
- `encoding` (string, optional): File encoding (default: "utf-8")

**Examples:**
```python
dari fileio impor write_json, tulis_json

// Write simple JSON
config = {"name": "RenzMcLang", "version": "1.0", "author": "RenzMc"}
write_json("config.json", config, indent=2)

// Write user data
users = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"}
]
tulis_json("users.json", users, indent=4)

// Write API response
response = {
    "status": "success",
    "data": {
        "total": 100,
        "items": ["item1", "item2", "item3"]
    }
}
write_json("response.json", response, indent=2)
```

---

### write_csv() / tulis_csv()
Writes data to CSV file.

**Syntax:**
```python
write_csv(file_path, rows, delimiter, encoding)
tulis_csv(file_path, rows, delimiter, encoding)
```

**Parameters:**
- `file_path` (string): Path to the CSV file
- `rows` (list): List of rows (each row is a list of strings)
- `delimiter` (string, optional): Field delimiter (default: ",")
- `encoding` (string, optional): File encoding (default: "utf-8")

**Examples:**
```python
dari fileio impor write_csv, tulis_csv

// Write simple CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "NYC"],
    ["Bob", "30", "LA"]
]
write_csv("output.csv", data)

// Write semicolon-delimited CSV
tulis_csv("data.csv", data, delimiter=";")

// Write tab-separated data
write_csv("data.tsv", data, delimiter="\t")

// Write generated data
csv_data = [["ID", "Value"]]
untuk i di rentang(1, 6)
    tambah(csv_data, [str(i), str(i * 10)])
selesai
tulis_csv("generated.csv", csv_data)
```

---

## File Operations

### copy() / salin()
Copies file from source to destination.

**Syntax:**
```python
copy(src, dst)
salin(src, dst)
```

**Parameters:**
- `src` (string): Source file path
- `dst` (string): Destination file path

**Examples:**
```python
dari fileio impor copy, salin, exists

// Backup file
copy("important.txt", "backup.txt")
tampilkan "File backed up successfully"

// Copy with Indonesian alias
salin("data.csv", "data_backup.csv")

// Conditional copy
jika exists("config.json")
    salin("config.json", "config_backup.json")
selesai
```

---

### move() / pindahkan()
Moves file from source to destination.

**Syntax:**
```python
move(src, dst)
pindahkan(src, dst)
```

**Parameters:**
- `src` (string): Source file path
- `dst` (string): Destination file path

**Examples:**
```python
dari fileio impor move, pindahkan

// Move file
move("temp.txt", "processed.txt")

// Reorganize files
pindahkan("downloads/file.pdf", "documents/file.pdf")

// Rename file (move within same directory)
move("old_name.txt", "new_name.txt")
```

---

### delete() / hapus()
Deletes a file.

**Syntax:**
```python
delete(file_path)
hapus(file_path)
```

**Parameters:**
- `file_path` (string): Path to file to delete

**Examples:**
```python
dari fileio impor delete, hapus, exists

// Delete temporary file
delete("temp.txt")

// Conditional deletion
jika exists("old_backup.txt")
    hapus("old_backup.txt")
    tampilkan "Old backup deleted"
selesai

// Clean up files
extensions = [".tmp", ".bak", ".temp"]
untuk ext dari extensions
    files = [f for f in list_dir() if f.endswith(ext)]
    untuk file dari files
        hapus(file)
    selesai
selesai
```

---

### exists() / ada()
Checks if a file or directory exists.

**Syntax:**
```python
exists(file_path)
ada(file_path)
```

**Parameters:**
- `file_path` (string): Path to check

**Returns:**
- Boolean: True if exists, False otherwise

**Examples:**
```python
dari fileio impor exists, ada

// Check file existence
jika exists("data.txt")
    content = read_text("data.txt")
    tampilkan content
lainnya
    tampilkan "File does not exist"
selesai

// Indonesian alias
jika ada("config.json")
    tampilkan "Configuration found"
selesai

// Validate multiple files
required_files = ["config.json", "data.txt", "output.csv"]
missing_files = []

untuk file dari required_files
    jika tidak ada(file)
        tambah(missing_files, file)
    selesai
selesai

jika missing_files
    tampilkan f"Missing files: {missing_files}"
lainnya
    tampilkan "All required files present"
selesai
```

---

### size() / ukuran()
Gets file size in bytes.

**Syntax:**
```python
size(file_path)
ukuran(file_path)
```

**Parameters:**
- `file_path` (string): Path to file

**Returns:**
- Integer: File size in bytes

**Examples:**
```python
dari fileio impor size, ukuran

// Get file size
file_size = size("data.txt")
tampilkan f"File size: {file_size} bytes"

// Format file size
file_size_kb = ukuran("image.jpg") / 1024
tampilkan f"Image size: {file_size_kb:.2f} KB"

// Check file size limits
max_size = 10 * 1024 * 1024  // 10 MB
jika size("upload.zip") > max_size
    tampilkan "File too large!"
selesai
```

---

### is_file() / adalah_file() & is_dir() / adalah_dir()
Checks if path is a file or directory.

**Syntax:**
```python
is_file(file_path)
is_dir(file_path)
adalah_file(file_path)
adalah_dir(file_path)
```

**Parameters:**
- `file_path` (string): Path to check

**Returns:**
- Boolean: True if file/directory, False otherwise

**Examples:**
```python
dari fileio impor is_file, is_dir, adalah_file, adalah_dir

// Check path type
path = "data.txt"
jika is_file(path)
    tampilkan f"{path} is a file"
lainnya jika is_dir(path)
    tampilkan f"{path} is a directory"
lainnya
    tampilkan f"{path} does not exist"
selesai

// Indonesian aliases
jika adalah_file("config.json")
    tampilkan "Configuration file found"
selesai

jika adalah_dir("logs")
    tampilkan "Logs directory exists"
selesai

// List directory contents with types
items = list_dir(".")
untuk item dari items
    jika adalah_file(item)
        tampilkan f"FILE: {item}"
    lainnya jika adalah_dir(item)
        tampilkan f"DIR:  {item}"
    selesai
selesai
```

---

## Directory Operations

### create_dir() / buat_dir()
Creates a directory.

**Syntax:**
```python
create_dir(dir_path, exist_ok)
buat_dir(dir_path, exist_ok)
```

**Parameters:**
- `dir_path` (string): Directory path to create
- `exist_ok` (boolean, optional): Don't error if directory exists (default: True)

**Examples:**
```python
dari fileio impor create_dir, buat_dir

// Create single directory
create_dir("output")

// Create nested directory
buat_dir("data/processed/2024")

// Create with error handling
create_dir("config", exist_ok=salah)
// Will raise error if config already exists

// Organize project structure
directories = ["src", "tests", "docs", "output", "logs"]
untuk dir dari directories
    buat_dir(dir)
selesai
tampilkan "Project structure created"
```

---

### remove_dir() / hapus_dir()
Removes directory and its contents.

**Syntax:**
```python
remove_dir(dir_path, ignore_errors)
hapus_dir(dir_path, ignore_errors)
```

**Parameters:**
- `dir_path` (string): Directory path to remove
- `ignore_errors` (boolean, optional): Ignore errors during removal (default: False)

**Examples:**
```python
dari fileio impor remove_dir, hapus_dir

// Remove empty directory
remove_dir("temp")

// Remove directory with contents
hapus_dir("data/old")

// Safe removal
hapus_dir("backup", ignore_errors=benar)

// Clean up temporary directories
temp_dirs = ["temp", "tmp", "cache"]
untuk dir dari temp_dirs
    jika adalah_dir(dir)
        hapus_dir(dir, ignore_errors=benar)
        tampilkan f"Removed {dir}"
    selesai
selesai
```

---

### list_dir() / daftar_dir()
Lists contents of a directory.

**Syntax:**
```python
list_dir(dir_path)
daftar_dir(dir_path)
```

**Parameters:**
- `dir_path` (string, optional): Directory path (default: current directory)

**Returns:**
- List: List of file and directory names

**Examples:**
```python
dari fileio impor list_dir, daftar_dir

// List current directory
files = list_dir()
tampilkan files

// List specific directory
config_files = daftar_dir("config")
tampilkan config_files

// Filter files by extension
all_files = list_dir(".")
txt_files = [f for f in all_files if f.endswith(".txt")]
tampilkan f"Text files: {txt_files}"

// Count directory items
item_count = panjang(daftar_dir("documents"))
tampilkan f"Documents contain {item_count} items"
```

---

## Advanced Usage Examples

### File Processing Pipeline

```python
dari fileio impor (
    read_text, write_text, copy, delete, 
    exists, size, create_dir, list_dir
)

fungsi proses_file_batch(input_dir, output_dir):
    """Process all text files in a directory"""
    
    // Ensure output directory exists
    buat_dir(output_dir)
    
    // Get all text files
    files = list_dir(input_dir)
    txt_files = [f for f in files jika f.endswith(".txt")]
    
    tampilkan f"Processing {panjang(txt_files)} files..."
    
    processed_count = 0
    untuk filename dari txt_files
        input_path = join_paths(input_dir, filename)
        
        coba
            // Read and process
            content = read_text(input_path)
            
            // Process: convert to uppercase
            processed_content = huruf_besar(content)
            
            // Write to output
            output_path = join_paths(output_dir, f"processed_{filename}")
            write_text(output_path, processed_content)
            
            // Backup original
            backup_path = join_paths(output_dir, f"backup_{filename}")
            copy(input_path, backup_path)
            
            processed_count = processed_count + 1
            tampilkan f"Processed: {filename}"
            
        except Exception sebagai e
            tampilkan f"Error processing {filename}: {e}"
        selesai
    selesai
    
    tampilkan f"Successfully processed {processed_count} files"
    hasil processed_count
selesai

// Usage
proses_file_batch("input_data", "processed_data")
```

### File System Monitor

```python
dari fileio impor size, exists, list_dir, adalah_file

fungsi monitor_direktori(directory, max_size_mb=100):
    """Monitor directory size and file count"""
    
    max_size_bytes = max_size_mb * 1024 * 1024
    total_size = 0
    file_count = 0
    large_files = []
    
    files = list_dir(directory)
    
    untuk filename dari files
        filepath = join_paths(directory, filename)
        
        jika adalah_file(filepath)
            file_size = size(filepath)
            total_size = total_size + file_size
            file_count = file_count + 1
            
            // Track large files (> 1 MB)
            jika file_size > 1024 * 1024
                large_files.append({
                    "name": filename,
                    "size_mb": file_size / (1024 * 1024)
                })
            selesai
        selesai
    selesai
    
    // Report
    tampilkan f"=== Directory Monitor: {directory} ==="
    tampilkan f"Total files: {file_count}"
    tampilkan f"Total size: {total_size / (1024 * 1024):.2f} MB"
    tampilkan f"Size limit: {max_size_mb} MB"
    
    jika total_size > max_size_bytes
        tampilkan "⚠️ Directory exceeds size limit!"
    selesai
    
    jika large_files
        tampilkan "Large files (>1 MB):"
        untuk file_info dari large_files
            tampilkan f"  {file_info['name']}: {file_info['size_mb']:.2f} MB"
        selesai
    selesai
    
    hasil {
        "file_count": file_count,
        "total_size_bytes": total_size,
        "large_files": large_files,
        "exceeds_limit": total_size > max_size_bytes
    }
selesai

// Usage
monitor_direktori("documents", max_size_mb=50)
```

### Backup System

```python
dari fileio impor (
    copy, create_dir, list_dir, join_paths,
    get_basename, get_extension, ada
)
dari datetime impor sekarang

fungsi buat_backup(source_dir, backup_base="backups"):
    """Create timestamped backup of directory"""
    
    jika tidak ada(source_dir)
        tampilkan f"Source directory {source_dir} does not exist"
        hasil salah
    selesai
    
    // Create backup directory with timestamp
    timestamp = sekarang().strftime("%Y%m%d_%H%M%S")
    backup_dir = join_paths(backup_base, f"backup_{timestamp}")
    buat_dir(backup_dir)
    
    // Copy all files
    files = list_dir(source_dir)
    copied_count = 0
    
    tampilkan f"Creating backup in {backup_dir}..."
    
    untuk filename dari files
        source_path = join_paths(source_dir, filename)
        backup_path = join_paths(backup_dir, filename)
        
        coba
            copy(source_path, backup_path)
            copied_count = copied_count + 1
            tampilkan f"Backed up: {filename}"
        except Exception sebagai e
            tampilkan f"Failed to backup {filename}: {e}"
        selesai
    selesai
    
    tampilkan f"Backup complete: {copied_count} files copied"
    tampilkan f"Backup location: {backup_dir}"
    
    hasil backup_dir
selesai

// Usage
buat_backup("important_documents")
```

### Log File Manager

```python
dari fileio impor (
    read_lines, write_lines, delete, size, 
    list_dir, join_paths, get_extension
)

fungsi kelola_log_files(log_dir="logs", max_size_mb=10, max_files=100):
    """Manage log files: rotate, compress, clean up"""
    
    max_size_bytes = max_size_mb * 1024 * 1024
    
    jika tidak ada(log_dir)
        tampilkan "Log directory does not exist"
        hasil
    selesai
    
    log_files = [f for f in list_dir(log_dir) jika f.endswith(".log")]
    
    tampilkan f"Managing {panjang(log_files)} log files..."
    
    // Check individual file sizes
    oversized_files = []
    untuk filename dari log_files
        filepath = join_paths(log_dir, filename)
        file_size = size(filepath)
        
        jika file_size > max_size_bytes
            oversized_files.append(filename)
        selesai
    selesai
    
    // Process oversized files
    untuk filename dari oversized_files
        filepath = join_paths(log_dir, filename)
        tampilkan f"Processing oversized file: {filename} ({size(filepath)} bytes)"
        
        // Read lines
        lines = read_lines(filepath)
        
        // Keep only last half of lines
        keep_lines = lines[-(panjang(lines)//2):]
        
        // Write back
        write_lines(filepath, keep_lines)
        tampilkan f"Rotated {filename}, kept {panjang(keep_lines)} lines"
    selesai
    
    // Clean up old log files if too many
    jika panjang(log_files) > max_files
        sort_files = sorted(log_files)
        files_to_remove = sort_files[:panjang(log_files) - max_files]
        
        tampilkan f"Removing {panjang(files_to_remove)} old log files..."
        untuk filename dari files_to_remove
            filepath = join_paths(log_dir, filename)
            delete(filepath)
            tampilkan f"Deleted: {filename}"
        selesai
    selesai
    
    tampilkan "Log file management complete"
selesai

// Usage
kelola_log_files("application_logs", max_size_mb=5, max_files=50)
```

## Performance Notes

- **Large files**: Use `read_bytes()` and `write_bytes()` for binary files
- **Memory efficiency**: `read_lines()` is more memory-efficient for large files
- **Encoding**: Always specify encoding for non-UTF8 files
- **Atomic operations**: Use temporary files for important write operations

## Error Handling Best Practices

```python
dari fileio impor read_text, write_text, exists

fungsi safe_file_operation(filepath):
    coba
        // Check if file exists
        jika exists(filepath)
            content = read_text(filepath)
            // Process content
            processed = huruf_besar(content)
            
            // Write to backup first
            write_text(f"{filepath}.backup", content)
            
            // Write processed content
            write_text(filepath, processed)
            
            tampilkan f"Successfully processed {filepath}"
            hasil benar
        lainnya
            tampilkan f"File {filepath} does not exist"
            hasil salah
        selesai
        
    except PermissionError
        tampilkan f"Permission denied for {filepath}"
        hasil salah
    except Exception sebagai e
        tampilkan f"Error processing {filepath}: {e}"
        hasil salah
    selesai
selesai
```

## Best Practices

1. **Always handle exceptions**: File operations can fail for many reasons
2. **Use context managers**: Prefer `dengan` statements for file operations
3. **Check file existence**: Use `exists()` before operations
4. **Specify encoding**: Always specify encoding for text files
5. **Clean up resources**: Ensure temporary files are cleaned up
6. **Backup important data**: Always create backups before modifications