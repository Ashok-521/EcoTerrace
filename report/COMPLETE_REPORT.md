REROOT Project Report

TABLE OF CONTENTS

- ABSTRACT ........................................................ iv
- PROBLEM STATEMENT ............................................... v
- TABLE OF CONTENTS ............................................... vi
- 1 INTRODUCTION .................................................. 1
- 2 SYSTEM REQUIREMENTS ........................................... 7
- 3 SYSTEM DESIGN ................................................. 9

---

# ABSTRACT

This document collects the table of contents and chapter drafts for the REROOT project. Replace this placeholder with the final abstract summarizing objectives, methods, results, and conclusions.

---

# PROBLEM STATEMENT

Deforestation and landscape degradation present urgent environmental challenges. Organizations need tools to prioritize restoration, estimate resources, and monitor outcomes. REROOT aims to fill this gap by combining geospatial analysis and machine learning into a decision-support platform that reduces uncertainty and improves the efficiency of planting programs.

---

# 1 INTRODUCTION

## 1.1 Understanding Reforestation and AI

Reforestation is the deliberate replanting and restoration of trees in areas that have been deforested or degraded. Modern reforestation efforts benefit from combining ecological science with data-driven techniques. Artificial intelligence (AI) helps by automating analysis of large datasets—satellite and drone imagery, climate records, and soil maps—to identify priority planting sites, predict species survival, and optimize planting schedules. This section introduces the ecological context and motivates an AI-enabled approach.

## 1.2 How REROOT Works?

REROOT is an integrated software solution that combines data ingestion, geospatial analysis, machine learning, and a user-facing dashboard to support reforestation planning and monitoring. Core workflow steps:

- Data ingestion: satellite imagery, drone photos, soil & climate data, and existing land-use layers.
- Preprocessing: image tiling, vegetation indices (e.g., NDVI), and feature extraction.
- Modeling: species suitability, growth and survival probability models, and change-detection models for monitoring.
- Decision support: ranked site recommendations, planting plans, and resource estimates.
- Monitoring & feedback: periodic re-analysis to evaluate survival and adapt plans.

## 1.3 Features and Functionality

Key features in REROOT include:

- Geospatial import and visualization of imagery and maps.
- Automated site suitability scoring with configurable constraints (e.g., slope, proximity to water).
- Species recommendation engine based on local climate, soil, and biodiversity goals.
- Project planning tools: estimated sapling counts, schedules, and cost summaries.
- Monitoring dashboard with temporal comparisons, alerts for degradation, and exportable reports.
- User management and role-based access for field teams, scientists, and stakeholders.

## 1.4 Environmental Impact and Use Cases

REROOT targets measurable environmental outcomes including increased canopy cover, improved carbon sequestration, and habitat restoration. Typical use cases:

- Government reforestation programs optimizing limited budgets across landscapes.
- NGOs planning community-led planting with guidance on species mix and planting density.
- Private restoration projects tracking carbon credits and survival rates over time.

## 1.5 How REROOT Matters?

By automating data-heavy tasks and making science-based recommendations accessible to non-experts, REROOT reduces planning time and improves planting success rates. The system enables iterative improvement through monitoring, helping organizations allocate resources where restoration impact is highest.

---

# 2 SYSTEM REQUIREMENTS

## 2.1 Hardware Requirements

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

## 2.2 Software Requirements

- Operating System: Linux (Ubuntu 20.04+ recommended) or Windows Server 2019+ for production.
- Python: 3.8+ (3.10 recommended).
- Core libraries: geopandas, rasterio, numpy, pandas, scikit-learn, tensorflow or PyTorch (for ML), Flask/FastAPI for backend, and a modern frontend stack (React/Vue) where applicable.
- Database: PostgreSQL with PostGIS for spatial storage.
- Optional: Docker and Docker Compose for containerized deployment; `nginx` for reverse proxy.

## 2.3 Functional Specifications

