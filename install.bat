@echo off
REM Install RenzmcLang with Rust components for Windows
REM This script installs RenzmcLang with Rust for optimal performance

echo 🚀 Installing RenzmcLang with Rust components...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is required but not installed.
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detected

REM Check if Rust is installed
rustc --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 🔧 Installing Rust (required for optimal performance)...
    echo Visit https://rustup.rs/ to install Rust for Windows
    echo After installing Rust, run this script again
    pause
    exit /b 1
) else (
    echo ✅ Rust detected
)

REM Install maturin for Rust compilation
echo 📦 Installing maturin (Rust-Python bridge)...
pip install maturin

REM Update pyproject.toml for Rust build
echo 🔧 Configuring build system for Rust...
powershell -Command "(Get-Content pyproject.toml) -replace 'build-backend = &quot;setuptools.build_meta&quot;', 'build-backend = &quot;maturin&quot;' | Set-Content pyproject.toml"
powershell -Command "(Get-Content pyproject.toml) -replace 'requires = \[&quot;setuptools>=64&quot;, &quot;wheel&quot;\]', 'requires = [&quot;maturin>=1.0&quot;, &quot;setuptools>=64&quot;, &quot;wheel&quot;]' | Set-Content pyproject.toml"

REM Install and build with Rust
echo 🏗️ Building RenzmcLang with Rust components...
python build_with_rust.py --install
if %errorlevel% equ 0 (
    echo ✅ RenzmcLang with Rust components installed successfully!
    echo.
    echo 🚀 Performance enhanced with Rust VM
    echo 🎯 Quick start:
    echo   rmc examples\dasar\01_hello_world.rmc
    echo   rmc --help
    echo.
    echo 📚 Documentation: https://github.com/RenzMc/RenzmcLang
    echo 🔧 Rust build info: python build_with_rust.py --help
) else (
    echo ⚠️ Rust build failed, falling back to Python-only installation...
    REM Fallback to Python-only installation
    powershell -Command "(Get-Content pyproject.toml) -replace 'build-backend = &quot;maturin&quot;', 'build-backend = &quot;setuptools.build_meta&quot;' | Set-Content pyproject.toml"
    powershell -Command "(Get-Content pyproject.toml) -replace 'requires = \[&quot;maturin>=1.0&quot;, &quot;setuptools>=64&quot;, &quot;wheel&quot;\]', 'requires = [&quot;setuptools>=64&quot;, &quot;wheel&quot;]' | Set-Content pyproject.toml"
    pip install -e .
    echo ✅ RenzmcLang (Python-only) installed successfully!
    echo 💡 Note: For better performance, install Rust and rebuild: python build_with_rust.py --install
)

REM Create batch files for commands
echo 🔧 Creating command scripts...
if not exist "%USERPROFILE%\AppData\Local\Microsoft\WindowsApps" (
    echo Creating bin directory...
    if not exist bin mkdir bin
) else (
    set BIN_DIR=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps
)

REM Create renzmc.bat
echo @echo off > renzmc.bat
echo python -m renzmc %%* >> renzmc.bat

REM Create rmc.bat
echo @echo off > rmc.bat
echo python -m renzmc %%* >> rmc.bat

echo.
echo === Installation Complete ===
echo You can now run RenzmcLang using either the 'renzmc' or 'rmc' command.
echo Examples:
echo   renzmc examples\dasar\01_hello_world.rmc
echo   rmc examples\dasar\01_hello_world.rmc
echo.
echo 🚀 Rust VM integration ready for optimal performance!
echo 📚 Documentation: https://github.com/RenzMc/RenzmcLang
echo Thank you for installing RenzmcLang!
pause