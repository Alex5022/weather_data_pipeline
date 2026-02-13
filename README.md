# Weather Data Pipeline

A containerized Python pipeline for fetching, processing, and storing weather data from external APIs.

---

## Overview
This project automates the process of fetching weather data from **Open-Meteo.com** APIs, transforming it into structured records, and persisting it inside a PostgreSQL container. It is designed for reproducibility, scalability, and easy integration with analytics or visualization tools.

---

## Features
- Fetches weather data from configurable API endpoints.
- Parameterized data retrieval via `weather_fetch_params.json`.
- Containerized with Docker `docker compose`.


---

## Installation

### Prerequisites
- Docker & Docker Compose installed

### Steps
```bash
# Clone the repository 
git clone https://github.com/Alex5022/weather_data_pipeline.git
cd weather_data_pipeline

# Build the Docker image and run the pipeline
docker compose up
```

Alternatively, download the ZIP file, extract it, open the folder in your terminal or code editor, and run:
```bash
docker compose up
```

## Data Access
#### To open the database and inspect the data, run:
```bash
docker exec -it postgres-db psql -U postgres -d weather_db 
