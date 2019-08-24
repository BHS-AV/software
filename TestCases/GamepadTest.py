from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo
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
            self.handle_joystick_event(event)

    # Handles joyStick Command with CommandMap
    def handle_joystick_event(self, js_event):
        if js_event.code == 'ABS_RZ':
            var = int((js_event.state / 255 * 3000) + 2900)
        elif js_event.code == 'ABS_Z':
            var = -int((js_event.state / 255 * 3000) + 2900)
        else:
            var = 0
        self.motor.set_Current(var)
        var = 0
        # vprint (js_event.code)
        print(js_event.state)
        #print(var)
        return

    # Handles button command with CommandMap
    def handle_button_event(self, btn_event):
        print(btn_event)
        return

    # Handle an Unknown Event
    def handle_unknown_event(self, event):
        # Check for various input types and convert is recognized, pass if not
        return


if __name__ == '__main__':
    port = serial.Serial('COM8', 115200, timeout=0.1)
    motor = Motor(port)
    servo = Servo(port)
    loop = motor.run()
    #motor.set_Current(2900)
    gamepad = Gamepad(motor, servo)
    while 1:
        gamepad.process_all_events()
