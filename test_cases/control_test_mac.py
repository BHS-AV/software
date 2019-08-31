

from control_scheme.Motor import Motor
from control_scheme.Servo import Servo

from test_cases.serial_port_picker import select_Port


import serial
import time

def main():


    port_string = select_Port()
    servo_port = serial.Serial(port_string, 9600, timeout=0.1)


    #motor = Motor(port)
    servo = Servo(servo_port)

    #motor.run()


    #motor.set_current(2900)
    servo.set_steering(100)



    x = 60
    while x<140:
        x += 10
        servo.set_steering(x)
        time.sleep(0.1)

   #time.sleep(5)

    #del motor
    del servo

    return

if __name__ == "__main__":
    main()
