# Random Module

The Random module provides comprehensive random number generation functionality following Python's random module standards with Indonesian function names.

## Import

```python
dari random impor *
// atau import specific functions
dari random impor random, randint, choice, shuffle, seed
```

## Basic Random Functions

### random() / acak()
Generates a random float between 0.0 and 1.0.

**Syntax:**
```python
random()
acak()
```

**Returns:**
- Float: Random number between 0.0 (inclusive) and 1.0 (exclusive)

**Examples:**
```python
dari random impor random, acak

// Basic random float
angka1 = random()
tampilkan angka1           // Output: 0.123456789 (example)

// Indonesian alias
angka2 = acak()
tampilkan angka2           // Same as random()

// Generate multiple random numbers
untuk i di rentang(5)
    tampilkan random()
selesai

// Scale random number to custom range
scaled = random() * 100     // 0.0 to 99.999...
tampilkan scaled
```

---

### randint() / acak_bulat()
Generates a random integer between specified bounds (inclusive).

**Syntax:**
```python
randint(a, b)
acak_bulat(a, b)
```

**Parameters:**
- `a` (integer): Lower bound (inclusive)
- `b` (integer): Upper bound (inclusive)

**Returns:**
- Integer: Random integer between a and b

**Examples:**
```python
dari random impor randint, acak_bulat

// Dice roll
dadu = randint(1, 6)
tampilkan dadu             // Output: 1, 2, 3, 4, 5, or 6

// Coin flip
koin = randint(0, 1)
tampilkan koin             // Output: 0 or 1

// Random percentage
persen = randint(0, 100)
tampilkan persen           // Output: 0-100

// Indonesian alias
angka_id = acak_bulat(10, 20)
tampilkan angka_id         // Output: 10-20

// Random year
tahun = randint(2000, 2024)
tampilkan tahun
```

---

### randrange() / rentang_acak()
Generates a random integer from a specified range.

**Syntax:**
```python
randrange(start, stop, step)
rentang_acak(start, stop, step)
```

**Parameters:**
- `start` (integer): Start value
- `stop` (integer, optional): Stop value (exclusive)
- `step` (integer, optional): Step size (default: 1)

**Returns:**
- Integer: Random integer from the range

**Examples:**
```python
dari random impor randrange, rentang_acak

// Basic range (0-9)
angka1 = randrange(10)
tampilkan angka1           // Output: 0-9

// Range with start and stop
angka2 = randrange(5, 15)
tampilkan angka2           // Output: 5-14

// Range with step (even numbers)
angka3 = randrange(0, 100, 2)
tampilkan angka3           // Output: 0, 2, 4, ..., 98

// Odd numbers only
angka4 = randrange(1, 100, 2)
tampilkan angka4           // Output: 1, 3, 5, ..., 99

// Indonesian alias
angka_id = rentang_acak(10, 50, 5)
tampilkan angka_id         // Output: 10, 15, 20, 25, 30, 35, 40, 45
```

---

### uniform() / seragam()
Generates a random float between specified bounds.

**Syntax:**
```python
uniform(a, b)
seragam(a, b)
```

**Parameters:**
- `a` (float): Lower bound
- `b` (float): Upper bound

**Returns:**
- Float: Random float between a and b

**Examples:**
```python
dari random impor uniform, seragam

// Random float between 1.0 and 10.0
angka1 = uniform(1.0, 10.0)
tampilkan angka1           // Output: 1.0-10.0

// Random temperature (Celsius)
temp = uniform(-10.0, 40.0)
tampilkan f"Temperature: {temp:.1f}°C"

// Random price with 2 decimal places
harga = uniform(10.0, 100.0)
tampilkan f"Price: ${harga:.2f}"

// Indonesian alias
angka_id = seragam(0.0, 1.0)
tampilkan angka_id         // Same as uniform(0.0, 1.0)

// Random angle in degrees
sudut = seragam(0, 360)
tampilkan f"Angle: {sudut:.1f}°"
```

---

### triangular() / segitiga()
Generates a random float with triangular distribution.

**Syntax:**
```python
triangular(low, high, mode)
segitiga(low, high, mode)
```

**Parameters:**
- `low` (float): Lower bound
- `high` (float): Upper bound
- `mode` (float, optional): Peak of distribution (default: midpoint)

**Returns:**
- Float: Random number with triangular distribution

