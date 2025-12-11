# Iteration Functions

This document covers all built-in iteration functions available in RenzMcLang. These functions are always available without importing any modules and provide powerful iteration and collection processing capabilities.

## Core Iteration Functions

### zip() / zip_func()
Combines multiple iterables into tuples of corresponding elements.

**Syntax:**
```python
zip(iterable1, iterable2, ...)
zip_func(iterable1, iterable2, ...)
```

**Parameters:**
- `iterable1, iterable2, ...`: Iterables to combine

**Returns:**
- List: List of tuples containing elements from each iterable

**Examples:**
```python
// Basic zip with two iterables
nama = ["Alice", "Bob", "Charlie"]
umur = [25, 30, 35]
hasil1 = zip(nama, umur)
tampilkan hasil1         // Output: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

// Zip with three iterables
buah = ["apple", "banana", "cherry"]
warna = ["red", "yellow", "red"]
harga = [1.0, 0.5, 2.0]
hasil2 = zip_func(buah, warna, harga)
tampilkan hasil2         // Output: [("apple", "red", 1.0), ("banana", "yellow", 0.5), ("cherry", "red", 2.0)]

// Zip with different lengths (stops at shortest)
pendek = [1, 2]
panjang = ["a", "b", "c", "d"]
hasil3 = zip(pendek, panjang)
tampilkan hasil3         // Output: [(1, "a"), (2, "b")]

// Zip with single iterable
hasil4 = zip([1, 2, 3])
tampilkan hasil4         // Output: [(1,), (2,), (3,)]
```

---

### enumerate() / enumerate_func()
Adds index to each element of an iterable.

**Syntax:**
```python
enumerate(iterable, start)
enumerate_func(iterable, start)
```

**Parameters:**
- `iterable`: Iterable to enumerate
- `start` (integer, optional): Starting index (default: 0)

**Returns:**
- List: List of (index, element) tuples

**Examples:**
```python
// Basic enumeration
buah = ["apple", "banana", "cherry"]
hasil1 = enumerate(buah)
tampilkan hasil1         // Output: [(0, "apple"), (1, "banana"), (2, "cherry")]

// Custom start index
hasil2 = enumerate_func(buah, 1)
tampilkan hasil2         // Output: [(1, "apple"), (2, "banana"), (3, "cherry")]

// Enumerate string
text = "hello"
hasil3 = enumerate(text)
tampilkan hasil3         // Output: [(0, "h"), (1, "e"), (2, "l"), (3, "l"), (4, "o")]

// Negative start index
hasil4 = enumerate([10, 20, 30], -1)
tampilkan hasil4         // Output: [(-1, 10), (0, 20), (1, 30)]
```

---

### filter() / filter_func() / saring()
Filters elements from an iterable based on a function.

**Syntax:**
```python
filter(function, iterable)
filter_func(function, iterable)
saring(function, iterable)
```

**Parameters:**
- `function`: Function that returns boolean for each element
- `iterable`: Iterable to filter

**Returns:**
- List: List of elements where function returns benar

**Examples:**
```python
// Filter with lambda function
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
genap = filter(lambda x -> x % 2 == 0, angka)
tampilkan genap          // Output: [2, 4, 6, 8, 10]

// Filter with named function
fungsi is_positive(x):
    hasil x > 0
selesai

negatif = [-5, -2, 0, 3, 7, -1]
positif = filter_func(is_positive, negatif)
tampilkan positif        // Output: [3, 7]

// Indonesian alias
besar_dari_5 = saring(lambda x -> x > 5, [1, 10, 3, 8, 2])
tampilkan besar_dari_5   // Output: [10, 8]

// Filter strings
kata = ["apple", "banana", "kiwi", "grape"]
pendek = filter(lambda x -> panjang(x) <= 5, kata)
tampilkan pendek         // Output: ["apple", "kiwi"]

// Filter with None (remove falsy values)
data = [0, 1, "", "hello", [], [1], salah, benar]
truthy = filter(None, data)
tampilkan truthy         // Output: [1, "hello", [1], benar]
```

---

### map() / map_func() / peta()
Applies a function to each element of an iterable.

**Syntax:**
```python
map(function, iterable)
map_func(function, iterable)
peta(function, iterable)
```

**Parameters:**
- `function`: Function to apply to each element
- `iterable`: Iterable to process

**Returns:**
- List: List of results after applying function

