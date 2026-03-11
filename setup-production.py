#!/usr/bin/env python3
"""
Professional EcoTerrace Production Setup
"""

import secrets
import os
import subprocess
from pathlib import Path

def generate_secure_key():
    """Generate secure secret key"""
    return secrets.token_hex(32)

def setup_production_env():
    """Setup professional production environment"""
    
    print("🚀 EcoTerrace Professional Setup")
    print("=" * 50)
    
    # Generate secure secret key
    secret_key = generate_secure_key()
    print(f"🔐 Generated Secret Key: {secret_key}")
    
    # Get user inputs
    print("\n📋 Please enter your production details:")
    
    # API Key
    api_key = input("🌤️ OpenWeatherMap API Key (or press Enter for demo key): ").strip()
    if not api_key:
        api_key = "a2fd88ad38939cb61fa26d46dac19b10"
        print("   Using demo API key (limited usage)")
    
    # Database setup
    print("\n🗄️ Database Configuration:")
    db_choice = input("   Use PostgreSQL? (y/n, default: n): ").strip().lower()
    
    if db_choice == 'y':
        db_host = input("   Database host (localhost): ").strip() or "localhost"
        db_port = input("   Database port (5432): ").strip() or "5432"
        db_name = input("   Database name (ecoterrace): ").strip() or "ecoterrace"
        db_user = input("   Database user: ").strip()
        db_password = input("   Database password: ").strip()
        database_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    else:
        database_url = "sqlite:///ecoterrace.db"
        print("   Using SQLite (good for development)")
    
    # Production environment
    print("\n🌐 Production Environment:")
    domain = input("   Your domain (localhost): ").strip() or "localhost"
    ssl_enabled = input("   Enable SSL? (y/n, default: n): ").strip().lower() == 'y'
    
    # Create production .env file
    env_content = f"""# Professional Production Environment - EcoTerrace
# Generated on: {subprocess.check_output(['date'], shell=True).decode().strip()}

# Security Configuration
SECRET_KEY={secret_key}
FLASK_ENV=production

# API Configuration
OPENWEATHER_API_KEY={api_key}

# Database Configuration
DATABASE_URL={database_url}

# File Upload Configuration
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216

# Server Configuration
DOMAIN={domain}
SSL_ENABLED={'true' if ssl_enabled else 'false'}
PORT=5000

# Optional Cloud Services (uncomment if needed)
# CLOUD_STORAGE_BUCKET=your_cloud_storage_bucket
# REDIS_URL=redis://localhost:6379/0

# Performance Settings
DEBUG=false
TESTING=false

# Security Headers
SECURE_SSL_REDIRECT={'true' if ssl_enabled else 'false'}
SECURE_HSTS_SECONDS=31536000
SECURE_CONTENT_TYPE_NOSNIFF=true
SECURE_BROWSER_XSS_FILTER=true
"""
    
    # Write production environment file
    with open('.env.production', 'w') as f:
        f.write(env_content)
    
    print(f"\n✅ Production environment saved to .env.production")
    
    # Create uploads directory
    uploads_dir = Path('uploads')
    uploads_dir.mkdir(exist_ok=True)
    print(f"✅ Created uploads directory: {uploads_dir}")
    
    # Generate SSL certificate (if needed)
    if ssl_enabled and domain == 'localhost':
        print("\n🔒 Generating self-signed SSL certificate...")
        try:
            subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:4096', 
                        '-keyout', 'key.pem', '-out', 'cert.pem', '-days', '365',
                        '-nodes', '-subj', '/CN=localhost'], check=True)
            print("✅ SSL certificate generated (key.pem, cert.pem)")
        except subprocess.CalledProcessError:
            print("⚠️ OpenSSL not found. Install OpenSSL for SSL certificates.")
    
    print("\n🎉 Professional setup complete!")
    print("\n📋 Next Steps:")
    print("1. Review .env.production file")
    print("2. Start with: docker-compose up -d")
    print("3. Access at: https://localhost" if ssl_enabled else "http://localhost")
    print("\n📱 For network access: Use start-network.bat")

if __name__ == "__main__":
    setup_production_env()
