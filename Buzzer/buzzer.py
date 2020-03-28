import RPi.GPIO as GPIO
from time import sleep
import random


class Buzz:
    def __init__(self, frequency = 400, cycle = 90, sleep = 0.1):
        self.frequency = frequency
        self.cycle = cycle
        self.sleep = sleep


class Buzzer:
    def __init__(self):
        self.pin = 12
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, 100)
        GPIO.output(self.pin, True)
        self.sounds = {
            "click": Buzz(400, 90, 0.05),
            "horn": Buzz(800, 50, 0.1),
            "error": Buzz(200, 90, 1)
        }


    def play(self, sound):
        self.p.start(0)
        self.p.ChangeFrequency(self.sounds[sound].frequency)
        self.p.ChangeDutyCycle(self.sounds[sound].cycle)
        sleep(self.sounds[sound].sleep)
        self.p.stop()
        
    def random(self):
        for x in range(0,30):
            self.random1()

    def random1(self):
        self.p.start(0)
        self.p.ChangeFrequency(random.randrange(100,1200))
        self.p.ChangeDutyCycle(random.randrange(10,90))
        #sleep(random.randrange(1,10) * 0.1)
        sleep(0.05)
        self.p.stop()
