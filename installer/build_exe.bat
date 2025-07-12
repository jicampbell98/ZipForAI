@echo off
REM Build ZipForAI into a single .exe in /dist

pyinstaller ^
  --onefile ^
  --name zipforai ^
  --clean ^
  ..\app\__main__.py

REM Move the exe to project root for convenience
move /Y dist\zipforai.exe ..\
echo.
echo ✅ Build complete: ..\zipforai.exe
pause
