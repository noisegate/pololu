"""
    ==================================
    Pololu 4988 GPIO raspberry module
    ==================================

    by Noisegate (c) 2015
    aka Marcell Marosvolgyi

    Do What the Fuck You Want to Public License, WTFPL
    no, just kiddin' it is GPLv2
    
    I Think this test program has potential 4 becoming a
    simple library. Maybe one day...

    Use @ own risk. If you blow stuff, I didn't do it.

        If my code suxx and kills your hardware, I feel bad for ya,
        but I dont take responsibily. Please let me know though what
        happened, I might improve my code.


"""

import RPi.GPIO as gpio
import time

class Timeunits(object):
    ms = 0.001
    us = 0.000001

class Pins(object):
    
    def __init__(self, *args, **kwargs):
        self.enable = kwargs['enable']
        self.direction = kwargs['direction']
        self.step = kwargs['step']

class Pololu(object):

    """
        instance = Pololu(Pins(enable=<pinnr>, direction=<pinnr>, step=<pinnr>))

        instance.speed = 60# RPM

        instance.stepsleft(400)#400 left &c
    """

    def __init__(self, pins):
        gpio.setmode(gpio.BCM)
    	gpio.setup(pins.enable,gpio.OUT)
        gpio.setup(pins.direction,gpio.OUT)
        gpio.setup(pins.step,gpio.OUT)

        gpio.output(pins.direction,gpio.LOW)

        self.currentangle = 0.0
        self.rpm=60
        self.stepdelay = 60.0/self.rpm/200.0
        self.pins = pins

    @property
    def speed(self):
        return self.rpm

    @speed.setter
    def speed(self, val):
        self.rpm = val
        self.stepdelay = 60.0/self.rpm/200.0

    def enable(self):
        gpio.output(self.pins.enable, gpio.LOW)	

    def disable(self):
        gpio.output(self.pins.enable, gpio.HIGH)

    def step(self):
        gpio.output(self.pins.step, gpio.HIGH)
        time.sleep(Timeunits.us*1)
        gpio.output(self.pins.step, gpio.LOW)

    def steps(self,n):
        self.enable()
        for i in range(n):
            self.step()
            time.sleep(self.stepdelay)

        self.disable()

    def stepsleft(self, n):
        gpio.output(self.pins.direction, gpio.LOW)
        self.steps(n)

    def stepsright(self,n):
        gpio.output(self.pins.direction, gpio.HIGH)
        self.steps(n)

    def goto(self, angle):

        diff = angle-self.currentangle
        
        if (diff<0):
            gpio.output(self.pins.direction, gpio.LOW)
            diff = -diff
        else:
            gpio.output(self.pins.direction, gpio.HIGH)

        steps = int(diff/360.0 * 200)

        self.steps(steps)

        self.currentangle = angle

    def resetposition(self):
        self.currentangle = 0.0

if __name__ == "__main__":
   
    #use your own pin defs here!
    instance = Pololu(Pins(enable = 22, direction=24, step=23))
    instance.speed = 60*1

    instance.stepsleft(400)
    instance.stepsright(400)

    instance.goto(270)
    instance.goto(90)
    instance.goto(0)
    
    print "I hope stepper is where it started..."