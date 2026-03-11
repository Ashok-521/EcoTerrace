3 SYSTEM DESIGN

3.1 Architectural Design

REROOT uses a modular, service-oriented architecture to separate concerns and enable scaling. Main components:

- Frontend: single-page application for visualization, project management, and reporting.
- Backend API: REST/GraphQL service (Flask/FastAPI) handling user auth, orchestration, and data endpoints.
- Processing workers: asynchronous workers for heavy tasks (image preprocessing, model training, inference).
- Spatial database: PostgreSQL + PostGIS for geospatial data and metadata.
- Object storage or local disk: for large raster datasets and imagery tiles.
- Monitoring & logging: Prometheus/Grafana (or equivalent) and structured logs for observability.

3.2 Data Flow Design

1. Ingest: External imagery and tabular inputs are uploaded via the frontend or a dedicated ingestion API. Files are stored in object storage and metadata recorded in PostGIS.
2. Preprocess: Workers normalize projections, compute vegetation indices (NDVI/EVI), and generate standardized tiles. Derived raster layers are added to the dataset catalog.
3. Model pipeline: Preprocessed tiles are fed into ML models for suitability scoring and change detection. Model outputs are stored as vector or raster layers with associated confidence scores.
4. Decision support: Aggregation services produce ranked lists of candidate sites and planting plans; results are surfaced through API endpoints and dashboard visualizations.
5. Monitor: Periodic re-ingestion of imagery triggers change-detection workflows that update project dashboards and generate alerts.

3.3 Component Interaction Design

- The frontend queries the backend API for map tiles, project data, and analytics results.
- The backend enqueues heavy jobs to a message broker (RabbitMQ/Redis). Worker services poll the queue and process jobs, writing results back to the database and storage.
- Authentication and authorization are enforced at API layer; field agents can upload monitoring photos that are linked to projects.
- Backup and snapshot workflows export critical data and allow recovery of datasets.

3.4 System behavior and features

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