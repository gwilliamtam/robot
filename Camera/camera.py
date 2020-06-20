import picamera
from Eyes.graphics import *

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.foto = ''
        self.set_directory()
        
    def set_directory(self):
        self.directory = '/' + 'home' + '/' + 'pi' + '/' + 'Willy' + '/' + 'robot' + '/' + 'Camera' + '/' + 'fotos' + '/'
        
    def shoot(self, filename = 'shoot_and_show.gif'):
        self.camera.resolution = (1024, 1024)
        self.camera.rotation = 180
        self.camera.capture(self.directory + filename)
        self.foto = Image(Point(512,300), self.directory + filename)
        
    def show_foto(self, face):
        self.foto.draw(face.win)
        
    #def shoot_and_eyes(self, car, filename = 'shoot_and_eyes.gif'):
    #    size = car.eyes.left_eye.iris_radius * 2
    #    self.camera.resolution = (size, size)
    #    self.camera.capture(filename)
    #    foto_left_eye = Image(car.eyes.left_eye.center, filename)
    #    foto_right_eye = Image(car.eyes.right_eye.center, filename)
    #    foto_left_eye.draw(car.face.win)
    #    foto_right_eye.draw(car.face.win)
                
