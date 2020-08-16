
(*goto howto overall 
  * generate python code
  * print all generated code to stdout 
  * pipe to generated/code.py
*)

let sp = Printf.sprintf

(* let w, h = 32, 9 *)
let w, h = 31, 9

let () =
  Random.self_init ();
  G_line_splitter.frames ~w ~h 
  |> Generate.code_py 
  |> print_endline
