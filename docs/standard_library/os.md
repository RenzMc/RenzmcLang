# Library OS

## Overview

Library `os` menyediakan interface untuk fungsi-fungsi sistem operasi dengan nama fungsi dalam Bahasa Indonesia. Library ini mencakup operasi environment variables, manajemen process, manipulasi path dan file, serta informasi sistem.

## Import Library

```python
dari renzmc.library.os impor *
```

Atau import fungsi spesifik:

```python
dari renzmc.library.os impor getcwd, chdir, listdir, mkdir, exists
```

## Environment Variables

### getenv(key, default=None)

Mendapatkan nilai environment variable.

**Parameter:**
- `key` (string): Nama environment variable
- `default` (string): Default value jika tidak ada (default None)

**Return:**
- `string`: Nilai environment variable atau default

**Contoh:**
```python
// Dapatkan PATH
path_value itu getenv("PATH", "")
tampilkan f"PATH: {path_value}"

// Dapatkan HOME
home_dir itu getenv("HOME")
tampilkan f"Home directory: {home_dir}"

// Dapatkan custom variable dengan default
custom_var itu getenv("MY_APP", "default_value")
tampilkan f"Custom var: {custom_var}"
```

### setenv(key, value)

Mengatur environment variable.

**Parameter:**
- `key` (string): Nama environment variable
- `value` (string): Nilai yang akan diset

**Contoh:**
```python
// Set environment variable
setenv("MY_APP_NAME", "RenzMcApp")
setenv("MY_VERSION", "1.0.0")

// Verifikasi
app_name itu getenv("MY_APP_NAME")
tampilkan f"App name: {app_name}"
```

### unsetenv(key)

Menghapus environment variable.

**Parameter:**
- `key` (string): Nama environment variable yang akan dihapus

**Contoh:**
```python
// Set dan hapus variable
setenv("TEMP_VAR", "temporary_value")
tampilkan getenv("TEMP_VAR")  // "temporary_value"

unsetenv("TEMP_VAR")
tampilkan getenv("TEMP_VAR")  // None
```

### environ()

Mendapatkan semua environment variables.

**Return:**
- `dict`: Dictionary berisi semua environment variables

**Contoh:**
```python
// Dapatkan semua environment variables
all_env itu environ()
tampilkan f"Total environment variables: {panjang(all_env)}"

// Tampilkan beberapa variables
tampilkan f"Shell: {all_env.get('SHELL', 'N/A')}"
tampilkan f"User: {all_env.get('USER', 'N/A')}"
tampilkan f"Language: {all_env.get('LANG', 'N/A')}"

// Iterasi semua variables
untuk key, value dalam all_env.items():
    jika "PATH" dalam key:
        tampilkan f"{key}: {potong(value, 0, 50)}..."
```

## Process Functions

### getpid()

Mendapatkan process ID dari process saat ini.

**Return:**
- `int`: Process ID

**Contoh:**
```python
current_pid itu getpid()
tampilkan f"Current process ID: {current_pid}"

// Gunakan untuk logging atau debugging
log_message itu f"Process {getpid()} started"
tampilkan log_message
```

### getppid()

Mendapatkan parent process ID.

**Return:**
- `int`: Parent Process ID

**Contoh:**
```python
my_pid itu getpid()
parent_pid itu getppid()

tampilkan f"My PID: {my_pid}"
tampilkan f"Parent PID: {parent_pid}"
```

### system(command)

Menjalankan command di system shell.

**Parameter:**
- `command` (string): Command yang akan dijalankan

**Return:**
- `int`: Exit code dari command

**Contoh:**
```python
// Jalankan system command
exit_code itu system("echo 'Hello from shell'")
tampilkan f"Exit code: {exit_code}"

// List files
exit_code itu system("ls -la")
tampilkan f"List exit code: {exit_code}"

// Create directory
exit_code itu system("mkdir -p test_dir")
tampilkan f"Create directory exit code: {exit_code}"
```

## Path Functions

### getcwd()

Mendapatkan current working directory.

**Return:**
- `string`: Path dari current working directory

