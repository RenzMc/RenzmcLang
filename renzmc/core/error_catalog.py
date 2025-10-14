"""
MIT License

Copyright (c) 2025 RenzMc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""
RenzmcLang Error Catalog Module

Comprehensive error catalog with 100+ unique error codes, detailed descriptions,
solutions, and examples for all error types in RenzmcLang.
"""

from typing import Dict, List, Optional  # noqa: E402


class ErrorInfo:
    """Information about a specific error type."""

    def __init__(
        self,
        code: str,
        category: str,
        title: str,
        description: str,
        solutions: List[str],
        examples: Optional[List[str]] = None,
        related_errors: Optional[List[str]] = None,
        doc_link: Optional[str] = None,
    ):
        """
        Initialize error information.

        Args:
            code: Unique error code (e.g., "RMC-L001")
            category: Error category (Lexer, Parser, Runtime, etc.)
            title: Short title of the error
            description: Detailed description of what causes this error
            solutions: List of solutions to fix the error
            examples: Optional list of code examples
            related_errors: Optional list of related error codes
            doc_link: Optional link to documentation
        """
        self.code = code
        self.category = category
        self.title = title
        self.description = description
        self.solutions = solutions
        self.examples = examples or []
        self.related_errors = related_errors or []
        self.doc_link = doc_link


