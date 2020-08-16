
let sp = Printf.sprintf

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
  | `Display0 -> 0
  | `Display1 -> 1

module Pixel = struct

  let turned_on ~chosen_display ~x ~y ~power =
    if power = 0 then [] else 
      [ sp "%d %d %d %d" (display chosen_display) x y power ]

  let turned_off ~chosen_display ~x ~y ~power =
    if power = 0 then [] else
      [ sp "%d %d %d 0" (display chosen_display) x y ]

end

let pixels pixels = pixels |> pixels_aux ~f:Pixel.turned_on

let pixels_reset pixels = pixels |> pixels_aux ~f:Pixel.turned_off

let frame frame = String.concat "\n" @@ List.flatten [
  frame.Frame.pixels |> pixels;
  [ sp "%.2f" frame.Frame.delay ];
  frame.Frame.pixels |> pixels_reset;
]

let commands frames = 
  frames
  |> List.map frame
  |> String.concat "\n\n";


