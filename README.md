# Intro To Programming
Introduction to Programming course with Python and Raspberry Pi

## Overview
This repo contains documentation, code examples, and exercises for an introduction to programming course aimed at middle school aged students. It is intended for students with no programming experience and should last between 1 and 2 hours. This branch (abridged_class) cleans up and shortens the examples to make the class move along quicker.

The code for this course is Python 3 and is targeted at a Raspberry Pi that has a Sense HAT.

## Presentation Material
A course overview, detailed outline, and presentation slides are available on [Google Drive](https://drive.google.com/open?id=1_RB1govPvCtqE3c3gReNsyUkUMzxBLm4) 

## Set Up
How to set up common environments to use the examples and exercises for the course.

### Easy
1. Acquire a Raspberry Pi 3 B through the [Raspberry Pi Foundation](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) or from [Amazon](http://a.co/bdqYFoy). Optionally [kits](http://a.co/42vVSm4) come with everything needed to get started. 
2. Acquire a Sense HAT through the [Raspberry Pi Foundation](https://www.raspberrypi.org/products/sense-hat/) or from [Amazon](http://a.co/4JfWAZ2).
3. [Download NOOBS](https://www.raspberrypi.org/downloads/) and [install](https://www.raspberrypi.org/learning/software-guide/quickstart/) Raspbian on SD Card for the Raspberry Pi.
4. Raspbian includes Python, the Sense HAT API, and the Sense HAT emulator. 

### Windows
Running the examples on Windows is a challenge. The Sense HAT Emulator is the only real option on Windows but it requires PyGObject (GTK3 bindings for Python) which is a challenge to [install](http://pygobject.readthedocs.io/en/latest/getting_started.html#windows) in an environment that the Python sense-emu library can also be installed. 
Instead:
1. Download and install [VirtualBox](https://www.virtualbox.org/)
2. Download an ISO of Linux (e.g. [Mint](https://linuxmint.com/))
3. Create a VM in Virtual Box with Linux ISO (note: may need to change BIOS settings for 64 bit virtualization)
4. Install the guest addon additions to Linux VM (under Devices in VirtualBox menu)
5. Install need Python libraries to Linux VM:
   1. `sudo apt install python3-setuptools`
   2. `sudo apt install python3-pip`
   3. `sudo pip3 install sense_emu` (may throw errors building bdist_wheel during install, but it seemed to work ok)
   4. `sudo pip3 install pygame`
6. Test that the install worked by launching the Sense HAT Emulator GUI from the command line with: `sense_emu_gui &`
7. Any source in this project can be run with the emulator by changing import statments to: `from sense_emu import SenseHat` 

## Reference Information

### Python
* [Python Software Foundation](https://www.python.org/)
* [Download Python](https://www.python.org/downloads/)
* [Python 3 Documentation](https://docs.python.org/3/)
* [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)

### Pygame
* [Pygame](https://www.pygame.org)
* [Invent with Python](http://inventwithpython.com/pygames)

### Raspberry Pi
* [Raspberry Pi Foundation](https://www.raspberrypi.org/)
* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)

### Sense HAT
* [Sense HAT](https://www.raspberrypi.org/products/sense-hat/)
* [Sense HAT Documentation](http://pythonhosted.org/sense-hat/)
* [Sense HAT API](http://pythonhosted.org/sense-hat/api/)
* [Sense HAT Emulator Documentation](https://sense-emu.readthedocs.io/en/v1.0/)
* [Installing the Sense HAT Emulator](https://sense-emu.readthedocs.io/en/v1.0/install.html)

### VirtualBox
* [VirtualBox](https://www.virtualbox.org/)
* [VirtualBox User Manual](https://www.virtualbox.org/manual/UserManual.html)

### Linux
* [Raspbian](https://www.raspberrypi.org/downloads/)
* [Linux Mint](https://linuxmint.com/)
