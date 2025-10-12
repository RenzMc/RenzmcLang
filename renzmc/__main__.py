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
RenzmcLang Main Entry Point

This module provides the command-line interface for running RenzmcLang programs.
"""

import argparse
import sys

from renzmc.core.error import format_error
from renzmc.core.interpreter import Interpreter
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.version import __version__


def run_file(filename):
    """
    Execute a RenzmcLang file.

    Args:
        filename: Path to the .rmc file to execute
    """
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
    """
    Execute RenzmcLang source code.

    Args:
        source_code: The source code string to execute
        filename: Name of the source file (for error reporting)
        interpreter: Optional existing interpreter instance

    Returns:
        The interpreter instance after execution
    """
    try:
        lexer = Lexer(source_code)
        if interpreter is None:
            interpreter = Interpreter()

        # Set the current file path for relative imports
        if filename != "<stdin>":
            import os

            interpreter.current_file = os.path.abspath(filename)

        parser = Parser(lexer)
        ast = parser.parse()
        interpreter.visit(ast)
        return interpreter
    except Exception as e:
        print(format_error(e, source_code))
        if filename != "<stdin>":
            sys.exit(1)
        return interpreter


def run_interactive():
    """Start the interactive REPL (Read-Eval-Print Loop)."""
    from renzmc.repl import RenzmcREPL

    repl = RenzmcREPL()
    repl.run()


def main():
    """Main entry point for the RenzmcLang CLI."""
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
