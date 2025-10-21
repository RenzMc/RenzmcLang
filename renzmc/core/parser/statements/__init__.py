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

from renzmc.core.parser.statements.assignments import (
    AssignmentStatements,
)
from renzmc.core.parser.statements.call_statements import CallStatements
from renzmc.core.parser.statements.control_flow import (
    ControlFlowStatements,
)
from renzmc.core.parser.statements.error_handling import (
    ErrorHandlingStatements,
)
from renzmc.core.parser.statements.flow_control import (
    FlowControlStatements,
)
from renzmc.core.parser.statements.router import StatementRouter
from renzmc.core.parser.statements.special_statements import (
    SpecialStatements,
)


class StatementParser(
    StatementRouter,
    ControlFlowStatements,
    AssignmentStatements,
    FlowControlStatements,
    ErrorHandlingStatements,
    SpecialStatements,
    CallStatements,
):
    """
    Main statement parser combining all statement parsing modules.

    This class inherits from all statement parsing modules to provide
    complete statement parsing functionality. The modular structure allows
    for easy maintenance and extension.

    Inheritance order:
    1. StatementRouter - Main routing logic
    2. ControlFlowStatements - Control flow statements
    3. AssignmentStatements - Assignment statements
    4. FlowControlStatements - Flow control statements
    5. ErrorHandlingStatements - Error handling statements
    6. SpecialStatements - Special statements
    7. CallStatements - Call statements
    """


__all__ = ["StatementParser"]
