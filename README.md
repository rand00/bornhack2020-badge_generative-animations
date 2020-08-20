# bornhack2020-badge generative-animations
Generative animations for the BornHack 2020 badge, pregenerated with OCaml. 

The primary animation-generator is the `G_line_splitter` module, where lines are spawned vertically or horizontally at random positions - ping-pong'ing between the borders. When lines spawn on top of existing crossing lines, lines are split at these points, and move in different directions. 

## Usage
* See `compile.sh` and `release.sh`. 
  * You might want to make changes to `release.sh` - e.g. choosing mount-directory, and maybe not needing the intermediary copy to `/tmp`. I got the most consistent badge-reloading by mounting and unmounting.
  * You need the binary `ocamlbuild` to build the code - no external dependencies
* To see python output from badge:
  * `sudo screen /dev/serial/by-id/usb-BornHack_Bornhack_Badge_FOO-if00 115200`
    * where you exchange the badge-device with your own 
