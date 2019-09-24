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
        try:
            self.FSESC = serial_connection
        except:
            raise Exception('COULD NOT CONNECT TO FSESC')


        self.duty_cycle = 0
        self.neutral = 5000

        self.active = True
        self.delta = 1

        self.current_time = time.time()
        self.previous_time = time.time()

        print("FSESC Connected")

    def exit(self):
        self.active = False


    @threaded
    def run(self):
        while self.active:

            self.current_time = time.time()
            if self.current_time != self.previous_time:

                try:
                    print("Duty Cycle", self.duty_cycle)
                    self.FSESC.write(Motor.duty_cycle_packet(self.duty_cycle))
                    self.FSESC.flush()
                except:
                    raise Exception("COULD NOT WRITE TO FSESC")
                self.previous_time = time.time()



    def set_duty_cycle(self, value):
        self.duty_cycle = value

    def handle_duty_cycle(self, value):

        applied_Neutral = round(self.neutral*(value / abs(value)))
        calculated_Duty_Cycle = value + applied_Neutral
        print(calculated_Duty_Cycle)
        self.set_duty_cycle(calculated_Duty_Cycle)



    @staticmethod
    def duty_cycle_packet(value) -> bytes:

        message = pyvesc.SetDutyCycle(value)
        packet = pyvesc.encode(message)
        return packet