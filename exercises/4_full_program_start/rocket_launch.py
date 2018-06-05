'''
This file is a rocket launch program that will be developed over
the remaining exercises. It will use the Sense HAT as both an input
and an output device. It will display and launch a virtual rocket.

In this file we will:
 - Review the requirements for the launch program
 - Use comments to lay out a general algorithm
 - Display the rocket on the launch pad
'''
# These import statments bring in other Python modules.
from sense_emu import SenseHat  # Allow access to the Sense HAT functions
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

# TODO Students should add additional comments here
# The comments should lay out the remaining structure of the program
# to cover all the requirements of the program

sleep(10)
sense.clear()
delta_iv_heavy.end()

