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

    def set_steering(self, value: int, delta=None):

        # Self Explanatory
        self.angle_value = value
        self.nano.write(self.build_packet('S', self.angle_value))
        # TODO: Smoother Angle Changes Testing
        if (delta):
            self.angle_smoothing = delta
            self.nano.write(self.build_packet('s', self.angle_smoothing))

    def read_angle(self) -> int:

        self.nano.write('r00'.encode())
        return int(self.nano.readline().decode())

    @staticmethod
    def build_packet(write_type, value):
        """
        :type write_type: Char
        :type value: Int
        """
        # split the byte in half
        # EX: 0010 0001 0100 0010 -> 0010 0001 and 0100 0010
        # Done to streamline sending the bytes to arduino and allow for numbers above 255.
        low = (value >> 8) & 0xFF
        high = value & 0xFF

        # Builds byte array out of the character in binary format and the two bytes above
        packet = bytes([ord(write_type), low, high])

        return packet