**Contoh:**
```python
current_dir itu getcwd()
tampilkan f"Current directory: {current_dir}"

// Gunakan untuk path operations
full_path itu join(getcwd(), "data", "file.txt")
tampilkan f"Full path: {full_path}"
```

### chdir(path)

Mengubah current working directory.

**Parameter:**
- `path` (string): Path directory baru

**Contoh:**
```python
original_dir itu getcwd()
tampilkan f"Original directory: {original_dir}"

coba
    chdir("/tmp")
    new_dir itu getcwd()
    tampilkan f"New directory: {new_dir}"
    
    // Kembali ke directory asli
    chdir(original_dir)
    tampilkan f"Back to: {getcwd()}"
tangkap e
    tampilkan f"Error changing directory: {e}"
selesai
```

### listdir(path=".")

Mendaftar file dan directory dalam path.

**Parameter:**
- `path` (string): Path yang akan di-list (default: current directory)

**Return:**
- `list`: List nama file dan directory

**Contoh:**
```python
// List current directory
files itu listdir(".")
tampilkan f"Items in current directory: {files}"

// List specific directory
coba
    tmp_files itu listdir("/tmp")
    tampilkan f"Items in /tmp: {panjang(tmp_files)} items"
    
    // Filter hanya files
    file_list itu [f untuk f dalam tmp_files jika isfile(join("/tmp", f))]
    dir_list itu [d untuk d dalam tmp_files jika isdir(join("/tmp", d))]
    
    tampilkan f"Files: {file_list}"
    tampilkan f"Directories: {dir_list}"
tangkap e
    tampilkan f"Error listing directory: {e}"
selesai
```

### mkdir(path, mode=0o777)

Membuat directory baru.

**Parameter:**
- `path` (string): Path directory yang akan dibuat
- `mode` (int): Permission mode (default 0o777)

**Contoh:**
```python
coba
    // Buat directory
    mkdir("my_new_dir")
    tampilkan "Directory created successfully"
    
    // Buat dengan permission spesifik
    mkdir("restricted_dir", 0o755)
    tampilkan "Directory with specific permissions created"
tangkap e
    tampilkan f"Error creating directory: {e}"
selesai
```

### makedirs(path, mode=0o777, exist_ok=False)

Membuat directory beserta parent directories.

**Parameter:**
- `path` (string): Path yang akan dibuat
- `mode` (int): Permission mode
- `exist_ok` (boolean): Tidak error jika directory sudah ada

**Contoh:**
```python
coba
    // Buat nested directories
    makedirs("level1/level2/level3")
    tampilkan "Nested directories created"
    
    // Buat dengan exist_ok
    makedirs("level1/level2", exist_ok=True)
    tampilkan "Directory exists or created successfully"
    
    // Buat dengan permission
    makedirs("secure/data/private", mode=0o700, exist_ok=True)
    tampilkan "Secure directories created"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### rmdir(path)

Menghapus directory (harus kosong).

**Parameter:**
- `path` (string): Path directory yang akan dihapus

**Contoh:**
```python
coba
    // Buat dan hapus directory kosong
    mkdir("temp_dir")
    rmdir("temp_dir")
    tampilkan "Directory removed successfully"
tangkap e
    tampilkan f"Error removing directory: {e}"
selesai
```

### removedirs(path)

Menghapus directory beserta parent directories yang kosong.

**Parameter:**
- `path` (string): Path yang akan dihapus

**Contoh:**
```python
coba
    // Buat nested directories
    makedirs("a/b/c")
    
    // Hapus dari dalam ke luar
    removedirs("a/b/c")
    tampilkan "Nested directories removed"
tangkap e
    tampilkan f"Error: {e}"
selesai
```

### remove(path)

Menghapus file.

**Parameter:**
- `path` (string): Path file yang akan dihapus

**Contoh:**
```python
coba
    // Buat test file
    "test content" >> test_file.txt
    
    // Hapus file
    remove("test_file.txt")
    tampilkan "File removed successfully"
tangkap e
    tampilkan f"Error removing file: {e}"
