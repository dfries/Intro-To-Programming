'''
This file contains the functions needed to display a rocket on the
launch pad and provide the visual for the rocket launch
'''

import pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500,700))
DISPLAYSURF.fill((0,0,0)) # black, change to blue?
pygame.display.set_caption("Rocket Launch")

# only calling one at a tiem for now, normally in a loop
pygame.display.update()

def display_launchpad():

    print("TODO: Displaying launchpad")
    # TODO

def display_rocket():

    rocketImg = pygame.image.load("../rocket_display/delta_iv_heavy.png")
    rocketX = 150
    rocketY = 60
    DISPLAYSURF.blit(rocketImg, (rocketX, rocketY))

    pygame.display.update()

    print("TODO: Displaying rocket")
    # TODO

def launch_rocket():
    print("TODO: Launching rocket")
    # TODO

def end():
    pygame.quit()
