"""
FIXED VERSION - Boolean String Bug Fix

This file contains the fix for the boolean string issue.
The key change is in the primary() method where we convert
boolean token values to Python True/False.
"""

# In the primary() method, replace these lines:
#
# elif token.type == TokenType.BENAR:
#     self.eat(TokenType.BENAR)
#     primary = Boolean(token)
# elif token.type == TokenType.SALAH:
#     self.eat(TokenType.SALAH)
#     primary = Boolean(token)
#
# With:
#
# elif token.type == TokenType.BENAR:
#     self.eat(TokenType.BENAR)
#     # Create a new token with boolean value True instead of string "benar"
#     bool_token = Token(TokenType.BENAR, True, token.line, token.column)
#     primary = Boolean(bool_token)
# elif token.type == TokenType.SALAH:
#     self.eat(TokenType.SALAH)
#     # Create a new token with boolean value False instead of string "salah"
#     bool_token = Token(TokenType.SALAH, False, token.line, token.column)
#     primary = Boolean(bool_token)

# This ensures that Boolean AST nodes contain Python True/False values
# instead of string "benar"/"salah", fixing the issue with Python builtin functions