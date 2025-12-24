@echo off
REM Ejecuta el servidor con soporte de uploads (server_upload.py) y abre el navegador
cd /d "%~dp0"
start "" "http://localhost:8000"
python server_upload.py
pause
