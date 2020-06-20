from tkinter import *
from Eyes.eyes import *
from Car.car import *
from Lights.lights import *
from Buzzer.buzzer import *
from Distance.distance import *
from Obstacles.obstacles import *
from KeyboardControl.keyboard_control import *
from LightDetector.light_detector import *
from MotorHat.Raspi_PWM_Servo_Driver import PWM
from MotorHat.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Arms.arms import *
from Wheels.wheels import *
from Camera.camera import *
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
    distance = Distance()
    buzzer = Buzzer()
    obstacles = Obstacles()

    mouth = Mouth(face)
    eyes = Eyes(face)
    lights = Lights()
    light_detector = LightDetector()

    mouth.small()
    wheels.setSpeed(75)

    blink_eyes = TimeEvent(7)
    macro_event = TimeEvent(5)
    light_detect_event = TimeEvent(1)
    lights_event = TimeEvent(1)
    foto_event = TimeEvent(2.5)
    
    camera = Camera()

    car = Car(face, eyes, mouth, wheels, arms, text_area, lights, buzzer, camera)
    key_control = KeyboardControl(car)
    
    in_loop = TRUE
    car.lights.front.turn_on()
    lights_event.hold()
    car.lights.front.turn_off()
    
    while in_loop:
        in_loop = key_control.handle()
        obstacles.check_move_forward(wheels, text_area, buzzer)
        obstacles.check_proximity(wheels, buzzer)
        
        if light_detect_event.interval():
            if light_detector.status() == 0:
                eyes.right_eye.big_pupil()
                eyes.left_eye.big_pupil()
            else:
                eyes.right_eye.normal_pupil()
                eyes.left_eye.normal_pupil()
            
        if blink_eyes.interval():
            car.eyes.blink_eyes()

        if foto_event.interval():
            camera.shoot()

    car.lights.front.turn_off()
    GPIO.cleanup()
     
     
main()

