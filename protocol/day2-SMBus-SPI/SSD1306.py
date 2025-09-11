import board, busio
import adafruit_ssd1306
from PIL import Image, ImageDraw

SSD_ADDR = 0x3c
WIDTH = 72
HEIGHT = 40

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=SSD_ADDR)

oled.fill(0)
oled.show()

img = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)
draw.text((0,0), "hi", fill=255)

oled.image(img)
oled.show()