from tkinter import *
from Eyes.eyes import *
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

    mouth = Mouth(face)
    eyes = Eyes(face)
    text_area.display('ip', host.ip)

    mouth.small()
    wheels.setSpeed(50)
    ip_event = TimeEvent(60)
    test_event = TimeEvent(1)
    test_event.hold()


    blink_eyes = TimeEvent(7)

    while TRUE:
        k = face.key()
        if k != "":
            print("Keypressed is ", k)
            if k == 'Up':
                wheels.advanceCar()
            elif k == 'Left':
                wheels.turnLeft()
            elif k == 'Right':
                wheels.turnRight()
            elif k == 'Down':
                wheels.reverseCar()
            elif k == 'Q':
                wheels.turnOffMotors()
                break
        
        if ip_event.interval():
            text_area.remove('ip')

        if blink_eyes.interval():
            eyes.blink_eyes()


    face.win.getMouse()
    face.win.close()


main()


atexit
atexit.register(wheels.turnOffMotors)
