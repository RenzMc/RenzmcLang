# Library Collections

## Overview

Library `collections` menyediakan struktur data lanjutan yang tidak tersedia dalam tipe data standar. Library ini mencakup queue, stack, dictionary dengan fitur tambahan, counter, dan struktur data lainnya untuk pengolahan data yang lebih efisien.

## Import Library

```python
dari renzmc.library.collections impor *
```

Atau import class/fungsi spesifik:

```python
dari renzmc.library.collections impor Antrian, Tumpukan, Counter
```

## Class dan Struktur Data

### Antrian (Queue)

Class `Antrian` mengimplementasikan struktur data FIFO (First In, First Out).

**Metode:**
- `masuk(item)`: Tambah item ke belakang antrian
- `keluar()`: Ambil item dari depan antrian
- `lihat_depan()`: Lihat item di depan tanpa menghapus
- `lihat_belakang()`: Lihat item di belakang tanpa menghapus
- `kosong()`: Cek apakah antrian kosong
- `ukuran()`: Dapatkan jumlah item dalam antrian

**Contoh:**
```python
// Buat antrian
antrian itu Antrian()

// Tambah item
antrian.masuk("Orang A")
antrian.masuk("Orang B")
antrian.masuk("Orang C")

tampilkan f"Ukuran antrian: {antrian.ukuran()}"
tampilkan f"Orang pertama: {antrian.lihat_depan()}"

// Ambil item
orang_pertama itu antrian.keluar()
tampilkan f"Dilayani: {orang_pertama}"
tampilkan f"Sisa antrian: {antrian.ukuran()}"
```

### Tumpukan (Stack)

Class `Tumpukan` mengimplementasikan struktur data LIFO (Last In, First Out).

**Metode:**
- `dorung(item)`: Push item ke atas tumpukan
- `ambil()`: Pop item dari atas tumpukan
- `lihat_atas()`: Lihat item di atas tanpa menghapus
- `kosong()`: Cek apakah tumpukan kosong
- `ukuran()`: Dapatkan jumlah item dalam tumpukan

**Contoh:**
```python
// Buat tumpukan
history itu Tumpukan()

// Tambah aksi
history.dorong("Buka file")
history.dorong("Edit teks")
history.dorong("Save file")

tampilkan f"Aksi terakhir: {history.lihat_atas()}"

// Undo
aksi_terakhir itu history.ambil()
tampilkan f"Undo: {aksi_terakhir}"
tampilkan f"Sisa history: {history.ukuran()}"
```

### DefaultDict

Class `DefaultDict` adalah dictionary dengan nilai default otomatis untuk key yang belum ada.

**Metode:**
- `dapatkan(key, default)`: Dapatkan nilai dengan default
- `set_default(key, default)`: Set default value untuk key

**Contoh:**
```python
// Buat defaultdict dengan list factory
data_groups itu DefaultDict(list)
data_groups["fruits"].tambah("apple")
data_groups["fruits"].tambah("orange")
data_groups["vegetables"].tambah("carrot")

// Key baru otomatis dibuat
data_groups["grains"].tambah("rice")

tampilkan data_groups  // Output: {'fruits': ['apple', 'orange'], 'vegetables': ['carrot'], 'grains': ['rice']}

// Dapatkan nilai dengan default
nilai itu data_groups.dapatkan("meats", "Tidak ada")
tampilkan nilai  // Output: "Tidak ada"
```

### OrderedDict

Class `OrderedDict` adalah dictionary yang mempertahankan urutan insertion.

**Metode:**
- `dapatkan_kunci_pertama()`: Dapatkan key pertama
- `dapatkan_kunci_terakhir()`: Dapatkan key terakhir
- `pindah_ke_akhir(key, last)`: Pindah key ke akhir
- `pop_item(last)`: Pop item dari awal/akhir

