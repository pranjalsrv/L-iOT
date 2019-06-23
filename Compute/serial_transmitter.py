import serial

def serial_transmit(PORT, BAUD_RATE, message):
    ser = serial.Serial(PORT,BAUD_RATE)
    ser.write(message.encode('UTF-8'))
    ser.close()
