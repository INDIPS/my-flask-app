@echo off
setlocal enabledelayedexpansion
cd /d %~dp0

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv venv || goto :venv_error
)

call "venv\Scripts\activate.bat"
if errorlevel 1 goto :venv_error

echo Installing required Python packages...
pip install -r src\requirements.txt
if errorlevel 1 goto :install_error

echo Starting Django development server...
start "" "http://127.0.0.1:8000/"
python src\manage.py runserver

goto :eof

:venv_error
echo.
echo Failed to create or activate the virtual environment.
echo Make sure Python is installed and available on your PATH.
pause
exit /b 1

:install_error
echo.
echo Failed to install dependencies.
echo Check your Python environment and package requirements.
pause
exit /b 1
