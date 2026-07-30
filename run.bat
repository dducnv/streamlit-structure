@echo off
title Running Streamlit App...
echo =======================================================
echo Streamlit Auto Launcher for Windows
echo =======================================================

:: 1. Kiem tra Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python not found on your system!
    echo Please download and install Python from: https://www.python.org/downloads/
    echo IMPORTANT: Make sure to check "Add python.exe to PATH" during installation.
    pause
    exit /b 1
)

:: 2. Tu dong tao .venv neu chua co
if not exist ".venv" (
    echo [INFO] Creating virtual environment .venv...
    python -m venv .venv
)

:: 3. Kich hoat .venv
call .venv\Scripts\activate.bat

:: 4. Cai dat thu vien
if exist "requirements.txt" (
    echo [INFO] Installing required packages...
    pip install -q -r requirements.txt
)

:: 5. Chai Streamlit
echo [SUCCESS] Starting Streamlit App...
streamlit run app.py
pause
