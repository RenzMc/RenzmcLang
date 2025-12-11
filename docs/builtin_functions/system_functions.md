# System Functions

This document covers all built-in system functions available in RenzMcLang. These functions provide system-level operations, file handling, time operations, and command execution capabilities.

## Core System Functions

### waktu()
Returns the current Unix timestamp.

**Syntax:**
```python
waktu()
```

**Returns:**
- Float: Current Unix timestamp in seconds

**Examples:**
```python
// Get current timestamp
timestamp = waktu()
tampilkan timestamp         // Output: 1703123456.789 (example)

// Use for timing operations
start = waktu()
// Do some work
end = waktu()
elapsed = end - start
tampilkan f"Elapsed time: {elapsed} seconds"
```

---

### tidur()
Pauses execution for a specified number of seconds.

**Syntax:**
```python
tidur(seconds)
```

**Parameters:**
- `seconds` (number): Number of seconds to pause

**Examples:**
```python
// Pause for 2 seconds
tampilkan "Starting..."
tidur(2)
tampilkan "Done!"

// Pause for half a second
tidur(0.5)

// Pause with user feedback
tampilkan "Processing data..."
tidur(1)
tampilkan "Data processed!"
```

---

### tanggal()
Returns the current date and time as a formatted string.

**Syntax:**
```python
tanggal()
```

**Returns:**
- String: Current date and time in "YYYY-MM-DD HH:MM:SS" format

**Examples:**
```python
// Get current date and time
sekarang = tanggal()
tampilkan sekarang           // Output: "2024-01-15 14:30:25"

// Use in logging
log_message = f"[{tanggal()}] Application started"
tampilkan log_message
```

---

### buat_uuid()
Generates a unique UUID (Universally Unique Identifier).

**Syntax:**
```python
buat_uuid()
```

**Returns:**
- String: UUID string in standard format

**Examples:**
```python
// Generate unique identifier
session_id = buat_uuid()
tampilkan session_id         // Output: "550e8400-e29b-41d4-a716-446655440000"

// Use for unique filenames
filename = f"data_{buat_uuid()}.json"
tampilkan filename          // Output: "data_550e8400-e29b-41d4-a716-446655440000.json"

// Use for transaction IDs
transaction_id = buat_uuid()
tampilkan f"Transaction ID: {transaction_id}"
```

## File Operations

### buka() / open_file()
Opens a file for reading or writing operations.

**Syntax:**
```python
buka(nama_file, mode)
open_file(nama_file, mode)
```

**Parameters:**
- `nama_file` (string): Path to the file
- `mode` (string, optional): File open mode (default: "r")
  - "r": Read mode (default)
  - "w": Write mode (overwrites existing file)
  - "a": Append mode
  - "r+": Read and write mode
  - "w+": Write and read mode
  - "a+": Append and read mode

**Returns:**
- File object: File handle for operations

**Examples:**
```python
// Read from file
file = buka("data.txt")
content = file.baca()
file.tutup()
tampilkan content

// Write to file
file = buka("output.txt", "w")
file.tulis("Hello, World!")
file.tutup()

// Append to file
file = buka("log.txt", "a")
file.tulis(f"[{tanggal()}] New entry\n")
file.tutup()

// Using English alias
file = open_file("config.json", "r")
config_data = file.baca()
file.tutup()

// Context manager style (if supported)
dengan buka("data.txt") sebagai file
    content = file.baca()
    tampilkan content
selesai
```

## Command Execution Functions

### jalankan_perintah()
Executes a system command with security controls.

**Syntax:**
```python
jalankan_perintah(command, shell, capture_output)
```

**Parameters:**
- `command` (string): Command to execute
- `shell` (boolean, optional): Use shell for execution (default: benar)
- `capture_output` (boolean, optional): Capture command output (default: benar)

**Returns:**
- Dict: Result containing:
  - "stdout": Standard output
  - "stderr": Standard error
  - "returncode": Exit code

**Examples:**
```python
// Execute safe command
result = jalankan_perintah("ls -la")
tampilkan result["stdout"]

// Check command result
result = jalankan_perintah("echo 'Hello World'")
tampilkan result["stdout"]    // Output: "Hello World\n"
tampilkan result["returncode"] // Output: 0

// Handle command errors
result = jalankan_perintah("cat nonexistent.txt")
tampilkan result["stderr"]    // Error message
tampilkan result["returncode"] // Non-zero exit code

// Execute command with custom shell
result = jalankan_perintah("python --version", shell=benar)
tampilkan result["stdout"]    // Python version info
```

## Security Functions

### atur_sandbox()
Enables or disables sandbox mode for command execution.

**Syntax:**
```python
atur_sandbox(enabled)
```

**Parameters:**
- `enabled` (boolean, optional): Enable sandbox (default: benar)

**Returns:**
- Boolean: Current sandbox status

