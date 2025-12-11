# Type Functions

This document covers all built-in type functions available in RenzMcLang. These functions are always available without importing any modules and provide type conversion, type checking, and basic type operations.

## Type Conversion Functions

### str() / teks()
Converts any object to a string.

**Syntax:**
```python
str(obj)
teks(obj)
```

**Parameters:**
- `obj` (any): Object to convert to string

**Returns:**
- String: String representation of the object

**Examples:**
```python
// Basic conversions
hasil1 itu str(123)              // Output: "123"
hasil2 itu teks(45.67)           // Output: "45.67"
hasil3 itu str(benar)            // Output: "True"
hasil4 itu teks(salah)           // Output: "False"

// Complex objects
hasil5 itu str([1, 2, 3])        // Output: "[1, 2, 3]"
hasil6 itu teks({"a": 1})        // Output: "{'a': 1}"
```

---

### int() / bilangan_bulat()
Converts an object to an integer.

**Syntax:**
```python
int(obj, base)
bilangan_bulat(obj, base)
```

**Parameters:**
- `obj` (any): Object to convert to integer
- `base` (integer, optional): Number base for string conversion (default: 10)

**Returns:**
- Integer: Integer representation of the object

**Examples:**
```python
// From numbers
hasil1 itu int(123.45)           // Output: 123
hasil2 itu bilangan_bulat(-67.8) // Output: -67

// From strings
hasil3 itu int("123")            // Output: 123
hasil4 itu int("-456")           // Output: -456

// From different bases
hasil5 itu int("101", 2)         // Output: 5 (binary)
hasil6 itu int("FF", 16)         // Output: 255 (hexadecimal)
hasil7 itu int("10", 8)          // Output: 8 (octal)

// From boolean
hasil8 itu int(benar)            // Output: 1
hasil9 itu int(salah)            // Output: 0
```

---

### float() / bilangan_desimal()
Converts an object to a floating-point number.

**Syntax:**
```python
float(obj)
bilangan_desimal(obj)
```

**Parameters:**
- `obj` (any): Object to convert to float

**Returns:**
- Float: Float representation of the object

**Examples:**
```python
// From integers
hasil1 itu float(123)            // Output: 123.0
hasil2 itu bilangan_desimal(-45) // Output: -45.0

// From strings
hasil3 itu float("123.45")       // Output: 123.45
hasil4 itu float("-67.89")       // Output: -67.89
hasil5 itu float("3.14e-2")      // Output: 0.0314

// From scientific notation
hasil6 itu float("1e3")          // Output: 1000.0
hasil7 itu float("2.5E-1")       // Output: 0.25

// From boolean
hasil8 itu float(benar)          // Output: 1.0
hasil9 itu float(salah)          // Output: 0.0
```

---

### bool() / boolean()
Converts an object to a boolean.

**Syntax:**
```python
bool(obj)
boolean(obj)
```

**Parameters:**
- `obj` (any): Object to convert to boolean

**Returns:**
- Boolean: Boolean representation of the object

**Truthiness Rules:**
- Numbers: 0 and 0.0 are `salah`, others are `benar`
- Strings: Empty string "" is `salah`, others are `benar`
- Collections: Empty list [], dict {}, set (), tuple () are `salah`, others are `benar`
- None: Always `salah`
- String values: "true", "1", "yes", "ya", "benar" (case insensitive) are `benar`

**Examples:**
```python
// From numbers
hasil1 itu bool(0)               // Output: salah
hasil2 itu bool(123)             // Output: benar
hasil3 itu boolean(0.0)          // Output: salah
hasil4 itu bool(-45.6)           // Output: benar

// From strings
hasil5 itu bool("")              // Output: salah
hasil6 itu bool("hello")         // Output: benar
hasil7 itu boolean("false")      // Output: salah
hasil8 itu bool("benar")         // Output: benar
hasil9 itu bool("ya")            // Output: benar

// From collections
hasil10 itu bool([])             // Output: salah
hasil11 itu bool([1, 2, 3])      // Output: benar
hasil12 itu bool({})             // Output: salah
hasil13 itu bool({"a": 1})       // Output: benar
hasil14 itu boolean(())          // Output: salah
hasil15 itu bool((1, 2))         // Output: benar
```

---

### list() / daftar()
Converts an iterable to a list.

**Syntax:**
```python
list(iterable)
daftar(iterable)
```

**Parameters:**
- `iterable` (iterable, optional): Object to convert to list

**Returns:**
- List: New list containing the elements

