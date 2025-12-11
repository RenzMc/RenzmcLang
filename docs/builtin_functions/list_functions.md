# List Functions

This document covers all built-in list functions available in RenzMcLang. These functions are always available without importing any modules and provide comprehensive list manipulation capabilities.

## Core List Functions

### tambah()
Adds an item to the end of a list.

**Syntax:**
```python
tambah(list, item)
```

**Parameters:**
- `list` (list): The list to add to
- `item` (any): The item to add

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Basic addition
daftar1 = [1, 2, 3]
hasil1 = tambah(daftar1, 4)
tampilkan daftar1         // Output: [1, 2, 3, 4]
tampilkan hasil1         // Output: [1, 2, 3, 4]

// Add different types
daftar2 = ["a", "b"]
tambah(daftar2, "c")      // daftar2 becomes ["a", "b", "c"]
tambah(daftar2, 123)      // daftar2 becomes ["a", "b", "c", 123]

// Add list
daftar3 = [1, 2]
tambah(daftar3, [3, 4])   // daftar3 becomes [1, 2, [3, 4]]
```

---

### hapus()
Removes the first occurrence of an item from a list.

**Syntax:**
```python
hapus(list, item)
```

**Parameters:**
- `list` (list): The list to remove from
- `item` (any): The item to remove

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Basic removal
daftar1 = [1, 2, 3, 2, 4]
hasil1 = hapus(daftar1, 2)
tampilkan daftar1         // Output: [1, 3, 2, 4]
tampilkan hasil1         // Output: [1, 3, 2, 4]

// Remove string
daftar2 = ["a", "b", "c"]
hapus(daftar2, "b")       // daftar2 becomes ["a", "c"]

// Remove all occurrences (loop)
daftar3 = [1, 2, 2, 2, 3]
selama 2 di daftar3
    hapus(daftar3, 2)
selesai
tampilkan daftar3         // Output: [1, 3]
```

**Error:**
- Raises `ValueError` if item is not found in the list

---

### hapus_pada()
Removes an item at a specific index from a list.

**Syntax:**
```python
hapus_pada(list, index)
```

**Parameters:**
- `list` (list): The list to remove from
- `index` (integer): Index of the item to remove

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Remove by index
daftar1 = [1, 2, 3, 4, 5]
hasil1 = hapus_pada(daftar1, 2)
tampilkan daftar1         // Output: [1, 2, 4, 5]

// Remove first item
daftar2 = ["a", "b", "c"]
hapus_pada(daftar2, 0)    // daftar2 becomes ["b", "c"]

// Remove last item (negative index)
daftar3 = [1, 2, 3]
hapus_pada(daftar3, -1)   // daftar3 becomes [1, 2]
```

**Error:**
- Raises `IndexError` if index is out of range

---

### masukkan()
Inserts an item at a specific index in a list.

**Syntax:**
```python
masukkan(list, index, item)
```

**Parameters:**
- `list` (list): The list to insert into
- `index` (integer): Position to insert at
- `item` (any): The item to insert

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Insert at position
daftar1 = [1, 3, 4]
hasil1 = masukkan(daftar1, 1, 2)
tampilkan daftar1         // Output: [1, 2, 3, 4]

// Insert at beginning
daftar2 = ["b", "c"]
masukkan(daftar2, 0, "a") // daftar2 becomes ["a", "b", "c"]

// Insert at end
daftar3 = [1, 2]
masukkan(daftar3, 2, 3)   // daftar3 becomes [1, 2, 3]

// Insert with negative index
daftar4 = [1, 3, 4]
masukkan(daftar4, -1, 2)  // daftar4 becomes [1, 3, 2, 4]
```

**Error:**
- Raises `IndexError` if index is invalid

---

### urutkan()
Sorts a list in ascending or descending order.

**Syntax:**
```python
urutkan(list, terbalik)
```

**Parameters:**
- `list` (list): The list to sort
- `terbalik` (boolean, optional): Sort in descending order (default: salah)

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Sort ascending (default)
daftar1 = [3, 1, 4, 1, 5, 9]
hasil1 = urutkan(daftar1)
tampilkan daftar1         // Output: [1, 1, 3, 4, 5, 9]

// Sort descending
daftar2 = [3, 1, 4, 1, 5, 9]
urutkan(daftar2, benar)   // daftar2 becomes [9, 5, 4, 3, 1, 1]

