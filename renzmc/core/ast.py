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


class AST:

    def __init__(self, token=None):
        self.token = token
        self.line = token.line if token else None
        self.column = token.column if token else None


class Program(AST):

    def __init__(self, statements):
        super().__init__()
        self.statements = statements


class Block(AST):

    def __init__(self, statements):
        super().__init__()
        self.statements = statements


class BinOp(AST):

    def __init__(self, left, op, right):
        super().__init__(op)
        self.left = left
        self.op = op
        self.right = right


class UnaryOp(AST):

    def __init__(self, op, expr):
        super().__init__(op)
        self.op = op
        self.expr = expr


class Num(AST):

    def __init__(self, token):
        super().__init__(token)
        self.value = token.value


class String(AST):

    def __init__(self, token):
        super().__init__(token)
        self.value = token.value


class Boolean(AST):

    def __init__(self, token):
        super().__init__(token)
        self.value = token.value


class NoneValue(AST):

    def __init__(self, token):
        super().__init__(token)
        self.value = None


class List(AST):

    def __init__(self, elements, token=None):
        super().__init__(token)
        self.elements = elements


class Dict(AST):

    def __init__(self, pairs, token=None):
        super().__init__(token)
        self.pairs = pairs


class Set(AST):

    def __init__(self, elements, token=None):
        super().__init__(token)
        self.elements = elements


class Tuple(AST):

    def __init__(self, elements, token=None):
        super().__init__(token)
        self.elements = elements


class DictComp(AST):

    def __init__(
        self, key_expr, value_expr, var_name, iterable, condition=None, token=None
    ):
        super().__init__(token)
        self.key_expr = key_expr
        self.value_expr = value_expr
        self.var_name = var_name
        self.iterable = iterable
        self.condition = condition


class Var(AST):

    def __init__(self, token):
        super().__init__(token)
        self.name = token.value


class VarDecl(AST):

    def __init__(self, var_name, value, token=None, type_hint=None):
        super().__init__(token)
        self.var_name = var_name
        self.value = value
        self.type_hint = type_hint


class Assign(AST):

    def __init__(self, var, value, token=None):
        super().__init__(token)
        self.var = var
        self.value = value


class MultiVarDecl(AST):

    def __init__(self, var_names, values, token=None, type_hints=None):
        super().__init__(token)
        self.var_names = var_names
        self.values = values
        self.type_hints = type_hints or {}


class MultiAssign(AST):

    def __init__(self, vars, values, token=None):
        super().__init__(token)
        self.vars = vars
        self.values = values


class NoOp(AST):
    pass


class Print(AST):

    def __init__(self, expr, token=None):
        super().__init__(token)
        self.expr = expr


class Input(AST):

    def __init__(self, prompt, var_name=None, token=None):
        super().__init__(token)
        self.prompt = prompt
        self.var_name = var_name


class If(AST):

    def __init__(self, condition, if_body, else_body=None, token=None):
        super().__init__(token)
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body


class While(AST):

    def __init__(self, condition, body, token=None):
        super().__init__(token)
        self.condition = condition
        self.body = body


class For(AST):

    def __init__(self, var_name, start, end, body, token=None):
        super().__init__(token)
        self.var_name = var_name
        self.start = start
        self.end = end
        self.body = body


class ForEach(AST):

    def __init__(self, var_name, iterable, body, token=None):
        super().__init__(token)
        self.var_name = var_name
        self.iterable = iterable
        self.body = body


class Break(AST):

    def __init__(self, token=None):
        super().__init__(token)


class Continue(AST):

    def __init__(self, token=None):
        super().__init__(token)


class FuncDecl(AST):

    def __init__(
        self, name, params, body, token=None, return_type=None, param_types=None
    ):
        super().__init__(token)
        self.name = name
        self.params = params
        self.body = body
        self.return_type = return_type
        self.param_types = param_types


