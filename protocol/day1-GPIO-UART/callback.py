from gpiozero import Button
from signal import pause

btn = Button(2, pull_up = True)

def on_press() :
    print("pressed")

def on_release() :
    print("released")

btn.when_pressed = on_press
btn.when_released = on_release

pause()