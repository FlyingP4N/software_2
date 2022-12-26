import platform
from GUI_test import *
import websocket
import time

if platform.system() == "Windows":
    from gamepad_win import XboxController
else:
    from gamepad_lin import XboxController

# Connect to WebSocket server
ws = websocket.WebSocket()
ws.connect("ws://192.168.0.1")

joy = XboxController(threads=True)
data = joy.read()
window.read(timeout=10)

if __name__ == '__main__':
    data_old = data
    while 1:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or bool(data['START button']):
            break
        data = joy.read()
        # print(data)
        if data_old != data:
            print("change detected")
            # get the start time
            st = time.time()
            # Ask the user for some input and transmit it
            ws.send(str(list(data.values())).replace('[', '').replace(']', ''))
            update_buttons(data, window)

            # Wait for server to respond and print it
            # result = ws.recv()
            # print(f"Answer received; ping {(time.time() - st)*1000:0.4f}")

        data_old = data

    # Gracefully close WebSocket connection
    ws.close()
