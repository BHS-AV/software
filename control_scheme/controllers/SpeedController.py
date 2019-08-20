import pyvesc
import serial


class Motor:

    def __init__(self):

        self.FSESC = serial.Serial('PLACEHOLDER',115200,timeout = 0.1)

        self.rrpm = 0 # Expected to be unusable
        self.current = 0
        self.brake = 0
        self.dutyCycle = 0
        self.pos = 0


        pass

    def dutyCyclePacket(self, value) -> bytes:

        message = pyvesc.setDutyCycle(value)
        packet = pyvesc.encode(message)
        return packet

    def currentPacket(self, value) -> bytes:

        message = pyvesc.setCurrent(value)
        packet = pyvesc.encode(message)
        return packet

    def brakePacket(self, value) -> bytes:

        message = pyvesc.SetCurrentBrake(value)
        packet = pyvesc.encode(message)
        return packet



    def speed_handle(self):
        pass