import spidev
from time import sleep
"""
25LC256 |  1  2  4  5   6   8
GPIO    |  8  9  G  10  11  V
"""


spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0 (CS0)
spi.max_speed_hz = 1000000  # 1MHz

# 25LC256 명령어
CMD_READ = 0x03     # Read data from memory array beginning at selected address
CMD_WRITE = 0x02    # Write data to memory beginning at selected address
CMD_WREN = 0x06     # Enable write operations

# Write Enable
spi.xfer2([CMD_WREN])
sleep(0.01)

# Write data (예: 0x55) to address 0x0000
addr = [0x00, 0x00]
data = [0x55]
spi.xfer2([CMD_WRITE] + addr + data)
sleep(0.01)

# Read data from address 0x0000
resp = spi.xfer2([CMD_READ] + addr + [0x00])
print("Read value:", hex(resp[-1]))

spi.close()
