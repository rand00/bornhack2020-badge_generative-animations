
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import busio
import adafruit_framebuf
import adafruit_is31fl3731

# configure I2C
i2c = busio.I2C(board.SCL, board.SDA)

# turn on LED drivers
sdb = DigitalInOut(board.SDB)
sdb.direction = Direction.OUTPUT
sdb.value = True

# set up the two LED drivers
display = adafruit_is31fl3731.Matrix(i2c, address=0x74)
display2 = adafruit_is31fl3731.Matrix(i2c, address=0x77)

text_to_show = "BornHack 2020 - make clean"

# Create a framebuffer for our display
buf = bytearray(64)  # 2 bytes tall x 32 wide = 64 bytes (9 bits is 2 bytes)
fb = adafruit_framebuf.FrameBuffer(
    buf, display.width*2, display.height, adafruit_framebuf.MVLSB
)

# > START CODE TO GENERATE

frame = 0  # start with frame 0


display.frame(frame, show=True)
display2.frame(frame, show=True)
display.pixel(0, 0, 20)
display.pixel(1, 8, 20)
display.pixel(2, 7, 20)
display.pixel(3, 6, 20)
display.pixel(4, 5, 20)
display.pixel(5, 4, 20)
display.pixel(6, 3, 20)
display.pixel(7, 2, 20)
display.pixel(8, 1, 20)
display.pixel(9, 0, 20)
display.pixel(10, 8, 20)
display.pixel(11, 7, 20)
display.pixel(12, 6, 20)
display.pixel(13, 5, 20)
display.pixel(14, 4, 20)
display2.pixel(0, 0, 20)
display2.pixel(1, 8, 20)
display2.pixel(2, 7, 20)
display2.pixel(3, 6, 20)
display2.pixel(4, 5, 20)
display2.pixel(5, 4, 20)
display2.pixel(6, 3, 20)
display2.pixel(7, 2, 20)
display2.pixel(8, 1, 20)
display2.pixel(9, 0, 20)
display2.pixel(10, 8, 20)
display2.pixel(11, 7, 20)
display2.pixel(12, 6, 20)
display2.pixel(13, 5, 20)
display2.pixel(14, 4, 20)
display2.pixel(15, 3, 20)
time.sleep(0.500000)
display.pixel(0, 0, 0)
display.pixel(1, 8, 0)
display.pixel(2, 7, 0)
display.pixel(3, 6, 0)
display.pixel(4, 5, 0)
display.pixel(5, 4, 0)
display.pixel(6, 3, 0)
display.pixel(7, 2, 0)
display.pixel(8, 1, 0)
display.pixel(9, 0, 0)
display.pixel(10, 8, 0)
display.pixel(11, 7, 0)
display.pixel(12, 6, 0)
display.pixel(13, 5, 0)
display.pixel(14, 4, 0)
display2.pixel(0, 0, 0)
display2.pixel(1, 8, 0)
display2.pixel(2, 7, 0)
display2.pixel(3, 6, 0)
display2.pixel(4, 5, 0)
display2.pixel(5, 4, 0)
display2.pixel(6, 3, 0)
display2.pixel(7, 2, 0)
display2.pixel(8, 1, 0)
display2.pixel(9, 0, 0)
display2.pixel(10, 8, 0)
display2.pixel(11, 7, 0)
display2.pixel(12, 6, 0)
display2.pixel(13, 5, 0)
display2.pixel(14, 4, 0)
display2.pixel(15, 3, 0)

display.frame(frame, show=True)
display2.frame(frame, show=True)
display.pixel(4, 8, 20)
display.pixel(5, 7, 20)
display.pixel(6, 6, 20)
display.pixel(7, 5, 20)
display.pixel(8, 4, 20)
display.pixel(9, 3, 20)
display.pixel(10, 2, 20)
display.pixel(11, 1, 20)
display.pixel(12, 0, 20)
display2.pixel(4, 8, 20)
display2.pixel(5, 7, 20)
display2.pixel(6, 6, 20)
display2.pixel(7, 5, 20)
display2.pixel(8, 4, 20)
display2.pixel(9, 3, 20)
display2.pixel(10, 2, 20)
display2.pixel(11, 1, 20)
display2.pixel(12, 0, 20)
time.sleep(30.000000)
display.pixel(4, 8, 0)
display.pixel(5, 7, 0)
display.pixel(6, 6, 0)
display.pixel(7, 5, 0)
display.pixel(8, 4, 0)
display.pixel(9, 3, 0)
display.pixel(10, 2, 0)
display.pixel(11, 1, 0)
display.pixel(12, 0, 0)
display2.pixel(4, 8, 0)
display2.pixel(5, 7, 0)
display2.pixel(6, 6, 0)
display2.pixel(7, 5, 0)
display2.pixel(8, 4, 0)
display2.pixel(9, 3, 0)
display2.pixel(10, 2, 0)
display2.pixel(11, 1, 0)
display2.pixel(12, 0, 0)

