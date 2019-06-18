#Female to 3 female.

#Wire up the sound sensor.

#Brown Black and white jumper cables

#White cable to VCC (Power) 5v pin
#Black cable to ground
#Brown goes to digital out 

#White pin goes go to the 5 pin (first on top row)
#Black goes to groun (any available, 3rd pin on top)
#Digital goes to GPIO 17.

#Power up PI

#On Sound Sensor Red light - circuit board is getting power
#	  Green Light (adjust pot until the light turns off)
#	  Now everytime you knock beside the sensor the light should turn off
	 
#CODE:
#/usr/bin/python

#importing package
import RPi.GPIO as GPIO
import time

#setting up pin 17
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel)
	if GPIO.input(channel):
		print "Sound Detectedtected!"
	else
		print "Sound Detected!"
	
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #;let us know if the pin goes high or low
GPIO.add_event_callback(channel, callback) # assign function to GPIO pin, run function on change

while True:
	time.sleep(1)