selesai
```

### rename(src, dst)

Mengubah nama file atau directory.

**Parameter:**
- `src` (string): Path lama
- `dst` (string): Path baru

**Contoh:**
```python
coba
    // Buat file
    "original content" >> old_name.txt
    
    // Rename file
    rename("old_name.txt", "new_name.txt")
    tampilkan "File renamed successfully"
    
    // Rename directory
    mkdir("old_dir")
    rename("old_dir", "new_dir")
    tampilkan "Directory renamed successfully"
tangkap e
    tampilkan f"Error renaming: {e}"
selesai
```

## File Functions

### exists(path)

Mengecek apakah file atau directory ada.

**Parameter:**
- `path` (string): Path yang akan dicek

**Return:**
- `boolean`: True jika ada, False jika tidak

**Contoh:**
```python
// Cek file
file_exists itu exists("/etc/passwd")
tampilkan f"/etc/passwd exists: {file_exists}"

// Cek directory
dir_exists itu exists("/tmp")
tampilkan f"/tmp exists: {dir_exists}"

// Cek custom path
custom_path itu "my_data.txt"
if exists(custom_path):
    tampilkan f"{custom_path} exists"
lainnya:
    tampilkan f"{custom_path} does not exist"
```

### isfile(path)

Mengecek apakah path adalah file.

**Parameter:**
- `path` (string): Path yang akan dicek

**Return:**
- `boolean`: True jika file, False jika bukan

**Contoh:**
```python
// Test various paths
paths itu ["/etc/passwd", "/tmp", ".", "nonexistent"]

untuk path dalam paths:
    jika exists(path):
        jika isfile(path):
            tampilkan f"{path} adalah file"
        lainnya:
            tampilkan f"{path} bukan file"
    lainnya:
        tampilkan f"{path} tidak ada"
```

### isdir(path)

Mengecek apakah path adalah directory.

**Parameter:**
- `path` (string): Path yang akan dicek

**Return:**
- `boolean`: True jika directory, False jika bukan

**Contoh:**
```python
// Filter directories dari listing
items itu listdir(".")
directories itu [item untuk item dalam items jika isdir(item)]
files itu [item untuk item dalam items jika isfile(item)]

tampilkan f"Directories: {directories}"
tampilkan f"Files: {files}"
```

### islink(path)

Mengecek apakah path adalah symbolic link.

**Parameter:**
- `path` (string): Path yang akan dicek

**Return:**
- `boolean`: True jika symbolic link, False jika bukan

**Contoh:**
```python
// Buat symbolic link (jika didukung)
coba
    system("ln -s /tmp tmp_link")
    jika islink("tmp_link"):
        tampilkan "tmp_link adalah symbolic link"
    lainnya:
        tampilkan "tmp_link bukan symbolic link"
tangkap e
    tampilkan "Symbolic link creation failed"
selesai
```

### access(path, mode)

Mengecek akses file/directory.

**Parameter:**
- `path` (string): Path yang akan dicek
- `mode` (int): Mode akses (F_OK, R_OK, W_OK, X_OK)

**Return:**
- `boolean`: True jika akses diizinkan

**Contoh:**
```python
test_path itu "/tmp"

// Cek berbagai akses
exists_check itu access(test_path, F_OK)
read_check itu access(test_path, R_OK)
write_check itu access(test_path, W_OK)
execute_check itu access(test_path, X_OK)

tampilkan f"Exists: {exists_check}"
tampilkan f"Readable: {read_check}"
tampilkan f"Writable: {write_check}"
tampilkan f"Executable: {execute_check}"
```

### stat(path)

Mendapatkan informasi file/directory.

**Parameter:**
- `path` (string): Path yang akan dicek

**Return:**
- `object`: Stat result object

**Contoh:**
```python
coba
    // Buat test file
    "test content" >> test_stat.txt
    
    // Dapatkan stat info
    info itu stat("test_stat.txt")
    
    tampilkan f"Size: {info.st_size} bytes"
    tampilkan f"Last modified: {info.st_mtime}"
    tampilkan f"Last accessed: {info.st_atime}"
    tampilkan f"Created: {info.st_ctime}"
    
    // Check mode
    mode itu info.st_mode
    tampilkan f"Mode: {mode}"
    
    // Clean up
    remove("test_stat.txt")
tangkap e
    tampilkan f"Error getting stat: {e}"
