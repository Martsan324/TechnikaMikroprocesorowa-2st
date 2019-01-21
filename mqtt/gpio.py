import RPi.GPIO as gp
import time

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(9, gp.OUT)
gp.setup(10,gp.OUT)
gp.setup(11,gp.IN,gp.PUD_UP)
gp.setup(8,gp.IN, gp.PUD_UP)

while True:
	if(gp.input(11) == 0):
		gp.output(10, not gp.input(10))
		time.sleep(0.4)
	if(gp.input(8) == 0):
		gp.output(9, not gp.input(9))
		time.sleep(0.4)