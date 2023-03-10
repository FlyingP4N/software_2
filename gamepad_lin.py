import os
import struct
import array
from fcntl import ioctl
import threading


def show_devises(directory: str):
    # Iterate over the joystick devices.
    print('Available devices:')
    output = []
    for device in os.listdir(directory):
        if device.startswith('js'):
            output.append(output)
            print(f'{directory}/%s' % device)
    return output


class XboxController(object):
    def __init__(self, threads=False):
        self.axis_names = {
            0x00: 'Left Joystick X',
            0x01: 'Left Joystick Y',
            0x02: 'Left Trigger',
            0x03: 'Right Joystick X',
            0x04: 'Right Joystick Y',
            0x05: 'Right Trigger',
            0x06: 'throttle',
            0x07: 'rudder',
            0x08: 'wheel',
            0x09: 'gas',
            0x0a: 'brake',
            0x10: 'D-pad X',
            0x11: 'D-pad Y',
            0x12: 'hat1x',
            0x13: 'hat1y',
            0x14: 'hat2x',
            0x15: 'hat2y',
            0x16: 'hat3x',
            0x17: 'hat3y',
            0x18: 'pressure',
            0x19: 'distance',
            0x1a: 'tilt_x',
            0x1b: 'tilt_y',
            0x1c: 'tool_width',
            0x20: 'volume',
            0x28: 'misc',
        }
        self.button_names = {
            0x120: 'trigger',
            0x121: 'thumb',
            0x122: 'thumb2',
            0x123: 'top',
            0x124: 'top2',
            0x125: 'pinkie',
            0x126: 'base',
            0x127: 'base2',
            0x128: 'base3',
            0x129: 'base4',
            0x12a: 'base5',
            0x12b: 'base6',
            0x12f: 'dead',
            0x130: 'A button',
            0x131: 'B button',
            0x132: 'c',
            0x133: 'X button',
            0x134: 'Y button',
            0x135: 'z',
            0x136: 'Left Bumper',
            0x137: 'Right Bumper',
            0x138: 'tl2',
            0x139: 'tr2',
            0x13a: 'SELECT button',
            0x13b: 'START button',
            0x13c: 'mode',
            0x13d: 'Thumb L',
            0x13e: 'Thumb R',

            0x220: 'dpad_up',
            0x221: 'dpad_down',
            0x222: 'dpad_left',
            0x223: 'dpad_right',

            # XBox 360 controller uses these codes.
            0x2c0: 'dpad_left',
            0x2c1: 'dpad_right',
            0x2c2: 'dpad_up',
            0x2c3: 'dpad_down',
        }
        self.axis_map = []
        self.button_map = []
        
        try:
            # Open the joystick device.
            fn = '/dev/input/js0'
            print('Opening %s...' % fn)
            self.jsdev = open(fn, 'rb')
            if threads:
                self._monitor_thread = threading.Thread(target=self._monitor_controller)
                self._monitor_thread.daemon = True
                self._monitor_thread.start()
        except:
            raise RuntimeError('Input device not found')

        self.get_axis()
        self.get_buttons()

        self.output = {'Left Joystick X': 0,
                       'Left Joystick Y': 0,
                       'Right Joystick X': 0,
                       'Right Joystick Y': 0,
                       'A button': 0,
                       'B button': 0,
                       'X button': 0,
                       'Y button': 0,
                       'START button': 0,
                       'SELECT button': 0,
                       'Left Bumper': 0,
                       'Right Bumper': 0,
                       'Left Trigger': 0,
                       'Right Trigger': 0,
                       'Thumb L': 0,
                       'Thumb R': 0,
                       'D-pad Y': 0,
                       'D-pad X': 0
                       }

    def get_device_name(self):
        # Get the device name.
        # buf = bytearray(63)
        buf = array.array('B', [0] * 64)
        ioctl(self.jsdev, 0x80006a13 + (0x10000 * len(buf)), buf)  # JSIOCGNAME(len)
        js_name = buf.tobytes().rstrip(b'\x00').decode('utf-8')
        return js_name

    def get_axis(self):
        # Get number of axes and buttons.
        buf = array.array('B', [0])
        ioctl(self.jsdev, 0x80016a11, buf)  # JSIOCGAXES
        num_axes = buf[0]

        # Get the axis map.
        buf = array.array('B', [0] * 0x40)
        ioctl(self.jsdev, 0x80406a32, buf)  # JSIOCGAXMAP

        for axis in buf[:num_axes]:
            axis_name = self.axis_names.get(axis, 'unknown(0x%02x)' % axis)
            self.axis_map.append(axis_name)

    def get_buttons(self):
        buf = array.array('B', [0])
        ioctl(self.jsdev, 0x80016a12, buf)  # JSIOCGBUTTONS
        num_buttons = buf[0]

        # Get the button map.
        buf = array.array('H', [0] * 200)
        ioctl(self.jsdev, 0x80406a34, buf)  # JSIOCGBTNMAP

        for btn in buf[:num_buttons]:
            btn_name = self.button_names.get(btn, 'unknown(0x%03x)' % btn)
            self.button_map.append(btn_name)

    def read(self):
        return self.output

    def _monitor_controller(self):
        while True:
            evbuf = self.jsdev.read(8)
            if evbuf:
                time, value, code, number = struct.unpack('IhBB', evbuf)

                if code & 0x01:
                    button = self.button_map[number]
                    if button:
                        self.output[button] = value

                if code & 0x02:
                    axis = self.axis_map[number]
                    if axis:
                        self.output[axis] = value
