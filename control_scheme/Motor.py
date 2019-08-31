'''
Motor.py
Benjamin S. Bussell
August 21st 2019
'''

from threading import Thread

import pyvesc
import time
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

        self.FSESC = serial.Serial(serial_Connection, 115200, timeout=0.1)

        self.current = 0


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

                print("Current: ", self.current)
                self.FSESC.write(self.current_Packet(self.current))

                self.FSESC.flush()

                self.previous_Time = time.time()

    def set_Current(self, value):
        self.current = value
        pass

    def current_Packet(self, value) -> bytes:

        message = pyvesc.SetCurrent(value)
        packet = pyvesc.encode(message)
        return packet

