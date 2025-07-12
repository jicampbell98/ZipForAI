@echo off
rem ───────────────────────────────────────────────────────────────
rem  Build ZipForAI into a single EXE that always lands alongside
rem  this project’s files (no “dist” juggling required).
rem  Works even if the user moves the whole ZipForAI folder.
rem ───────────────────────────────────────────────────────────────

:: %~dp0  →  path of THIS .bat file (trailing \ already included)
set "PROJECT_DIR=%~dp0.."
cd /d "%PROJECT_DIR%"

echo Building ZipForAI in "%PROJECT_DIR%" …

pyinstaller ^
  --onefile ^
  --name zipforai ^
  --icon "media\zipforai.ico" ^
  --distpath "%PROJECT_DIR%" ^
  --workpath "%PROJECT_DIR%\build" ^
  --specpath "%PROJECT_DIR%\build" ^
  --clean ^
  zipforai_cli.py

if exist "%PROJECT_DIR%\zipforai.exe" (
    echo.
    echo ✅ Build complete → "%PROJECT_DIR%\zipforai.exe"
) else (
    echo.
    echo ❌ Build failed.  Check PyInstaller output above.
)

pause