**Examples:**
```python
// Enable sandbox
status = atur_sandbox(benar)
tampilkan status            // Output: benar

// Disable sandbox
status = atur_sandbox(salah)
tampilkan status            // Output: salah

// Check current status
is_sandboxed = atur_sandbox()
tampilkan f"Sandbox enabled: {is_sandboxed}"
```

### tambah_perintah_aman()
Adds a command to the safe commands list.

**Syntax:**
```python
tambah_perintah_aman(command)
```

**Parameters:**
- `command` (string): Command to add to safe list

**Returns:**
- Boolean: True if added successfully

**Examples:**
```python
// Add custom safe command
tambah_perintah_aman("python")
tambah_perintah_aman("node")
tambah_perintah_aman("npm")

// Now these commands can be executed in sandbox mode
atur_sandbox(benar)
result = jalankan_perintah("python --version")
tampilkan result["stdout"]
```

### hapus_perintah_aman()
Removes a command from the safe commands list.

**Syntax:**
```python
hapus_perintah_aman(command)
```

**Parameters:**
- `command` (string): Command to remove from safe list

**Returns:**
- Boolean: True if removed successfully, False if not found

**Examples:**
```python
// Remove command from safe list
success = hapus_perintah_aman("python")
tampilkan success            // Output: benar

// Try to remove non-existent command
success = hapus_perintah_aman("nonexistent")
tampilkan success            // Output: salah
```

## System Information Operations

### Safe Commands List
By default, the following commands are safe to execute in sandbox mode:
- `ls` - List directory contents
- `cat` - Display file contents
- `echo` - Display message
- `pwd` - Print working directory
- `date` - Display date and time
- `whoami` - Display current user
- `uname` - Display system information
- `grep` - Search text patterns
- `find` - Find files
- `wc` - Word count
- `head` - Display first lines
- `tail` - Display last lines
- `sort` - Sort lines
- `uniq` - Remove duplicate lines

## Advanced Usage Examples

### File Processing Pipeline

```python
// Process multiple files with timing
start_time = waktu()

files = ["data1.txt", "data2.txt", "data3.txt"]
results = []

untuk setiap filename dari files
    tampilkan f"Processing {filename}..."
    
    file = buka(filename, "r")
    content = file.baca()
    file.tutup()
    
    // Process content
    processed = huruf_besar(content)
    results.append(processed)
    
    tidur(0.1)  // Brief pause
selesai

end_time = waktu()
elapsed = end_time - start_time

tampilkan f"Processed {panjang(files)} files in {elapsed} seconds"
```

### System Monitoring

```python
// Create system monitoring function
fungsi monitor_system():
    timestamp = waktu()
    date_str = tanggal()
    session_id = buat_uuid()
    
    tampilkan f"=== System Monitor ==="
    tampilkan f"Time: {date_str}"
    tampilkan f"Timestamp: {timestamp}"
    tampilkan f"Session: {session_id}"
    
    // Get system info
    hasil whoami = jalankan_perintah("whoami")
    tampilkan f"User: {hasil['stdout'].strip()}"
    
    hasil uname = jalankan_perintah("uname -a")
    tampilkan f"System: {hasil['stdout'].strip()}"
selesai

// Run monitoring
monitor_system()
```

### Secure File Operations

```python
// Secure file backup with UUID
fungsi backup_file(filepath):
    // Validate file exists
    coba
        original = buka(filepath, "r")
        content = original.baca()
        original.tutup()
    except
        tampilkan "Error: File not found or not readable"
        hasil salah
    selesai
    
    // Create backup with UUID
    backup_name = f"backup_{buat_uuid()}_{filepath}"
    backup = buka(backup_name, "w")
    backup.tulis(content)
    backup.tutup()
    
    tampilkan f"Backup created: {backup_name}"
    hasil benar
selesai

// Usage
backup_file("important.txt")
```

## Security Considerations

1. **Sandbox Mode**: Always enable sandbox mode for untrusted code
2. **Command Validation**: Only execute commands from the safe list
3. **File Permissions**: Ensure proper file permissions before operations
4. **Timeout Protection**: Commands have built-in 30-second timeout
5. **Input Validation**: Validate file paths and command inputs

## Error Handling

```python
// Safe command execution with error handling
fungsi safe_execute(command):
    coba
        result = jalankan_perintah(command)
        tampilkan "Command executed successfully"
        tampilkan f"Exit code: {result['returncode']}"
        
        jika result['returncode'] == 0
            tampilkan "Output:"
            tampilkan result['stdout']
        lainnya
            tampilkan "Error output:"
            tampilkan result['stderr']
        selesai
        
    except SecurityError sebagai e
        tampilkan f"Security error: {e.message}"
    except TimeoutError
        tampilkan "Command timed out"
    except Exception sebagai e
        tampilkan f"Unexpected error: {e}"
    selesai
selesai

// Usage
safe_execute("ls -la")
```