selesai
```

### chmod(path, mode)

Mengubah permission file/directory.

**Parameter:**
- `path` (string): Path yang akan diubah
- `mode` (int): Permission mode

**Contoh:**
```python
coba
    // Buat file
    "test content" >> test_perm.txt
    
    // Ubah permission
    chmod("test_perm.txt", 0o644)
    tampilkan "Permissions changed to 644"
    
    // Make executable
    chmod("test_perm.txt", 0o755)
    tampilkan "Permissions changed to 755"
    
    // Clean up
    remove("test_perm.txt")
tangkap e
    tampilkan f"Error changing permissions: {e}"
selesai
```

## System Information

### uname()

Mendapatkan informasi sistem.

**Return:**
- `object`: System information object

**Contoh:**
```python
sys_info itu uname()
tampilkan f"System name: {sys_info.sysname}"
tampilkan f"Node name: {sys_info.nodename}"
tampilkan f"Release: {sys_info.release}"
tampilkan f"Version: {sys_info.version}"
tampilkan f"Machine: {sys_info.machine}"
```

### platform()

Mendapatkan platform informasi.

**Return:**
- `string`: Platform string

**Contoh:**
```python
platform_info itu platform()
tampilkan f"Platform: {platform_info}"

// Check operating system
jika "Linux" dalam platform_info:
    tampilkan "Running on Linux"
jika "Darwin" dalam platform_info:
    tampilkan "Running on macOS"
jika "Windows" dalam platform_info:
    tampilkan "Running on Windows"
```

### architecture()

Mendapatkan arsitektur sistem.

**Return:**
- `tuple`: (architecture, linkage)

**Contoh:**
```python
arch, linkage itu architecture()
tampilkan f"Architecture: {arch}"
tampilkan f"Linkage: {linkage}"

// Check 64-bit vs 32-bit
jika "64" dalam arch:
    tampilkan "64-bit system"
lainnya:
    tampilkan "32-bit system"
```

## Path Utilities

### join(*paths)

Menggabungkan path components.

**Parameter:**
- `*paths`: Path components yang akan digabungkan

**Return:**
- `string`: Combined path

**Contoh:**
```python
// Basic path joining
path1 itu join("home", "user", "documents")
tampilkan path1  // "home/user/documents"

// Cross-platform path joining
path2 itu join("/", "tmp", "data", "file.txt")
tampilkan path2  // "/tmp/data/file.txt"

// Multiple components
base_dir itu "/var"
app_dir itu "myapp"
log_file itu "logs"
file_name itu "app.log"

full_path itu join(base_dir, app_dir, log_file, file_name)
tampilkan f"Full path: {full_path}"
```

### split(path)

Memisahkan path menjadi (head, tail).

**Parameter:**
- `path` (string): Path yang akan dipisahkan

**Return:**
- `tuple`: (head, tail)

**Contoh:**
```python
// Split path components
head, tail itu split("/home/user/documents/file.txt")
tampilkan f"Head: {head}"   // "/home/user/documents"
tampilkan f"Tail: {tail}"   // "file.txt"

// Split relative path
head2, tail2 itu split("relative/path/file")
tampilkan f"Head: {head2}"  // "relative/path"
tampilkan f"Tail: {tail2}"  // "file"
```

### basename(path)

Mendapatkan filename dari path.

**Parameter:**
- `path` (string): Path input

**Return:**
- `string`: Filename

**Contoh:**
```python
// Extract filename
filename1 itu basename("/home/user/documents/file.txt")
tampilkan filename1  // "file.txt"

filename2 itu basename("/var/log/syslog")
tampilkan filename2  // "syslog"

filename3 itu basename("relative/path/data.csv")
tampilkan filename3  // "data.csv"
```

### dirname(path)

Mendapatkan directory dari path.

**Parameter:**
- `path` (string): Path input

**Return:**
- `string`: Directory path

**Contoh:**
```python
// Extract directory
dir1 itu dirname("/home/user/documents/file.txt")
tampilkan dir1  // "/home/user/documents"

dir2 itu dirname("/var/log/syslog")
tampilkan dir2  // "/var/log"

