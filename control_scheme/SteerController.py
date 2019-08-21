'''
SteerController.py
Benjamin S. Bussell
August 21st 2019
'''


import pyvesc
import serial

class SERVO:

    def __init__(self, serialConnection):

        self.FSESC = serialConnection

        self.position = 0
        pass



    def buildPositionPacket(self, value):

        message = pyvesc.SetPosition(value)
        packet = pyvesc.encode(message)
        return packet

    def set_Steering(self, value):

        self.position = value
        self.FSESC.write(self.buildPositionPacket(self.position))
        pass

def main():
    servo = SERVO(serial.Serial('/dev/tty.usbmodem3011',115200,timeout = 0.1))
    servo.set_Steering(10)
