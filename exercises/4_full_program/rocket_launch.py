'''
This file is a rocket launch program that will be developed over
the remaining exercises. It will use the Sense HAT as both an input
and an output device. It will display and launch a virtual rocket.

In this file we will do:
 - Exercise 4 - Read input for environmental conditions
 - Exercise 5 - Use conditional logic (if/else) to verify env conditions
 - Exercise 6 - Create a for loop for the rocket countdown and output that to the SenseHAT
 - Exercise 7 -  Use functions to launch out rocket

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

# Read and store the temperature from the Sense HAT
# TODO Ex4: Add a variable and store temp reading
''' 
Example:
temp_deg_C = sense.get_temperature()
'''

# Read and store the relative humidity from the Sense HAT
# TODO Ex4: Add a variable and store humidity reading
''' 
Example:
humidity = sense.get_humidity()
'''

# Verify values read in
# TODO Ex4: print out both variables
''' 
Example:
print("Temperature reading (deg C):", temp_deg_C)
print("Humidity reading (%rH):", humidity)
'''

# Verify that the temperature is between 10 and 37.8 degrees Celsius
temp_good = False # Variable to store result of temp check
# TODO Ex 5: Add an if/else statment here that checks temperature
'''
Example:
if (temp_deg_C >= minmum and temp_deg_C <= maximum):
    temp_good = True
else:
    print a warning message
'''

# Verify that the percentage of relative humidity is between 20 and 90 percent
humidity_good = False # Variable to store result of humidity check
# TODO Ex 5: Add an if/else statment here that checks humidity that is similar to temp
'''
Example:
if (humidity >= minmum and humidity <= maximum):
    humidity_good = True
else:
    print a warning message
'''

# Overall environment status is a combination of temperature and humidity.
# If either is False the environment good status will also be set to False.
# TODO Ex 5: Add env_good boolean variable set by combining temp and humidity with 'and'
'''
Example:
env_good = (temp_good and humidity_good)
'''

# Count down from 9 to 0
# Display each number on the Sense HAT LED dsiplay
countdown_complete = False
# TODO Ex 6: Add a for loop here that counts down from 9 
#            Inside the loop display the count on the SenseHAT
#            and use an if/else to either wait 1 sec or set conntdown_complete
'''
Example:
for i in range(??, ??, -1):
    sense.show_letter(str(??))
    if i == 0:
         countdown_complete = True
    else:
        sleep 1 second
'''

# Once the countdown completes and the environmental conditions are
# verified as good, use the rocket display module to launch the rocket
# TODO EX 7: Add an if/else block that verfies lauch conditions and 
#            launches the rocket if all conditions are good or 
#            aborts the launch with a message
'''
Example:
if env_good and countdown_complete:
    # Launch the rocket with delta_iv_heavy functions 
    delta_iv_heavy.enginesOn(True) 
    delta_iv_heavy.launch_rocket()
else:
    # Abort the launch
    print an abort message
    turn the eingins off with delta_iv_heavy.enginesOn(False)
'''

sleep(10)
sense.clear()
delta_iv_heavy.end()