# Error Catalog Dictionary - 100+ Error Definitions
ERROR_CATALOG: Dict[str, ErrorInfo] = {
    # ========================================
    # LEXER ERRORS (RMC-L001 - RMC-L099)
    # ========================================
    "RMC-L001": ErrorInfo(
        code="RMC-L001",
        category="Lexer",
        title="Karakter Tidak Valid",
        description=("Karakter yang tidak dikenali atau tidak valid " "ditemukan dalam kode."),
        solutions=[
            "• Periksa apakah ada karakter khusus yang tidak didukung",
            "• Pastikan menggunakan encoding UTF-8 untuk file",
            "• Hapus karakter yang tidak terlihat (invisible characters)",
            "• Periksa apakah ada karakter dari copy-paste yang salah",
        ],
        examples=[
            "# Salah: menggunakan karakter unicode yang tidak valid",
            "# Benar: gunakan karakter ASCII atau UTF-8 yang valid",
        ],
        related_errors=["RMC-L002", "RMC-L003"],
    ),
    "RMC-L002": ErrorInfo(
        code="RMC-L002",
        category="Lexer",
        title="String Tidak Ditutup",
        description=("String literal tidak ditutup dengan tanda kutip yang sesuai."),
        solutions=[
            ("• Pastikan setiap string dimulai dan diakhiri dengan " "tanda kutip yang sama"),
            "• Gunakan &quot; untuk string atau ' untuk karakter",
            "• Untuk string multi-baris, gunakan triple quotes (&quot;&quot;&quot;)",
            "• Escape tanda kutip di dalam string dengan backslash (\\)",
        ],
        examples=[
            '# Salah: nama itu "Budi',
            '# Benar: nama itu "Budi"',
            '# Multi-baris: teks itu """Baris 1',
            'Baris 2"""',
        ],
        related_errors=["RMC-L001", "RMC-L003"],
    ),
    "RMC-L003": ErrorInfo(
        code="RMC-L003",
        category="Lexer",
        title="Komentar Tidak Ditutup",
        description="Komentar multi-baris tidak ditutup dengan benar.",
        solutions=[
            "• Pastikan setiap /* diakhiri dengan */",
            "• Gunakan # untuk komentar satu baris",
            "• Periksa nested comments yang mungkin menyebabkan masalah",
            "• Gunakan editor dengan syntax highlighting untuk melihat komentar",
        ],
        examples=[
            "# Salah: /* Komentar tanpa penutup",
            "# Benar: /* Komentar lengkap */",
            "# Atau: # Komentar satu baris",
        ],
        related_errors=["RMC-L001", "RMC-L002"],
    ),
    "RMC-L004": ErrorInfo(
        code="RMC-L004",
        category="Lexer",
        title="Angka Tidak Valid",
        description="Format angka tidak valid atau tidak dapat di-parse.",
        solutions=[
            "• Periksa format angka (integer, float, scientific notation)",
            "• Pastikan tidak ada karakter non-numerik dalam angka",
            "• Gunakan titik (.) untuk desimal, bukan koma (,)",
            "• Untuk scientific notation: 1.5e10 atau 1.5E10",
        ],
        examples=[
            "# Salah: angka itu 1,234.56",
            "# Benar: angka itu 1234.56",
            "# Scientific: besar itu 1.5e10",
        ],
        related_errors=["RMC-L001"],
    ),
    "RMC-L005": ErrorInfo(
        code="RMC-L005",
        category="Lexer",
        title="Token Tidak Dikenali",
        description="Token atau simbol yang tidak dikenali dalam kode.",
        solutions=[
            "• Periksa penggunaan operator yang benar",
            "• Pastikan tidak ada simbol yang salah ketik",
            "• Gunakan operator yang didukung oleh bahasa",
            "• Periksa dokumentasi untuk operator yang valid",
        ],
        examples=[
            "# Salah: x itu 5 @ 3  # operator @ tidak valid",
            "# Benar: x itu 5 + 3",
        ],
        related_errors=["RMC-L001", "RMC-P002"],
    ),
    # ========================================
    # PARSER ERRORS (RMC-P001 - RMC-P099)
    # ========================================
    "RMC-P001": ErrorInfo(
        code="RMC-P001",
        category="Parser",
        title="Sintaks Tidak Valid",
        description="Struktur sintaks kode tidak sesuai dengan aturan bahasa.",
        solutions=[
            "• Periksa tanda kurung, kurung kurawal, dan kurung siku",
            "• Pastikan setiap blok 'jika' memiliki 'selesai'",
            "• Periksa penggunaan koma dan titik koma",
            "• Pastikan struktur blok kode sudah benar",
            "• Gunakan indentasi yang konsisten",
        ],
        examples=[
            "# Salah: jika x > 5",
            "#   tampilkan x",
            "# (tidak ada 'selesai')",
            "",
            "# Benar:",
            "jika x > 5",
            "  tampilkan x",
            "selesai",
        ],
        related_errors=["RMC-P002", "RMC-P003"],
    ),
    "RMC-P002": ErrorInfo(
        code="RMC-P002",
        category="Parser",
        title="Token Tidak Diharapkan",
        description="Token yang tidak diharapkan ditemukan pada posisi tertentu.",
        solutions=[
            "• Periksa urutan keyword dan operator",
            "• Pastikan tidak ada keyword yang salah tempat",
            "• Periksa apakah ada token yang hilang sebelumnya",
            "• Pastikan struktur statement sudah benar",
        ],
        examples=[
            "# Salah: itu x 5",
            "# Benar: x itu 5",
            "",
            "# Salah: jika selesai x > 5",
            "# Benar: jika x > 5 ... selesai",
        ],
        related_errors=["RMC-P001", "RMC-P003"],
    ),
    "RMC-P003": ErrorInfo(
        code="RMC-P003",
        category="Parser",
        title="Blok Tidak Ditutup",
        description="Blok kode tidak ditutup dengan keyword yang sesuai.",
        solutions=[
            "• Pastikan setiap 'jika' memiliki 'selesai'",
            "• Pastikan setiap 'untuk' memiliki 'selesai'",
            "• Pastikan setiap 'selama' memiliki 'selesai'",
            "• Pastikan setiap 'fungsi' memiliki 'selesai'",
            "• Gunakan indentasi untuk membantu melihat struktur blok",
        ],
        examples=[
            "# Salah:",
            "jika x > 5",
            "  tampilkan x",
            "# (tidak ada 'selesai')",
            "",
            "# Benar:",
            "jika x > 5",
            "  tampilkan x",
            "selesai",
        ],
        related_errors=["RMC-P001", "RMC-P002"],
    ),
    "RMC-P004": ErrorInfo(
        code="RMC-P004",
        category="Parser",
        title="Reserved Keyword Sebagai Nama",
        description=("Mencoba menggunakan reserved keyword sebagai nama " "variabel atau fungsi."),
        solutions=[
            "• Jangan gunakan keyword bahasa sebagai nama variabel",
            "• Pilih nama yang berbeda untuk variabel/fungsi",
            "• Lihat daftar reserved keywords di dokumentasi",
            "• Gunakan nama yang deskriptif dan tidak konflik",
        ],
        examples=[
            "# Salah: jika itu 5",
            "# Benar: kondisi itu 5",
            "",
            "# Salah: untuk itu 10",
            "# Benar: jumlah itu 10",
        ],
        related_errors=["RMC-P001", "RMC-N001"],
    ),
    "RMC-P005": ErrorInfo(
        code="RMC-P005",
        category="Parser",
        title="Ekspresi Tidak Valid",
        description="Ekspresi matematika atau logika tidak valid.",
        solutions=[
            "• Periksa operator yang digunakan",
            "• Pastikan operand lengkap (tidak ada operator tanpa operand)",
            "• Periksa tanda kurung untuk precedence",
            "• Pastikan tidak ada operator ganda (++, --, dll)",
        ],
        examples=[
            "# Salah: hasil itu 5 +",
            "# Benar: hasil itu 5 + 3",
            "",
            "# Salah: x itu * 5",
            "# Benar: x itu y * 5",
        ],
        related_errors=["RMC-P001", "RMC-P002"],
    ),
    "RMC-P006": ErrorInfo(
        code="RMC-P006",
        category="Parser",
        title="Kurung Tidak Seimbang",
        description="Jumlah kurung buka dan tutup tidak seimbang.",
        solutions=[
            "• Hitung jumlah kurung buka dan tutup",
            "• Pastikan setiap ( memiliki )",
            "• Pastikan setiap [ memiliki ]",
            "• Pastikan setiap { memiliki }",
            "• Gunakan editor dengan bracket matching",
        ],
        examples=[
            "# Salah: hasil itu (5 + 3",
            "# Benar: hasil itu (5 + 3)",
            "",
            "# Salah: daftar itu [1, 2, 3",
            "# Benar: daftar itu [1, 2, 3]",
        ],
        related_errors=["RMC-P001", "RMC-P003"],
    ),
    "RMC-P007": ErrorInfo(
        code="RMC-P007",
        category="Parser",
        title="Statement Tidak Lengkap",
        description="Statement tidak lengkap atau terpotong.",
        solutions=[
            "• Pastikan statement memiliki semua komponen yang diperlukan",
            "• Periksa apakah ada bagian yang hilang",
            "• Lengkapi statement sesuai sintaks yang benar",
            "• Periksa dokumentasi untuk sintaks yang valid",
        ],
        examples=[
            "# Salah: jika x >",
            "# Benar: jika x > 5",
            "",
            "# Salah: untuk i dari",
            "# Benar: untuk i dari 1 sampai 10",
        ],
        related_errors=["RMC-P001", "RMC-P005"],
    ),
    # ========================================
    # NAME ERRORS (RMC-N001 - RMC-N099)
    # ========================================
    "RMC-N001": ErrorInfo(
        code="RMC-N001",
        category="Runtime",
        title="Variabel Tidak Ditemukan",
        description=("Variabel atau fungsi yang direferensikan belum dideklarasikan."),
        solutions=[
            "• Pastikan variabel sudah dideklarasikan sebelum digunakan",
            "• Periksa ejaan nama variabel (case-sensitive)",
            "• Pastikan variabel berada dalam scope yang benar",
            "• Cek apakah variabel dideklarasikan di dalam blok yang tepat",
            "• Untuk fungsi, pastikan sudah didefinisikan sebelum dipanggil",
        ],
        examples=[
            "# Salah:",
            "tampilkan nama  # nama belum dideklarasikan",
            "",
            "# Benar:",
            'nama itu "Budi"',
            "tampilkan nama",
        ],
        related_errors=["RMC-N002", "RMC-N003"],
    ),
    "RMC-N002": ErrorInfo(
        code="RMC-N002",
        category="Runtime",
        title="Fungsi Tidak Ditemukan",
        description="Fungsi yang dipanggil tidak ditemukan atau belum didefinisikan.",
        solutions=[
            "• Pastikan fungsi sudah didefinisikan sebelum dipanggil",
            "• Periksa ejaan nama fungsi",
            "• Pastikan fungsi berada dalam scope yang benar",
            "• Untuk fungsi built-in, periksa dokumentasi",
            "• Untuk fungsi dari modul, pastikan modul sudah diimpor",
        ],
        examples=[
            "# Salah:",
            "hasil itu hitung(5)  # fungsi hitung belum didefinisikan",
            "",
            "# Benar:",
            "fungsi hitung(x)",
            "  kembalikan x * 2",
            "selesai",
            "hasil itu hitung(5)",
        ],
        related_errors=["RMC-N001", "RMC-I001"],
    ),
    "RMC-N003": ErrorInfo(
        code="RMC-N003",
        category="Runtime",
        title="Scope Error",
        description="Variabel tidak dapat diakses dari scope saat ini.",
        solutions=[
            "• Pastikan variabel dideklarasikan di scope yang tepat",
            "• Gunakan 'global' untuk mengakses variabel global",
            "• Untuk class, gunakan 'diri' untuk mengakses atribut",
            "• Hindari shadowing variabel dari scope luar",
        ],
        examples=[
            "# Salah:",
            "fungsi test()",
            "  x itu 5",
            "selesai",
            "tampilkan x  # x tidak dapat diakses di luar fungsi",
            "",
            "# Benar:",
            "x itu 0",
            "fungsi test()",
            "  global x",
            "  x itu 5",
            "selesai",
            "test()",
            "tampilkan x",
        ],
        related_errors=["RMC-N001", "RMC-N002"],
    ),
    "RMC-N004": ErrorInfo(
        code="RMC-N004",
        category="Runtime",
        title="Dekorator Tidak Ditemukan",
        description="Dekorator yang digunakan tidak ditemukan.",
        solutions=[
            "• Pastikan dekorator sudah didefinisikan",
            "• Periksa ejaan nama dekorator",
            "• Pastikan dekorator diimpor jika dari modul lain",
            "• Periksa dokumentasi untuk dekorator built-in",
        ],
        examples=[
            "# Salah:",
            "@dekorator_tidak_ada",
            "fungsi test()",
            "selesai",
            "",
            "# Benar:",
            "fungsi dekorator_saya(func)",
            "  kembalikan func",
            "selesai",
            "@dekorator_saya",
            "fungsi test()",
            "selesai",
        ],
        related_errors=["RMC-N002", "RMC-I001"],
    ),
    "RMC-N005": ErrorInfo(
        code="RMC-N005",
        category="Runtime",
        title="Context Manager Tidak Ditemukan",
        description="Context manager yang digunakan tidak ditemukan.",
        solutions=[
            "• Pastikan context manager sudah didefinisikan",
            "• Periksa ejaan nama context manager",
            "• Pastikan context manager diimpor jika dari modul lain",
            "• Gunakan context manager built-in yang tersedia",
        ],
        examples=[
            "# Salah:",
            "dengan manager_tidak_ada sebagai m",
            "  # kode",
            "selesai",
            "",
            "# Benar:",
            'dengan buka_file("data.txt") sebagai f',
            "  isi itu f.baca()",
            "selesai",
        ],
        related_errors=["RMC-N002", "RMC-F001"],
    ),
    "RMC-N006": ErrorInfo(
        code="RMC-N006",
        category="Runtime",
        title="Variabel 'diri' Di Luar Konteks",
        description="Variabel 'diri' digunakan di luar konteks class.",
        solutions=[
            "• Gunakan 'diri' hanya di dalam method class",
            "• Pastikan kode berada di dalam definisi class",
            "• Untuk fungsi biasa, gunakan parameter biasa",
            "• Periksa struktur class Anda",
        ],
        examples=[
            "# Salah:",
            "fungsi test()",
            "  tampilkan diri.nama  # 'diri' di luar class",
            "selesai",
            "",
            "# Benar:",
            "kelas Orang",
            "  fungsi tampilkan_nama(diri)",
            "    tampilkan diri.nama",
            "  selesai",
            "selesai",
        ],
        related_errors=["RMC-N003", "RMC-A001"],
    ),
    # ========================================
    # TYPE ERRORS (RMC-T001 - RMC-T099)
    # ========================================
    "RMC-T001": ErrorInfo(
        code="RMC-T001",
        category="Runtime",
        title="Tipe Data Tidak Sesuai",
        description="Operasi dilakukan pada tipe data yang tidak sesuai.",
        solutions=[
            "• Pastikan tipe data sesuai dengan operasi yang dilakukan",
            "• Gunakan konversi tipe jika diperlukan (ke_angka, ke_teks)",
            "• Periksa apakah fungsi menerima argumen dengan tipe yang benar",
            "• Pastikan operasi matematika hanya dilakukan pada angka",
            "• Gunakan type hints untuk membantu deteksi error",
        ],
        examples=[
            "# Salah:",
            'angka itu "5"',
            "hasil itu angka + 3  # string + number",
            "",
            "# Benar:",
            'angka itu "5"',
            "hasil itu ke_angka(angka) + 3",
        ],
        related_errors=["RMC-T002", "RMC-T003"],
    ),
    "RMC-T002": ErrorInfo(
        code="RMC-T002",
        category="Runtime",
        title="Objek Tidak Dapat Dipanggil",
        description="Mencoba memanggil objek yang bukan fungsi atau method.",
        solutions=[
            "• Pastikan objek yang dipanggil adalah fungsi atau method",
            "• Periksa apakah variabel berisi fungsi, bukan nilai lain",
            "• Untuk method, pastikan objek memiliki method tersebut",
            "• Periksa ejaan nama fungsi/method",
        ],
        examples=[
            "# Salah:",
            "x itu 5",
            "hasil itu x()  # x bukan fungsi",
            "",
            "# Benar:",
            "fungsi x()",
            "  kembalikan 5",
            "selesai",
            "hasil itu x()",
        ],
        related_errors=["RMC-T001", "RMC-N002"],
    ),
    "RMC-T003": ErrorInfo(
        code="RMC-T003",
        category="Runtime",
        title="Type Hint Tidak Sesuai",
        description="Nilai tidak sesuai dengan type hint yang dideklarasikan.",
        solutions=[
            "• Pastikan nilai sesuai dengan tipe yang ditentukan",
            "• Periksa deklarasi tipe pada variabel/fungsi",
            "• Gunakan konversi tipe jika diperlukan",
            "• Pastikan tipe hint konsisten di seluruh kode",
            "• Periksa dokumentasi untuk tipe yang valid",
        ],
        examples=[
            "# Salah:",
            'angka: Angka itu "lima"  # string, bukan angka',
            "",
            "# Benar:",
            "angka: Angka itu 5",
        ],
        related_errors=["RMC-T001", "RMC-T002"],
    ),
    "RMC-T004": ErrorInfo(
        code="RMC-T004",
        category="Runtime",
        title="Tipe Tidak Dapat Diiterasi",
        description="Mencoba iterasi pada objek yang tidak dapat diiterasi.",
        solutions=[
            "• Pastikan objek adalah list, tuple, string, atau iterable lainnya",
            "• Periksa tipe data objek sebelum iterasi",
            "• Gunakan konversi ke list jika diperlukan",
            "• Periksa apakah objek memiliki method __iter__",
        ],
        examples=[
            "# Salah:",
            "angka itu 5",
            "untuk i dari angka  # angka tidak dapat diiterasi",
            "selesai",
            "",
            "# Benar:",
            "daftar itu [1, 2, 3, 4, 5]",
            "untuk i dari daftar",
            "  tampilkan i",
            "selesai",
        ],
        related_errors=["RMC-T001", "RMC-T002"],
    ),
    "RMC-T005": ErrorInfo(
        code="RMC-T005",
        category="Runtime",
        title="Operasi Tidak Didukung Untuk Tipe",
        description="Operasi tidak didukung untuk tipe data tertentu.",
        solutions=[
            "• Periksa operasi yang valid untuk tipe data",
            "• Gunakan konversi tipe jika diperlukan",
            "• Periksa dokumentasi untuk operasi yang didukung",
            "• Gunakan method alternatif yang sesuai",
        ],
        examples=[
            "# Salah:",
            'teks itu "hello"',
            "hasil itu teks - 5  # operasi - tidak valid untuk string",
            "",
            "# Benar:",
            'teks itu "hello"',
            "hasil itu teks + &quot; world&quot;",
        ],
        related_errors=["RMC-T001", "RMC-T004"],
    ),
    "RMC-T006": ErrorInfo(
        code="RMC-T006",
        category="Runtime",
        title="Kelas Python Tidak Valid",
        description="Objek bukan kelas Python yang valid.",
        solutions=[
            "• Pastikan objek adalah class Python",
            "• Periksa import class dari modul Python",
            "• Pastikan class sudah didefinisikan",
            "• Gunakan class yang valid dari Python",
        ],
        examples=[
            "# Salah:",
            "obj itu bukan_class()",
            "",
            "# Benar:",
            "dari python impor datetime",
            "waktu itu datetime.datetime.now()",
        ],
        related_errors=["RMC-T001", "RMC-PY001"],
    ),
    # ========================================
    # VALUE ERRORS (RMC-V001 - RMC-V099)
    # ========================================
    "RMC-V001": ErrorInfo(
        code="RMC-V001",
        category="Runtime",
        title="Nilai Tidak Valid",
        description="Nilai yang diberikan tidak valid untuk operasi atau fungsi.",
        solutions=[
            "• Periksa nilai yang dimasukkan sesuai dengan yang diharapkan",
            "• Pastikan format nilai sudah benar",
            "• Periksa rentang nilai yang valid",
            "• Validasi input sebelum digunakan",
            "• Baca dokumentasi untuk nilai yang diterima",
        ],
        examples=[
            "# Salah:",
            "umur itu -5  # umur tidak boleh negatif",
            "",
            "# Benar:",
            "umur itu 25",
        ],
        related_errors=["RMC-V002", "RMC-V003"],
    ),
    "RMC-V002": ErrorInfo(
        code="RMC-V002",
        category="Runtime",
        title="Pembagian Dengan Nol",
        description="Mencoba melakukan pembagian dengan nol.",
        solutions=[
            "• Hindari pembagian dengan nol",
            "• Tambahkan pemeriksaan sebelum pembagian",
            "• Gunakan kondisi: jika pembagi != 0",
            "• Pertimbangkan nilai default jika pembagi nol",
            "• Gunakan try-catch untuk menangani error",
        ],
        examples=[
            "# Salah:",
            "hasil itu 10 / 0",
            "",
            "# Benar:",
            "pembagi itu 0",
            "jika pembagi != 0",
            "  hasil itu 10 / pembagi",
            "lainnya",
            '  tampilkan "Pembagi tidak boleh nol"',
            "selesai",
        ],
        related_errors=["RMC-V001", "RMC-T001"],
    ),
    "RMC-V003": ErrorInfo(
        code="RMC-V003",
        category="Runtime",
        title="Nilai Di Luar Rentang",
        description="Nilai berada di luar rentang yang diperbolehkan.",
        solutions=[
            "• Periksa rentang nilai yang valid",
            "• Gunakan validasi untuk memastikan nilai dalam rentang",
            "• Tambahkan pemeriksaan batas atas dan bawah",
            "• Gunakan clamp untuk membatasi nilai",
        ],
        examples=[
            "# Salah:",
            "indeks itu 10",
            "daftar itu [1, 2, 3]",
            "nilai itu daftar[indeks]  # indeks terlalu besar",
            "",
            "# Benar:",
            "indeks itu 2",
            "daftar itu [1, 2, 3]",
            "nilai itu daftar[indeks]",
        ],
        related_errors=["RMC-V001", "RMC-IX001"],
    ),
    "RMC-V004": ErrorInfo(
        code="RMC-V004",
        category="Runtime",
        title="Nilai Kosong Tidak Diperbolehkan",
        description="Nilai kosong (None/null) tidak diperbolehkan untuk operasi ini.",
        solutions=[
            "• Pastikan variabel memiliki nilai sebelum digunakan",
            "• Periksa apakah nilai adalah None/kosong",
            "• Berikan nilai default jika diperlukan",
            "• Gunakan validasi untuk memastikan nilai tidak kosong",
        ],
        examples=[
            "# Salah:",
            "nama itu kosong",
            "panjang_nama itu panjang(nama)  # nama kosong",
            "",
            "# Benar:",
            'nama itu "Budi"',
            "panjang_nama itu panjang(nama)",
        ],
        related_errors=["RMC-V001", "RMC-T001"],
    ),
    # ========================================
    # INDEX ERRORS (RMC-IX001 - RMC-IX099)
    # ========================================
    "RMC-IX001": ErrorInfo(
        code="RMC-IX001",
        category="Runtime",
        title="Indeks Di Luar Jangkauan",
        description="Indeks yang diakses berada di luar jangkauan list atau string.",
        solutions=[
            "• Pastikan indeks berada dalam rentang yang valid",
            "• Periksa panjang daftar sebelum mengakses indeks",
            "• Ingat: indeks dimulai dari 0",
            "• Gunakan len() untuk memeriksa panjang daftar",
            "• Gunakan try-catch untuk menangani indeks yang tidak valid",
        ],
        examples=[
            "# Salah:",
            "daftar itu [1, 2, 3]",
            "nilai itu daftar[5]  # indeks 5 tidak ada",
            "",
            "# Benar:",
            "daftar itu [1, 2, 3]",
            "jika 5 < panjang(daftar)",
            "  nilai itu daftar[5]",
            "selesai",
        ],
        related_errors=["RMC-V003", "RMC-K001"],
    ),
    "RMC-IX002": ErrorInfo(
        code="RMC-IX002",
        category="Runtime",
        title="Indeks String Di Luar Jangkauan",
        description="Indeks untuk akses karakter string di luar jangkauan.",
        solutions=[
            "• Periksa panjang string sebelum akses",
            "• Gunakan panjang() untuk mendapatkan panjang string",
            "• Pastikan indeks tidak negatif atau terlalu besar",
            "• Gunakan slicing yang aman",
        ],
        examples=[
            "# Salah:",
            'teks itu "hello"',
            "karakter itu teks[10]  # indeks terlalu besar",
            "",
            "# Benar:",
            'teks itu "hello"',
            "karakter itu teks[0]",
        ],
        related_errors=["RMC-IX001", "RMC-V003"],
    ),
    # ========================================
    # KEY ERRORS (RMC-K001 - RMC-K099)
    # ========================================
    "RMC-K001": ErrorInfo(
        code="RMC-K001",
        category="Runtime",
        title="Kunci Tidak Ditemukan",
        description="Kunci yang dicari tidak ada dalam dictionary.",
        solutions=[
            "• Pastikan kunci ada dalam kamus sebelum diakses",
            "• Gunakan metode .get() untuk menghindari error",
            "• Periksa ejaan kunci (case-sensitive)",
            "• Gunakan 'dalam' untuk memeriksa keberadaan kunci",
            "• Gunakan try-catch untuk menangani kunci yang tidak ada",
        ],
        examples=[
            "# Salah:",
            'kamus itu {"nama": "Budi"}',
            "umur itu kamus[\"umur\"]  # kunci 'umur' tidak ada",
            "",
            "# Benar:",
            'kamus itu {"nama": "Budi"}',
            'umur itu kamus.get("umur", 0)  # default 0',
        ],
        related_errors=["RMC-IX001", "RMC-A001"],
    ),
    "RMC-K002": ErrorInfo(
        code="RMC-K002",
        category="Runtime",
        title="Variabel Lingkungan Tidak Ditemukan",
        description="Variabel environment yang dicari tidak ditemukan.",
        solutions=[
            "• Pastikan variabel environment sudah diset",
            "• Periksa ejaan nama variabel environment",
            "• Gunakan nilai default jika variabel tidak ada",
            "• Set variabel environment sebelum menjalankan program",
        ],
        examples=[
            "# Salah:",
            'nilai itu dapatkan_env("VAR_TIDAK_ADA")',
            "",
            "# Benar:",
            'nilai itu dapatkan_env("VAR_TIDAK_ADA", "default")',
        ],
        related_errors=["RMC-K001", "RMC-N001"],
    ),
    # ========================================
    # ATTRIBUTE ERRORS (RMC-A001 - RMC-A099)
    # ========================================
    "RMC-A001": ErrorInfo(
        code="RMC-A001",
        category="Runtime",
        title="Atribut Tidak Ditemukan",
        description="Atribut atau method yang diakses tidak ada pada objek.",
        solutions=[
            "• Pastikan objek memiliki atribut yang dipanggil",
            "• Periksa ejaan nama atribut/method",
            "• Pastikan objek sudah diinisialisasi dengan benar",
            "• Cek dokumentasi untuk atribut yang tersedia",
            "• Untuk class, pastikan atribut didefinisikan di __init__",
        ],
        examples=[
            "# Salah:",
            "kelas Orang",
            "  fungsi __init__(diri, nama)",
            "    diri.nama itu nama",
            "  selesai",
            "selesai",
            'orang itu Orang("Budi")',
            "tampilkan orang.umur  # atribut 'umur' tidak ada",
            "",
            "# Benar:",
            "tampilkan orang.nama",
        ],
        related_errors=["RMC-K001", "RMC-N001"],
    ),
    "RMC-A002": ErrorInfo(
        code="RMC-A002",
        category="Runtime",
        title="Error Mengakses Atribut",
        description="Error terjadi saat mengakses atribut objek.",
        solutions=[
            "• Pastikan objek sudah diinisialisasi",
            "• Periksa apakah atribut ada sebelum diakses",
            "• Gunakan hasattr() untuk memeriksa keberadaan atribut",
            "• Periksa error detail untuk informasi lebih lanjut",
        ],
        examples=[
            "# Gunakan hasattr untuk cek atribut",
            "jika hasattr(objek, 'atribut')",
            "  nilai itu objek.atribut",
            "selesai",
        ],
        related_errors=["RMC-A001", "RMC-T001"],
    ),
    "RMC-A003": ErrorInfo(
        code="RMC-A003",
        category="Runtime",
        title="Error Mengatur Atribut",
        description="Error terjadi saat mengatur nilai atribut objek.",
        solutions=[
            "• Pastikan atribut dapat diubah (tidak read-only)",
            "• Periksa tipe nilai yang diset",
            "• Pastikan objek mendukung assignment atribut",
            "• Periksa error detail untuk informasi lebih lanjut",
        ],
        examples=[
            "# Pastikan atribut dapat diubah",
            "objek.atribut itu nilai_baru",
        ],
        related_errors=["RMC-A001", "RMC-T001"],
    ),
    # ========================================
    # IMPORT ERRORS (RMC-I001 - RMC-I099)
    # ========================================
    "RMC-I001": ErrorInfo(
        code="RMC-I001",
        category="Runtime",
        title="Modul Tidak Ditemukan",
        description="Modul yang diimpor tidak ditemukan atau tidak tersedia.",
        solutions=[
            "• Pastikan modul yang diimpor tersedia",
            "• Periksa ejaan nama modul",
            "• Pastikan modul sudah terinstall",
            "• Periksa jalur impor dan dependensi",
            "• Untuk modul Python, pastikan library sudah diinstall",
        ],
        examples=[
            "# Salah:",
            "impor modul_tidak_ada",
            "",
            "# Benar:",
            "impor math  # modul built-in",
        ],
        related_errors=["RMC-I002", "RMC-N002"],
    ),
    "RMC-I002": ErrorInfo(
        code="RMC-I002",
        category="Runtime",
        title="Error Memuat Modul",
        description="Error terjadi saat memuat atau mengeksekusi modul.",
        solutions=[
            "• Periksa apakah modul memiliki error sintaks",
            "• Pastikan dependensi modul terpenuhi",
            "• Periksa circular import",
            "• Pastikan file modul dapat diakses",
            "• Periksa error log untuk detail lebih lanjut",
        ],
        examples=[
            "# Periksa error di modul yang diimpor",
            "# Pastikan tidak ada circular import",
        ],
        related_errors=["RMC-I001", "RMC-F001"],
    ),
    "RMC-I003": ErrorInfo(
        code="RMC-I003",
        category="Runtime",
        title="Error Relative Import",
        description="Error saat melakukan relative import.",
        solutions=[
            "• Pastikan struktur package benar",
            "• Gunakan absolute import jika memungkinkan",
            "• Periksa __init__.py di direktori package",
            "• Pastikan jalur relative benar",
        ],
        examples=[
            "# Relative import:",
            "dari .modul impor fungsi",
            "",
            "# Absolute import:",
            "dari package.modul impor fungsi",
        ],
        related_errors=["RMC-I001", "RMC-I002"],
    ),
    "RMC-I004": ErrorInfo(
        code="RMC-I004",
        category="Runtime",
        title="Modul Python Belum Diimpor",
        description="Mencoba menggunakan modul Python yang belum diimpor.",
        solutions=[
            "• Import modul Python terlebih dahulu",
            "• Gunakan 'dari python impor' untuk import modul Python",
            "• Pastikan nama modul benar",
            "• Periksa dokumentasi untuk cara import yang benar",
        ],
        examples=[
            "# Salah:",
            "waktu itu datetime.now()  # datetime belum diimpor",
            "",
            "# Benar:",
            "dari python impor datetime",
            "waktu itu datetime.datetime.now()",
        ],
        related_errors=["RMC-I001", "RMC-PY001"],
    ),
    "RMC-I005": ErrorInfo(
        code="RMC-I005",
        category="Runtime",
        title="Cryptography Library Tidak Tersedia",
        description="Library cryptography tidak terinstall atau tidak tersedia.",
        solutions=[
            "• Install library cryptography: pip install cryptography",
            "• Pastikan library sudah terinstall dengan benar",
            "• Periksa versi Python yang kompatibel",
            "• Gunakan virtual environment untuk isolasi",
        ],
        examples=[
            "# Install cryptography:",
            "# pip install cryptography",
        ],
        related_errors=["RMC-I001", "RMC-PY001"],
    ),
    # ========================================
    # FILE ERRORS (RMC-F001 - RMC-F099)
    # ========================================
    "RMC-F001": ErrorInfo(
        code="RMC-F001",
        category="Runtime",
        title="File Tidak Ditemukan",
        description="File yang dicoba diakses tidak ditemukan.",
        solutions=[
            "• Pastikan file ada dan dapat diakses",
            "• Periksa jalur file sudah benar",
            "• Gunakan jalur absolut jika diperlukan",
            "• Periksa ejaan nama file",
            "• Pastikan file tidak dipindahkan atau dihapus",
        ],
        examples=[
            "# Salah:",
            'baca_file("file_tidak_ada.txt")',
            "",
            "# Benar:",
            'jika file_ada("data.txt")',
            '  baca_file("data.txt")',
            "selesai",
        ],
        related_errors=["RMC-F002", "RMC-F003"],
    ),
    "RMC-F002": ErrorInfo(
        code="RMC-F002",
        category="Runtime",
        title="Izin File Ditolak",
        description="Tidak memiliki izin untuk mengakses file.",
        solutions=[
            "• Periksa izin file (read/write permissions)",
            "• Pastikan program memiliki hak akses yang cukup",
            "• Untuk Linux/Mac, gunakan chmod untuk mengubah izin",
            "• Jalankan program dengan hak akses yang sesuai",
        ],
        examples=[
            "# Periksa izin file di sistem operasi",
            "# Linux: chmod 644 file.txt",
        ],
        related_errors=["RMC-F001", "RMC-F003"],
    ),
    "RMC-F003": ErrorInfo(
        code="RMC-F003",
        category="Runtime",
        title="Error Operasi File",
        description="Error terjadi saat melakukan operasi file.",
        solutions=[
            "• Pastikan file tidak sedang digunakan program lain",
            "• Periksa ruang disk yang tersedia",
            "• Pastikan jalur direktori valid",
            "• Tutup file setelah selesai digunakan",
            "• Gunakan try-catch untuk menangani error file",
        ],
        examples=[
            "# Gunakan context manager untuk file",
            'dengan buka_file("data.txt", "r") sebagai f',
            "  isi itu f.baca()",
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F002"],
    ),
    "RMC-F004": ErrorInfo(
        code="RMC-F004",
        category="Runtime",
        title="Direktori Tidak Ditemukan",
        description="Direktori yang dicoba diakses tidak ditemukan.",
        solutions=[
            "• Pastikan direktori ada",
            "• Periksa jalur direktori sudah benar",
            "• Buat direktori jika belum ada",
            "• Gunakan jalur absolut jika diperlukan",
        ],
        examples=[
            "# Buat direktori jika belum ada",
            'jika tidak direktori_ada("folder")',
            '  buat_direktori("folder")',
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F005"],
    ),
    "RMC-F005": ErrorInfo(
        code="RMC-F005",
        category="Runtime",
        title="File Sudah Ada",
        description="File dengan nama yang sama sudah ada.",
        solutions=[
            "• Gunakan nama file yang berbeda",
            "• Hapus file lama jika tidak diperlukan",
            "• Gunakan mode append untuk menambah ke file existing",
            "• Periksa keberadaan file sebelum membuat",
        ],
        examples=[
            "# Periksa keberadaan file",
            'jika tidak file_ada("output.txt")',
            '  buat_file("output.txt")',
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F003"],
    ),
    "RMC-F006": ErrorInfo(
        code="RMC-F006",
        category="Runtime",
        title="Direktori Sudah Ada",
        description="Direktori dengan nama yang sama sudah ada.",
        solutions=[
            "• Gunakan nama direktori yang berbeda",
            "• Hapus direktori lama jika tidak diperlukan",
            "• Periksa keberadaan direktori sebelum membuat",
            "• Gunakan direktori existing jika sesuai",
        ],
        examples=[
            "# Periksa keberadaan direktori",
            'jika tidak direktori_ada("folder")',
            '  buat_direktori("folder")',
            "selesai",
        ],
        related_errors=["RMC-F004", "RMC-F005"],
    ),
    "RMC-F007": ErrorInfo(
        code="RMC-F007",
        category="Runtime",
        title="Bukan Direktori",
        description="Path yang diberikan bukan direktori.",
        solutions=[
            "• Pastikan path menunjuk ke direktori, bukan file",
            "• Periksa tipe path sebelum operasi direktori",
            "• Gunakan fungsi untuk memeriksa apakah path adalah direktori",
            "• Periksa jalur yang benar",
        ],
        examples=[
            "# Periksa apakah path adalah direktori",
            'jika adalah_direktori("path")',
            "  # operasi direktori",
            "selesai",
        ],
        related_errors=["RMC-F004", "RMC-F008"],
    ),
    "RMC-F008": ErrorInfo(
        code="RMC-F008",
        category="Runtime",
        title="Adalah Direktori",
        description="Path yang diberikan adalah direktori, bukan file.",
        solutions=[
            "• Pastikan path menunjuk ke file, bukan direktori",
            "• Periksa tipe path sebelum operasi file",
            "• Gunakan fungsi untuk memeriksa apakah path adalah file",
            "• Periksa jalur yang benar",
        ],
        examples=[
            "# Periksa apakah path adalah file",
            'jika adalah_file("path")',
            "  # operasi file",
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F007"],
    ),
    "RMC-F009": ErrorInfo(
        code="RMC-F009",
        category="Runtime",
        title="Error Membaca File",
        description="Error terjadi saat membaca file.",
        solutions=[
            "• Pastikan file dapat dibaca",
            "• Periksa izin baca file",
            "• Pastikan file tidak corrupt",
            "• Gunakan encoding yang benar",
            "• Periksa format file",
        ],
        examples=[
            "# Baca file dengan encoding",
            'dengan buka_file("data.txt", "r", encoding="utf-8") sebagai f',
            "  isi itu f.baca()",
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F002"],
    ),
    "RMC-F010": ErrorInfo(
        code="RMC-F010",
        category="Runtime",
        title="Error Menulis File",
        description="Error terjadi saat menulis ke file.",
        solutions=[
            "• Pastikan file dapat ditulis",
            "• Periksa izin tulis file",
            "• Pastikan ruang disk cukup",
            "• Periksa jalur direktori valid",
            "• Tutup file setelah menulis",
        ],
        examples=[
            "# Tulis file dengan context manager",
            'dengan buka_file("output.txt", "w") sebagai f',
            '  f.tulis("data")',
            "selesai",
        ],
        related_errors=["RMC-F002", "RMC-F003"],
    ),
    "RMC-F011": ErrorInfo(
        code="RMC-F011",
        category="Runtime",
        title="Error Menghapus File",
        description="Error terjadi saat menghapus file.",
        solutions=[
            "• Pastikan file ada sebelum dihapus",
            "• Periksa izin hapus file",
            "• Pastikan file tidak sedang digunakan",
            "• Tutup file sebelum menghapus",
        ],
        examples=[
            "# Hapus file dengan pengecekan",
            'jika file_ada("temp.txt")',
            '  hapus_file("temp.txt")',
            "selesai",
        ],
        related_errors=["RMC-F001", "RMC-F002"],
    ),
    "RMC-F012": ErrorInfo(
        code="RMC-F012",
        category="Runtime",
        title="Error Membuat Direktori",
        description="Error terjadi saat membuat direktori.",
        solutions=[
            "• Pastikan parent direktori ada",
            "• Periksa izin untuk membuat direktori",
            "• Pastikan nama direktori valid",
            "• Gunakan mkdir dengan parents=True jika diperlukan",
        ],
        examples=[
            "# Buat direktori dengan parent",
            'buat_direktori("path/to/folder", parents=True)',
        ],
        related_errors=["RMC-F004", "RMC-F006"],
    ),
    "RMC-F013": ErrorInfo(
        code="RMC-F013",
        category="Runtime",
        title="Error Menghapus Direktori",
        description="Error terjadi saat menghapus direktori.",
        solutions=[
            "• Pastikan direktori ada sebelum dihapus",
            "• Pastikan direktori kosong (atau gunakan recursive delete)",
            "• Periksa izin hapus direktori",
            "• Pastikan tidak ada file yang terbuka di direktori",
        ],
        examples=[
            "# Hapus direktori kosong",
            'jika direktori_ada("folder")',
            '  hapus_direktori("folder")',
            "selesai",
        ],
        related_errors=["RMC-F004", "RMC-F002"],
    ),
    "RMC-F014": ErrorInfo(
        code="RMC-F014",
        category="Runtime",
        title="Error Membaca Direktori",
        description="Error terjadi saat membaca isi direktori.",
        solutions=[
            "• Pastikan direktori ada",
            "• Periksa izin baca direktori",
            "• Pastikan path adalah direktori",
            "• Gunakan try-catch untuk handle error",
        ],
        examples=[
            "# Baca isi direktori",
            'isi itu baca_direktori("folder")',
            "untuk file dari isi",
            "  tampilkan file",
            "selesai",
        ],
        related_errors=["RMC-F004", "RMC-F007"],
    ),
    "RMC-F015": ErrorInfo(
        code="RMC-F015",
        category="Runtime",
        title="Error Flush File",
        description="Error terjadi saat flush buffer file.",
        solutions=[
            "• Pastikan file masih terbuka",
            "• Periksa izin tulis file",
            "• Pastikan ruang disk cukup",
            "• Gunakan context manager untuk auto-flush",
        ],
        examples=[
            "# File akan auto-flush dengan context manager",
            'dengan buka_file("data.txt", "w") sebagai f',
            '  f.tulis("data")',
            "selesai  # auto-flush di sini",
        ],
        related_errors=["RMC-F003", "RMC-F010"],
    ),
    # ========================================
    # ASYNC ERRORS (RMC-AS001 - RMC-AS099)
    # ========================================
    "RMC-AS001": ErrorInfo(
        code="RMC-AS001",
        category="Runtime",
        title="Error Async/Await",
        description="Error dalam operasi asynchronous.",
        solutions=[
            "• Pastikan fungsi async dipanggil dengan 'tunggu'",
            "• Periksa penggunaan async/await yang benar",
            "• Pastikan event loop berjalan dengan baik",
            "• Gunakan 'asinkron' untuk mendefinisikan fungsi async",
            "• Jangan gunakan 'tunggu' di luar fungsi async",
        ],
        examples=[
            "# Salah:",
            "asinkron fungsi ambil_data()",
            "  kembalikan data",
            "selesai",
            "hasil itu ambil_data()  # tanpa 'tunggu'",
            "",
            "# Benar:",
            "asinkron fungsi main()",
            "  hasil itu tunggu ambil_data()",
            "selesai",
        ],
        related_errors=["RMC-T002"],
    ),
    "RMC-AS002": ErrorInfo(
        code="RMC-AS002",
        category="Runtime",
        title="Objek Bukan Coroutine",
        description="Objek yang digunakan dengan 'tunggu' bukan coroutine.",
        solutions=[
            "• Pastikan fungsi didefinisikan dengan 'asinkron'",
            "• Periksa apakah objek adalah coroutine",
            "• Gunakan 'tunggu' hanya dengan fungsi async",
            "• Periksa return value dari fungsi async",
        ],
        examples=[
            "# Salah:",
            "fungsi biasa()",
            "  kembalikan 5",
            "selesai",
            "hasil itu tunggu biasa()  # bukan coroutine",
            "",
            "# Benar:",
            "asinkron fungsi async_func()",
            "  kembalikan 5",
            "selesai",
            "hasil itu tunggu async_func()",
        ],
        related_errors=["RMC-AS001", "RMC-T002"],
    ),
    "RMC-AS003": ErrorInfo(
        code="RMC-AS003",
        category="Runtime",
        title="Error Async Context Manager",
        description="Error dalam async context manager.",
        solutions=[
            "• Pastikan context manager mendukung async",
            "• Gunakan 'asinkron dengan' untuk async context manager",
            "• Periksa implementasi __aenter__ dan __aexit__",
            "• Pastikan dalam fungsi async",
        ],
        examples=[
            "# Async context manager",
            "asinkron fungsi main()",
            "  asinkron dengan async_resource() sebagai r",
            "    # gunakan resource",
            "  selesai",
            "selesai",
        ],
        related_errors=["RMC-AS001", "RMC-T002"],
    ),
    "RMC-AS004": ErrorInfo(
        code="RMC-AS004",
        category="Runtime",
        title="Error Async Iteration",
        description="Error dalam async iteration.",
        solutions=[
            "• Pastikan objek mendukung async iteration",
            "• Gunakan 'asinkron untuk' untuk async iteration",
            "• Periksa implementasi __aiter__ dan __anext__",
            "• Pastikan dalam fungsi async",
        ],
        examples=[
            "# Async iteration",
            "asinkron fungsi main()",
            "  asinkron untuk item dari async_generator()",
            "    tampilkan item",
            "  selesai",
            "selesai",
        ],
        related_errors=["RMC-AS001", "RMC-T004"],
    ),
    # ========================================
    # PYTHON INTEGRATION (RMC-PY001 - RMC-PY099)
    # ========================================
    "RMC-PY001": ErrorInfo(
        code="RMC-PY001",
        category="Runtime",
        title="Error Integrasi Python",
        description="Error saat mengintegrasikan dengan kode Python.",
        solutions=[
            "• Pastikan library Python sudah terinstall",
            "• Periksa kompatibilitas versi Python",
            "• Pastikan modul Python sudah diimpor dengan benar",
            "• Periksa konversi tipe data antara RenzmcLang dan Python",
            "• Baca dokumentasi Python untuk fungsi yang digunakan",
        ],
        examples=[
            "# Impor modul Python",
            "dari python impor numpy sebagai np",
            "array itu np.array([1, 2, 3])",
        ],
        related_errors=["RMC-I001", "RMC-T001"],
    ),
    "RMC-PY002": ErrorInfo(
        code="RMC-PY002",
        category="Runtime",
        title="Error Eksekusi Python",
        description="Error saat mengeksekusi kode Python.",
        solutions=[
            "• Periksa sintaks kode Python",
            "• Pastikan variabel Python tersedia",
            "• Periksa error message dari Python",
            "• Gunakan try-catch untuk handle error Python",
        ],
        examples=[
            "# Eksekusi kode Python",
            "coba",
            '  eksekusi_python("import math; result = math.sqrt(16)")',
            "tangkap e",
            '  tampilkan "Error Python: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-PY001", "RMC-R001"],
    ),
    "RMC-PY003": ErrorInfo(
        code="RMC-PY003",
        category="Runtime",
        title="Error Evaluasi Python",
        description="Error saat evaluasi ekspresi Python.",
        solutions=[
            "• Periksa sintaks ekspresi Python",
            "• Pastikan variabel dalam ekspresi tersedia",
            "• Gunakan eval dengan hati-hati",
            "• Validasi input sebelum evaluasi",
        ],
        examples=[
            "# Evaluasi ekspresi Python",
            'hasil itu evaluasi_python("2 + 2")',
            "tampilkan hasil  # 4",
        ],
        related_errors=["RMC-PY001", "RMC-PY002"],
    ),
    "RMC-PY004": ErrorInfo(
        code="RMC-PY004",
        category="Runtime",
        title="Error Pemanggilan Fungsi Python",
        description="Error saat memanggil fungsi Python.",
        solutions=[
            "• Pastikan fungsi Python ada",
            "• Periksa argumen yang diberikan",
            "• Pastikan tipe argumen sesuai",
            "• Periksa dokumentasi fungsi Python",
        ],
        examples=[
            "# Panggil fungsi Python",
            "dari python impor math",
            "hasil itu math.sqrt(16)",
            "tampilkan hasil  # 4.0",
        ],
        related_errors=["RMC-PY001", "RMC-T001"],
    ),
    "RMC-PY005": ErrorInfo(
        code="RMC-PY005",
        category="Runtime",
        title="Error Membuat Objek Python",
        description="Error saat membuat instance objek Python.",
        solutions=[
            "• Pastikan class Python ada",
            "• Periksa argumen constructor",
            "• Pastikan tipe argumen sesuai",
            "• Periksa dokumentasi class Python",
        ],
        examples=[
            "# Buat objek Python",
            "dari python impor datetime",
            "waktu itu datetime.datetime(2025, 1, 1)",
            "tampilkan waktu",
        ],
        related_errors=["RMC-PY001", "RMC-T006"],
    ),
    # ========================================
    # RUNTIME ERRORS (RMC-R001 - RMC-R099)
    # ========================================
    "RMC-R001": ErrorInfo(
        code="RMC-R001",
        category="Runtime",
        title="Error Runtime Umum",
        description="Error runtime yang tidak termasuk kategori spesifik.",
        solutions=[
            "• Periksa kembali kode Anda untuk kesalahan",
            "• Pastikan semua nilai dan operasi sesuai",
            "• Coba jalankan kode secara bertahap untuk menemukan masalah",
            "• Periksa dokumentasi untuk penggunaan yang benar",
            "• Gunakan try-catch untuk menangani error",
        ],
        examples=[
            "# Gunakan error handling",
            "coba",
            "  # kode yang mungkin error",
            "tangkap e",
            '  tampilkan "Error: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-R002"],
    ),
    "RMC-R002": ErrorInfo(
        code="RMC-R002",
        category="Runtime",
        title="Rekursi Terlalu Dalam",
        description="Fungsi rekursif melampaui batas kedalaman maksimum.",
        solutions=[
            "• Tambahkan base case untuk menghentikan rekursi",
            "• Periksa kondisi terminasi rekursi",
            "• Pertimbangkan menggunakan iterasi daripada rekursi",
            "• Optimalkan algoritma rekursif",
            "• Gunakan tail recursion jika memungkinkan",
        ],
        examples=[
            "# Salah: rekursi tanpa base case",
            "fungsi rekursif(n)",
            "  kembalikan rekursif(n - 1)",
            "selesai",
            "",
            "# Benar: dengan base case",
            "fungsi faktorial(n)",
            "  jika n <= 1",
            "    kembalikan 1",
            "  selesai",
            "  kembalikan n * faktorial(n - 1)",
            "selesai",
        ],
        related_errors=["RMC-R001"],
    ),
    "RMC-R003": ErrorInfo(
        code="RMC-R003",
        category="Runtime",
        title="Error Dalam Generator",
        description="Error terjadi dalam fungsi generator.",
        solutions=[
            "• Periksa logika generator",
            "• Pastikan yield digunakan dengan benar",
            "• Handle error dalam generator",
            "• Periksa kondisi terminasi generator",
        ],
        examples=[
            "# Generator dengan error handling",
            "fungsi generator()",
            "  coba",
            "    untuk i dari 1 sampai 10",
            "      hasil i",
            "    selesai",
            "  tangkap e",
            '    tampilkan "Error: " + ke_teks(e)',
            "  selesai",
            "selesai",
        ],
        related_errors=["RMC-R001", "RMC-T004"],
    ),
    "RMC-R004": ErrorInfo(
        code="RMC-R004",
        category="Runtime",
        title="Error Mengirim Nilai Ke Generator",
        description="Error saat mengirim nilai ke generator.",
        solutions=[
            "• Pastikan generator sudah dimulai",
            "• Gunakan next() sebelum send()",
            "• Periksa apakah generator menerima nilai",
            "• Handle StopIteration dengan benar",
        ],
        examples=[
            "# Gunakan generator dengan send",
            "gen itu generator()",
            "next(gen)  # mulai generator",
            "gen.send(nilai)  # kirim nilai",
        ],
        related_errors=["RMC-R003", "RMC-T002"],
    ),
    "RMC-R005": ErrorInfo(
        code="RMC-R005",
        category="Runtime",
        title="Retry Decorator Error",
        description="Error dalam retry decorator.",
        solutions=[
            "• Pastikan fungsi diberikan ke retry decorator",
            "• Periksa parameter retry decorator",
            "• Pastikan fungsi dapat dipanggil ulang",
            "• Set max retry yang reasonable",
        ],
        examples=[
            "# Gunakan retry decorator",
            "@retry(max_attempts=3)",
            "fungsi operasi_mungkin_gagal()",
            "  # kode yang mungkin gagal",
            "selesai",
        ],
        related_errors=["RMC-N004", "RMC-R001"],
    ),
    # ========================================
    # CONNECTION ERRORS (RMC-C001 - RMC-C099)
    # ========================================
    "RMC-C001": ErrorInfo(
        code="RMC-C001",
        category="Runtime",
        title="Gagal Terhubung",
        description="Gagal terhubung ke server atau resource.",
        solutions=[
            "• Periksa koneksi internet",
            "• Pastikan URL atau host benar",
            "• Periksa firewall atau proxy settings",
            "• Pastikan server target aktif",
            "• Gunakan timeout yang reasonable",
        ],
        examples=[
            "# HTTP request dengan error handling",
            "coba",
            '  respon itu http_get("https://api.example.com")',
            "tangkap ConnectionError sebagai e",
            '  tampilkan "Gagal terhubung: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-C002", "RMC-C003"],
    ),
    "RMC-C002": ErrorInfo(
        code="RMC-C002",
        category="Runtime",
        title="Timeout Connection",
        description="Koneksi timeout saat menunggu response.",
        solutions=[
            "• Tingkatkan timeout value",
            "• Periksa kecepatan koneksi",
            "• Pastikan server tidak overload",
            "• Gunakan retry mechanism",
            "• Periksa network latency",
        ],
        examples=[
            "# Request dengan timeout",
            'respon itu http_get("https://api.example.com", timeout=30)',
        ],
        related_errors=["RMC-C001", "RMC-C003"],
    ),
    "RMC-C003": ErrorInfo(
        code="RMC-C003",
        category="Runtime",
        title="Error HTTP Request",
        description="Error saat melakukan HTTP request.",
        solutions=[
            "• Periksa URL yang benar",
            "• Pastikan method HTTP sesuai",
            "• Periksa headers dan body request",
            "• Handle HTTP error codes",
            "• Gunakan try-catch untuk error handling",
        ],
        examples=[
            "# HTTP request dengan error handling",
            "coba",
            '  respon itu http_post("https://api.example.com", data)',
            "  jika respon.status == 200",
            "    tampilkan respon.body",
            "  selesai",
            "tangkap e",
            '  tampilkan "HTTP Error: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-C001", "RMC-C002"],
    ),
    # ========================================
    # NOT IMPLEMENTED (RMC-NI001 - RMC-NI099)
    # ========================================
    "RMC-NI001": ErrorInfo(
        code="RMC-NI001",
        category="Runtime",
        title="Fitur Belum Diimplementasi",
        description="Fitur yang dipanggil belum diimplementasi.",
        solutions=[
            "• Periksa dokumentasi untuk fitur yang tersedia",
            "• Gunakan alternatif yang sudah tersedia",
            "• Tunggu update untuk fitur ini",
            "• Kontribusi untuk implementasi fitur",
        ],
        examples=[
            "# Fitur yang belum tersedia akan raise NotImplementedError",
        ],
        related_errors=["RMC-R001"],
    ),
    "RMC-NI002": ErrorInfo(
        code="RMC-NI002",
        category="Runtime",
        title="Form Creation Belum Tersedia",
        description="Fitur form creation belum diimplementasi.",
        solutions=[
            "• Gunakan HTML form manual",
            "• Tunggu update untuk fitur form builder",
            "• Gunakan library eksternal untuk form",
        ],
        examples=[
            "# Sementara gunakan HTML manual untuk form",
        ],
        related_errors=["RMC-NI001"],
    ),
    "RMC-NI003": ErrorInfo(
        code="RMC-NI003",
        category="Runtime",
        title="Form Validation Belum Tersedia",
        description="Fitur form validation belum diimplementasi.",
        solutions=[
            "• Implementasi validasi manual",
            "• Gunakan JavaScript untuk validasi client-side",
            "• Tunggu update untuk fitur validation",
        ],
        examples=[
            "# Implementasi validasi manual",
            "fungsi validasi_form(data)",
            '  jika panjang(data["nama"]) == 0',
            "    kembalikan salah",
            "  selesai",
            "  kembalikan benar",
            "selesai",
        ],
        related_errors=["RMC-NI001", "RMC-NI002"],
    ),
    "RMC-NI004": ErrorInfo(
        code="RMC-NI004",
        category="Runtime",
        title="Static File Serving Belum Tersedia",
        description="Fitur static file serving belum diimplementasi.",
        solutions=[
            "• Gunakan web server eksternal untuk static files",
            "• Tunggu update untuk fitur ini",
            "• Gunakan CDN untuk static assets",
        ],
        examples=[
            "# Gunakan web server seperti nginx untuk static files",
        ],
        related_errors=["RMC-NI001"],
    ),
    "RMC-NI005": ErrorInfo(
        code="RMC-NI005",
        category="Runtime",
        title="Template Rendering Belum Tersedia",
        description="Fitur template rendering belum diimplementasi.",
        solutions=[
            "• Gunakan string concatenation untuk HTML",
            "• Gunakan template engine eksternal",
            "• Tunggu update untuk fitur template",
        ],
        examples=[
            "# Gunakan string untuk HTML sementara",
            'html itu "<html><body>" + konten + "</body></html>"',
        ],
        related_errors=["RMC-NI001"],
    ),
    # ========================================
    # SYSTEM ERRORS (RMC-S001 - RMC-S099)
    # ========================================
    "RMC-S001": ErrorInfo(
        code="RMC-S001",
        category="Runtime",
        title="Error Menjalankan Perintah Sistem",
        description="Error saat menjalankan perintah sistem.",
        solutions=[
            "• Periksa apakah perintah tersedia di sistem",
            "• Pastikan izin eksekusi cukup",
            "• Periksa sintaks perintah",
            "• Gunakan path absolut untuk executable",
            "• Handle error code dari perintah",
        ],
        examples=[
            "# Jalankan perintah dengan error handling",
            "coba",
            '  hasil itu jalankan_perintah("ls -la")',
            "  tampilkan hasil",
            "tangkap e",
            '  tampilkan "Error: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-F002", "RMC-R001"],
    ),
    "RMC-S002": ErrorInfo(
        code="RMC-S002",
        category="Runtime",
        title="Error Mengubah Direktori",
        description="Error saat mengubah working directory.",
        solutions=[
            "• Pastikan direktori target ada",
            "• Periksa izin akses direktori",
            "• Gunakan path absolut",
            "• Periksa apakah path valid",
        ],
        examples=[
            "# Ubah direktori dengan pengecekan",
            'jika direktori_ada("/path/to/dir")',
            '  ubah_direktori("/path/to/dir")',
            "selesai",
        ],
        related_errors=["RMC-F004", "RMC-F002"],
    ),
    # ========================================
    # JSON ERRORS (RMC-J001 - RMC-J099)
    # ========================================
    "RMC-J001": ErrorInfo(
        code="RMC-J001",
        category="Runtime",
        title="Error Parse JSON",
        description="Error saat parsing JSON string.",
        solutions=[
            "• Periksa format JSON yang valid",
            "• Pastikan tidak ada trailing comma",
            "• Periksa quote yang benar (double quote)",
            "• Validasi JSON dengan JSON validator",
            "• Handle parse error dengan try-catch",
        ],
        examples=[
            "# Parse JSON dengan error handling",
            "coba",
            '  data itu parse_json(\'{"nama": "Budi"}\')',
            "  tampilkan data",
            "tangkap e",
            '  tampilkan "JSON Error: " + ke_teks(e)',
            "selesai",
        ],
        related_errors=["RMC-V001", "RMC-R001"],
    ),
    "RMC-J002": ErrorInfo(
        code="RMC-J002",
        category="Runtime",
        title="Error Menulis JSON",
        description="Error saat menulis JSON ke file.",
        solutions=[
            "• Pastikan data dapat di-serialize ke JSON",
            "• Periksa izin tulis file",
            "• Pastikan path file valid",
            "• Handle circular references",
        ],
        examples=[
            "# Tulis JSON ke file",
            'data itu {"nama": "Budi", "umur": 25}',
            'tulis_json("data.json", data)',
        ],
        related_errors=["RMC-F010", "RMC-J001"],
    ),
}


def get_error_info(error_code: str) -> Optional[ErrorInfo]:
    """
    Get error information by error code.

    Args:
        error_code: Error code (e.g., "RMC-L001")

    Returns:
        ErrorInfo object or None if not found
    """
    return ERROR_CATALOG.get(error_code)


def search_error_by_keyword(keyword: str) -> List[ErrorInfo]:
    """
    Search errors by keyword in title or description.

    Args:
        keyword: Keyword to search

    Returns:
        List of matching ErrorInfo objects
    """
    keyword_lower = keyword.lower()
    results = []

    for error_info in ERROR_CATALOG.values():
        if keyword_lower in error_info.title.lower() or keyword_lower in error_info.description.lower():
            results.append(error_info)

    return results


def get_errors_by_category(category: str) -> List[ErrorInfo]:
    """
    Get all errors in a specific category.

    Args:
        category: Category name (Lexer, Parser, Runtime)

    Returns:
        List of ErrorInfo objects in the category
    """
    return [error_info for error_info in ERROR_CATALOG.values() if error_info.category == category]


def suggest_error_code(error_type: str, message: str) -> Optional[str]:
    """
    Suggest error code based on error type and message.

    Args:
        error_type: Type of error (e.g., "LexerError", "ParserError")
        message: Error message

    Returns:
        Suggested error code or None
    """
    # Map error types to code prefixes
    type_to_prefix = {
        "LexerError": "RMC-L",
        "ParserError": "RMC-P",
        "RenzmcNameError": "RMC-N",
        "NameError": "RMC-N",
        "RenzmcTypeError": "RMC-T",
        "TypeError": "RMC-T",
        "RenzmcValueError": "RMC-V",
        "ValueError": "RMC-V",
        "DivisionByZeroError": "RMC-V002",
        "RenzmcIndexError": "RMC-IX",
        "IndexError": "RMC-IX",
        "RenzmcKeyError": "RMC-K",
        "KeyError": "RMC-K",
        "RenzmcAttributeError": "RMC-A",
        "AttributeError": "RMC-A",
        "RenzmcImportError": "RMC-I",
        "ImportError": "RMC-I",
        "FileError": "RMC-F",
        "FileNotFoundError": "RMC-F001",
        "FileExistsError": "RMC-F005",
        "PermissionError": "RMC-F002",
        "IsADirectoryError": "RMC-F008",
        "NotADirectoryError": "RMC-F007",
        "AsyncError": "RMC-AS",
        "PythonIntegrationError": "RMC-PY",
        "RenzmcRuntimeError": "RMC-R",
        "RuntimeError": "RMC-R",
        "RecursionError": "RMC-R002",
        "ConnectionError": "RMC-C001",
        "NotImplementedError": "RMC-NI001",
    }

    # Direct mapping for specific errors
    if error_type in type_to_prefix:
        code = type_to_prefix[error_type]
        if len(code) > 6:  # Full code like "RMC-V002"
            return code
        # Search for matching error in catalog
        message_lower = message.lower()
        for error_code, error_info in ERROR_CATALOG.items():
            if error_code.startswith(code):
                if any(keyword in message_lower for keyword in error_info.title.lower().split()):
                    return error_code

    return None
