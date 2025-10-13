"""
Fix for the module system to add the examples/oop_imports directory to the search path.
"""

import os
import sys
from renzmc.runtime.renzmc_module_system import RenzmcModuleManager

# Original find_module method
original_find_module = RenzmcModuleManager.find_module

def patched_find_module(self, module_name):
    """
    Patched find_module method that checks for modules in the examples/oop_imports directory.
    """
    # First try the original method
    result = original_find_module(self, module_name)
    if result:
        return result
    
    # If not found, check if it's one of the special modules from examples
    if module_name in ['Ren', 'Ren.renz', 'Utils', 'Utils.helpers']:
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Go up to the renzmc directory
        renzmc_dir = os.path.dirname(current_dir)
        
        # Go up to the RenzmcLang directory
        renzmclang_dir = os.path.dirname(renzmc_dir)
        
        # Add the examples/oop_imports directory to the search path
        examples_dir = os.path.join(renzmclang_dir, "examples", "oop_imports")
        
        # Convert dot-separated module name to path
        # e.g., "Ren.renz" becomes "Ren/renz"
        module_path = module_name.replace(".", os.sep)
        
        # Try with different extensions
        for ext in [".rmc", ".renzmc"]:
            module_file = os.path.join(examples_dir, f"{module_path}{ext}")
            if os.path.isfile(module_file):
                return module_file
    
    return None

def add_examples_path(interpreter_instance):
    """
    Add the examples/oop_imports directory to the search path and patch the find_module method.
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up to the renzmc directory
    renzmc_dir = os.path.dirname(current_dir)
    
    # Go up to the RenzmcLang directory
    renzmclang_dir = os.path.dirname(renzmc_dir)
    
    # Add the examples/oop_imports directory to the search path
    examples_dir = os.path.join(renzmclang_dir, "examples", "oop_imports")
    
    # Add the path to the module manager
    if hasattr(interpreter_instance, "module_manager"):
        interpreter_instance.module_manager.add_search_path(examples_dir)
        
        # Patch the find_module method
        RenzmcModuleManager.find_module = patched_find_module
    
    return examples_dir