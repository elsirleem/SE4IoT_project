import random
import time
import json
import paho.mqtt.client as mqtt
from mqtt_config import BROKER, PORT, BASE_TOPIC, ALERT_TOPIC, PUBLISH_INTERVAL

# MQTT Client Setup
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Locations for simulation
LOCATIONS = ["location1", "location2", "location3"]

# Thresholds for Alerts
THRESHOLDS = {
    "traffic_density": 80,
    "average_speed": 25,  # Minimum speed
    "co2": 400,
    "pm25": 35,
    "pm10": 50,
    "decibel_level": 85,
    "co": 3.5
}

# Sensor Simulation Functions
def simulate_traffic_density():
    return random.randint(10, 100)

def simulate_average_speed():
    return round(random.uniform(20, 60), 2)

def simulate_co2():
    return round(random.uniform(300, 500), 2)

def simulate_pm25():
    return round(random.uniform(10, 50), 2)

def simulate_pm10():
    return round(random.uniform(20, 70), 2)

def simulate_decibel_level():
    return round(random.uniform(50, 90), 2)

def simulate_co():
    return round(random.uniform(0.5, 5.0), 2)

# Publish Critical Alert
def publish_alert(metric, value, location):
    alert_payload = {
        "metric": metric,
        "value": value,
        "location": location,
        "timestamp": int(time.time()),
        "message": f"Critical {metric} level detected at {location}: {value}",
        "details": {
            "component": metric,
            "location": location,
            "threshold_exceeded": THRESHOLDS[metric],
            "current_value": value
        }
    }
    client.publish(ALERT_TOPIC, json.dumps(alert_payload))
    print(f"ALERT Published to {ALERT_TOPIC}: {alert_payload}")

# Main Function to Simulate and Publish Data
def publish_sensor_data():
    while True:
        for location in LOCATIONS:
            # Simulate data
            data = {
                "traffic_density": simulate_traffic_density(),
                "average_speed": simulate_average_speed(),
                "co2": simulate_co2(),
                "pm25": simulate_pm25(),
                "pm10": simulate_pm10(),
                "decibel_level": simulate_decibel_level(),
                "co": simulate_co()
            }
            # Publish data to MQTT and check for alerts
            for metric, value in data.items():
                topic = f"{BASE_TOPIC}/{location}/{metric}"
                payload = json.dumps({f"{metric}": value})
                client.publish(topic, payload)

                #print(f"Published to {topic}: {payload}")

                # Check for critical levels
                if metric in THRESHOLDS and value > THRESHOLDS[metric]:
                    publish_alert(metric, value, location)
        
        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    try:
        publish_sensor_data()
    except KeyboardInterrupt:
        print("Simulation stopped.")
        client.disconnect()
