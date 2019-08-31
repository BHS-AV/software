

from control_scheme.Motor import Motor
from control_scheme.Servo import Servo

from test_cases.serial_port_picker import select_Port


import time

def main():

    port = serial.Serial('COM8', 115200, timeout=0.1)

    #motor = Motor(port)
    servo = Servo(port)

    #motor.run()


    #motor.set_Current(2900)
    servo.set_Steering(100)


    x = 60
    while x<140:
        x += 10
        servo.set_Steering(x)
        time.sleep(0.1)

    #ime.sleep(5)

    #motor.kill()
    servo.kill()

    return

if __name__ == "__main__":
    main()
