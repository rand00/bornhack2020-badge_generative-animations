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

# text_to_show = "BornHack 2020 - make clean"
 
# Create a framebuffer for our display
# buf = bytearray(64)  # 2 bytes tall x 32 wide = 64 bytes (9 bits is 2 bytes)
# fb = adafruit_framebuf.FrameBuffer(
#     buf, display.width*2, display.height, adafruit_framebuf.MVLSB
# )

generated_file = open("generated.txt", "r")

frame = 0  # start with frame 0
display.frame(frame, show=False)
display2.frame(frame, show=False)

while True:
    generated_line = generated_file.readline()
    if generated_line == '':
        display.frame(frame, show=True)
        display2.frame(frame, show=True)
        frame = 0 if frame else 1
        display.frame(frame, show=False)
        display2.frame(frame, show=False)
    else:
        splits = generated_line.split(' ')
        if splits.length > 1:
            display_choice = int(splits[0])
            x = int(splits[1])
            y = int(splits[2])
            power = int(splits[3])
            chosen_display = display if display_choice == 0 else display2
            chosen_display.pixel(x, y, power)
        else:
            delay = float(splits[0])
            time.sleep(delay)

            
        
