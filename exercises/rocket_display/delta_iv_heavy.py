'''
This file contains the functions needed to display a rocket on the
launch pad and provide the visual for the rocket launch
'''

import pygame
import os
from pygame.locals import *
from time import sleep

def init():
    global launchpadImg, rocketImg, flamesImg
    launchpadImg = pygame.image.load("../rocket_display/launch_pad.png")
    rocketImg = pygame.image.load("../rocket_display/delta_iv_heavy.png")
    flamesImg = pygame.image.load("../rocket_display/flames.png")

    fill_background()

    # only calling one at a time for now, normally in a loop
    pygame.display.update()

def fill_background():
    DISPLAYSURF.fill((16,110,172))

def display_launchpad():

    global launchpadImg
    DISPLAYSURF.blit(launchpadImg, (0, 0))

def display_rocket(x = 0, y = 0):

    global rocketImg
    rocketX = 150 + x
    rocketY = 60 + y
    DISPLAYSURF.blit(rocketImg, (rocketX, rocketY))

    pygame.display.update()

def display_flames(x = 0, y = 0):

    global showFlames
    if showFlames:
        global flamesImg
        flamesX = 162 + x
        flamesY = 677 + y
        DISPLAYSURF.blit(flamesImg, (flamesX, flamesY))

        pygame.display.update()

def enginesOn(running):
    global showFlames
    showFlames = running
    display_flames()

def launch_rocket():
    global rocketImg, showFlames
    if showFlames:
        y_acceleration = -.2
    else:
        y_acceleration = .3
    x = 0
    y = 0
    rotate = 0
    y_velocity = 0
    while (y_acceleration > 0 and y < 700) or (y_acceleration < 0 and y > -700):
        y_velocity += y_acceleration
        y += y_velocity
        if y_acceleration > 0:
            # Give the launching with the engines off a cheap dramatic
            # end to the rocket.  Rotate it, and with ypgame, the rotation
            # isn't a very high quality rotation distorting the image as
            # it "falls".
            rotate += 4
            x -= 7
            rocketImg = pygame.transform.rotate(rocketImg, 1)
        fill_background()
        display_launchpad()
        display_rocket(x, y)
        display_flames(x, y)
        sleep(.033)

def end():
    pygame.quit()

pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "50,30"
DISPLAYSURF = pygame.display.set_mode((500,700))
pygame.display.set_caption("Rocket Launch")
launchpadImg = None
rocketImg = None
flamesImg = None
showFlames = False
init()
