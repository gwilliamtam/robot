import picamera
from Eyes.graphics import *

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        
    def shoot_and_show(self, car, filename = 'shoot_and_show.gif'):
        self.camera.resolution = (500, 500)
        self.camera.capture(filename)
        foto = Image(Point(512,300), filename)
        foto.draw(car.face.win)
        
    def shoot_and_eyes(self, car, filename = 'shoot_and_eyes.gif'):
        size = car.eyes.left_eye.iris_radius * 2
        self.camera.resolution = (size, size)
        self.camera.capture(filename)
        foto_left_eye = Image(car.eyes.left_eye.center, filename)
        foto_right_eye = Image(car.eyes.right_eye.center, filename)
        foto_left_eye.draw(car.face.win)
        foto_right_eye.draw(car.face.win)
                
