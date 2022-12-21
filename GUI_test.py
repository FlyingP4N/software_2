import PySimpleGUI as sg
from inputs import DeviceManager

SIG_MAX = 32767
win_size = (1280, 800)
trig_size = (201, 21)
buttons_size = (201, 201)
buttons_offset = 55
maximise = False
outline = 'white'
highlight = 'white'
buttons = 'blue'
back = 'black'
sg.theme('DarkBlue')

if len(DeviceManager().gamepads) != 0:
    text = f'Gamepad found: \n {DeviceManager().gamepads[0]}'
elif len(DeviceManager().keyboards) != 0:
    text = f'Gamepad not found, switched to keyboard: \n {DeviceManager().keyboards[0]}'
else:
    text = f'Input device not found, here is the list: \n {DeviceManager().all_devices}'

layout_t_l = [[sg.ProgressBar(SIG_MAX, orientation='h', size_px=trig_size, key='Trigger Left')],
              [sg.Graph(canvas_size=trig_size, graph_bottom_left=(0, 0), graph_top_right=trig_size, key='Bumper Left')]]
layout_t_r = [[sg.ProgressBar(SIG_MAX, orientation='h', size_px=trig_size, key='Trigger Right')],
              [sg.Graph(canvas_size=trig_size, graph_bottom_left=(0, 0), graph_top_right=trig_size, key='Bumper Right')]]
layout_b_r = [[sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Stick Right')],
              [sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Buttons')]]
layout_b_l = [[sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Stick Left')],
              [sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='D-Pad')]]

layout = [[sg.Col(layout_t_l, p=0), sg.Push(), sg.Text(text, justification='c', font=14), sg.Push(), sg.Col(layout_t_r, p=0)],
          [sg.VPush()],
          [sg.Col(layout_b_l, p=0), sg.Push(), sg.Col(layout_b_r, p=0)]]

window = sg.Window('Graph test', layout, finalize=True, resizable=True, size=win_size)
if maximise:
    window.Maximize()

window['Stick Right'].DrawRectangle(top_left=(0, buttons_size[1]), bottom_right=(buttons_size[0]-1, 1), line_color=outline)
window['Stick Right'].DrawLine((buttons_size[0]//2, 2), (buttons_size[0]//2, buttons_size[1]))
window['Stick Right'].DrawLine((2, buttons_size[1]//2), (buttons_size[0]-1, buttons_size[1]//2))
window['Stick Left'].DrawRectangle(top_left=(0, buttons_size[1]), bottom_right=(buttons_size[0]-1, 1), line_color=outline)
window['Stick Left'].DrawLine((buttons_size[0]//2, 2), (buttons_size[0]//2, buttons_size[1]))
window['Stick Left'].DrawLine((2, buttons_size[1]//2), (buttons_size[0]-1, buttons_size[1]//2))

bumper_l = window['Bumper Left'].DrawRectangle(top_left=(0, trig_size[1]), bottom_right=(trig_size[0]-1, 1), line_color=outline, fill_color=back)
bumper_r = window['Bumper Right'].DrawRectangle(top_left=(0, trig_size[1]), bottom_right=(trig_size[0]-1, 1), line_color=outline, fill_color=back)
stick_l = window['Stick Left'].DrawPoint((buttons_size[0]//2, buttons_size[1]//2), 5, color=highlight)
stick_r = window['Stick Right'].DrawPoint((buttons_size[0]//2, buttons_size[1]//2), 5, color=highlight)
button_a = window['Buttons'].DrawCircle((buttons_size[0]//2, buttons_size[1]//2-buttons_offset), 30, line_color=outline, fill_color=back)
button_b = window['Buttons'].DrawCircle((buttons_size[0]//2+buttons_offset, buttons_size[1]//2), 30, line_color=outline, fill_color=back)
button_x = window['Buttons'].DrawCircle((buttons_size[0]//2-buttons_offset, buttons_size[1]//2), 30, line_color=outline, fill_color=back)
button_y = window['Buttons'].DrawCircle((buttons_size[0]//2, buttons_size[1]//2+buttons_offset), 30, line_color=outline, fill_color=back)
dpad_up = window['D-Pad'].DrawPolygon([(70, 180), (130, 180), (130, 130), (100, 100), (70, 130)], line_color=outline, fill_color=back)
dpad_down = window['D-Pad'].DrawPolygon([(70, 20), (130, 20), (130, 70), (100, 100), (70, 70)], line_color=outline, fill_color=back)
dpad_right = window['D-Pad'].DrawPolygon([(180, 70), (180, 130), (130, 130), (100, 100), (130, 70)], line_color=outline, fill_color=back)
dpad_left = window['D-Pad'].DrawPolygon([(20, 130), (20, 70), (70, 70), (100, 100), (70, 130)], line_color=outline, fill_color=back)


def update_buttons(data, window):
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

    window['Stick Left'].relocate_figure(stick_l,
                                         x=int((data['Left Joystick X'] / SIG_MAX + 1) * buttons_size[0] // 2),
                                         y=int((-data['Left Joystick Y'] / SIG_MAX + 1) * buttons_size[1] // 2))
    window['Stick Right'].relocate_figure(stick_l,
                                          x=int((data['Right Joystick X'] / SIG_MAX + 1) * buttons_size[0] // 2),
                                          y=int((-data['Right Joystick Y'] / SIG_MAX + 1) * buttons_size[1] // 2))
