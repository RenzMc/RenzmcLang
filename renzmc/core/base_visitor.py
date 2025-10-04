from renzmc.core.error import RenzmcError


class NodeVisitor:

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        try:
            return visitor(node)
        except RenzmcError as e:
            raise e
        except Exception as e:
            if hasattr(node, "line") and hasattr(node, "column"):
                line = node.line
                column = node.column
                raise RuntimeError(str(e), line, column)
            else:
                raise RuntimeError(str(e))

    def generic_visit(self, node):
        raise RuntimeError(f"Tidak ada metode visit_{type(node).__name__}")
