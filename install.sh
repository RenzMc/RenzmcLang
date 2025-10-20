#!/bin/bash

# RenzmcLang Installation Script
# This script installs RenzmcLang and its dependencies

echo "=== RenzmcLang Installation Script ==="
echo "Installing RenzmcLang and its dependencies..."

# Check if Python is installed
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "Error: Python is not installed. Please install Python 3.6 or later."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$($PYTHON -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 6 ]); then
    echo "Error: RenzmcLang requires Python 3.6 or later. You have Python $PYTHON_VERSION."
    exit 1
fi

echo "Using Python $PYTHON_VERSION"

# Install dependencies
echo "Installing dependencies..."
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt

# Install RenzmcLang
echo "Installing RenzmcLang..."
$PYTHON -m pip install -e .

# Create command scripts
echo "Creating command scripts..."
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
$PYTHON -m renzmc "\$@"
EOF

chmod +x "$BIN_DIR/renzmc"

# Create rmc command (shorthand)
cat > "$BIN_DIR/rmc" << EOF
#!/bin/bash
$PYTHON -m renzmc "\$@"
EOF

chmod +x "$BIN_DIR/rmc"

# Check if the bin directory is in PATH
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Adding $BIN_DIR to PATH..."
    echo "export PATH=&quot;\$PATH:$BIN_DIR&quot;" >> "$HOME/.bashrc"
    echo "export PATH=&quot;\$PATH:$BIN_DIR&quot;" >> "$HOME/.zshrc" 2>/dev/null || true
    echo "Please restart your terminal or run 'source ~/.bashrc' to update your PATH."
fi

echo "=== Installation Complete ==="
echo "You can now run RenzmcLang using either the 'renzmc' or 'rmc' command."
echo "Examples:"
echo "  renzmc examples/hello_world.rmc"
echo "  rmc examples/hello_world.rmc"
echo ""
echo "Thank you for installing RenzmcLang!"
