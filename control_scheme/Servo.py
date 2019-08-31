'''

Servo.py
Benjamin S. Bussell
August 21st 2019

'''

import time
import serial


class Servo:

    def __init__(self, serial_connection):

        try:
            self.nano = serial_connection

        except(FileNotFoundError, serial.SerialException):

            print("Serial Port Unavailable Initialisation Failed... Your Codes About to Go To Shit")
            return

        time.sleep(4)

        self.angle_value = 90
        self.angle_smoothing = 1

        self.set_steering(self.angle_value)

        # If nothing catches fire you'll get here.
        print(" Successful initialisation")

    # If you unplug it, it goes to neutral
    def __del__(self):

        # self.buildPacket is explained in the update function bellow.
        self.nano.write(self.build_packet('S', 90))

        # Close Port so no longer connected.
        self.nano.close()

        print("Successful Destruction")

    def set_steering(self, Value: int, Delta=None):

        # Self Explanatory
        self.angle_value = Value
        self.nano.write(self.build_packet('S', self.angle_value))
        # TODO: Smoother Angle Changes Testing
        if (Delta):
            self.angle_smoothing = Delta
            self.nano.write(self.build_packet('s', self.angle_smoothing))

    def read_angle(self) -> int:

        self.nano.write('r00'.encode())
        return int(self.nano.readline().decode())

    def build_packet(self, char, value):
        # split the byte in half
        # EX: 0010 0001 0100 0010 -> 0010 0001 and 0100 0010
        # Done to streamline sending the bytes to arduino and allow for numbers above 255.
        self.Low = (value >> 8) & 0xFF
        self.High = value & 0xFF

        # Builds byte array out of the character in binary format and the two bytes above
        self.Packet = bytes([ord(char), self.Low, self.High])

        return self.Packet
