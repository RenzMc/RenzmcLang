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
RenzmcLang Error Module

This module defines all error types and error formatting functionality
for the RenzmcLang programming language.
"""

from renzmc.core.error_catalog import get_error_info, suggest_error_code  # noqa: E402


class RenzmcError(Exception):
    """Base exception class for all RenzmcLang errors."""

    def __init__(self, message, line=None, column=None, source_code=None):
        """
        Initialize a RenzmcError.

        Args:
            message: Error message describing what went wrong
            line: Line number where error occurred (optional)
            column: Column number where error occurred (optional)
            source_code: Source code text for context (optional)
        """
        self.message = message
        self.line = line
        self.column = column
        self.source_code = source_code
        if line is not None and column is not None:
            super().__init__(f"{message} (baris {line}, kolom {column})")
        else:
            super().__init__(message)


class LexerError(RenzmcError):
    """Error during lexical analysis (tokenization)."""


class ParserError(RenzmcError):
    """Error during parsing (syntax analysis)."""


class InterpreterError(RenzmcError):
    """Error during interpretation (runtime execution)."""


class RenzmcNameError(RenzmcError):
    """Error when a name/variable is not found."""


class RenzmcTypeError(RenzmcError):
    """Error when an operation receives wrong type."""


class RenzmcValueError(RenzmcError):
    """Error when a value is invalid or out of range."""


class RenzmcImportError(RenzmcError):
    """Error when importing modules fails."""


class RenzmcAttributeError(RenzmcError):
    """Error when accessing non-existent attribute."""


class RenzmcIndexError(RenzmcError):
    """Error when index is out of range."""


class RenzmcKeyError(RenzmcError):
    """Error when dictionary key is not found."""


class RenzmcRuntimeError(RenzmcError):
    """General runtime error."""


class DivisionByZeroError(RenzmcError):
    """Error when dividing by zero."""


class FileError(RenzmcError):
    """Error related to file operations."""


class PythonIntegrationError(RenzmcError):
    """Error when integrating with Python code."""


class RenzmcSyntaxError(RenzmcError):
    """Error in code syntax."""


class TypeHintError(RenzmcError):
    """Error related to type hints and type checking."""


class AsyncError(RenzmcError):
    """Error in asynchronous operations."""


def format_error(error, source_code=None):  # noqa: C901
    """
    Format error messages in a user-friendly and informative way.

    Args:
        error: The error object to format
        source_code: Optional source code for context

    Returns:
        Formatted error message string with helpful information
    """
    if isinstance(error, KeyboardInterrupt):
        return "✓ Program dihentikan oleh pengguna (Ctrl+C)"

    # Get error type and message
    error_type = error.__class__.__name__
    error_msg = str(error)

    # Try to get error code from catalog
    error_code = suggest_error_code(error_type, error_msg)
    error_info = get_error_info(error_code) if error_code else None

    # Format error type name
    display_type = error_type
    if display_type.endswith("Error"):
        display_type = display_type[:-5]

    # Build result string
    result = ""

    # Error header with code
    if error_code:
        result += f"🚫 Error [{error_code}] {display_type}\n"
        if error_info:
            result += f"📋 {error_info.title}\n"
    else:
        result += f"🚫 Error {display_type}\n"

    # Handle errors without line/column information
    if not hasattr(error, "line") or not hasattr(error, "column") or error.line is None or error.column is None:
        result += f"💬 {error_msg}\n"

        # Add quick tips for common errors
        if "tidak ditemukan" in error_msg.lower():
            result += "\n💡 Tips: Pastikan variabel atau fungsi sudah " "dideklarasikan sebelum digunakan"
        elif "tidak dapat dipanggil" in error_msg.lower():
            result += "\n💡 Tips: Pastikan objek yang dipanggil " "adalah fungsi atau metode"
        elif "server" in error_msg.lower():
            result += "\n💡 Tips: Periksa apakah port sudah digunakan " "atau coba restart aplikasi"

        # Add catalog solutions if available
        if error_info:
            result += "\n\n💡 Solusi:\n"
            for solution in error_info.solutions[:3]:  # Show top 3 solutions
                result += f"   {solution}\n"

            # Add examples if available
            if error_info.examples:
                result += "\n📝 Contoh:\n"
                for example in error_info.examples[:2]:  # Show first 2 examples
                    result += f"   {example}\n"

        return result

    # Error with line/column information
    message = error.message if hasattr(error, "message") else error_msg
    result += f"💬 {message}\n"
    result += f"📍 Lokasi: Baris {error.line}, Kolom {error.column}\n"

    # Source code context
    code_to_use = error.source_code if hasattr(error, "source_code") and error.source_code else source_code

    if code_to_use:
        lines = code_to_use.split("\n")
        if 0 <= error.line - 1 < len(lines):
            # Show error line with pointer
            line = lines[error.line - 1]
            result += f"\n{error.line:4d} | {line}\n"
            pointer = " " * (7 + error.column - 1) + "^"
            if error.column + 10 < len(line):
                pointer += "~" * min(len(line) - error.column, 10)
            result += pointer + "\n"

            # Show context lines
            context_lines = 2
            start_line = max(0, error.line - 1 - context_lines)
            end_line = min(len(lines), error.line - 1 + context_lines + 1)

            if start_line > 0:
                result += "     ...\n"

            for i in range(start_line, end_line):
                if i == error.line - 1:
                    continue
                result += f"{i + 1:4d} | {lines[i]}\n"

            if end_line < len(lines):
                result += "     ...\n"

    # Solutions section
    result += "\n💡 Solusi:\n"

    if error_info:
        # Use catalog solutions
        for solution in error_info.solutions:
            result += f"   {solution}\n"

        # Add examples if available
        if error_info.examples:
            result += "\n📝 Contoh:\n"
            for example in error_info.examples:
                result += f"   {example}\n"

        # Add related errors if available
        if error_info.related_errors:
            result += "\n🔗 Error Terkait:\n"
            for related_code in error_info.related_errors[:3]:
                related_info = get_error_info(related_code)
                if related_info:
                    result += f"   • [{related_code}] {related_info.title}\n"

        # Add documentation link if available
        if error_info.doc_link:
            result += f"\n📚 Dokumentasi: {error_info.doc_link}\n"
    else:
        # Fallback to legacy solutions
        error_solutions = _get_error_solutions(error)
        for solution in error_solutions:
            result += f"   {solution}\n"

    return result


def _get_error_solutions(error):  # noqa: C901
    """
    Get specific solutions for different error types.

    Args:
        error: The error object

    Returns:
        List of solution strings
    """
    solutions = []

    if isinstance(error, LexerError):
        solutions.extend(
            [
                "• Periksa karakter yang tidak valid atau tidak dikenali",
                "• Pastikan string ditutup dengan tanda kutip yang sesuai",
                "• Pastikan komentar ditutup dengan benar",
                "• Periksa penggunaan karakter khusus yang tidak didukung",
            ]
        )
    elif isinstance(error, ParserError):
        # Check if this is a reserved keyword error
        error_msg = str(error.message) if hasattr(error, "message") else str(error)
        if "tidak dapat digunakan sebagai nama variabel" in error_msg or "reserved keyword" in error_msg.lower():
            # This is a reserved keyword error - the message already has the solution
            pass  # Don't add generic solutions
        else:
            solutions.extend(
                [
                    "• Periksa tanda kurung, kurung kurawal, dan kurung siku",
                    "• Pastikan setiap 'jika' memiliki 'selesai' yang sesuai",
                    "• Periksa penggunaan koma dan titik koma",
                    "• Pastikan struktur blok kode sudah benar",
                ]
            )
    elif isinstance(error, (RenzmcNameError, type(None))):
        if isinstance(error, RenzmcNameError) or "NameError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan variabel sudah dideklarasikan sebelum digunakan",
                    "• Periksa ejaan nama variabel (case-sensitive)",
                    "• Pastikan variabel berada dalam scope yang benar",
                    "• Cek apakah variabel dideklarasikan di dalam blok yang tepat",
                ]
            )
    elif isinstance(error, (RenzmcTypeError, type(None))):
        if isinstance(error, RenzmcTypeError) or "TypeError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan tipe data sesuai dengan operasi yang dilakukan",
                    "• Gunakan konversi tipe jika diperlukan (ke_angka, ke_teks)",
                    "• Periksa apakah fungsi menerima argumen dengan tipe yang benar",
                    "• Pastikan operasi matematika hanya dilakukan pada angka",
                ]
            )
    elif isinstance(error, (RenzmcValueError, type(None))):
        if isinstance(error, RenzmcValueError) or "ValueError" in str(type(error)):
            solutions.extend(
                [
                    "• Periksa nilai yang dimasukkan sesuai dengan yang diharapkan",
                    "• Pastikan format nilai sudah benar",
                    "• Periksa rentang nilai yang valid",
                    "• Validasi input sebelum digunakan",
                ]
            )
    elif isinstance(error, (RenzmcImportError, type(None))):
        if isinstance(error, RenzmcImportError) or "ImportError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan modul yang diimpor tersedia",
                    "• Periksa ejaan nama modul",
                    "• Pastikan modul sudah terinstall",
                    "• Periksa jalur impor dan dependensi",
                ]
            )
    elif isinstance(error, (RenzmcAttributeError, type(None))):
        if isinstance(error, RenzmcAttributeError) or "AttributeError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan objek memiliki atribut yang dipanggil",
                    "• Periksa ejaan nama atribut/metode",
                    "• Pastikan objek sudah diinisialisasi dengan benar",
                    "• Cek dokumentasi untuk atribut yang tersedia",
                ]
            )
    elif isinstance(error, (RenzmcIndexError, type(None))):
        if isinstance(error, RenzmcIndexError) or "IndexError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan indeks berada dalam rentang yang valid",
                    "• Periksa panjang daftar sebelum mengakses indeks",
                    "• Ingat: indeks dimulai dari 0",
                    "• Gunakan len() untuk memeriksa panjang daftar",
                ]
            )
    elif isinstance(error, (RenzmcKeyError, type(None))):
        if isinstance(error, RenzmcKeyError) or "KeyError" in str(type(error)):
            solutions.extend(
                [
                    "• Pastikan kunci ada dalam kamus sebelum diakses",
                    "• Gunakan metode .get() untuk menghindari error",
                    "• Periksa ejaan kunci (case-sensitive)",
                    "• Gunakan 'dalam' untuk memeriksa keberadaan kunci",
                ]
            )
    elif isinstance(error, DivisionByZeroError):
        solutions.extend(
            [
                "• Hindari pembagian dengan nol",
                "• Tambahkan pemeriksaan sebelum pembagian",
                "• Gunakan kondisi: jika pembagi != 0",
                "• Pertimbangkan nilai default jika pembagi nol",
            ]
        )
    elif isinstance(error, FileError):
        solutions.extend(
            [
                "• Pastikan file ada dan dapat diakses",
                "• Periksa izin file (read/write permissions)",
                "• Pastikan jalur file sudah benar",
                "• Gunakan jalur absolut jika diperlukan",
            ]
        )
    elif isinstance(error, TypeHintError):
        solutions.extend(
            [
                "• Pastikan nilai sesuai dengan tipe yang ditentukan",
                "• Periksa deklarasi tipe pada variabel/fungsi",
                "• Gunakan konversi tipe jika diperlukan",
                "• Pastikan tipe hint konsisten di seluruh kode",
            ]
        )
    elif isinstance(error, (RenzmcSyntaxError, type(None))):
        if isinstance(error, RenzmcSyntaxError) or "SyntaxError" in str(type(error)):
            solutions.extend(
                [
                    "• Periksa sintaks kode untuk kesalahan",
                    "• Pastikan tanda kurung seimbang",
                    "• Periksa penggunaan kata kunci yang benar",
                    "• Pastikan struktur kode sesuai dengan aturan bahasa",
                ]
            )
    elif isinstance(error, AsyncError):
        solutions.extend(
            [
                "• Pastikan fungsi async dipanggil dengan 'tunggu'",
                "• Periksa penggunaan async/await yang benar",
                "• Pastikan event loop berjalan dengan baik",
                "• Gunakan 'asinkron' untuk mendefinisikan fungsi async",
            ]
        )
    else:
        solutions.extend(
            [
                "• Periksa kembali kode Anda untuk kesalahan",
                "• Pastikan semua nilai dan operasi sesuai",
                "• Coba jalankan kode secara bertahap untuk menemukan masalah",
                "• Periksa dokumentasi untuk penggunaan yang benar",
            ]
        )

    return solutions
