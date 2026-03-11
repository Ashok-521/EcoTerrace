@echo off
echo ========================================
echo EcoTerrace Professional Setup
echo ========================================
echo.

REM Generate secure secret key
echo Generating secure secret key...
python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))" > temp_key.txt
set /p SECRET_KEY=<temp_key.txt
del temp_key.txt

echo Generated secure secret key

REM Get production API key
echo.
echo Please enter your production details:
echo.
set /p API_KEY=OpenWeatherMap API Key (or press Enter for demo): 
if "%API_KEY%"=="" set API_KEY=a2fd88ad38939cb61fa26d46dac19b10

REM Create professional environment file
echo Creating professional environment configuration...
echo # Professional Production Environment - EcoTerrace > .env.production
echo # Generated on: %date% %time% >> .env.production
echo. >> .env.production
echo # Security Configuration >> .env.production
echo SECRET_KEY=%SECRET_KEY% >> .env.production
echo FLASK_ENV=production >> .env.production
echo DEBUG=false >> .env.production
echo TESTING=false >> .env.production
echo. >> .env.production
echo # API Configuration >> .env.production
echo OPENWEATHER_API_KEY=%API_KEY% >> .env.production
echo. >> .env.production
echo # Database Configuration >> .env.production
echo DATABASE_URL=postgresql://ecoterrace_user:secure_ecoterrace_2026@db:5432/ecoterrace >> .env.production
echo. >> .env.production
echo # File Upload Configuration >> .env.production
echo UPLOAD_FOLDER=uploads >> .env.production
echo MAX_CONTENT_LENGTH=16777216 >> .env.production
echo. >> .env.production
echo # Performance Settings >> .env.production
echo DB_PASSWORD=secure_ecoterrace_2026 >> .env.production
echo REDIS_PASSWORD=redis_secure_2026 >> .env.production
echo. >> .env.production
echo # Security Headers >> .env.production
echo SECURE_SSL_REDIRECT=false >> .env.production
echo SECURE_HSTS_SECONDS=31536000 >> .env.production
echo SECURE_CONTENT_TYPE_NOSNIFF=true >> .env.production
echo SECURE_BROWSER_XSS_FILTER=true >> .env.production

echo.
echo ========================================
echo Professional Setup Complete!
echo ========================================
echo.
echo Created: .env.production
echo Secret Key: [SECURE]
echo API Key: %API_KEY%
echo.
echo Next Steps:
echo 1. Review .env.production file
echo 2. Run: docker-compose up -d
echo 3. Access at: http://localhost
echo.
echo For SSL/HTTPS: Generate certificates first
echo ========================================

pause
