'''
SpeedController.py
Benjamin S. Bussell
August 21st 2019
'''


from threading import Thread
import pyvesc
import serial

# TODO: DONT LET THIS IMPORT SURVIVE TESTING
import time


# This allows the run function to quietly run in the background.
def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


class MOTOR:

    def __init__(self, serialConnection):

        # Uncomment this for the actual program, it is just commented so I can test.
        self.FSESC = serialConnection

        # Current: the current applied to the motor
        self.current = 0
        # Duty Cycle: Controlling work load without accounting for current
        self.dutyCycle = 0
        self.brake = 0

        self.active = True

        self.currentTime = time.time()
        self.previousTime = time.time()

        pass

    @threaded
    def run(self):
        while self.active:

            self.currentTime = time.time()
            if (self.previousTime != self.currentTime):

                # Fixes conflicting commands
                # Priortize brake then current then duty cycle
                if (self.brake != 0):
                    print("Brake: ", self.brake)
                    self.FSESC.write(self.brakePacket(self.brake))
                elif (self.current != 0):
                    print("Current: ", self.current)
                    self.FSESC.write(self.currentPacket(self.current))
                elif (self.dutyCycle != 0):
                    print("Duty Cycle: ", self.dutyCycle)
                    self.FSESC.write(self.dutyCyclePacket(self.dutyCycle))
                self.FSESC.flush()


                self.previousTime = time.time()

    def dutyCyclePacket(self, value) -> bytes:

        message = pyvesc.SetDutyCycle(value)
        packet = pyvesc.encode(message)
        return packet

    def currentPacket(self, value) -> bytes:

        message = pyvesc.SetCurrent(value)
        packet = pyvesc.encode(message)
        return packet

    def brakePacket(self, value) -> bytes:

        message = pyvesc.SetCurrentBrake(value)
        packet = pyvesc.encode(message)
        return packet

    def speed_handle(self, value):
        self.current = value
        pass

    def kill(self):
        self.active = False
        pass


def main():

    macbookPort = serial.Serial('/dev/tty.usbmodem3011',115200,timeout = 0.1)
    speed = MOTOR(macbookPort)
    loop = speed.run()
    speed.speed_handle(0)
    time.sleep(5)
    speed.speed_handle(2700)
    time.sleep(15)
    speed.kill()


if __name__ == "__main__":
    main()
