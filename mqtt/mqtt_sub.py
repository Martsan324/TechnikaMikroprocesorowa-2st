import paho.mqtt.client as mqtt
import RPi.GPIO as gp 
MQTT_SERVER = "192.168.43.158"
MQTT_PATH = "test"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected!")
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(str(msg.payload))
	if "red1" in str(msg.payload):
		gp.output(10,gp.HIGH)
	if "red0" in str(msg.payload):
		gp.output(10,gp.LOW)
	if "green1" in str(msg.payload):
		gp.output(9,gp.HIGH)
	if "green0" in str(msg.payload):
		gp.output(9,gp.LOW)
gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(9, gp.OUT)
gp.setup(10,gp.OUT)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()