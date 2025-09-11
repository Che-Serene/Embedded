import board, busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageOps
import datetime
from time import sleep

SSD_ADDR = 0x3c
WIDTH = 72
HEIGHT = 40
MARGIN = 3

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=SSD_ADDR)

oled.fill(0)
oled.show()

x_pos = 36
y_pos = 20

x_inc = 4
y_inc = 4

mirror_flag = False  # 좌우 반전 토글 플래그

def dr_clock(xpos0, ypos0):
    global mirror_flag
    time_str = datetime.datetime.now().strftime('%H:%M:%S')
    img = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    text_bbox = draw.textbbox((xpos0, ypos0), time_str)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    xpos0 = max(MARGIN, min(xpos0, oled.width - text_width - MARGIN))
    ypos0 = max(MARGIN, min(ypos0, oled.height - text_height - MARGIN))

    draw.text((xpos0, ypos0), time_str, fill=255)

    if mirror_flag:
        img = ImageOps.mirror(img)

    oled.image(img)

while True:
    # 텍스트 크기 미리 계산
    img_tmp = Image.new("1", (WIDTH, HEIGHT))
    draw_tmp = ImageDraw.Draw(img_tmp)
    time_str_tmp = datetime.datetime.now().strftime('%H:%M')
    bbox_tmp = draw_tmp.textbbox((0, 0), time_str_tmp)
    text_w = bbox_tmp[2] - bbox_tmp[0]
    text_h = bbox_tmp[3] - bbox_tmp[1]

    # 좌우 바운스 체크
    if x_pos >= oled.width - text_w - MARGIN:
        x_inc = -x_inc
        mirror_flag = not mirror_flag  # 좌우 충돌 시 반전 토글
    elif x_pos <= MARGIN:
        x_inc = -x_inc
        mirror_flag = not mirror_flag  # 좌우 충돌 시 반전 토글

    # 상하 바운스 체크
    if y_pos >= oled.height - text_h - MARGIN:
        y_inc = -y_inc
    elif y_pos <= MARGIN:
        y_inc = -y_inc

    x_pos += x_inc
    y_pos += y_inc

    dr_clock(x_pos, y_pos)
    oled.show()

