'''
This file provides an example of the final step of a rocket launch program
that will be developed over the remaining exercises. It will use the
Sense HAT as both an input and an output device. It will display and
launch a virtual rocket.

In this file we:
 - Organize the Program into functions
 - Verify launch conditions
 - Launch the rocket
'''
# These import statments bring in other Python modules.
# Load the module or the hardware Sense HAT, or the emulator
try:
    from sense_hat import SenseHat             # Allow access to the Sense HAT functions
except Exception as e:
    print(e)
    print("Using emulator instead")
    from sense_emu import SenseHat             # Allow access to Sense HAT emulator
from time import sleep                     # Allows us to pause our program

# Allow us to display our rocket
import sys
sys.path.append("..")
from rocket_display import delta_iv_heavy

# Set up some Sense HAT display colors. Colors are represented as
# lists containg R-G-B (red, green, blue) values between 0 and 255.
white   = [255, 255,  255]
green   = [  0, 255,    0]
yellow  = [255, 255,    0]
red     = [255,   0,    0]

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
print("Read temperature: %s C" % temp_deg_C)
print("Read humidity %s %%rH" % relative_humidity)

# Verify that the temperature is between 10 and 37.8 degrees Celsius
temp_good = False
if (temp_deg_C >= 10.0 and temp_deg_C <= 37.8): # Between 50 and 100 F
    temp_good = True
else:
    print("WARNING: Temperature of %s C is outside nominal" % temp_deg_C)

# Verify that the percentage of relative humidity is between 20 and 90 percent
humidity_good = False
if (relative_humidity >= 20.0 and relative_humidity <= 90.0):
    humidity_good = True
else:
    print("WARNING: Humidity of %s %%rH is outside nominal" % relative_humidity)

# Overall environment status is a combination of temperature and humidity.
# If either if False the envirnment good status will also be set to False.
env_good = (temp_good and humidity_good)

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay
countdown_complete = False
letter_color = white
for i in range(9, -1, -1):
    if i == 3:
        # Ignite the engines before takeoff
        delta_iv_heavy.enginesOn(True)
        letter_color = red
    if i == 1:
        letter_color = yellow
    if i == 0:
        countdown_complete = True
        letter_color = green
    sense.show_letter(str(i), text_colour=letter_color)
    sleep(1.0)

# Once the countdown completes and the environmental conditions are
# verified as good, use the rocket display module to launch the rocket
if env_good and countdown_complete:
    # TODO launch the rocket
    delta_iv_heavy.launch_rocket()
else:
    # Abort the launch
    print("Aborting Launch Sequence")
    delta_iv_heavy.enginesOn(False)
