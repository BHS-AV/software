'''
SteerController.py
Benjamin S. Bussell
August 21st 2019
'''

import pyvesc
import serial


class Servo:

    def __init__(self, serial_Connection):
        self.FSESC = serial_Connection

        self.position = 0
        pass

    def build_Position_Packet(self, value):
        message = pyvesc.SetPosition(value)
        packet = pyvesc.encode(message)
        return packet

    def set_Steering(self, value):
        self.position = value
        self.FSESC.write(self.build_Position_Packet(self.position))
        pass

    def kill(self):
        self.position = 0
        self.FSESC.write(self.build_Position_Packet(self.position))


