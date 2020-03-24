import RPi.GPIO as GPIO
from time import sleep

pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 100)

def Blink():
    #for x in range(0,4):
    GPIO.output(pin, True)
    p.start(100)
    sleep(1)
    p.ChangeDutyCycle(45)
    p.ChangeFrequency(2000)
    sleep(3)
    p.stop()
    GPIO.cleanup()
    
Blink()