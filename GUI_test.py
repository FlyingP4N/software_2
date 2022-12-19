import PySimpleGUI as sg

BAR_MAX = 200


class GUIWindow:
    def __init__(self, layout, maximise=False):
        # layout the Window
        self.layout = layout
        # create the Window
        self.window = sg.Window('Custom Progress Meter', self.layout).Finalize()
        if maximise:
            self.window.Maximize()

    def update_window(self, data: dict):
        f = True
        self.event, self.values = self.window.read(timeout=10)
        if self.event == 'Cancel' or self.event == sg.WIN_CLOSED:
            f = False
            self.window.close()
        for key in data.keys():
            if key in self.window.key_dict:
                self.window[key].update(data[key])
        return f

"""
# loop that would normally do something useful
f = True
while f:
    for i in range(BAR_MAX):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            f = False
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['-PROG-'].update(i+1)
        window['-LEFT-'].update(str(i))


layout = [[sg.Text('A custom progress meter')],
          [sg.T('0', size=(4, 1), key='-LEFT-'), sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), key='-PROG-'), sg.T('0', size=(4, 1), key='-RIGHT-')],
          [sg.Cancel()]]
scene = GUIWindow(layout)
data = {'-LEFT-': 0,
        '-RIGHT-': 0,
        '-PROG-': 0}
while True:
    for i in range(100):
        data['-LEFT-'] = i
        data['-RIGHT-'] = i - 100
        data['-PROG-'] = i+1
        scene.update_window(data)
"""