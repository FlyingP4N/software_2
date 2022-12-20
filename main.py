import platform
import PySimpleGUI as sg
import inputs
from pynput import keyboard
# import GUI_test

if platform.system() == "Windows":
    from gamepad_win import XboxController
else:
    from gamepad_lin import XboxController

url = 'http://192.168.4.1/'
my_obj = {'text_true': 'true',
          'text_false': 'false',
          'text_test': 'test'}

"""
start = time.time()
for i in range(0, 10):
    for key in my_obj:
        print(key)
        response = requests.get(f'{url}{my_obj[key]}')
        print(response.text)
        print(my_obj[key])
        print()

end = time.time()
print((end - start)/30)

if __name__ == '__main__':
    # joy = XboxController()
    while True:
        events = inputs.get_key()
        if events:
            for event in events:
                print(event.ev_type, event.code, event.state)
"""
SIG_MAX = 32767
win_size = (1280, 800)
trig_size = (201, 21)
buttons_size = (201, 201)
buttons_offset = 55

outline = 'white'
highlight = 'white'
buttons = 'red'
back = 'black'
sg.theme('DarkBlue')
maximise = False

window = sg.Window('Graph test', layout, finalize=True, resizable=True, size=win_size)
if maximise:
    window.Maximize()


joy = XboxController()
data = joy.read()
window.read(timeout=10)

data = {'START button': 0}

if __name__ == '__main__':
    while 1:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break
        # print(inputs.DeviceManager().keyboards)
        print(data)
        try:
            events = inputs.get_key()
            print(events.state, event.code)
        except:
            print('', end='')

        
        if bool(data['START button']):
            break
        if bool(data['Right Bumper']):
            window['Bumper Right'].TKCanvas.itemconfig(bumper_r, fill=buttons)
        else:
            window['Bumper Right'].TKCanvas.itemconfig(bumper_r, fill=back)
        if bool(data['Left Bumper']):
            window['Bumper Left'].TKCanvas.itemconfig(bumper_l, fill=buttons)
        else:
            window['Bumper Left'].TKCanvas.itemconfig(bumper_l, fill=back)
        if bool(data['A button']):
            window['Buttons'].TKCanvas.itemconfig(button_a, fill=buttons)
        else:
            window['Buttons'].TKCanvas.itemconfig(button_a, fill=back)
        if bool(data['B button']):
            window['Buttons'].TKCanvas.itemconfig(button_b, fill=buttons)
        else:
            window['Buttons'].TKCanvas.itemconfig(button_b, fill=back)
        if bool(data['X button']):
            window['Buttons'].TKCanvas.itemconfig(button_x, fill=buttons)
        else:
            window['Buttons'].TKCanvas.itemconfig(button_x, fill=back)
        if bool(data['Y button']):
            window['Buttons'].TKCanvas.itemconfig(button_y, fill=buttons)
        else:
            window['Buttons'].TKCanvas.itemconfig(button_y, fill=back)
    
        if data['D-pad Y'] > 0:
            window['D-Pad'].TKCanvas.itemconfig(dpad_up, fill=back)
            window['D-Pad'].TKCanvas.itemconfig(dpad_down, fill=buttons)
        elif data['D-pad Y'] < 0:
            window['D-Pad'].TKCanvas.itemconfig(dpad_up, fill=buttons)
            window['D-Pad'].TKCanvas.itemconfig(dpad_down, fill=back)
        else:
            window['D-Pad'].TKCanvas.itemconfig(dpad_up, fill=back)
            window['D-Pad'].TKCanvas.itemconfig(dpad_down, fill=back)
        if data['D-pad X'] < 0:
            window['D-Pad'].TKCanvas.itemconfig(dpad_right, fill=back)
            window['D-Pad'].TKCanvas.itemconfig(dpad_left, fill=buttons)
        elif data['D-pad X'] > 0:
            window['D-Pad'].TKCanvas.itemconfig(dpad_right, fill=buttons)
            window['D-Pad'].TKCanvas.itemconfig(dpad_left, fill=back)
        else:
            window['D-Pad'].TKCanvas.itemconfig(dpad_right, fill=back)
            window['D-Pad'].TKCanvas.itemconfig(dpad_left, fill=back)
    
        window['Trigger Left'].update(data['Left Trigger'] + SIG_MAX)
        window['Trigger Right'].update(data['Right Trigger'] + SIG_MAX)
    
        window['Stick Left'].relocate_figure(stick_l, x=int((data['Left Joystick X']/SIG_MAX + 1) * buttons_size[0]//2), y=int((-data['Left Joystick Y']/SIG_MAX + 1) * buttons_size[1]//2))
        window['Stick Right'].relocate_figure(stick_l, x=int((data['Right Joystick X']/SIG_MAX + 1) * buttons_size[0]//2), y=int((-data['Right Joystick Y']/SIG_MAX + 1) * buttons_size[1]//2))
        
        if platform.system() == "Windows":
            joy.monitor_controller()
        print(joy.read())
        data = joy.read()
        print(bool(data['D-pad Y']))


