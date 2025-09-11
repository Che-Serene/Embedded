from smbus2 import SMBus
from time import sleep

MPU_ADDR = 0x68
WHO_AM_I = 0x75
PWR_MGMT_1 = 0x6B

def _readword(adr) :
    h = bus.read_byte_data(MPU_ADDR, adr)
    l = bus.read_byte_data(MPU_ADDR, adr+1)
    ret = h<<8|l
    if ret & 0x8000 :
        ret -= 0x10000
    return ret


with SMBus(1) as bus :


    # 디바이스 리셋
    bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)


    # 센서 ID -> MPU6050 센서의 고유 식별 번호, 상태 확인
    ret = bus.read_byte_data(MPU_ADDR, WHO_AM_I)
    print(hex(ret))


    # 온도
    print(f"temperature : {round(int(_readword(0x41))/340+36.53, 2)}")


    # 가속도
    print("x  y  z   accelerometer")
    for _ in range(10) :
        
        acc_x = round(int(_readword(0x3b))/16384, 2)
        acc_y = round(int(_readword(0x3d))/16384, 2)
        acc_z = round(int(_readword(0x3f))/16384, 2)

        print(f"ACC | x : {acc_x} y : {acc_y} z : {acc_z}")
        sleep(0.5)