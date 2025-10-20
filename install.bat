@echo off
chcp 65001 >nul
echo === RenzmcLang Windows Installer ===
echo Installing RenzmcLang and its dependencies...

:: Run a PowerShell block to do the heavy lifting
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
"& {
  try {
    Write-Host 'Checking for Python...'

    $candidates = @('py','python','python3')
    $pyExe = $null
    foreach ($c in $candidates) {
      $cmd = Get-Command $c -ErrorAction SilentlyContinue
      if ($cmd) { $pyExe = $cmd.Source; break }
    }

    if (-not $pyExe) {
      Write-Host 'Error: Python not found. Please install Python 3.6 or later.' -ForegroundColor Red
      exit 1
    }

    # Get major/minor from python
    $verText = & $pyExe -c 'import sys; print(sys.version_info.major); print(sys.version_info.minor)' 2>&1
    $lines = $verText -split \"\r?\n\" | Where-Object { $_ -match '\d+' }
    if ($lines.Count -lt 2) {
      Write-Host 'Error: Could not determine Python version.' -ForegroundColor Red
      exit 1
    }
    $major = [int]$lines[0]; $minor = [int]$lines[1]

    if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 6)) {
      Write-Host \"Error: Python $major.$minor found. RenzmcLang requires Python 3.6 or later.\" -ForegroundColor Red
      exit 1
    }

    Write-Host \"Using Python: $pyExe (version $major.$minor)\"

    Write-Host 'Upgrading pip...'
    & $pyExe -m pip install --upgrade pip

    Write-Host 'Installing dependencies from requirements.txt...'
    if (-not (Test-Path '.\\requirements.txt')) {
      Write-Host 'Warning: requirements.txt not found in current directory. Skipping pip install -r requirements.txt.' -ForegroundColor Yellow
    } else {
      & $pyExe -m pip install -r requirements.txt
    }

    Write-Host 'Installing RenzmcLang (editable)...'
    & $pyExe -m pip install -e .

    Write-Host 'Creating command wrappers in %USERPROFILE%\\bin ...'
    $bin = Join-Path $env:USERPROFILE 'bin'
    if (-not (Test-Path $bin)) { New-Item -ItemType Directory -Path $bin | Out-Null }

    $content = '@echo off' + [Environment]::NewLine + '\"' + $pyExe + '\" -m renzmc %*'
    Set-Content -Path (Join-Path $bin 'renzmc.bat') -Value $content -Encoding ASCII
    Set-Content -Path (Join-Path $bin 'rmc.bat') -Value $content -Encoding ASCII

    # Add to user PATH if not present
    $userPath = [Environment]::GetEnvironmentVariable('PATH','User')
    if (-not $userPath) { $userPath = '' }
    if ($userPath -notlike ('*' + $bin + '*')) {
      Write-Host 'Adding %USERPROFILE%\\bin to user PATH (via setx)...'
      # get current system-expanded PATH from environment to avoid losing it (setx has limits but is the common approach)
      $cur = [Environment]::GetEnvironmentVariable('PATH','User')
      if (-not $cur) { $cur = [Environment]::GetEnvironmentVariable('PATH','Machine') }
      if (-not $cur) { $cur = '' }
      $new = $cur + ';' + $bin
      [Environment]::SetEnvironmentVariable('PATH',$new,'User')
      Write-Host 'Added. Restart your terminal or log off/on to make it effective.' -ForegroundColor Green
    } else {
      Write-Host '%USERPROFILE%\\bin already in PATH.'
    }

    Write-Host '=== Installation Complete ===' -ForegroundColor Green
    Write-Host 'You can now run: renzmc <file>  OR  rmc <file>'
    exit 0
  } catch {
    Write-Host 'Installation failed:' $_.Exception.Message -ForegroundColor Red
    exit 1
  }
}"
if %ERRORLEVEL% NEQ 0 (
  echo.
  echo Installation encountered an error. See messages above.
  pause
) else (
  echo.
  echo Done. If wrappers not found in this session, open a new Command Prompt.
)
