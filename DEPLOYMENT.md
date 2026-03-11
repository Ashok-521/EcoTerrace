# EcoTerrace Deployment Guide

## Quick Start (Docker)

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### 1. Setup Environment Variables
```bash
# Copy production environment file
cp .env.production .env

# Edit with your values
nano .env
```

### 2. Deploy
```bash
# On Windows
deploy.bat

# On Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

### 3. Access
- Frontend: http://localhost
- Backend API: http://localhost/api/

## Manual Deployment

### Option 1: Local Server
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=production
export DATABASE_URL=postgresql://user:password@localhost:5432/ecoterrace

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

### Option 2: Cloud Platforms

#### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku config:set OPENWEATHER_API_KEY=your_key
heroku config:set SECRET_KEY=your_secret
git push heroku main
```

#### Vercel (Frontend only)
```bash
# Install Vercel CLI
vercel --prod
```

#### AWS/Google Cloud
- Use Docker containers
- Set up load balancer
- Configure database (RDS/Cloud SQL)
- Set up file storage (S3/Cloud Storage)

## Environment Variables

Required for production:
- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key
- `SECRET_KEY`: Flask secret key (generate with: python -c 'import secrets; print(secrets.token_hex(32))')
- `DATABASE_URL`: PostgreSQL connection string
- `FLASK_ENV`: Set to 'production'

## Database Setup

### PostgreSQL (Recommended for production)
```sql
CREATE DATABASE ecoterrace;
CREATE USER ecoterrace_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ecoterrace TO ecoterrace_user;
```

### SQLite (Development only)
- Works out of the box
- Not recommended for production

## File Uploads

Production file storage options:
- Local filesystem (current setup)
- AWS S3
- Google Cloud Storage
- Azure Blob Storage

## Security Notes

1. **Change default passwords** in production
2. **Use HTTPS** in production
3. **Set up firewall** rules
4. **Regular backups** of database
5. **Monitor logs** for suspicious activity

## Troubleshooting

### Database Connection Issues
```bash
# Check database status
docker-compose logs db

# Reset database
docker-compose down -v
docker-compose up -d db
```

### Port Conflicts
```bash
# Check what's using port 80/5000
netstat -tulpn | grep :80
netstat -tulpn | grep :5000
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
docker-compose logs -f db
```

## Performance Optimization

1. **Enable caching** (Redis)
2. **Use CDN** for static files
3. **Optimize database** queries
4. **Enable compression** (gzip)
5. **Monitor resources** usage

## Scaling

- **Horizontal scaling**: Add more web containers
- **Database scaling**: Read replicas, connection pooling
- **Load balancing**: Multiple nginx instances
- **Microservices**: Split into separate services
