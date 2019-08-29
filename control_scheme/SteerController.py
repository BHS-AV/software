'''
SteerController.py
Benjamin S. Bussell
August 21st 2019
'''

import pyfirmata

class Servo:

    def __init__(self, serial_Connection):

        self.board = pyfirmata.ArduinoNano(serial_Connection)
        self.board.servo_config(10, min_pulse=1000, max_pulse=2000, angle=90)

        self.position = 100
        self.board.digital[10].write(self.position)

    # TODO: Need to smooth the servo to prevent servo damage

    def set_Steering(self, value):

        self.position = value
        self.board.digital[10].write(self.position)


    def kill(self):
        self.position = 100
        self.board.exit();


