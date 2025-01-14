import random
import time
import json
import configparser
import paho.mqtt.client as mqtt

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# MQTT Client Setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(config['mqtt']['broker'], int(config['mqtt']['port']), 60)

# Locations for simulation
LOCATIONS = config['locations']['locations'].split(',')

# Thresholds for Alerts
THRESHOLDS = {
    "traffic_density": int(config['thresholds']['traffic_density']),
    "average_speed": int(config['thresholds']['average_speed']),
    "co2": int(config['thresholds']['co2']),
    "pm25": int(config['thresholds']['pm25']),
    "pm10": int(config['thresholds']['pm10']),
    "decibel_level": int(config['thresholds']['decibel_level']),
    "co": float(config['thresholds']['co'])
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
    client.publish(config['mqtt']['alert_topic'], json.dumps(alert_payload))
    #print(f"ALERT Published to {config['mqtt']['alert_topic']}: {alert_payload}")

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
                topic = f"{config['mqtt']['base_topic']}/{location}/{metric}"
                payload = json.dumps({f"{metric}": value})
                client.publish(topic, payload)

                print(f"Published to {topic}: {payload}")

                # Check for critical levels
                if metric in THRESHOLDS and value > THRESHOLDS[metric]:
                    publish_alert(metric, value, location)
        
        time.sleep(int(config['mqtt']['publish_interval']))

if __name__ == "__main__":
    try:
        publish_sensor_data()
    except KeyboardInterrupt:
        print("Simulation stopped.")
        client.disconnect()
