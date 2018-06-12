'''
This file will use the Sense HAT as an output device. It will
dislpay a test string and numeric value on the Sense HAT's LED matrix.
'''
# These import statments bring in other Python modules.
from sense_hat import SenseHat # Provides access the Sense HAT functions
from time import sleep         # Provides pause function for our program

# String variable assigned the hello world message
message = "hello, world"

# Integer variable to display on the Sense HAT
display_number = 1

# Create a Sense HAT interface
sense = SenseHat()

# Set up the Sense HAT display color. Colors are represented as a
# list containg R-G-B (red, green, blue) values between 0 and 255.
# Try changing the values to get a different color
color = [255,0,0]

# Display the text string on the LED display using the
# Sense HAT's show_meesage function.
# text_colour isn't a typo, the Raspberry Pi originated in the UK,
# and must use their spelling for color.
# TODO Students should add their own show_message here
'''
Example:
sense.show_message(message, text_colour=color)
'''

# Wait the number of seconds passed to sleep
sleep(2)

# Display a numeric value on the LED display using the
# Sense HAT's show_letter function. The number must be turned into
# a string like str(1) 
# TODO Students should add their own show_letter here
'''
Example:
sense.show_letter(str(display_number), text_colour=color)
'''

# Wait the number of seconds passed to sleep
# TODO Students should add another sleep here
'''
Example:
sleep(1)
'''

# Clear the LED display
sense.clear()
