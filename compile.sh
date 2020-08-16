#! /bin/bash

ocamlbuild -use-ocamlfind generative.native
./generative.native > generated/generated.txt


