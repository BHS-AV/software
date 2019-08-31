'''
Servo.py
Benjamin S. Bussell
August 21st 2019
'''


import serial

class Servo:

    def __init__(self, serial_Connection):


        self.position = 90
        #self.board.digital[10].write(self.position)


    def set_Steering(self, value):

        self.position = value
        print(self.position)
        print("Actual: ",self.board.digital[10].read())


    def kill(self):
        self.position = 90


