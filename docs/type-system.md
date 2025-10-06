# Sistem Tipe RenzmcLang

## Pengenalan

RenzmcLang sekarang memiliki **sistem tipe yang robust** dengan dukungan untuk type hints opsional. Sistem ini dirancang untuk:

- ✅ Mendeteksi kesalahan tipe saat runtime
- ✅ Meningkatkan keamanan kode
- ✅ Memberikan dokumentasi yang lebih baik
- ✅ Mempertahankan backward compatibility penuh

## Fitur Phase 1

### 1. Type Hints untuk Variabel

Anda dapat menambahkan anotasi tipe pada variabel menggunakan sintaks `:`:

```python
umur: Integer itu 25
nama: String itu "Budi"
tinggi: Float itu 175.5
is_active: Boolean itu benar
hobi: List itu ["membaca", "coding"]
profil: Dict itu {"nama": "Budi", "umur": 25}
```

### 2. Type Hints untuk Parameter Fungsi

Parameter fungsi dapat memiliki anotasi tipe:

```python
fungsi jumlahkan(a: Integer, b: Integer):
    hasil a + b
selesai

fungsi sapa(nama: String, umur: Integer):
    tampilkan "Halo " + nama + ", umur " + ke_teks(umur)
selesai
```

### 3. Tipe Data yang Didukung

#### Tipe Dasar

| Tipe | Nama Indonesia | Nama Inggris | Contoh |
|------|----------------|--------------|--------|
| Integer | `Integer`, `Bilangan`, `BilanganBulat` | `int`, `integer` | `42` |
| Float | `Float`, `Desimal`, `BilanganDesimal` | `float` | `3.14` |
| String | `String`, `Teks` | `str`, `string` | `"Hello"` |
| Boolean | `Boolean`, `Bool` | `bool`, `boolean` | `benar`, `salah` |
| List | `List`, `Daftar` | `list` | `[1, 2, 3]` |
| Dict | `Dict`, `Kamus`, `Dictionary` | `dict` | `{"key": "value"}` |
| Tuple | `Tuple` | `tuple` | `(1, 2, 3)` |
| Set | `Set`, `Himpunan` | `set` | `{1, 2, 3}` |
| None | `None`, `Kosong` | `none` | `kosong` |
| Any | `Any`, `Apapun` | `any` | Semua tipe |

### 4. Validasi Tipe Runtime

Sistem tipe melakukan validasi saat runtime:

```python
angka: Integer itu 42
tampilkan angka

angka: Integer itu "bukan angka"
```

### 5. Konversi Tipe Otomatis

Integer dapat otomatis dikonversi ke Float:

```python
nilai: Float itu 10
tampilkan nilai
```

### 6. Backward Compatibility

**Kode tanpa type hints tetap berfungsi 100%!**

```python
nama itu "Budi"
umur itu 25

fungsi tambah(a, b):
    hasil a + b
selesai
```

### 7. Mixing Type Hints

Anda dapat mencampur kode dengan dan tanpa type hints:

```python
fungsi hitung_diskon(harga: Float, persen):
    diskon itu harga * persen / 100
    hasil harga - diskon
selesai

harga_akhir itu hitung_diskon(100.0, 10)
```

## Advanced Type Features (Phase 2)

### Union Types

Union types memungkinkan variabel menerima beberapa tipe data:

```python
nilai: Integer | String itu 42
tampilkan nilai

nilai itu "empat puluh dua"
tampilkan nilai

fungsi format_nilai(x: Integer | String):
    hasil "Nilai: " + ke_teks(x)
selesai

hasil1 itu format_nilai(100)
hasil2 itu format_nilai("seratus")
```

### Optional Types

Optional types untuk nilai yang bisa None/kosong:

```python
nama: String? itu "Budi"
tampilkan nama

nama itu kosong
tampilkan nama

fungsi sapa(nama: String?):
    jika nama == kosong
        hasil "Halo, Tamu!"
    selesai
    hasil "Halo, " + nama + "!"
selesai

pesan1 itu sapa("Budi")
pesan2 itu sapa(kosong)
```

### Generic Types

Generic types untuk koleksi dengan tipe spesifik:

