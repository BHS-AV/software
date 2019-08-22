
from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo
import serial

import time

def main():

    macbook_Port = serial.Serial('/dev/tty.usbmodem3011', 115200, timeout=0.1)

    motor = Motor(macbook_Port)
    servo = Servo(macbook_Port)

    loop = Motor.run()

    motor.set_Current(2900)
    servo.set_Steering(30)

    time.sleep(5)

    motor.kill()
    servo.kill()

    loop.join()
    pass

if __name__ == "__main__":
    main()