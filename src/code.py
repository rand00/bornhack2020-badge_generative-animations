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

generated_file = open("generated.txt", "r")

frame = 0
print('Show frame ' + str(frame) + ' = false')
# display.frame(frame, show=False)
# display2.frame(frame, show=False)

while True:
    generated_line = generated_file.readline()
    if generated_line.strip() == '':
        # print('Frame switch from ' + str(frame) + ' (show = true)')
        # display.frame(frame, show=True)
        # display2.frame(frame, show=True)
        # frame = 0 if frame else 1
        # print('Show frame ' + str(frame) + '= false')
        # display.frame(frame, show=False)
        # display2.frame(frame, show=False)
        display.fill(0)
        display2.fill(0)
        # continue
    else:
        splits = generated_line.split(' ')
        if len(splits) > 1:
            display_choice = int(splits[0])
            x = int(splits[1])
            y = int(splits[2])
            power = int(splits[3])
            chosen_display = display if display_choice == 0 else display2
            chosen_display.pixel(x, y, power)
        else:
            #print('delay = \'' + generated_line.strip() + '\'')
            delay = float(generated_line.strip())
            print('delay = \'' + str(delay) + '\'')
            time.sleep(delay)

            

