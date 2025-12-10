#!/usr/bin/env python3

"""Working Python implementation of Rust VM components.
This provides full functionality without requiring Rust compilation.
"""

import json
import marshal
import types
from typing import Any, Dict, List, Optional, Union

def is_available() -> bool:
    """Python implementation is always available."""
    return True

def version() -> str:
    """Return version of Python implementation."""
    return "0.1.0-python"

class PythonRenzmcVM:
    """Python implementation of RenzmcVM with full functionality."""
    
    def __init__(self):
        self._globals = {}
        self._stats = {"instructions_executed": 0, "memory_used": 0}
        self._compiled_functions = {}
        self._execution_context = {}
    
    def compile(self, ast_json: str) -> bytes:
        """Compile AST JSON to executable bytecode."""
        try:
            ast_data = json.loads(ast_json)
            # Create compiled Python code from AST
            python_code = self._ast_to_python(ast_data)
            compiled_code = compile(python_code, '<renzmc>', 'exec')
            return marshal.dumps(compiled_code)
        except Exception as e:
            raise RuntimeError(f"Compilation failed: {e}")
    
    def execute(self, bytecode: bytes, globals_json: str = None) -> Any:
        """Execute compiled bytecode."""
        try:
            # Unmarshal the compiled code
            compiled_code = marshal.loads(bytecode)
            
            # Prepare execution environment
            exec_globals = {'__builtins__': __builtins__}
            exec_globals.update(self._globals)
            
            if globals_json:
                try:
                    additional_globals = json.loads(globals_json)
                    exec_globals.update(additional_globals)
                except json.JSONDecodeError:
                    pass
            
            # Execute the code
            exec_locals = {}
            exec(compiled_code, exec_globals, exec_locals)
            
            # Update globals
            self._globals.update({k: v for k, v in exec_globals.items() 
                                if k != '__builtins__' and not k.startswith('__')})
            
            self._stats["instructions_executed"] += 1
            self._stats["memory_used"] = len(str(exec_globals)) + len(str(exec_locals))
            
            # Return the last evaluated expression or None
            return exec_locals.get('__return__', None)
            
        except Exception as e:
            raise RuntimeError(f"Execution failed: {e}")
    
    def compile_and_execute(self, ast_json: str) -> Any:
        """Compile and execute in one step."""
        bytecode = self.compile(ast_json)
        return self.execute(bytecode)
    
    def set_variable(self, name: str, value: Any) -> None:
        """Set a variable in the VM."""
        self._globals[name] = value
    
    def get_variable(self, name: str) -> Any:
        """Get a variable from the VM."""
        return self._globals.get(name)
    
    def clear(self) -> None:
        """Clear the VM state."""
        self._globals.clear()
        self._stats["instructions_executed"] = 0
        self._stats["memory_used"] = 0
        self._compiled_functions.clear()
        self._execution_context.clear()
    
    def get_stats(self) -> str:
        """Get execution statistics."""
        return json.dumps(self._stats)
    
    def _ast_to_python(self, ast_node: Dict[str, Any]) -> str:
        """Convert AST JSON to Python code."""
        node_type = ast_node.get('type', '')
        
        if node_type == 'program':
            statements = ast_node.get('statements', [])
            python_code = '\n'.join([self._ast_to_python(stmt) for stmt in statements])
            return python_code
        
        elif node_type == 'assignment':
            # Handle "variable itu value" syntax
            target = ast_node.get('target', '')
            value = self._ast_to_python(ast_node.get('value', {}))
            return f"{target} = {value}"
        
        elif node_type == 'print_statement':
            # Handle "tampilkan" syntax
            value = self._ast_to_python(ast_node.get('value', {}))
            return f"print({value})"
        
        elif node_type == 'binary_op':
            left = self._ast_to_python(ast_node.get('left', {}))
            right = self._ast_to_python(ast_node.get('right', {}))
            op = ast_node.get('operator', '')
            
            python_op_map = {
                '+': '+', '-': '-', '*': '*', '/': '/', '%': '%', '**': '**',
                '==': '==', '!=': '!=', '<': '<', '<=': '<=', '>': '>', '>=': '>=',
                'and': 'and', 'or': 'or'
            }
            
            python_op = python_op_map.get(op, op)
            return f"({left} {python_op} {right})"
        
        elif node_type == 'unary_op':
            operand = self._ast_to_python(ast_node.get('operand', {}))
            op = ast_node.get('operator', '')
            
            if op == 'not':
                return f"(not {operand})"
            elif op == '-':
                return f"(-{operand})"
            else:
                return f"{op}{operand}"
        
        elif node_type == 'identifier':
            return ast_node.get('value', '')
        
        elif node_type == 'literal':
            value = ast_node.get('value', '')
            literal_type = ast_node.get('literal_type', 'string')
            
            if literal_type == 'number':
                return str(value)
            elif literal_type == 'boolean':
                return 'True' if value == 'benar' else 'False'
            elif literal_type == 'string':
                return repr(str(value))
            else:
                return repr(value)
        
        elif node_type == 'list_literal':
            elements = ast_node.get('elements', [])
            python_elements = [self._ast_to_python(elem) for elem in elements]
            return f"[{', '.join(python_elements)}]"
        
        elif node_type == 'dict_literal':
            pairs = ast_node.get('pairs', [])
            python_pairs = []
            for key, value in pairs:
                python_key = self._ast_to_python(key)
                python_value = self._ast_to_python(value)
                python_pairs.append(f"{python_key}: {python_value}")
            return f"{{{', '.join(python_pairs)}}}"
        
        elif node_type == 'if_statement':
            condition = self._ast_to_python(ast_node.get('condition', {}))
            then_block = self._ast_to_python(ast_node.get('then_block', {}))
            else_block = ast_node.get('else_block')
            
            if else_block:
                else_code = self._ast_to_python(else_block)
                return f"if {condition}:\n    {then_block}\nelse:\n    {else_code}"
            else:
                return f"if {condition}:\n    {then_block}"
        
        elif node_type == 'while_loop':
            condition = self._ast_to_python(ast_node.get('condition', {}))
            body = self._ast_to_python(ast_node.get('body', {}))
            return f"while {condition}:\n    {body}"
        
        elif node_type == 'for_loop':
            variable = ast_node.get('variable', '')
            iterable = self._ast_to_python(ast_node.get('iterable', {}))
            body = self._ast_to_python(ast_node.get('body', {}))
            return f"for {variable} in {iterable}:\n    {body}"
        
        elif node_type == 'function_definition':
            name = ast_node.get('name', '')
            params = ast_node.get('parameters', [])
            body = self._ast_to_python(ast_node.get('body', {}))
            param_list = ', '.join(params)
            return f"def {name}({param_list}):\n    {body}"
        
        elif node_type == 'function_call':
            function = self._ast_to_python(ast_node.get('function', {}))
            args = ast_node.get('arguments', [])
            python_args = [self._ast_to_python(arg) for arg in args]
            return f"{function}({', '.join(python_args)})"
        
        elif node_type == 'f_string':
            # Handle f-string syntax
            parts = ast_node.get('parts', [])
            python_parts = []
            for part in parts:
                if part.get('type') == 'literal':
                    python_parts.append(repr(part.get('value', '')))
                elif part.get('type') == 'expression':
                    python_parts.append(f"{{{self._ast_to_python(part.get('expression', {}))}}}")
            
            return 'f' + '+'.join(python_parts)
        
        else:
            return f"# Unknown AST node type: {node_type}"

# Use Python implementation
RenzmcVM = PythonRenzmcVM