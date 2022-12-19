import PySimpleGUI as sg

sg.theme('DarkBrown4')
BAR_MAX = 200


class GUIWindow:
    def __init__(self, layout):
        # layout the Window
        self.layout = [[sg.Text('A custom progress meter')],
                       [sg.T('0', size=(4, 1), key='-LEFT-'), sg.ProgressBar(BAR_MAX, orientation='h', size=(20, 20), key='-PROG-')],
                       [sg.Cancel()]]
        self.layout = layout
        # create the Window
        self.window = sg.Window('Custom Progress Meter', self.layout).Finalize()
        self.window.Maximize()

    def update_window(self, data: dict):
        self.event, self.values = self.window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            self.window.close()
        return self.event, self.values


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

