'''
SpeedController.py
Benjamin S. Bussell
August 21st 2019
'''

# TODO: DONT LET THIS IMPORT SURVIVE TESTING
import time
from threading import Thread

import pyvesc
import serial


# This allows the run function to quietly run in the background.
def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


class Motor:

    def __init__(self, serial_Connection):

        self.FSESC = serial_Connection

        self.current = 0
        self.duty_Cycle = 0
        self.brake = 0

        self.active = True

        self.current_Time = time.time()
        self.previous_Time = time.time()

        pass

    @threaded
    def run(self):
        while self.active:

            self.current_Time = time.time()
            if (self.previous_Time != self.current_Time):

                # Only one value is applied at a time to avoid damaging motor
                if (self.brake != 0):
                    print("Brake: ", self.brake)
                    self.FSESC.write(self.brake_Packet(self.brake))
                elif (self.current != 0):
                    print("Current: ", self.current)
                    self.FSESC.write(self.current_Packet(self.current))
                elif (self.duty_Cycle != 0):
                    print("Duty Cycle: ", self.duty_Cycle)
                    self.FSESC.write(self.duty_Cycle_Packet(self.duty_Cycle))
                self.FSESC.flush()

                self.previous_Time = time.time()

    def duty_Cycle_Packet(self, value) -> bytes:

        message = pyvesc.SetDutyCycle(value)
        packet = pyvesc.encode(message)
        return packet

    def current_Packet(self, value) -> bytes:

        message = pyvesc.SetCurrent(value)
        packet = pyvesc.encode(message)
        return packet

    def brake_Packet(self, value) -> bytes:

        message = pyvesc.SetCurrentBrake(value)
        packet = pyvesc.encode(message)
        return packet

    def set_Current(self, value):
        self.current = value
        pass

    def set_Duty_Handle(self, value):
        self.duty_Cycle = value
        pass

    def kill(self):
        self.active = False
        pass


