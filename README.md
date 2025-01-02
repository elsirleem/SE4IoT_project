# Iot Smart Traffic Management System

## Overview
This project demonstrated a simulated IoT system designed to manage urban traffic and monitor environmental conditions for improved sustainability. 
It integrates different components such as: 
- Random sensor data generated using Python
- Message Broker (MQTT) to route messages to the middleware 
- Middleware (NodeRed) to create alert and save to a time series Database
- Databases (InfluxDB) to save the simulated sensor data, and 
- Dashboards (Grafana) to visualize captured sensor data.

Overall, the major aim of the system is to optimize traffic flow and reduce environmental impact.

## Features
- Simulates environmental metrics like traffic density, speed, CO2, PM2.5, PM10, and noise levels.
- Processes data using Node-RED and publishes threshold-based alerts.
- Stores time-series data in InfluxDB for long-term analysis.
- Visualizes data in Grafana with customizable dashboards.
- Fully containerized for seamless deployment using Docker Compose.

## Prerequisites
Ensure the following packages are installed on your computer
- Docker Desktop 
- Python 3 and above 

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <https://github.com/elsirleem/SE4IoT_project.git>
cd <SE4IoT_project>
```

### Step 2: Start Docker Services
Run the following command to start all services (InfluxDB, Node-RED, Mosquitto MQTT broker, and Grafana):
```bash
docker-compose up -d
```
Verify the services are running:
```bash
docker ps
```

### Step 3: Run the Sensor Simulation
Navigate to the simulation script directory and run the Python script:
```bash
py sensor_simulation.py
```
Ensure the script publishes data to the MQTT broker.

### Step 4: Access the Services
- **Node-RED**: [http://localhost:1880](http://localhost:1880)
- **Grafana**: [http://localhost:3000](http://localhost:3000)

### Step 5: Configure Grafana
1. Log in to Grafana.
2. Add InfluxDB as a data source:
   - **URL**: `http://influxdb:8087`
   - **Database**: `smart_city`
3. Create dashboards to visualize metrics.


## License
This project is licensed under the MIT License.
