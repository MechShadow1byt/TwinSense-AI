# 🌍 TwinSense AI

> An AI-powered Environmental Digital Twin platform for monitoring, analysing, and optimising industrial energy and sustainability.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

TwinSense AI is an AI-powered Environmental Digital Twin platform that helps industries understand, monitor, and optimise their factory operations.

The project creates a virtual representation of a factory where machines, sensors, and operational data are connected together. The Digital Twin can analyse energy usage, estimate environmental impact, and eventually provide AI-driven recommendations for improving efficiency and sustainability.

The long-term vision is to make Digital Twin technology affordable and accessible for small and medium-sized manufacturers.

---

# ✨ Current Features

## Backend

- FastAPI backend
- REST API architecture
- Interactive Swagger documentation
- Modular project structure

## Factory Management

- Create factories
- Retrieve factory information
- Store multiple factories

## Machine Management

- Add machines to factories
- Store machine specifications
- Operating hours tracking

## Sensor Management

- Attach sensors to individual machines
- Support for multiple sensor types
- Sensor value storage

## Energy Analytics

- Calculate total factory energy consumption
- Machine-wise energy calculation
- Energy report generation
- Energy usage classification
  - High
  - Medium
  - Low

---

# 🚧 Planned Features

- AI optimisation engine
- Machine efficiency prediction
- Carbon footprint estimation
- Pollution prediction
- Predictive maintenance
- Digital Twin visualisation
- Real-time dashboard
- IoT sensor integration
- Weather API integration
- Satellite data integration
- Production analytics
- Cost optimisation
- REGENARC energy intelligence module

---

# 🏗 Current Architecture

```
Factory
│
├── Machines
│      │
│      ├── Sensors
│      ├── Power Rating
│      ├── Operating Hours
│      └── Energy Usage
│
└── Energy Analytics
       │
       ├── Total Factory Energy
       ├── Machine Reports
       └── Usage Classification
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

## AI (Planned)

- Scikit-learn
- TensorFlow
- PyTorch

## Data

- Pandas
- NumPy

## Computer Vision (Planned)

- OpenCV

## Database (Upcoming)

- SQLite
- PostgreSQL

## IoT (Future)

- ESP32
- MQTT
- Environmental Sensors

---

# 🚀 Current API Endpoints

## System

```
GET /
GET /system/health
```

## Factory APIs

```
POST /factory
GET /factory/{factory_id}
```

## Machine APIs

```
POST /factory/{factory_id}/machine
POST /machine
```

## Sensor APIs

```
POST /factory/{factory_id}/machine/{machine_index}/sensor
```

## Energy APIs

```
GET /factory/{factory_id}/energy
GET /factory/{factory_id}/energy/report
```

---

# 🚀 Running the Project

Clone the repository

```bash
git clone https://github.com/MechShadow1byt/TwinSense-AI.git
```

Move into backend

```bash
cd TwinSense-AI/backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

---

# 📄 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📂 Project Structure

```
TwinSense-AI/

backend/
│
├── app/
│   ├── main.py
│   ├── models.py
│   └── __init__.py
│
├── requirements.txt
│
README.md
```

---

# 🎯 Development Roadmap

## Phase 1 ✅

- FastAPI backend
- Factory APIs
- Machine APIs
- Sensor APIs
- Energy calculation
- Energy reporting

## Phase 2 (Current Goal)

- Database integration
- Machine efficiency scoring
- AI recommendations
- Factory dashboard endpoint

## Phase 3

- Digital Twin visualisation
- Dashboard
- Live IoT data
- REGENARC integration

## Phase 4

- Predictive AI
- Cloud deployment
- Multi-factory management
- Mobile application

---

# 👨‍💻 Author

**Bhavit**

Class 10 Student • AI & Mechanical Engineering Enthusiast

Building intelligent systems that connect AI with the physical world through Digital Twins, Energy Optimisation, and Sustainable Manufacturing.

---

⭐ Star the repository if you'd like to follow the development of TwinSense AI.