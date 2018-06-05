'''
This file provides an example of the start of a rocket launch program
that will be developed over the remaining exercises. It will use the
Sense HAT as both an input and an output device. It will display and
launch a virtual rocket.

In this file we will:
 - Review the requirements for the launch program
 - Use comments to lay out a general algorithm
 - Display the rocket on the launch pad
'''
# These import statments bring in other Python modules.
from sense_emu import SenseHat             # Allow access to the Sense HAT functions
from time import sleep                     # Allows us to pause our program

# Allow us to display our rocket
import sys
sys.path.append("..")
from rocket_display import delta_iv_heavy

# Requirements for this program:
# 1. Display rocket on the launch pad
# 2. Verify temperature and humidity are within acceptable ranges to launch
# 3. Display a countdown to launch from 9 to 0
# 4. Launch rocket at end of countdown if conditions are nominal

# Algorithm

# Use rocket display module to draw rocket on the launchpad
delta_iv_heavy.display_launchpad()
delta_iv_heavy.display_rocket()

# Read and store the temperature from the Sense HAT
# Read and store the humidity from the Sense HAT
# Verify that the temperature is between ?? and ?? degrees Celsius
# Verify that the percentage of relative humidity is between ?? and ?? percent
# The Sense HAT can also provide pressure in millibars. Also check that?

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay

# Once the countdown completes and the environmental conditions are
# verified as good, use the rocket display module to launch the rocket
sleep(20)
delta_iv_heavy.end()


