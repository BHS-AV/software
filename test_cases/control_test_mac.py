

from control_scheme.Motor import Motor
from control_scheme.Servo import Servo

from test_cases.serial_port_picker import select_port


import serial
import time

def main():


    servo_port_string = select_port()
    servo_port = serial.Serial(servo_port_string, 9600, timeout=0.1)

    # motor_port_string = select_port()
    # motor_port = serial.Serial(motor_port_string, 11500, timeout=0.1)

    # motor = Motor(port)
    servo = Servo(servo_port)

    Servo.build_packet('T',5)
    # motor.run()


    # motor.set_current(2900)
    servo.set_steering(100)



    x = 65
    while x<135:
        x += 2
        servo.set_steering(x)
        time.sleep(0.1)
        print("Angle Read Directly: ", servo.read_angle())
    while x>65:
        x -= 2
        servo.set_steering(x)
        time.sleep(0.1)
        print("Angle Read Directly: ", servo.read_angle())
    while x < 135:
        x += 2
        servo.set_steering(x)
        time.sleep(0.1)
        print("Angle Read Directly: ", servo.read_angle())
    while x > 65:
        x -= 2
        servo.set_steering(x)
        time.sleep(0.1)
        print("Angle Read Directly: ", servo.read_angle())

    # time.sleep(5)

    # del motor
    del servo

    return

if __name__ == "__main__":
    main()