**Examples:**
```python
// Map with lambda function
angka = [1, 2, 3, 4, 5]
kuadrat = map(lambda x -> x * x, angka)
tampilkan kuadrat       // Output: [1, 4, 9, 16, 25]

// Map with named function
fungsi double(x):
    hasil x * 2
selesai

nilai = [10, 20, 30]
ganda = map_func(double, nilai)
tampilkan ganda         // Output: [20, 40, 60]

// Indonesian alias
pangkat_tiga = peta(lambda x -> x ** 3, [1, 2, 3])
tampilkan pangkat_tiga   // Output: [1, 8, 27]

// Map strings to uppercase
kata = ["hello", "world", "python"]
besar = map(huruf_besar, kata)
tampilkan besar         // Output: ["HELLO", "WORLD", "PYTHON"]

// Map multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
jumlah = map(lambda x, y, z -> x + y + z, a, b, c)
tampilkan jumlah         // Output: [111, 222, 333]

// Map with type conversion
string_nums = ["1", "2", "3", "4"]
numbers = map(bilangan_bulat, string_nums)
tampilkan numbers        // Output: [1, 2, 3, 4]
```

---

### reduce() / reduce_func() / kurangi()
Applies a function cumulatively to items of an iterable.

**Syntax:**
```python
reduce(function, iterable, initial)
reduce_func(function, iterable, initial)
kurangi(function, iterable, initial)
```

**Parameters:**
- `function`: Function that takes two arguments and returns one value
- `iterable`: Iterable to reduce
- `initial` (optional): Initial value for the accumulator

**Returns:**
- Any: Single value result of reduction

**Examples:**
```python
// Sum all numbers
angka = [1, 2, 3, 4, 5]
jumlah = reduce(lambda x, y -> x + y, angka)
tampilkan jumlah        // Output: 15

// Product of all numbers
faktorial = reduce(lambda x, y -> x * y, [1, 2, 3, 4, 5])
tampilkan faktorial     // Output: 120

// With initial value
angka = [10, 20, 30]
dengan_awal = reduce(lambda x, y -> x + y, angka, 100)
tampilkan dengan_awal   // Output: 160

// Indonesian alias
max_reduce = kurangi(lambda x, y -> x jika x > y lainnya y, [5, 3, 8, 2, 9])
tampilkan max_reduce    // Output: 9

// Find minimum string (lexicographically)
kata = ["zebra", "apple", "banana"]
min_str = reduce(lambda x, y -> x jika x < y lainnya y, kata)
tampilkan min_str       // Output: "apple"

// Custom reduction - build string
chars = ["h", "e", "l", "l", "o"]
text = reduce(lambda x, y -> x + y, chars, "Result: ")
tampilkan text           // Output: "Result: hello"
```

---

### all() / all_func() / semua()
Returns benar if all elements of an iterable are truthy.

**Syntax:**
```python
all(iterable)
all_func(iterable)
semua(iterable)
```

**Parameters:**
- `iterable`: Iterable to check

**Returns:**
- Boolean: benar if all elements are truthy, salah otherwise

**Examples:**
```python
// All positive numbers
positif = [1, 2, 3, 4, 5]
hasil1 = all(positif)
tampilkan hasil1         // Output: benar

// Contains zero (falsy)
ada_nol = [1, 2, 0, 4, 5]
hasil2 = all_func(ada_nol)
tampilkan hasil2         // Output: salah

// Indonesian alias
all_benar = semua([benar, benar, benar])
tampilkan all_benar       // Output: benar

// With empty iterable
kosong = []
hasil3 = all(kosong)
tampilkan hasil3         // Output: benar (vacuously true)

// Check if all strings are non-empty
kata = ["hello", "world", "python"]
hasil4 = all(lambda x -> panjang(x) > 0, kata)
tampilkan hasil4         // Output: benar

// Check if all numbers are even
angka = [2, 4, 6, 8, 10]
hasil5 = semua(lambda x -> x % 2 == 0, angka)
tampilkan hasil5         // Output: benar
```

---

### any() / any_func() / ada()
Returns benar if any element of an iterable is truthy.

**Syntax:**
```python
any(iterable)
any_func(iterable)
ada(iterable)
```

**Parameters:**
- `iterable`: Iterable to check

**Returns:**
- Boolean: benar if any element is truthy, salah otherwise

