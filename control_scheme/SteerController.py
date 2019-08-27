'''
SteerController.py
Benjamin S. Bussell
August 21st 2019
'''

import serial

# Working to find a PWM Output devices pray its not an arduino...

class Servo:

    def __init__(self, serial_Connection):


        self.position = 0
        pass

    def build_Position_Packet(self, value):
        pass
        #return packet

    def set_Steering(self, value):

        pass

    def kill(self):
        self.position = 0



