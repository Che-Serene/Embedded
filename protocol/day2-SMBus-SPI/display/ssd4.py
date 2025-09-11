import board, busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageOps
import datetime
from time import sleep
import math

SSD_ADDR = 0x3c
WIDTH = 72
HEIGHT = 40
MARGIN = 3

# I2C 및 OLED 초기화
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=SSD_ADDR)

oled.fill(0)
oled.show()

# 초기 위치 및 각도 설정
x_pos = 36
y_pos = 20
angle = 0
rotation_angle = 0  # 회전용 별도 각도
angle_inc = 10      # 이동 방향 변경 각도
rotation_inc = 15   # 회전 각도 증가량 (빠른 회전)

# 이동 속도
move_speed = 5

def dr_clock_spinning(xpos0, ypos0, spin_angle):
    time_str = datetime.datetime.now().strftime('%H:%M')
    img = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), time_str)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 위치 경계 체크
    xpos0 = max(MARGIN, min(xpos0, oled.width - text_width - MARGIN))
    ypos0 = max(MARGIN, min(ypos0, oled.height - text_height - MARGIN))

    # 텍스트 그리기
    draw.text((xpos0, ypos0), time_str, fill=255)

    # 이미지를 지속적으로 회전 (중앙 기준)
    img = img.rotate(spin_angle, center=(WIDTH//2, HEIGHT//2), fillcolor=0)

    oled.image(img)

while True:
    # 텍스트 크기 미리 계산 (충돌 감지용)
    img_tmp = Image.new("1", (WIDTH, HEIGHT))
    draw_tmp = ImageDraw.Draw(img_tmp)
    time_str_tmp = datetime.datetime.now().strftime('%H:%M')
    bbox_tmp = draw_tmp.textbbox((0, 0), time_str_tmp)
    text_w = bbox_tmp[2] - bbox_tmp[0]
    text_h = bbox_tmp[3] - bbox_tmp[1]

    # 이동 벡터 계산 (현재 각도 기준)
    rad = math.radians(angle)
    dx = move_speed * math.cos(rad)
    dy = move_speed * math.sin(rad)

    # 새로운 위치 계산
    new_x = x_pos + dx
    new_y = y_pos + dy

    # 좌우 경계 충돌 체크
    if new_x >= oled.width - text_w - MARGIN or new_x <= MARGIN:
        # X축 반전
        angle = 180 - angle
        if angle < 0:
            angle += 360
        elif angle >= 360:
            angle -= 360

    # 상하 경계 충돌 체크
    if new_y >= oled.height - text_h - MARGIN or new_y <= MARGIN:
        # Y축 반전
        angle = 360 - angle
        if angle < 0:
            angle += 360
        elif angle >= 360:
            angle -= 360

    # 위치 업데이트
    rad = math.radians(angle)
    x_pos += move_speed * math.cos(rad)
    y_pos += move_speed * math.sin(rad)

    # 경계 내 유지
    x_pos = max(MARGIN, min(x_pos, oled.width - text_w - MARGIN))
    y_pos = max(MARGIN, min(y_pos, oled.height - text_h - MARGIN))

    # **지속적인 회전 각도 증가** (계속 빙글빙글)
    rotation_angle += rotation_inc
    if rotation_angle >= 360:
        rotation_angle -= 360

    # 회전하면서 시계 표시
    dr_clock_spinning(x_pos, y_pos, rotation_angle)
    oled.show()
    sleep(0.01)  # 갱신 속도 조절
