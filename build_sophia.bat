@echo off
echo [*] INITIATING SOVEREIGN COMPILATION PROTOCOL...

:: Ensure PyInstaller is installed (for 3.14t)
py -3.14t -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PyInstaller not found. Installing...
    py -3.14t -m pip install pyinstaller
)

:: Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del "*.spec"

:: Compile
echo [*] Compiling genesis_boot.py -> sophia_unlesangled.exe (NO-GIL)...
py -3.14t -m PyInstaller --noconfirm --onefile --console --name "sophia_unlesangled" --icon "NONE" --collect-all "rich" --collect-all "engine" --clean "genesis_boot.py"


echo.
if exist "dist\sophia_unlesangled.exe" (
    echo [SUCCESS] Unlesangled Build Complete.
    echo Target: dist\sophia_unlesangled.exe
    
    echo [*] Deploying to Root...
    copy /Y "dist\sophia_unlesangled.exe" "sophia_unlesangled.exe"
    if exist "sophia.exe" (
        echo [CLEANUP] Removing legacy sophia.exe...
        del "sophia.exe"
    )
    echo [SUCCESS] Deployed to .\sophia_unlesangled.exe
) else (
    echo [FAILURE] Build Failed. Check logs.
)
pause
