# import serial
import time
from pynput.keyboard import Controller
import PySimpleGUI as sg
import serial.tools.list_ports
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
layoutConfig = [[sg.Text(f'{element} -'), sg.In(key=element, size=(2,0)), sg.Text(joyE)] for element in 'NSE']
layoutConfig += [[sg.Text(f'{element}-'), sg.In(key=element, size=(2,0)), sg.Text(joyE)] for element in 'W']
layoutConfig += [[sg.Text(f'{i} -'), sg.In(key=i, size=(2,0))] for i in range(1,9)]


setupWindow = sg.Window('ArduinoStick 1.0', layoutSetup)
configWindow = sg.Window('ArduinoStick 1.0', layoutConfig)

time.sleep(3)

while True:
    while setup:
        print(availablePorts)
        event, values = setupWindow.read()
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'OK':
            arduino = serial.Serial(values[1], 1000000, timeout=.1)
            setup = False
            break

    while not setup:
        event, values = configWindow.read()
        # noinspection PyUnboundLocalVariable
        data = arduino.read()
        print(data)


#   data = arduino.read()
#   if data.decode('utf-8') == 'd': #D
#       keyboard.press('d')
#   github test 123