**Examples:**
```python
// Any positive numbers
campuran = [-5, -2, 0, 3, -1]
hasil1 = any(campuran)
tampilkan hasil1         // Output: benar

// All negative numbers
semua_negatif = [-5, -2, -1, -8]
hasil2 = any_func(semua_negatif)
tampilkan hasil2         // Output: salah

// Indonesian alias
ada_benar = ada([salah, salah, benar, salah])
tampilkan ada_benar       // Output: benar

// With empty iterable
kosong = []
hasil3 = any(kosong)
tampilkan hasil3         // Output: salah

// Check if any string contains "a"
kata = ["hello", "world", "python"]
hasil4 = any(lambda x -> "a" di x, kata)
tampilkan hasil4         // Output: salah

// Check if any number is greater than 5
angka = [1, 2, 3, 4, 5]
hasil5 = ada(lambda x -> x > 5, angka)
tampilkan hasil5         // Output: salah

// Check for any vowels in string
text = "bcdfg"
hasil6 = any(lambda x -> x di "aeiou", text)
tampilkan hasil6         // Output: salah
```

---

### sorted() / sorted_func() / terurut()
Returns a sorted list from the items in an iterable.

**Syntax:**
```python
sorted(iterable, key, reverse)
sorted_func(iterable, key, reverse)
terurut(iterable, key, reverse)
```

**Parameters:**
- `iterable`: Iterable to sort
- `key` (function, optional): Function to extract comparison key from each element
- `reverse` (boolean, optional): Sort in descending order (default: salah)

**Returns:**
- List: New sorted list

**Examples:**
```python
// Basic sorting
angka = [3, 1, 4, 1, 5, 9, 2, 6]
hasil1 = sorted(angka)
tampilkan hasil1         // Output: [1, 1, 2, 3, 4, 5, 6, 9]

// Descending order
hasil2 = sorted_func(angka, reverse=benar)
tampilkan hasil2         // Output: [9, 6, 5, 4, 3, 2, 1, 1]

// Indonesian alias
terbalik = terurut(angka, reverse=benar)
tampilkan terbalik       // Output: [9, 6, 5, 4, 3, 2, 1, 1]

// Sort by key function (length of strings)
kata = ["apple", "banana", "kiwi", "grape"]
by_length = sorted(kata, key=panjang)
tampilkan by_length      // Output: ["kiwi", "apple", "grape", "banana"]

// Sort complex objects
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]
by_age = sorted(people, key=lambda x -> x["age"])
tampilkan by_age

// Sort by multiple criteria
data = [(1, "b"), (2, "a"), (1, "a"), (2, "c")]
sorted_data = sorted(data, key=lambda x -> (x[0], x[1]))
tampilkan sorted_data    // Output: [(1, "a"), (1, "b"), (2, "a"), (2, "c")]

// Sort strings (lexicographical)
kata = ["zebra", "apple", "banana"]
sorted_strings = sorted(kata)
tampilkan sorted_strings // Output: ["apple", "banana", "zebra"]
```

---

### range() / range_func() / rentang()
Creates a list of numbers within a specified range.

**Syntax:**
```python
range(stop)
range(start, stop)
range(start, stop, step)
range_func(stop)
range_func(start, stop)
range_func(start, stop, step)
rentang(stop)
rentang(start, stop)
rentang(start, stop, step)
```

**Parameters:**
- `start` (integer, optional): Start of range (default: 0)
- `stop` (integer): End of range (exclusive)
- `step` (integer, optional): Step between numbers (default: 1)

**Returns:**
- List: List of numbers in the specified range

**Examples:**
```python
// Basic range (0 to n)
hasil1 = range(5)
tampilkan hasil1         // Output: [0, 1, 2, 3, 4]

// Range with start and stop
hasil2 = range(1, 6)
tampilkan hasil2         // Output: [1, 2, 3, 4, 5]

// Range with step
hasil3 = range(0, 10, 2)
tampilkan hasil3         // Output: [0, 2, 4, 6, 8]

// Indonesian alias
hasil4 = rentang(3)
tampilkan hasil4         // Output: [0, 1, 2]

// Negative step (countdown)
hasil5 = range(5, 0, -1)
tampilkan hasil5         // Output: [5, 4, 3, 2, 1]

// Range with negative numbers
hasil6 = range(-3, 4)
tampilkan hasil6         // Output: [-3, -2, -1, 0, 1, 2, 3]

// Complex range
hasil7 = range_func(1, 20, 3)
tampilkan hasil7         // Output: [1, 4, 7, 10, 13, 16, 19]

// Empty range
hasil8 = range(5, 5)
tampilkan hasil8         // Output: []
```

---

### reversed() / reversed_renzmc() / terbalik()
Returns a list with elements in reverse order.

**Syntax:**
```python
reversed(sequence)
reversed_renzmc(sequence)
terbalik(sequence)
```

**Parameters:**
- `sequence`: Sequence to reverse (list, tuple, string, etc.)

**Returns:**
- List: List with elements in reverse order

