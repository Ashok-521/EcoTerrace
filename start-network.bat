@echo off
echo 🌱 Starting EcoTerrace for Network Access...
echo.

REM Get local IP address
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| find "IPv4"') do set IP=%%a

echo 📍 Your IP Address: %IP%
echo.

REM Update config with current IP
echo const ECO_TERRACE_CONFIG = { > frontend\config.js
echo     development: { >> frontend\config.js
echo         API_BASE: 'http://127.0.0.1:5000', >> frontend\config.js
echo         FRONTEND_URL: 'file:///e:/Ecoterrace/frontend/index.html' >> frontend\config.js
echo     }, >> frontend\config.js
echo     production: { >> frontend\config.js
echo         API_BASE: 'http://%IP%:5000', >> frontend\config.js
echo         FRONTEND_URL: 'http://%IP%:8000' >> frontend\config.js
echo     } >> frontend\config.js
echo. >> frontend\config.js
echo const getEnvironment = () => 'production'; >> frontend\config.js
echo window.EcoTerrace = { >> frontend\config.js
echo     config: ECO_TERRACE_CONFIG.production, >> frontend\config.js
echo     environment: 'production' >> frontend\config.js
echo }; >> frontend\config.js

echo 🔧 Starting Backend Server...
start "Backend Server" cmd /k "cd backend && venv\Scripts\python.exe -m flask run --host=0.0.0.0 --port=5000"

echo 🌐 Starting Frontend Server...
timeout /t 3 >nul
start "Frontend Server" cmd /k "cd frontend && python server.py"

echo.
echo ✅ EcoTerrace is starting...
echo 📡 Backend: http://%IP%:5000
echo 🌐 Frontend: http://%IP%:8000
echo 📱 Mobile Access: http://%IP%:8000
echo.
echo ⏹️  Press any key to open browser...
pause >nul
start http://%IP%:8000

echo 🎉 EcoTerrace is ready for network access!
echo 📱 Other devices can access: http://%IP%:8000
echo ⏹️  Press Ctrl+C in each window to stop servers
