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

        self.current_Goal = 0
        self.current = 0

        self.duty_Cycle_Goal = 0
        self.duty_Cycle = 0

        self.brake = 0
        self.brake_Goal = 0

        self.active = True
        self.delta = 1

        self.current_Time = time.time()
        self.previous_Time = time.time()

        pass

    def kill(self):
        self.active = False
        pass

    @threaded
    def run(self):
        while self.active:

            self.current_Time = time.time()
            if (self.previous_Time != self.current_Time):

                duty_Cycle_Error = self.duty_Cycle_Goal-self.duty_Cycle
                current_Error = self.current_Goal - self.current
                brake_Error = self.brake_Goal - self.brake

                duty_Cycle_Sign = abs(duty_Cycle_Error) / duty_Cycle_Error
                current_Sign = abs(current_Error) / current_Error
                brake_Sign = abs(brake_Error) / brake_Error


                # Only one value is applied at a time to avoid damaging motor
                if (self.brake != 0):

                    if (abs(brake_Error) > self.delta):
                        self.brake += self.delta * brake_Sign
                    else:
                        self.brake = self.brake_Goal

                    print("Brake: ", self.brake)
                    self.FSESC.write(self.brake_Packet(self.brake))
                elif (self.current != 0):

                    if (abs(current_Error) > self.delta):
                        self.current += self.delta * current_Sign
                    else:
                        self.current = self.current_Goal

                    print("Current: ", self.current)
                    self.FSESC.write(self.current_Packet(self.current))
                elif (self.duty_Cycle != 0):

                    if (abs(duty_Cycle_Error) > self.delta):
                        self.duty_Cycle += self.delta * duty_Cycle_Sign
                    else:
                        self.duty_Cycle = self.duty_Cycle_Goal

                    print("Duty Cycle: ", self.duty_Cycle)
                    self.FSESC.write(self.duty_Cycle_Packet(self.duty_Cycle))
                self.FSESC.flush()

                self.previous_Time = time.time()

    def set_Current(self, value):
        self.current_Goal = value
        pass

    def set_Duty_Handle(self, value):
        self.duty_Cycle_Goal = value
        pass

    def set_Brake(self, value):
        self.brake_Goal = value
        pass

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




