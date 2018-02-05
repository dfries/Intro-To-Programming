'''
This file porvides an example of the start of a rocket launch program
that will be developed over the remaining exercises. It will use the
Sense HAT as both an input and an output device. It will display and
launch a virtual rocket.

In this file we will:
 - Review the requiremnts for the launch program
 - Use comments to lay out a genral algoritm
 - Display the rocet on the laucnh pad
'''
# These import statments bring in other Python modules.
# The first will allow us to access the Sense HAT functions.
# The second will allows us to pause our program
# The third will allow us to display our rocket
from sense_hat import SenseHat
from time import sleep
from rocket_display import delta_iv_heavy

# Requirements for this program:
# 1. Display rocket on the launch pad
# 2. Verify temperature and humidity are within acceptable ranges to launch
# 3. Display a countdown to launch from 9 to 0
# 4. Launch rocket at end of countdown if conditions are nominal

# Algorithm

# Use rocket display module to draw rocket on the launchpad

# Read and store the temperature from the Sense HAT
# Read and store the humidiity from the Sense HAT
# Verify that the temperature is between ?? and ?? degrees Celsius
# Verify that the percentage of relative humidity is between ?? and ?? percent
# The Sense HAT can also provide pressure in millibars. Also check that?

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay

# Once the countdown completes and the environmental conditions are verified as good
# Use the rocket display module to launch the rocket


