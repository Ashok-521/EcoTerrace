@echo off
echo ========================================
echo EcoTerrace Professional Deployment
echo ========================================
echo.

REM Check if Docker is running
echo Checking Docker status...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed or not running
    echo Please install Docker Desktop first
    pause
    exit /b 1
)

echo Docker is ready
echo.

REM Check if production environment exists
if not exist .env.production (
    echo ERROR: .env.production file not found
    echo Run setup-professional.bat first
    pause
    exit /b 1
)

echo Production configuration found
echo.

REM Stop any existing containers
echo Stopping existing containers...
docker-compose down 2>nul

REM Build and start services
echo Building and starting professional services...
docker-compose up -d --build

REM Wait for services to start
echo Waiting for services to initialize...
timeout /t 15 /nobreak >nul

REM Check service health
echo Checking service health...
docker-compose ps

REM Show access URLs
echo.
echo ========================================
echo DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo Access URLs:
echo - Frontend: http://localhost
echo - Backend API: http://localhost/api
echo - Database: localhost:5432
echo - Redis: localhost:6379
echo.
echo Management Commands:
echo - View logs: docker-compose logs -f
echo - Stop services: docker-compose down
echo - Restart: docker-compose restart
echo - Update: docker-compose pull && docker-compose up -d
echo.
echo For SSL/HTTPS:
echo 1. Generate certificates in ssl/ folder
echo 2. Update nginx.conf with your domain
echo 3. Restart: docker-compose restart nginx
echo.
echo ========================================

pause
