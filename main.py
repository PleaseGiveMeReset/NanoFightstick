# import serial
import time
from pynput.keyboard import Controller
import PySimpleGUI as sg
import serial.tools.list_ports
sg.theme('reddit')
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

availablePorts = list(serial.tools.list_ports.comports())
availablePortsList = {}
AP = 1
for x in availablePorts:
    availablePortsList[AP] = {x.description}
    AP += 1
keyboard = Controller()
setup = True

layoutSetup = [[sg.Text("Please Select an Available COM Port:")],
          [sg.Text(availablePortsList)],
          [sg.Combo(['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8'], enable_events=True, key=1)],
          [sg.Button('OK')]]
col = [[sg.Text(f'{element} -'), sg.In(key=element, size=(2,0))] for element in 'NSE']
col += [[sg.Text(f'{element}-'), sg.In(key=element, size=(2,0))] for element in 'W']
col += [[sg.Text(f'{i} -'), sg.In(key=i, size=(2,0))] for i in range(1,9)]
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
layoutConfig = [[sg.Column(col)] + [sg.Column(col2)] + [sg.Image(r'C:\Users\manny\Desktop\config.png')], [sg.Button('Apply'), sg.Button('Start')]]

setupWindow = sg.Window('ArduinoStick 1.0', layoutSetup)
configWindow = sg.Window('ArduinoStick 1.0', layoutConfig)

time.sleep(3)

while True:
    while setup:
        print(availablePorts)
        event, valuesSetup = setupWindow.read()
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'OK':
            arduino = serial.Serial(valuesSetup[1], 1000000, timeout=.1)
            setup = False
            break

    while not setup:
        setupWindow.close()
        event, values = configWindow.read()
        # noinspection PyUnboundLocalVariable
        if event == 'Apply':
            joyE = 'left'
            joyW = 'right'
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
            configWindow['btn1'].update(btn1)
            configWindow['btn2'].update(btn2)
            configWindow['btn3'].update(btn3)
            configWindow['btn4'].update(btn4)
            configWindow['btn5'].update(btn5)
            configWindow['btn6'].update(btn6)
            configWindow['btn7'].update(btn7)
            configWindow['btn8'].update(btn8)
            configWindow.Refresh()
        if event == sg.WIN_CLOSED:
            quit()
        data = arduino.read()
        print(btn1, btn2, btn3)


#   data = arduino.read()
#   if data.decode('utf-8') == 'd': #D
#       keyboard.press('d')
#   github test 123