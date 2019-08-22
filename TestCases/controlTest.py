
from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo
import serial



def main():

    macbook_Port = serial.Serial('/dev/tty.usbmodem3011', 115200, timeout=0.1)
    motor = Motor(macbook_Port)
    servo = Servo(macbook_Port)
    pass

if __name__ == "__main__":
    main()