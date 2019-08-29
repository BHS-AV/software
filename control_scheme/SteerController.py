'''
SteerController.py
Benjamin S. Bussell
August 21st 2019
'''


import serial
import pyfirmata
from threading import Thread

# Working to find a PWM Output devices pray its not an arduino...



class Servo:

    def __init__(self, serial_Connection):


        self.board = pyfirmata.ArduinoNano(serial_Connection)
        self.board.servo_config(10,  90)



        self.position = 90
        self.board.digital[10].write(self.position)





    def build_Position_Packet(self, value):
        pass
        #return packet

    def set_Steering(self, value):


        self.position = value
        self.board.digital[10].write(self.position)
        pass

    def kill(self):
        self.position = 90



