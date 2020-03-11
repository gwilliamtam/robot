from tkinter import *
from Eyes.graphics import *
from datetime import datetime
import socket
import random
import math


class Face:
    def __init__(self):
        self.window_width = 600
        self.window_height = 1024

        self.face_width = 600
        self.face_height = 600

        self.eye_center_to_side = 160
        self.eye_center_to_top = 120

        self.mouth_center_to_top = 350
        self.mouth_center_to_side = getint(self.face_width / 2)

        self.center = Point(self.face_width / 2, self.face_height / 2)
        self.win = GraphWin("Bouncing Ball", self.window_width, self.window_height)
        self. win.setBackground(color_rgb(0, 0, 0))


class Host:
    def __init__(self):
        self.name = socket.gethostname()
        self.ip = socket.gethostbyname(self.name)


class Eyes:
    def __init__(self, face):
        self.face = face
        self.look_dir = 'center'
        self.are_eyes_open = TRUE
        self.left_eye = Eye(self.face, Point(self.face.eye_center_to_side, self.face.eye_center_to_top))
        self.right_eye = Eye(self.face,
                             Point(self.face.face_width - self.face.eye_center_to_side, self.face.eye_center_to_top))
        self.left_eye.show()
        self.right_eye.show()

    def look_left(self):
        if self.look_dir == "center":
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_left()
        if self.look_dir == "down":
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_left()
            self.left_eye.move_pupil_up()
            self.right_eye.move_pupil_up()
        if self.look_dir == "up":
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_left()
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_down()
        if self.look_dir == "right":
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_left()
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_left()
        self.look_dir = "left"
        print("Look left")

    def look_right(self):
        if self.look_dir == "center":
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_right()
        if self.look_dir == "down":
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_right()
            self.left_eye.move_pupil_up()
            self.right_eye.move_pupil_up()
        if self.look_dir == "up":
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_right()
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_down()
        if self.look_dir == "left":
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_right()
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_right()
        self.look_dir = "right"
        print("Look right")

    def look_down(self):
        if self.look_dir == "center":
            self.right_eye.move_pupil_down()
            self.left_eye.move_pupil_down()
        if self.look_dir == "up":
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_down()
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_down()
        if self.look_dir == "left":
            self.right_eye.move_pupil_down()
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_right()
            self.left_eye.move_pupil_right()
        if self.look_dir == "right":
            self.right_eye.move_pupil_down()
            self.left_eye.move_pupil_down()
            self.right_eye.move_pupil_left()
            self.left_eye.move_pupil_left()
        self.look_dir = "down"
        print("Look down")

    def look_up(self):
        if self.look_dir == "center":
            self.left_eye.move_pupil_up()
            self.right_eye.move_pupil_up()
        if self.look_dir == "down":
            self.left_eye.move_pupil_up()
            self.right_eye.move_pupil_up()
            self.left_eye.move_pupil_up()
            self.right_eye.move_pupil_up()
        if self.look_dir == "left":
            self.right_eye.move_pupil_right()
            self.left_eye.move_pupil_right()
            self.right_eye.move_pupil_up()
            self.left_eye.move_pupil_up()
        if self.look_dir == "right":
            self.right_eye.move_pupil_left()
            self.left_eye.move_pupil_left()
            self.right_eye.move_pupil_up()
            self.left_eye.move_pupil_up()
        self.look_dir = "up"
        print("Look up")

    def look_center(self):
        self.left_eye.move_pupil_center()
        self.right_eye.move_pupil_center()
        self.look_dir = "center"
        print("Look center")

    def close_eyes(self):
        self.right_eye.eye_lid_down(1)
        self.left_eye.eye_lid_down(1)
        self.right_eye.eye_lid_down(1)
        self.left_eye.eye_lid_down(1)
        self.right_eye.eye_lid_down(1)
        self.left_eye.eye_lid_down(1)
        self.right_eye.eye_lid_down(1)
        self.left_eye.eye_lid_down(1)
        self.are_eyes_open = FALSE
        print("Close eyes")

    def open_eyes(self):
        self.right_eye.eye_lid_up(1)
        self.left_eye.eye_lid_up(1)
        self.right_eye.eye_lid_up(1)
        self.left_eye.eye_lid_up(1)
        self.right_eye.eye_lid_up(1)
        self.left_eye.eye_lid_up(1)
        self.right_eye.eye_lid_up(1)
        self.left_eye.eye_lid_up(1)
        self.are_eyes_open = TRUE
        print("Open eyes")

    def blink_eyes(self):
        blink = TimeEvent(0.2)
        self.close_eyes()
        blink.hold()
        self.open_eyes()

    def roll_eyes_left(self):
        roll = TimeEvent(0.1)
        self.look_left()
        roll.hold()
        self.look_down()
        roll.hold()
        self.look_right()
        roll.hold()
        self.look_up()
        roll.hold()
        self.look_left()

    def roll_eyes_right(self):
        roll = TimeEvent(0.1)
        self.look_right()
        roll.hold()
        self.look_down()
        roll.hold()
        self.look_left()
        roll.hold()
        self.look_up()
        roll.hold()
        self.look_right()