**Examples:**
```python
dari random impor triangular, segitiga

// Basic triangular (peak at middle)
angka1 = triangular(0.0, 1.0)
tampilkan angka1

// Triangular with custom peak (biased toward lower values)
angka2 = triangular(0.0, 10.0, 2.0)
tampilkan angka2           // More likely to be near 2.0

// Triangular with custom peak (biased toward higher values)
angka3 = triangular(0.0, 10.0, 8.0)
tampilkan angka3           // More likely to be near 8.0

// Indonesian alias
angka_id = segitiga(1, 100, 50)
tampilkan angka_id

// Simulate exam scores (most students get average scores)
nilai = segitiga(0, 100, 70)
tampilkan f"Exam score: {nilai:.1f}"
```

---

## Sequence Functions

### choice() / pilih_acak()
Selects a random element from a sequence.

**Syntax:**
```python
choice(sequence)
pilih_acak(sequence)
```

**Parameters:**
- `sequence`: Any sequence (list, tuple, string, etc.)

**Returns:**
- Any: Random element from the sequence

**Examples:**
```python
dari random impor choice, pilih_acak

// Random choice from list
buah = ["apple", "banana", "cherry", "date"]
pilihan_buah = choice(buah)
tampilkan pilihan_buah     // Output: "apple", "banana", "cherry", or "date"

// Random choice from tuple
angka = (1, 2, 3, 4, 5)
pilihan_angka = choice(angka)
tampilkan pilihan_angka

// Random character from string
kata = "RENZMC"
huruf = choice(kata)
tampilkan huruf            // Output: R, E, N, Z, M, or C

// Random card from deck
kartu = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
kartu_acak = choice(kartu)
tampilkan kartu_acak

// Indonesian alias
pilihan_id = pilih_acak(["merah", "biru", "hijau"])
tampilkan pilihan_id
```

---

### choices() / banyak_pilihan()
Selects multiple random elements with replacement.

**Syntax:**
```python
choices(sequence, weights, cum_weights, k)
banyak_pilihan(sequence, weights, cum_weights, k)
```

**Parameters:**
- `sequence`: Input sequence
- `weights` (list, optional): Weights for each element
- `cum_weights` (list, optional): Cumulative weights
- `k` (integer, optional): Number of choices (default: 1)

**Returns:**
- List: List of k random elements

**Examples:**
```python
dari random impor choices, banyak_pilihan

// Multiple choices with replacement
warna = ["merah", "kuning", "hijau"]
pilihan = choices(warna, k=3)
tampilkan pilihan          // Output: ["merah", "hijau", "merah"] (example)

// Weighted choices
hobi = ["membaca", "olahraga", "musik", "game"]
bobot = [3, 2, 4, 1]        // musik most likely, game least likely
pilihan_terbobot = choices(hobi, weights=bobot, k=5)
tampilkan pilihan_terbobot

// Simulate dice rolls
dadu = choices([1, 2, 3, 4, 5, 6], k=5)
tampilkan dadu             // Output: [3, 1, 6, 2, 4] (example)

// Indonesian alias
pilihan_id = banyak_pilihan(["A", "B", "C"], weights=[1, 2, 3], k=4)
tampilkan pilihan_id
```

---

### sample() / contoh_acak()
Selects unique random elements without replacement.

**Syntax:**
```python
sample(sequence, k)
contoh_acak(sequence, k)
```

**Parameters:**
- `sequence`: Input sequence
- `k` (integer): Number of elements to select

**Returns:**
- List: List of k unique random elements

**Examples:**
```python
dari random impor sample, contoh_acak

// Sample unique elements
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contoh = sample(angka, k=3)
tampilkan contoh            // Output: [7, 2, 9] (example, unique)

// Sample lottery numbers
lotto = rentang(1, 51)
nomor_menang = sample(lotto, k=6)
tampilkan nomor_menang

// Sample team members
tim = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
tim_proyek = sample(tim, k=3)
tampilkan tim_proyek

// Indonesian alias
contoh_id = contoh_acak(["x", "y", "z", "w"], k=2)
tampilkan contoh_id
```

---

### shuffle() / acak_urutan()
Shuffles a list in place.

**Syntax:**
```python
shuffle(list)
acak_urutan(list)
```

**Parameters:**
- `list`: List to shuffle (modified in place)

**Returns:**
- None: List is modified in place

