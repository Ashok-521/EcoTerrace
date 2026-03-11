#!/bin/bash

# EcoTerrace Deployment Script

echo "Starting EcoTerrace deployment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create production environment file if it doesn't exist
if [ ! -f .env.production ]; then
    echo "Creating .env.production file..."
    cp .env.production.example .env.production
    echo "Please edit .env.production with your production values before continuing."
    exit 1
fi

# Build and start containers
echo "Building Docker containers..."
docker-compose build

echo "Starting services..."
docker-compose up -d

# Wait for database to be ready
echo "Waiting for database to be ready..."
sleep 10

# Initialize database
echo "Initializing database..."
docker-compose exec web python -c "from app import app, db; app.app_context().push(); db.create_all()"

echo "Deployment complete!"
echo "Your application is running at: http://localhost"
echo "Backend API is available at: http://localhost/api/"
echo ""
echo "To view logs: docker-compose logs -f"
echo "To stop: docker-compose down"
