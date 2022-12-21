import platform
from GUI_test import *

if platform.system() == "Windows":
    from gamepad_win import XboxController
else:
    from gamepad_lin import XboxController

# url = 'http://192.168.4.1/'
# my_obj = {'text_true': 'true',
#           'text_false': 'false',
#           'text_test': 'test'}
#
# start = time.time()
# for i in range(0, 10):
#     for key in my_obj:
#         print(key)
#         response = requests.get(f'{url}{my_obj[key]}')
#         print(response.text)
#         print(my_obj[key])
#         print()
#
# end = time.time()
# print((end - start)/30)

joy = XboxController(threads=True)
data = joy.read()
window.read(timeout=10)

if __name__ == '__main__':
    while 1:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or bool(data['START button']):
            break
        data = joy.read()
        print(data)
        update_buttons(data, window)
