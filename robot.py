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

def MyGui():
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
        if keyboard.is_pressed('q'):
            print("Keypressed is q ")
        
        if ip_event.interval():
            text_area.remove('ip')

        if blink_eyes.interval():
            eyes.blink_eyes()

        if test_event.interval():
            option = random.randrange(15)
            if option == 1:
                eyes.roll_eyes_left()
            if option == 2:
                eyes.look_left()
            if option == 3:
                eyes.look_right()
            if option == 4:
                eyes.look_center()
            if option == 4:
                eyes.look_up()
            if option == 6:
                eyes.look_down()

            option = random.randrange(6)
            if option == 1:
                mouth.large()
            if option == 2:
                mouth.small()
            if option == 3:
                mouth.medium()

            option = random.randrange(10)
            if option == 1:
                arms.right_arm.arm_up()
                arms.left_arm.arm_up()
            if option == 2:
                arms.right_arm.arm_down()
                arms.left_arm.arm_down()
            if option == 3:
                arms.right_arm.arm_up()
                arms.left_arm.arm_down()
            if option == 4:
                arms.right_arm.arm_down()
                arms.left_arm.arm_up()
            if option == 5:
                arms.right_arm.arm_middle()
                arms.left_arm.arm_middle()
                
            option = random.randrange(10)
            if option == 1:    
                wheels.advanceCar()
                time.sleep(1)
                wheels.stopCar()
            if option == 2:
                wheels.turnLeft()
                time.sleep(1)
                wheels.stopCar()
            if option == 3:
                wheels.turnRight()
                time.sleep(1)
                wheels.stopCar()
            if option == 4:
                wheels.reverseCar()
                time.sleep(1)
                wheels.stopCar()

    face.win.getMouse()
    face.win.close()

    atexit
    atexit.register(wheels.turnOffMotors)


root = Tk()

def key(event):
    print("pressed", repr(event.char))
    
def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)
    
frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

my_gui = MyGui(root)
root.mainloop()
