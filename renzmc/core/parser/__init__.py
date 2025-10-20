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



from renzmc.core.parser.base import ParserBase
from renzmc.core.parser.declarations import DeclarationParser
from renzmc.core.parser.expressions import ExpressionParser
from renzmc.core.parser.imports import ImportParser
from renzmc.core.parser.literals import LiteralParser
from renzmc.core.parser.oop import OOPParser
from renzmc.core.parser.statements import StatementParser
from renzmc.core.parser.utilities import UtilityParser


class Parser(
    ParserBase,
    ExpressionParser,
    StatementParser,
    DeclarationParser,
    LiteralParser,
    OOPParser,
    UtilityParser,
    ImportParser,
):
    """
    Main Parser class combining all parser modules.

    This class inherits from all parser modules to provide a complete
    parsing implementation. The modular structure allows for easy
    maintenance and extension of parser functionality.

    Inheritance order:
    1. ParserBase - Core functionality (must be first)
    2. ExpressionParser - Expression parsing
    3. StatementParser - Statement parsing
    4. DeclarationParser - Declaration parsing
    5. LiteralParser - Literal parsing
    6. OOPParser - OOP features
    7. UtilityParser - Utility methods
    8. ImportParser - Import statements
    """


__all__ = ["Parser"]
