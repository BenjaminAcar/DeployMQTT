import paho.mqtt.client as mqtt

# Set the MQTT broker address
broker_address = "<master-ip>"

# Set the MQTT broker port
broker_port = 31022

# Set the MQTT client ID
client_id = "test-consumer"

# Set the MQTT username and password
username = "test"
password = "test"

# Create a new MQTT client instance
client = mqtt.Client(client_id)

# Set the MQTT authentication credentials
client.username_pw_set(username, password)

# Define the error callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed: " + str(rc))

# Set the error callback function
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Start the MQTT client loop
client.loop_start()

# Subscribe to the "test" topic
topic = "test"
client.subscribe(topic)

# Define the message callback function
def on_message(client, userdata, message):
    print("Received message on topic " + message.topic + ": " + str(message.payload))

# Set the message callback function
client.on_message = on_message

# Wait for messages
while True:
    pass

# Stop the MQTT client loop
client.loop_stop()
