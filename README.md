# IoT Project: Smart Traffic Management System

## Overview
This project is a simulated IoT system designed to manage urban traffic and monitor environmental conditions. It integrates components such as sensors, middleware, databases, and dashboards to optimize traffic flow and reduce environmental impact.

## Features
- Simulates environmental metrics like traffic density, speed, CO2, PM2.5, PM10, and noise levels.
- Processes data using Node-RED and publishes threshold-based alerts.
- Stores time-series data in InfluxDB for long-term analysis.
- Visualizes data in Grafana with customizable dashboards.
- Fully containerized for seamless deployment using Docker Compose.

## Prerequisites
- Docker and Docker Compose installed on your system.
- Python (for running simulation scripts).

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_name>
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
python sensor_simulation.py
```
Ensure the script publishes data to the MQTT broker.

### Step 4: Access the Services
- **Node-RED**: [http://localhost:1880](http://localhost:1880)
- **Grafana**: [http://localhost:3000](http://localhost:3000)
  - Default Username: `admin`
  - Default Password: `admin`

### Step 5: Configure Grafana
1. Log in to Grafana.
2. Add InfluxDB as a data source:
   - **URL**: `http://influxdb:8086`
   - **Database**: `smart_city`
3. Create dashboards to visualize metrics.

## Docker Compose Configuration
The `docker-compose.yml` file includes the following services:
- **InfluxDB**: Stores time-series data.
- **Node-RED**: Processes data and publishes alerts.
- **Mosquitto MQTT Broker**: Handles messaging between components.
- **Grafana**: Visualizes data from InfluxDB.

## File Structure
```
|-- docker-compose.yml      # Docker Compose configuration
|-- sensor_simulation.py    # Python script for simulating sensor data
|-- mqtt_config.py          # MQTT configuration file
|-- README.md               # Project documentation
```

## Future Enhancements
- Add authentication and encryption for MQTT and InfluxDB.
- Implement machine learning models for traffic prediction.
- Integrate additional environmental sensors.

## Troubleshooting
### Common Issues
- **MQTT Connection Error**:
  - Ensure the Mosquitto broker is running and the simulation script points to the correct broker address.
- **InfluxDB Write Error**:
  - Verify the database exists and the data format matches InfluxDB requirements.
- **Grafana Connection Issue**:
  - Check the InfluxDB URL in the data source configuration.

## License
This project is licensed under the MIT License.
