from gpiozero import LED
import time
import random

green = LED(14)
blue = LED(15)
red = LED(18)

green.on()