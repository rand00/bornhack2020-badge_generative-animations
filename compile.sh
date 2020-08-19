#! /bin/bash

ocamlbuild -use-ocamlfind generative.native
env time ./generative.native > generated/generated.txt


