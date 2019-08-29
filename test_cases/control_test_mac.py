
from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo

from test_cases.serial_port_picker import select_Port

import time

def main():

    port = select_Port()

    motor = Motor(port)
    servo = Servo(port)

    loop = motor.run()

    motor.set_Current(2900)
    servo.set_Steering(100)

    time.sleep(5)

    motor.kill()
    servo.kill()

    return

if __name__ == "__main__":
    main()
