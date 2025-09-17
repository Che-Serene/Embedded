from gpiozero import AngularServo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep


Device.pin_factory = LGPIOFactory()
servo =AngularServo(18, min_angle=0, max_angle=180,min_pulse_width=0.0005, max_pulse_width=0.0024)

try:
    angle = 0
    direct = 10
    while True:
        servo.angle = angle
        angle+=direct
        if angle>=180:
            direct *=-1
        if angle<=0:
            direct *= -1
        print(angle)
        sleep(1)

finally:
    servo.detach()