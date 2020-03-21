#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
  print("EXIT: stop Car Movement!")
  mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
  mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

rightWheels = mh.getMotor(1)
leftWheels = mh.getMotor(2)

def setSpeed(value):
  print("Set Speed to " + str(value))
  rightWheels.setSpeed(value)
  leftWheels.setSpeed(value)

def advanceCar(seconds):
  print("Advance for " + str(seconds) + " seconds")
  rightWheels.run(Raspi_MotorHAT.FORWARD)
  leftWheels.run(Raspi_MotorHAT.FORWARD)
  time.sleep(seconds)

def reverseCar(seconds):
  print("Reverse for " + str(seconds) + " seconds")
  rightWheels.run(Raspi_MotorHAT.BACKWARD)
  leftWheels.run(Raspi_MotorHAT.BACKWARD)
  time.sleep(seconds)

def stopCar(seconds):
  print("Stop for " + str(seconds) + " seconds")
  rightWheels.run(Raspi_MotorHAT.RELEASE)
  leftWheels.run(Raspi_MotorHAT.RELEASE)
  time.sleep(seconds)

def turnLeft(seconds):
  print("Left for " + str(seconds) + " seconds")
  rightWheels.run(Raspi_MotorHAT.FORWARD)
  leftWheels.run(Raspi_MotorHAT.BACKWARD)
  time.sleep(seconds)

def turnRight(seconds):
  print("Right for " + str(seconds) + " seconds")
  rightWheels.run(Raspi_MotorHAT.BACKWARD)
  leftWheels.run(Raspi_MotorHAT.FORWARD)
  time.sleep(seconds)

### MAIN START HERE WILLY
setSpeed(50)
advanceCar(2)
stopCar(1)
turnLeft(3)
stopCar(1)
turnRight(3)