dir3 itu dirname("relative/path/data.csv")
tampilkan dir3  // "relative/path"
```

### abspath(path)

Mendapatkan absolute path.

**Parameter:**
- `path` (string): Path input

**Return:**
- `string`: Absolute path

**Contoh:**
```python
// Get absolute paths
abs1 itu abspath("file.txt")
tampilkan f"Absolute of file.txt: {abs1}"

abs2 itu abspath("./data/info.json")
tampilkan f"Absolute of ./data/info.json: {abs2}"

abs3 itu abspath("../parent/child")
tampilkan f"Absolute of ../parent/child: {abs3}"

// Current directory absolute
current_abs itu abspath(".")
tampilkan f"Current directory absolute: {current_abs}"
```

## Constants

### Access Modes
- `F_OK`: Test existence
- `R_OK`: Test read permission
- `W_OK`: Test write permission  
- `X_OK`: Test execute permission

## Indonesian Aliases

Library juga menyediakan alias dalam Bahasa Indonesia:

```python
// Environment aliases
dapatkan_env(key, default=None)  // getenv
atur_env(key, value)            // setenv
hapus_env(key)                  // unsetenv
lingkungan()                    // environ

// Process aliases  
id_proses()                     // getpid
id_proses_orang_tua()           // getppid
jalankan_sistem(command)        // system

// Path aliases
dapatkan_dir_sekarang()         // getcwd
ubah_dir(path)                  // chdir
daftar_dir(path=".")            // listdir
buat_dir(path, mode=0o777)      // mkdir
buat_dir_banyak(path, mode=0o777, exist_ok=False)  // makedirs
hapus_dir(path)                 // rmdir
hapus_dir_banyak(path)          // removedirs
hapus_file(path)                // remove
ganti_nama(src, dst)            // rename

// File aliases
ada(path)                       // exists
adalah_file(path)               // isfile
adalah_dir(path)                // isdir
adalah_link(path)               // islink
akses(path, mode)               // access
info_file(path)                 // stat
ubah_mode(path, mode)           // chmod

// System aliases
info_sistem()                   // uname
platform_sistem()               // platform
arsitektur()                    // architecture

// Path utility aliases
gabung_path(*paths)             // join
pisah_path(path)                // split
nama_file(path)                 // basename
nama_dir(path)                  // dirname
path_absolut(path)              // abspath
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.os impor *

tampilkan "=== Demo OS Library ==="

// 1. Environment variables
tampilkan "\n1. Environment Variables:"
setenv("DEMO_APP", "RenzMcLang")
demo_var itu getenv("DEMO_APP")
tampilkan f"DEMO_APP: {demo_var}"

all_env itu environ()
tampilkan f"Total environment vars: {panjang(all_env)}"

// 2. Process information
tampilkan "\n2. Process Information:"
pid saya getpid()
ppid saya getppid()
tampilkan f"Process ID: {pid}"
tampilkan f"Parent PID: {ppid}"

// 3. Working directory operations
tampilkan "\n3. Directory Operations:"
original_dir itu getcwd()
tampilkan f"Current directory: {original_dir}"

// Buat struktur directory untuk demo
demo_dirs itu ["demo_data", "demo_data/logs", "demo_data/config"]

untuk dir_path dalam demo_dirs:
    coba
        makedirs(dir_path, exist_ok=True)
        tampilkan f"Created: {dir_path}"
    tangkap e:
        tampilkan f"Failed to create {dir_path}: {e}"
    selesai

// List directories
current_items itu listdir(".")
dirs_only itu [item untuk item dalam current_items jika isdir(item)]
files_only itu [item untuk item dalam current_items jika isfile(item)]

tampilkan f"Directories: {dirs_only}"
tampilkan f"Files: {files_only}"

// 4. File operations
tampilkan "\n4. File Operations:"
// Buat beberapa files
test_files itu ["demo.txt", "demo_data/logs/app.log", "demo_data/config/settings.json"]

untuk file_path dalam test_files:
    coba
        "Demo content" >> {file_path}
        tampilkan f"Created: {file_path}"
        
        // Get file info
        jika exists(file_path):
            info itu stat(file_path)
            tampilkan f"  Size: {info.st_size} bytes"
    tangkap e:
        tampilkan f"Error with {file_path}: {e}"
    selesai

