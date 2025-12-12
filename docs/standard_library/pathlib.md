# Library Pathlib

## Overview

Library `pathlib` menyediakan interface object-oriented untuk path manipulation filesystem. Library ini mengimplementasikan konsep modern untuk operasi path yang lebih intuitive dan cross-platform, dengan nama fungsi dalam Bahasa Indonesia.

## Import Library

```python
dari renzmc.library.pathlib impor *
```

Atau import class/fungsi spesifik:

```python
dari renzmc.library.pathlib impor Path, path_current, gabung_path
```

## Class Path

Class `Path` adalah class utama untuk operasi path object-oriented.

### Constructor

```python
Path(*pathsegments)
```

**Parameter:**
- `*pathsegments`: Path segments yang akan digabungkan

**Contoh:**
```python
// Buat Path object dari string
p1 itu Path("/home/user/documents")
tampilkan p1  // /home/user/documents

// Buat Path dari multiple segments
p2 itu Path("/home", "user", "documents", "file.txt")
tampilkan p2  // /home/user/documents/file.txt

// Buat relative path
p3 itu Path("data", "files", "output.json")
tampilkan p3  // data/files/output.json
```

### Properties dan Basic Methods

#### dapatkan_nama()

Mendapatkan nama file atau direktori terakhir.

**Return:**
- `string`: Nama file atau direktori

**Contoh:**
```python
p itu Path("/home/user/documents/report.pdf")
filename itu p.dapatkan_nama()
tampilkan filename  // "report.pdf"

dir_path itu Path("/home/user/documents")
dirname itu dir_path.dapatkan_nama()
tampilkan dirname  // "documents"
```

#### dapatkan_stem()

Mendapatkan nama tanpa extension.

**Return:**
- `string`: Nama tanpa extension

**Contoh:**
```python
p itu Path("/home/user/documents/report.pdf")
stem itu p.dapatkan_stem()
tampilkan stem  // "report"

p2 itu Path("archive.tar.gz")
stem2 itu p2.dapatkan_stem()
tampilkan stem2  // "archive.tar"
```

#### dapatkan_extension()

Mendapatkan file extension.

**Return:**
- `string`: Extension file (termasuk titik)

**Contoh:**
```python
p itu Path("/home/user/documents/report.pdf")
ext itu p.dapatkan_extension()
tampilkan ext  // ".pdf"

p2 itu Path("archive.tar.gz")
ext2 itu p2.dapatkan_extension()
tampilkan ext2  // ".gz"
```

#### dapatkan_parent()

Mendapatkan parent directory.

**Return:**
- `Path`: Path object untuk parent directory

**Contoh:**
```python
p itu Path("/home/user/documents/report.pdf")
parent itu p.dapatkan_parent()
tampilkan parent  // /home/user/documents

// Chain multiple parent calls
grandparent itu parent.dapatkan_parent()
tampilkan grandparent  // /home/user
```

#### dapatkan_absolute()

Mendapatkan absolute path.

**Return:**
- `Path`: Absolute path object

**Contoh:**
```python
// Relative path
p itu Path("data/file.txt")
abs_p itu p.dapatkan_absolute()
tampilkan abs_p  // /current/working/directory/data/file.txt

// Already absolute path
abs_dir itu Path("/tmp/data")
abs_result itu abs_dir.dapatkan_absolute()
tampilkan abs_result  // /tmp/data
```

#### dapatkan_resolve()

Resolve path (hilangkan symbolic links, .., .).

**Return:**
- `Path`: Resolved path object

**Contoh:**
```python
// Path dengan .. dan .
p itu Path("/home/user/../user/documents/./file.txt")
resolved itu p.dapatkan_resolve()
tampilkan resolved  // /home/user/documents/file.txt

// Resolve relative path
rel_p itu Path("../data/file.txt")
resolved_rel itu rel_p.dapatkan_resolve()
tampilkan resolved_rel  // /actual/resolved/path
```

### Existence dan Type Checking

#### ada()

Mengecek apakah path ada.

**Return:**
- `boolean`: True jika ada, False jika tidak

