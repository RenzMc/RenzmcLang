import os
import sys
import argparse
import readline
import atexit
from pathlib import Path
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.interpreter import Interpreter
from renzmc.core.error import format_error
from renzmc.version import __version__

HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".renzmc_history")


def run_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            source_code = f.read()
        run_code(source_code, filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


def run_code(source_code, filename="<stdin>", interpreter=None):
    try:
        lexer = Lexer(source_code)
        if interpreter is None:
            interpreter = Interpreter()
        parser = Parser(lexer)
        ast = parser.parse()
        result = interpreter.visit(ast)
        return interpreter
    except Exception as e:
        print(format_error(e, source_code))
        if not filename == "<stdin>":
            sys.exit(1)
        return interpreter


def run_interactive():
    try:
        readline.parse_and_bind("tab: complete")
        if not os.path.exists(HISTORY_FILE):
            open(HISTORY_FILE, "a").close()
        readline.read_history_file(HISTORY_FILE)
        atexit.register(readline.write_history_file, HISTORY_FILE)
    except (ImportError, IOError):
        pass
    print(f"RenzmcLang {__version__} - Bahasa pemrograman berbasis Bahasa Indonesia")
    print("Ketik 'keluar' untuk keluar dari interpreter.")
    print("Untuk kode multi-baris, akhiri dengan baris kosong.")
    print()
    interpreter = Interpreter()
    block_keywords = [
        "jika",
        "kalau",
        "selama",
        "untuk",
        "ulangi",
        "fungsi",
        "kelas",
        "coba",
        "tangkap",
        "akhirnya",
        "dengan",
        "async",
        "def",
    ]
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() == "keluar":
                break
            needs_continuation = False
            first_word = line.strip().split()[0] if line.strip() else ""
            if first_word in block_keywords:
                needs_continuation = True
            open_parens = line.count("(") - line.count(")")
            open_brackets = line.count("[") - line.count("]")
            open_braces = line.count("{") - line.count("}")
            single_quotes = line.count("'") - line.count("\\'")
            double_quotes = line.count('"') - line.count("\\&quot;")
            if (
                open_parens > 0
                or open_brackets > 0
                or open_braces > 0
                or (single_quotes % 2 != 0)
                or (double_quotes % 2 != 0)
            ):
                needs_continuation = True
            if line.rstrip().endswith(":"):
                needs_continuation = True
            if needs_continuation:
                lines = [line]
                while True:
                    try:
                        continuation = input("... ")
                        if not continuation.strip():
                            break
                        lines.append(continuation)
                        open_parens += continuation.count("(") - continuation.count(")")
                        open_brackets += continuation.count("[") - continuation.count(
                            "]"
                        )
                        open_braces += continuation.count("{") - continuation.count("}")
                        if (
                            open_parens <= 0
                            and open_brackets <= 0
                            and (open_braces <= 0)
                            and (not continuation.rstrip().endswith(":"))
                        ):
                            pass
                    except EOFError:
                        break
                code = "\n".join(lines)
            else:
                code = line
            if code.strip():
                interpreter = run_code(code, interpreter=interpreter)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            break
        except Exception as e:
            print(f"Error: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="RenzmcLang - Bahasa pemrograman berbasis Bahasa Indonesia"
    )
    parser.add_argument("file", nargs="?", help="File RenzmcLang untuk dijalankan")
    parser.add_argument(
        "-v", "--version", action="store_true", help="Tampilkan versi RenzmcLang"
    )
    parser.add_argument("-c", "--code", help="Jalankan kode RenzmcLang")
    args = parser.parse_args()
    if args.version:
        print(f"RenzmcLang {__version__}")
        return
    if args.code:
        run_code(args.code)
    elif args.file:
        run_file(args.file)
    else:
        run_interactive()


if __name__ == "__main__":
    main()
