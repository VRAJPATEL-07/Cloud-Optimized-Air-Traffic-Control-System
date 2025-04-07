# Cloud-Optimized-Air-Traffic-Control-System
# ✈️ Cloud-Optimized Air Traffic Control System

A cloud-based solution designed to modernize and optimize air traffic control using real-time data handling, congestion prediction, and automated rerouting. This project reflects my passion for aviation and my technical journey into cloud computing and scalable system architecture.

---

## 🚀 Project Overview

This system simulates a cloud-native Air Traffic Control (ATC) solution to:

- Monitor and manage real-time flight data across multiple airports.
- Predict airspace congestion and dynamically reroute flights.
- Handle system failures gracefully using cloud redundancy.
- Utilize scalable and distributed messaging for efficient data flow.

---

## 🌐 Tech Stack

- **Python** – Backend logic and simulation engine
- **Google Cloud Pub/Sub** – Real-time messaging and event distribution
- **PostgreSQL** – Persistent storage for flight and traffic data
- **GCP** – Infrastructure and cloud tools

---

## ⚙️ Features

- ✈️ Live monitoring of simulated flights
- 📊 Congestion prediction engine
- 🔁 Dynamic flight rerouting
- 🛡️ Disaster recovery and fault tolerance
- ☁️ Scalable cloud-first architecture

---

## 📦 Project Structure
cloud-atc-system/ ├── backend/ │ ├── main.py # Core application logic │ ├── pubsub_producer.py # Publishes flight events │ └── pubsub_subscriber.py # Subscribes and processes flight events ├── database/ │ ├── schema.sql # PostgreSQL DB structure │ └── db_connector.py # DB interaction ├── utils/ │ └── flight_generator.py # Simulated flight data generator ├── README.md └── requirements.txt

---

## 🔧 Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/VRAJPATEL-07/cloud-optimized-air-traffic-control-system.git
   cd cloud-optimized-air-traffic-control-system
Install dependencies

pip install -r requirements.txt
Set up Google Cloud credentials
Make sure you have GCP Pub/Sub configured and authentication set.

Initialize database

psql -U your_user -d your_db -f database/schema.sql
Run the system

python backend/main.py
