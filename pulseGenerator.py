#Generate a square wave


#Joint project between Michael Cheng and Karl Roth
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
#Signal can come from any of the GPIO pins on the BBB
#Maximum voltage is 1.8V from GPIO pins
GPIO.setup("P9_12",GPIO.OUT)

#Have the GPIO Pin run on pulse mode
#The shorter the sleep time for the HIGH Output,
#the narrower the pulse width
#Frequency is 60 Hz, like that of the pulse generators
#in the NPRE 451 Lab
while True:
	GPIO.output("P9_12",GPIO.HIGH)
	time.sleep(0.02)
	GPIO.output("P9_12",GPIO.LOW)
	time.sleep(0.02)


