# Global-Energy-Price-Platform
 Real-Time Energy Market Data Platform
- ingests real-time energy market data from the EIA API,
- validates and transforms incoming datasets,
- stores raw and curated data in MongoDB,
- orchestrates workflows using Apache Airflow 3,
- and exposes analytics through a Flask API and dashboard.

The project demonstrates modern data engineering concepts including:

- ETL/ELT pipeline design
- workflow orchestration
- data quality validation
- MongoDB data modeling
- observability and metadata tracking
- API engineering
- modular Python architecture
- integration testing

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Apache Airflow 3 | Workflow orchestration |
| MongoDB | Raw + curated data storage |
| Flask | Reporting API + dashboard |
| UV | Python package and environment management |
| Pytest | Testing framework |
| Docker | Containerization |
| EIA API | Real-time energy market data |

---

# Data Source

Source: U.S. Energy Information Administration (EIA)

Datasets include:

- Petroleum spot prices
- Natural gas spot prices
- Time-series energy market data

API Documentation:
https://www.eia.gov/opendata/

---

# Project Architecture

global-energy-price-platform/
│
├── airflow/
├── app/
│   ├── ingestion/
│   ├── transformation/
│   ├── validation/
│   ├── loaders/
│   ├── services/
│   └── utils/
│
├── flask_app/
├── config/
├── tests/
├── docker/
├── .env.example
├── docker-compose.yml
├── pyproject.toml
└── README.md
