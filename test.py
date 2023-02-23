import paho.mqtt.client as mqtt
import time
# Set the MQTT broker address
broker_address = "<master-IP>"

# Set the MQTT broker port
broker_port = 31022

# Set the MQTT client ID
client_id = "test-client"

# Set the MQTT username and password
username = "test"
password = "test"

# Create a new MQTT client instance
client = mqtt.Client(client_id)

# Set the MQTT authentication credentials
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish a message to the "test" topic
topic = "test"
payload = "Hello, world!"
while True:
    time.sleep(5)
    client.publish(topic, payload)

# Disconnect from the MQTT broker
client.disconnect()
