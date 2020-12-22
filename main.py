import serial
import time
from pynput.keyboard import Controller
import PySimpleGUI as sg
import serial.tools.list_ports
import threading

joyN = 'up'
joyS = 'down'
joyE = 'left'
joyW = 'right'
btn1 = 'a'
btn2 = 's'
btn3 = 'd'
btn4 = 'f'
btn5 = 'z'
btn6 = 'x'
btn7 = 'c'
btn8 = 'v'
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
        [sg.Text(joyW, key='joyW')],
        [sg.Text(btn1, key='btn1')],
        [sg.Text(btn2, key='btn2')],
        [sg.Text(btn3, key='btn3')],
        [sg.Text(btn4, key='btn4')],
        [sg.Text(btn5, key='btn5')],
        [sg.Text(btn6, key='btn6')],
        [sg.Text(btn7, key='btn7')],
        [sg.Text(btn8, key='btn8')]]
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
        print(btn1)
        time.sleep(3)


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
            if values[1] != '':
                btn1 = values[1]
            if values[2] != '':
                btn2 = values[2]
            if values[3] != '':
                btn3 = values[3]
            if values[4] != '':
                btn4 = values[4]
            if values[5] != '':
                btn5 = values[5]
            if values[6] != '':
                btn5 = values[6]
            if values[7] != '':
                btn5 = values[7]
            if values[8] != '':
                btn5 = values[8]
            config_window['btn1'].update(btn1)
            config_window['btn2'].update(btn2)
            config_window['btn3'].update(btn3)
            config_window['btn4'].update(btn4)
            config_window['btn5'].update(btn5)
            config_window['btn6'].update(btn6)
            config_window['btn7'].update(btn7)
            config_window['btn8'].update(btn8)
            config_window.Refresh()
        if event == sg.WIN_CLOSED:
            stop_threads = True
            t1.join()
            quit()
#   data = arduino.read()
# #   if data.decode('utf-8') == 'd': #D
# #       keyboard.press('d')
