@echo off
REM RenzmcLang Installation Script for Windows
REM This script installs RenzmcLang and its dependencies

echo === RenzmcLang Installation Script ===
echo Installing RenzmcLang and its dependencies...

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed. Please install Python 3.6 or later.
    exit /b 1
)

REM Check Python version
for /f "tokens=2 delims=." %%a in ('python -c "import sys; print(sys.version.split()[0])"') do (
    set PYTHON_VERSION=%%a
)

if %PYTHON_VERSION% LSS 6 (
    echo Error: RenzmcLang requires Python 3.6 or later.
    exit /b 1
)

echo Using Python 3.%PYTHON_VERSION%

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Install RenzmcLang
echo Installing RenzmcLang...
python -m pip install -e .

REM Create renzmc-plus.bat script
echo Creating renzmc-plus.bat script...
echo @echo off > renzmc-plus.bat
echo python -m renzmc %%* >> renzmc-plus.bat

REM Add to PATH
echo Adding RenzmcLang to PATH...
setx PATH "%PATH%;%CD%"

echo === Installation Complete ===
echo You can now run RenzmcLang using the 'renzmc-plus' command.
echo Example: renzmc-plus examples\fitur_baru.rmc
echo.
echo Thank you for installing RenzmcLang!