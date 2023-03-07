# This code initializes the HC-SR04 ultrasonic sensor on GPIO pins 2 and 4, and continuously 
# measures the distance to an object in front of the sensor. The write() method is used to 
# send a 10us trigger pulse to start the measurement, and the read() method is used to 
# measure the duration of the echo pulse. The distance is then calculated from the duration 
# of the echo pulse and printed to the console.

import mraa
import time

# initialize GPIO pins
trig_pin = mraa.Gpio(2)
echo_pin = mraa.Gpio(4)

# set GPIO directions
trig_pin.dir(mraa.DIR_OUT)
echo_pin.dir(mraa.DIR_IN)

while True:
    # send 10us trigger pulse to start measurement
    trig_pin.write(0)
    time.sleep(0.00001)
    trig_pin.write(1)
    time.sleep(0.00001)
    trig_pin.write(0)
    
    # measure duration of echo pulse
    while echo_pin.read() == 0:
        pulse_start = time.time()
    while echo_pin.read() == 1:
        pulse_end = time.time()
    
    # calculate distance from duration of echo pulse
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    
    # print distance in centimeters
    print("Distance: %.2f cm" % distance)
    
    # wait 0.5 seconds before taking another measurement
    time.sleep(0.5)
