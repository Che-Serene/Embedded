import serial
import time

ser = serial.Serial("/dev/ttyAMA10", baudrate=115200, timeout=0.1)

for i in range(1, 11) :
    msg = f"Hello World! {i}\n"

    ser.write(msg.encode())
    time.sleep(1)
ser.close()