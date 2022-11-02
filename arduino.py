import serial
import time

ser = serial.Serial('COM3',9600,timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print('serial ok')

try:
    while True:
        time.sleep(1)
        #print("sending message to arduino")
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8')
            print(line)
except KeyboardInterrupt:
    print("close serial communication")
    ser.close()
