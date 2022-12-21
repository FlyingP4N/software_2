from inputs import get_gamepad, DeviceManager
from pynput import keyboard
import math
import threading


class XboxController(object):
    MAX_AXIS_VAL = 32767

    def __init__(self, threads=False):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.DPadY = 0
        self.DPadX = 0

        if threads:
            if len(DeviceManager().gamepads) != 0:
                self._monitor_thread = threading.Thread(target=self._monitor_controller)
                self._monitor_thread.daemon = True
                self._monitor_thread.start()
            elif len(DeviceManager().keyboards) != 0:
                self._monitor_thread = threading.Thread(target=self._monitor_keyboard)
                self._monitor_thread.daemon = True
                self._monitor_thread.start()
            else:
                raise RuntimeError('Input device not found')

    def read(self):  # return the buttons/triggers that you care about in this methode
        output = {'Left Joystick X': self.LeftJoystickX,
                  'Left Joystick Y': self.LeftJoystickY,
                  'Right Joystick X': self.RightJoystickX,
                  'Right Joystick Y': self.RightJoystickY,
                  'A button': self.A,
                  'B button': self.B,
                  'X button': self.X,
                  'Y button': self.Y,
                  'START button': self.Start,
                  'SELECT button': self.Back,
                  'Left Bumper': self.LeftBumper,
                  'Right Bumper': self.RightBumper,
                  'Left Trigger': self.LeftTrigger,
                  'Right Trigger': self.RightTrigger,
                  'Thumb L': self.LeftThumb,
                  'Thumb R': self.RightThumb,
                  'D-pad Y': self.DPadY,
                  'D-pad X': self.DPadX
                  }

        return output

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                # print(event.code)
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = - event.state
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = - event.state
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = ((2 * event.state / 255) - 1) * XboxController.MAX_AXIS_VAL
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = ((2 * event.state / 255) - 1) * XboxController.MAX_AXIS_VAL
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state
                elif event.code == 'ABS_HAT0Y':
                    self.DPadY = event.state * XboxController.MAX_AXIS_VAL
                elif event.code == 'ABS_HAT0X':
                    self.DPadX = event.state * XboxController.MAX_AXIS_VAL

    def _monitor_keyboard(self):
        with keyboard.Events() as events:
            for event in events:
                # print(event)
                self.A = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='w')))
                self.B = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='s')))
                self.X = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='a')))
                self.Y = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='d')))
                self.LeftBumper = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='q')))
                self.RightBumper = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='e')))
                self.RightTrigger = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='w'))) * XboxController.MAX_AXIS_VAL
                self.LeftTrigger = int((type(event) is keyboard.Events.Press) and (event.key == keyboard.KeyCode(char='s'))) * XboxController.MAX_AXIS_VAL
