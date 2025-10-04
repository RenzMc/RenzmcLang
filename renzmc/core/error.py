class RenzmcError(Exception):

    def __init__(self, message, line=None, column=None, source_code=None):
        self.message = message
        self.line = line
        self.column = column
        self.source_code = source_code
        if line is not None and column is not None:
            super().__init__(f"{message} (baris {line}, kolom {column})")
        else:
            super().__init__(message)


class LexerError(RenzmcError):
    pass


class ParserError(RenzmcError):
    pass


class InterpreterError(RenzmcError):
    pass


class NameError(RenzmcError):
    pass


class TypeError(RenzmcError):
    pass


class ValueError(RenzmcError):
    pass


class ImportError(RenzmcError):
    pass


class AttributeError(RenzmcError):
    pass


class IndexError(RenzmcError):
    pass


class KeyError(RenzmcError):
    pass


class RuntimeError(RenzmcError):
    pass


class DivisionByZeroError(RenzmcError):
    pass


class FileError(RenzmcError):
    pass


class PythonIntegrationError(RenzmcError):
    pass


class SyntaxError(RenzmcError):
    pass


class TypeHintError(RenzmcError):
    pass


class AsyncError(RenzmcError):
    pass


def format_error(error, source_code=None):
    if isinstance(error, KeyboardInterrupt):
        return "✓ Program dihentikan oleh pengguna (Ctrl+C)"
    if (
        not hasattr(error, "line")
        or not hasattr(error, "column")
        or error.line is None
        or (error.column is None)
    ):
        error_type = error.__class__.__name__
        if error_type.endswith("Error"):
            error_type = error_type[:-5]
        error_msg = str(error)
        result = f"🚫 Error {error_type}: {error_msg}\n"
        if "tidak ditemukan" in error_msg.lower():
            result += "\n💡 Tips: Pastikan variabel atau fungsi sudah dideklarasikan sebelum digunakan"
        elif "tidak dapat dipanggil" in error_msg.lower():
            result += (
                "\n💡 Tips: Pastikan objek yang dipanggil adalah fungsi atau metode"
            )
        elif "server" in error_msg.lower():
            result += "\n💡 Tips: Periksa apakah port sudah digunakan atau coba restart aplikasi"
        return result
    error_type = error.__class__.__name__
    if error_type.endswith("Error"):
        error_type = error_type[:-5]
    result = f"🚫 Error {error_type}: {error.message}\n"
    result += f"📍 Pada baris {error.line}, kolom {error.column}\n"
    code_to_use = (
        error.source_code
        if hasattr(error, "source_code") and error.source_code
        else source_code
    )
    if code_to_use:
        lines = code_to_use.split("\n")
        if 0 <= error.line - 1 < len(lines):
            line = lines[error.line - 1]
            result += f"\n{error.line} | {line}\n"
            pointer = " " * (len(str(error.line)) + 3 + error.column - 1) + "^"
            if error.column + 10 < len(line):
                pointer += "~" * min(len(line) - error.column, 10)
            result += pointer + "\n"
            context_lines = 2
            start_line = max(0, error.line - 1 - context_lines)
            end_line = min(len(lines), error.line - 1 + context_lines + 1)
            if start_line > 0:
                result += "...\n"
            for i in range(start_line, end_line):
                if i == error.line - 1:
                    continue
                result += f"{i + 1} | {lines[i]}\n"
            if end_line < len(lines):
                result += "...\n"
    result += "\n💡 Saran perbaikan:\n"
    if isinstance(error, LexerError):
        result += "- Periksa karakter yang tidak valid atau tidak dikenali\n"
        result += "- Pastikan string dan komentar ditutup dengan benar\n"
    elif isinstance(error, ParserError):
        result += "- Periksa sintaks dan tanda baca (kurung, koma, titik koma)\n"
        result += "- Pastikan semua blok kode ditutup dengan benar\n"
    elif isinstance(error, NameError):
        result += "- Pastikan variabel sudah dideklarasikan sebelum digunakan\n"
        result += "- Periksa ejaan nama variabel (huruf besar/kecil)\n"
    elif isinstance(error, TypeError):
        result += "- Pastikan tipe data yang digunakan sesuai dengan operasi\n"
        result += "- Periksa konversi tipe data jika diperlukan\n"
    elif isinstance(error, ValueError):
        result += "- Periksa nilai yang dimasukkan sesuai dengan yang diharapkan\n"
        result += "- Pastikan format nilai sudah benar\n"
    elif isinstance(error, ImportError):
        result += "- Pastikan modul yang diimpor tersedia dan dieja dengan benar\n"
        result += "- Periksa jalur impor dan dependensi\n"
    elif isinstance(error, AttributeError):
        result += "- Pastikan objek memiliki atribut atau metode yang dipanggil\n"
        result += "- Periksa ejaan nama atribut/metode\n"
    elif isinstance(error, IndexError):
        result += "- Pastikan indeks berada dalam rentang yang valid\n"
        result += "- Periksa panjang daftar atau string sebelum mengakses indeks\n"
    elif isinstance(error, KeyError):
        result += "- Pastikan kunci ada dalam kamus sebelum diakses\n"
        result += (
            "- Gunakan metode .get() untuk menghindari error jika kunci tidak ada\n"
        )
    elif isinstance(error, DivisionByZeroError):
        result += "- Hindari pembagian dengan nol\n"
        result += (
            "- Tambahkan pemeriksaan untuk nilai nol sebelum melakukan pembagian\n"
        )
    elif isinstance(error, FileError):
        result += "- Pastikan file ada dan dapat diakses\n"
        result += "- Periksa izin file dan jalur yang benar\n"
    elif isinstance(error, TypeHintError):
        result += "- Pastikan nilai sesuai dengan tipe data yang ditentukan\n"
        result += "- Periksa deklarasi tipe dan konversi nilai jika diperlukan\n"
    elif isinstance(error, SyntaxError):
        result += "- Periksa sintaks kode untuk kesalahan\n"
        result += "- Pastikan semua tanda kurung, koma, dan titik koma berada di tempat yang benar\n"
    else:
        result += "- Periksa kembali kode Anda untuk kesalahan\n"
        result += "- Pastikan semua nilai dan operasi sesuai dengan yang diharapkan\n"
    return result
