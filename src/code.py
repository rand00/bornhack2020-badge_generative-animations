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
#display.fill(0)
#display2.fill(1)
display.pixel(0, 0, 30)
# < goto make a lot of these, depending on display w and h
display2.pixel(0, 0, 30)
# < goto make a lot of these, depending on display w and h
display.frame(frame, show=True)
display2.frame(frame, show=True)
time.sleep(1)
#> setting pixel to zero again
display.pixel(0, 0, 0)
display2.pixel(0, 0, 0)
frame = 0 if frame else 1

display.frame(frame, show=False)
display2.frame(frame, show=False)
#display.fill(0)
#display2.fill(1)
display.pixel(0, 1, 30)
# < goto make a lot of these, depending on display w and h
display2.pixel(0, 1, 30)
# < goto make a lot of these, depending on display w and h
display.frame(frame, show=True)
display2.frame(frame, show=True)
time.sleep(1)
#> setting pixel to zero again
display.pixel(0, 1, 0)
display2.pixel(0, 1, 0)
frame = 0 if frame else 1

display.frame(frame, show=False)
display2.frame(frame, show=False)
#display.fill(0)
#display2.fill(1)
display.pixel(1, 0, 30)
# < goto make a lot of these, depending on display w and h
display2.pixel(1, 0, 30)
# < goto make a lot of these, depending on display w and h
display.frame(frame, show=True)
display2.frame(frame, show=True)
time.sleep(1)
#> setting pixel to zero again
display.pixel(1, 0, 0)
display2.pixel(1, 0, 0)
frame = 0 if frame else 1

display.frame(frame, show=False)
display2.frame(frame, show=False)
#display.fill(0)
#display2.fill(1)
display.pixel(1, 1, 30)
# < goto make a lot of these, depending on display w and h
display2.pixel(1, 1, 30)
# < goto make a lot of these, depending on display w and h
display.frame(frame, show=True)
display2.frame(frame, show=True)
time.sleep(1)
#> setting pixel to zero again
display.pixel(1, 1, 0)
display2.pixel(1, 1, 0)
frame = 0 if frame else 1


