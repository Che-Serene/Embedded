from gpiozero import LED, Button, Buzzer
import time
from random import uniform

btn = Button(2, pull_up = True)
led = LED(14)
buz = Buzzer(15)

try :
    while True :
        time.sleep(uniform(0.6, 1.6))

        led.on()
        pressed = btn.wait_for_press(timeout = 0.5)
        led.off()

        if pressed :
            print('잡았다')
            buz.on()
            time.sleep(0.2)
            buz.off()
        else :
            print('놓쳤다,,')
except KeyboardInterrupt :
    pass
finally :
    led.off()
    buz.off()
    print("종료!")