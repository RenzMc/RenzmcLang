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

import builtins as py_builtins

from renzmc.core.ast import (
    AttributeRef,
    IndexAccess,
    Var,
)
from renzmc.core.error import TypeHintError
from renzmc.core.token import TokenType
from renzmc.utils.error_handler import log_exception

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class StatementVisitorsMixin:
    """
    Mixin class for statement visitors.

    Provides 9 methods for handling statement visitors.
    """

    def visit_Var(self, node):
        return self.get_variable(node.name)

    def visit_VarDecl(self, node):
        value = self.visit(node.value)

        if node.type_hint:
            try:
                self._check_variable_type(node.var_name, value, node.type_hint)
            except Exception:
                type_name = node.type_hint.type_name
                if type_name in self.type_registry:
                    expected_type = self.type_registry[type_name]
                    try:
                        if isinstance(expected_type, type) and not isinstance(value, expected_type):
                            raise TypeHintError(f"Nilai '{value}' bukan tipe '{type_name}'")
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")
                elif hasattr(py_builtins, type_name):
                    expected_type = getattr(py_builtins, type_name)
                    try:
                        if isinstance(expected_type, type) and not isinstance(value, expected_type):
                            raise TypeHintError(f"Nilai '{value}' bukan tipe '{type_name}'")
                    except TypeError as e:
                        # Type checking failed - this is expected for non-type objects
                        log_exception("type validation", e, level="debug")

        return self.set_variable(node.var_name, value)

    def visit_Assign(self, node):
        value = self.visit(node.value)
        if isinstance(node.var, Var):
            return self.set_variable(node.var.name, value)
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                self.instance_scopes[id(obj)][attr] = value
                return value
            elif hasattr(obj, attr):
                setattr(obj, attr, value)
                return value
            elif isinstance(obj, dict):
                obj[attr] = value
                return value
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            if isinstance(obj, (list, dict)):
                obj[index] = value
                return value
            else:
                raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan")
        raise RuntimeError(f"Tipe assignment tidak didukung: {type(node.var).__name__}")

    def visit_CompoundAssign(self, node):

        if isinstance(node.var, Var):
            current_value = self.get_variable(node.var.name)
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            current_value = obj[index]
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                current_value = self.instance_scopes[id(obj)].get(attr)
            elif hasattr(obj, attr):
                current_value = getattr(obj, attr)
            elif isinstance(obj, dict):
                current_value = obj[attr]
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
        else:
            raise RuntimeError(
                f"Tipe compound assignment tidak didukung: {type(node.var).__name__}"
            )
        operand = self.visit(node.value)
        if node.op.type == TokenType.TAMBAH_SAMA_DENGAN:
            new_value = current_value + operand
        elif node.op.type == TokenType.KURANG_SAMA_DENGAN:
            new_value = current_value - operand
        elif node.op.type == TokenType.KALI_SAMA_DENGAN:
            new_value = current_value * operand
        elif node.op.type == TokenType.BAGI_SAMA_DENGAN:
            new_value = current_value / operand
        elif node.op.type == TokenType.SISA_SAMA_DENGAN:
            new_value = current_value % operand
        elif node.op.type == TokenType.PANGKAT_SAMA_DENGAN:
            new_value = current_value**operand
        elif node.op.type == TokenType.PEMBAGIAN_BULAT_SAMA_DENGAN:
            new_value = current_value // operand
        elif node.op.type in (
            TokenType.BIT_DAN_SAMA_DENGAN,
            TokenType.BITWISE_AND_SAMA_DENGAN,
        ):
            new_value = current_value & operand
        elif node.op.type in (
            TokenType.BIT_ATAU_SAMA_DENGAN,
            TokenType.BITWISE_OR_SAMA_DENGAN,
        ):
            new_value = current_value | operand
        elif node.op.type in (
            TokenType.BIT_XOR_SAMA_DENGAN,
            TokenType.BITWISE_XOR_SAMA_DENGAN,
        ):
            new_value = current_value ^ operand
        elif node.op.type == TokenType.GESER_KIRI_SAMA_DENGAN:
            new_value = current_value << operand
        elif node.op.type == TokenType.GESER_KANAN_SAMA_DENGAN:
            new_value = current_value >> operand
        else:
            raise RuntimeError(f"Operator compound assignment tidak dikenal: {node.op.type}")
        if isinstance(node.var, Var):
            return self.set_variable(node.var.name, new_value)
        elif isinstance(node.var, IndexAccess):
            obj = self.visit(node.var.obj)
            index = self.visit(node.var.index)
            obj[index] = new_value
            return new_value
        elif isinstance(node.var, AttributeRef):
            obj = self.visit(node.var.obj)
            attr = node.var.attr
            if id(obj) in self.instance_scopes:
                self.instance_scopes[id(obj)][attr] = new_value
            elif hasattr(obj, attr):
                setattr(obj, attr, new_value)
            elif isinstance(obj, dict):
                obj[attr] = new_value
            else:
                raise AttributeError(
                    f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                )
            return new_value

    def visit_MultiVarDecl(self, node):
        values = self.visit(node.values)
        if isinstance(values, (list, tuple)):
            if len(node.var_names) != len(values):
                raise ValueError(
                    f"Tidak dapat membongkar {len(values)} nilai menjadi {len(node.var_names)} variabel"
                )
            results = []
            for var_name, value in zip(node.var_names, values):
                result = self.set_variable(var_name, value)
                results.append(result)
            return tuple(results)
        elif len(node.var_names) == 1:
            return self.set_variable(node.var_names[0], values)
        else:
            raise ValueError(
                f"Tidak dapat membongkar 1 nilai menjadi {len(node.var_names)} variabel"
            )

    def visit_MultiAssign(self, node):
        values = self.visit(node.values)
        if isinstance(values, (list, tuple)):
            if len(node.vars) != len(values):
                raise ValueError(
                    f"Tidak dapat membongkar {len(values)} nilai menjadi {len(node.vars)} variabel"
                )
            results = []
            for var_node, value in zip(node.vars, values):
                if isinstance(var_node, Var):
                    result = self.set_variable(var_node.name, value)
                elif isinstance(var_node, AttributeRef):
                    obj = self.visit(var_node.obj)
                    attr = var_node.attr
                    if hasattr(obj, attr):
                        setattr(obj, attr, value)
                    elif isinstance(obj, dict):
                        obj[attr] = value
                    else:
                        raise AttributeError(
                            f"Objek '{type(obj).__name__}' tidak memiliki atribut '{attr}'"
                        )
                    result = value
                elif isinstance(var_node, IndexAccess):
                    obj = self.visit(var_node.obj)
                    index = self.visit(var_node.index)
                    if isinstance(obj, (list, dict)):
                        obj[index] = value
                    else:
                        raise TypeError(
                            f"Objek tipe '{type(obj).__name__}' tidak mendukung pengindeksan"
                        )
                    result = value
                else:
                    raise RuntimeError(f"Tipe assignment tidak didukung: {type(var_node).__name__}")
                results.append(result)
            return tuple(results)
        elif len(node.vars) == 1:
            var_node = node.vars[0]
            if isinstance(var_node, Var):
                return self.set_variable(var_node.name, values)
            else:
                from renzmc.core.ast import Assign as AssignNode

                temp_assign = AssignNode(var_node, node.values)
                return self.visit_Assign(temp_assign)
        else:
            raise ValueError(f"Tidak dapat membongkar 1 nilai menjadi {len(node.vars)} variabel")

    def visit_Print(self, node):
        value = self.visit(node.expr)
        print(value)
        return None

    def visit_Input(self, node):
        prompt = self.visit(node.prompt)
        value = input(prompt)
        if node.var_name:
            try:
                int_value = int(value)
                self.set_variable(node.var_name, int_value)
                return int_value
            except ValueError:
                try:
                    float_value = float(value)
                    self.set_variable(node.var_name, float_value)
                    return float_value
                except ValueError:
                    self.set_variable(node.var_name, value)
                    return value
        return value

    def visit_SliceAssign(self, node):
        target = self.visit(node.target)
        start = self.visit(node.start) if node.start else None
        end = self.visit(node.end) if node.end else None
        step = self.visit(node.step) if node.step else None
        value = self.visit(node.value)
        try:
            slice_obj = slice(start, end, step)
            target[slice_obj] = value
        except Exception as e:
            self.error(f"Kesalahan dalam slice assignment: {str(e)}", node.token)
