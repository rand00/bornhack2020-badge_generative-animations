
type power = int

type t = {
  pixels : power array array;
  delay : float;
}

let print frame =
  let w, h = Array.length frame.pixels, Array.length frame.pixels.(0) in
  for y = 0 to h - 1 do
    for x = 0 to w - 1 do
      Printf.printf "%2d " frame.pixels.(x).(y)
    done;
    print_newline ()
  done;
  print_newline ();
  print_newline ()