// Sort strings
daftar3 = ["zebra", "apple", "banana"]
urutkan(daftar3)          // daftar3 becomes ["apple", "banana", "zebra"]

// Sort strings descending
daftar4 = ["zebra", "apple", "banana"]
urutkan(daftar4, benar)   // daftar4 becomes ["zebra", "banana", "apple"]
```

**Error:**
- Raises `TypeError` if list contains items that cannot be compared

---

### balikkan()
Reverses the order of items in a list.

**Syntax:**
```python
balikkan(list)
```

**Parameters:**
- `list` (list): The list to reverse

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Reverse list
daftar1 = [1, 2, 3, 4, 5]
hasil1 = balikkan(daftar1)
tampilkan daftar1         // Output: [5, 4, 3, 2, 1]

// Reverse strings
daftar2 = ["a", "b", "c"]
balikkan(daftar2)         // daftar2 becomes ["c", "b", "a"]

// Reverse already sorted
daftar3 = [1, 2, 3]
balikkan(daftar3)         // daftar3 becomes [3, 2, 1]
```

---

### hitung()
Counts the number of occurrences of an item in a list.

**Syntax:**
```python
hitung(list, item)
```

**Parameters:**
- `list` (list): The list to search in
- `item` (any): The item to count

**Returns:**
- Integer: Number of occurrences

**Examples:**
```python
// Count numbers
daftar1 = [1, 2, 3, 2, 4, 2, 5]
hasil1 = hitung(daftar1, 2)
tampilkan hasil1         // Output: 3

// Count strings
daftar2 = ["a", "b", "a", "c", "a"]
count_a = hitung(daftar2, "a")
count_b = hitung(daftar2, "b")
tampilkan count_a        // Output: 3
tampilkan count_b        // Output: 1

// Count non-existent item
daftar3 = [1, 2, 3]
hasil3 = hitung(daftar3, 5)
tampilkan hasil3         // Output: 0
```

---

### indeks()
Returns the index of the first occurrence of an item in a list.

**Syntax:**
```python
indeks(list, item)
```

**Parameters:**
- `list` (list): The list to search in
- `item` (any): The item to find

**Returns:**
- Integer: Index of the first occurrence

**Examples:**
```python
// Find index
daftar1 = [10, 20, 30, 40, 30]
hasil1 = indeks(daftar1, 30)
tampilkan hasil1         // Output: 2

// Find string index
daftar2 = ["a", "b", "c", "d"]
hasil2 = indeks(daftar2, "c")
tampilkan hasil2         // Output: 2

// Find first occurrence
daftar3 = [1, 2, 3, 2, 1]
hasil3 = indeks(daftar3, 2)
tampilkan hasil3         // Output: 1
```

**Error:**
- Raises `ValueError` if item is not found in the list

---

### extend()
Extends a list by appending elements from an iterable.

**Syntax:**
```python
extend(list, iterable)
```

**Parameters:**
- `list` (list): The list to extend
- `iterable`: Iterable of items to add

**Returns:**
- List: The modified list (in-place operation)

**Examples:**
```python
// Extend with list
daftar1 = [1, 2, 3]
hasil1 = extend(daftar1, [4, 5, 6])
tampilkan daftar1         // Output: [1, 2, 3, 4, 5, 6]

// Extend with tuple
daftar2 = ["a", "b"]
extend(daftar2, ("c", "d"))
tampilkan daftar2         // Output: ["a", "b", "c", "d"]

// Extend with string (characters)
daftar3 = [1, 2]
extend(daftar3, "abc")
tampilkan daftar3         // Output: [1, 2, "a", "b", "c"]

// Extend with range
daftar4 = [0]
extend(daftar4, range(1, 4))
tampilkan daftar4         // Output: [0, 1, 2, 3]
```

---

### salin()
Creates a shallow copy of an object.

**Syntax:**
```python
salin(obj)
```

**Parameters:**
- `obj` (any): Object to copy

**Returns:**
- Any: Shallow copy of the object

