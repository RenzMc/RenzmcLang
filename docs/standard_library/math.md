# Math Module

The Math module provides comprehensive mathematical functions following Python's math module standards with Indonesian function names.

## Import

```python
dari math impor *
// atau import specific functions
dari math impor pi, sin, cos, sqrt
```

## Mathematical Constants

### pi
The mathematical constant π (3.141592653589793).

```python
dari math impor pi
tampilkan pi  // Output: 3.141592653589793

// Calculate circumference
jari_jari itu 10
keliling itu 2 * pi * jari_jari
tampilkan keliling  // Output: 62.83185307179586
```

### e
The mathematical constant e (2.718281828459045).

```python
dari math impor e
tampilkan e  // Output: 2.718281828459045

// Calculate exponential
hasil itu e ** 2
tampilkan hasil  // Output: 7.38905609893065
```

### tau
The mathematical constant τ (2π = 6.283185307179586).

```python
dari math impor tau
tampilkan tau  // Output: 6.283185307179586

// Full rotation
sudut_penuh itu tau
tampilkan sudut_penuh
```

### inf
Positive infinity.

```python
dari math impor inf
tampilkan inf  // Output: inf

// Check if value is infinite
dari math impor isinf
hasil itu isinf(inf)
tampilkan hasil  // Output: benar
```

### nan
Not a Number (NaN).

```python
dari math impor nan
tampilkan nan  // Output: nan

// Check if value is NaN
dari math impor isnan
hasil itu isnan(nan)
tampilkan hasil  // Output: benar
```

## Basic Operations

### abs() / nilai_absolut()
Returns the absolute value of x.

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
dari math impor abs, nilai_absolut

hasil1 itu abs(-5.5)        // Output: 5.5
hasil2 itu abs(10)          // Output: 10
hasil3 itu nilai_absolut(-3) // Output: 3
```

### round()
Rounds x to specified decimal places.

**Syntax:**
```python
round(x, digits)
```

**Parameters:**
- `x` (number): Number to round
- `digits` (integer, optional): Decimal places (default: 0)

**Returns:**
- Number: Rounded value

**Examples:**
```python
dari math impor round

hasil1 itu round(3.14159, 2)   // Output: 3.14
hasil2 itu round(2.71828)      // Output: 3
hasil3 itu round(-2.7)         // Output: -3
```

### pow() / pangkat()
Calculates base raised to the power of exp.

**Syntax:**
```python
pow(base, exp)
pangkat(base, exp)
```

**Parameters:**
- `base` (number): Base number
- `exp` (number): Exponent

**Returns:**
- Number: Base^exp

**Examples:**
```python
dari math impor pow, pangkat

hasil1 itu pow(2, 8)          // Output: 256.0
hasil2 itu pow(9, 0.5)        // Output: 3.0
hasil3 itu pangkat(5, 3)      // Output: 125.0
```

### sqrt() / akar()
Calculates the square root of x.

**Syntax:**
```python
sqrt(x)
akar(x)
```

**Parameters:**
- `x` (number): Input number (must be non-negative)

**Returns:**
- Number: Square root

**Examples:**
```python
dari math impor sqrt, akar

hasil1 itu sqrt(16)           // Output: 4.0
hasil2 itu sqrt(2)            // Output: 1.4142135623730951
hasil3 itu akar(25)           // Output: 5.0
```

## Trigonometric Functions

### sin() / sinus()
Calculates the sine of x (in radians).

**Syntax:**
```python
sin(x)
sinus(x)
```

**Parameters:**
- `x` (number): Angle in radians

**Returns:**
- Number: Sine value

**Examples:**
```python
dari math impor sin, sinus, pi

hasil1 itu sin(0)              // Output: 0.0
hasil2 itu sin(pi/2)           // Output: 1.0
hasil3 itu sinus(pi)           // Output: 1.2246467991473532e-16 (≈ 0)
```

### cos() / cosinus()
Calculates the cosine of x (in radians).

**Syntax:**
```python
cos(x)
cosinus(x)
```

**Parameters:**
- `x` (number): Angle in radians

**Returns:**
- Number: Cosine value

**Examples:**
```python
dari math impor cos, cosinus, pi

