
from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo
import serial

import time

def main():

    #port = serial.Serial('COM8', 115200, timeout=0.1)

    #motor = Motor(port)
    servo = Servo("/dev/tty.usbserial-14220")

    #loop = motor.run()

    #motor.set_Current(2900)
    #servo.set_Steering(30)

    time.sleep(5)

    servo.set_Steering(60)

    time.sleep(5)
    #motor.kill()
    servo.kill()

    return

if __name__ == "__main__":
    main()
