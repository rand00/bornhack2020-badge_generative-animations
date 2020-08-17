
let pixels_aux ~w ~h ~p = 
  Array.init w (fun x -> Array.init h (fun y ->
    if p x y then 10 else 0
  ))

let number_one ~w ~h =
  let pixels = pixels_aux ~w ~h in
  let rec frames i n =
    if i = n then [] else 
      Frame.{
        pixels = pixels ~p:(fun x y -> (x+y+i) mod 11 = 0);
        delay = 0.0
      } :: frames (succ i) n
  in
  frames 0 100

let number_two ~w ~h =
  let pixels = pixels_aux ~w ~h in
  let rec frames i n =
    if i = n then [] else 
      Frame.{
        pixels = pixels ~p:(fun x y ->
          let x' = (float x +. float i) /. 2. in
          let half_h = float h /. 2. in
          let y' = sin x' *. half_h +. half_h in
          truncate y' = y
        );
        delay = 0.0
      } :: frames (succ i) n
  in
  frames 0 1000
