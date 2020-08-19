
module Board = struct

  type line = {
    pos : float;       (*range: [0; 1]*)
    cut_left : float;  (*range: [0; 1]*)
    cut_right : float; (*range: [0; 1]*)
    dimension : [ `Vertical | `Horizontal ];
    direction : [ `Up | `Down ];
    is_new : bool;
  }[@@deriving show]
  
  type t = line list
  [@@deriving show]
  
  let make () = []

  let overlaps l0 l1 =
    l0.pos > l1.cut_left &&
    l0.pos < l1.cut_right &&
    l1.pos > l0.cut_left &&
    l1.pos < l0.cut_right 

  let split_aux line pos =
    let l = { line with cut_right = pos; direction = `Up } in
    let r = { line with cut_left = pos; direction = `Down } in
    l, r 
  
  let split_line ~splitter line =
    if splitter.dimension = line.dimension then
      [ line ]
    else (
      if not (overlaps splitter line) then
        [ line ]
      else
        let line_l, line_r = split_aux line splitter.pos in
        [ line_l; line_r ]
    )
      
      
  (*spec;
    * every existing line should try to split new line
      * (folded over board) f : new_line -> existing_line -> new_line list (+ acc)
    * new line (still unsplit) should try to split every existing line 
      * (folded over board) f : existing_line -> new_line -> existing_line list (+ acc)
  *)
  let spawn_line board =
    let new_line = {
      pos = Random.float 1.;
      dimension = if Random.bool () then `Vertical else `Horizontal;
      direction = if Random.bool () then `Up else `Down;
      cut_left = 0.;
      cut_right = 1.;
      is_new = true;
    } in
    let board' =
      board |> List.fold_left (fun acc line ->
        split_line line ~splitter:new_line @ acc) [] in
    let new_segments =
      let init_segments = [ new_line ]
      in
      board |> List.fold_left (fun acc_segments line ->
        acc_segments |> List.fold_left (fun acc' segment ->
          let split_segments = segment |> split_line ~splitter:line in
          split_segments @ acc'
        ) []
      ) init_segments
    in
    (* Printf.printf "spawning line: %s\n%!" (show_line new_line); *)
    board' @ new_segments

  let line_speed_y = 1. /. 9. 
  let line_speed_x = 1. /. 32.
  
  let step_line line =
    let is_new = false in
    let line_speed = match line.dimension with
      | `Vertical -> line_speed_x
      | `Horizontal -> line_speed_y
    in
    match line.direction with
    | `Up ->
      let pos = line.pos +. line_speed in
      if pos > 1. then
        let direction = `Down
        and pos = 1. -. (pos -. 1.) in
        { line with direction; pos; is_new }
      else
        { line with pos; is_new }
    | `Down ->
      let pos = line.pos -. line_speed in
      if pos < 0. then
        let direction = `Up
        and pos = 1. -. (pos +. 1.) in 
        { line with direction; pos; is_new }
      else
        { line with pos; is_new }
  
  let step board = board |> List.map step_line

  let to_frame ~w ~h board =
    let pixels = Array.init w (fun _ -> Array.init h (fun _ -> 0)) in
    let restrict ~max_v float_v =
      float_v
      |> truncate
      |> min (max_v-1)
      |> max 0
    in
    board |> List.iter (fun line ->
      let power = if line.is_new then 30 else 2 in
      match line.dimension with
      | `Horizontal ->
        let x_from = line.cut_left *. float w |> restrict ~max_v:w in
        let x_to = line.cut_right *. float w |> restrict ~max_v:w in
        let y = line.pos *. float h |> restrict ~max_v:h in
        (* Printf.printf "to_frame: writing to %d pixels\n%!" (x_to - x_from); *)
        for x = x_from to x_to do
          (* Printf.printf "  -- write pixel %d,%d = %d\n%!" x y 10; *)
          pixels.(x).(y) <- power
        done
      | `Vertical ->
        let y_from = line.cut_left *. float h |> restrict ~max_v:h in
        let y_to = line.cut_right *. float h |> restrict ~max_v:h in
        let x = line.pos *. float w |> restrict ~max_v:w in
        (* Printf.printf "to_frame: writing to %d pixels\n%!" (y_to - y_from); *)
        for y = y_from to y_to do
          (* Printf.printf "  -- write pixel %d,%d = %d\n%!" x y 10; *)
          pixels.(x).(y) <- power
        done
    );
    Frame.{ pixels; delay = 0.0 }

end

module Simulate = struct

  let spawn_line ~i board =
    if i mod (Random.int (i+1) + 5) = 0 then 
      board |> Board.spawn_line
    else
      board

end

let frames ~w ~h =
  let n_simulations = 400 in
  let rec simulate i board =
    (* Printf.printf "frame %d\n%!" i; *)
    if i >= n_simulations then [] else (
      let board = 
        board
        |> Board.step
        |> Simulate.spawn_line ~i
      in
      let frame = board |> Board.to_frame ~w ~h
      in
      frame :: simulate (succ i) board 
    )
      
  in
  simulate 0 (Board.make ())
  
