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

import json
from typing import Any, Dict


class ASTSerializer:
    """
    Serializes AST nodes to JSON for Rust compiler consumption.

    This class converts Python AST objects into JSON representations
    that can be understood by the Rust bytecode compiler.
    """

    def serialize(self, ast_node) -> Dict[str, Any]:
        """
        Serialize an AST node to a dictionary.

        Args:
            ast_node: The AST node to serialize

        Returns:
            Dictionary representation of the AST node
        """
        if ast_node is None:
            return {"type": "None"}

        node_type = ast_node.__class__.__name__
        result = {"type": node_type}

        # Add position information if available
        if hasattr(ast_node, "line") and ast_node.line is not None:
            result["line"] = ast_node.line
        if hasattr(ast_node, "column") and ast_node.column is not None:
            result["column"] = ast_node.column

        # Serialize based on node type
        method_name = f"_serialize_{node_type.lower()}"
        if hasattr(self, method_name):
            getattr(self, method_name)(ast_node, result)
        else:
            self._serialize_generic(ast_node, result)

        return result

    def _serialize_generic(self, ast_node, result: Dict[str, Any]):
        """Generic serialization for unknown node types."""
        for attr_name in dir(ast_node):
            if not attr_name.startswith("_") and not callable(getattr(ast_node, attr_name)):
                if attr_name not in ["line", "column", "token"]:
                    value = getattr(ast_node, attr_name)
                    if value is not None:
                        result[attr_name] = self._serialize_value(value)

    def _serialize_program(self, ast_node, result: Dict[str, Any]):
        """Serialize Program node."""
        result["statements"] = [self.serialize(stmt) for stmt in ast_node.statements]

    def _serialize_block(self, ast_node, result: Dict[str, Any]):
        """Serialize Block node."""
        result["statements"] = [self.serialize(stmt) for stmt in ast_node.statements]

    def _serialize_binop(self, ast_node, result: Dict[str, Any]):
        """Serialize BinOp node."""
        result["left"] = self.serialize(ast_node.left)
        result["op"] = {"type": ast_node.op.type, "value": ast_node.op.value}
        result["right"] = self.serialize(ast_node.right)

    def _serialize_unaryop(self, ast_node, result: Dict[str, Any]):
        """Serialize UnaryOp node."""
        result["op"] = {"type": ast_node.op.type, "value": ast_node.op.value}
        result["expr"] = self.serialize(ast_node.expr)

    def _serialize_num(self, ast_node, result: Dict[str, Any]):
        """Serialize Num node."""
        result["value"] = ast_node.value

    def _serialize_string(self, ast_node, result: Dict[str, Any]):
        """Serialize String node."""
        result["value"] = ast_node.value

    def _serialize_boolean(self, ast_node, result: Dict[str, Any]):
        """Serialize Boolean node."""
        result["value"] = ast_node.value

    def _serialize_nonevalue(self, ast_node, result: Dict[str, Any]):
        """Serialize NoneValue node."""
        result["value"] = None

    def _serialize_list(self, ast_node, result: Dict[str, Any]):
        """Serialize List node."""
        result["elements"] = [self.serialize(elem) for elem in ast_node.elements]

    def _serialize_dict(self, ast_node, result: Dict[str, Any]):
        """Serialize Dict node."""
        result["pairs"] = [
            {"key": self.serialize(key), "value": self.serialize(value)}
            for key, value in ast_node.pairs
        ]

    def _serialize_set(self, ast_node, result: Dict[str, Any]):
        """Serialize Set node."""
        result["elements"] = [self.serialize(elem) for elem in ast_node.elements]

    def _serialize_tuple(self, ast_node, result: Dict[str, Any]):
        """Serialize Tuple node."""
        result["elements"] = [self.serialize(elem) for elem in ast_node.elements]

    def _serialize_var(self, ast_node, result: Dict[str, Any]):
        """Serialize Var node."""
        result["name"] = ast_node.name

    def _serialize_vardecl(self, ast_node, result: Dict[str, Any]):
        """Serialize VarDecl node."""
        result["var_name"] = ast_node.var_name
        result["value"] = self.serialize(ast_node.value)
        if hasattr(ast_node, "type_hint") and ast_node.type_hint:
            result["type_hint"] = self.serialize(ast_node.type_hint)

    def _serialize_assign(self, ast_node, result: Dict[str, Any]):
        """Serialize Assign node."""
        result["var"] = self.serialize(ast_node.var)
        result["value"] = self.serialize(ast_node.value)

    def _serialize_print(self, ast_node, result: Dict[str, Any]):
        """Serialize Print node."""
        result["expr"] = self.serialize(ast_node.expr)

    def _serialize_input(self, ast_node, result: Dict[str, Any]):
        """Serialize Input node."""
        result["prompt"] = self.serialize(ast_node.prompt)
        if ast_node.var_name:
            result["var_name"] = ast_node.var_name

    def _serialize_if(self, ast_node, result: Dict[str, Any]):
        """Serialize If node."""
        result["condition"] = self.serialize(ast_node.condition)
        result["if_body"] = self.serialize(ast_node.if_body)
        if ast_node.else_body:
            result["else_body"] = self.serialize(ast_node.else_body)

    def _serialize_while(self, ast_node, result: Dict[str, Any]):
        """Serialize While node."""
        result["condition"] = self.serialize(ast_node.condition)
        result["body"] = self.serialize(ast_node.body)

    def _serialize_for(self, ast_node, result: Dict[str, Any]):
        """Serialize For node."""
        result["var_name"] = ast_node.var_name
        result["start"] = self.serialize(ast_node.start)
        result["end"] = self.serialize(ast_node.end)
        result["body"] = self.serialize(ast_node.body)

    def _serialize_foreach(self, ast_node, result: Dict[str, Any]):
        """Serialize ForEach node."""
        result["var_name"] = ast_node.var_name
        result["iterable"] = self.serialize(ast_node.iterable)
        result["body"] = self.serialize(ast_node.body)

    def _serialize_funcdecl(self, ast_node, result: Dict[str, Any]):
        """Serialize FuncDecl node."""
        result["name"] = ast_node.name
        result["params"] = [self.serialize(param) for param in ast_node.params]
        result["body"] = self.serialize(ast_node.body)
        if hasattr(ast_node, "return_type") and ast_node.return_type:
            result["return_type"] = self.serialize(ast_node.return_type)
        if hasattr(ast_node, "param_types") and ast_node.param_types:
            result["param_types"] = ast_node.param_types

    def _serialize_funccall(self, ast_node, result: Dict[str, Any]):
        """Serialize FuncCall node."""
        if hasattr(ast_node, "name") and ast_node.name:
            result["name"] = ast_node.name
        else:
            result["name_expr"] = self.serialize(ast_node.name_or_expr)
        result["args"] = [self.serialize(arg) for arg in ast_node.args]
        if hasattr(ast_node, "kwargs") and ast_node.kwargs:
            result["kwargs"] = {
                key: self.serialize(value) for key, value in ast_node.kwargs.items()
            }

    def _serialize_return(self, ast_node, result: Dict[str, Any]):
        """Serialize Return node."""
        if ast_node.expr:
            result["expr"] = self.serialize(ast_node.expr)

    def _serialize_classdecl(self, ast_node, result: Dict[str, Any]):
        """Serialize ClassDecl node."""
        result["name"] = ast_node.name
        result["methods"] = [self.serialize(method) for method in ast_node.methods]
        if ast_node.parent:
            result["parent"] = self.serialize(ast_node.parent)
        if hasattr(ast_node, "class_vars") and ast_node.class_vars:
            result["class_vars"] = [self.serialize(var) for var in ast_node.class_vars]

    def _serialize_attributeref(self, ast_node, result: Dict[str, Any]):
        """Serialize AttributeRef node."""
        result["obj"] = self.serialize(ast_node.obj)
        result["attr"] = self.serialize(ast_node.attr)

    def _serialize_methodcall(self, ast_node, result: Dict[str, Any]):
        """Serialize MethodCall node."""
        result["obj"] = self.serialize(ast_node.obj)
        result["method"] = self.serialize(ast_node.method)
        result["args"] = [self.serialize(arg) for arg in ast_node.args]
        if hasattr(ast_node, "kwargs") and ast_node.kwargs:
            result["kwargs"] = {
                key: self.serialize(value) for key, value in ast_node.kwargs.items()
            }

    def _serialize_import(self, ast_node, result: Dict[str, Any]):
        """Serialize Import node."""
        result["module"] = ast_node.module
        if ast_node.alias:
            result["alias"] = ast_node.alias

    def _serialize_fromimport(self, ast_node, result: Dict[str, Any]):
        """Serialize FromImport node."""
        result["module"] = ast_node.module
        result["imports"] = ast_node.imports
        if ast_node.alias:
            result["alias"] = ast_node.alias

    def _serialize_pythonimport(self, ast_node, result: Dict[str, Any]):
        """Serialize PythonImport node."""
        result["module"] = ast_node.module
        if ast_node.alias:
            result["alias"] = ast_node.alias

    def _serialize_pythontcall(self, ast_node, result: Dict[str, Any]):
        """Serialize PythonCall node."""
        result["func_expr"] = self.serialize(ast_node.func_expr)
        result["args"] = [self.serialize(arg) for arg in ast_node.args]
        if hasattr(ast_node, "kwargs") and ast_node.kwargs:
            result["kwargs"] = {
                key: self.serialize(value) for key, value in ast_node.kwargs.items()
            }

    def _serialize_trycatch(self, ast_node, result: Dict[str, Any]):
        """Serialize TryCatch node."""
        result["try_block"] = self.serialize(ast_node.try_block)
        result["except_blocks"] = [self.serialize(block) for block in ast_node.except_blocks]
        if ast_node.finally_block:
            result["finally_block"] = self.serialize(ast_node.finally_block)

    def _serialize_raise(self, ast_node, result: Dict[str, Any]):
        """Serialize Raise node."""
        result["exception"] = self.serialize(ast_node.exception)

    def _serialize_indexaccess(self, ast_node, result: Dict[str, Any]):
        """Serialize IndexAccess node."""
        result["obj"] = self.serialize(ast_node.obj)
        result["index"] = self.serialize(ast_node.index)

    def _serialize_sliceaccess(self, ast_node, result: Dict[str, Any]):
        """Serialize SliceAccess node."""
        result["obj"] = self.serialize(ast_node.obj)
        result["start"] = self.serialize(ast_node.start)
        if ast_node.end:
            result["end"] = self.serialize(ast_node.end)
        if ast_node.step:
            result["step"] = self.serialize(ast_node.step)

    def _serialize_selfvar(self, ast_node, result: Dict[str, Any]):
        """Serialize SelfVar node."""
        result["name"] = ast_node.name

    def _serialize_lambda(self, ast_node, result: Dict[str, Any]):
        """Serialize Lambda node."""
        result["params"] = [self.serialize(param) for param in ast_node.params]
        result["body"] = self.serialize(ast_node.body)

    def _serialize_listcomp(self, ast_node, result: Dict[str, Any]):
        """Serialize ListComp node."""
        result["expr"] = self.serialize(ast_node.expr)
        result["var_name"] = ast_node.var_name
        result["iterable"] = self.serialize(ast_node.iterable)
        if ast_node.condition:
            result["condition"] = self.serialize(ast_node.condition)

    def _serialize_setcomp(self, ast_node, result: Dict[str, Any]):
        """Serialize SetComp node."""
        result["expr"] = self.serialize(ast_node.expr)
        result["var_name"] = ast_node.var_name
        result["iterable"] = self.serialize(ast_node.iterable)
        if ast_node.condition:
            result["condition"] = self.serialize(ast_node.condition)

    def _serialize_generator(self, ast_node, result: Dict[str, Any]):
        """Serialize Generator node."""
        result["expr"] = self.serialize(ast_node.expr)
        result["var_name"] = ast_node.var_name
        result["iterable"] = self.serialize(ast_node.iterable)
        if ast_node.condition:
            result["condition"] = self.serialize(ast_node.condition)

    def _serialize_yield(self, ast_node, result: Dict[str, Any]):
        """Serialize Yield node."""
        if ast_node.expr:
            result["expr"] = self.serialize(ast_node.expr)

    def _serialize_yieldfrom(self, ast_node, result: Dict[str, Any]):
        """Serialize YieldFrom node."""
        result["expr"] = self.serialize(ast_node.expr)

    def _serialize_decorator(self, ast_node, result: Dict[str, Any]):
        """Serialize Decorator node."""
        result["name"] = ast_node.name
        result["args"] = [self.serialize(arg) for arg in ast_node.args]
        result["decorated"] = self.serialize(ast_node.decorated)

    def _serialize_asyncfuncdecl(self, ast_node, result: Dict[str, Any]):
        """Serialize AsyncFuncDecl node."""
        result["name"] = ast_node.name
        result["params"] = [self.serialize(param) for param in ast_node.params]
        result["body"] = self.serialize(ast_node.body)
        result["is_async"] = True

    def _serialize_await(self, ast_node, result: Dict[str, Any]):
        """Serialize Await node."""
        result["expr"] = self.serialize(ast_node.expr)

    def _serialize_typehint(self, ast_node, result: Dict[str, Any]):
        """Serialize TypeHint node."""
        result["type_name"] = ast_node.type_name

    def _serialize_formatstring(self, ast_node, result: Dict[str, Any]):
        """Serialize FormatString node."""
        result["parts"] = [self.serialize(part) for part in ast_node.parts]

    def _serialize_ternary(self, ast_node, result: Dict[str, Any]):
        """Serialize Ternary node."""
        result["condition"] = self.serialize(ast_node.condition)
        result["if_expr"] = self.serialize(ast_node.if_expr)
        result["else_expr"] = self.serialize(ast_node.else_expr)

    def _serialize_unpacking(self, ast_node, result: Dict[str, Any]):
        """Serialize Unpacking node."""
        result["expr"] = self.serialize(ast_node.expr)

    def _serialize_walrusoperator(self, ast_node, result: Dict[str, Any]):
        """Serialize WalrusOperator node."""
        result["var_name"] = ast_node.var_name
        result["value"] = self.serialize(ast_node.value)

    def _serialize_compoundassign(self, ast_node, result: Dict[str, Any]):
        """Serialize CompoundAssign node."""
        result["var"] = self.serialize(ast_node.var)
        result["op"] = {"type": ast_node.op.type, "value": ast_node.op.value}
        result["value"] = self.serialize(ast_node.value)

    def _serialize_switch(self, ast_node, result: Dict[str, Any]):
        """Serialize Switch node."""
        result["expr"] = self.serialize(ast_node.expr)
        result["cases"] = [self.serialize(case) for case in ast_node.cases]
        if ast_node.default_case:
            result["default_case"] = self.serialize(ast_node.default_case)

    def _serialize_case(self, ast_node, result: Dict[str, Any]):
        """Serialize Case node."""
        result["values"] = [self.serialize(value) for value in ast_node.values]
        result["body"] = self.serialize(ast_node.body)

    def _serialize_with(self, ast_node, result: Dict[str, Any]):
        """Serialize With node."""
        result["context_expr"] = self.serialize(ast_node.context_expr)
        result["var_name"] = ast_node.var_name
        result["body"] = self.serialize(ast_node.body)

    def _serialize_value(self, value) -> Any:
        """Serialize a value (could be primitive, list, dict, or AST node)."""
        if value is None:
            return None
        elif isinstance(value, (str, int, float, bool)):
            return value
        elif isinstance(value, list):
            return [self._serialize_value(item) for item in value]
        elif isinstance(value, dict):
            return {key: self._serialize_value(val) for key, val in value.items()}
        elif hasattr(value, "__class__") and hasattr(value.__class__, "__name__"):
            # Check if it's an AST node
            if hasattr(value, "token") or any(
                attr in ["statements", "left", "right", "value", "name", "body"]
                for attr in dir(value)
                if not attr.startswith("_")
            ):
                return self.serialize(value)
            else:
                return str(value)
        else:
            return str(value)

    def to_json(self, ast_node) -> str:
        """
        Convert AST node to JSON string.

        Args:
            ast_node: The AST node to convert

        Returns:
            JSON string representation
        """
        serialized = self.serialize(ast_node)
        return json.dumps(serialized, indent=2, ensure_ascii=False)


# Global serializer instance
_ast_serializer = None


def get_ast_serializer() -> ASTSerializer:
    """
    Get the global AST serializer instance.

    Returns:
        ASTSerializer instance
    """
    global _ast_serializer
    if _ast_serializer is None:
        _ast_serializer = ASTSerializer()
    return _ast_serializer


def ast_to_json(ast_node) -> str:
    """
    Convert AST node to JSON string.

    Args:
        ast_node: The AST node to convert

    Returns:
        JSON string representation
    """
    serializer = get_ast_serializer()
    return serializer.to_json(ast_node)


def ast_to_dict(ast_node) -> Dict[str, Any]:
    """
    Convert AST node to dictionary.

    Args:
        ast_node: The AST node to convert

    Returns:
        Dictionary representation
    """
    serializer = get_ast_serializer()
    return serializer.serialize(ast_node)


__all__ = ["ASTSerializer", "get_ast_serializer", "ast_to_json", "ast_to_dict"]
