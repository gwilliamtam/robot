from tkinter import *
from Eyes.eyes import *
from datetime import datetime
import socket
import random
import math


def main():
    face = Face()
    host = Host()
    text_area = TextScreen(face)

    mouth = Mouth(face)
    eyes = Eyes(face)
    text_area.display('ip', host.ip)

    mouth.small()

    ip_event = TimeEvent(60)
    test_event = TimeEvent(1)
    test_event.hold()

    # eyes.look_down()
    # test_event.hold()
    # eyes.roll_eyes_left()
    # test_event.hold()

    blink_eyes = TimeEvent(7)

    while TRUE:
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

    face.win.getMouse()
    face.win.close()
