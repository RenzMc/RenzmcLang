#!/usr/bin/env python3

"""
Setup script for RenzmcLang with Rust integration.
This setup script automatically handles Rust compilation if available.
"""

import os
import subprocess
import sys
from pathlib import Path

def check_rust():
    """Check if Rust is available."""
    try:
        result = subprocess.run(['rustc', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_maturin():
    """Check if maturin is available."""
    try:
        result = subprocess.run(['maturin', '--version'], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_maturin():
    """Install maturin if not available."""
    if not check_maturin():
        print("📦 Installing maturin for Rust compilation...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'maturin'], 
                      check=True)

def configure_for_rust():
    """Configure pyproject.toml for Rust build."""
    pyproject_path = Path('pyproject.toml')
    if not pyproject_path.exists():
        return False
    
    content = pyproject_path.read_text()
    
    # Update for Rust build
    content = content.replace(
        'build-backend = "setuptools.build_meta"',
        'build-backend = "maturin"'
    )
    content = content.replace(
        'requires = ["setuptools>=64", "wheel"]',
        'requires = ["maturin>=1.0", "setuptools>=64", "wheel"]'
    )
    
    pyproject_path.write_text(content)
    return True

def configure_for_python():
    """Configure pyproject.toml for Python-only build."""
    pyproject_path = Path('pyproject.toml')
    if not pyproject_path.exists():
        return False
    
    content = pyproject_path.read_text()
    
    # Update for Python build
    content = content.replace(
        'build-backend = "maturin"',
        'build-backend = "setuptools.build_meta"'
    )
    content = content.replace(
        'requires = ["maturin>=1.0", "setuptools>=64", "wheel"]',
        'requires = ["setuptools>=64", "wheel"]'
    )
    
    pyproject_path.write_text(content)
    return True

def main():
    """Main setup function."""
    print("🚀 Setting up RenzmcLang...")
    
    # Check if Rust is available
    if check_rust():
        print("✅ Rust detected - configuring for optimal performance")
        install_maturin()
        configure_for_rust()
        
        # Try to build with Rust
        try:
            print("🏗️ Building with Rust components...")
            subprocess.run([sys.executable, 'build_with_rust.py', '--install'], 
                          check=True)
            print("✅ RenzmcLang with Rust installed successfully!")
            return
        except subprocess.CalledProcessError:
            print("⚠️ Rust build failed, falling back to Python...")
            configure_for_python()
    else:
        print("⚠️ Rust not detected, using Python-only installation")
        print("💡 Install Rust for better performance: https://rustup.rs/")
        configure_for_python()
    
    # Python-only installation
    print("📦 Installing Python-only version...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-e '.], check=True)
    print("✅ RenzmcLang installed successfully!")
    print("💡 For Rust performance, install and run: python build_with_rust.py --install")

if __name__ == '__main__':
    main()