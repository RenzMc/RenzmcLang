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

from renzmc.core.error import RenzmcError


class NodeVisitor:

    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        try:
            return visitor(node)
        except RenzmcError as e:
            raise e
        except RuntimeError as e:
            if len(e.args) >= 3 and isinstance(e.args[1], int) and isinstance(e.args[2], int):
                raise
            error_msg = e.args[0] if e.args else str(e)
            while isinstance(error_msg, tuple) and len(error_msg) >= 1:
                error_msg = error_msg[0]
            if hasattr(node, "line") and hasattr(node, "column"):
                line = node.line
                column = node.column
                raise RuntimeError(error_msg, line, column)
            else:
                raise RuntimeError(error_msg)
        except Exception as e:
            error_msg = str(e)
            if hasattr(node, "line") and hasattr(node, "column"):
                line = node.line
                column = node.column
                raise RuntimeError(error_msg, line, column)
            else:
                raise RuntimeError(error_msg)

    def generic_visit(self, node):
        raise RuntimeError(f"Tidak ada metode visit_{type(node).__name__}")