```python
angka: List[Integer] itu [1, 2, 3, 4, 5]
nama: List[String] itu ["Budi", "Ani", "Citra"]

umur: Dict[String, Integer] itu {
    "Budi": 25,
    "Ani": 23,
    "Citra": 27
}

fungsi jumlahkan_list(data: List[Integer]):
    total itu 0
    untuk item dari data
        total itu total + item
    selesai
    hasil total
selesai

total itu jumlahkan_list([1, 2, 3, 4, 5])
tampilkan total
```

### Type Aliases

Type aliases memungkinkan Anda membuat nama alias untuk tipe yang kompleks:

```python
tipe UserId = Integer
tipe Username = String
tipe UserData = Dict[String, Integer | String]

user_id: UserId itu 12345
username: Username itu "budi_santoso"

user: UserData itu {
    "id": 12345,
    "nama": "Budi Santoso",
    "umur": 25
}

fungsi get_user_by_id(id: UserId) -> UserData:
    hasil {
        "id": id,
        "nama": "User " + ke_teks(id),
        "umur": 20
    }
selesai

data_user itu get_user_by_id(user_id)
tampilkan data_user
```

### Return Type Hints

Fungsi dapat memiliki anotasi tipe untuk nilai kembalian menggunakan sintaks `->`:

```python
fungsi tambah(a: Integer, b: Integer) -> Integer:
    hasil a + b
selesai

fungsi bagi(a: Float, b: Float) -> Float:
    jika b == 0
        hasil 0.0
    selesai
    hasil a / b
selesai

fungsi get_nama() -> String:
    hasil "Budi Santoso"
selesai

fungsi get_data() -> Dict[String, Integer]:
    hasil {"umur": 25, "tinggi": 175}
selesai

fungsi cari_user(id: Integer) -> String?:
    jika id == 1
        hasil "Budi"
    selesai
    hasil kosong
selesai

hasil_tambah itu tambah(5, 3)
hasil_bagi itu bagi(10.0, 2.0)
nama itu get_nama()
data itu get_data()
user itu cari_user(1)
```

### Literal Types

Literal types membatasi nilai ke set literal tertentu:

```python
tipe Status = Literal["aktif", "nonaktif", "pending"]
tipe Level = Literal[1, 2, 3, 4, 5]
tipe Mode = Literal["baca", "tulis", "eksekusi"]

status: Status itu "aktif"
tampilkan status

level: Level itu 3
tampilkan level

fungsi set_mode(mode: Mode):
    tampilkan "Mode diatur ke: " + mode
selesai

set_mode("baca")
set_mode("tulis")
```

### TypedDict

TypedDict mendefinisikan struktur dictionary dengan field dan tipe spesifik:

```python
tipe Person = TypedDict["nama": String, "umur": Integer, "kota": String]

person: Person itu {
    "nama": "Budi",
    "umur": 25,
    "kota": "Jakarta"
}

fungsi buat_person(nama: String, umur: Integer, kota: String) -> Person:
    hasil {
        "nama": nama,
        "umur": umur,
        "kota": kota
    }
selesai

person2 itu buat_person("Ani", 23, "Bandung")
tampilkan person2
```

## Contoh Penggunaan

### Contoh 1: Variabel dengan Type Hints

```python
tampilkan "=== Type Hints Dasar ==="

umur: Integer itu 25
nama: String itu "Budi"
tinggi: Float itu 175.5
is_student: Boolean itu benar

tampilkan "Nama: " + nama
tampilkan "Umur: " + ke_teks(umur)
tampilkan "Tinggi: " + ke_teks(tinggi)
tampilkan "Mahasiswa: " + ke_teks(is_student)
```

### Contoh 2: Fungsi dengan Type Hints

```python
fungsi hitung_luas_persegi(sisi: Float) -> Float:
    luas itu sisi * sisi
    hasil luas
selesai

fungsi buat_profil(nama: String, umur: Integer, tinggi: Float) -> Dict[String, Integer | String | Float]:
    profil itu {
        "nama": nama,
        "umur": umur,
        "tinggi": tinggi
    }
    hasil profil
selesai

luas itu hitung_luas_persegi(5.0)
tampilkan "Luas: " + ke_teks(luas)

data itu buat_profil("Budi", 25, 175.5)
tampilkan data
```

### Contoh 3: Type Aliases dan Return Types

