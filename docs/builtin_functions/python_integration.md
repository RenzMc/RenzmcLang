# Python Integration Functions

This document covers all built-in Python integration functions available in RenzMcLang. These functions enable seamless interoperability with Python's ecosystem, allowing you to import Python modules, execute Python code, and work with Python objects directly.

## Core Integration Functions

### evaluasi_python()
Evaluates a Python expression and returns the result.

**Syntax:**
```python
evaluasi_python(expression)
```

**Parameters:**
- `expression` (string): Valid Python expression to evaluate

**Returns:**
- Any: Result of the evaluated expression

**Examples:**
```python
// Basic mathematical expressions
result1 = evaluasi_python("2 + 3 * 4")
tampilkan result1            // Output: 14

// Python string operations
result2 = evaluasi_python("'hello'.upper()")
tampilkan result2            // Output: "HELLO"

// Python list operations
result3 = evaluasi_python("[1, 2, 3, 4, 5][-3:]")
tampilkan result3            // Output: [3, 4, 5]

// Python dictionary operations
result4 = evaluasi_python("{'a': 1, 'b': 2}.get('a')")
tampilkan result4            // Output: 1

// Python function calls
result5 = evaluasi_python("sum([1, 2, 3, 4, 5])")
tampilkan result5            // Output: 15

// Python built-in functions
result6 = evaluasi_python("len('RenzMcLang')")
tampilkan result6            // Output: 10
```

**Error:**
- Raises `Exception` if Python expression is invalid

---

### eksekusi_python()
Executes Python code statements.

**Syntax:**
```python
eksekusi_python(code)
```

**Parameters:**
- `code` (string): Valid Python code to execute

**Returns:**
- Boolean: True if execution successful

**Examples:**
```python
// Define and use Python variables
eksekusi_python("x = 10")
eksekusi_python("y = 20")
result = evaluasi_python("x + y")
tampilkan result            // Output: 30

// Define Python functions
eksekusi_python("""
def python_multiply(a, b):
    return a * b
""")
result = evaluasi_python("python_multiply(6, 7)")
tampilkan result            // Output: 42

// Import and use Python modules
eksekusi_python("import math")
result = evaluasi_python("math.pi")
tampilkan result            // Output: 3.141592653589793

// Create Python classes
eksekusi_python("""
class PythonCounter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
""")
eksekusi_python("counter = PythonCounter()")
eksekusi_python("counter.increment()")
result = evaluasi_python("counter.count")
tampilkan result            // Output: 1
```

**Error:**
- Raises `Exception` if Python code is invalid

---

## Module Management Functions

### cek_modul_python()
Checks if a Python module is available for import.

**Syntax:**
```python
cek_modul_python(module_name)
```

**Parameters:**
- `module_name` (string): Name of Python module to check

**Returns:**
- Boolean: True if module is available, False otherwise

**Examples:**
```python
// Check standard library modules
has_math = cek_modul_python("math")
tampilkan has_math           // Output: benar

has_json = cek_modul_python("json")
tampilkan has_json           // Output: benar

has_os = cek_modul_python("os")
tampilkan has_os             // Output: benar

// Check popular third-party modules
has_numpy = cek_modul_python("numpy")
tampilkan f"NumPy available: {has_numpy}"

has_pandas = cek_modul_python("pandas")
tampilkan f"Pandas available: {has_pandas}"

has_requests = cek_modul_python("requests")
tampilkan f"Requests available: {has_requests}"

// Check non-existent module
has_fake = cek_modul_python("fake_module_12345")
tampilkan has_fake           // Output: salah
```

---

### path_modul_python()
Gets the file path of a Python module.

**Syntax:**
```python
path_modul_python(module_name)
```

**Parameters:**
- `module_name` (string): Name of Python module

**Returns:**
- String or None: File path of the module, or None if built-in

**Examples:**
```python
// Get path of standard library modules
math_path = path_modul_python("math")
tampilkan math_path          // Output: "/usr/lib/python3.11/math.py" (example)

json_path = path_modul_python("json")
tampilkan json_path          // Output: "/usr/lib/python3.11/json/__init__.py" (example)

// Built-in modules might return None
sys_path = path_modul_python("sys")
tampilkan sys_path           // Output: None

// Third-party module paths
numpy_path = path_modul_python("numpy")
tampilkan numpy_path         // Path to NumPy installation
```

