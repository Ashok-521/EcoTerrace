@echo off
REM EcoTerrace Deployment Script for Windows

echo Starting EcoTerrace deployment...

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker is not installed. Please install Docker Desktop first.
    pause
    exit /b 1
)

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Docker Compose is not installed. Please install Docker Compose first.
    pause
    exit /b 1
)

REM Create production environment file if it doesn't exist
if not exist .env.production (
    echo Creating .env.production file...
    copy .env.production .env.production
    echo Please edit .env.production with your production values before continuing.
    pause
    exit /b 1
)

REM Build and start containers
echo Building Docker containers...
docker-compose build

echo Starting services...
docker-compose up -d

REM Wait for database to be ready
echo Waiting for database to be ready...
timeout /t 10 /nobreak

REM Initialize database
echo Initializing database...
docker-compose exec web python -c "from app import app, db; app.app_context().push(); db.create_all()"

echo Deployment complete!
echo Your application is running at: http://localhost
echo Backend API is available at: http://localhost/api/
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down
pause
