import Adafruit_BBIO.GPIO as GPIO
import time
import datetime

GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_10", GPIO.OUT)

old_switch_state = 0
GPIO.output("P8_10", GPIO.LOW)
LED = 0

while True:
    new_switch_state = GPIO.input("P8_12")
    if new_switch_state == 1 and old_switch_state == 0 :
	#Turn on or off LED
	if LED == 0 :
	    GPIO.output("P8_10", GPIO.HIGH)
	    LED = 1
	    print("Its On!")
	elif LED == 1:
	    GPIO.output("P8_10", GPIO.LOW)
	    print("AHHHHH I'M SCARED OF THE DARK!!!!!")
	    LED = 0
	#Set and print time
	now = datetime.datetime.now().strftime("%B-%d %Y %H:%M:%S")       
	print(now)
        time.sleep(0.5)
    old_switch_state = new_switch_state
