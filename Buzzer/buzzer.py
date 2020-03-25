import RPi.GPIO as GPIO
from time import sleep


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
        p = GPIO.PWM(self.pin, 100)
        self.sounds = {
            "click": Buzz(400, 90, 0.1)
        }


    def play(self, sound):
        #for x in range(0,4):
        GPIO.output(self.pin, True)
        self.p.start(0)
        self.p.ChangeFrequency(self.sounds[sound].frequency)
        self.p.ChangeDutyCycle(self.sounds[sound].cycle)
        sleep(self.sounds[sound].sleep)
        self.p.stop()
        GPIO.cleanup()