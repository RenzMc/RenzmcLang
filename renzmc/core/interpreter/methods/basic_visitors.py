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
RenzmcLang Interpreter Basic Visitors Module

This module contains basic visitors methods.
"""


try:
    from renzmc.jit import JITCompiler

    JIT_AVAILABLE = True
except ImportError:
    JIT_AVAILABLE = False
    JITCompiler = None


class BasicVisitorsMixin:
    """
    Mixin class for basic visitors.

    Provides 12 methods for handling basic visitors.
    """

    def visit_Program(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
        return result

    def visit_Block(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
            if self.return_value is not None or self.break_flag or self.continue_flag:
                break
        return result

    def visit_Num(self, node):
        return node.value

    def visit_String(self, node):
        return node.value

    def visit_Boolean(self, node):
        return node.value

    def visit_NoneValue(self, node):
        return None

    def visit_List(self, node):
        return [self.visit(element) for element in node.elements]

    def visit_Dict(self, node):
        return {self.visit(key): self.visit(value) for key, value in node.pairs}

    def visit_Set(self, node):
        return {self.visit(element) for element in node.elements}

    def visit_Tuple(self, node):
        return tuple((self.visit(element) for element in node.elements))

    def visit_NoOp(self, node):
        pass

    def visit_NoneType(self, node):
        return None
