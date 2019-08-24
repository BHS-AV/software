import inputs


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
            self.process_gamepad_event(event)

    # Proccess gamepad event
    def process_gamepad_event(self, event):
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
        return

    # Handles button command with CommandMap
    def handle_button_event(self, btn_event):
        return

    # Handle an Unknown Event
    def handle_unknown_event(self, event):
        # Check for various input types and convert is recognized, pass if not
        return
