import paho.mqtt.publish as publish
import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
gp.setup(11,gp.IN,gp.PUD_UP)
gp.setup(8,gp.IN, gp.PUD_UP)
MQTT_SERVER = "192.168.43.158"
MQTT_PATH = "test"
while True:
	if (gp.input(11) == 0):
		print("switch #1")
		publish.single(MQTT_PATH, "switch1", hostname=MQTT_SERVER)
		time.sleep(0.4)
	if (gp.input(8) == 0):
		print("switch #2")
		publish.single(MQTT_PATH, "switch2", hostname=MQTT_SERVER)
		time.sleep(0.4)