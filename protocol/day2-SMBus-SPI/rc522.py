from RC522_wrapper import RC522
from time import sleep

reader = RC522()

try:
    while True:
        uid = reader.read_uid()
        if uid:
            print("태그 발견! UID:", *[int(i) for i in uid])
        sleep(1)

except KeyboardInterrupt:
    pass

finally:
    reader.close()
