from control_scheme.Motor import Motor
from control_scheme.Servo import Servo
import serial
import inputs
import time


class Gamepad(object):
    def __init__(self, motor, servo, gamepad=None):
        self.btn_states = {}
        self.old_btn_states = {}
        self.abs_states = {}
        self.old_abs_states = {}
        self.gamepad = gamepad
        self.motor = motor
        self.servo = servo
        if not gamepad:
            self.init_gamepad()
        self._misc = 0

    def init_gamepad(self):
        try:
            self.gamepad = inputs.devices.gamepads[0]
        except IndexError:
            raise inputs.UnpluggedError("Gamepad not found.")

    # Handles all incoming events from inputs
    def process_all_events(self):
        # process all gamepad events, calling process_gamepad_event for each
        try:
            events = self.gamepad.read()
        except EOFError:
            events = []
        for event in events:
            self.process_gamepad_event(self.gamepad, event)

    # Proccess gamepad event
    def process_gamepad_event(self, gamepad, event):
        # Process gamepad event. Assign to handlers after parsing
        if event.ev_type == 'Sync' or event.ev_type == 'Misc':
            self.handle_unknown_event(event)
            return
        if event.ev_type == 'Key':
            self.handle_button_event(event)
        if event.ev_type == 'Absolute':
            if event.code in ['ABS_RX', 'ABS_RY', 'ABS_X', 'ABS_Y']:
                self.handle_trigger_event(event)
            else:
                self.handle_joystick_event(event)

    # Handles trigger_event
    def handle_trigger_event(self, trigger_event):
        global steer_ang
        # steer_ang = 0
        state = trigger_event.state
        code = trigger_event.code
        if code == 'ABS_RX':
            steer_ang = int((state / 32767) * 30 + 90)
            print(steer_ang)
        self.servo.set_steering(steer_ang)
        return

    # Handles jostick_event
    def handle_joystick_event(self, js_event):
        global current
        state = js_event.state
        code = js_event.code
        if code == 'ABS_RZ':
            if state != 0:
                current = int((state / 255 * 4000) + 4000)
            else:
                current = 0
        elif code == 'ABS_Z':
            if state != 0:
                current = -int((state / 255 * 4000) + 4000)
            else:
                current = 0
        self.motor.set_current(current)
        return

    # Handles button_event
    def handle_button_event(self, btn_event):
        print(btn_event)
        return

    # Handle an Unknown Event
    def handle_unknown_event(self, event):
        # Check for various input types and convert is recognized, pass if not
        return


if __name__ == '__main__':

    # Windows Ports
    #servo_port = serial.Serial('COM11', 9600, timeout=0.1)
    motor_port = serial.Serial('COM8', 11520, timeout=0.1)

    # Linux Ports
    # servo_port = serial.Serial('COM11', 9600, timeout=0.1)
    # motor_port = serial.Serial('COM8', 11520, timeout=0.1)

    # Mac Ports
    # servo_port = serial.Serial('COM11', 9600, timeout=0.1)
    # motor_port = serial.Serial('COM8', 11520, timeout=0.1)

    motor = Motor(motor_port)
    #servo = Servo(servo_port)

    loop = motor.run()

    gamepad = Gamepad(motor, None)

    print('Initializing...')

    while 1:
        gamepad.process_all_events()