**Contoh:**
```python
// Buat ordered dict
mahasiswa itu OrderedDict()
mahasiswa["nama"] = "Ahmad"
mahasiswa["nim"] = "2024001"
mahasiswa["jurusan"] = "Teknik Informatika"

tampilkan f"Mahasiswa pertama: {mahasiswa.dapatkan_kunci_pertama()}"
tampilkan f"Mahasiswa terakhir: {mahasiswa.dapatkan_kunci_terakhir()}"

// Pindah key ke akhir
mahasiswa.pindah_ke_akhir("nama")

// Pop item
item_terakhir itu mahasiswa.pop_item()
tampilkan f"Item terakhir: {item_terakhir}"
```

### Counter

Class `Counter` adalah subclass dictionary untuk counting objects.

**Metode:**
- `paling_umum(n)`: Dapatkan n elements yang paling umum
- `tambah(iterable, **kwargs)`: Tambah counts
- `kurangi(iterable, **kwargs)`: Kurangi counts
- `hitung_total()`: Hitung total semua counts
- `dapatkan_elements()`: Dapatkan semua unique elements

**Contoh:**
```python
// Buat counter dari string
teks itu "hello world hello"
counter_kata itu Counter(teks bagi " ")

tampilkan "Kata-kata yang paling umum:"
untuk kata, count dalam counter_kata.paling_umum(3):
    tampilkan f"  {kata}: {count} kali"

tampilkan f"Total kata: {counter_kata.hitung_total()}"

// Tambah counts
counter_kata.tambah(["hello", "hello", "there"])
tampilkan f"Hello count: {counter_kata['hello']}"
```

### RantaiMap (ChainMap)

Class `RantaiMap` menggabungkan多个 maps menjadi single view.

**Metode:**
- `dapatkan_peta()`: Dapatkan semua maps
- `tambah_peta(map)`: Tambah map ke depan chain
- `buat_child(**kwargs)`: Buat child chain map

**Contoh:**
```python
// Buat chain map
global_config itu {debug: false, timeout: 30}
user_config itu {debug: true}
config itu RantaiMap(user_config, global_config)

tampilkan f"Debug mode: {config['debug']}"  // True (user_config)
tampilkan f"Timeout: {config['timeout']}"   // 30 (global_config)

// Tambah map baru
env_config itu {timeout: 60}
config.tambah_peta(env_config)
tampilkan f"Timeout baru: {config['timeout']}"  // 60
```

### NamedTuple

Class factory untuk membuat tuple dengan named fields.

**Contoh:**
```python
// Buat named tuple class
Point itu NamedTuple("Point", ["x", "y"])

// Buat instance
p1 itu Point(10, 20)
p2 itu Point(5, 15)

tampilkan f"Point 1: x={p1.x}, y={p1.y}"
tampilkan f"Point 2: x={p2.x}, y={p2.y}"
```

## Fungsi Helper

### Fungsi Factory

- `buat_antrian(iterable=None)`: Buat instance Antrian
- `buat_tumpukan(iterable=None)`: Buat instance Tumpukan
- `buat_defaultdict(default_factory, **kwargs)`: Buat instance DefaultDict
- `buat_ordered_dict(*args, **kwargs)`: Buat instance OrderedDict
- `buat_counter(iterable=None, **kwargs)`: Buat instance Counter
- `buat_named_tuple(typename, field_names)`: Buat named tuple class
- `buat_chain_map(*maps)`: Buat instance RantaiMap

**Contoh:**
```python
// Buat queue factory
antrian_task itu buat_antrian(["task1", "task2", "task3"])

// Buat counter factory
counter_huruf itu buat_counter("hello world")
```

### Fungsi Heap

- `heapify(list)`: Ubah list menjadi heap
- `heappush(heap, item)`: Push item ke heap
- `heappop(heap)`: Pop smallest item dari heap
- `heappushpop(heap, item)`: Push lalu pop
- `heapreplace(heap, item)`: Pop lalu push
- `nlargest(n, iterable, key=None)`: Dapatkan n largest items
- `nsmallest(n, iterable, key=None)`: Dapatkan n smallest items

