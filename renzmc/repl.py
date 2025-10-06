""" REPL (Read-Eval-Print Loop) untuk RenzMcLang
Interactive shell dengan fitur modern seperti Python REPL
"""

import sys
import os
import readline
import atexit
from typing import List, Optional
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.interpreter import Interpreter
from renzmc.core.error import RenzmcError
from renzmc.version import __version__

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'


class RenzmcREPL:

    KEYWORDS = [
        'jika', 'kalau', 'selama', 'untuk', 'fungsi', 'kelas', 'coba',
        'cocok', 'dengan', 'selesai', 'akhir', 'kembalikan', 'lanjut',
        'berhenti', 'dan', 'atau', 'bukan', 'dalam', 'adalah', 'impor',
        'dari', 'sebagai', 'global', 'nonlokal', 'lewati', 'tegas',
        'tangkap', 'akhirnya', 'lempar', 'async', 'await'
    ]

    BUILTINS = [
        'cetak', 'masukan', 'panjang', 'tipe', 'str', 'int', 'float',
        'bool', 'list', 'dict', 'set', 'tuple', 'range', 'enumerate',
        'zip', 'map', 'filter', 'sum', 'min', 'max', 'abs', 'round',
        'sorted', 'reversed', 'all', 'any', 'open', 'baca', 'tulis'
    ]

    def __init__(self):
        self.interpreter = Interpreter()
        self.history = []
        self.multiline_buffer = []
        self.in_multiline = False
        self.line_number = 1
        self.history_file = os.path.expanduser('~/.renzmc_history')

        self._setup_readline()

    def _setup_readline(self):
        try:
            if os.path.exists(self.history_file):
                readline.read_history_file(self.history_file)

            readline.set_history_length(1000)

            atexit.register(self._save_history)

            readline.set_completer(self._completer)
            readline.parse_and_bind('tab: complete')

            readline.parse_and_bind('set editing-mode emacs')

        except Exception:
            pass

    def _save_history(self):
        try:
            readline.write_history_file(self.history_file)
        except Exception:
            pass

    def _completer(self, text: str, state: int) -> Optional[str]:
        options = []

        options.extend([kw for kw in self.KEYWORDS if kw.startswith(text)])

        options.extend([bf for bf in self.BUILTINS if bf.startswith(text)])

        if hasattr(self.interpreter, 'global_scope'):
            options.extend([
                var for var in self.interpreter.global_scope.keys()
                if var.startswith(text) and not var.startswith('__')
            ])

        try:
            return options[state]
        except IndexError:
            return None

    def _colorize(self, text: str, color: str) -> str:
        return f"{color}{text}{Colors.RESET}"

    def _syntax_highlight(self, code: str) -> str:
        result = code

        for keyword in self.KEYWORDS:
            result = result.replace(
                f" {keyword} ",
                f" {self._colorize(keyword, Colors.BRIGHT_MAGENTA)} "
            )
            if result.startswith(keyword + " "):
                result = self._colorize(keyword, Colors.BRIGHT_MAGENTA) + result[len(keyword):]

        for builtin in self.BUILTINS:
            result = result.replace(
                f"{builtin}(",
                f"{self._colorize(builtin, Colors.BRIGHT_BLUE)}("
            )

        return result

    def print_banner(self):
        banner = f"""
{Colors.BRIGHT_CYAN}RenzMcLang {Colors.BRIGHT_YELLOW}v{__version__}{Colors.RESET}
{Colors.BRIGHT_GREEN}Selamat datang di RenzMcLang Interactive Shell!{Colors.RESET}

{Colors.YELLOW}Ketik 'bantuan' untuk melihat perintah | 'keluar' untuk keluar{Colors.RESET}
"""
        print(banner)

    def print_help(self):
        help_text = f"""
{Colors.BRIGHT_CYAN}📚 Perintah REPL:{Colors.RESET}
  {Colors.GREEN}bantuan{Colors.RESET}      - Tampilkan pesan bantuan ini
  {Colors.GREEN}keluar{Colors.RESET}       - Keluar dari REPL
  {Colors.GREEN}bersih{Colors.RESET}       - Bersihkan layar
  {Colors.GREEN}riwayat{Colors.RESET}      - Tampilkan riwayat perintah
  {Colors.GREEN}reset{Colors.RESET}        - Reset interpreter (hapus semua variabel)
  {Colors.GREEN}variabel{Colors.RESET}     - Tampilkan semua variabel yang ada
  {Colors.GREEN}inspect{Colors.RESET} <var> - Inspect variabel dengan detail
  {Colors.GREEN}tipe{Colors.RESET} <var>    - Tampilkan tipe variabel
     {Colors.GREEN}jit{Colors.RESET}          - Tampilkan statistik JIT compilation

{Colors.BRIGHT_CYAN}💡 Tips:{Colors.RESET}
  • Gunakan {Colors.YELLOW}Tab{Colors.RESET} untuk auto-completion
  • Gunakan {Colors.YELLOW}↑/↓{Colors.RESET} untuk navigasi history
  • Gunakan {Colors.YELLOW}←/→{Colors.RESET} untuk edit baris
  • Gunakan {Colors.YELLOW}'selesai'{Colors.RESET} untuk mengakhiri blok multiline
  • Tekan {Colors.YELLOW}Enter dua kali{Colors.RESET} untuk mengeksekusi blok multiline
  • Gunakan {Colors.YELLOW}Ctrl+C{Colors.RESET} untuk membatalkan input
  • Gunakan {Colors.YELLOW}f-string{Colors.RESET} untuk string interpolation: f"Nilai: {{x}}"
"""
        print(help_text)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_history(self):
        if not self.history:
            print(f"{Colors.YELLOW}Tidak ada riwayat perintah{Colors.RESET}")
            return

        print(f"\n{Colors.BRIGHT_CYAN}📜 Riwayat Perintah:{Colors.RESET}")
        for i, cmd in enumerate(self.history[-20:], max(1, len(self.history) - 19)):
            cmd_preview = cmd[:60] + ('...' if len(cmd) > 60 else '')
            print(f"  {Colors.BRIGHT_BLACK}{i:3d}{Colors.RESET} │ {cmd_preview}")
        print()

    def show_variables(self):
        if not hasattr(self.interpreter, 'global_scope') or not self.interpreter.global_scope:
            print(f"{Colors.YELLOW}Tidak ada variabel yang didefinisikan{Colors.RESET}")
            return

        print(f"\n{Colors.BRIGHT_CYAN}📦 Variabel yang Didefinisikan:{Colors.RESET}")
        for name, value in sorted(self.interpreter.global_scope.items()):
            if not name.startswith('__'):
                value_str = str(value)
                value_type = type(value).__name__

                if len(value_str) > 50:
                    value_str = value_str[:50] + "..."

                print(f"  {Colors.GREEN}{name}{Colors.RESET} : {Colors.CYAN}{value_type}{Colors.RESET} = {Colors.YELLOW}{value_str}{Colors.RESET}")
        print()

    def inspect_variable(self, var_name: str):
        if not hasattr(self.interpreter, 'global_scope'):
            print(f"{Colors.RED}Error: Tidak ada scope yang tersedia{Colors.RESET}")
            return

        if var_name not in self.interpreter.global_scope:
            print(f"{Colors.RED}Error: Variabel '{var_name}' tidak ditemukan{Colors.RESET}")
            return

        value = self.interpreter.global_scope[var_name]
        value_type = type(value).__name__

        print(f"\n{Colors.BRIGHT_CYAN}🔍 Inspeksi Variabel: {Colors.GREEN}{var_name}{Colors.RESET}")
        print(f"{Colors.CYAN}Tipe:{Colors.RESET} {value_type}")
        print(f"{Colors.CYAN}Nilai:{Colors.RESET} {value}")

        if hasattr(value, '__len__'):
            print(f"{Colors.CYAN}Panjang:{Colors.RESET} {len(value)}")

        if hasattr(value, '__dict__'):
            print(f"{Colors.CYAN}Atribut:{Colors.RESET}")
            for attr in dir(value):
                if not attr.startswith('_'):
                    print(f"  • {attr}")

        print()

    def reset_interpreter(self):
        self.interpreter = Interpreter()
        self.line_number = 1
        print(f"{Colors.GREEN}✅ Interpreter direset (semua variabel dihapus){Colors.RESET}")

    def is_multiline_start(self, line: str) -> bool:
        multiline_keywords = [
            'jika', 'kalau', 'selama', 'untuk', 'fungsi',
            'kelas', 'coba', 'cocok', 'dengan'
        ]

        stripped = line.strip()
        for keyword in multiline_keywords:
            if stripped.startswith(keyword):
                return True
        return False

    def is_multiline_end(self, line: str) -> bool:
        return line.strip() in ['selesai', 'akhir']

    def get_indent_level(self, line: str) -> int:
        return len(line) - len(line.lstrip())

    def execute_code(self, code: str) -> bool:
        try:
            lexer = Lexer(code)

            parser = Parser(lexer)
            ast = parser.parse()

            result = self.interpreter.interpret(ast)

            if result is not None and result != '':
                print(f"{Colors.BRIGHT_WHITE}{result}{Colors.RESET}")

            return True

        except RenzmcError as e:
            self._print_enhanced_error(e, code)
            return False
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}KeyboardInterrupt{Colors.RESET}")
            return False
        except Exception as e:
            print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.RESET}")
            import traceback
            traceback.print_exc()
            return False

    def _print_enhanced_error(self, error: RenzmcError, source_code: str):
        error_type = error.__class__.__name__

        print(f"\n{Colors.BRIGHT_RED}Traceback (most recent call last):{Colors.RESET}")

        code_to_use = error.source_code if hasattr(error, 'source_code') and error.source_code else source_code

        if code_to_use and hasattr(error, 'line') and error.line is not None:
            lines = code_to_use.split('\n')
            if 0 <= error.line - 1 < len(lines):
                filename = getattr(error, 'filename', '<stdin>')
                print(f'  File "{filename}", line {error.line}')

                line_content = lines[error.line - 1]
                print(f"    {line_content}")

                if hasattr(error, 'column') and error.column is not None:
                    pointer_padding = ' ' * (error.column + 3)
                    pointer_length = max(1, min(10, len(line_content) - error.column + 1))
                    pointer = '^' * pointer_length
                    print(f"{pointer_padding}{Colors.BRIGHT_RED}{pointer}{Colors.RESET}")

        print(f"{Colors.BRIGHT_RED}{error_type}: {Colors.RESET}{error.message}")

        suggestions = self._get_error_suggestions(error)
        if suggestions:
            print(f"\n{Colors.BRIGHT_YELLOW}Suggestions:{Colors.RESET}")
            for suggestion in suggestions:
                print(f"  • {suggestion}")

        print()

    def _get_error_suggestions(self, error: RenzmcError) -> List[str]:
        error_type = error.__class__.__name__
        error_msg = str(error.message).lower() if hasattr(error, 'message') else str(error).lower()
        suggestions = []

        if 'NameError' in error_type:
            suggestions.extend([
                "Pastikan variabel sudah dideklarasikan sebelum digunakan",
                "Periksa ejaan nama variabel (case-sensitive)",
                "Gunakan 'variabel' untuk melihat semua variabel yang tersedia"
            ])
            if 'tidak ditemukan' in error_msg or 'not found' in error_msg:
                suggestions.append("Mungkin ada typo dalam nama variabel?")

        elif 'TypeError' in error_type:
            suggestions.extend([
                "Pastikan tipe data sesuai dengan operasi yang dilakukan",
                "Gunakan konversi tipe: int(), str(), float(), list(), dll",
                "Periksa apakah objek dapat dipanggil (callable)"
            ])
            if 'tidak dapat' in error_msg or 'cannot' in error_msg:
                suggestions.append("Periksa dokumentasi fungsi untuk tipe parameter yang benar")

        elif 'SyntaxError' in error_type or 'ParserError' in error_type:
            suggestions.extend([
                "Periksa tanda kurung, kurung kurawal, dan tanda kutip yang berpasangan",
                "Pastikan blok kode ditutup dengan 'selesai' atau 'akhir'",
                "Periksa indentasi - gunakan spasi atau tab secara konsisten",
                "Periksa operator dan tanda baca yang valid"
            ])
            if 'unexpected' in error_msg:
                suggestions.append("Token tidak diharapkan - periksa sintaks sebelum posisi error")

        elif 'IndexError' in error_type:
            suggestions.extend([
                "Indeks list dimulai dari 0, bukan 1",
                "Gunakan len(list) untuk memeriksa panjang sebelum akses",
                "Gunakan try-except untuk menangani indeks yang tidak valid",
                "Periksa apakah list kosong sebelum mengakses elemen"
            ])

        elif 'KeyError' in error_type:
            suggestions.extend([
                "Gunakan 'kunci in dict' untuk memeriksa keberadaan kunci",
                "Gunakan dict.get(kunci, default) untuk nilai default",
                "Periksa ejaan kunci (case-sensitive)",
                "Gunakan dict.keys() untuk melihat semua kunci"
            ])

        elif 'DivisionByZero' in error_type or 'ZeroDivision' in error_type:
            suggestions.extend([
                "Tambahkan pengecekan: jika pembagi != 0 maka ...",
                "Gunakan try-except untuk menangani pembagian dengan nol",
                "Periksa nilai variabel sebelum operasi pembagian"
            ])

        elif 'ValueError' in error_type:
            suggestions.extend([
                "Periksa format dan nilai input",
                "Pastikan konversi tipe data valid (contoh: int('abc') akan error)",
                "Validasi input sebelum diproses",
                "Gunakan try-except untuk menangani nilai yang tidak valid"
            ])

        elif 'AttributeError' in error_type:
            suggestions.extend([
                "Periksa apakah objek memiliki atribut/metode tersebut",
                "Gunakan dir(objek) untuk melihat atribut yang tersedia",
                "Periksa ejaan nama atribut/metode",
                "Pastikan objek sudah diinisialisasi dengan benar"
            ])

        elif 'ImportError' in error_type or 'ModuleNotFound' in error_type:
            suggestions.extend([
                "Pastikan modul sudah diinstall",
                "Periksa ejaan nama modul",
                "Gunakan 'pip install nama_modul' untuk install modul Python",
                "Periksa path modul jika menggunakan modul lokal"
            ])

        elif 'FileError' in error_type or 'FileNotFound' in error_type:
            suggestions.extend([
                "Periksa apakah file ada di lokasi yang benar",
                "Gunakan path absolut atau relatif yang benar",
                "Periksa permission file (read/write)",
                "Pastikan nama file dan ekstensi benar"
            ])

        elif 'RuntimeError' in error_type:
            suggestions.extend([
                "Periksa logika program untuk infinite loop atau rekursi",
                "Pastikan semua resource (file, connection) ditutup dengan benar",
                "Periksa kondisi yang menyebabkan error saat runtime"
            ])

        elif 'RecursionError' in error_type:
            suggestions.extend([
                "Tambahkan base case untuk menghentikan rekursi",
                "Periksa apakah kondisi berhenti dapat tercapai",
                "Pertimbangkan menggunakan iterasi daripada rekursi",
                "Tingkatkan recursion limit jika memang diperlukan"
            ])

        elif 'MemoryError' in error_type:
            suggestions.extend([
                "Kurangi ukuran data yang diproses",
                "Gunakan generator untuk data besar",
                "Proses data secara batch/chunk",
                "Periksa memory leak dalam kode"
            ])

        elif 'Async' in error_type:
            suggestions.extend([
                "Pastikan fungsi async dipanggil dengan 'await'",
                "Gunakan 'async def' untuk mendefinisikan fungsi async",
                "Jalankan dalam event loop yang benar",
                "Periksa dokumentasi async/await"
            ])

        else:
            suggestions.extend([
                "Baca pesan error dengan teliti untuk memahami masalahnya",
                "Gunakan 'bantuan' untuk dokumentasi",
                "Coba jalankan kode secara bertahap untuk isolasi masalah",
                "Periksa dokumentasi RenzmcLang untuk contoh penggunaan"
            ])

        return suggestions

    def run(self):
        self.print_banner()

        while True:
            try:
                if self.in_multiline:
                    prompt = f"{Colors.BRIGHT_BLACK}... {Colors.RESET}"
                else:
                    prompt = f"{Colors.BRIGHT_GREEN}>>> {Colors.RESET}"

                try:
                    line = input(prompt)
                except EOFError:
                    print(f"\n{Colors.CYAN}Keluar dari REPL...{Colors.RESET}")
                    break

                if not line.strip():
                    if self.in_multiline and self.multiline_buffer:
                        code = '\n'.join(self.multiline_buffer)
                        self.multiline_buffer = []
                        self.in_multiline = False

                        self.history.append(code)
                        self.execute_code(code)
                        self.line_number += 1
                    continue

                if line.strip() in ['keluar', 'exit', 'quit']:
                    print(f"{Colors.CYAN}Keluar dari REPL...{Colors.RESET}")
                    break

                if line.strip() == 'bantuan':
                    self.print_help()
                    continue

                if line.strip() == 'bersih':
                    self.clear_screen()
                    self.print_banner()
                    continue

                if line.strip() == 'riwayat':
                    self.show_history()
                    continue

                if line.strip() == 'reset':
                    self.reset_interpreter()
                    continue

                if line.strip() == 'variabel':
                    self.show_variables()
                    continue

                if line.strip().startswith('inspect '):
                    var_name = line.strip()[8:].strip()
                    self.inspect_variable(var_name)
                    continue

                if line.strip().startswith('tipe '):
                    var_name = line.strip()[5:].strip()
                    if hasattr(self.interpreter, 'global_scope') and var_name in self.interpreter.global_scope:
                        value = self.interpreter.global_scope[var_name]
                        print(f"{Colors.CYAN}{type(value).__name__}{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}Variabel '{var_name}' tidak ditemukan{Colors.RESET}")
                    continue

                if self.is_multiline_start(line):
                    self.in_multiline = True
                    self.multiline_buffer.append(line)
                    continue

                if self.in_multiline:
                    self.multiline_buffer.append(line)

                    if self.is_multiline_end(line):
                        code = '\n'.join(self.multiline_buffer)
                        self.multiline_buffer = []
                        self.in_multiline = False

                        self.history.append(code)
                        self.execute_code(code)
                        self.line_number += 1

                    continue

                self.history.append(line)
                self.execute_code(line)
                self.line_number += 1

            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}KeyboardInterrupt{Colors.RESET}")
                self.multiline_buffer = []
                self.in_multiline = False
                continue
            except Exception as e:
                print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.RESET}")
                import traceback
                traceback.print_exc()
                continue


def main():
    repl = RenzmcREPL()
    repl.run()


if __name__ == '__main__':
    main()
