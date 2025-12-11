#!/usr/bin/env python3
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

import argparse
import os
import sys

from renzmc.core.ast_cache import ASTCache
from renzmc.core.error import format_error
from renzmc.core.error_logger import log_error
from renzmc.core.interpreter import Interpreter
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.utils.linter import RenzmcLinter
from renzmc.utils.formater import RenzmcFormatter
from renzmc.version import __version__

# Global AST cache instance
_ast_cache = ASTCache()


def run_file(filename, use_cache=True):
    """
    Execute a RenzmcLang file.

    Args:
        filename: Path to the .rmc file to execute
        use_cache: Whether to use AST caching (default: True)
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            source_code = f.read()
        return run_code(source_code, filename, use_cache=use_cache)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


def run_code(source_code, filename="<stdin>", interpreter=None, use_cache=True):
    """
    Execute RenzmcLang source code.

    Args:
        source_code: The source code string to execute
        filename: Name of the source file (for error reporting)
        interpreter: Optional existing interpreter instance
        use_cache: Whether to use AST caching (default: True)

    Returns:
        The interpreter instance after execution
    """
    try:
        if interpreter is None:
            interpreter = Interpreter()

        # Set the current file path for relative imports
        if filename != "<stdin>":
            interpreter.current_file = os.path.abspath(filename)

        # Try to load cached AST if caching is enabled and not stdin
        ast = None
        if use_cache and filename != "<stdin>":
            cache_key = _ast_cache.get_cache_key(source_code)
            ast = _ast_cache.load(cache_key)

        # Parse if no cached AST found
        if ast is None:
            lexer = Lexer(source_code)
            parser = Parser(lexer)
            ast = parser.parse()

            # Cache the AST if caching is enabled and not stdin
            if use_cache and filename != "<stdin>":
                cache_key = _ast_cache.get_cache_key(source_code)
                _ast_cache.save(cache_key, ast)

        # Use Rust-aware execution (automatic)
        if hasattr(interpreter, "visit_with_rust"):
            interpreter.visit_with_rust(ast)
        else:
            interpreter.visit(ast)

        return interpreter
    except Exception as e:
        # Log error to file with full context
        log_error(
            error=e,
            source_code=source_code,
            filename=filename,
            context={
                "interpreter_state": "parsing" if interpreter is None else "executing",
                "file_type": "stdin" if filename == "<stdin>" else "file",
            },
        )

        # Print formatted error to console
        print(format_error(e, source_code))

        if filename != "<stdin>":
            sys.exit(1)
        return interpreter


def run_interactive():
    """Start the interactive REPL (Read-Eval-Print Loop)."""
    from renzmc.repl import RenzmcREPL

    repl = RenzmcREPL()
    repl.run()


def lint_file(filename):
    """Lint a RenzmcLang file and display results."""
    try:
        print(f"🔍 Memeriksa file: {filename}")
        linter = RenzmcLinter()
        messages = linter.lint_file(filename)

        if not messages:
            print("✅ Tidak ada masalah yang ditemukan!")
            return

        errors = linter.get_errors()
        warnings = linter.get_warnings()
        info = linter.get_info()

        if errors:
            print(f"\n❌ Ditemukan {len(errors)} error:")
            for error in errors:
                print(f"  {error}")

        if warnings:
            print(f"\n⚠️  Ditemukan {len(warnings)} warning:")
            for warning in warnings:
                print(f"  {warning}")

        if info:
            print(f"\nℹ️  Informasi ({len(info)}):")
            for msg in info:
                print(f"  {msg}")

        if errors:
            print(f"\n💡 Gunakan --format untuk memperbaiki beberapa masalah secara otomatis")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error saat linting: {str(e)}")
        sys.exit(1)


def format_file(filename, save_changes=False):
    """Format a RenzmcLang file."""
    try:
        print(f"📝 Memformat file: {filename}")

        with open(filename, "r", encoding="utf-8") as f:
            original_code = f.read()

        formatter = RenzmcFormatter()
        formatted_code = formatter.format_code(original_code)

        if original_code == formatted_code:
            print("✅ File sudah diformat dengan benar!")
            return

        print("🔧 Perubahan yang akan dilakukan:")

        original_lines = original_code.split("\n")
        formatted_lines = formatted_code.split("\n")

        changes_count = 0
        for i, (orig, fmt) in enumerate(zip(original_lines, formatted_lines)):
            if orig != fmt:
                changes_count += 1
                print(f"  Baris {i+1}:")
                print(f"    - {orig}")
                print(f"    + {fmt}")

        if len(original_lines) != len(formatted_lines):
            changes_count += abs(len(original_lines) - len(formatted_lines))
            print(f"  Jumlah baris berubah: {len(original_lines)} → {len(formatted_lines)}")

        print(f"\n📊 Total {changes_count} perubahan")

        if save_changes:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(formatted_code)
            print(f"💾 File {filename} berhasil disimpan!")
        else:
            print("💡 Gunakan --fix untuk menyimpan perubahan ke file")
            print("\n📄 Hasil format:")
            print("-" * 50)
            print(formatted_code)
            print("-" * 50)

    except Exception as e:
        print(f"❌ Error saat formatting: {str(e)}")
        sys.exit(1)


def main():
    """Main entry point for the RenzmcLang CLI."""
    parser = argparse.ArgumentParser(
        prog="rmc",
        description="RenzmcLang - Bahasa pemrograman berbasis Bahasa Indonesia",
        epilog="Untuk dokumentasi lengkap, kunjungi: https://github.com/RenzMc/RenzmcLang",
    )
    parser.add_argument("file", nargs="?", help="File RenzmcLang (.rmc) untuk dijalankan")
    parser.add_argument(
        "-v",
        "--version",
        "--versi",
        "--ver",
        action="store_true",
        help="Tampilkan versi RenzmcLang",
    )
    parser.add_argument(
        "-c",
        "--code",
        "--kode",
        help="Jalankan kode RenzmcLang langsung dari command line",
    )
    parser.add_argument(
        "-b", "--bantuan", action="help", help="Tampilkan pesan bantuan ini dan keluar"
    )
    parser.add_argument(
        "--hapussampaherror",
        action="store_true",
        help="Hapus semua error log files dari direktori error_logs",
    )
    parser.add_argument(
        "--no-cache",
        "--tanpa-cache",
        action="store_true",
        help="Nonaktifkan AST caching untuk eksekusi ini (berguna untuk debugging)",
    )
    parser.add_argument(
        "--hapuscache",
        "--clear-cache",
        action="store_true",
        help="Hapus semua cache AST files dari direktori .rmc_cache",
    )
    parser.add_argument(
        "--lint",
        action="store_true",
        help="Periksa kode RenzmcLang dengan linter",
    )
    parser.add_argument(
        "--format",
        action="store_true",
        help="Format kode RenzmcLang sesuai standar",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Format dan simpan perubahan ke file (gunakan dengan --format)",
    )

    args = parser.parse_args()

    if args.version:
        print(f"RenzmcLang {__version__}")
        return

    if args.hapussampaherror:
        from renzmc.core.error_logger import clear_error_logs, get_error_logs_dir

        error_logs_dir = get_error_logs_dir()
        print(f"🗑️  Menghapus error logs dari: {error_logs_dir}")
        print("⏳ Mohon tunggu...")

        deleted_count = clear_error_logs()

        if deleted_count > 0:
            print(f"✅ Berhasil menghapus {deleted_count} error log file(s)")
        else:
            print("ℹ️  Tidak ada error log yang perlu dihapus")
        return

    if args.hapuscache:
        import shutil

        cache_dir = _ast_cache.cache_dir
        if os.path.exists(cache_dir):
            print(f"🗑️  Menghapus AST cache dari: {cache_dir}")
            print("⏳ Mohon tunggu...")
            try:
                shutil.rmtree(cache_dir)
                print("✅ Berhasil menghapus AST cache")
            except Exception as e:
                print(f"❌ Gagal menghapus cache: {e}")
        else:
            print("ℹ️  Tidak ada cache yang perlu dihapus")
        return

    # Handle linting
    if args.lint:
        if args.file:
            lint_file(args.file)
        else:
            print("Error: --lint memerlukan file yang akan diperiksa")
            sys.exit(1)
        return

    # Handle formatting
    if args.format:
        if args.file:
            format_file(args.file, args.fix)
        else:
            print("Error: --format memerlukan file yang akan diformat")
            sys.exit(1)
        return

    # Determine if caching should be used
    use_cache = not args.no_cache

    if args.code:
        run_code(args.code, use_cache=False)
    elif args.file:
        run_file(args.file, use_cache=use_cache)
    else:
        run_interactive()


if __name__ == "__main__":
    main()
