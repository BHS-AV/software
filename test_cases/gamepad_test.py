from control_scheme.SpeedController import Motor
from control_scheme.SteerController import Servo
import serial
import inputs
import time


class Gamepad(object):
    def __init__(self, gamepad=None):
        self.btn_states = {}
        self.old_btn_states = {}
        self.abs_states = {}
        self.old_abs_states = {}
        self.gamepad = gamepad
        if not gamepad:
            self.init_gamepad()
        self._misc = 0

    def init_gamepad(self):
        try:
            self.gamepad = inputs.devices.gamepads[0]
        except IndexError:
            raise inputs.UnpluggedError("Gamepad not found.")

    # Handles all incoming events from inputs
    def process_all_events(self, var):
        # process all gamepad events, calling process_gamepad_event for each
        try:
            events = self.gamepad.read()
        except EOFError:
            events = []
        for event in events:
            self.process_gamepad_event(self.gamepad, event, var)

    # Proccess gamepad event
    def process_gamepad_event(self, gamepad, event, var):
        # Process gamepad event. Assign to handlers after parsing
        if event.ev_type == 'Sync' or event.ev_type == 'Misc':
            self.handle_unknown_event(event)
            return
        if event.ev_type == 'Key':
            self.handle_button_event(event)
        if event.ev_type == 'Absolute':
            self.handle_joystick_event(event, var)

    # Handles joyStick Command with CommandMap
    def handle_joystick_event(self, jsEvent, var):
        var = int((jsEvent.state / 255 * 2000) + 2500)
        return int(var)

    # Handles button command with CommandMap
    def handle_button_event(self, btnEvent):
        print(btnEvent)
        return

    # Handle an Unknown Event
    def handle_unknown_event(self, event):
        # Check for various input types and convert is recognized, pass if not
        return


def main():
    com = serial.Serial('COM8', 115200, timeout=0.1)

    motor = Motor(com)
    servo = Servo(com)

    gamepad = Gamepad()

    loop = motor.run()

    motor.set_Current(2500)
    servo.set_Steering(30)
    gamepad = inputs.devices.gamepads[0]
    var = 2500
    while 1:
        event = gamepad.read()

    motor.kill()
    servo.kill()


if __name__ == "__main__":
    main()
