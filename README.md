# Intro To Programming
Introduction to Programming course with Python and Raspberry Pi

## Overview
This repo contains documentation, code examples, and exercises for an introduction to programming couse aimed at middle school aged students. It is intended for students with no programming experience and should last between 1 and 2 hours.

The code for this course is Python 3 and is targeted at a Raspberry Pi that has a Sense HAT.

## TODO
List of items still to do in the project
* Add additional comments and explanation to all code examples
* Create the grapical scene for rocket display main program module
* Create the launchpad for the rocket display graphical scene
* Add code for the launch that lifts the rocket off int he rocket display module

## Set Up
How to set up common environments to use the examples and exercises for the course.

### Easy
1. Acquire a Raspberry Pi 3 B through the [Raspberry Pi Foundation](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) or from [Amazon](http://a.co/bdqYFoy). Optionally [kits](http://a.co/42vVSm4) come with everything needed to get started. 
2. Acquire a Sense HAT through the [Raspberry Pi Foundation](https://www.raspberrypi.org/products/sense-hat/) or from [Amazon](http://a.co/4JfWAZ2).
3. [Download NOOBS](https://www.raspberrypi.org/downloads/) and [install](https://www.raspberrypi.org/learning/software-guide/quickstart/) Raspbian on SD Card for the Raspberry Pi.
4. Raspbian includes Python, the Sense HAT API, and the Sense HAT emulator. 

### Windows
Running the examples on Windows is a challenge. The Sense HAT Emulator is the only real option on Windows but it requires PyGObject (GTK3 bindings for Ptyhon) which is a challenge to [install](http://pygobject.readthedocs.io/en/latest/getting_started.html#windows) in an environment that the Python sense-emu library can also be installed. Instead:
1. Download and install [VirtualBox](https://www.virtualbox.org/)
2. Download an ISO of Linux (e.g. [Mint](https://linuxmint.com/))
3. Create a VM in Virtual Box with Linux ISO (note: may need to change BIOS settings for 64 bit virtualization)
4. Install the guest addon additions under Devices in VirtualBox
5. Install need Python libraries to Linux VM:
   1. sudo apt install python3-setuptools
   2. sudo apt install python3-pip
   3. sudo pip install sense_emu (this may throw errors building bdist_wheel during install but it seemed to work ok)
6. Test that the install worked by launching the Sense HAT Emulator GUI fomr the command line with: sense_emu_gui

## Reference Information

### Python
* [Python Software Foundation](https://www.python.org/)
* [Download Python](https://www.python.org/downloads/)
* [Python 3 Documentation](https://docs.python.org/3/)
* [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)

### Raspberry Pi
* [Raspberry Pi Foundation](https://www.raspberrypi.org/)
* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* [Raspberri Pi Documentation](https://www.raspberrypi.org/documentation/)

### Sense HAT
* [Sense HAT](https://www.raspberrypi.org/products/sense-hat/)
* [Sense HAT Documentation](http://pythonhosted.org/sense-hat/)
* [Sense HAT API](http://pythonhosted.org/sense-hat/api/)
* [Sense HAT Emuulator Documentation](https://sense-emu.readthedocs.io/en/v1.0/)
* [Installing the Sense HAT Emulator](https://sense-emu.readthedocs.io/en/v1.0/install.html)

### VirtualBox
* [VirtualBox](https://www.virtualbox.org/)
* [VirtualBox User Manual](https://www.virtualbox.org/manual/UserManual.html)

### Linux
* [Raspbian](https://www.raspberrypi.org/downloads/)
* [Linux Mint](https://linuxmint.com/)