**Examples:**
```python
// From other collections
hasil1 itu list((1, 2, 3))       // Output: [1, 2, 3]
hasil2 itu daftar({1, 2, 3})     // Output: [1, 2, 3] (order may vary)
hasil3 itu list("hello")         // Output: ["h", "e", "l", "l", "o"]

// From range
hasil4 itu list(range(5))        // Output: [0, 1, 2, 3, 4]

// From dictionary (keys only)
hasil5 itu daftar({"a": 1, "b": 2}) // Output: ["a", "b"] (order may vary)

// Empty list
hasil6 itu list()                // Output: []
```

---

### dict() / kamus()
Creates a dictionary from arguments or iterable.

**Syntax:**
```python
dict(iterable)
dict(**kwargs)
kamus(iterable)
kamus(**kwargs)
```

**Parameters:**
- `iterable` (iterable, optional): Iterable of key-value pairs
- `**kwargs`: Keyword arguments as key-value pairs

**Returns:**
- Dictionary: New dictionary

**Examples:**
```python
// From keyword arguments
hasil1 itu dict(a=1, b=2, c=3)   // Output: {"a": 1, "b": 2, "c": 3}
hasil2 itu kamus(name="John", age=25) // Output: {"name": "John", "age": 25}

// From list of tuples
hasil3 itu dict([("a", 1), ("b", 2), ("c", 3)]) // Output: {"a": 1, "b": 2, "c": 3}

// From another dictionary
hasil4 itu dict({"x": 10, "y": 20}) // Output: {"x": 10, "y": 20}

// Empty dictionary
hasil5 itu dict()                // Output: {}
```

---

### set() / himpunan()
Converts an iterable to a set.

**Syntax:**
```python
set(iterable)
himpunan(iterable)
```

**Parameters:**
- `iterable` (iterable, optional): Object to convert to set

**Returns:**
- Set: New set containing unique elements

**Examples:**
```python
// From list (removes duplicates)
hasil1 itu set([1, 2, 2, 3, 3, 3]) // Output: {1, 2, 3}
hasil2 itu himpunan(["a", "b", "a"]) // Output: {"a", "b"}

// From string
hasil3 itu set("hello")          // Output: {"h", "e", "l", "o"}

// From tuple
hasil4 itu set((1, 2, 3, 2, 1))  // Output: {1, 2, 3}

// Empty set
hasil5 itu set()                 // Output: set()
```

---

### tuple() / tupel()
Converts an iterable to a tuple.

**Syntax:**
```python
tuple(iterable)
tupel(iterable)
```

**Parameters:**
- `iterable` (iterable, optional): Object to convert to tuple

**Returns:**
- Tuple: New tuple containing the elements

**Examples:**
```python
// From list
hasil1 itu tuple([1, 2, 3])      // Output: (1, 2, 3)
hasil2 itu tupel(["a", "b"])     // Output: ("a", "b")

// From string
hasil3 itu tuple("hi")           // Output: ("h", "i")

// From set
hasil4 itu tuple({1, 2, 3})      // Output: (1, 2, 3) (order may vary)

// Empty tuple
hasil5 itu tuple()               // Output: ()
```

## Type Information Functions

### jenis() / type()
Returns the type name of an object.

**Syntax:**
```python
jenis(obj)
type(obj)
```

**Parameters:**
- `obj` (any): Object to get type information from

**Returns:**
- String: Type name of the object

**Examples:**
```python
// Basic types
hasil1 itu jenis(123)            // Output: "int"
hasil2 itu jenis(45.67)          // Output: "float"
hasil3 itu jenis("hello")        // Output: "str"
hasil4 itu jenis(benar)          // Output: "bool"

// Collections
hasil5 itu jenis([1, 2, 3])      // Output: "list"
hasil6 itu jenis({"a": 1})       // Output: "dict"
hasil7 itu jenis({1, 2, 3})      // Output: "set"
hasil8 itu jenis((1, 2, 3))      // Output: "tuple"

// Functions and classes
fungsi_test = lambda x -> x + 1
hasil9 itu jenis(fungsi_test)    // Output: "function"
hasil10 itu jenis(RenzMcLang)    // Output: "type" (for classes)
```

---

### panjang() / len()
Returns the length of an object.

**Syntax:**
```python
panjang(obj)
len(obj)
```

**Parameters:**
- `obj` (any): Object with length (string, list, tuple, dict, set)

**Returns:**
- Integer: Length of the object