class FuncCall(AST):

    def __init__(self, name_or_expr, args, token=None, kwargs=None):
        super().__init__(token)
        if isinstance(name_or_expr, str):
            self.name = name_or_expr
            self.func_expr = None
        else:
            self.name = None
            self.func_expr = name_or_expr
        self.args = args
        self.kwargs = kwargs or {}


class Return(AST):

    def __init__(self, expr=None, token=None):
        super().__init__(token)
        self.expr = expr


class ClassDecl(AST):

    def __init__(self, name, methods, parent=None, token=None, class_vars=None):
        super().__init__(token)
        self.name = name
        self.methods = methods
        self.parent = parent
        self.class_vars = class_vars or []


class MethodDecl(AST):

    def __init__(
        self, name, params, body, token=None, return_type=None, param_types=None
    ):
        super().__init__(token)
        self.name = name
        self.params = params
        self.body = body
        self.return_type = return_type
        self.param_types = param_types


class Constructor(AST):

    def __init__(self, params, body, token=None, param_types=None):
        super().__init__(token)
        self.params = params
        self.body = body
        self.param_types = param_types


class AttributeRef(AST):

    def __init__(self, obj, attr, token=None):
        super().__init__(token)
        self.obj = obj
        self.attr = attr


class MethodCall(AST):

    def __init__(self, obj, method, args, token=None, kwargs=None):
        super().__init__(token)
        self.obj = obj
        self.method = method
        self.args = args
        self.kwargs = kwargs or {}


class Import(AST):

    def __init__(self, module, alias=None, token=None):
        super().__init__(token)
        self.module = module
        self.alias = alias


class FromImport(AST):
    """
    AST node for 'from module import item1, item2' statements
    Supports:
    - Simple and nested module paths (e.g., 'from Ren.renz import Class')
    - Wildcard imports (e.g., 'from module import *')
    - Relative imports (e.g., 'from .module import func')
    """

    def __init__(self, module, items, token=None, is_relative=False, relative_level=0):
        super().__init__(token)
        self.module = module  # Module path (can be dot-separated like "Ren.renz")
        self.items = items  # List of (name, alias) tuples to import
        self.is_relative = is_relative  # True if relative import (starts with .)
        self.relative_level = relative_level  # Number of dots (1 for ., 2 for .., etc.)


class PythonImport(AST):

    def __init__(self, module, alias=None, token=None):
        super().__init__(token)
        self.module = module
        self.alias = alias


class PythonCall(AST):

    def __init__(self, func_expr, args, token=None, kwargs=None):
        super().__init__(token)
        self.func_expr = func_expr
        self.args = args
        self.kwargs = kwargs if kwargs is not None else {}


class TryCatch(AST):

    def __init__(self, try_block, except_blocks, finally_block=None, token=None):
        super().__init__(token)
        self.try_block = try_block
        self.except_blocks = except_blocks
        self.finally_block = finally_block


class Raise(AST):

    def __init__(self, exception, token=None):
        super().__init__(token)
        self.exception = exception


class IndexAccess(AST):

    def __init__(self, obj, index, token=None):
        super().__init__(token)
        self.obj = obj
        self.index = index


class SliceAccess(AST):

    def __init__(self, obj, start, end=None, step=None, token=None):
        super().__init__(token)
        self.obj = obj
        self.start = start
        self.end = end
        self.step = step


class SelfVar(AST):

    def __init__(self, name, token=None):
        super().__init__(token)
        self.name = name


class Lambda(AST):

    def __init__(self, params, body, token=None, param_types=None, return_type=None):
        super().__init__(token)
        self.params = params
        self.body = body
        self.param_types = param_types
        self.return_type = return_type


class ListComp(AST):

    def __init__(self, expr, var_name, iterable, condition=None, token=None):
        super().__init__(token)
        self.expr = expr
        self.var_name = var_name
        self.iterable = iterable
        self.condition = condition


class SetComp(AST):

    def __init__(self, expr, var_name, iterable, condition=None, token=None):
        super().__init__(token)
        self.expr = expr
        self.var_name = var_name
        self.iterable = iterable
        self.condition = condition


