# First connect the active piezo-buzzer module to digital pin D8. 
# Then we initialize the MRAA library and set up the buzzer pin as a digital output. 
# Finally, we use a loop to turn the buzzer on and off every 0.5 seconds.
# Note that the write method of the mraa.Gpio object is used to set the state of the buzzer pin. A value of 1 sets the pin to HIGH, 
# while a value of 0 sets it to LOW.

import mraa
import time

# Connect the buzzer module to digital pin D8
buzzer_pin = 8

# Initialize the MRAA library
mraa.init()

# Initialize the buzzer as a digital output pin
buzzer = mraa.Gpio(buzzer_pin)
buzzer.dir(mraa.DIR_OUT)

# Turn the buzzer on and off in a loop
while True:
    buzzer.write(1)  # set buzzer pin to HIGH
    time.sleep(0.5)  # wait for 0.5 seconds
    buzzer.write(0)  # set buzzer pin to LOW
    time.sleep(0.5)  # wait for 0.5 seconds






