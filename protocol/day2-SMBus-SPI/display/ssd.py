import board, busio
import adafruit_ssd1306
from PIL import Image
from time import sleep
import os

SSD_ADDR = 0x3c
WIDTH = 72
HEIGHT = 40

chars = os.listdir('characters')


i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=SSD_ADDR)

oled.fill(0)
oled.show()
while True :
    for ch in chars :
        image = Image.open('characters/'+ch).resize((WIDTH,HEIGHT)).convert("1")
        oled.image(image)
        oled.show()
        sleep(5)