class Generator(AST):

    def __init__(self, expr, var_name, iterable, condition=None, token=None):
        super().__init__(token)
        self.expr = expr
        self.var_name = var_name
        self.iterable = iterable
        self.condition = condition


class Yield(AST):

    def __init__(self, expr=None, token=None):
        super().__init__(token)
        self.expr = expr


class YieldFrom(AST):

    def __init__(self, expr, token=None):
        super().__init__(token)
        self.expr = expr


class Decorator(AST):

    def __init__(self, name, args, decorated, token=None):
        super().__init__(token)
        self.name = name
        self.args = args
        self.decorated = decorated


class AsyncFuncDecl(AST):

    def __init__(
        self, name, params, body, token=None, return_type=None, param_types=None
    ):
        super().__init__(token)
        self.name = name
        self.params = params
        self.body = body
        self.return_type = return_type
        self.param_types = param_types


class AsyncMethodDecl(AST):

    def __init__(
        self, name, params, body, token=None, return_type=None, param_types=None
    ):
        super().__init__(token)
        self.name = name
        self.params = params
        self.body = body
        self.return_type = return_type
        self.param_types = param_types


class Await(AST):

    def __init__(self, expr, token=None):
        super().__init__(token)
        self.expr = expr


class TypeHint(AST):

    def __init__(self, type_name, token=None):
        super().__init__(token)
        self.type_name = type_name


class FormatString(AST):

    def __init__(self, parts, token=None):
        super().__init__(token)
        self.parts = parts


class Ternary(AST):

    def __init__(self, condition, if_expr, else_expr, token=None):
        super().__init__(token)
        self.condition = condition
        self.if_expr = if_expr
        self.else_expr = else_expr


class Unpacking(AST):

    def __init__(self, expr, token=None):
        super().__init__(token)
        self.expr = expr


class WalrusOperator(AST):

    def __init__(self, var_name, value, token=None):
        super().__init__(token)
        self.var_name = var_name
        self.value = value


class CompoundAssign(AST):

    def __init__(self, var, op, value, token=None):
        super().__init__(token)
        self.var = var
        self.op = op
        self.value = value


class Switch(AST):

    def __init__(self, expr, cases, default_case=None, token=None):
        super().__init__(token)
        self.expr = expr
        self.cases = cases
        self.default_case = default_case


class Case(AST):

    def __init__(self, values, body, token=None):
        super().__init__(token)
        self.values = values
        self.body = body


class With(AST):

    def __init__(self, context_expr, var_name, body, token=None):
        super().__init__(token)
        self.context_expr = context_expr
        self.var_name = var_name
        self.body = body


class SliceAssign(AST):

    def __init__(self, target, start, end, step, value, token):
        self.target = target
        self.start = start
        self.end = end
        self.step = step
        self.value = value
        self.token = token


class ExtendedUnpacking(AST):

    def __init__(self, targets, value, token):
        self.targets = targets
        self.value = value
        self.token = token


class StarredExpr(AST):

    def __init__(self, expr, token):
        self.expr = expr
        self.token = token


class PropertyDecl(AST):

    def __init__(self, name, getter, setter=None, deleter=None, token=None):
        self.name = name
        self.getter = getter
        self.setter = setter
        self.deleter = deleter
        self.token = token


class StaticMethodDecl(AST):

    def __init__(self, name, func, token=None):
        self.name = name
        self.func = func
        self.token = token


class ClassMethodDecl(AST):

    def __init__(self, name, func, token=None):
        self.name = name
        self.func = func
        self.token = token


class TypeAlias(AST):

    def __init__(self, name, type_expr, token=None):
        super().__init__(token)
        self.name = name
        self.type_expr = type_expr


class LiteralType(AST):

    def __init__(self, values, token=None):
        super().__init__(token)
        self.values = values


class TypedDictType(AST):

    def __init__(self, fields, token=None):
        super().__init__(token)
        self.fields = fields
