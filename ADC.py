import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep







analogPin="P9_33"
while(1):
        potVal=ADC.read(analogPin)
        potVolt=potVal*1.8
	now = datetime.datetime.now().strftime("%B-%d %Y %H:%M:%S")
        print(now)
        print "The Potentiometer Voltage is: ",potVolt
        sleep(1)