hasil1 itu cos(0)              // Output: 1.0
hasil2 itu cos(pi)             // Output: -1.0
hasil3 itu cosinus(pi/2)       // Output: 6.123233995736766e-17 (≈ 0)
```

### tan() / tangen()
Calculates the tangent of x (in radians).

**Syntax:**
```python
tan(x)
tangen(x)
```

**Parameters:**
- `x` (number): Angle in radians

**Returns:**
- Number: Tangent value

**Examples:**
```python
dari math impor tan, tangen, pi

hasil1 itu tan(0)              // Output: 0.0
hasil2 itu tan(pi/4)           // Output: 0.9999999999999999 (≈ 1)
hasil3 itu tangen(pi/6)        // Output: 0.5773502691896257
```

### asin()
Calculates the inverse sine (arcsin) of x.

**Syntax:**
```python
asin(x)
```

**Parameters:**
- `x` (number): Value between -1 and 1

**Returns:**
- Number: Angle in radians

**Examples:**
```python
dari math impor asin

hasil1 itu asin(0)             // Output: 0.0
hasil2 itu asin(1)             // Output: 1.5707963267948966 (π/2)
hasil3 itu asin(0.5)           // Output: 0.5235987755982989 (π/6)
```

### acos()
Calculates the inverse cosine (arccos) of x.

**Syntax:**
```python
acos(x)
```

**Parameters:**
- `x` (number): Value between -1 and 1

**Returns:**
- Number: Angle in radians

**Examples:**
```python
dari math impor acos

hasil1 itu acos(1)             // Output: 0.0
hasil2 itu acos(0)             // Output: 1.5707963267948966 (π/2)
hasil3 itu acos(-1)            // Output: 3.141592653589793 (π)
```

### atan()
Calculates the inverse tangent (arctan) of x.

**Syntax:**
```python
atan(x)
```

**Parameters:**
- `x` (number): Any real number

**Returns:**
- Number: Angle in radians

**Examples:**
```python
dari math impor atan

hasil1 itu atan(0)             // Output: 0.0
hasil2 itu atan(1)             // Output: 0.7853981633974483 (π/4)
hasil3 itu atan(1000)          // Output: 1.5697963271282298 (≈ π/2)
```

### atan2()
Calculates the arctangent of y/x, considering the quadrant.

**Syntax:**
```python
atan2(y, x)
```

**Parameters:**
- `y` (number): Y coordinate
- `x` (number): X coordinate

**Returns:**
- Number: Angle in radians

**Examples:**
```python
dari math impor atan2

hasil1 itu atan2(1, 1)         // Output: 0.7853981633974483 (π/4)
hasil2 itu atan2(1, 0)         // Output: 1.5707963267948966 (π/2)
hasil3 itu atan2(0, 1)         // Output: 0.0
```

## Logarithmic Functions

### log() / logaritma()
Calculates the logarithm of x with specified base.

**Syntax:**
```python
log(x, base)
logaritma(x, base)
```

**Parameters:**
- `x` (number): Positive number
- `base` (number, optional): Base (default: e for natural log)

**Returns:**
- Number: Logarithm value

**Examples:**
```python
dari math impor log, logaritma, e

hasil1 itu log(100)            // Output: 4.605170185988092 (natural log)
hasil2 itu log(100, 10)        // Output: 2.0 (log base 10)
hasil3 itu logaritma(e)        // Output: 1.0
```

### log10()
Calculates the base-10 logarithm of x.

**Syntax:**
```python
log10(x)
```

**Parameters:**
- `x` (number): Positive number

**Returns:**
- Number: Base-10 logarithm

**Examples:**
```python
dari math impor log10

hasil1 itu log10(1000)         // Output: 3.0
hasil2 itu log10(100)          // Output: 2.0
hasil3 itu log10(1)            // Output: 0.0
```

### log2()
Calculates the base-2 logarithm of x.

**Syntax:**
```python
log2(x)
```

**Parameters:**
- `x` (number): Positive number

**Returns:**
- Number: Base-2 logarithm

**Examples:**
```python
dari math impor log2

