import paho.mqtt.client as mqtt
import json
import time
import random

broker_address = "mqtt_broker_ip"
port = 1883
topic_temperature = "sensors/temperature"
topic_humidity = "sensors/humidity"

client = mqtt.Client()
client.connect(broker_address, port)

while True:
    sensor_data = {
        "sensor_id": "unique_sensor_id",
        "value": str(random.uniform(20, 30)),  # Replace with actual sensor data
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S')
    }
    
    payload = json.dumps(sensor_data)
    
    client.publish(topic_temperature, payload)
    
    time.sleep(5)  # Adjust the publishing interval as needed
