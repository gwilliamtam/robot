import RPi.GPIO as GPIO
import time


class Lights:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin
        self.type = GPIO.OUT
        GPIO.setup(self.pin, self.type)
    
    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        
    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def clean(self):
        GPIO.cleanup()
