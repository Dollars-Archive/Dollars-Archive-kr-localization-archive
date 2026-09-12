@echo off
setlocal
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0install-global.ps1" %*
set ERR=%ERRORLEVEL%
if not "%ERR%"=="0" (
  echo.
  echo Installation failed with exit code %ERR%.
  pause
  exit /b %ERR%
)
echo.
echo Installation completed. Start a new Codex session and say: 한글화 작업할 거야
pause
