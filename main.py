import platform
from GUI_test import GUIWindow

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
"""
if __name__ == '__main__':
    joy = XboxController()
    while True:
        if platform.system() == "Windows":
            joy.monitor_controller()
        print(joy.read())