**Examples:**
```python
dari random impor shuffle, acak_urutan

// Shuffle deck of cards
kartu = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
tampilkan "Before:", kartu
shuffle(kartu)
tampilkan "After:", kartu      // Random order

// Shuffle list of numbers
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
acak_urutan(angka)
tampilkan angka                // Random order

// Random playlist
lagu = ["Song1", "Song2", "Song3", "Song4", "Song5"]
shuffle(lagu)
tampilkan "Random playlist:", lagu

// Fisher-Yates shuffle implementation check
test_list = [1, 2, 3, 4, 5]
shuffle(test_list)
tampilkan test_list            // Still contains same elements, different order
```

---

## Statistical Distributions

### gauss() / distribusi_gauss()
Generates random number with Gaussian (normal) distribution.

**Syntax:**
```python
gauss(mu, sigma)
distribusi_gauss(mu, sigma)
```

**Parameters:**
- `mu` (float): Mean
- `sigma` (float): Standard deviation

**Returns:**
- Float: Random number with normal distribution

**Examples:**
```python
dari random impor gauss, distribusi_gauss

// Normal distribution (mean=0, std=1)
angka1 = gauss(0, 1)
tampilkan angka1

// IQ scores (mean=100, std=15)
iq = gauss(100, 15)
tampilkan f"IQ: {iq:.1f}"

// Height distribution (mean=170cm, std=10cm)
tinggi = gauss(170, 10)
tampilkan f"Height: {tinggi:.1f}cm"

// Indonesian alias
angka_id = distribusi_gauss(50, 10)
tampilkan angka_id

// Simulate test scores
scores = []
untuk i di rentang(100)
    score = gauss(75, 12)
    // Clamp to 0-100 range
    jika score < 0
        score = 0
    selesai
    jika score > 100
        score = 100
    selesai
    tambah(scores, score)
selesai
tampilkan "Sample scores:", scores[:10]
```

---

### expovariate() / distribusi_eksponensial()
Generates random number with exponential distribution.

**Syntax:**
```python
expovariate(lambd)
distribusi_eksponensial(lambd)
```

**Parameters:**
- `lambd` (float): Lambda parameter (> 0)

**Returns:**
- Float: Random number with exponential distribution

**Examples:**
```python
dari random impor expovariate, distribusi_eksponensial

// Time between events (lambda=0.1 = average 10 units)
waktu1 = expovariate(0.1)
tampilkan f"Time until next event: {waktu1:.2f}"

// Customer arrival rate (lambda=2 = 2 customers per minute)
arrival_time = expovariate(2)
tampilkan f"Next customer in: {arrival_time:.3f} minutes"

// Indonesian alias
waktu_id = distribusi_eksponensial(1.5)
tampilkan waktu_id

// Simulate queue system
fungsi simulasi_antrian(lambda_rate, total_customers):
    wait_times = []
    total_wait = 0
    
    untuk i di rentang(total_customers)
        wait_time = expovariate(lambda_rate)
        tambah(wait_times, wait_time)
        total_wait = total_wait + wait_time
    selesai
    
    avg_wait = total_wait / total_customers
    tampilkan f"Average wait time: {avg_wait:.3f}"
    hasil wait_times
selesai

simulasi_antrian(3, 50)  // 3 customers per minute, 50 customers
```

---

## Utility Functions

### seed() / inisialisasi()
Initializes the random number generator.

**Syntax:**
```python
seed(value)
inisialisasi(value)
```

**Parameters:**
- `value` (integer/float/string/bytes, optional): Seed value (default: system time)

**Examples:**
```python
dari random impor seed, random, inisialisasi

// Deterministic sequence
seed(12345)
tampilkan random()          // Always same value for seed 12345
tampilkan random()          // Second value always same for seed 12345

// Reset with same seed
seed(12345)
tampilkan random()          // Same as first call above

// Random seed (current time)
seed()                     // Using system time
tampilkan random()          // Different each time

// Indonesian alias
inisialisasi(42)
tampilkan random()

// String seed
seed("hello")
tampilkan random()
```

---

## Advanced Usage Examples

### Random Password Generator

