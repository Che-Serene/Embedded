import serial
import time

ser = serial.Serial("/dev/ttyAMA10", baudrate=115200, timeout=0.1)

msg = input()

ser.write(msg.encode())
time.sleep(0.2)
ret = ser.readline().decode()
print(ret)

ser.close()