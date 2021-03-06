from tkinter import *
from Eyes.graphics import *
from datetime import datetime
import socket
import random
import math

class Face:
    def __init__(self):
        self.window_width = 1024
        self.window_height = 600

        self.face_width = 1024
        self.face_height = 400

        self.eye_center_to_side = 160
        self.eye_center_to_top = 120

        self.mouth_center_to_top = 300
        self.mouth_center_to_side = getint(self.face_width / 2)

        self.center = Point(self.face_width / 2, self.face_height / 2)
        self.win = GraphWin("Willybot", self.window_width, self.window_height)
        self.win.setBackground(color_rgb(0, 0, 0))

    def key(self):
        return self.win.checkKey()


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
        self.pupil_radius_normal = 80
        self.pupil_radius_big = 100
        self.pupil_radius = self.pupil_radius_normal
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
        
    def redraw_pupil(self):
        self.pupil.undraw()
        self.pupil = Circle(self.center, self.pupil_radius);
        self.pupil.setFill(color_rgb(0, 0, 0))
        self.pupil.draw(self.face.win)
        
    def big_pupil(self):
        if self.pupil_radius != self.pupil_radius_big:
            self.pupil_radius = self.pupil_radius_big
            self.redraw_pupil()
        
    def normal_pupil(self):
        if self.pupil_radius != self.pupil_radius_normal:
            self.pupil_radius = self.pupil_radius_normal
            self.redraw_pupil()

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
            
    def get_time_interval(self):
        return self.time_interval


class TextScreen:
    def __init__(self, face):
        self.content = {}
        self.face = face
        self.text_bg_gap = 10
        self.text_bg = Rectangle(Point(self.text_bg_gap, self.face.face_height + self.text_bg_gap),
                                 Point(self.face.window_width - self.text_bg_gap, self.face.window_height - self.text_bg_gap))
        self.text_bg.setFill(color_rgb(3, 30, 74))
        self.text_bg.draw(self.face.win)
        self.text_size = 16
        self.text_starts_y = self.face.face_height + self.text_bg_gap + self.text_size
        self.text_ends_y = self.face.window_height - self.text_bg_gap
        self.cnt = 0


    def display(self, message):
        self.cnt = self.cnt + 1
        key = self.cnt
        for row_key in list(self.content.keys()):
            if self.content[row_key].anchor.y > self.text_ends_y:
                self.content[row_key].undraw()
                del self.content[row_key]
            else:
                self.content[row_key].move(0, self.text_size + 10)

        self.content[key] = Text(Point(getint(self.face.window_width / 2), self.text_starts_y), str(message))
        self.content[key].setFill(color_rgb(0, 255, 0))
        self.content[key].setSize(self.text_size)
        self.content[key].draw(self.face.win)

    def remove(self, key):
        if key in self.content:
            self.content[key].undraw()
            del self.content[key]
