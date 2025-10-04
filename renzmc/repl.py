#!/usr/bin/env python3
"""
REPL (Read-Eval-Print Loop) untuk RenzMcLang
Interactive shell untuk testing dan eksperimen
"""

import sys
import os
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.interpreter import Interpreter
from renzmc.core.error import RenzmcError

class RenzmcREPL:
    """Interactive REPL for RenzMcLang"""
    
    def __init__(self):
        self.interpreter = Interpreter()
        self.history = []
        self.multiline_buffer = []
        self.in_multiline = False
        
    def print_banner(self):
        """Print welcome banner"""
        print("╔════════════════════════════════════════════════════════════════╗")
        print("║           RenzMcLang Interactive Shell (REPL)                 ║")
        print("║                    Version 0.0.3                               ║")
        print("╚════════════════════════════════════════════════════════════════╝")
        print()
        print("Selamat datang di RenzMcLang REPL!")
        print("Ketik 'bantuan' untuk melihat perintah yang tersedia")
        print("Ketik 'keluar' atau tekan Ctrl+D untuk keluar")
        print()
    
    def print_help(self):
        """Print help message"""
        print("\n📚 Perintah REPL:")
        print("  bantuan      - Tampilkan pesan bantuan ini")
        print("  keluar       - Keluar dari REPL")
        print("  bersih       - Bersihkan layar")
        print("  riwayat      - Tampilkan riwayat perintah")
        print("  reset        - Reset interpreter (hapus semua variabel)")
        print("  variabel     - Tampilkan semua variabel yang ada")
        print()
        print("💡 Tips:")
        print("  - Gunakan 'selesai' untuk mengakhiri blok multiline")
        print("  - Tekan Enter dua kali untuk mengeksekusi blok multiline")
        print("  - Gunakan f-string untuk string interpolation: f&quot;Nilai: {x}&quot;")
        print()
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_history(self):
        """Show command history"""
        if not self.history:
            print("Tidak ada riwayat perintah")
            return
        
        print("\n📜 Riwayat Perintah:")
        for i, cmd in enumerate(self.history, 1):
            print(f"  {i}. {cmd[:60]}{'...' if len(cmd) > 60 else ''}")
        print()
    
    def show_variables(self):
        """Show all defined variables"""
        if not hasattr(self.interpreter, 'global_scope') or not self.interpreter.global_scope:
            print("Tidak ada variabel yang didefinisikan")
            return
        
        print("\n📦 Variabel yang Didefinisikan:")
        for name, value in self.interpreter.global_scope.items():
            if not name.startswith('__'):
                value_str = str(value)
                if len(value_str) > 50:
                    value_str = value_str[:50] + "..."
                print(f"  {name} = {value_str}")
        print()
    
    def reset_interpreter(self):
        """Reset interpreter state"""
        self.interpreter = Interpreter()
        print("✅ Interpreter direset (semua variabel dihapus)")
    
    def is_multiline_start(self, line):
        """Check if line starts a multiline block"""
        multiline_keywords = [
            'jika', 'kalau', 'selama', 'untuk', 'fungsi', 
            'kelas', 'coba', 'cocok', 'dengan'
        ]
        
        stripped = line.strip()
        for keyword in multiline_keywords:
            if stripped.startswith(keyword):
                return True
        return False
    
    def is_multiline_end(self, line):
        """Check if line ends a multiline block"""
        return line.strip() in ['selesai', 'akhir']
    
    def execute_code(self, code):
        """Execute RenzMcLang code"""
        try:
            # Lexer
            lexer = Lexer(code)
            
            # Parser (takes lexer, not tokens)
            parser = Parser(lexer)
            ast = parser.parse()
            
            # Interpreter
            result = self.interpreter.interpret(ast)
            
            # Print result if not None
            if result is not None and result != '':
                print(result)
            
            return True
            
        except RenzmcError as e:
            print(f"❌ Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def run(self):
        """Run the REPL"""
        self.print_banner()
        
        while True:
            try:
                # Prompt
                if self.in_multiline:
                    prompt = "... "
                else:
                    prompt = ">>> "
                
                # Read input
                try:
                    line = input(prompt)
                except EOFError:
                    print("\nKeluar dari REPL...")
                    break
                
                # Skip empty lines
                if not line.strip():
                    if self.in_multiline and self.multiline_buffer:
                        # Empty line in multiline mode - execute buffer
                        code = '\n'.join(self.multiline_buffer)
                        self.multiline_buffer = []
                        self.in_multiline = False
                        
                        self.history.append(code)
                        self.execute_code(code)
                    continue
                
                # Handle special commands
                if line.strip() in ['keluar', 'exit', 'quit']:
                    print("Keluar dari REPL...")
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
                
                # Handle multiline input
                if self.is_multiline_start(line):
                    self.in_multiline = True
                    self.multiline_buffer.append(line)
                    continue
                
                if self.in_multiline:
                    self.multiline_buffer.append(line)
                    
                    if self.is_multiline_end(line):
                        # Execute multiline block
                        code = '\n'.join(self.multiline_buffer)
                        self.multiline_buffer = []
                        self.in_multiline = False
                        
                        self.history.append(code)
                        self.execute_code(code)
                    
                    continue
                
                # Execute single line
                self.history.append(line)
                self.execute_code(line)
                
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                self.multiline_buffer = []
                self.in_multiline = False
                continue
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                import traceback
                traceback.print_exc()
                continue

def main():
    """Main entry point for REPL"""
    repl = RenzmcREPL()
    repl.run()

if __name__ == '__main__':
    main()