**Contoh:**
```python
p itu Path("/etc/passwd")
jika p.ada():
    tampilkan "File exists"
lainnya:
    tampilkan "File does not exist"

// Check custom path
custom_file itu Path("my_data.txt")
jika custom_file.ada():
    tampilkan "Custom file exists"
```

#### adalah_file()

Mengecek apakah path adalah file.

**Return:**
- `boolean`: True jika file, False jika bukan

**Contoh:**
```python
p itu Path("/etc/passwd")
jika p.ada() dan p.adalah_file():
    tampilkan "Path is a file"

dir_path itu Path("/tmp")
jika dir_path.ada() dan dir_path.adalah_dir():
    tampilkan "Path is a directory"
```

#### adalah_dir()

Mengecek apakah path adalah directory.

**Return:**
- `boolean`: True jika directory, False jika bukan

**Contoh:**
```python
// Filter directories dari list
paths itu [Path("."), Path("/etc"), Path("/etc/passwd")]
dirs itu [p untuk p dalam paths jika p.ada() dan p.adalah_dir()]
tampilkan dirs
```

#### adalah_symlink()

Mengecek apakah path adalah symbolic link.

**Return:**
- `boolean`: True jika symbolic link, False jika bukan

**Contoh:**
```python
// Check symbolic link
link_path itu Path("/usr/bin/python")
jika link_path.ada() dan link_path.adalah_symlink():
    tampilkan "Path is a symbolic link"
```

### Directory Operations

#### buat_dir(parents=False, exist_ok=False)

Membuat directory.

**Parameter:**
- `parents` (boolean): Buat parent directories jika tidak ada
- `exist_ok` (boolean): Tidak error jika directory sudah ada

**Contoh:**
```python
// Buat single directory
p itu Path("new_directory")
p.buat_dir()
tampilkan "Directory created"

// Buat nested directories
nested itu Path("level1/level2/level3")
nested.buat_dir(parents=True)
tampilkan "Nested directories created"

// Buat dengan exist_ok
existing itu Path("existing_dir")
existing.buat_dir(exist_ok=True)
tampilkan "Directory exists or created"
```

#### hapus_dir(ignore_errors=False)

Menghapus directory tree.

**Parameter:**
- `ignore_errors` (boolean): Ignore errors saat penghapusan

**Contoh:**
```python
// Hapus directory dengan semua isinya
p itu Path("temp_directory")
jika p.ada() dan p.adalah_dir():
    p.hapus_dir()
    tampilkan "Directory tree removed"

// Hapus dengan ignore errors
p.hapus_dir(ignore_errors=True)
```

### File Operations

#### hapus_file()

Menghapus file.

**Contoh:**
```python
p itu Path("temp_file.txt")
jika p.ada() dan p.adalah_file():
    p.hapus_file()
    tampilkan "File removed"
```

#### hapus()

Menghapus file atau directory (jika kosong).

**Contoh:**
```python
// Hapus file
file_p itu Path("file.txt")
jika file_p.ada():
    file_p.hapus()

// Hapus empty directory
empty_dir itu Path("empty_dir")
jika empty_dir.ada():
    empty_dir.hapus()
```

#### salin_ke(destination)

Menyalin file ke destination.

**Parameter:**
- `destination` (string/Path): Destination path

**Contoh:**
```python
source itu Path("source.txt")
dest itu Path("backup/backup.txt")

jika source.ada():
    source.salip_ke(dest)
    tampilkan "File copied"

// Copy dengan string destination
source.salip_ke("new_copy.txt")
```

#### pindah_ke(destination)

Memindahkan file ke destination.

**Parameter:**
- `destination` (string/Path): Destination path

**Contoh:**
```python
file_path itu Path("data.txt")
new_location itu Path("archive/data.txt")

jika file_path.ada():
    file_path.pindah_ke(new_location)
    tampilkan "File moved"
```

#### rename_ke(nama_baru)

Mengubah nama file atau directory.

**Parameter:**
- `nama_baru` (string): Nama baru

**Contoh:**
```python
old_file itu Path("old_name.txt")
old_file.rename_ke("new_name.txt")
tampilkan "File renamed"

// Rename directory
dir_path itu Path("old_dir")
dir_path.rename_ke("new_dir")
```

### Path Manipulation

#### gabung(*pathsegments)

