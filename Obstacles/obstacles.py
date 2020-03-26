from Distance.distance import *

class Obstacles:
    def __init__(self):
        self.distance = Distance()
        self.front_min_distance = 15 #cm
        
    def check_move_forward(self, wheels, text_area, buzzer):
        if wheels.status == 'forward' and self.distance.get() < self.front_min_distance:
            wheels.stopCar()
            text_area.display('Obstacle')
            buzzer.play('error')