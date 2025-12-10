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

import re
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.ast import *
from renzmc.core.token import TokenType


class FormattingConfig:
    def __init__(self):
        self.indent_size = 4
        self.use_tabs = False
        self.max_line_length = 120
        self.trailing_comma = True
        self.align_multiline = True
        self.brace_style = "same_line"
        self.space_around_operators = True
        self.space_after_comma = True
        self.line_break_after_statements = True
        self.comment_style = "hanging"
        self.string_quotes = "double"


class RenzmcFormatter:
    def __init__(self, config=None):
        self.config = config or FormattingConfig()
        self.indent_char = '\t' if self.config.use_tabs else ' '
        self.indent_string = self.indent_char * self.config.indent_size
        self.current_indent = 0
        self.lines = []
        self.current_line = ""
        self.source_code = ""
        
        self.block_keywords = {
            'jika', 'kalau', 'selama', 'untuk', 'setiap', 'coba', 'fungsi', 'kelas', 'cocok'
        }
        
        self.end_keywords = {
            'selesai', 'akhir', 'akhirnya'
        }

    def format_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source_code = f.read()
            return self.format_code(source_code)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except Exception as e:
            raise Exception(f"Error reading file {filepath}: {str(e)}")

    def format_code(self, source_code, filename="<string>"):
        self.source_code = source_code
        self.lines = []
        self.current_line = ""
        self.current_indent = 0
        
        try:
            lexer = Lexer(source_code)
            parser = Parser(lexer)
            ast = parser.parse()
            
            self._format_ast(ast)
            self._flush_current_line()
            
            formatted_code = '\n'.join(self.lines)
            return self._post_process(formatted_code)
            
        except Exception as e:
            return self._fallback_format(source_code)

    def _format_ast(self, node):
        if isinstance(node, Program):
            self._format_program(node)
        elif isinstance(node, Block):
            self._format_block(node)
        elif isinstance(node, VarDecl):
            self._format_var_decl(node)
        elif isinstance(node, Assign):
            self._format_assign(node)
        elif isinstance(node, FuncDecl):
            self._format_func_decl(node)
        elif isinstance(node, FuncCall):
            self._format_func_call(node)
        elif isinstance(node, If):
            self._format_if(node)
        elif isinstance(node, While):
            self._format_while(node)
        elif isinstance(node, For):
            self._format_for(node)
        elif isinstance(node, ForEach):
            self._format_for_each(node)
        elif isinstance(node, Num):
            self._format_num(node)
        elif isinstance(node, String):
            self._format_string(node)
        elif isinstance(node, Var):
            self._format_var(node)
        elif isinstance(node, Print):
            self._format_print(node)
        elif isinstance(node, Return):
            self._format_return(node)

    def _format_program(self, node):
        for i, stmt in enumerate(node.statements):
            self._format_ast(stmt)
            if i < len(node.statements) - 1:
                self._add_blank_line()

    def _format_block(self, node):
        self.current_indent += 1
        for i, stmt in enumerate(node.statements):
            self._format_ast(stmt)
            if i < len(node.statements) - 1 and self.config.line_break_after_statements:
                self._add_blank_line()
        self.current_indent -= 1

    def _format_var_decl(self, node):
        var_name = node.var_name.name if hasattr(node.var_name, 'name') else str(node.var_name)
        self._add_to_current_line(f"{var_name} itu ")
        self._format_ast(node.value)

    def _format_assign(self, node):
        var_name = node.var.name if hasattr(node.var, 'name') else str(node.var)
        self._add_to_current_line(f"{var_name} itu ")
        self._format_ast(node.value)

    def _format_func_decl(self, node):
        params_str = self._format_params(node.params)
        self._add_line(f"buat fungsi {node.name} dengan {params_str}")
        self._format_ast(node.body)
        self._add_line("selesai")

    def _format_func_call(self, node):
        name = node.name if hasattr(node, 'name') and node.name else ""
        args_str = self._format_args(node.args)
        if name:
            self._add_to_current_line(f"panggil {name} dengan {args_str}")
        else:
            self._format_ast(node.func_expr)
            self._add_to_current_line(f" dengan {args_str}")

    def _format_if(self, node):
        self._add_to_current_line("jika ")
        self._format_ast(node.condition)
        self._flush_current_line()
        self._format_ast(node.if_body)
        self._add_line("selesai")
        
        if node.else_body:
            self._add_line("lainnya")
            self._format_ast(node.else_body)
            self._add_line("selesai")

    def _format_while(self, node):
        self._add_to_current_line("selama ")
        self._format_ast(node.condition)
        self._flush_current_line()
        self._format_ast(node.body)
        self._add_line("selesai")

    def _format_for(self, node):
        var_name = node.var_name.name if hasattr(node.var_name, 'name') else str(node.var_name)
        self._add_to_current_line(f"untuk {var_name} dari ")
        self._format_ast(node.start)
        self._add_to_current_line(" sampai ")
        self._format_ast(node.end)
        self._flush_current_line()
        self._format_ast(node.body)
        self._add_line("selesai")

    def _format_for_each(self, node):
        var_name = node.var_name.name if hasattr(node.var_name, 'name') else str(node.var_name)
        self._add_to_current_line(f"untuk setiap {var_name} dari ")
        self._format_ast(node.iterable)
        self._flush_current_line()
        self._format_ast(node.body)
        self._add_line("selesai")

    def _format_num(self, node):
        self._add_to_current_line(str(node.value))

    def _format_string(self, node):
        quote = self.config.string_quotes
        self._add_to_current_line(f"{quote}{node.value}{quote}")

    def _format_var(self, node):
        self._add_to_current_line(node.name)

    def _format_print(self, node):
        self._add_to_current_line("tampilkan ")
        self._format_ast(node.expr)

    def _format_return(self, node):
        self._add_to_current_line("hasil ")
        self._format_ast(node.expr)

    def _format_params(self, params):
        if not params:
            return ""
        
        param_names = []
        for param in params:
            if hasattr(param, 'name'):
                param_names.append(param.name)
            else:
                param_names.append(str(param))
        
        return ", ".join(param_names)

    def _format_args(self, args):
        if not args:
            return ""
        
        arg_values = []
        for arg in args:
            if hasattr(arg, 'value'):
                arg_values.append(str(arg.value))
            elif hasattr(arg, 'name'):
                arg_values.append(arg.name)
            else:
                arg_values.append(str(arg))
        
        return ", ".join(arg_values)

    def _add_to_current_line(self, text):
        self.current_line += text

    def _add_line(self, line=""):
        if self.current_indent > 0:
            self.lines.append(self.indent_string * self.current_indent + line)
        else:
            self.lines.append(line)
        self.current_line = ""

    def _add_blank_line(self):
        if self.lines and self.lines[-1].strip():
            self.lines.append("")

    def _flush_current_line(self):
        if self.current_line.strip():
            self._add_line(self.current_line)
        self.current_line = ""

    def _post_process(self, code):
        lines = code.split('\n')
        processed_lines = []
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped or stripped.startswith('//'):
                processed_lines.append("")
                continue
            
            if self.config.max_line_length > 0 and len(stripped) > self.config.max_line_length:
                wrapped_lines = self._wrap_long_line(line)
                processed_lines.extend(wrapped_lines)
            else:
                processed_lines.append(line)
        
        return '\n'.join(processed_lines).strip() + '\n'

    def _wrap_long_line(self, line):
        indent_match = re.match(r'^(\s*)', line)
        indent = indent_match.group(1) if indent_match else ""
        content = line[len(indent):]
        
        if ' itu ' in content:
            parts = content.split(' itu ', 1)
            return [
                f"{indent}{parts[0]} itu",
                f"{indent}{self.indent_string}{parts[1]}"
            ]
        elif ' dengan ' in content:
            parts = content.split(' dengan ', 1)
            return [
                f"{indent}{parts[0]} dengan",
                f"{indent}{self.indent_string}{parts[1]}"
            ]
        else:
            return [line]

    def _fallback_format(self, source_code):
        lines = source_code.split('\n')
        formatted_lines = []
        indent_level = 0
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped or stripped.startswith('//'):
                formatted_lines.append(line)
                continue
            
            if stripped.startswith(tuple(self.end_keywords)):
                indent_level = max(0, indent_level - 1)
            
            if indent_level > 0:
                formatted_lines.append(self.indent_string * indent_level + stripped)
            else:
                formatted_lines.append(stripped)
            
            if stripped.startswith(tuple(self.block_keywords)) and 'selesai' not in stripped:
                indent_level += 1
        
        return '\n'.join(formatted_lines)


def format_file(filepath, config=None):
    formatter = RenzmcFormatter(config)
    return formatter.format_file(filepath)


def format_code(source_code, config=None):
    formatter = RenzmcFormatter(config)
    return formatter.format_code(source_code)