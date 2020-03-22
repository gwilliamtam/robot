from MotorHat.Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import atexit


class Wheels:
    def __init__(self):
        self.mh = Raspi_MotorHAT(addr=0x6f)
        self.rightWheels = self.mh.getMotor(1)
        self.leftWheels = self.mh.getMotor(2)

    def turnOffMotors(self):
        print("EXIT: stop Car Movement!")
        mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
        mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)

    def setSpeed(self, value):
        print("Set Speed to " + str(value))
        self.rightWheels.setSpeed(value)
        self.leftWheels.setSpeed(value)

    def advanceCar(self):
        print("Advance")
        self.rightWheels.run(Raspi_MotorHAT.FORWARD)
        self.leftWheels.run(Raspi_MotorHAT.FORWARD)

    def reverseCar(self):
        print("Reverse")
        self.rightWheels.run(Raspi_MotorHAT.BACKWARD)
        self.leftWheels.run(Raspi_MotorHAT.BACKWARD)

    def stopCar(self):
        print("Stop")
        self.rightWheels.run(Raspi_MotorHAT.RELEASE)
        self.leftWheels.run(Raspi_MotorHAT.RELEASE)

    def turnLeft(self):
        print("Left")
        self.rightWheels.run(Raspi_MotorHAT.FORWARD)
        self.leftWheels.run(Raspi_MotorHAT.BACKWARD)

    def turnRight(self):
        print("Right")
        self.rightWheels.run(Raspi_MotorHAT.BACKWARD)
        self.leftWheels.run(Raspi_MotorHAT.FORWARD)