Menggabungkan dengan path segments lain.

**Parameter:**
- `*pathsegments`: Path segments untuk digabungkan

**Return:**
- `Path`: Path baru yang digabungkan

**Contoh:**
```python
base itu Path("/home/user")
full_path itu base.gabung("documents", "report.pdf")
tampilkan full_path  // /home/user/documents/report.pdf

// Chain gabung
path itu Path("data")
final_path itu path.gabung("subdir").gabung("file.txt")
tampilkan final_path  // data/subdir/file.txt
```

#### bagi_semua()

Membagi path menjadi semua components.

**Return:**
- `list`: List path components

**Contoh:**
```python
p itu Path("/home/user/documents/report.pdf")
parts itu p.bagi_semua()
tampilkan parts  // ['/', 'home', 'user', 'documents', 'report.pdf']

relative_p itu Path("data/files/output.json")
rel_parts itu relative_p.bagi_semua()
tampilkan rel_parts  // ['data', 'files', 'output.json']
```

#### dapatkan_anchors()

Mendapatkan anchor (drive atau root).

**Return:**
- `string`: Anchor path

**Contoh:**
```python
// Unix-like system
p1 itu Path("/home/user/file.txt")
anchor1 itu p1.dapatkan_anchors()
tampilkan anchor1  // '/'

// Relative path
p2 itu Path("relative/file.txt")
anchor2 itu p2.dapatkan_anchors()
tampilkan anchor2  // ''

// Windows (jika applicable)
p3 itu Path("C:\\Users\\file.txt")
anchor3 itu p3.dapatkan_anchors()
tampilkan anchor3  // 'C:\\'
```

#### dapatkan_drive()

Mendapatkan drive letter (Windows).

**Return:**
- `string`: Drive letter

**Contoh:**
```python
// Windows path
win_path itu Path("C:\\Users\\file.txt")
drive itu win_path.dapatkan_drive()
tampilkan drive  // 'C:'

// Unix path (empty)
unix_path itu Path("/home/user/file.txt")
drive_unix itu unix_path.dapatkan_drive()
tampilkan drive_unix  // ''
```

#### dapatkan_root()

Mendapatkan root (/ atau C:\\).

**Return:**
- `string`: Root path

**Contoh:**
```python
// Unix root
unix_path itu Path("/home/user/file.txt")
root_unix itu unix_path.dapatkan_root()
tampilkan root_unix  // '/'

// Relative path (empty)
rel_path itu Path("relative/file.txt")
root_rel itu rel_path.dapatkan_root()
tampilkan root_rel  // ''
```

#### relatif_ke(other)

Mendapatkan relative path terhadap path lain.

**Parameter:**
- `other` (string/Path): Path lain untuk reference

**Return:**
- `Path`: Relative path

**Contoh:**
```python
base itu Path("/home/user/documents")
target itu Path("/home/user/downloads/file.txt")

relative_path itu target.relatif_ke(base)
tampilkan relative_path  // ../downloads/file.txt

// Relative dalam current directory
current itu Path("/current/dir")
other itu Path("/current/dir/sub/file.txt")
rel_current itu other.relatif_ke(current)
tampilkan rel_current  // sub/file.txt
```

## Fungsi Utility

### path_current()

Mendapatkan current working directory sebagai Path.

**Return:**
- `Path`: Current working directory

**Contoh:**
```python
cwd itu path_current()
tampilkan f"Current directory: {cwd}"

// Gunakan sebagai Path object
files dalam cwd.ada() dan cwd.adalah_dir():
    file_list itu cwd.bagi_semua()
    tampilkan f"Path parts: {file_list}"
```

### path_home()

Mendapatkan home directory sebagai Path.

**Return:**
- `Path`: Home directory

**Contoh:**
```python
home itu path_home()
tampilkan f"Home directory: {home}"

// Buat path di home
config_path itu home.gabung(".config", "myapp")
tampilkan f"Config path: {config_path}"
```

### path_temp()

Mendapatkan temporary directory sebagai Path.

**Return:**
- `Path`: Temporary directory

**Contoh:**
```python
temp_dir itu path_temp()
tampilkan f"Temp directory: {temp_dir}"

// Buat temporary file
temp_file itu temp_dir.gabung("my_temp_file.txt")
tampilkan f"Temp file path: {temp_file}"
```

