# 🐍 Python Integration - RenzMcLang latest version

**Last Updated:** 2025-10-04  
[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)

---

## 🎯 Overview

RenzMcLang memiliki integrasi penuh dengan Python, memungkinkan Anda menggunakan library Python dan mengakses ekosistem Python yang luas.

---

## 📋 Table of Contents

1. [Importing Python Modules](#importing-python-modules)
2. [Calling Python Functions](#calling-python-functions)
3. [Using Python Libraries](#using-python-libraries)
4. [Data Conversion](#data-conversion)
5. [Common Use Cases](#common-use-cases)
6. [Best Practices](#best-practices)

---

## Importing Python Modules

### 1. Basic Import

```python
// Import Python module
impor_python "math"
impor_python "datetime"
impor_python "json"

// Use imported modules
hasil itu panggil_python math.sqrt(16)
tampilkan hasil  // 4.0
```

### 2. Import with Alias

```python
// Import with alias
impor_python "numpy" sebagai np
impor_python "pandas" sebagai pd

// Use with alias
array itu panggil_python np.array([1, 2, 3, 4])
```

### 3. Import Specific Functions

```python
// Import specific items
dari_python "math" impor sqrt, pi, sin
dari_python "datetime" impor datetime, timedelta

// Use directly
hasil itu panggil_python sqrt(25)
tampilkan hasil  // 5.0
```

---

## Calling Python Functions

### 1. Simple Function Calls

```python
impor_python "math"

// Call Python function
hasil itu panggil_python math.sqrt(16)
tampilkan hasil  // 4.0

// Multiple calls
sin_val itu panggil_python math.sin(0)
cos_val itu panggil_python math.cos(0)
```

### 2. Function with Multiple Arguments

```python
impor_python "math"

// Function with multiple args
hasil itu panggil_python math.pow(2, 3)
tampilkan hasil  // 8.0

// With keyword arguments
hasil itu panggil_python math.log(100, base=10)
tampilkan hasil  // 2.0

// Multiline function calls for better readability
impor_python "builtins"
hasil itu panggil_python builtins.str(
    "hello world"
)
```

### 3. Chaining Calls

```python
impor_python "datetime"

// Chain Python calls
sekarang itu panggil_python datetime.now()
formatted itu panggil_python sekarang.strftime("%Y-%m-%d %H:%M:%S")
tampilkan formatted
```

---

## Using Python Libraries

### 1. Requests Library

```python
// Note: In latest version+, use built-in http_get instead
// But you can still use Python requests if needed

impor_python "requests"

// Make HTTP request
response itu panggil_python requests.get("https://api.github.com")
status itu panggil_python response.status_code
tampilkan f"Status: {status}"

// Get JSON data
data itu panggil_python response.json()
tampilkan data
```

**Better Alternative (latest version+):**
```python
// Use built-in HTTP client (no import needed)
response itu http_get("https://api.github.com")
tampilkan f"Status: {response.status_code}"
data itu response.json()
```

### 2. NumPy

```python
impor_python "numpy" sebagai np

// Create array
arr itu panggil_python np.array([1, 2, 3, 4, 5])
tampilkan arr

// Array operations
mean itu panggil_python np.mean(arr)
std itu panggil_python np.std(arr)
tampilkan f"Mean: {mean}, Std: {std}"

// Matrix operations
matrix itu panggil_python np.array([[1, 2], [3, 4]])
det itu panggil_python np.linalg.det(matrix)
tampilkan f"Determinant: {det}"
```

### 3. Pandas

```python
impor_python "pandas" sebagai pd

// Create DataFrame
data itu {
    "nama": ["Budi", "Ani", "Citra"],
    "umur": [25, 22, 27],
    "kota": ["Jakarta", "Bandung", "Surabaya"]
}

df itu panggil_python pd.DataFrame(data)
tampilkan df

// DataFrame operations
mean_age itu panggil_python df["umur"].mean()
tampilkan f"Rata-rata umur: {mean_age}"

// Filter data
jakarta_df itu panggil_python df[df["kota"] == "Jakarta"]
tampilkan jakarta_df
```

### 4. BeautifulSoup (Web Scraping)

```python
impor_python "requests"
impor_python "bs4" sebagai BeautifulSoup

// Fetch webpage
response itu panggil_python requests.get("https://example.com")
html itu panggil_python response.text

// Parse HTML
soup itu panggil_python BeautifulSoup(html, "html.parser")

// Extract data
title itu panggil_python soup.find("title")
title_text itu panggil_python title.get_text()
tampilkan f"Title: {title_text}"

// Find all links
links itu panggil_python soup.find_all("a")
untuk setiap link dari links
    href itu panggil_python link.get("href")
    tampilkan href
selesai
```

### 5. Matplotlib (Plotting)

```python
impor_python "matplotlib.pyplot" sebagai plt
impor_python "numpy" sebagai np

// Generate data
x itu panggil_python np.linspace(0, 10, 100)
y itu panggil_python np.sin(x)

// Create plot
panggil_python plt.figure(figsize=(10, 6))
panggil_python plt.plot(x, y)
panggil_python plt.title("Sine Wave")
panggil_python plt.xlabel("X")
panggil_python plt.ylabel("Y")
panggil_python plt.grid(True)
panggil_python plt.savefig("sine_wave.png")
tampilkan "Plot saved to sine_wave.png"
```

### 6. SQLite

```python
impor_python "sqlite3"

// Connect to database
conn itu panggil_python sqlite3.connect("database.db")
cursor itu panggil_python conn.cursor()

// Create table
panggil_python cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

// Insert data
panggil_python cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("Budi", "budi@example.com")
)

// Commit and close
panggil_python conn.commit()
panggil_python conn.close()
```

### 7. PIL (Image Processing)

```python
impor_python "PIL" sebagai Image

// Open image
img itu panggil_python Image.open("photo.jpg")

// Get image info
width, height itu panggil_python img.size
tampilkan f"Size: {width}x{height}"

// Resize image
new_size itu (800, 600)
resized itu panggil_python img.resize(new_size)

// Save image
panggil_python resized.save("photo_resized.jpg")
tampilkan "Image resized and saved"
```

---

## Data Conversion

### 1. RenzMcLang to Python

```python
// RenzMcLang data types automatically convert to Python

// List
rmc_list itu [1, 2, 3, 4, 5]
py_array itu panggil_python np.array(rmc_list)

// Dict
rmc_dict itu {"nama": "Budi", "umur": 25}
py_df itu panggil_python pd.DataFrame([rmc_dict])

// String
rmc_str itu "Hello, World!"
py_bytes itu panggil_python rmc_str.encode("utf-8")
```

### 2. Python to RenzMcLang

```python
impor_python "numpy" sebagai np

// Python array to RenzMcLang list
py_array itu panggil_python np.array([1, 2, 3])
rmc_list itu panggil_python py_array.tolist()
tampilkan rmc_list  // [1, 2, 3]

// Python dict to RenzMcLang dict
py_dict itu {"key": "value"}
rmc_dict itu py_dict  // Direct assignment
```

---

## Common Use Cases

### 1. Data Analysis

```python
impor_python "pandas" sebagai pd
impor_python "numpy" sebagai np

// Load data
df itu panggil_python pd.read_csv("data.csv")

// Basic statistics
tampilkan "=== Data Statistics ==="
tampilkan panggil_python df.describe()

// Group by analysis
grouped itu panggil_python df.groupby("category")["value"].mean()
tampilkan "\n=== Average by Category ==="
tampilkan grouped

// Correlation
corr itu panggil_python df.corr()
tampilkan "\n=== Correlation Matrix ==="
tampilkan corr
```

### 2. Machine Learning

```python
impor_python "sklearn.model_selection" sebagai train_test_split
impor_python "sklearn.linear_model" sebagai LinearRegression
impor_python "numpy" sebagai np

// Prepare data
X itu panggil_python np.array([[1], [2], [3], [4], [5]])
y itu panggil_python np.array([2, 4, 6, 8, 10])

// Split data
X_train, X_test, y_train, y_test itu panggil_python train_test_split(
    X, y, test_size=0.2, random_state=42
)

// Train model
model itu panggil_python LinearRegression()
panggil_python model.fit(X_train, y_train)

// Predict
predictions itu panggil_python model.predict(X_test)
tampilkan f"Predictions: {predictions}"

// Score
score itu panggil_python model.score(X_test, y_test)
tampilkan f"R² Score: {score}"
```

### 3. Web Scraping

```python
impor_python "requests"
impor_python "bs4" sebagai BeautifulSoup

fungsi scrape_website(url):
    // Fetch page
    response itu panggil_python requests.get(url)
    html itu panggil_python response.text
    
    // Parse HTML
    soup itu panggil_python BeautifulSoup(html, "html.parser")
    
    // Extract data
    articles itu []
    elements itu panggil_python soup.find_all("article")
    
    untuk setiap elem dari elements
        title itu panggil_python elem.find("h2")
        jika title
            title_text itu panggil_python title.get_text()
            articles.tambah(title_text)
        selesai
    selesai
    
    hasil articles
selesai

// Usage
articles itu scrape_website("https://news.example.com")
untuk setiap article dari articles
    tampilkan article
selesai
```

### 4. File Processing

```python
impor_python "openpyxl"

// Read Excel file
workbook itu panggil_python openpyxl.load_workbook("data.xlsx")
sheet itu panggil_python workbook.active

// Process data
data itu []
untuk setiap row dari panggil_python sheet.iter_rows(min_row=2, values_only=True)
    data.tambah(row)
selesai

// Write to new file
new_wb itu panggil_python openpyxl.Workbook()
new_sheet itu panggil_python new_wb.active

untuk setiap row dari data
    panggil_python new_sheet.append(row)
selesai

panggil_python new_wb.save("output.xlsx")
```

---

## Best Practices

### 1. Error Handling

```python
// ✅ Good - Handle Python errors
coba
    impor_python "some_module"
    hasil itu panggil_python some_module.function()
tangkap ImportError sebagai e
    tampilkan f"Module not found: {e}"
tangkap Exception sebagai e
    tampilkan f"Python error: {e}"
selesai

// ❌ Bad - No error handling
impor_python "some_module"
hasil itu panggil_python some_module.function()
```

### 2. Resource Management

```python
// ✅ Good - Close resources
impor_python "sqlite3"

conn itu panggil_python sqlite3.connect("db.sqlite")
coba
    cursor itu panggil_python conn.cursor()
    // Use cursor
akhirnya
    panggil_python conn.close()
selesai

// ❌ Bad - No cleanup
conn itu panggil_python sqlite3.connect("db.sqlite")
cursor itu panggil_python conn.cursor()
// No close
```

### 3. Use Built-in Functions When Available

```python
// ✅ Good - Use RenzMcLang built-ins (latest version+)
response itu http_get("https://api.example.com")
data itu response.json()

// ❌ Less optimal - Import Python when not needed
impor_python "requests"
response itu panggil_python requests.get("https://api.example.com")
data itu panggil_python response.json()
```

### 4. Type Conversion

```python
// ✅ Good - Explicit conversion
impor_python "numpy" sebagai np

py_array itu panggil_python np.array([1, 2, 3])
rmc_list itu panggil_python py_array.tolist()  // Convert to RenzMcLang list

// ❌ Bad - Assuming compatibility
py_array itu panggil_python np.array([1, 2, 3])
// Using py_array directly might cause issues
```

---

## 💡 Tips & Tricks

### 1. Check Module Availability

```python
fungsi check_module(module_name):
    coba
        impor_python module_name
        hasil benar
    tangkap ImportError
        hasil salah
    selesai
selesai

jika check_module("pandas")
    tampilkan "Pandas is available"
    impor_python "pandas" sebagai pd
kalau_tidak
    tampilkan "Please install pandas: pip install pandas"
selesai
```

### 2. List Python Attributes

```python
impor_python "math"

// Get all attributes
attrs itu dir(math)
tampilkan "Math module functions:"
untuk setiap attr dari attrs
    jika tidak attr.startswith("_")
        tampilkan f"  - {attr}"
    selesai
selesai
```

### 3. Python Help

```python
impor_python "math"

// Get help for Python function
help_text itu panggil_python help(math.sqrt)
tampilkan help_text
```

---

## 📚 See Also

- [Syntax Basics](syntax-basics.md) - Basic syntax
- [Built-in Functions](builtin-functions.md) - Built-in functions
- [Advanced Features](advanced-features.md) - Advanced features
- [Examples](examples.md) - Code examples

---

## 🔗 Useful Python Libraries

### Data Science
- **NumPy** - Numerical computing
- **Pandas** - Data analysis
- **Matplotlib** - Plotting
- **Seaborn** - Statistical visualization
- **SciPy** - Scientific computing

### Web Development
- **Flask** - Web framework
- **Django** - Full-stack framework
- **FastAPI** - Modern API framework
- **Requests** - HTTP library (use built-in http_get in latest version+)
- **BeautifulSoup** - Web scraping

### Machine Learning
- **scikit-learn** - Machine learning
- **TensorFlow** - Deep learning
- **PyTorch** - Deep learning
- **Keras** - Neural networks

### Utilities
- **Pillow** - Image processing
- **openpyxl** - Excel files
- **python-docx** - Word documents
- **PyPDF2** - PDF processing

---

**Version: Latest**  
**Last Updated: 2025-10-04**

**Note:** In latest version+, many common operations (like HTTP requests) have built-in functions. Use Python integration for specialized libraries and advanced use cases.