from MotorHat.Raspi_PWM_Servo_Driver import PWM
import time


class Arms:
    def __init__(self):
        self.right_arm = Arm(0, 0)
        self.left_arm = Arm(1, 1)
        self.camera_arm = Arm(14, 0)

class Arm:
    def __init__(self, id, inverted):
        self.inverted = inverted
        self.arm_id = id
        self.pwm = PWM(0x6F)
        if inverted:
            self.servoMin = 150  # Min pulse length out of 4096
            self.servoMax = 600  # Max pulse length out of 4096
        else:
            self.servoMin = 600  # Min pulse length out of 4096
            self.servoMax = 150  # Max pulse length out of 4096
        self.pwm.setPWMFreq(60)
    
    def setServoPulse(self, channel, pulse):
        pulseLength = 1000000                   # 1,000,000 us per second
        pulseLength /= 60                       # 60 Hz
        #print ("%d us per period" % pulseLength)
        pulseLength /= 4096                     # 12 bits of resolution
        #print ("%d us per bit" % pulseLength)
        pulse *= 1000
        pulse /= pulseLength
        pwm.setPWM(channel, 0, pulse)
    
  
    def arm_up(self):
        self.pwm.setPWM(self.arm_id, 0, self.servoMin)
        print("Arm Up")
  
    def arm_down(self):
        self.pwm.setPWM(self.arm_id, 0, self.servoMax)
        print("Arm Down")
    
    def arm_middle(self):
        middleInterval = int((self.servoMax + self.servoMin)/2)
        self.pwm.setPWM(self.arm_id, 0, middleInterval)
        print("Arm Middle")

