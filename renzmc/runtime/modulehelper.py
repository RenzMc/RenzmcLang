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

from pathlib import Path


def add_examples_path(interpreter_instance):
    """
    Add examples directory to module search paths.

    This function adds the examples directory to the module manager's search paths,
    allowing RenzmcLang programs to import modules from the examples directory.

    Args:
        interpreter_instance: The Interpreter instance to modify
    """
    # Get the package root directory
    package_root = Path(__file__).parent.parent.parent
    examples_path = package_root / "examples"

    # Add examples path if it exists
    if examples_path.exists() and examples_path.is_dir():
        interpreter_instance.module_manager.add_search_path(str(examples_path))

        # Also add common subdirectories that might be imported
        common_dirs = [
            "oop_imports",
            "test_imports",
            "utilities",
        ]

        for subdir in common_dirs:
            subdir_path = examples_path / subdir
            if subdir_path.exists() and subdir_path.is_dir():
                interpreter_instance.module_manager.add_search_path(str(subdir_path))