**Examples:**
```python
// String length
hasil1 itu panjang("hello")      // Output: 5
hasil2 itu len("RenzMcLang")     // Output: 10

// List length
hasil3 itu panjang([1, 2, 3, 4, 5]) // Output: 5
hasil4 itu len([])               // Output: 0

// Dictionary length (number of keys)
hasil5 itu panjang({"a": 1, "b": 2, "c": 3}) // Output: 3
hasil6 itu len({})               // Output: 0

// Set length
hasil7 itu panjang({1, 2, 3})     // Output: 3

// Tuple length
hasil8 itu len((1, 2, 3, 4))      // Output: 4
```

---

### ke_angka()
Converts string to number, trying integer first then float.

**Syntax:**
```python
ke_angka(obj)
```

**Parameters:**
- `obj` (string): String to convert to number

**Returns:**
- Integer or Float: Numeric representation

**Examples:**
```python
// Integer conversion
hasil1 itu ke_angka("123")       // Output: 123
hasil2 itu ke_angka("-456")      // Output: -456

// Float conversion
hasil3 itu ke_angka("123.45")    // Output: 123.45
hasil4 itu ke_angka("-67.89")    // Output: -67.89

// Scientific notation
hasil5 itu ke_angka("1e3")       // Output: 1000.0
hasil6 itu ke_angka("2.5E-1")    // Output: 0.25

// Error cases
// hasil7 = ke_angka("abc")      // Raises ValueError
// hasil8 = ke_angka("")         // Raises ValueError
```

## Mathematical Type Functions

### sum() / jumlah_sum()
Sum of all items in an iterable.

**Syntax:**
```python
sum(iterable, start)
jumlah_sum(iterable, start)
```

**Parameters:**
- `iterable`: Iterable of numbers
- `start` (number, optional): Starting value (default: 0)

**Returns:**
- Number: Sum of all items

**Examples:**
```python
// Basic summation
hasil1 itu sum([1, 2, 3, 4, 5])   // Output: 15
hasil2 itu jumlah_sum([10, 20, 30]) // Output: 60

// With starting value
hasil3 itu sum([1, 2, 3], 10)     // Output: 16
hasil4 itu jumlah_sum([5, 5], 100) // Output: 110

// With floats
hasil5 itu sum([1.5, 2.5, 3.0])   // Output: 7.0

// Empty iterable
hasil6 itu sum([])                // Output: 0
hasil7 itu sum([], 5)             // Output: 5
```

---

### min() / minimum_min()
Returns the smallest item in an iterable.

**Syntax:**
```python
min(iterable)
min(arg1, arg2, ...)
minimum_min(iterable)
minimum_min(arg1, arg2, ...)
```

**Parameters:**
- `iterable`: Iterable of comparable items
- `arg1, arg2, ...`: Individual items to compare

**Returns:**
- Any: The smallest item

**Examples:**
```python
// From iterable
hasil1 itu min([5, 3, 8, 1, 9])   // Output: 1
hasil2 itu minimum_min([10, 20, 5, 15]) // Output: 5

// From arguments
hasil3 itu min(5, 3, 8, 1, 9)     // Output: 1
hasil4 itu minimum_min("apple", "banana", "cherry") // Output: "apple"

// With strings (lexicographical)
hasil5 itu min(["dog", "cat", "elephant"]) // Output: "cat"

// With floats
hasil6 itu min([3.14, 2.71, 1.41]) // Output: 1.41
```

---

### max() / maksimum_max()
Returns the largest item in an iterable.

**Syntax:**
```python
max(iterable)
max(arg1, arg2, ...)
maksimum_max(iterable)
maksimum_max(arg1, arg2, ...)
```

**Parameters:**
- `iterable`: Iterable of comparable items
- `arg1, arg2, ...`: Individual items to compare

**Returns:**
- Any: The largest item

**Examples:**
```python
// From iterable
hasil1 itu max([5, 3, 8, 1, 9])   // Output: 9
hasil2 itu maksimum_max([10, 20, 5, 15]) // Output: 20

// From arguments
hasil3 itu max(5, 3, 8, 1, 9)     // Output: 9
hasil4 itu maksimum_max("apple", "banana", "cherry") // Output: "cherry"

// With strings (lexicographical)
hasil5 itu max(["dog", "cat", "elephant"]) // Output: "elephant"

// With floats
hasil6 itu max([3.14, 2.71, 1.41]) // Output: 3.14
```

---

### abs() / nilai_absolut()
Returns the absolute value of a number.

**Syntax:**
```python
abs(x)
nilai_absolut(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Number: Absolute value

**Examples:**
```python
// Integers
hasil1 itu abs(-5)               // Output: 5
hasil2 itu nilai_absolut(10)     // Output: 10

