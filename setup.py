#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

# Read the long description from README.md
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = """
# RenzMcLang - Bahasa Pemrograman Berbasis Bahasa Indonesia

RenzMcLang adalah bahasa pemrograman modern yang menggunakan sintaks Bahasa Indonesia,
dirancang untuk memudahkan pembelajaran pemrograman bagi penutur Bahasa Indonesia.

## ✨ Fitur Utama

### 🎯 Sintaks Bahasa Indonesia
- Keyword dalam Bahasa Indonesia yang intuitif
- Error messages yang helpful dalam Bahasa Indonesia
- Dokumentasi lengkap dalam Bahasa Indonesia

### 🔥 Fitur Modern
- **Lambda Functions** - Fungsi anonim untuk functional programming
- **Comprehensions** - List dan Dict comprehension untuk kode yang ringkas
- **Ternary Operator** - Kondisi inline yang elegant
- **OOP** - Object-Oriented Programming dengan class dan inheritance
- **Async/Await** - Pemrograman asynchronous
- **Error Handling** - Try-catch-finally yang robust
- **Type Hints** - Optional type annotations

### 🔌 Integrasi Python
- Import dan gunakan library Python
- Akses Python builtins
- Interoperability penuh dengan ekosistem Python

### 📦 Built-in Functions Lengkap
- String manipulation (143+ functions)
- Math & statistics
- File operations
- JSON utilities
- HTTP functions
- System operations
- Database operations
- Dan banyak lagi!

## 📥 Instalasi

```bash
pip install renzmc
```

## 🚀 Quick Start

```python
# hello.rmc
tampilkan "Hello, World!"
tampilkan "Selamat datang di RenzMcLang!"
```

Jalankan:
```bash
rmc hello.rmc
```

## 📚 Dokumentasi

Untuk dokumentasi lengkap, kunjungi: https://github.com/RenzMc/RenzmcLang

## 📊 Statistik

- **Total Examples**: 95 contoh kode
- **Success Rate**: 89.5% (85/95 files berjalan sempurna)
- **Built-in Functions**: 143+ fungsi
- **Categories**: 30+ kategori contoh

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buka issue atau pull request di GitHub.

## 📝 License

Distributed under the MIT License.

---

**Made with ❤️ for Indonesian developers**

*"Coding in your native language, thinking in your native way"*
"""

# Read the version from version.py
version = {}
with open(os.path.join("renzmc", "version.py"), "r", encoding="utf-8") as fh:
    exec(fh.read(), version)

setup(
    name="renzmc",
    version=version["__version__"],
    author="RenzMc",
    author_email="renzaja11@gmail.com",
    description="Bahasa pemrograman berbasis Bahasa Indonesia yang powerful dan modern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenzMc/RenzmcLang",
    project_urls={
        "Bug Tracker": "https://github.com/RenzMc/RenzmcLang/issues",
        "Documentation": "https://github.com/RenzMc/RenzmcLang/tree/main/docs",
        "Source Code": "https://github.com/RenzMc/RenzmcLang",
        "Examples": "https://github.com/RenzMc/RenzmcLang/tree/main/examples",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Compilers",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Education :: Testing",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    keywords=[
        "indonesian", "bahasa-indonesia", "programming-language", "interpreter",
        "education", "learning", "coding", "pemrograman", "bahasa-pemrograman",
        "python", "compiler", "transpiler", "indonesian-language", "educational",
        "beginner-friendly", "native-language", "localized", "async", "oop",
        "functional-programming", "modern-language"
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.8.1",
        "requests>=2.27.1",
        "cryptography>=36.0.0",
        "python-dateutil>=2.8.2",
        "pytz>=2021.3",
        "pyyaml>=6.0",
        "ujson>=5.1.0",
        "regex>=2022.1.18",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.18.0",
            "black>=22.1.0",
            "isort>=5.10.1",
            "mypy>=0.931",
            "flake8>=4.0.1",
            "pylint",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "rmc=renzmc.__main__:main",
            "renzmc=renzmc.__main__:main",
        ],
    },
    include_package_data=True,
    package_data={
        "renzmc": [
            "examples/**/*.rmc",
            "docs/*.md",
            "*.png",
            "icon.png",
        ],
    },
    zip_safe=False,
    platforms=["any"],
)