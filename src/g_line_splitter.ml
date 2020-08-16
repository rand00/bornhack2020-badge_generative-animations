
let frames ~w ~h =
  let pixels =
    Array.init w (fun x -> Array.init h (fun y ->
      if
        (* (x+y) mod 5 = 0 *) (*doesn't work together with frame 1*)
           (x+y) mod 9 = 0
        (* && x mod 9 = 0 *)
      then
        20
      else 0
    ))
  in
  let delay = 0.5 in
  let frame0 = Frame.{ pixels; delay } in
  let pixels =
    Array.init w (fun x -> Array.init h (fun y ->
      if
        (* (x+y+1) mod 5 = 0 *) (*doesn't work together with frame 0*)
           (x+y+1) mod 13 = 0
        (* && x mod 9 = 0 *)
      then
        20
      else 0
    ))
  in
  let delay = 30.0 in
  let frame1 = Frame.{ pixels; delay } in
  [
    frame0;
    frame1;
  ]
