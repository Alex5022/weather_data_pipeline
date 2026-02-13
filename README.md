# Weather Data Pipeline

A containerized Python pipeline for fetching, processing, and storing weather data from external APIs.

---

## 📖 Overview
This project automates the collection of weather data, transforming it into structured formats suitable for analysis or integration with other systems. It leverages Docker for reproducibility and portability, ensuring consistent deployments across environments.

---

## 🚀 Features
- Fetches weather data from configurable API endpoints.
- Parameterized data retrieval via `weather_fetch_params.json`.
- Modular Python codebase inside `src/`.
- Containerized with Docker and orchestrated via `docker-compose`.
- Easy dependency management with `requirements.txt`.

---

## 🛠️ Tech Stack
- **Language:** Python (97.5%)
- **Containerization:** Docker, Docker Compose
- **Dependencies:** Listed in `requirements.txt`

---

## 📦 Installation

### Prerequisites
- Docker & Docker Compose installed
- Python 3.9+ (optional, if running locally without Docker)

### Steps
```bash
# Clone the repository
git clone https://github.com/Alex5022/weather_data_pipeline.git
cd weather_data_pipeline

# Build the Docker image
docker-compose build

# Run the pipeline
docker-compose up
