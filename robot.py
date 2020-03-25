from tkinter import *
from Eyes.eyes import *
from Car.car import *
from Lights.lights import *
from Buzzer.buzzer import *
from KeyboardControl.keyboard_control import *
from MotorHat.Raspi_PWM_Servo_Driver import PWM
from MotorHat.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Arms.arms import *
from Wheels.wheels import *
from datetime import datetime
import socket
import random
import math
import atexit


def main():
    wheels = Wheels()
    face = Face()
    host = Host()
    arms = Arms()
    text_area = TextScreen(face)
    buzzer = Buzz()

    mouth = Mouth(face)
    eyes = Eyes(face)
    lights = Lights()

    mouth.small()
    wheels.setSpeed(150)
    ip_event = TimeEvent(60)
    test_event = TimeEvent(1)
    test_event.hold()

    blink_eyes = TimeEvent(7)
    macro_event = TimeEvent(5)

    car = Car(face, eyes, mouth, wheels, arms, text_area, lights, buzzer)
    key_control = KeyboardControl(car)
    
    in_loop = TRUE
    car.lights.front.turn_on()
    while in_loop:
        in_loop = key_control.handle()

        if blink_eyes.interval():
            car.eyes.blink_eyes()

    car.lights.front.turn_off()
    car.lights.clean()
     
     
main()

