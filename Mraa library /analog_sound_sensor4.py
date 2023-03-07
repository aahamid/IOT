# This code initializes the analog sound sensor with 4 pins on analog pin 0 and continuously 
# reads the analog value from the sensor. The read() method returns the analog value as 
# an integer between 0 and 1023.

import mraa
import time

# initialize analog input pin
analog_pin = mraa.Aio(0)

while True:
    # read analog value from sensor
    value = analog_pin.read()
    
    # print analog value
    print("Analog value: %d" % value)
    
    # wait 0.5 seconds before taking another measurement
    time.sleep(0.5)
