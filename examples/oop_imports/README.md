# OOP Import System Examples

This directory contains comprehensive examples demonstrating RenzMcLang's Python-like import system for classes and functions across different folders.

## Directory Structure

```
oop_imports/
├── Ren/
│   └── renz.rmc          # Module with Person, Calculator, BankAccount classes
├── Utils/
│   └── helpers.rmc       # Module with Logger, Validator classes and utility functions
├── 01_basic_import.rmc   # Basic single and multiple class imports
├── 02_multiple_imports.rmc  # Importing from multiple modules
├── 03_import_with_alias.rmc # Using aliases with imports
└── 04_complex_example.rmc   # Real-world application example

```

## Import Syntax

### Basic Import
```python
dari Ren.renz impor buat_Person, Person_perkenalan
```

### Import with Alias
```python
dari Ren.renz impor buat_Person sebagai create_person
```

### Multiple Imports
```python
dari Ren.renz impor buat_Person, buat_Calculator, buat_BankAccount
```

### Import from Nested Modules
```python
dari Utils.helpers impor format_currency, buat_Logger
```

## Running Examples

```bash
# Run basic import example
renzmc examples/oop_imports/01_basic_import.rmc

# Run multiple imports example
renzmc examples/oop_imports/02_multiple_imports.rmc

# Run import with alias example
renzmc examples/oop_imports/03_import_with_alias.rmc

# Run complex application example
renzmc examples/oop_imports/04_complex_example.rmc
```

## Features Demonstrated

1. **Cross-folder imports**: Import classes from different directories
2. **Nested module paths**: Use dot notation (e.g., `Ren.renz`)
3. **Multiple imports**: Import multiple items in one statement
4. **Import aliases**: Rename imports to avoid conflicts
5. **Real-world patterns**: Complete application with multiple modules

## Module Structure

### Ren/renz.rmc
Contains:
- `Person` class (constructor, methods)
- `Calculator` class (arithmetic operations)
- `BankAccount` class (banking operations)
- Utility functions

### Utils/helpers.rmc
Contains:
- `Logger` class (logging functionality)
- `Validator` class (validation methods)
- Formatting utility functions

## Notes

- All class constructors follow the `buat_ClassName` naming convention
- All methods follow the `ClassName_methodName` naming convention
- This pattern allows for clean OOP-style programming in RenzMcLang
- The import system supports both `.rmc` and `.renzmc` file extensions