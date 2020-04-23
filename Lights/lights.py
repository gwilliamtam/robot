import RPi.GPIO as GPIO
from tkinter import TRUE
from tkinter import FALSE
import time


class Light:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin
        self.type = GPIO.OUT
        self.lights_on = FALSE
        GPIO.setup(self.pin, self.type)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.lights_on = TRUE
            
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.lights_on = FALSE


class Lights:
    def __init__(self):
        self.front = Light(7)