- User authentication and role-based access.
- Data ingestion pipeline for imagery and tabular inputs.
- Geospatial indexing and storage in PostGIS.
- Species suitability and survival probability modeling.
- Project planning module with resource and cost estimation.
- Monitoring and reporting dashboard with exportable reports (PDF/CSV).

## 2.4 Performance Specifications

- Ingestion throughput: ability to process daily imagery updates (depending on dataset size) — target: process a 100 km² area within 24 hours on recommended hardware.
- Model inference latency: near-real-time for single-tile predictions (under 5 seconds per tile on GPU), batch-mode for large area scoring.
- Scalability: horizontal scaling for ingestion and inference components using worker queues (Celery/RQ or Kubernetes jobs).

## 2.5 Installation Steps

High-level steps to deploy REROOT:

1. Provision server(s) or cloud resources.
2. Install system packages and create Python virtual environment.
3. Install Postgres + PostGIS and create application database.
4. Configure environment variables and secrets (database, cloud credentials).
5. Build and run backend and worker services (Docker Compose or systemd services).
6. Deploy frontend and configure reverse proxy.
7. Ingest initial datasets and run baseline model training or use pre-trained models.

See repository deployment scripts (`deploy.bat`, `deploy.sh`, `Dockerfile`, `docker-compose.yml`) for environment-specific instructions.

---

# 3 SYSTEM DESIGN

## 3.1 Architectural Design

REROOT uses a modular, service-oriented architecture to separate concerns and enable scaling. Main components:

- Frontend: single-page application for visualization, project management, and reporting.
- Backend API: REST/GraphQL service (Flask/FastAPI) handling user auth, orchestration, and data endpoints.
- Processing workers: asynchronous workers for heavy tasks (image preprocessing, model training, inference).
- Spatial database: PostgreSQL + PostGIS for geospatial data and metadata.
- Object storage or local disk: for large raster datasets and imagery tiles.
- Monitoring & logging: Prometheus/Grafana (or equivalent) and structured logs for observability.

## 3.2 Data Flow Design

1. Ingest: External imagery and tabular inputs are uploaded via the frontend or a dedicated ingestion API. Files are stored in object storage and metadata recorded in PostGIS.
2. Preprocess: Workers normalize projections, compute vegetation indices (NDVI/EVI), and generate standardized tiles. Derived raster layers are added to the dataset catalog.
3. Model pipeline: Preprocessed tiles are fed into ML models for suitability scoring and change detection. Model outputs are stored as vector or raster layers with associated confidence scores.
4. Decision support: Aggregation services produce ranked lists of candidate sites and planting plans; results are surfaced through API endpoints and dashboard visualizations.
5. Monitor: Periodic re-ingestion of imagery triggers change-detection workflows that update project dashboards and generate alerts.

## 3.3 Component Interaction Design

- The frontend queries the backend API for map tiles, project data, and analytics results.
- The backend enqueues heavy jobs to a message broker (RabbitMQ/Redis). Worker services poll the queue and process jobs, writing results back to the database and storage.
- Authentication and authorization are enforced at API layer; field agents can upload monitoring photos that are linked to projects.
- Backup and snapshot workflows export critical data and allow recovery of datasets.

## 3.4 System behavior and features

Resilience & error handling:

- Jobs are retried with exponential backoff; failures are logged and surfaced to operators.
- Graceful degradation: if model inference resources are unavailable, the system falls back to rule-based heuristics for recommendations.

Scalability:

- Use horizontally scalable workers for preprocessing and inference.
- Partition geospatial datasets and use tiling strategies to parallelize processing.

Security and privacy:

- Encrypt data at rest and in transit; enforce least-privilege access for credentials and APIs.
- Audit logging for sensitive project actions.

Extensibility:

- Pluggable model interfaces to allow swapping or improving ML components.
- Export adapters for integrating with external reporting tools and carbon-credit platforms.

---

# Appendix

- See the `report/` folder for source Markdown files.
