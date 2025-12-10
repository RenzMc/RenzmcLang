#!/bin/bash

# Install RenzmcLang with Rust components
# This script installs RenzmcLang with Rust for optimal performance

echo "🚀 Installing RenzmcLang with Rust components..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8 or higher."
    exit 1
fi

# Check for Rust and install if needed
if ! command -v rustc &> /dev/null; then
    echo "🦀 Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal
    source "$HOME/.cargo/env"
    echo "✅ Rust installed successfully"
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Check if Rust is installed
if ! command -v rustc &> /dev/null; then
    echo "🔧 Installing Rust (required for optimal performance)..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source ~/.cargo/env
    echo "✅ Rust installed successfully"
else
    echo "✅ Rust detected"
fi

# Install maturin for Rust compilation
echo "📦 Installing maturin (Rust-Python bridge)..."
pip3 install maturin

# Update pyproject.toml for Rust build
echo "🔧 Configuring build system for Rust..."
sed -i 's/build-backend = "setuptools.build_meta"/build-backend = "maturin"/' pyproject.toml
sed -i 's/requires = \["setuptools>=64", "wheel"\]/requires = ["maturin>=1.0", "setuptools>=64", "wheel"]/' pyproject.toml

# Install and build with Rust
echo "🏗️ Building RenzmcLang with Rust components..."
if python3 build_with_rust.py --install; then
    echo "✅ RenzmcLang with Rust components installed successfully!"
    echo ""
    echo "🚀 Performance enhanced with Rust VM"
    echo "🎯 Quick start:"
    echo "  rmc examples/dasar/01_hello_world.rmc"
    echo "  rmc --help"
    echo ""
    echo "📚 Documentation: https://github.com/RenzMc/RenzmcLang"
    echo "🔧 Rust build info: python3 build_with_rust.py --help"
else
    echo "⚠️ Rust build failed, falling back to Python-only installation..."
    # Fallback to Python-only installation
    sed -i 's/build-backend = "maturin"/build-backend = "setuptools.build_meta"/' pyproject.toml
    sed -i 's/requires = \["maturin>=1.0", "setuptools>=64", "wheel"\]/requires = ["setuptools>=64", "wheel"]/' pyproject.toml
    pip3 install -e .
    echo "✅ RenzmcLang (Python-only) installed successfully!"
    echo "💡 Note: For better performance, install Rust and rebuild: python3 build_with_rust.py --install"
fi

# Create command scripts
echo "🔧 Creating command scripts..."
if [ -d "$HOME/.local/bin" ]; then
    BIN_DIR="$HOME/.local/bin"
elif [ -d "/usr/local/bin" ] && [ -w "/usr/local/bin" ]; then
    BIN_DIR="/usr/local/bin"
else
    BIN_DIR="$PWD/bin"
    mkdir -p "$BIN_DIR"
fi

# Create renzmc command
cat > "$BIN_DIR/renzmc" << EOF
#!/bin/bash
python3 -m renzmc "\$@"
EOF

chmod +x "$BIN_DIR/renzmc"

# Create rmc command (shorthand)
cat > "$BIN_DIR/rmc" << EOF
#!/bin/bash
python3 -m renzmc "\$@"
EOF

chmod +x "$BIN_DIR/rmc"

# Check if the bin directory is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "📝 Adding $BIN_DIR to PATH..."
    echo "export PATH=&quot;\$PATH:$BIN_DIR&quot;" >> "$HOME/.bashrc"
    echo "export PATH=&quot;\$PATH:$BIN_DIR&quot;" >> "$HOME/.zshrc" 2>/dev/null || true
    echo "Please restart your terminal or run 'source ~/.bashrc' to update your PATH."
fi

echo ""
echo "=== Installation Complete ==="
echo "You can now run RenzmcLang using either the 'renzmc' or 'rmc' command."
echo "Examples:"
echo "  renzmc examples/dasar/01_hello_world.rmc"
echo "  rmc examples/dasar/01_hello_world.rmc"
echo ""
echo "🚀 Rust VM integration ready for optimal performance!"
echo "📚 Documentation: https://github.com/RenzMc/RenzmcLang"
echo "Thank you for installing RenzmcLang!"