**Error:**
- Raises `ImportError` if module is not found

---

### versi_modul_python()
Gets the version of a Python module.

**Syntax:**
```python
versi_modul_python(module_name)
```

**Parameters:**
- `module_name` (string): Name of Python module

**Returns:**
- String or None: Version string, or None if no version available

**Examples:**
```python
// Get versions of installed modules
math_version = versi_modul_python("math")
tampilkan math_version       // Output: None (standard library modules may not have version)

// Third-party module versions
numpy_version = versi_modul_python("numpy")
tampilkan f"NumPy version: {numpy_version}"

pandas_version = versi_modul_python("pandas")
tampilkan f"Pandas version: {pandas_version}"

requests_version = versi_modul_python("requests")
tampilkan f"Requests version: {requests_version}"

// Custom module with __version__
eksekusi_python("__version__ = '1.0.0'")
current_version = evaluasi_python("__version__")
tampilkan current_version    // Output: "1.0.0"
```

**Error:**
- Raises `ImportError` if module is not found

---

## Function Inspection Functions

### get_function_signature()
Gets the signature of a Python function.

**Syntax:**
```python
get_function_signature(func)
```

**Parameters:**
- `func` (function): Python function to inspect

**Returns:**
- String: Function signature

**Examples:**
```python
// Get signature of built-in functions
eksekusi_python("""
def example_func(a, b=10, *args, **kwargs):
    pass
""")
sig = get_function_signature(evaluasi_python("example_func"))
tampilkan sig               // Output: "(a, b=10, *args, **kwargs)"

// RenzMcLang function signatures
sig2 = get_function_signature(tambah)
tampilkan sig2              // Output: "(lst, item)"
```

---

### get_function_parameters()
Gets parameter names of a Python function.

**Syntax:**
```python
get_function_parameters(func)
```

**Parameters:**
- `func` (function): Python function to inspect

**Returns:**
- List: List of parameter names

**Examples:**
```python
eksekusi_python("""
def complex_func(a, b, c=10, *args, d=20, **kwargs):
    pass
""")
params = get_function_parameters(evaluasi_python("complex_func"))
tampilkan params            // Output: ["a", "b", "c", "args", "d", "kwargs"]
```

---

### get_function_name()
Gets the name of a Python function.

**Syntax:**
```python
get_function_name(func)
```

**Parameters:**
- `func` (function): Python function to inspect

**Returns:**
- String or None: Function name

**Examples:**
```python
eksekusi_python("def test_function(): pass")
name = get_function_name(evaluasi_python("test_function"))
tampilkan name              // Output: "test_function"
```

---

## Async Functions

### is_async_function()
Checks if a function is asynchronous.

**Syntax:**
```python
is_async_function(func)
```

**Parameters:**
- `func` (function): Function to check

**Returns:**
- Boolean: True if function is async

**Examples:**
```python
eksekusi_python("""
import asyncio

async def async_func():
    return "async result"

def sync_func():
    return "sync result"
""")
is_async1 = is_async_function(evaluasi_python("async_func"))
is_async2 = is_async_function(evaluasi_python("sync_func"))

tampilkan is_async1         // Output: benar
tampilkan is_async2         // Output: salah
```

---

### run_async()
Runs an async coroutine to completion.

**Syntax:**
```python
run_async(coroutine)
```

**Parameters:**
- `coroutine`: Async coroutine to run

**Returns:**
- Any: Result of the coroutine

**Examples:**
```python
eksekusi_python("""
import asyncio

async def calculate_async(a, b):
    await asyncio.sleep(0.1)
    return a + b
""")
result = run_async(evaluasi_python("calculate_async(5, 3)"))
tampilkan result            // Output: 8
```

---

## Advanced Usage Examples

### Python Library Integration

