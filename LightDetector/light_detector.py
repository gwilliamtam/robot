from tkinter import TRUE
from tkinter import FALSE
import RPi.GPIO as GPIO
from time import sleep


class LightDetector:
    def __init__(self):
        self.pin = 16
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin , GPIO.IN)
        
    def status(self):
        # return 0 or 1 if light is present
        if GPIO.input(self.pin) == 1:
            return TRUE
        else:
            return FALSE
