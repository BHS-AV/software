'''

Motor.py
Benjamin S. Bussell
August 21st 2019

'''

from threading import Thread

import pyvesc
import time


# This allows the run function to quietly run in the background.
def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


class Motor:

    def __init__(self, serial_connection):
        """

        :type serial_connection: Serial Object
        """
        self.FSESC = serial_connection

        self.current = 0

        self.active = True
        self.delta = 1

        self.current_time = time.time()
        self.previous_time = time.time()

        pass

    def __del__(self):
        self.active = False
        pass

    @threaded
    def run(self):
        while self.active:

            self.current_time = time.time()
            if self.current_time != self.previous_time:
                print("Current: ", self.current)
                self.FSESC.write(self.current_packet(self.current))
                self.FSESC.flush()
                self.previous_time = time.time()

    def set_current(self, value):
        self.current = value
        pass

    @staticmethod
    def current_packet(value) -> bytes:

        message = pyvesc.SetCurrent(value)
        packet = pyvesc.encode(message)
        return packet
