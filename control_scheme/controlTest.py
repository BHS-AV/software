
from control_scheme.SpeedController import MOTOR
from control_scheme.SteerController import SERVO
import serial



def main():

    macbookPort = serial.Serial('/dev/tty.usbmodem3011', 115200, timeout=0.1)
    motor = MOTOR(macbookPort)
    servo = SERVO(macbookPort)
    pass

if __name__ == "__main__":
    main()