### gabung_path(*paths)

Menggabungkan path components.

**Parameter:**
- `*paths`: Path components yang akan digabungkan

**Return:**
- `Path`: Combined path

**Contoh:**
```python
// Basic joining
path1 itu gabung_path("home", "user", "documents")
tampilkan path1  // home/user/documents

// Multiple components
path2 itu gabung_path("/var", "log", "app", "debug.log")
tampilkan path2  // /var/log/app/debug.log

// Mixed Path objects dan strings
base itu Path("/data")
result itu gabung_path(base, "processed", "output.csv")
tampilkan result  // /data/processed/output.csv
```

### path_absolute(path)

Mendapatkan absolute path dari string.

**Parameter:**
- `path` (string): Path input

**Return:**
- `string`: Absolute path

**Contoh:**
```python
abs_path itu path_absolute("relative/path/file.txt")
tampilkan f"Absolute: {abs_path}"

abs_current itu path_absolute(".")
tampilkan f"Current absolute: {abs_current}"
```

### path_relatif(path, start)

Mendapatkan relative path.

**Parameter:**
- `path` (string): Target path
- `start` (string): Start path

**Return:**
- `string`: Relative path

**Contoh:**
```python
target itu "/home/user/downloads/file.txt"
start_dir itu "/home/user/documents"

rel itu path_relatif(target, start_dir)
tampilkan f"Relative path: {rel}"
```

### expand_user(path)

Expand user (~) dalam path.

**Parameter:**
- `path` (string): Path dengan ~

**Return:**
- `string`: Expanded path

**Contoh:**
```python
home_path itu expand_user("~/documents")
tampilkan f"Home expanded: {home_path}"

config_path itu expand_user("~/.config/app")
tampilkan f"Config expanded: {config_path}"
```

### expand_vars(path)

Expand environment variables dalam path.

**Parameter:**
- `path` (string): Path dengan variables

**Return:**
- `string`: Expanded path

**Contoh:**
```python
// Set environment variable
setenv("MY_DATA_DIR", "/home/user/data")

path_with_var itu "$MY_DATA_DIR/files"
expanded itu expand_vars(path_with_var)
tampilkan f"Expanded: {expanded}"
```

### path_normal(path)

Normalisasi path (hilangkan .., .).

**Parameter:**
- `path` (string): Path untuk dinormalisasi

**Return:**
- `string`: Normalized path

**Contoh:**
```python
messy_path itu "/home/../home/user/./documents/../downloads"
clean_path itu path_normal(messy_path)
tampilkan f"Clean path: {clean_path}"
```

### split_path(path)

Memisahkan path menjadi directory dan filename.

**Parameter:**
- `path` (string): Path untuk dipisahkan

**Return:**
- `tuple`: (directory, filename)

**Contoh:**
```python
dir, filename itu split_path("/home/user/documents/file.txt")
tampilkan f"Directory: {dir}"      // /home/user/documents
tampilkan f"Filename: {filename}"  // file.txt

dir2, filename2 itu split_path("relative/path/data.csv")
tampilkan f"Dir: {dir2}"           // relative/path
tampilkan f"File: {filename2}"     // data.csv
```

### split_ext(path)

Memisahkan filename dari extension.

**Parameter:**
- `path` (string): Path untuk dipisahkan

**Return:**
- `tuple`: (filename, extension)

**Contoh:**
```python
name, ext itu split_ext("report.pdf")
tampilkan f"Name: {name}"   // report
tampilkan f"Ext: {ext}"     // .pdf

name2, ext2 itu split_ext("archive.tar.gz")
tampilkan f"Name: {name2}"  // archive.tar
tampilkan f"Ext: {ext2}"    // .gz
```

### Fungsi Helper

```python
def get_extension(path):
    """Dapatkan file extension."""
    return str(Path(path).dapatkan_extension())

def get_filename(path):
    """Dapatkan filename dengan extension."""
    return str(Path(path).dapatkan_nama())

def get_basename(path):
    """Dapatkan filename tanpa extension."""
    return str(Path(path).dapatkan_stem())

def get_directory(path):
    """Dapatkan directory dari path."""
    return str(Path(path).dapatkan_parent())
```

