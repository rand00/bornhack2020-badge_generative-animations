
let sp = Printf.sprintf

let header = {|
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

|}

let choose_display ~x ~y ~w ~h =
  if x < w / 2 then `Display0 else `Display1

let pixels_aux ~f pixels =
  let w, h = Array.length pixels, Array.length pixels.(0) in
  let rec aux_xy x =
    if x >= w then [] else 
      let rec aux_y y =
        if y >= h then [] else
          let chosen_display = choose_display ~x ~y ~w ~h in
          let x, y = match chosen_display with
            | `Display0 -> x, y
            | `Display1 -> x - (w / 2), y
          in
          let f = f ~chosen_display in
          let power = pixels.(x).(y) in
          f ~x ~y ~power @ aux_y (succ y)
      in
      aux_y 0 @ aux_xy (succ x)
  in
  aux_xy 0

let display = function
  | `Display0 -> "display"
  | `Display1 -> "display2"

module Pixel = struct

  let turned_on ~chosen_display ~x ~y ~power =
    if power = 0 then [] else 
      [ sp "%s.pixel(%d, %d, %d)" (display chosen_display) x y power ]

  let turned_off ~chosen_display ~x ~y ~power =
    if power = 0 then [] else
      [ sp "%s.pixel(%d, %d, 0)" (display chosen_display) x y ]

end

let pixels pixels = pixels |> pixels_aux ~f:Pixel.turned_on

let pixels_reset pixels = pixels |> pixels_aux ~f:Pixel.turned_off

let frame frame = String.concat "\n" @@ List.flatten [
  [
    (* "display.frame(frame, show=False)";
     * "display2.frame(frame, show=False)"; *)

    (*goto remove debug*)
    "display.frame(frame, show=True)";
    "display2.frame(frame, show=True)";
    
    (*goto remove if doensn't magically get working*)
    (* "display.fill(0)"; 
     * "display2.fill(0)"; *)
  ];
  frame.Frame.pixels |> pixels;
  [
    (*goto reenable*)
    (* "display.frame(frame, show=True)";
     * "display2.frame(frame, show=True)"; *)
    sp "time.sleep(%f)" frame.Frame.delay;
  ];
  (*> goto get working if this kills it *)
  frame.Frame.pixels |> pixels_reset;
  (*goto reenable*)
  (* [ "frame = 0 if frame else 1" ]; *)
  [ "" ];
]

let code_py frames = String.concat "\n" [
  header;
  frames |> List.map frame |> String.concat "\n";
]