**Examples:**
```python
// Reverse list
angka = [1, 2, 3, 4, 5]
hasil1 = reversed(angka)
tampilkan hasil1         // Output: [5, 4, 3, 2, 1]

// Reverse string
text = "hello"
hasil2 = reversed_renzmc(text)
tampilkan hasil2         // Output: ["o", "l", "l", "e", "h"]

// Indonesian alias
kata = ["apple", "banana", "cherry"]
hasil3 = terbalik(kata)
tampilkan hasil3         // Output: ["cherry", "banana", "apple"]

// Reverse tuple
tup = (1, 2, 3)
hasil4 = reversed(tup)
tampilkan hasil4         // Output: [3, 2, 1]

// Reverse range
hasil5 = reversed(range(5))
tampilkan hasil5         // Output: [4, 3, 2, 1, 0]

// Single element
single = [42]
hasil6 = reversed(single)
tampilkan hasil6         // Output: [42]
```

## Complete Examples

### Data Processing Pipeline
```python
// Process a list of student scores
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95},
    {"name": "Eve", "score": 67}
]

// Filter high scores (>= 80)
high_scorers = filter(lambda s -> s["score"] >= 80, students)

// Extract names
names = map(lambda s -> s["name"], high_scorers)

// Sort names alphabetically
sorted_names = sorted(names)

tampilkan "High scoring students:", sorted_names
```

### Number Analysis
```python
// Generate and analyze numbers
numbers = range(1, 11)

// Get squares
squares = map(lambda x -> x * x, numbers)

// Get even squares
even_squares = filter(lambda x -> x % 2 == 0, squares)

// Sum of even squares
sum_even = reduce(lambda x, y -> x + y, even_squares)

// Check conditions
all_positive = all(lambda x -> x > 0, squares)
any_over_50 = any(lambda x -> x > 50, squares)

tampilkan "Numbers:", numbers
tampilkan "Squares:", squares
tampilkan "Even squares:", even_squares
tampilkan "Sum of even squares:", sum_even
tampilkan "All positive?", all_positive
tampilkan "Any over 50?", any_over_50
```

### Text Processing
```python
// Process a list of words
words = ["python", "programming", "language", "code", "developer"]

// Enumerate with indices
indexed_words = enumerate(words, 1)

// Filter long words (> 6 characters)
long_words = filter(lambda x -> panjang(x[1]) > 6, indexed_words)

// Extract just the words (not indices)
just_long_words = map(lambda x -> x[1], long_words)

// Sort by length
sorted_by_length = sorted(just_long_words, key=panjang)

tampilkan "Original words:", words
tampilkan "Long words:", sorted_by_length
```

### Complex Data Transformation
```python
// Transform sales data
sales = [
    {"product": "A", "quantity": 5, "price": 10},
    {"product": "B", "quantity": 3, "price": 20},
    {"product": "C", "quantity": 8, "price": 5},
    {"product": "D", "quantity": 2, "price": 50}
]

// Calculate total for each item
with_total = map(lambda s -> {**s, "total": s["quantity"] * s["price"]}, sales)

// Filter items with total > 50
expensive_items = filter(lambda s -> s["total"] > 50, with_total)

// Sort by total descending
sorted_expensive = sorted(expensive_items, key=lambda x -> x["total"], reverse=benar)

// Calculate grand total
grand_total = reduce(lambda x, y -> x + y["total"], sorted_expensive, 0)

tampilkan "Expensive items (sorted):", sorted_expensive
tampilkan "Grand total:", grand_total
```

## Usage Notes

1. **Function Aliases**: Many functions have Indonesian aliases:
   - `saring()` for `filter()`
   - `peta()` for `map()`
   - `kurangi()` for `reduce()`
   - `semua()` for `all()`
   - `ada()` for `any()`
   - `terurut()` for `sorted()`
   - `rentang()` for `range()`
   - `terbalik()` for `reversed()`

2. **Memory Usage**: Functions like `map()`, `filter()`, and `zip()` return actual lists, not iterators, so they consume memory immediately.

3. **Function Parameters**: Higher-order functions (map, filter, reduce, etc.) accept both lambda functions and named functions.

4. **Type Safety**: Functions validate inputs and provide appropriate error messages.

5. **Performance**: These functions are optimized for common iteration patterns and are generally more efficient than manual loops for the same operations.

6. **Chaining**: Functions can be chained together for complex data transformations:
   ```python
   result = sorted(map(lambda x -> x * 2, filter(lambda x -> x > 5, range(1, 11))))
   ```

7. **Reduce Initial Value**: The `reduce()` function works best with an explicit initial value to avoid errors with empty iterables.