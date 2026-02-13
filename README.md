# Weather Data Pipeline

A containerized Python pipeline for fetching, processing, and storing weather data from external APIs.

---

## Overview
This project automates the collection of weather data, transforming it into structured formats suitable for analysis or integration with other systems. It leverages Docker for reproducibility and portability, ensuring consistent deployments across environments.

---

## Features
- Fetches weather data from configurable API endpoints.
- Parameterized data retrieval via `weather_fetch_params.json`.
- Containerized with Docker `docker compose`.


---

## 📦 Installation

### Prerequisites
- Docker & Docker Compose installed

### Steps
```bash
# Clone the repository
git clone https://github.com/Alex5022/weather_data_pipeline.git
cd weather_data_pipeline

# Build the Docker image and run the pipeline
docker-compose up
