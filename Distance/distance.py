import RPi.GPIO as GPIO
import time


class Distance:
    def __init__(self):
        self.pins = {
            "0": {
                "trigger": 8,
                "echo": 10,
                "distance": 0
            },
            "1": {
                "trigger": 11,
                "echo": 13,
                "distance": 0
            },
            "2": {
                "trigger": 15,
                "echo": 18,
                "distance": 0
            }
        }
        # self.trigger_pin = 8
        # self.echo_pin = 10
        # self.trigger_pin2 = 11
        # self.echo_pin2 = 13
        # self.trigger_pin3 = 15
        # self.echo_pin3 = 18
        GPIO.setmode(GPIO.BOARD)
        for key in self.pins:
            GPIO.setup(self.pins[key]['trigger'], GPIO.OUT)
            GPIO.setup(self.pins[key]['echo'] , GPIO.IN)

    def get(self):
        distance = 10000
        for key in self.pins:
            # set Trigger to HIGH
            GPIO.output(self.pins[key]['trigger'], True)

            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.pins[key]['trigger'], False)

            start_time = time.time()
            stop_time = time.time()

            # save StartTime
            while GPIO.input(self.pins[key]['echo']) == 0:
                start_time = time.time()

            # save time of arrival
            while GPIO.input(self.pins[key]['echo']) == 1:
                stop_time = time.time()

            # time difference between start and arrival
            time_elapsed = stop_time - start_time
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            self.pins[key]['distance'] = (time_elapsed * 34300) / 2

            if self.pins[key]['distance'] < distance:
                distance = self.pins[key]['distance']

        return distance
