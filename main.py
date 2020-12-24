import serial
from pynput.keyboard import Controller
import PySimpleGUI as sg
import serial.tools.list_ports
import threading

joyN = 'up'
joyS = 'down'
joyE = 'left'
joyW = 'right'
buttons = {1: 'a', 2: 's', 3: 'd', 4: 'f', 5: 'z', 6: 'x', 7: 'c', 8: 'v'}


setup = True
keyboard = Controller()

# Create List Of Available COM Ports
availablePorts = list(serial.tools.list_ports.comports())
availablePortsList = {}
AP = 1
for x in availablePorts:
    availablePortsList[AP] = {x.description}
    AP += 1


# Gui Layouts
sg.theme('reddit')

col = [[sg.Text(f'{element} -'), sg.In(key=element, size=(2, 0))] for element in 'NSE']
col += [[sg.Text(f'{element}-'), sg.In(key=element, size=(2, 0))] for element in 'W']
col += [[sg.Text(f'{i} -'), sg.In(key=i, size=(2, 0))] for i in range(1, 9)]
col2 = [[sg.Text(joyN, key='joyN')],
        [sg.Text(joyS, key='joyS')],
        [sg.Text(joyE, key='joyE')],
        [sg.Text(joyW, key='joyW')]]
col2 += [[sg.Text(buttons[i - 20], key=i)] for i in range(21, 29)]

layout_config = [[sg.Column(col)] + [sg.Column(col2)] + [sg.Image(r'C:\Users\manny\Desktop\config.png')],
                 [sg.Button('Apply'), sg.Button('Start')]]
config_window = sg.Window('ArduinoStick 1.0', layout_config)


layoutSetup = [[sg.Text("Please Select an Available COM Port:")],
               [sg.Text(availablePortsList)],
               [sg.Combo(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8'], key=1)],
               [sg.Button('OK')]]
setupWindow = sg.Window('ArduinoStick 1.0', layoutSetup)


def run_process():
    while not stop_threads:
        data = arduino.read()


stop_threads = False


t1 = threading.Thread(target=run_process)

if True:
    while setup:
        print(availablePorts)
        event, valuesSetup = setupWindow.read()
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'OK':
            arduino = serial.Serial(valuesSetup[1], 1000000, timeout=.1)
            setup = False
            t1.start()
            setupWindow.close()
            break

    while not setup:
        event, values = config_window.read()
        if event == 'Apply':
            check_key = 1
            while True:
                if values[check_key] != '':
                    buttons[check_key] = values[check_key]
                    i = check_key + 20
                    config_window[i].update(values[check_key])
                check_key += 1
                if check_key > 8:
                    break

        if event == sg.WIN_CLOSED:
            stop_threads = True
            t1.join()
            quit()