```python
// Use Python pandas for data analysis
jika cek_modul_python("pandas")
    eksekusi_python("import pandas as pd")
    
    // Create DataFrame
    eksekusi_python("""
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
""")
    
    // Get statistics
    avg_age = evaluasi_python("df['Age'].mean()")
    tampilkan f"Average age: {avg_age}"
    
    // Filter data
    filtered = evaluasi_python("df[df['Age'] > 28]")
    tampilkan filtered
lainnya
    tampilkan "Pandas not available"
selesai
```

### Dynamic Code Execution

```python
// Safe code execution with validation
fungsi safe_python_execute(code):
    // Basic validation
    dangerous_words = ["import", "exec", "eval", "open", "file"]
    
    untuk setiap word dari dangerous_words
        jika word di code
            tampilkan f"Potentially dangerous code detected: {word}"
            hasil None
        selesai
    selesai
    
    coba
        result = evaluasi_python(code)
        hasil result
    except Exception sebagai e
        tampilkan f"Execution error: {e}"
        hasil None
    selesai
selesai

// Usage
result1 = safe_python_execute("2 ** 10")
tampilkan result1           // Output: 1024

result2 = safe_python_execute("import os")  // Blocked
tampilkan result2           // Output: None
```

### Module Discovery

```python
// Discover available Python modules
fungsi scan_python_modules():
    modules_to_check = [
        "math", "json", "os", "sys", "datetime", "random",
        "numpy", "pandas", "requests", "flask", "django",
        "scipy", "matplotlib", "seaborn", "sqlalchemy"
    ]
    
    available_modules = []
    unavailable_modules = []
    
    untuk setiap module dari modules_to_check
        jika cek_modul_python(module)
            version = versi_modul_python(module)
            info = {"name": module, "version": version}
            tambah(available_modules, info)
        lainnya
            tambah(unavailable_modules, module)
        selesai
    selesai
    
    tampilkan "=== Available Modules ==="
    untuk setiap info dari available_modules
        tampilkan f"{info['name']}: {info['version']}"
    selesai
    
    tampilkan "=== Unavailable Modules ==="
    untuk setiap module dari unavailable_modules
        tampilkan module
    selesai
selesai

// Run module scan
scan_python_modules()
```

### Cross-Language Function Calls

```python
// Create hybrid functions using Python and RenzMcLang
eksekusi_python("import math")

fungsi hybrid_statistics(data_list):
    // Use Python's statistics module if available
    jika cek_modul_python("statistics")
        eksekusi_python("import statistics")
        
        // Convert RenzMcLang list to Python
        eksekusi_python(f"data = {data_list}")
        
        mean_val = evaluasi_python("statistics.mean(data)")
        median_val = evaluasi_python("statistics.median(data)")
        stdev_val = evaluasi_python("statistics.stdev(data) if len(data) > 1 else 0")
        
        hasil {
            "mean": mean_val,
            "median": median_val,
            "stdev": stdev_val,
            "count": panjang(data_list)
        }
    lainnya
        // Fallback to manual calculations
        total = 0
        untuk setiap value dari data_list
            total = total + value
        selesai
        mean_val = total / panjang(data_list)
        
        hasil {
            "mean": mean_val,
            "median": "N/A",
            "stdev": "N/A",
            "count": panjang(data_list)
        }
    selesai
selesai

// Usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = hybrid_statistics(data)
tampilkan stats
```

## Performance Considerations

1. **Import Overhead**: Python imports can be expensive, cache imports when possible
2. **Data Conversion**: Converting between RenzMcLang and Python types has overhead
3. **Execution Speed**: Python code execution is generally fast, but consider bottlenecks
4. **Memory Usage**: Be careful with large Python objects

## Security Considerations

1. **Code Injection**: Never execute untrusted Python code
2. **Module Access**: Control which Python modules can be imported
3. **File System**: Python code can access the file system, use sandboxing
4. **Network Access**: Python can make network requests, monitor and restrict

## Best Practices

1. **Error Handling**: Always wrap Python execution in try-catch blocks
2. **Module Validation**: Check module availability before importing
3. **Type Safety**: Understand type conversion between languages
4. **Resource Management**: Clean up Python resources properly