**Contoh:**
```python
// Heap operations
data itu [5, 1, 3, 7, 2, 9]
heapify(data)
tampilkan f"Min element: {data[0]}"

smallest itu heappop(data)
tampilkan f"Smallest: {smallest}"

heappush(data, 4)
largest_three itu nlargest(3, data)
tampilkan f"3 largest: {largest_three}"
```

### Fungsi Utilitas Lain

- `deque_siklus(iterable, n)`: Buat deque berputar dari iterable

**Contoh:**
```python
// Deque siklus
data_siklis itu deque_siklus([1, 2, 3, 4, 5], 3)
tampilkan data_siklis  // Output: deque([3, 4, 5])
```

## Contoh Penggunaan Lengkap

```python
// Import library
dari renzmc.library.collections impor *

tampilkan "=== Demo Collections Library ==="

// 1. Queue untuk sistem antrian
tampilkan "\n1. Queue Example:"
antrian_bank itu Antrian()
antrian_bank.masuk("Nasabah A")
antrian_bank.masuk("Nasabah B")
antrian_bank.masuk("Nasabah C")

selama tidak antrian_bank.kosong():
    nasabah itu antrian_bank.keluar()
    tampilkan f"Melayani: {nasabah}"

// 2. Stack untuk undo/redo
tampilkan "\n2. Stack Example:"
undo_stack itu Tumpukan()
undo_stack.dorung("Tulis teks")
undo_stack.dorung("Format bold")
undo_stack.dorung("Tambah gambar")

tampilkan f"Aksi terakhir: {undo_stack.lihat_atas()}"
undo_stack.ambil()
tampilkan f"Undo ke: {undo_stack.lihat_atas()}"

// 3. Counter untuk analisis teks
tampilkan "\n3. Counter Example:"
kalimat itu "renzmclang adalah bahasa pemrograman yang menyenangkan"
counter_kata itu Counter(kalimat bagi " ")
tampilkan "Kata yang paling umum:"
untuk kata, count dalam counter_kata.paling_umum(3):
    tampilkan f"  '{kata}': {count} kali"

// 4. DefaultDict untuk grouping
tampilkan "\n4. DefaultDict Example:"
data_kategori itu DefaultDict(list)
data_kategori["buah"].tambah("apel")
data_kategori["buah"].tambah("jeruk")
data_kategori["sayur"].tambah("wortel")

untuk kategori, items dalam data_kategori.items():
    tampilkan f"{kategori}: {items}"

// 5. ChainMap untuk konfigurasi
tampilkan "\n5. ChainMap Example:"
global_config itu {debug: false, timeout: 30}
user_config itu {debug: true}
config itu RantaiMap(user_config, global_config)

tampilkan f"Debug mode: {config['debug']}"
tampilkan f"Timeout: {config['timeout']}"

tampilkan "\n=== Demo Selesai ==="
```

## Use Cases Umum

1. **Queue (Antrian)**: Task scheduling, message queue, customer service
2. **Stack (Tumpukan)**: Undo/redo systems, expression evaluation, backtracking
3. **DefaultDict**: Grouping operations, counting with default values
4. **OrderedDict**: Configuration management, maintaining insertion order
5. **Counter**: Text analysis, frequency counting, statistics
6. **ChainMap**: Configuration precedence, multiple context management
7. **NamedTuple**: Data containers with named fields, immutability
8. **Heap**: Priority queues, sorting algorithms, top-n selection

## Performa Tips

- Gunakan `Antrian` untuk operasi FIFO yang sering
- Gunakan `Tumpukan` untuk operasi LIFO dan undo systems
- `Counter` lebih efisien untuk counting daripada manual dictionary
- `OrderedDict` memiliki sedikit overhead dibanding dict biasa
- `Heap` operations memiliki O(log n) complexity
- `RantaiMap` efisien untuk lookup dalam multiple mappings

## Error Handling

- Queue dan Stack akan melempar `IndexError` jika kosong
- Counter otomatis menangani key yang tidak ada
- DefaultDict tidak akan melempar KeyError
- NamedTuple fields yang tidak ada akan melempar AttributeError