from tkinter import TRUE
from tkinter import FALSE
from Eyes.eyes import TimeEvent
from Obstacles.obstacles import *

class KeyboardControl:
    def __init__(self, car):
        self.command = '';
        self.car = car
        self.in_loop = TRUE
        self.keys_dict = {
            ':': 'Enter your command and hit Enter',
            'D': 'Danger Willy Williamson!',
            'l': 'Lights',
            'Up': 'Advance',
            'Down': 'Reverse',
            'Left': 'Rotate left',
            'Right': 'Rotate right',
            'Return': 'Stop',
            'space': 'Horn',
            'w': 'Arms up',
            's': 'Arms middle',
            'x': 'Arms down',
            'a': 'Left down, right up',
            'd': 'Right down, left up',
            'f': 'Camera Front',
            'less': 'Camera Right',
            'greater': 'Camera Left',
            't': 'Take foto',
            '1': 'Speed 1',
            '2': 'Speed 2',
            '3': 'Speed 3',
            '4': 'Speed 4',
            '5': 'Speed 5',
            '6': 'Speed 6',
            '7': 'Speed 7',
            '8': 'Speed 8',
            '9': 'Speed 9',
            '0': 'Speed 10',
            'm': 'Record macros (start/end)',
            'n': 'Erase macros',
            'r': 'Run macros',
            'Escape': 'Terminate',
            'h': 'Help'
            }
        self.macros_length = {
            '1': 0.25,
            '2': 0.5,
            '3': 0.75,
            '4': 1,
            '5': 1.5,
            '6': 2,
            '7': 3,
            '8': 4,
            '9': 5,
            '0': 10
            }
        self.macro_length = 0.25
        self.my_time = TimeEvent(0.25)
        self.macros = []
        self.obstacles = Obstacles()
        
        
    def run_macros(self):
        self.my_time = TimeEvent(self.macro_length)
        for macro in self.macros:
            self.handle(macro)
            self.obstacles.check_move_forward(self.car.wheels, self.car.text_area, self.car.buzzer)
            # prevent run macro for set speed
            if macro < '0' or macro > '9':
                self.my_time.hold()

    def handle(self, k = ''):
        if k == '':
            k = self.car.face.key()
        if k != '':
            print(k)
            #self.car.text_area.display(k)
        if k in self.keys_dict:
            self.car.text_area.display(self.keys_dict[k])
            self.car.buzzer.play('click')
            if k == ':':
                self.command = ":"
                self.car.text_area.display(self.keys_dict[k])
            elif k == 'l':
                if self.car.lights.front.lights_on == TRUE:
                    self.car.lights.front.turn_off()
                else:
                    self.car.lights.front.turn_on()
            elif k == 'D':
                self.danger()
            elif k == 'Up':
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
            elif k == 'space':
                #self.car.buzzer.play('horn')
                self.car.buzzer.random()
            elif k >= '0' and k <='9':
                speed_key = int(k)
                if speed_key == 0:
                    speed_key = 10
                self.car.wheels.setSpeed(25*speed_key)
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
            elif k == 'f':
                self.car.arms.camera_arm.arm_middle()
            elif k == 'less':
                self.car.arms.camera_arm.arm_up()
            elif k == 'greater':
                self.car.arms.camera_arm.arm_down()
            elif k == 't':
                self.car.camera.shoot()
                #self.car.camera.show_foto(self.car.face)
            elif k == 'Escape':
                self.car.wheels.stopCar()
                self.in_loop = FALSE
                return self.in_loop
            elif k == 'm':
                self.record_macros()
            elif k == 'n':
                self.erase_macros()
            elif k == 'r':
                self.run_macros()
            elif k == 'h':
                message = ''
                cnt = 0
                for key in self.keys_dict:
                    cnt = cnt + 1
                    message = message + key + '=' + self.keys_dict[key] + ' '
                    if cnt >= 5:
                        self.car.text_area.display(message)
                        cnt = 0
                        message = ''
                if cnt > 0:
                    self.car.text_area.display(message)
                
        return self.in_loop
    
    def danger(self):
        self.erase_macros()
        self.macro_length = 0.1
        
        self.macros.append('0')
        message = "Danger! Danger! Danger!"
        for x in range(0,5):
            self.macros.append('Left')
            self.macros.append('l')
            self.macros.append('w')
            self.macros.append('l')
            self.macros.append('a')
            self.macros.append('l')
            self.macros.append('x')
            self.macros.append('l')
            self.macros.append('Right')
            self.macros.append('l')
            self.macros.append('a')
            self.macros.append('l')
            self.macros.append('s')
            self.macros.append('l')
            self.macros.append('d')
        
        self.macros.append('Return')
        
        self.run_macros()
        self.car.text_area.display(message)
        self.erase_macros()
    
    def record_macros(self):
        recording = TRUE
        self.car.text_area.display("'Set Speed' macros are not affected by macro length duration")
        message = ''
        for key in self.macros_length:
            message = message + key + '=' + str(self.macros_length[key]) + '  '
        self.car.text_area.display(message + ' (seconds)')
        self.my_time = TimeEvent(self.macro_length)
        self.car.text_area.display("Set macro length:")
        
        self.macro_length = 0
        while self.macro_length == 0:
            k = self.car.face.key()
            if k >= '0' and k <= '9':
                self.macro_length = self.macros_length[k]
        self.car.text_area.display("Macro length set to "
            + str(self.macro_length) + " seconds")
        
        while recording == TRUE:
            k = self.car.face.key()
            if k == 'Escape':
                k = ''
            if k == 'D':
                k = ''
            if k != '':
                self.car.text_area.display(k)
            if k in self.keys_dict:
                if k == 'm':
                    recording = FALSE
                else:
                    self.macros.append(k)
                    self.car.text_area.display("+" + self.keys_dict[k])
        self.car.text_area.display(str(len(self.macros)) + " macros stored")
                    
    def erase_macros(self):
        self.macros = []
        self.car.text_area.display("Macros erased")
        