class Eye:
    global center

    def __init__(self, face, point):
        self.face = face
        self.iris_radius = 120
        self.pupil_radius = 80
        self.center = point

        self.iris = Circle(point, self.iris_radius)
        self.iris.setFill(color_rgb(255, 255, 255))

        self.pupil = Circle(point, self.pupil_radius)
        self.pupil.setFill(color_rgb(0, 0, 0))

        self.lid = Circle(Point(point.x, point.y - self.iris_radius * 2), self.iris_radius)
        self.lid.setFill(color_rgb(0, 0, 0))

    def show(self):
        self.iris.draw(self.face.win)
        self.pupil.draw(self.face.win)
        self.lid.draw(self.face.win)

    def move_pupil_left(self):
        dx = self.iris_radius - self.pupil_radius
        self.pupil.move(dx, 0)

    def move_pupil_right(self):
        dx = self.iris_radius - self.pupil_radius
        self.pupil.move(-dx, 0)

    def move_pupil_down(self):
        dy = self.iris_radius - self.pupil_radius
        self.pupil.move(0, dy)

    def move_pupil_up(self):
        dy = self.iris_radius - self.pupil_radius
        self.pupil.move(0, -dy)

    def move_pupil_center(self):
        dx = self.center.x - self.pupil.getCenter().x
        dy = self.center.y - self.pupil.getCenter().y
        self.pupil.move(dx, dy)

    def eye_lid_up(self, quarter):
        dy = getint(self.iris_radius * 2) / 4
        self.lid.move(0, -dy * quarter)

    def eye_lid_down(self, quarter):
        dy = getint(self.iris_radius * 2) / 4
        self.lid.move(0, dy * quarter)


class Mouth:

    def __init__(self, face):
        self.face = face
        self.width = 300
        self.height = 150
        self.size = "medium"
        self.center = Point(self.face.mouth_center_to_side, self.face.mouth_center_to_top)
        self.mouth_p1 = Point(self.center.x - getint(self.width/2), self.center.y - getint(self.height/2))
        self.mouth_p2 = Point(self.center.x + getint(self.width/2), self.center.y + getint(self.height/2))
        self.mouth = Oval(self.mouth_p1, self.mouth_p2)
        self.mouth.setFill(color_rgb(255, 255, 255))

        self.upper_lip_p1 = Point(self.center.x - getint(self.width/2), self.center.y - self.height)
        self.upper_lip_p2 = Point(self.center.x + getint(self.width/2), self.center.y)
        self.upper_lip = Rectangle(self.upper_lip_p1, self.upper_lip_p2)
        self.upper_lip.setFill(color_rgb(0, 0, 0))

        self.mouth.draw(self.face.win)
        self.upper_lip.draw(self.face.win)

    def move_upper_lip_up(self):
        self.upper_lip.move(0, -60)

    def move_upper_lip_down(self):
        self.upper_lip.move(0, 60)

    def small(self):
        if self.size == "large":
            self.move_upper_lip_down()
            self.move_upper_lip_down()
        if self.size == "medium":
            self.move_upper_lip_down()
        self.size = "small"

    def medium(self):
        if self.size == "large":
            self.move_upper_lip_down()
        if self.size == "small":
            self.move_upper_lip_up()
        self.size = "medium"

    def large(self):
        if self.size == "medium":
            self.move_upper_lip_up()
        if self.size == "small":
            self.move_upper_lip_up()
            self.move_upper_lip_up()
        self.size = "large"


class TimeEvent:

    def __init__(self, time_interval):
        self.curr_time = self.prev_time = time.time()
        self.time_interval = time_interval  # in seconds

    def interval(self):
        self.curr_time = time.time()
        if self.curr_time - self.prev_time > self.time_interval:
            self.prev_time = self.curr_time
            return TRUE
        else:
            return FALSE

    def hold(self):
        while self.interval() == FALSE:
            nothing = TRUE


class TextScreen:
    def __init__(self, face):
        self.content = {}
        self.face = face
        self.text_bg_gap = 10
        self.text_bg = Rectangle(Point(self.text_bg_gap, self.face.face_height + self.text_bg_gap),
                                 Point(self.face.window_width - self.text_bg_gap, self.face.window_height - self.text_bg_gap))
        self.text_bg.setFill(color_rgb(3, 30, 74))
        self.text_bg.draw(self.face.win)
        self.text_size = 30
        self.text_starts_y = self.face.face_height + self.text_bg_gap + self.text_size
        self.text_ends_y = self.face.window_height - self.text_bg_gap - self.text_size
        print(str(self.text_ends_y))

    def display(self, key, message):
        for row_key in list(self.content.keys()):
            print(str(self.content[row_key]))
            if self.content[row_key].anchor.y > self.text_ends_y:
                self.content[row_key].undraw()
                del self.content[row_key]
            else:
                self.content[row_key].move(0, self.text_size)

        self.content[key] = Text(Point(getint(self.face.window_width / 2), self.text_starts_y), str(message))
        self.content[key].setFill(color_rgb(0, 255, 0))
        self.content[key].setSize(self.text_size)
        self.content[key].draw(self.face.win)

    def remove(self, key):
        if key in self.content:
            self.content[key].undraw()
            del self.content[key]


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

    cnt = 0
    while TRUE:
        if ip_event.interval():
            text_area.remove('ip')

        if blink_eyes.interval():
            eyes.blink_eyes()

        if test_event.interval():
            cnt = cnt + 1
            text_area.display(str(cnt), str(cnt))

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


main()
