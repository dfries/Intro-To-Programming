'''
This file will use the Sense HAT as an output device. It will
dislpay a test string and numeric value on the Sense HAT's LED matrix.
'''
# These import statments bring in other Python modules.
# The first will allow us to access the Sense HAT functions.
# The second will allows us to pause our program
from sense_hat import SenseHat
from time import sleep

# String variable assigned the hello world message
message = "hello, world"

# Integer variable to display on the Sense HAT
display_number = 1

# Create a Sense HAT interface
sense = SenseHat()

# Set up some Sense HAT display colors. Colors are represented as
# lists containg R-G-B (red, green, blue) values between 0 and 255.
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

# Display the text string on the LED display using the 
# Sense HAT's show_meesage function. Example:
# sense.show_message(message, text_colour=red)
# TODO Sthudents should add their own show_message here

# Wait the number of seconds passed to sleep
sleep(2)

# Display a numeric value on the LED display using the 
# Sense HAT's show_letter function. Example:
# sense.show_letter(str(display_number), text_colour=blue)
# TODO Students should add their own show_letter here


# Wait the number of seconds passed to sleep
# TODO Students should add another sleep here

# Clear the LED display
sense.clear()