```python
tipe UserId = Integer
tipe Email = String
tipe UserProfile = Dict[String, Integer | String]

fungsi create_user(id: UserId, email: Email, nama: String) -> UserProfile:
    hasil {
        "id": id,
        "email": email,
        "nama": nama
    }
selesai

fungsi get_user_id(profile: UserProfile) -> UserId:
    hasil profile["id"]
selesai

user itu create_user(123, "budi@example.com", "Budi")
tampilkan user

user_id itu get_user_id(user)
tampilkan "User ID: " + ke_teks(user_id)
```

### Contoh 4: Literal dan TypedDict

```python
tipe Status = Literal["aktif", "nonaktif", "pending"]
tipe User = TypedDict["id": Integer, "nama": String, "status": Status]

fungsi buat_user(id: Integer, nama: String, status: Status) -> User:
    hasil {
        "id": id,
        "nama": nama,
        "status": status
    }
selesai

fungsi update_status(user: User, status_baru: Status) -> User:
    user["status"] itu status_baru
    hasil user
selesai

user1 itu buat_user(1, "Budi", "aktif")
tampilkan user1

user1 itu update_status(user1, "pending")
tampilkan user1
```

## Pesan Error

Sistem tipe memberikan pesan error yang jelas dalam Bahasa Indonesia:

```python
angka: Integer itu "bukan angka"

fungsi tambah(a: Integer, b: Integer) -> Integer:
    hasil a + b
selesai

tambah("5", 3)
```

## Best Practices

### 1. Gunakan Type Hints untuk Fungsi Publik

```python
fungsi hitung_pajak(harga: Float, tarif: Float) -> Float:
    pajak itu harga * tarif
    hasil pajak
selesai
```

### 2. Type Hints Opsional untuk Fungsi Internal

```python
fungsi _helper_internal(x, y):
    hasil x + y
selesai
```

### 3. Dokumentasi dengan Type Hints

```python
fungsi konversi_suhu(celsius: Float) -> Float:
    fahrenheit itu (celsius * 9/5) + 32
    hasil fahrenheit
selesai
```

### 4. Gunakan Type Aliases untuk Tipe Kompleks

```python
tipe UserData = Dict[String, Integer | String | Float]
tipe UserId = Integer

fungsi get_user(id: UserId) -> UserData:
    hasil {"id": id, "nama": "User"}
selesai
```

### 5. Gunakan Return Type Hints

```python
fungsi calculate(x: Integer, y: Integer) -> Integer:
    hasil x + y
selesai
```

## Roadmap

### Phase 1 (Selesai) ✅
- ✅ Basic type hints untuk variables
- ✅ Type hints untuk function parameters
- ✅ Runtime type validation
- ✅ Indonesian and English type names
- ✅ Backward compatibility

### Phase 2 (Selesai) ✅
- ✅ Union types: `nilai: Integer | String`
- ✅ Optional types: `nama: String?`
- ✅ Generic types: `List[Integer]`, `Dict[String, Integer]`
- ✅ Type aliases: `tipe UserId = Integer`
- ✅ Return type hints: `fungsi tambah(...) -> Integer:`
- ✅ Literal types: `Literal["aktif", "nonaktif"]`
- ✅ TypedDict: `TypedDict["nama": String, "umur": Integer]`

### Phase 3 (Masa Depan)
- [ ] Static type checking (compile-time)
- [ ] Type inference (Partial implementation available)
- [ ] Advanced type features (Callable, Protocol, etc.)

## FAQ

### Q: Apakah type hints wajib?
**A:** Tidak! Type hints bersifat **opsional**. Kode tanpa type hints tetap berfungsi 100%.

### Q: Apakah kode lama saya akan rusak?
**A:** Tidak! Sistem tipe dirancang dengan **backward compatibility penuh**. Semua kode lama tetap berfungsi.

### Q: Kapan sebaiknya menggunakan type hints?
**A:** Gunakan type hints untuk:
- Fungsi publik yang digunakan di banyak tempat
- Kode yang kompleks
- API dan library
- Kode yang perlu dokumentasi jelas

### Q: Bisakah saya mixing kode dengan dan tanpa type hints?
**A:** Ya! Anda bisa mencampur keduanya dengan bebas.

### Q: Bagaimana cara menggunakan type aliases?
**A:** Gunakan sintaks `tipe NamaAlias = TipeAsli` untuk membuat alias tipe.

### Q: Bagaimana cara menambahkan return type hints?
**A:** Gunakan sintaks `-> TipeKembalian` setelah parameter fungsi dan sebelum titik dua.

Selamat coding dengan type safety! 🚀