// Floats
hasil3 itu abs(-3.14)            // Output: 3.14
hasil4 itu nilai_absolut(2.71)   // Output: 2.71

// Zero
hasil5 itu abs(0)                // Output: 0
```

---

### round() / bulatkan()
Rounds a number to specified decimal places.

**Syntax:**
```python
round(number, ndigits)
bulatkan(number, ndigits)
```

**Parameters:**
- `number` (number): Number to round
- `ndigits` (integer, optional): Decimal places (default: 0)

**Returns:**
- Number: Rounded value

**Examples:**
```python
// Round to nearest integer
hasil1 itu round(3.14159)        // Output: 3
hasil2 itu bulatkan(2.71828)     // Output: 3
hasil3 itu round(-2.7)           // Output: -3

// Round to specific decimal places
hasil4 itu round(3.14159, 2)     // Output: 3.14
hasil5 itu bulatkan(2.71828, 3)  // Output: 2.718
hasil6 itu round(1.5, 0)         // Output: 2

// Round negative numbers
hasil7 itu round(-3.14159, 2)    // Output: -3.14
```

---

### pow() / pangkat_pow()
Raises base to the power of exp, optionally with modulus.

**Syntax:**
```python
pow(base, exp, mod)
pangkat_pow(base, exp, mod)
```

**Parameters:**
- `base` (number): Base number
- `exp` (number): Exponent
- `mod` (number, optional): Modulus for modular exponentiation

**Returns:**
- Number: Base raised to the power of exp (mod mod, if provided)

**Examples:**
```python
// Basic exponentiation
hasil1 itu pow(2, 8)             // Output: 256
hasil2 itu pangkat_pow(3, 3)     // Output: 27
hasil3 itu pow(9, 0.5)           // Output: 3.0

// With fractional exponents
hasil4 itu pow(16, 0.25)         // Output: 2.0
hasil5 itu pangkat_pow(27, 1/3)  // Output: 3.0

// With modulus
hasil6 itu pow(2, 8, 100)        // Output: 56 (256 % 100)
hasil7 itu pangkat_pow(3, 4, 50) // Output: 31 (81 % 50)

// Negative exponents
hasil8 itu pow(2, -3)            // Output: 0.125
```

## Input/Output Type Functions

### input() / masukan()
Reads input from the user.

**Syntax:**
```python
input(prompt)
masukan(prompt)
```

**Parameters:**
- `prompt` (string, optional): Prompt to display to user

**Returns:**
- String: User input

**Examples:**
```python
// Basic input
nama itu input("Masukkan nama: ")
tampilkan "Hello, " + nama

// Indonesian alias
umur itu masukan("Berapa umur Anda: ")
tampilkan "Umur Anda: " + umur

// Without prompt
password itu input()
tampilkan "Password received"
```

---

### print() / cetak()
Outputs text to the console.

**Syntax:**
```python
print(*args, sep, end)
cetak(*args, sep, end)
```

**Parameters:**
- `*args`: Items to print
- `sep` (string, optional): Separator between items (default: " ")
- `end` (string, optional): String appended after last item (default: "\n")

**Returns:**
- None

**Examples:**
```python
// Basic printing
print("Hello, World!")
cetak("Halo, Dunia!")

// Multiple items
print("Nama:", "John", "Umur:", 25)

// Custom separator
print("A", "B", "C", sep="-")   // Output: A-B-C

// Custom end
print("Loading", end="...")
print(" done")                  // Output: Loading...done

// Indonesian alias
cetak("Total:", 100, "items")
```

## Usage Notes

1. **Function Aliases**: Many functions have both Indonesian and English names:
   - `jenis()` and `type()`
   - `panjang()` and `len()`
   - `teks()` and `str()`
   - `bilangan_bulat()` and `int()`
   - `bilangan_desimal()` and `float()`
   - `boolean()` and `bool()`
   - `daftar()` and `list()`
   - `kamus()` and `dict()`
   - `himpunan()` and `set()`
   - `tupel()` and `tuple()`
   - `masukan()` and `input()`
   - `cetak()` and `print()`

2. **Type Conversion**: Conversion functions raise appropriate exceptions for invalid inputs.

3. **Boolean Conversion**: The `bool()` function follows Python's truthiness rules with additional support for Indonesian boolean strings.

4. **Number Conversion**: `ke_angka()` tries integer conversion first, then float conversion.

5. **Input/Output**: `input()` and `print()` work exactly like their Python counterparts.

6. **Collection Operations**: Type conversion functions create new copies, they don't modify original objects.