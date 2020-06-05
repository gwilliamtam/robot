import RPi.GPIO as GPIO
import time


class Distance:
    def __init__(self):
        self.trigger_pin = 8
        self.echo_pin = 10
        # self.trigger_pin2 = 11
        # self.echo_pin2 = 13
        # self.trigger_pin3 = 15
        # self.echo_pin3 = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin , GPIO.IN)

    def get(self):
        # set Trigger to HIGH
        GPIO.output(self.trigger_pin, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        # save StartTime
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        # save time of arrival
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        # time difference between start and arrival
        time_elapsed = stop_time - start_time
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (time_elapsed * 34300) / 2

        return distance
