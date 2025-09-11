import board, busio
import adafruit_ssd1306
from PIL import Image, ImageDraw
import datetime
from time import sleep

SSD_ADDR = 0x3c
WIDTH = 72
HEIGHT = 40

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=SSD_ADDR)

oled.fill(0)
oled.show()

while True :
    time = datetime.datetime.now()
    img = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.text((25,15), f"{time.hour}:{time.minute}", fill=255)

    oled.image(img)
    oled.show()
    sleep(30)