**Examples:**
```python
// Copy list
original1 = [1, 2, 3]
copy1 = salin(original1)
copy1.tambah(4)
tampilkan original1       // Output: [1, 2, 3]
tampilkan copy1           // Output: [1, 2, 3, 4]

// Copy string
text = "Hello"
copy_text = salin(text)
tampilkan copy_text       // Output: "Hello"

// Copy number
num = 42
copy_num = salin(num)
tampilkan copy_num        // Output: 42
```

---

### salin_dalam()
Creates a deep copy of an object.

**Syntax:**
```python
salin_dalam(obj)
```

**Parameters:**
- `obj` (any): Object to deep copy

**Returns:**
- Any: Deep copy of the object

**Examples:**
```python
// Deep copy nested list
original1 = [[1, 2], [3, 4]]
deep_copy1 = salin_dalam(original1)
deep_copy1[0].tambah(99)
tampilkan original1       // Output: [[1, 2], [3, 4]]
tampilkan deep_copy1      // Output: [[1, 2, 99], [3, 4]]

// Shallow vs Deep copy comparison
original2 = [[1], [2]]
shallow = salin(original2)
deep = salin_dalam(original2)
shallow[0].tambah(99)
deep[1].tambah(88)
tampilkan original2       // Output: [[1, 99], [2, 88]] (shallow affected original)
tampilkan shallow         // Output: [[1, 99], [2, 88]]
tampilkan deep            // Output: [[1], [2, 88]]
```

## Complete Examples

### List Processing Pipeline
```python
// Process a list of numbers
angka = [5, 2, 8, 1, 9, 3, 7, 4, 6]

// Sort ascending
urutkan(angka)
tampilkan "Sorted:", angka

// Find and remove extremes
max_val = angka[-1]
min_val = angka[0]
hapus(angka, max_val)
hapus(angka, min_val)

tampilkan "Without extremes:", angka

// Insert new values
masukkan(angka, 0, 0)
tambah(angka, 10)

tampilkan "Final:", angka
```

### Data Deduplication
```python
// Remove duplicates from list
data = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
unique_data = []

untuk setiap item dari data
    jika item tidak di unique_data
        tambah(unique_data, item)
selesai

tampilkan "Original:", data
tampilkan "Unique:", unique_data
tampilkan "Original length:", hitung(data, 2) + hitung(data, 4)
tampilkan "Unique count:", panjang(unique_data)
```

### List Statistics
```python
// Calculate list statistics
numbers = [1, 5, 3, 9, 2, 8, 4, 7, 6]

// Basic stats
panjang_list = panjang(numbers)
max_val = max(numbers)
min_val = min(numbers)

// Find specific values
index_max = indeks(numbers, max_val)
index_min = indeks(numbers, min_val)

tampilkan "List:", numbers
tampilkan "Length:", panjang_list
tampilkan "Max:", max_val, "at index", index_max
tampilkan "Min:", min_val, "at index", index_min

// Create sorted copy
sorted_copy = salin(numbers)
urutkan(sorted_copy)
tampilkan "Sorted copy:", sorted_copy
```

### Nested List Operations
```python
// Work with nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

// Extract diagonal
diagonal = []
untuk i dari 0 sampai panjang(matrix)
    tambah(diagonal, matrix[i][i])
selesai

tampilkan "Original matrix:", matrix
tampilkan "Diagonal:", diagonal

// Deep copy for modification
matrix_copy = salin_dalam(matrix)
// Swap first and last rows
temp = matrix_copy[0]
matrix_copy[0] = matrix_copy[2]
matrix_copy[2] = temp
tampilkan "Modified copy:", matrix_copy
```

## Usage Notes

1. **In-place Operations**: Most list functions (`tambah`, `hapus`, `masukkan`, `urutkan`, `balikkan`, `extend`) modify the original list in-place and return the modified list.

2. **Type Safety**: Functions validate input types and provide clear error messages in Indonesian.

3. **Index Handling**: Use negative indices for positions from the end of the list.

4. **Copy Operations**: 
   - `salin()` creates a shallow copy (nested objects are shared)
   - `salin_dalam()` creates a deep copy (nested objects are independent)

5. **Error Handling**: Functions raise appropriate exceptions for invalid operations:
   - `TypeError` for wrong input types
   - `ValueError` for items not found
   - `IndexError` for out-of-range indices

6. **Performance**: List operations are optimized for common use cases but consider using appropriate data structures for specific needs.

7. **Comparison**: `urutkan()` requires items to be comparable with each other.