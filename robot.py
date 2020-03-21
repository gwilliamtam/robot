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
    #text_area.display('ip', host.ip)

    mouth.small()
    wheels.setSpeed(150)
    ip_event = TimeEvent(60)
    test_event = TimeEvent(1)
    test_event.hold()


    blink_eyes = TimeEvent(7)

    in_loop = TRUE
    while in_loop:
        k = face.key()
        if k != "":
            if k == 'Up':
                wheels.advanceCar()
                eyes.look_down()
            elif k == 'Left':
                wheels.turnLeft()
                eyes.look_left()
            elif k == 'Right':
                wheels.turnRight()
                eyes.look_right()
            elif k == 'Down':
                wheels.reverseCar()
                eyes.look_up()
            elif k == 'Return':
                wheels.stopCar()
                eyes.look_center()
            elif k >= '0' and k <='9':
                speed_key = int(k)
                if speed_key == 0:
                    speed_key = 10
                wheels.setSpeed(25*speed_key)
            elif k == 'w':
                arms.left_arm.arm_up()
                arms.right_arm.arm_up()
            elif k == 'a':
                arms.left_arm.arm_down()
                arms.right_arm.arm_up()
            elif k == 's':
                arms.left_arm.arm_middle()
                arms.right_arm.arm_middle()
            elif k == 'x':
                arms.left_arm.arm_down()
                arms.right_arm.arm_down()
            elif k == 'd':
                arms.left_arm.arm_up()
                arms.right_arm.arm_down()
            elif k == 'Escape':
                wheels.stopCar()
                in_loop = FALSE
                break
        
        #if ip_event.interval():
            #text_area.remove('ip')

        if blink_eyes.interval():
            eyes.blink_eyes()
main()

