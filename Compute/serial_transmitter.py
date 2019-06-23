import serial
ser = serial.Serial("COM13",9600)
a=input()
ser.write(a.encode('UTF-8'))
ser.close()
