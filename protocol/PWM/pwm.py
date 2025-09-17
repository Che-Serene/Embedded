from time import sleep
from gpiozero import Device, PWMOutputDevice
from gpiozero.pins.lgpio import LGPIOFactory

Device.pin_factory = LGPIOFactory()
pwm = PWMOutputDevice(18, frequency=1000)

try :
    pwm.value=1.0
    down_flag = False
    while True :
        if pwm.value >= 1:
            down_flag = True
        if pwm.value <= 0:
            down_flag = False

        if down_flag is True:
            pwm.value-=0.1
        if down_flag is False:
            pwm.value+=0.1

        print(f"{pwm.value*100}%")
        sleep(0.1)
        
finally :
    pwm.off()