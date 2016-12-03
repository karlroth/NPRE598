import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep



GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_10", GPIO.OUT)
old_switch_state = 0

analogPin="P9_33"
rn=0


while True:
    new_switch_state = GPIO.input("P8_12")
    if new_switch_state == 1 and old_switch_state == 0 :
	if rn==0:
	    rn=1		
	elif rn==1:
	    exit()
    if rn==1:
	potVal=ADC.read(analogPin)
        potVolt=potVal*1.8
	now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        print "The Potentiometer Voltage is: ",potVolt
        ref = 1.8 - potVal
	current = ref/100
	Res = potVal/current
	print("The resistance is: ",Res)
	# Write to a file
        file = open("pot_data.txt", "a")
        file.write(str(potVolt)+","+str(Res)+","+str(now)+"\n")
        file.close()
        sleep(1)

