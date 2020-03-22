from tkinter import TRUE
from tkinter import FALSE


class KeyboardControl:
    def __init__(self, car):
        self.car = car
        self.in_loop = TRUE
        self.desplegables = ['Up', 'Down', 'Left', 'Right', 'Escape', 'Return']
        self.arms_action = ['a', 's', 'd', 'w', 'x']

    def handle(self, k = None):
        if k is None:
            k = self.car.face.key()

        if k != "":
            if k == 'Up':
                self.car.wheels.advanceCar()
                self.car.eyes.look_down()
                self.car.mouth.large()
            elif k == 'Left':
                self.car.wheels.turnLeft()
                self.car.eyes.look_left()
                self.car.mouth.medium()
            elif k == 'Right':
                self.car.wheels.turnRight()
                self.car.eyes.look_right()
                self.car.mouth.medium()
            elif k == 'Down':
                self.car.wheels.reverseCar()
                self.car.eyes.look_up()
                self.car.mouth.large()
            elif k == 'Return':
                self.car.wheels.stopCar()
                self.car.eyes.look_center()
                self.car.mouth.small()
            elif k >= '0' and k <='9':
                speed_key = int(k)
                if speed_key == 0:
                    speed_key = 10
                self.car.wheels.setSpeed(25*speed_key)
                self.car.text_area.display("Speed: " + str(speed_key))
                self.car.eyes.blink_eyes()
            elif k == 'w':
                self.car.arms.left_arm.arm_up()
                self.car.arms.right_arm.arm_up()
                self.car.eyes.look_up()
            elif k == 'a':
                self.car.arms.left_arm.arm_down()
                self.car.arms.right_arm.arm_up()
                self.car.eyes.roll_eyes_right()
            elif k == 's':
                self.car.arms.left_arm.arm_middle()
                self.car.arms.right_arm.arm_middle()
                self.car.eyes.look_center()
            elif k == 'x':
                self.car.arms.left_arm.arm_down()
                self.car.arms.right_arm.arm_down()
                self.car.eyes.look_down()
            elif k == 'd':
                self.car.arms.left_arm.arm_up()
                self.car.arms.right_arm.arm_down()
                self.car.eyes.roll_eyes_left()
            elif k == 'Escape':
                self.car.wheels.stopCar()
                self.in_loop = FALSE
                return self.in_loop
            if k in self.desplegables:
                self.car.text_area.display("Keypressed: " + k)
            if k in self.arms_action:
                self.car.text_area.display("Arms action")