// 5. Path utilities
tampilkan "\n5. Path Utilities:"
test_path itu "/home/user/documents/project/data/file.txt"
tampilkan f"Original path: {test_path}"
tampilkan f"Directory: {dirname(test_path)}"
tampilkan f"Filename: {basename(test_path)}"

joined_path itu join("/tmp", "data", "files", "output.txt")
tampilkan f"Joined path: {joined_path}"

absolute_path itu abspath("./relative/path.txt")
tampilkan f"Absolute path: {absolute_path}"

// 6. System information
tampilkan "\n6. System Information:"
sys_info itu uname()
tampilkan f"System: {sys_info.sysname} {sys_info.release}"
tampilkan f"Machine: {sys_info.machine}"

platform_info itu platform()
tampilkan f"Platform: {platform_info}"

arch, linkage itu architecture()
tampilkan f"Architecture: {arch}"

// 7. Permission and access checks
tampilkan "\n7. Permission Checks:"
demo_file itu "demo.txt"

jika exists(demo_file):
    tampilkan f"{demo_file} exists: {True}"
    tampilkan f"{demo_file} is file: {isfile(demo_file)}"
    tampilkan f"{demo_file} readable: {access(demo_file, R_OK)}"
    tampilkan f"{demo_file} writable: {access(demo_file, W_OK)}"
selesai

// 8. Indonesian aliases demo
tampilkan "\n8. Indonesian Aliases:"
gunakan_alias itu getcwd()
alias_dir itu dapatkan_dir_sekarang()
tampilkan f"Same result: {gunakan_alias == alias_dir}"

// 9. Cleanup
tampilkan "\n9. Cleanup:"
// Hapus files yang dibuat
untuk file_path dalam test_files:
    coba
        jika exists(file_path):
            remove(file_path)
            tampilkan f"Removed: {file_path}"
    tangkap e:
        tampilkan f"Error removing {file_path}: {e}"
    selesai

// Hapus directories
untuk dir_path dalam reversed(demo_dirs):
    coba
        jika exists(dir_path):
            rmdir(dir_path)
            tampilkan f"Removed directory: {dir_path}"
    tangkap e:
        tampilkan f"Error removing {dir_path}: {e}"
    selesai

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **File Management**: Create, read, write, delete files dan directories
2. **Path Operations**: Manipulasi path untuk cross-platform compatibility
3. **Environment Configuration**: Mengatur dan membaca environment variables
4. **System Integration**: Interaksi dengan sistem operasi
5. **Process Management**: Mendapatkan informasi process
6. **Permission Management**: Mengatur file/directory permissions
7. **Application Deployment**: Setup dan cleanup application directories
8. **Logging dan Monitoring**: System information gathering

## Security Considerations

- **Path Traversal**: Validasi input path untuk mencegah directory traversal
- **Permission Checks**: Selalu cek permission sebelum operasi file
- **Command Injection**: Hati-hati dengan `system()` - gunakan subprocess yang lebih aman
- **Environment Variables**: Jangan simpan sensitive data di environment variables
- **Symbolic Links**: Perhatikan symbolic links untuk security implications

## Error Handling

- Gunakan `coba...tangkap...selesai` untuk file operations
- `FileNotFoundError` untuk file tidak ditemukan
- `PermissionError` untuk permission issues
- `OSError` untuk system-related errors
- `ValueError` untuk invalid paths atau parameters

## Cross-Platform Considerations

- Gunakan `join()` untuk path separator yang tepat
- Permission modes berbeda antara Windows dan Unix-like systems
- Path case sensitivity berbeda antar sistem
- Beberapa functions mungkin tidak tersedia di semua platform

## Best Practices

1. Gunakan `abspath()` untuk consistent path handling
2. Selalu cek dengan `exists()` sebelum operasi file
3. Gunakan `with open()` untuk file operations (jika available)
4. Clean up temporary files dan directories
5. Gunakan appropriate permission modes
6. Handle exceptions dengan baik
7. Gunakan Indonesian aliases untuk code readability