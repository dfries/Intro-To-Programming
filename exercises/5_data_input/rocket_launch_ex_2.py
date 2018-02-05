'''
This file porvides an example of the second step of a rocket launch program
that will be developed over the remaining exercises. It will use the
Sense HAT as both an input and an output device. It will display and
launch a virtual rocket.

In this file we will:
 - Read and store the temperature value from the Sense HAT
 - Read and store the humidity value from the Sense HAT  
'''
# These import statments bring in other Python modules.
# The first will allow us to access the Sense HAT functions.
# The second will allows us to pause our program
from sense_hat import SenseHat
from time import sleep
# TODO import rocket_display

# Requirements for this program:
# 1. Display rocket on the launch pad
# 2. Verify temperature and humidity are within acceptable ranges to launch
# 3. Display a countdown to launch from 9 to 0
# 4. Launch rocket at end of countdown if conditions are nominal

# Create a Sense HAT interface
sense = SenseHat()

# Use rocket display module to draw rocket on the launchpad
# TODO

# Read and store the temperature from the Sense HAT
temp_deg_C = sense.get_temperature()

# Read and store the humidiity from the Sense HAT
relative_humidity = sense.get_humidity

# Verify values read in
print("Read temperature: %s C" % temp_deg_C)
print("Read humidity %s %%rH" % relative_humidity)

# Verify that the temperature is between ?? and ?? degrees Celsius
# Verify that the percentage of relative humidity is between ?? and ?? percent

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay

# Once the countdown completes and the environmental conditions are verified as good
# Use the rocket display module to launch the rocket