```python
dari random impor choice, randint
dari string impor (from Python integration)

fungsi buat_password(panjang=12, gunakan_simbol=benar):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    angka = "0123456789"
    simbol = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    karakter = huruf_kecil + huruf_besar + angka
    jika gunakan_simbol
        karakter = karakter + simbol
    selesai
    
    password = ""
    untuk i di rentang(panjang)
        password = password + choice(karakter)
    selesai
    
    // Ensure at least one of each type
    password_list = list(password)
    password_list[0] = choice(huruf_kecil)
    password_list[1] = choice(huruf_besar)
    password_list[2] = choice(angka)
    
    jika gunakan_simbol dan panjang > 3
        password_list[3] = choice(simbol)
    selesai
    
    // Shuffle the password
    shuffle(password_list)
    
    hasil "".join(password_list)
selesai

// Usage
secure_password = buat_password(16, benar)
tampilkan f"Secure password: {secure_password}"

simple_password = buat_password(8, salah)
tampilkan f"Simple password: {simple_password}"
```

### Monte Carlo Simulation

```python
dari random impor random, uniform

fungsi estimasi_pi(jumlah_sampel=100000):
    di_dalam_lingkaran = 0
    
    untuk i di rentang(jumlah_sampel)
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        
        // Check if point is inside unit circle
        jika x*x + y*y <= 1
            di_dalam_lingkaran = di_dalam_lingkaran + 1
        selesai
    selesai
    
    // Pi = 4 * (points inside circle / total points)
    pi_estimasi = 4 * di_dalam_lingkaran / jumlah_sampel
    tampilkan f"π ≈ {pi_estimasi:.6f}"
    hasil pi_estimasi
selesai

// Usage
pi_approx = estimasi_pi(100000)
tampilkan f"Actual π: 3.141593"
tampilkan f"Error: {abs(pi_approx - 3.141593):.6f}"
```

### Random Walk Simulation

```python
dari random impor choice, randint

fungsi simulasi_random_walk(langkah=100, probabilitas_naik=0.5):
    posisi = 0
    posisi_sejarah = [posisi]
    
    untuk i di rentang(langkah)
        // 50% chance up, 50% chance down
        jika random() < probabilitas_naik
            posisi = posisi + 1
        lainnya
            posisi = posisi - 1
        selesai
        
        tambah(posisi_sejarah, posisi)
    selesai
    
    akhir_posisi = posisi
    posisi_max = max(posisi_sejarah)
    posisi_min = min(posisi_sejarah)
    
    tampilkan f"Final position: {akhir_posisi}"
    tampilkan f"Max position: {posisi_max}"
    tampilkan f"Min position: {posisi_min}"
    
    hasil {
        "final_position": akhir_posisi,
        "max_position": posisi_max,
        "min_position": posisi_min,
        "history": posisi_sejarah
    }
selesai

// Usage
walk_result = simulasi_random_walk(1000, 0.55)  // Slightly biased upward
```

### Weighted Random Selection

```python
dari random impor choices, random

fungsi pilih_berbobot(options, weights):
    // Normalize weights
    total_weight = sum(weights)
    normalized_weights = []
    
    untuk weight dari weights
        normalized_weight = weight / total_weight
        tambah(normalized_weights, normalized_weight)
    selesai
    
    hasil choices(options, weights=normalized_weights, k=1)[0]
selesai

// Simulate weather with probabilities
cuaca = ["cerah", "berawan", "hujan", "badai"]
prob_cuaca = [0.5, 0.3, 0.15, 0.05]  // 50% sunny, 30% cloudy, etc.

// Simulate 30 days of weather
prediksi_cuaca = []
untuk day di rentang(30)
    hari_cuaca = pilih_berbobot(cuaca, prob_cuaca)
    tambah(prediksi_cuaca, hari_cuaca)
selesai

tampilkan "30-day weather forecast:", prediksi_cuaca

// Count occurrences
cuaca_count = {"cerah": 0, "berawan": 0, "hujan": 0, "badai": 0}
untuk weather dari prediksi_cuaca
    cuaca_count[weather] = cuaca_count[weather] + 1
selesai

tampilkan "Weather counts:", cuaca_count
```

## Performance Notes

- **Speed**: `random()` is fastest, distributions are slower
- **Memory**: `choices()` with large k uses more memory
- **Seed**: Setting seed ensures reproducible results
- **Threading**: Each thread has its own random generator

## Best Practices

1. **Use appropriate function**: `randint()` for integers, `random()` for floats
2. **Security**: Use `SystemRandom` for cryptographic applications
3. **Reproducibility**: Set seed for testing and debugging
4. **Bias**: Be aware of distribution characteristics when using statistical functions