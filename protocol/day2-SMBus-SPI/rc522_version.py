import spidev

spi = spidev.SpiDev()
spi.open(0,0)

spi.max_speed_hz = 1_000_000
spi.mode = 0

def read_reg(addr: int) -> int:
    # [7]: r/w, [6:1]: addr, 0111 1110, 1000 0000
    value = spi.xfer2([((addr<<1)&0x7e)|0x80, 0])
    return value[1]

version = read_reg(0x37)
print(f"ver: {hex(version)}")
spi.close()