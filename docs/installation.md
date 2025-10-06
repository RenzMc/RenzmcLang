# 📦 Installation Guide - RenzMcLang

[![PyPI version](https://img.shields.io/pypi/v/renzmc.svg)](https://pypi.org/project/renzmc/)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

**Last Updated:** 2025-10-04

---

## 🎯 Overview

RenzMcLang adalah bahasa pemrograman berbasis Bahasa Indonesia yang modern dan powerful. Panduan ini akan membantu Anda menginstall RenzMcLang di sistem Anda.

---

## 📋 System Requirements

### Minimum Requirements
- **Python:** 3.8 atau lebih tinggi
- **Operating System:** Windows, macOS, atau Linux
- **RAM:** 512 MB (minimum)
- **Disk Space:** 100 MB

### Recommended Requirements
- **Python:** 3.11 atau lebih tinggi
- **RAM:** 2 GB atau lebih
- **Disk Space:** 500 MB

---

## 🚀 Installation Methods

### Method 1: Install from PyPI (Recommended)

Cara termudah untuk menginstall RenzMcLang adalah melalui PyPI:

```bash
pip install renzmc
```

**Verify Installation:**
```bash
rmc --version
# Output: RenzmcLang <version>
```

### Method 2: Install from Source

Untuk development atau kontribusi:

```bash
# Clone repository
git clone https://github.com/RenzMc/RenzmcLang.git
cd RenzmcLang

# Install in development mode
pip install -e .
```

**Verify Installation:**
```bash
rmc --version
# Output: RenzmcLang <version>
```

### Method 3: Using Installation Scripts

#### For Linux/macOS:
```bash
cd RenzmcLang
chmod +x install.sh
./install.sh
```

#### For Windows:
```cmd
cd RenzmcLang
install.bat
```

---

## 📦 Dependencies

RenzMcLang memerlukan beberapa Python packages:

### Core Dependencies
- `aiohttp>=3.8.1` - Async HTTP client
- `requests>=2.27.1` - HTTP library
- `cryptography>=36.0.0` - Cryptographic operations
- `python-dateutil>=2.8.2` - Date utilities
- `pytz>=2021.3` - Timezone support
- `pyyaml>=6.0` - YAML parser
- `ujson>=5.1.0` - Fast JSON parser
- `regex>=2022.1.18` - Advanced regex

### Optional Dependencies

#### For Development:
```bash
pip install renzmc[dev]
```

Includes:
- `pytest>=7.0.0` - Testing framework
- `pytest-asyncio>=0.18.0` - Async testing
- `black>=22.1.0` - Code formatter
- `isort>=5.10.1` - Import sorter
- `mypy>=0.931` - Type checker
- `flake8>=4.0.1` - Linter

#### For Documentation:
```bash
pip install renzmc[docs]
```

Includes:
- `sphinx>=4.0.0` - Documentation generator
- `sphinx-rtd-theme>=1.0.0` - ReadTheDocs theme

---

## ✅ Verification

### 1. Check Version
```bash
rmc --version
```

**Expected Output:**
```
RenzmcLang <version>
```

### 2. Run Hello World
Create a file `hello.rmc`:
```python
tampilkan "Hello, World!"
tampilkan "Selamat datang di RenzMcLang!"
```

Run it:
```bash
rmc hello.rmc
```

**Expected Output:**
```
Hello, World!
Selamat datang di RenzMcLang!
```

### 3. Test REPL (Interactive Shell)
```bash
rmc
```

**Expected Output:**
```
╔════════════════════════════════════════════════════════════════╗
║           RenzMcLang Interactive Shell (REPL)                 ║
║                    Version <version>                               ║
╚════════════════════════════════════════════════════════════════╝

Selamat datang di RenzMcLang REPL!
Ketik 'bantuan' untuk melihat perintah yang tersedia
Ketik 'keluar' atau tekan Ctrl+D untuk keluar

>>>
```

### 4. Test HTTP Client
Create a file `test_http.rmc`:
```python
response itu http_get("https://jsonplaceholder.typicode.com/posts/1")
tampilkan f"Status: {response.status_code}"
data itu response.json()
tampilkan f"Title: {data['title']}"
```

Run it:
```bash
rmc test_http.rmc
```

**Expected Output:**
```
Status: 200
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

---

## 🔧 Configuration

### Environment Variables

RenzMcLang supports the following environment variables:

```bash
# Set default timeout for HTTP requests (in seconds)
export RENZMC_HTTP_TIMEOUT=30

# Set log level (DEBUG, INFO, WARNING, ERROR)
export RENZMC_LOG_LEVEL=INFO

# Set REPL history file location
export RENZMC_HISTORY_FILE=~/.renzmc_history
```

### Configuration File

Create `~/.renzmcrc` for custom configuration:

```yaml
# RenzMcLang Configuration
http:
  timeout: 30
  user_agent: "RenzMcLang/latest"

repl:
  history_size: 1000
  multiline_mode: true

logging:
  level: INFO
  file: ~/.renzmc.log
```

---

## 🐛 Troubleshooting

### Issue 1: Command Not Found

**Problem:**
```bash
rmc: command not found
```

**Solution:**
```bash
# Make sure pip bin directory is in PATH
export PATH="$PATH:$HOME/.local/bin"

# Or use python -m
python -m renzmc --version
```

### Issue 2: Import Error

**Problem:**
```
ImportError: No module named 'renzmc'
```

**Solution:**
```bash
# Reinstall RenzMcLang
pip uninstall renzmc
pip install renzmc

# Or check Python path
python -c "import sys; print(sys.path)"
```

### Issue 3: Permission Denied

**Problem:**
```
Permission denied: '/usr/local/bin/rmc'
```

**Solution:**
```bash
# Install for user only
pip install --user renzmc

# Or use sudo (not recommended)
sudo pip install renzmc
```

### Issue 4: HTTP Client Not Working

**Problem:**
```
Error: http_get not found
```

**Solution:**
```bash
# Make sure you have the latest version
pip install --upgrade renzmc

# Check version
rmc --version  # Should be latest version or higher
```

---

## 🔄 Updating

### Update from PyPI
```bash
pip install --upgrade renzmc
```

### Update from Source
```bash
cd RenzmcLang
git pull origin main
pip install -e . --upgrade
```

### Check for Updates
```bash
pip list --outdated | grep renzmc
```

---

## 🗑️ Uninstallation

### Uninstall RenzMcLang
```bash
pip uninstall renzmc
```

### Remove Configuration Files
```bash
# Remove REPL history
rm ~/.renzmc_history

# Remove configuration
rm ~/.renzmcrc

# Remove logs
rm ~/.renzmc.log
```

---

## 📚 Next Steps

After installation, you can:

1. **Learn the Basics:** Read [Syntax Basics](syntax-basics.md)
2. **Try Examples:** Explore [Examples Guide](examples.md)
3. **Use REPL:** Start interactive shell with `rmc`
4. **Build Projects:** Check [Advanced Features](advanced-features.md)
5. **Integrate Python:** See [Python Integration](python-integration.md)

---

## 🆘 Getting Help

### Documentation
- [Quick Reference](quick-reference.md)
- [Built-in Functions](builtin-functions.md)
- [Examples](examples.md)

### Community
- **GitHub:** https://github.com/RenzMc/RenzmcLang
- **Issues:** https://github.com/RenzMc/RenzmcLang/issues
- **Email:** renzaja11@gmail.com

### Support
If you encounter any issues:
1. Check this troubleshooting guide
2. Search existing GitHub issues
3. Create a new issue with details
4. Contact via email

---

## 📝 Notes

- RenzMcLang requires Python 3.8+
- All dependencies are automatically installed
- REPL is available in latest version+
- HTTP client is built-in (no imports needed)
- Backward compatible with latest version

---

**Happy Coding with RenzMcLang! 🚀**