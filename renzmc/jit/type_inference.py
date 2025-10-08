from __future__ import annotations
from typing import Any, Optional
from typing import Dict as PyDict
from typing import List as PyList
from typing import Set as PySet
from renzmc.core.ast import (
    AST, Assign, BinOp, Boolean, Break, Continue, Dict, For, ForEach, FuncCall, If, List, NoOp, Num, Return, Set, String, Tuple, UnaryOp, Var, VarDecl, While
)


class TypeInferenceEngine:

    def __init__(self):
        self.type_map: Dict[str, type] = {}
        self.numeric_types = {int, float}
        self.collection_types = {list, dict, set, tuple}

    def infer_type(self, node: AST, context: Dict[str, Any] = None) -> Optional[type]:
        if context is None:
            context = {}

        if isinstance(node, Num):
            return int if isinstance(node.value, int) else float
        elif isinstance(node, String):
            return str
        elif isinstance(node, Boolean):
            return bool
        elif isinstance(node, List):
            return list
        elif isinstance(node, Dict):
            return dict
        elif isinstance(node, Set):
            return set
        elif isinstance(node, Tuple):
            return tuple

        elif isinstance(node, Var):
            return context.get(node.name)

        elif isinstance(node, BinOp):
            left_type = self.infer_type(node.left, context)
            right_type = self.infer_type(node.right, context)

            if left_type and right_type:
                if left_type in self.numeric_types and right_type in self.numeric_types:
                    if left_type == float or right_type == float:
                        return float
                    return int

                if left_type == str or right_type == str:
                    return str

        elif isinstance(node, UnaryOp):
            expr_type = self.infer_type(node.expr, context)
            if expr_type in self.numeric_types:
                return expr_type
            elif expr_type == bool:
                return bool

        return None

    def is_numeric_function(self, params: List[str], body: List[AST],
                           context: Dict[str, Any] = None) -> bool:
        if context is None:
            context = {}

        for param in params:
            context[param] = int

        try:
            for stmt in body:
                if not self._is_numeric_statement(stmt, context):
                    return False
            return True
        except Exception:
            return False

    def _is_numeric_statement(self, stmt: AST, context: Dict[str, Any]) -> bool:

        if isinstance(stmt, (VarDecl, Assign)):
            value = stmt.value
            value_type = self.infer_type(value, context)

            if value_type is None:
                value_type = int

            if value_type not in self.numeric_types:
                return False

            var_name = stmt.var_name if isinstance(stmt, VarDecl) else stmt.var.name
            context[var_name] = value_type
            return True

        elif isinstance(stmt, Return):
            if hasattr(stmt, 'value') and stmt.value:
                return_type = self.infer_type(stmt.value, context)
                return return_type in self.numeric_types or return_type is None
            return True

        elif isinstance(stmt, (If, While)):
            # # cond_type = self.infer_type(stmt.condition, context)  # Unused variable  # Unused variable

            body = stmt.if_body if isinstance(stmt, If) else stmt.body
            for s in body:
                if not self._is_numeric_statement(s, context.copy()):
                    return False

            if isinstance(stmt, If) and stmt.else_body:
                for s in stmt.else_body:
                    if not self._is_numeric_statement(s, context.copy()):
                        return False

            return True

        elif isinstance(stmt, For):
            loop_context = context.copy()
            loop_context[stmt.var_name] = int

            for s in stmt.body:
                if not self._is_numeric_statement(s, loop_context):
                    return False
            return True

        elif isinstance(stmt, (BinOp, UnaryOp)):
            stmt_type = self.infer_type(stmt, context)
            return stmt_type in self.numeric_types

        elif isinstance(stmt, FuncCall):
            return True

        elif isinstance(stmt, (NoOp, Break, Continue)):
            return True

        return False

    def analyze_function_complexity(self, body: List[AST], func_name: str = None) -> Dict[str, Any]:
        analysis = {
            'has_loops': False,
            'loop_depth': 0,
            'has_recursion': False,
            'operation_count': 0,
            'has_function_calls': False
        }

        def analyze_node(node: AST, depth: int = 0):
            if isinstance(node, (For, While, ForEach)):
                analysis['has_loops'] = True
                analysis['loop_depth'] = max(analysis['loop_depth'], depth + 1)

                body = node.body
                for stmt in body:
                    analyze_node(stmt, depth + 1)

            elif isinstance(node, FuncCall):
                analysis['has_function_calls'] = True
                analysis['operation_count'] += 1
                
                # Check for recursion - check both direct name and func_expr
                if func_name:
                    # Check direct name attribute
                    if hasattr(node, 'name') and node.name and node.name == func_name:
                        analysis['has_recursion'] = True
                    # Check func_expr (which is a Var node for 'panggil' syntax)
                    elif hasattr(node, 'func_expr') and node.func_expr:
                        # If func_expr is a Var node with the function name
                        if hasattr(node.func_expr, 'name') and node.func_expr.name == func_name:
                            analysis['has_recursion'] = True
                
                # Recursively analyze function call arguments
                if hasattr(node, 'args'):
                    for arg in node.args:
                        analyze_node(arg, depth)

            elif isinstance(node, BinOp):
                analysis['operation_count'] += 1
                analyze_node(node.left, depth)
                analyze_node(node.right, depth)

            elif isinstance(node, UnaryOp):
                analysis['operation_count'] += 1
                analyze_node(node.expr, depth)

            elif isinstance(node, If):
                for stmt in node.if_body:
                    analyze_node(stmt, depth)
                if node.else_body:
                    for stmt in node.else_body:
                        analyze_node(stmt, depth)
            
            elif isinstance(node, Return):
                if hasattr(node, 'value') and node.value:
                    analyze_node(node.value, depth)

        for stmt in body:
            analyze_node(stmt)

        return analysis
