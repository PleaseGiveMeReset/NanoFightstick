import serial

arduino = serial.Serial('COM7', 1000000, timeout=.1)

while True:
    data = arduino.read()
    print (data)