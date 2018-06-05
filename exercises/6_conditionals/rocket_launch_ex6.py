'''
This file provides an example of the third step of a rocket launch program
that will be developed over the remaining exercises. It will use the
Sense HAT as both an input and an output device. It will display and
launch a virtual rocket.

In this file we:
 - Verify the ranges of the humidity and temperature
'''
# These import statments bring in other Python modules.
from sense_hat import SenseHat  # Allow access to the Sense HAT functions
from time import sleep          # Allows us to pause our program

# Allow us to display our rocket
import sys
sys.path.append("..")
from rocket_display import delta_iv_heavy

# Requirements for this program:
# 1. Display rocket on the launch pad
# 2. Verify temperature and humidity are within acceptable ranges to launch
# 3. Display a countdown to launch from 9 to 0
# 4. Launch rocket at end of countdown if conditions are nominal

# Create a Sense HAT interface
sense = SenseHat()

# Use rocket display module to draw rocket on the launchpad
delta_iv_heavy.display_launchpad()
delta_iv_heavy.display_rocket()

# Read and store the temperature from the Sense HAT
temp_deg_C = sense.get_temperature()

# Read and store the humidity from the Sense HAT
relative_humidity = sense.get_humidity()

# Verify values read in
print("Temperature reading (deg C): ", temp_deg_C)
print("Humidity reading (%rH): ", relative_humidity)

# Verify that the temperature is between 10 and 37.8 degrees Celsius
temp_good = False
if (temp_deg_C >= 10.0 and temp_deg_C <= 37.8): # Between 50 and 100 F
    temp_good = True
else:
    print("WARNING: Temperature is outside nominal: ", temp_deg_C)

# Verify that the percentage of relative humidity is between 20 and 90 percent
humidity_good = False
if (relative_humidity >= 20.0 and relative_humidity <= 90.0):
    humidity_good = True
else:
    print("WARNING: Humidity is outside nominal: ", relative_humidity)

# Overall environment status is a combination of temperature and humidity.
# If either is False the environment good status will also be set to False.
env_good = (temp_good and humidity_good)

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay

# Once the countdown completes and the environmental conditions are
# verified as good, use the rocket display module to launch the rocket

sleep(10)
sense.clear()
delta_iv_heavy.end()
