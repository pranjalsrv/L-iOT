import serial

def serial_receive(PORT, BAUD_RATE):
    ser = serial.Serial(PORT, BAUD_RATE)
    while True:
        reading = ser.readline()
        print(reading)
