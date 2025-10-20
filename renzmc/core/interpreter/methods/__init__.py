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



from renzmc.core.interpreter.methods.advanced_visitors import AdvancedVisitorsMixin
from renzmc.core.interpreter.methods.basic_visitors import BasicVisitorsMixin
from renzmc.core.interpreter.methods.class_visitors import ClassVisitorsMixin
from renzmc.core.interpreter.methods.control_flow_visitors import (
    ControlFlowVisitorsMixin,
)
from renzmc.core.interpreter.methods.execution_helpers import ExecutionHelpersMixin
from renzmc.core.interpreter.methods.expression_visitors import (
    ExpressionVisitorsMixin,
)
from renzmc.core.interpreter.methods.function_visitors import FunctionVisitorsMixin
from renzmc.core.interpreter.methods.import_visitors import ImportVisitorsMixin
from renzmc.core.interpreter.methods.statement_visitors import StatementVisitorsMixin


class ExecutionMethodsMixin(
    BasicVisitorsMixin,
    ExpressionVisitorsMixin,
    StatementVisitorsMixin,
    FunctionVisitorsMixin,
    ClassVisitorsMixin,
    ImportVisitorsMixin,
    ControlFlowVisitorsMixin,
    AdvancedVisitorsMixin,
    ExecutionHelpersMixin,
):
    """
    Combined mixin class for all execution and visitor methods.

    This class combines all visitor method mixins to provide complete
    AST interpretation functionality.

    Functionality Areas:
        - BasicVisitorsMixin: Basic AST node visitors (Program, Block, literals)
        - ExpressionVisitorsMixin: Expression evaluation (BinOp, UnaryOp, etc.)
        - StatementVisitorsMixin: Statement execution (Assign, VarDecl, etc.)
        - FunctionVisitorsMixin: Function handling (FuncDecl, FuncCall, etc.)
        - ClassVisitorsMixin: Class and OOP features (ClassDecl, MethodCall, etc.)
        - ImportVisitorsMixin: Import statement handling
        - ControlFlowVisitorsMixin: Control flow (If, While, For, etc.)
        - AdvancedVisitorsMixin: Advanced features (Decorator, comprehensions, etc.)
        - ExecutionHelpersMixin: Helper methods for execution
    """


__all__ = ["ExecutionMethodsMixin"]
