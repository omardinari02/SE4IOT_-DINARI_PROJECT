import paho.mqtt.client as mqtt
import time
import json
import random

MQTT_BROKER = "mqtt_broker"
MQTT_PORT = 1883
MQTT_TOPIC = "agriculture/field1/sensors"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(15, 35), 2),
        "soil_moisture": round(random.uniform(20, 80), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "timestamp": time.time()
    }

while True:
    sensor_data = generate_sensor_data()
    payload = json.dumps(sensor_data)
    client.publish(MQTT_TOPIC, payload)
    print(f"Published: {payload}")
    time.sleep(5)
