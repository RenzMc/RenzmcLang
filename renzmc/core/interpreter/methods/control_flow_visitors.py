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
RenzmcLang Interpreter Control Flow Visitors Module

This module contains control flow visitors methods.
"""


from renzmc.core.ast import Block

try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class ControlFlowVisitorsMixin:
    """
    Mixin class for control flow visitors.

    Provides 11 methods for handling control flow visitors.
    """

    def visit_If(self, node):
        condition = self.visit(node.condition)
        if condition:
            if_block = Block(node.if_body)
            return self.visit(if_block)
        elif node.else_body:
            else_block = Block(node.else_body)
            return self.visit(else_block)
        return None

    def visit_While(self, node):
        result = None
        while self.visit(node.condition):
            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_For(self, node):
        var_name = node.var_name
        start = self.visit(node.start)
        end = self.visit(node.end)
        result = None
        for i in range(start, end + 1):
            self.set_variable(var_name, i)
            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_ForEach(self, node):
        var_name = node.var_name
        iterable = self.visit(node.iterable)
        result = None
        if not hasattr(iterable, "__iter__"):
            raise TypeError(f"Objek tipe '{type(iterable).__name__}' tidak dapat diiterasi")
        for item in iterable:
            if isinstance(var_name, tuple):
                if hasattr(item, "__iter__") and not isinstance(item, str):
                    unpacked = list(item)
                    if len(unpacked) != len(var_name):
                        raise ValueError(
                            f"Tidak dapat unpack {len(unpacked)} nilai ke {len(var_name)} variabel"  # noqa: E501
                        )
                    for var, val in zip(var_name, unpacked):
                        self.set_variable(var, val)
                else:
                    raise TypeError(f"Tidak dapat unpack nilai tipe '{type(item).__name__}'")
            else:
                self.set_variable(var_name, item)

            body_block = Block(node.body)
            result = self.visit(body_block)
            if self.break_flag:
                self.break_flag = False
                break
            if self.continue_flag:
                self.continue_flag = False
                continue
            if self.return_value is not None:
                break
        return result

    def visit_Break(self, node):
        self.break_flag = True

    def visit_Continue(self, node):
        self.continue_flag = True

    def visit_TryCatch(self, node):
        try:
            return self.visit_Block(Block(node.try_block))
        except Exception as e:
            for exception_type, var_name, except_block in node.except_blocks:
                should_catch = False
                if exception_type is None:
                    should_catch = True
                else:
                    try:
                        exc_type = eval(exception_type)
                        if isinstance(exc_type, type):
                            should_catch = isinstance(e, exc_type)
                    except Exception:
                        should_catch = True

                if should_catch:
                    if var_name:
                        self.set_variable(var_name, e)
                    return self.visit_Block(Block(except_block))
            raise e
        finally:
            if node.finally_block:
                self.visit_Block(Block(node.finally_block))

    def visit_Raise(self, node):
        exception = self.visit(node.exception)
        raise exception

    def visit_Switch(self, node):
        match_value = self.visit(node.expr)
        for case in node.cases:
            for case_value_node in case.values:
                case_value = self.visit(case_value_node)
                if match_value == case_value:
                    return self.visit_Block(Block(case.body))
        if node.default_case:
            return self.visit_Block(Block(node.default_case))
        return None

    def visit_Case(self, node):
        pass

    def visit_With(self, node):
        context_manager = self.visit(node.context_expr)
        if not (hasattr(context_manager, "__enter__") and hasattr(context_manager, "__exit__")):
            raise TypeError(
                f"Objek tipe '{type(context_manager).__name__}' tidak mendukung context manager protocol"  # noqa: E501
            )
        context_value = context_manager.__enter__()
        if node.var_name:
            self.set_variable(node.var_name, context_value)
        try:
            result = self.visit_Block(Block(node.body))
            return result
        except Exception as e:
            exc_type = type(e)
            exc_value = e
            exc_traceback = e.__traceback__
            if not context_manager.__exit__(exc_type, exc_value, exc_traceback):
                raise
        finally:
            if not hasattr(self, "_exception_occurred"):
                context_manager.__exit__(None, None, None)