## Class Methods

### Path.cwd()

Mendapatkan current working directory.

**Contoh:**
```python
current itu Path.cwd()
tampilkan f"Current: {current}"
```

### Path.home()

Mendapatkan home directory.

**Contoh:**
```python
home itu Path.home()
tampilkan f"Home: {home}"
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.pathlib impor *

tampilkan "=== Demo Pathlib Library ==="

// 1. Basic Path creation
tampilkan "\n1. Basic Path Operations:"
p1 itu Path("/home/user/documents/report.pdf")
tampilkan f"Path: {p1}"
tampilkan f"Name: {p1.dapatkan_nama()}"
tampilkan f"Stem: {p1.dapatkan_stem()}"
tampilkan f"Extension: {p1.dapatkan_extension()}"
tampilkan f"Parent: {p1.dapatkan_parent()}"

// 2. Path manipulation
tampilkan "\n2. Path Manipulation:"
base itu Path("/home/user")
data_path itu base.gabung("data", "files", "output.json")
tampilkan f"Full path: {data_path}"

relative itu Path("project").gabung("src", "main.py")
tampilkan f"Relative: {relative}"
tampilkan f"Absolute: {relative.dapatkan_absolute()}"

// 3. Path parts analysis
tampilkan "\n3. Path Analysis:"
complex_path itu Path("/var/log/app/debug.log")
tampilkan f"All parts: {complex_path.bagi_semua()}"
tampilkan f"Anchor: {complex_path.dapatkan_anchors()}"
tampilkan f"Drive: {complex_path.dapatkan_drive()}"
tampilkan f"Root: {complex_path.dapatkan_root()}"

// 4. File system operations
tampilkan "\n4. File System Operations:"

// Buat directory structure
project_dir itu Path("demo_project")
src_dir itu project_dir.gabung("src")
data_dir itu project_dir.gabung("data")

coba
    // Buat directories
    src_dir.buat_dir(parents=True, exist_ok=True)
    data_dir.buat_dir(parents=True, exist_ok=True)
    tampilkan "Directory structure created"
    
    // Buat files
    main_file itu src_dir.gabung("main.py")
    config_file itu src_dir.gabung("config.json")
    data_file itu data_dir.gabung("data.csv")
    
    // Check existence
    tampilkan f"Project exists: {project_dir.ada()}"
    tampilkan f"Project is dir: {project_dir.adalah_dir()}"
    
    // Path relationships
    tampilkan f"main.py parent: {main_file.dapatkan_parent()}"
    tampilkan f"Relative to project: {main_file.relatif_ke(project_dir)}"
tangkap e
    tampilkan f"Error: {e}"
selesai

// 5. Working with special directories
tampilkan "\n5. Special Directories:"
cwd itu path_current()
home itu path_home()
temp itu path_temp()

tampilkan f"Current: {cwd}"
tampilkan f"Home: {home}"
tampilkan f"Temp: {temp}"

// 6. Path utility functions
tampilkan "\n6. Path Utilities:"

// Expand user dan variables
user_config itu expand_user("~/.config/myapp")
tampilkan f"User config path: {user_config}"

// Set dan expand environment variable
setenv("PROJECT_ROOT", "/home/user/projects")
env_path itu expand_vars("$PROJECT_ROOT/src")
tampilkan f"Env expanded: {env_path}"

// Normalize messy path
messy_path itu "folder/../folder/sub/./file.txt"
clean_path itu path_normal(messy_path)
tampilkan f"Clean path: {clean_path}"

// Split operations
dir_part, file_part itu split_path("/home/user/data/file.txt")
tampilkan f"Dir: {dir_part}, File: {file_part}"

name_part, ext_part itu split_ext("archive.tar.gz")
tampilkan f"Name: {name_part}, Ext: {ext_part}")

// 7. Advanced path operations
tampilkan "\n7. Advanced Operations:"

// Resolve symbolic links dan normalize
test_path itu Path("./data/../config/settings.json")
resolved itu test_path.dapatkan_resolve()
tampilkan f"Original: {test_path}"
tampilkan f"Resolved: {resolved}"

// Path iteration dan filtering
if project_dir.ada() dan project_dir.adalah_dir():
    // Walk through directory (manual implementation)
    all_files itu []
    
    // List immediate contents
    items itu listdir(str(project_dir))
    untuk item dalam items:
        item_path itu project_dir.gabung(item)
        jika item_path.adalah_file():
            all_files.tambah(item_path)
        lainnya jika item_path.adalah_dir():
            tampilkan f"Subdirectory: {item_path}"
    
    tampilkan f"All files: {all_files}"

// 8. Cross-platform considerations
tampilkan "\n8. Cross-Platform Path Handling:"

// Platform-independent path joining
platform_path itu gabung_path("data", "subdir", "file.txt")
tampilkan f"Platform path: {platform_path}"

// Path yang work di semua platforms
config_locations itu [
    expand_user("~/.config/app"),
    gabung_path(path_current(), "config"),
    "/etc/app/config"
]

untuk config_path dalam config_locations:
    jika Path(config_path).ada():
        tampilkan f"Config found at: {config_path}"
    selesai

// 9. Error handling dan best practices
tampilkan "\n9. Error Handling:"

// Safe file operations
safe_path itu Path("safe_operation.txt")
coba
    // Check before operations
    jika safe_path.ada():
        tampilkan f"File size: {safe_path.stat().st_size if hasattr(safe_path, 'stat') else 'Unknown'}"
    
    // Create parent directories if needed
    deep_path itu Path("level1/level2/level3/file.txt")
    parent_dir itu deep_path.dapatkan_parent()
    
    jika tidak parent_dir.ada():
        parent_dir.buat_dir(parents=True)
        tampilkan "Created parent directories"
    
tangkap e
    tampilkan f"Error in safe operations: {e}"
selesai

// 10. Cleanup
tampilkan "\n10. Cleanup:"
coba
    if project_dir.ada():
        project_dir.hapus_dir(ignore_errors=True)
        tampilkan "Demo project cleaned up"
tangkap e
    tampilkan f"Cleanup error: {e}"
selesai

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **File Management**: Organize dan manage files dengan struktur yang jelas
2. **Application Configuration**: Handle config files di user directories
3. **Data Processing**: Batch process files dalam directories
4. **Cross-Platform Apps**: Path handling yang work di Windows/Linux/macOS
5. **Build Systems**: Manage build artifacts dan dependencies
6. **Backup Systems**: Organize backup paths dengan struktur yang konsisten
7. **Web Applications**: Handle static file paths dan uploads
8. **Data Science**: Manage dataset paths dan output directories

## Keunggulan Pathlib vs String Paths

1. **Object-Oriented**: Methods terintegrasi dengan Path objects
2. **Cross-Platform**: Otomatis handle path separators
3. **Type Safety**: Clear distinction antara paths dan strings
4. **Readability**: Code lebih intuitive dengan methods
5. **Composable**: Chain operations dengan mudah
6. **Immutable**: Path objects tidak berubah saat digunakan

## Performance Tips

- Gunakan `Path.cwd()` dan `Path.home()` untuk directories spesial
- Hindari konversi string ke Path berulang kali
- Gunakan `gabung()` untuk path composition
- Cache path objects yang sering digunakan
- Gunakan `dapatkan_resolve()` sekali untuk path final

## Error Handling Best Practices

1. Selalu cek `.ada()` sebelum file operations
2. Gunakan `coba...tangkap...selesai` untuk I/O operations
3. Handle permission errors dengan baik
4. Validasi path inputs untuk security
5. Gunakan `exist_ok=True` untuk idempotent operations

## Security Considerations

- Validasi path inputs untuk mencegah directory traversal
- Gunakan absolute paths untuk critical operations
- Check permissions sebelum file operations
- Be careful dengan symbolic link resolution
- Sanitize user-provided paths

## Indonesian Language Integration

Library ini dirancang dengan Bahasa Indonesia sebagai first-class citizen:
- Method names dalam Bahasa Indonesia yang intuitive
- Consistent naming conventions
- Documentation dalam Bahasa Indonesia
- Examples dengan konteks Indonesia
- Easy untuk Indonesian developers learning programming