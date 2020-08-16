
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


display.frame(frame, show=False)
display2.frame(frame, show=False)
display.pixel(0, 0, 20)
display.pixel(0, 5, 20)
display.pixel(1, 4, 20)
display.pixel(2, 3, 20)
display.pixel(2, 8, 20)
display.pixel(3, 2, 20)
display.pixel(3, 7, 20)
display.pixel(4, 1, 20)
display.pixel(4, 6, 20)
display.pixel(5, 0, 20)
display.pixel(5, 5, 20)
display.pixel(6, 4, 20)
display.pixel(7, 3, 20)
display.pixel(7, 8, 20)
display.pixel(8, 2, 20)
display.pixel(8, 7, 20)
display.pixel(9, 1, 20)
display.pixel(9, 6, 20)
display.pixel(10, 0, 20)
display.pixel(10, 5, 20)
display.pixel(11, 4, 20)
display.pixel(12, 3, 20)
display.pixel(12, 8, 20)
display.pixel(13, 2, 20)
display.pixel(13, 7, 20)
display.pixel(14, 1, 20)
display.pixel(14, 6, 20)
display2.pixel(0, 0, 20)
display2.pixel(0, 5, 20)
display2.pixel(1, 4, 20)
display2.pixel(2, 3, 20)
display2.pixel(2, 8, 20)
display2.pixel(3, 2, 20)
display2.pixel(3, 7, 20)
display2.pixel(4, 1, 20)
display2.pixel(4, 6, 20)
display2.pixel(5, 0, 20)
display2.pixel(5, 5, 20)
display2.pixel(6, 4, 20)
display2.pixel(7, 3, 20)
display2.pixel(7, 8, 20)
display2.pixel(8, 2, 20)
display2.pixel(8, 7, 20)
display2.pixel(9, 1, 20)
display2.pixel(9, 6, 20)
display2.pixel(10, 0, 20)
display2.pixel(10, 5, 20)
display2.pixel(11, 4, 20)
display2.pixel(12, 3, 20)
display2.pixel(12, 8, 20)
display2.pixel(13, 2, 20)
display2.pixel(13, 7, 20)
display2.pixel(14, 1, 20)
display2.pixel(14, 6, 20)
display2.pixel(15, 0, 20)
display2.pixel(15, 5, 20)
display.frame(frame, show=True)
display2.frame(frame, show=True)
time.sleep(0.500000)
display.pixel(0, 0, 0)
display.pixel(0, 5, 0)
display.pixel(1, 4, 0)
display.pixel(2, 3, 0)
display.pixel(2, 8, 0)
display.pixel(3, 2, 0)
display.pixel(3, 7, 0)
display.pixel(4, 1, 0)
display.pixel(4, 6, 0)
display.pixel(5, 0, 0)
display.pixel(5, 5, 0)
display.pixel(6, 4, 0)
display.pixel(7, 3, 0)
display.pixel(7, 8, 0)
display.pixel(8, 2, 0)
display.pixel(8, 7, 0)
display.pixel(9, 1, 0)
display.pixel(9, 6, 0)
display.pixel(10, 0, 0)
display.pixel(10, 5, 0)
display.pixel(11, 4, 0)
display.pixel(12, 3, 0)
display.pixel(12, 8, 0)
display.pixel(13, 2, 0)
display.pixel(13, 7, 0)
display.pixel(14, 1, 0)
display.pixel(14, 6, 0)
display2.pixel(0, 0, 0)
display2.pixel(0, 5, 0)
display2.pixel(1, 4, 0)
display2.pixel(2, 3, 0)
display2.pixel(2, 8, 0)
display2.pixel(3, 2, 0)
display2.pixel(3, 7, 0)
display2.pixel(4, 1, 0)
display2.pixel(4, 6, 0)
display2.pixel(5, 0, 0)
display2.pixel(5, 5, 0)
display2.pixel(6, 4, 0)
display2.pixel(7, 3, 0)
display2.pixel(7, 8, 0)
display2.pixel(8, 2, 0)
display2.pixel(8, 7, 0)
display2.pixel(9, 1, 0)
display2.pixel(9, 6, 0)
display2.pixel(10, 0, 0)
display2.pixel(10, 5, 0)
display2.pixel(11, 4, 0)
display2.pixel(12, 3, 0)
display2.pixel(12, 8, 0)
display2.pixel(13, 2, 0)
display2.pixel(13, 7, 0)
display2.pixel(14, 1, 0)
display2.pixel(14, 6, 0)
display2.pixel(15, 0, 0)
display2.pixel(15, 5, 0)
frame = 0 if frame else 1

