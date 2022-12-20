import PySimpleGUI as sg

SIG_MAX = 32767
win_size = (1280, 800)
trig_size = (201, 21)
buttons_size = (201, 201)
buttons_offset = 55
outline = 'white'
highlight = 'white'
buttons = 'blue'
back = 'black'
sg.theme('DarkBlue')

layout_t_l = [[sg.ProgressBar(SIG_MAX, orientation='h', size_px=trig_size, key='Trigger Left')],
              [sg.Graph(canvas_size=trig_size, graph_bottom_left=(0, 0), graph_top_right=trig_size, key='Bumper Left')]]
layout_t_r = [[sg.ProgressBar(SIG_MAX, orientation='h', size_px=trig_size, key='Trigger Right')],
              [sg.Graph(canvas_size=trig_size, graph_bottom_left=(0, 0), graph_top_right=trig_size, key='Bumper Right')]]
layout_b_r = [[sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Stick Right')],
              [sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Buttons')]]
layout_b_l = [[sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='Stick Left')],
              [sg.Graph(canvas_size=buttons_size, graph_bottom_left=(0, 0), graph_top_right=buttons_size, key='D-Pad')]]

layout = [[sg.Col(layout_t_l, p=0), sg.Push(), sg.Col(layout_t_r, p=0)],
          [sg.VPush()],
          [sg.Col(layout_b_l, p=0), sg.Push(), sg.Col(layout_b_r, p=0)]]

window = sg.Window('Graph test', layout, finalize=True, resizable=True, size=win_size)
# window.bind('<Configure>', "Configure")

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

while True:
    event, values = window.read()
    print(event, ', ', values)
    if event == sg.WIN_CLOSED:
        break
