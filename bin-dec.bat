@echo off
REM Batch file to run the Advanced Number Base Converter
setlocal

REM Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"

REM Check if Python 3 is available using python3 command
python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    python3 "%SCRIPT_DIR%bin_dec_converter.py"
) else (
    REM Fall back to python command
    python --version >nul 2>&1
    if %errorlevel% equ 0 (
        python "%SCRIPT_DIR%bin_dec_converter.py"
    ) else (
        echo Error: Python 3 is not installed or not in the PATH.
        echo Please install Python 3 and try again.
        pause
        exit /b 1
    )
)

endlocal
pause