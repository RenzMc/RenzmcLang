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
    from renzmc.repl import RenzmcREPL
    repl = RenzmcREPL()
    repl.run()


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