hasil1 itu log2(8)             // Output: 3.0
hasil2 itu log2(16)            // Output: 4.0
hasil3 itu log2(1)             // Output: 0.0
```

### ln() / logaritma_natural()
Calculates the natural logarithm (base e) of x.

**Syntax:**
```python
ln(x)
logaritma_natural(x)
```

**Parameters:**
- `x` (number): Positive number

**Returns:**
- Number: Natural logarithm

**Examples:**
```python
dari math impor ln, logaritma_natural, e

hasil1 itu ln(e)               // Output: 1.0
hasil2 itu ln(e ** 2)          // Output: 2.0
hasil3 itu logaritma_natural(1) // Output: 0.0
```

## Angle Conversion Functions

### degrees() / derajat()
Converts radians to degrees.

**Syntax:**
```python
degrees(x)
derajat(x)
```

**Parameters:**
- `x` (number): Angle in radians

**Returns:**
- Number: Angle in degrees

**Examples:**
```python
dari math impor degrees, derajat, pi

hasil1 itu degrees(pi)         // Output: 180.0
hasil2 itu degrees(pi/2)       // Output: 90.0
hasil3 itu derajat(0)          // Output: 0.0
```

### radians() / radian()
Converts degrees to radians.

**Syntax:**
```python
radians(x)
radian(x)
```

**Parameters:**
- `x` (number): Angle in degrees

**Returns:**
- Number: Angle in radians

**Examples:**
```python
dari math impor radians, radian

hasil1 itu radians(180)        // Output: 3.141592653589793
hasil2 itu radians(90)         // Output: 1.5707963267948966
hasil3 itu radian(45)          // Output: 0.7853981633974483
```

## Special Functions

### factorial() / faktorial()
Calculates the factorial of n (n!).

**Syntax:**
```python
factorial(n)
faktorial(n)
```

**Parameters:**
- `n` (integer): Non-negative integer

**Returns:**
- Integer: Factorial value

**Examples:**
```python
dari math impor factorial, faktorial

hasil1 itu factorial(5)        // Output: 120
hasil2 itu factorial(0)        // Output: 1
hasil3 itu faktorial(10)       // Output: 3628800
```

### gcd()
Calculates the greatest common divisor of a and b.

**Syntax:**
```python
gcd(a, b)
```

**Parameters:**
- `a` (integer): First integer
- `b` (integer): Second integer

**Returns:**
- Integer: Greatest common divisor

**Examples:**
```python
dari math impor gcd

hasil1 itu gcd(48, 18)         // Output: 6
hasil2 itu gcd(100, 25)        // Output: 25
hasil3 itu gcd(17, 13)         // Output: 1
```

### lcm()
Calculates the least common multiple of a and b.

**Syntax:**
```python
lcm(a, b)
```

**Parameters:**
- `a` (integer): First integer
- `b` (integer): Second integer

**Returns:**
- Integer: Least common multiple

**Examples:**
```python
dari math impor lcm

