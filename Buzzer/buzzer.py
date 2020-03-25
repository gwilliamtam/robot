import RPi.GPIO as GPIO
from time import sleep

pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 100)

def Blink():
    #for x in range(0,4):
    GPIO.output(pin, True)
    p.start(0)
    p.ChangeFrequency(400)
    p.ChangeDutyCycle(90)
    sleep(0.1)
    p.stop()
    GPIO.cleanup()
    
Blink()