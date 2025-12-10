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
import os
import ast
import collections
from typing import List, Dict, Any, Optional, Tuple, Set
from enum import Enum
from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser
from renzmc.core.ast import *
from renzmc.core.token import TokenType


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    STYLE = "style"


class LinterMessage:
    def __init__(self, severity: Severity, message: str, line: int, column: int, rule: str, suggestion: Optional[str] = None):
        self.severity = severity
        self.message = message
        self.line = line
        self.column = column
        self.rule = rule
        self.suggestion = suggestion

    def __str__(self):
        prefix = {
            Severity.ERROR: "ERROR",
            Severity.WARNING: "WARNING",
            Severity.INFO: " INFO",
            Severity.STYLE: "STYLE"
        }[self.severity]

        result = f"{prefix} at line {self.line}, column {self.column}: {self.message} ({self.rule})"
        if self.suggestion:
            result += f"\n   Suggestion: {self.suggestion}"
        return result


class LinterError(Exception):
    pass


class LinterWarning(Exception):
    pass


class RenzmcLinter:
    def __init__(self, config=None):
        self.config = config or {}
        self.messages: List[LinterMessage] = []
        self.source_lines: List[str] = []
        self.variable_scope: List[Set[str]] = [set()]
        self.function_stack: List[str] = []
        self.class_stack: List[str] = []
        self.loop_depth: int = 0
        self.complexity_scores: Dict[str, int] = {}
        self.import_order: List[str] = []

        self.comprehensive_rules = {
            'syntax_validation': True,
            'variable_naming': True,
            'function_naming': True,
            'class_naming': True,
            'constant_naming': True,
            'unused_variables': True,
            'unused_functions': True,
            'unused_imports': True,
            'undefined_variables': True,
            'undefined_functions': True,
            'reassigned_variables': True,
            'variable_scope': True,
            'function_length': True,
            'function_complexity': True,
            'function_parameters': True,
            'class_size': True,
            'method_complexity': True,
            'duplicate_code': True,
            'magic_numbers': True,
            'hardcoded_strings': True,
            'boolean_expressions': True,
            'comparison_chaining': True,
            'null_checks': True,
            'type_safety': True,
            'import_organization': True,
            'import_style': True,
            'circular_imports': True,
            'dead_code': True,
            'unreachable_code': True,
            'infinite_loops': True,
            'resource_leaks': True,
            'exception_handling': True,
            'security_issues': True,
            'performance_issues': True,
            'memory_efficiency': True,
            'concurrency_issues': True,
            'documentation': True,
            'code_style': True,
            'indentation': True,
            'line_length': True,
            'trailing_whitespace': True,
            'file_organization': True,
            'api_design': True,
            'error_messages': True,
            'testing_practices': True,
            'debugging_code': True,
            'deprecated_features': True,
            'internationalization': True,
            'accessibility': True
        }

        self.rules = {**self.comprehensive_rules, **self.config.get('rules', {})}

        self.reserved_keywords = {
            'jika', 'kalau', 'maka', 'tidak', 'lainnya', 'kalau_tidak', 'selesai', 'akhir',
            'selama', 'ulangi', 'kali', 'untuk', 'setiap', 'dari', 'sampai', 'lanjut', 'berhenti',
            'lewati', 'coba', 'tangkap', 'akhirnya', 'cocok', 'kasus', 'bawaan', 'simpan',
            'ke', 'dalam', 'itu', 'adalah', 'sebagai', 'bukan', 'tampilkan', 'tulis', 'cetak',
            'tunjukkan', 'tanya', 'buat', 'fungsi', 'dengan', 'parameter', 'panggil', 'jalankan',
            'kembali', 'hasil', 'kembalikan', 'kelas', 'metode', 'konstruktor', 'warisi',
            'gunakan', 'impor', 'impor_python', 'panggil_python', 'modul', 'paket', 'lambda',
            'async', 'await', 'yield', 'yield_from', 'dekorator', 'properi', 'metode_statis',
            'metode_kelas', 'tipe', 'jenis_data', 'generator', 'asinkron', 'benar', 'salah',
            'diri', 'ini', 'super', 'global', 'lokal', 'statis'
        }

        self.dangerous_functions = {
            'eval', 'exec', 'compile', '__import__', 'open', 'file', 'input', 'raw_input',
            'reload', 'exit', 'quit', 'help', 'copyright', 'credits', 'license'
        }

        self.built_in_functions = {
            'tampilkan', 'tulis', 'cetak', 'tanya', 'buat', 'simpan', 'panggil', 'jalankan',
            'hasil', 'kembali', 'kembalikan', 'impor', 'impor_python', 'panggil_python',
            'len', 'str', 'int', 'float', 'bool', 'list', 'dict', 'set', 'tuple',
            'type', 'isinstance', 'hasattr', 'getattr', 'setattr', 'delattr',
            'min', 'max', 'sum', 'sorted', 'reversed', 'enumerate', 'zip',
            'map', 'filter', 'reduce', 'all', 'any', 'abs', 'round',
            'pow', 'divmod', 'complex', 'bin', 'oct', 'hex', 'chr', 'ord'
        }

        self.constant_pattern = re.compile(r'^[A-Z_][A-Z0-9_]*$')
        self.variable_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
        self.function_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
        self.class_pattern = re.compile(r'^[A-Z][a-zA-Z0-9_]*$')
        self.private_pattern = re.compile(r'^_[a-zA-Z_][a-zA-Z0-9_]*$')
        self.dunder_pattern = re.compile(r'^__[a-zA-Z_][a-zA-Z0-9_]*__$')

    def lint_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source_code = f.read()
            return self.lint_code(source_code, filepath)
        except FileNotFoundError:
            raise LinterError(f"File not found: {filepath}")
        except Exception as e:
            raise LinterError(f"Error reading file {filepath}: {str(e)}")

    def lint_code(self, source_code, filename="<string>"):
        self.messages = []
        self.source_lines = source_code.split('\n')
        self.variable_scope = [set()]
        self.function_stack = []
        self.class_stack = []
        self.loop_depth = 0
        self.complexity_scores = {}
        self.import_order = []

        try:
            lexer = Lexer(source_code)
            parser = Parser(lexer)
            ast = parser.parse()

            self._check_ast(ast)
            self._check_file_level_rules(source_code, filename)
            self._perform_comprehensive_analysis(source_code)

        except Exception as e:
            if self.rules.get('syntax_validation', True):
                self._add_message(Severity.ERROR, f"Syntax error: {str(e)}", 1, 1, "syntax_error")

        return self.messages

    def _check_ast(self, node):
        if isinstance(node, Program):
            self._check_program(node)
        elif isinstance(node, Block):
            self._check_block(node)
        elif isinstance(node, VarDecl):
            self._check_var_decl(node)
        elif isinstance(node, Assign):
            self._check_assign(node)
        elif isinstance(node, FuncDecl):
            self._check_func_decl(node)
        elif isinstance(node, FuncCall):
            self._check_func_call(node)
        elif isinstance(node, ClassDecl):
            self._check_class_decl(node)
        elif isinstance(node, If):
            self._check_if(node)
        elif isinstance(node, While):
            self._check_while(node)
        elif isinstance(node, For):
            self._check_for(node)
        elif isinstance(node, ForEach):
            self._check_for_each(node)
        elif isinstance(node, TryCatch):
            self._check_try_catch(node)
        elif isinstance(node, Import):
            self._check_import(node)
        elif isinstance(node, PythonImport):
            self._check_python_import(node)
        elif isinstance(node, BinOp):
            self._check_binop(node)

        self._check_children(node)

    def _check_program(self, node):
        defined_functions = set()
        defined_classes = set()
        defined_variables = set()
        used_functions = set()
        used_classes = set()
        used_variables = set()

        for stmt in node.statements:
            if isinstance(stmt, FuncDecl):
                if self.rules.get('duplicate_code', True):
                    if stmt.name in defined_functions:
                        self._add_message(Severity.ERROR, f"Function '{stmt.name}' is already defined",
                                          stmt.line or 1, stmt.column or 1, "duplicate_function_definition",
                                          "Consider renaming one of the functions or refactoring into a single function")
                    if stmt.name in self.reserved_keywords:
                        self._add_message(Severity.ERROR, f"Function '{stmt.name}' uses reserved keyword",
                                          stmt.line or 1, stmt.column or 1, "reserved_keyword_function",
                                          "Choose a different name that is not a keyword")
                defined_functions.add(stmt.name)
                self._check_function_length(stmt)
                self._check_function_parameters(stmt)
                self.complexity_scores[stmt.name] = self._calculate_complexity(stmt.body)

            elif isinstance(stmt, ClassDecl):
                if self.rules.get('duplicate_code', True):
                    if stmt.name in defined_classes:
                        self._add_message(Severity.ERROR, f"Class '{stmt.name}' is already defined",
                                          stmt.line or 1, stmt.column or 1, "duplicate_class_definition",
                                          "Consider renaming one of the classes or using inheritance")
                defined_classes.add(stmt.name)
                self._check_class_size(stmt)

            elif isinstance(stmt, VarDecl):
                if hasattr(stmt, 'var_name') and stmt.var_name:
                    var_name = stmt.var_name.name if hasattr(stmt.var_name, 'name') else str(stmt.var_name)
                    if self.rules.get('duplicate_code', True):
                        if var_name in defined_variables:
                            self._add_message(Severity.WARNING, f"Variable '{var_name}' is redefined",
                                              stmt.line or 1, stmt.column or 1, "duplicate_variable_definition",
                                              "Consider using a different variable name or reusing the existing one")
                    defined_variables.add(var_name)
                    self._check_variable_naming(stmt.var_name, stmt.line or 1, stmt.column or 1)

        if self.rules.get('unused_variables', True):
            unused_vars = defined_variables - used_variables
            for var in unused_vars:
                self._add_message(Severity.WARNING, f"Variable '{var}' is defined but never used",
                                  1, 1, "unused_variable",
                                  "Remove the unused variable or use it in your code")

        if self.rules.get('unused_functions', True):
            unused_funcs = defined_functions - used_functions - {'__init__', '__main__'}
            for func in unused_funcs:
                self._add_message(Severity.INFO, f"Function '{func}' is defined but never called",
                                  1, 1, "unused_function",
                                  "Consider removing the function or documenting it for future use")

    def _check_function_length(self, func_decl):
        if self.rules.get('function_length', True):
            length = self._count_statements(func_decl.body)
            if length > 50:
                self._add_message(Severity.WARNING, f"Function '{func_decl.name}' is too long ({length} statements)",
                                  func_decl.line or 1, func_decl.column or 1, "long_function",
                                  "Consider breaking this function into smaller, more focused functions")
            elif length > 30:
                self._add_message(Severity.INFO, f"Function '{func_decl.name}' is moderately long ({length} statements)",
                                  func_decl.line or 1, func_decl.column or 1, "moderate_function_length",
                                  "Consider if this function could be simplified")

    def _check_function_parameters(self, func_decl):
        if self.rules.get('function_parameters', True):
            param_count = len(func_decl.params) if func_decl.params else 0
            if param_count > 7:
                self._add_message(Severity.WARNING, f"Function '{func_decl.name}' has too many parameters ({param_count})",
                                  func_decl.line or 1, func_decl.column or 1, "too_many_parameters",
                                  "Consider using a configuration object or reducing parameters")
            elif param_count > 5:
                self._add_message(Severity.INFO, f"Function '{func_decl.name}' has many parameters ({param_count})",
                                  func_decl.line or 1, func_decl.column or 1, "many_parameters",
                                  "Consider if some parameters could be grouped together")

    def _check_class_size(self, class_decl):
        if self.rules.get('class_size', True):
            method_count = len(class_decl.methods) if class_decl.methods else 0
            if method_count > 20:
                self._add_message(Severity.WARNING, f"Class '{class_decl.name}' has too many methods ({method_count})",
                                  class_decl.line or 1, class_decl.column or 1, "large_class",
                                  "Consider splitting this class into smaller, more focused classes")
            elif method_count > 15:
                self._add_message(Severity.INFO, f"Class '{class_decl.name}' has many methods ({method_count})",
                                  class_decl.line or 1, class_decl.column or 1, "moderate_class_size",
                                  "Consider if this class follows the Single Responsibility Principle")

    def _check_block(self, node):
        self.variable_scope.append(set())
        for stmt in node.statements:
            self._check_ast(stmt)
        self.variable_scope.pop()

    def _check_var_decl(self, node):
        if self.rules.get('variable_naming', True):
            self._check_variable_naming(node.var_name, node.line or 1, node.column or 1)

        if hasattr(node, 'var_name') and node.var_name:
            var_name = node.var_name.name if hasattr(node.var_name, 'name') else str(node.var_name)
            self.variable_scope[-1].add(var_name)

        if node.value:
            self._check_ast(node.value)

    def _check_assign(self, node):
        if self.rules.get('type_safety', True) and node.value:
            self._check_type_consistency(node.var, node.value, node.line or 1, node.column or 1)

        if self.rules.get('magic_numbers', True):
            self._check_magic_numbers(node.value, node.line or 1, node.column or 1)

        if self.rules.get('hardcoded_strings', True):
            self._check_hardcoded_strings(node.value, node.line or 1, node.column or 1)

        self._check_ast(node.var)
        self._check_ast(node.value)

    def _check_func_decl(self, node):
        if self.rules.get('function_naming', True):
            if node.name in self.reserved_keywords:
                self._add_message(Severity.ERROR, f"Function name '{node.name}' is a reserved keyword",
                                  node.line or 1, node.column or 1, "reserved_keyword_function",
                                  "Choose a different function name that is not a keyword")
            elif not self.function_pattern.match(node.name):
                if not self.dunder_pattern.match(node.name) and not self.private_pattern.match(node.name):
                    self._add_message(Severity.STYLE, f"Function name '{node.name}' should follow snake_case convention",
                                      node.line or 1, node.column or 1, "function_naming_convention",
                                      "Use lowercase letters with underscores, e.g., 'my_function'")

        if self.rules.get('documentation', True) and not self._has_documentation(node):
            self._add_message(Severity.INFO, f"Function '{node.name}' lacks documentation",
                              node.line or 1, node.column or 1, "missing_function_documentation",
                              "Add a docstring to explain what the function does")

        self.function_stack.append(node.name)
        complexity = self._calculate_complexity(node.body)
        if self.rules.get('function_complexity', True):
            if complexity > 15:
                self._add_message(Severity.WARNING, f"Function '{node.name}' has high cyclomatic complexity ({complexity})",
                                  node.line or 1, node.column or 1, "high_function_complexity",
                                  "Consider breaking this function into smaller functions or simplifying logic")
            elif complexity > 10:
                self._add_message(Severity.INFO, f"Function '{node.name}' has moderate complexity ({complexity})",
                                  node.line or 1, node.column or 1, "moderate_complexity",
                                  "Consider if this function could be simplified")

        for param in node.params:
            self._check_ast(param)

        self._check_ast(node.body)
        self.function_stack.pop()

    def _check_func_call(self, node):
        if hasattr(node, 'name') and node.name:
            if self.rules.get('undefined_functions', True):
                if (node.name not in self.reserved_keywords
                    and node.name not in self.built_in_functions
                        and not self._is_function_defined(node.name)):
                    self._add_message(Severity.ERROR, f"Function '{node.name}' is not defined",
                                      node.line or 1, node.column or 1, "undefined_function",
                                      "Define the function or import it from a module")

            if self.rules.get('security_issues', True):
                if node.name in self.dangerous_functions:
                    self._add_message(Severity.WARNING, f"Use of potentially dangerous function '{node.name}'",
                                      node.line or 1, node.column or 1, "dangerous_function",
                                      "Ensure you understand the security implications and sanitize inputs")

        for arg in node.args:
            self._check_ast(arg)

    def _check_class_decl(self, node):
        if self.rules.get('class_naming', True):
            if node.name in self.reserved_keywords:
                self._add_message(Severity.ERROR, f"Class name '{node.name}' is a reserved keyword",
                                  node.line or 1, node.column or 1, "reserved_keyword_class",
                                  "Choose a different class name that is not a keyword")
            elif not self.class_pattern.match(node.name):
                self._add_message(Severity.STYLE, f"Class name '{node.name}' should follow PascalCase convention",
                                  node.line or 1, node.column or 1, "class_naming_convention",
                                  "Use PascalCase: start with uppercase, e.g., 'MyClass'")

        if self.rules.get('documentation', True) and not self._has_documentation(node):
            self._add_message(Severity.INFO, f"Class '{node.name}' lacks documentation",
                              node.line or 1, node.column or 1, "missing_class_documentation",
                              "Add a docstring to explain the purpose and usage of this class")

        self.class_stack.append(node.name)
        for method in node.methods:
            self._check_ast(method)
        self.class_stack.pop()

    def _check_if(self, node):
        if self.rules.get('boolean_expressions', True):
            self._check_boolean_expression(node.condition, node.line or 1, node.column or 1)

        if self.rules.get('null_checks', True):
            self._check_null_handling(node.condition, node.line or 1, node.column or 1)

        self._check_ast(node.condition)
        self._check_ast(node.if_body)
        if node.else_body:
            self._check_ast(node.else_body)

    def _check_while(self, node):
        if self.rules.get('boolean_expressions', True):
            self._check_boolean_expression(node.condition, node.line or 1, node.column or 1)

        if self.rules.get('infinite_loops', True):
            self._check_potential_infinite_loop(node.condition, node.body, node.line or 1, node.column or 1)

        self.loop_depth += 1
        self._check_ast(node.condition)
        self._check_ast(node.body)
        self.loop_depth -= 1

    def _check_for(self, node):
        if self.rules.get('performance_issues', True):
            self._check_loop_performance(node, node.line or 1, node.column or 1)

        self.loop_depth += 1
        self._check_ast(node.start)
        self._check_ast(node.end)
        self._check_ast(node.body)
        self.loop_depth -= 1

    def _check_for_each(self, node):
        if self.rules.get('performance_issues', True):
            self._check_loop_performance(node, node.line or 1, node.column or 1)

        self.loop_depth += 1
        self._check_ast(node.iterable)
        self._check_ast(node.body)
        self.loop_depth -= 1

    def _check_try_catch(self, node):
        if self.rules.get('exception_handling', True):
            if not node.except_blocks and not node.finally_block:
                self._add_message(Severity.ERROR, "Try block without except or finally blocks",
                                  node.line or 1, node.column or 1, "incomplete_try_catch",
                                  "Add except blocks to handle exceptions or a finally block")

            if node.except_blocks:
                for except_block in node.except_blocks:
                    if not self._has_exception_handling(except_block):
                        self._add_message(Severity.WARNING, "Except block doesn't handle the exception",
                                          except_block.line or 1, except_block.column or 1, "empty_except_block",
                                          "Add proper exception handling code")

        self._check_ast(node.try_block)
        for except_block in node.except_blocks:
            self._check_ast(except_block)
        if node.finally_block:
            self._check_ast(node.finally_block)

    def _check_import(self, node):
        if self.rules.get('import_organization', True):
            self.import_order.append(('standard', node.module, node.line or 1))

        if self.rules.get('import_style', True):
            if not node.module.islower():
                self._add_message(Severity.STYLE, f"Module name '{node.module}' should be lowercase",
                                  node.line or 1, node.column or 1, "module_naming_style",
                                  "Use lowercase for module names, e.g., 'my_module'")

    def _check_python_import(self, node):
        if self.rules.get('import_organization', True):
            self.import_order.append(('python', node.module, node.line or 1))

        if self.rules.get('security_issues', True):
            dangerous_modules = ['os', 'subprocess', 'eval', 'exec', 'compile', 'pickle', 'marshal',
                                 'shelve', 'ctypes', 'sys', 'importlib', 'types']
            if node.module in dangerous_modules:
                self._add_message(Severity.WARNING, f"Importing potentially dangerous Python module '{node.module}'",
                                  node.line or 1, node.column or 1, "dangerous_python_import",
                                  "Ensure you trust the source and sanitize all inputs")

        if self.rules.get('circular_imports', True):
            self._check_circular_import(node.module, node.line or 1, node.column or 1)

    def _check_binop(self, node):
        if self.rules.get('comparison_chaining', True):
            self._check_comparison_chaining(node, node.line or 1, node.column or 1)

        if self.rules.get('boolean_expressions', True):
            if hasattr(node.op, 'type') and node.op.type in (TokenType.DAN, TokenType.ATAU):
                self._check_boolean_expression(node, node.line or 1, node.column or 1)

        self._check_ast(node.left)
        self._check_ast(node.right)

    def _check_variable_naming(self, var_node, line, column):
        if not var_node or not hasattr(var_node, 'name'):
            return

        var_name = var_node.name

        if var_name in self.reserved_keywords:
            self._add_message(Severity.ERROR, f"Variable name '{var_name}' is a reserved keyword",
                              line, column, "reserved_keyword_variable",
                              "Choose a different variable name that is not a keyword")
        elif self.constant_pattern.match(var_name) and var_name not in self.variable_scope[-2:] if len(self.variable_scope) > 1 else False:
            self._add_message(Severity.WARNING, f"Constant '{var_name}' should be defined at module level",
                              line, column, "constant_naming_scope",
                              "Move constants to module level or use lowercase for local variables")
        elif not self.variable_pattern.match(var_name):
            if not self.dunder_pattern.match(var_name) and not self.private_pattern.match(var_name):
                self._add_message(Severity.STYLE, f"Variable name '{var_name}' should follow snake_case convention",
                                  line, column, "variable_naming_convention",
                                  "Use lowercase letters with underscores, e.g., 'my_variable'")

    def _check_boolean_expression(self, expr, line, column):
        pass

    def _check_type_consistency(self, var, value, line, column):
        pass

    def _check_magic_numbers(self, value, line, column):
        pass

    def _check_hardcoded_strings(self, value, line, column):
        pass

    def _check_null_handling(self, condition, line, column):
        pass

    def _check_potential_infinite_loop(self, condition, body, line, column):
        pass

    def _check_loop_performance(self, loop_node, line, column):
        pass

    def _check_circular_import(self, module, line, column):
        pass

    def _check_comparison_chaining(self, node, line, column):
        pass

    def _check_children(self, node):
        for attr_name in dir(node):
            attr = getattr(node, attr_name)
            if isinstance(attr, AST):
                self._check_ast(attr)
            elif isinstance(attr, list):
                for item in attr:
                    if isinstance(item, AST):
                        self._check_ast(item)

    def _check_file_level_rules(self, source_code, filename):
        if self.rules.get('line_length', True):
            self._check_line_length(source_code)

        if self.rules.get('trailing_whitespace', True):
            self._check_trailing_whitespace(source_code)

        if self.rules.get('indentation', True):
            self._check_indentation(source_code)

        if self.rules.get('file_organization', True):
            self._check_file_organization(source_code)

        if self.rules.get('debugging_code', True):
            self._check_debugging_code(source_code)

        if self.rules.get('internationalization', True):
            self._check_internationalization(source_code)

    def _perform_comprehensive_analysis(self, source_code):
        if self.rules.get('duplicate_code', True):
            self._check_duplicate_code(source_code)

        if self.rules.get('memory_efficiency', True):
            self._check_memory_efficiency(source_code)

        if self.rules.get('concurrency_issues', True):
            self._check_concurrency_issues(source_code)

        if self.rules.get('api_design', True):
            self._check_api_design(source_code)

    def _check_line_length(self, source_code):
        lines = source_code.split('\n')
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                self._add_message(Severity.STYLE, f"Line too long ({len(line)} characters, maximum is 120)",
                                  i, 120, "long_line",
                                  "Break the line or use line continuation techniques")

    def _check_trailing_whitespace(self, source_code):
        lines = source_code.split('\n')
        for i, line in enumerate(lines, 1):
            if line.rstrip() != line:
                self._add_message(Severity.STYLE, f"Line {i} has trailing whitespace",
                                  i, len(line), "trailing_whitespace",
                                  "Remove trailing spaces or tabs")

    def _check_indentation(self, source_code):
        lines = source_code.split('\n')
        for i, line in enumerate(lines, 1):
            stripped = line.lstrip()
            if not stripped or stripped.startswith('//'):
                continue

            if line.startswith('\t') and any(' ' in l for l in lines[i:i + 5]):
                self._add_message(Severity.STYLE, f"Mixed tabs and spaces detected at line {i}",
                                  i, 1, "mixed_indentation",
                                  "Use either tabs or spaces consistently, preferably 4 spaces")

            if any(keyword in stripped for keyword in ['jika', 'untuk', 'selama', 'coba', 'fungsi', 'kelas']):
                if not line.startswith('    ') and not line.startswith('\t'):
                    self._add_message(Severity.STYLE, f"Inconsistent indentation at line {i}",
                                      i, 1, "inconsistent_indentation",
                                      "Use consistent indentation (4 spaces recommended)")

    def _check_file_organization(self, source_code):
        lines = source_code.split('\n')

        has_imports = False
        has_constants = False
        has_functions = False
        has_classes = False
        has_main_code = False

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('//'):
                continue

            if 'impor' in stripped or 'impor_python' in stripped:
                has_imports = True
            elif 'itu' in stripped and '=' not in stripped and any(c.isupper() for c in stripped):
                has_constants = True
            elif 'buat fungsi' in stripped:
                has_functions = True
            elif 'kelas' in stripped:
                has_classes = True
            elif not any(keyword in stripped for keyword in ['buat', 'kelas', 'impor', '//']):
                has_main_code = True

        if has_main_code and has_functions and not self._is_properly_structured(lines):
            self._add_message(Severity.INFO, "Consider organizing code with proper structure: imports, constants, classes, functions, main code",
                              1, 1, "file_organization",
                              "Follow standard file organization for better maintainability")

    def _check_debugging_code(self, source_code):
        debug_patterns = ['print(', 'tampilkan', 'debug', 'DEBUG', 'console.log', 'console.debug']
        lines = source_code.split('\n')

        for i, line in enumerate(lines, 1):
            if any(pattern in line for pattern in debug_patterns):
                if 'tampilkan' in line and not line.strip().startswith('//'):
                    self._add_message(Severity.INFO, f"Possible debugging code found at line {i}",
                                      i, 1, "debugging_code",
                                      "Remove or comment out debugging statements in production code")

    def _check_internationalization(self, source_code):
        lines = source_code.split('\n')

        for i, line in enumerate(lines, 1):
            if '"' in line and any(indicator in line.lower() for indicator in ['error', 'warning', 'message']):
                if not line.strip().startswith('//'):
                    self._add_message(Severity.INFO, f"Hardcoded user-facing string at line {i} should be internationalized",
                                      i, 1, "hardcoded_user_string",
                                      "Use localization system for user-facing text")

    def _check_duplicate_code(self, source_code):
        lines = source_code.split('\n')
        code_blocks = {}

        for i, line in enumerate(lines):
            stripped = line.strip()
            if len(stripped) > 10 and not stripped.startswith('//'):
                if stripped in code_blocks:
                    code_blocks[stripped].append(i + 1)
                else:
                    code_blocks[stripped] = [i + 1]

        for code, occurrences in code_blocks.items():
            if len(occurrences) > 2:
                self._add_message(Severity.WARNING, f"Duplicate code block found at lines: {', '.join(map(str, occurrences))}",
                                  occurrences[0], 1, "duplicate_code",
                                  "Consider extracting common code into a function or method")

    def _check_memory_efficiency(self, source_code):
        inefficient_patterns = [
            (r'list\(range\([^)]+\)\)', 'Consider using generators instead of list(range()) for memory efficiency'),
            (r'\[\s*x\s+for\s+x\s+in\s+', 'Consider using generator expressions instead of list comprehensions for large datasets'),
            (r'\.sort\(\)', 'Consider using sorted() function for better memory usage patterns')
        ]

        lines = source_code.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, suggestion in inefficient_patterns:
                if re.search(pattern, line):
                    self._add_message(Severity.INFO, f"Memory inefficiency detected at line {i}",
                                      i, 1, "memory_efficiency", suggestion)

    def _check_concurrency_issues(self, source_code):
        concurrent_patterns = ['async', 'await', 'thread', 'lock', 'semaphore']
        lines = source_code.split('\n')

        for i, line in enumerate(lines, 1):
            if any(pattern in line.lower() for pattern in concurrent_patterns):
                if 'selama' in line.lower() or 'untuk' in line.lower():
                    self._add_message(Severity.WARNING, f"Potential concurrency issue at line {i}",
                                      i, 1, "concurrency_issue",
                                      "Ensure proper synchronization when using loops in concurrent code")

    def _check_api_design(self, source_code):
        if 'buat fungsi' in source_code:
            lines = source_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'buat fungsi' in line and '(' in line:
                    func_name = re.search(r'buat fungsi (\w+)', line)
                    if func_name and func_name.group(1).startswith('_'):
                        self._add_message(Severity.INFO, f"Private function '{func_name.group(1)}' detected in API",
                                          i, 1, "private_api_function",
                                          "Consider if private functions should be part of the public API")

    def _calculate_complexity(self, node):
        complexity = 1

        if isinstance(node, If):
            complexity += 1 + self._calculate_complexity(node.if_body)
            if node.else_body:
                complexity += self._calculate_complexity(node.else_body)
        elif isinstance(node, While):
            complexity += 1 + self._calculate_complexity(node.body)
        elif isinstance(node, For):
            complexity += 1 + self._calculate_complexity(node.body)
        elif isinstance(node, ForEach):
            complexity += 1 + self._calculate_complexity(node.body)
        elif isinstance(node, TryCatch):
            complexity += 1
            for except_block in node.except_blocks:
                complexity += self._calculate_complexity(except_block)

        for attr_name in dir(node):
            attr = getattr(node, attr_name)
            if isinstance(attr, AST) and attr != node:
                complexity += self._calculate_complexity(attr)
            elif isinstance(attr, list):
                for item in attr:
                    if isinstance(item, AST) and item != node:
                        complexity += self._calculate_complexity(item)

        return complexity

    def _count_statements(self, node):
        count = 0
        if isinstance(node, list):
            for item in node:
                count += self._count_statements(item)
        elif hasattr(node, 'statements'):
            count += self._count_statements(node.statements)
        else:
            count += 1

        return count

    def _has_documentation(self, node):
        return False

    def _is_function_defined(self, name):
        return False

    def _has_exception_handling(self, node):
        return True

    def _is_properly_structured(self, lines):
        return True

    def _add_message(self, severity, message, line, column, rule, suggestion=None):
        self.messages.append(LinterMessage(severity, message, line, column, rule, suggestion))

    def get_messages(self):
        return self.messages

    def get_errors(self):
        return [msg for msg in self.messages if msg.severity == Severity.ERROR]

    def get_warnings(self):
        return [msg for msg in self.messages if msg.severity == Severity.WARNING]

    def get_info(self):
        return [msg for msg in self.messages if msg.severity == Severity.INFO]

    def get_style_issues(self):
        return [msg for msg in self.messages if msg.severity == Severity.STYLE]

    def has_errors(self):
        return any(msg.severity == Severity.ERROR for msg in self.messages)

    def has_warnings(self):
        return any(msg.severity == Severity.WARNING for msg in self.messages)

    def get_summary(self):
        errors = len(self.get_errors())
        warnings = len(self.get_warnings())
        info = len(self.get_info())
        style = len(self.get_style_issues())

        return {
            'total': len(self.messages),
            'errors': errors,
            'warnings': warnings,
            'info': info,
            'style': style,
            'status': 'failed' if errors > 0 else 'passed'
        }


def lint_file(filepath, config=None):
    linter = RenzmcLinter(config)
    return linter.lint_file(filepath)


def lint_code(source_code, config=None):
    linter = RenzmcLinter(config)
    return linter.lint_code(source_code)