hasil1 itu lcm(4, 6)           // Output: 12
hasil2 itu lcm(5, 7)           // Output: 35
hasil3 itu lcm(10, 15)         // Output: 30
```

### ceil() / pembulatan_atas()
Rounds x up to the nearest integer.

**Syntax:**
```python
ceil(x)
pembulatan_atas(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Integer: Rounded up value

**Examples:**
```python
dari math impor ceil, pembulatan_atas

hasil1 itu ceil(3.2)           // Output: 4
hasil2 itu ceil(3.8)           // Output: 4
hasil3 itu pembulatan_atas(-2.3) // Output: -2
```

### floor() / pembulatan_bawah()
Rounds x down to the nearest integer.

**Syntax:**
```python
floor(x)
pembulatan_bawah(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Integer: Rounded down value

**Examples:**
```python
dari math impor floor, pembulatan_bawah

hasil1 itu floor(3.2)          // Output: 3
hasil2 itu floor(3.8)          // Output: 3
hasil3 itu pembulatan_bawah(-2.3) // Output: -3
```

### trunc()
Truncates the decimal part of x.

**Syntax:**
```python
trunc(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Integer: Truncated value

**Examples:**
```python
dari math impor trunc

hasil1 itu trunc(3.2)          // Output: 3
hasil2 itu trunc(3.8)          // Output: 3
hasil3 itu trunc(-2.3)         // Output: -2
```

## Utility Functions

### fsum() / jumlah_presisi()
Performs high-precision summation of iterable.

**Syntax:**
```python
fsum(iterable)
jumlah_presisi(iterable)
```

**Parameters:**
- `iterable`: Iterable of numbers

**Returns:**
- Number: Precise sum

**Examples:**
```python
dari math impor fsum, jumlah_presisi

angka itu [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
hasil1 itu fsum(angka)         // Output: 1.0
hasil2 itu jumlah_presisi([1, 2, 3, 4, 5]) // Output: 15.0
```

### isfinite()
Checks if x is a finite number.

**Syntax:**
```python
isfinite(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Boolean: `benar` if finite, `salah` otherwise

**Examples:**
```python
dari math impor isfinite, inf, nan

hasil1 itu isfinite(123)       // Output: benar
hasil2 itu isfinite(inf)       // Output: salah
hasil3 itu isfinite(nan)       // Output: salah
```

### isinf()
Checks if x is infinity.

**Syntax:**
```python
isinf(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Boolean: `benar` if infinity, `salah` otherwise

**Examples:**
```python
dari math impor isinf, inf

hasil1 itu isinf(inf)          // Output: benar
hasil2 itu isinf(123)          // Output: salah
hasil3 itu isinf(-inf)         // Output: benar
```

### isnan()
Checks if x is NaN (Not a Number).

**Syntax:**
```python
isnan(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Boolean: `benar` if NaN, `salah` otherwise

**Examples:**
```python
dari math impor isnan, nan

hasil1 itu isnan(nan)          // Output: benar
hasil2 itu isnan(123)          // Output: salah
hasil3 itu isnan(0)            // Output: salah
```

### copysign()
Copies the sign of y to x.

**Syntax:**
```python
copysign(x, y)
```

**Parameters:**
- `x` (number): Magnitude
- `y` (number): Sign source

**Returns:**
- Number: x with sign of y

**Examples:**
```python
dari math impor copysign

hasil1 itu copysign(5, -3)     // Output: -5.0
hasil2 itu copysign(-5, 3)     // Output: 5.0
hasil3 itu copysign(5, 0)      // Output: 5.0
```

### frexp()
Returns mantissa and exponent of x.

**Syntax:**
```python
frexp(x)
```

**Parameters:**
- `x` (number): Input number

**Returns:**
- Tuple: (mantissa, exponent)

**Examples:**
```python
dari math impor frexp

hasil1 itu frexp(8)            // Output: (0.5, 4)
hasil2 itu frexp(0.75)         // Output: (0.75, 0)
```

### ldexp()
Calculates x * (2**i).

**Syntax:**
```python
ldexp(x, i)
```

**Parameters:**
- `x` (number): Mantissa
- `i` (integer): Exponent

**Returns:**
- Number: x * (2**i)

**Examples:**
```python
dari math impor ldexp

hasil1 itu ldexp(0.5, 4)       // Output: 8.0
hasil2 itu ldexp(1, 3)         // Output: 8.0
hasil3 itu ldexp(2, 0)         // Output: 2.0
```

## Usage Notes

1. **Import Required**: All math functions must be imported from the math module.

2. **Indonesian Aliases**: Many functions have Indonesian aliases for convenience:
   - `nilai_absolut()` for `abs()`
   - `pangkat()` for `pow()`
   - `akar()` for `sqrt()`
   - `sinus()` for `sin()`
   - `cosinus()` for `cos()`
   - `tangen()` for `tan()`
   - `logaritma()` for `log()`
   - `logaritma_natural()` for `ln()`
   - `derajat()` for `degrees()`
   - `radian()` for `radians()`
   - `faktorial()` for `factorial()`
   - `pembulatan_atas()` for `ceil()`
   - `pembulatan_bawah()` for `floor()`
   - `jumlah_presisi()` for `fsum()`

3. **Angle Units**: Trigonometric functions use radians by default. Use `degrees()`/`radians()` for conversion.

4. **Precision**: Functions use double-precision floating-point arithmetic.

5. **Error Handling**: Functions will raise appropriate exceptions for invalid inputs (e.g., negative numbers for square roots).