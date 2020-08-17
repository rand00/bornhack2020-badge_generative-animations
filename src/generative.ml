
let w, h = 32, 9

let () =
  Random.self_init ();
  (* G_line_splitter.frames ~w ~h  *)
  (* G_mixed_play.number_one ~w ~h  *)
  G_mixed_play.number_two ~w ~h 
  |> Generate.commands
  |> print_endline
