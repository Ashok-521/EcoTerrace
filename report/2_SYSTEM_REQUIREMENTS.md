2 SYSTEM REQUIREMENTS

2.1 Hardware Requirements

Minimum (for small teams / development):

- CPU: 4 cores
- RAM: 16 GB
- Disk: 200 GB SSD (for datasets and imagery cache)
- GPU: optional (NVIDIA GTX 1660 or better) for model training and image processing

Recommended (production / large datasets):

- CPU: 8+ cores
- RAM: 64 GB+
- Disk: 1 TB NVMe
- GPU: NVIDIA RTX-class (e.g., RTX 3080) or cloud GPU instances for model training

2.2 Software Requirements

- Operating System: Linux (Ubuntu 20.04+ recommended) or Windows Server 2019+ for production.
- Python: 3.8+ (3.10 recommended).
- Core libraries: geopandas, rasterio, numpy, pandas, scikit-learn, tensorflow or PyTorch (for ML), Flask/FastAPI for backend, and a modern frontend stack (React/Vue) where applicable.
- Database: PostgreSQL with PostGIS for spatial storage.
- Optional: Docker and Docker Compose for containerized deployment; `nginx` for reverse proxy.

2.3 Functional Specifications

- User authentication and role-based access.
- Data ingestion pipeline for imagery and tabular inputs.
- Geospatial indexing and storage in PostGIS.
- Species suitability and survival probability modeling.
- Project planning module with resource and cost estimation.
- Monitoring and reporting dashboard with exportable reports (PDF/CSV).

2.4 Performance Specifications

- Ingestion throughput: ability to process daily imagery updates (depending on dataset size) — target: process a 100 km² area within 24 hours on recommended hardware.
- Model inference latency: near-real-time for single-tile predictions (under 5 seconds per tile on GPU), batch-mode for large area scoring.
- Scalability: horizontal scaling for ingestion and inference components using worker queues (Celery/RQ or Kubernetes jobs).

2.5 Installation Steps

High-level steps to deploy REROOT:

1. Provision server(s) or cloud resources.
2. Install system packages and create Python virtual environment.
3. Install Postgres + PostGIS and create application database.
4. Configure environment variables and secrets (database, cloud credentials).
5. Build and run backend and worker services (Docker Compose or systemd services).
6. Deploy frontend and configure reverse proxy.
7. Ingest initial datasets and run baseline model training or use pre-trained models.

See repository deployment scripts (`deploy.bat`, `deploy.sh`, `Dockerfile`, `docker-compose.yml`) for environment-specific instructions.