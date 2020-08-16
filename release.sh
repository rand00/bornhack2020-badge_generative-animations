#! /bin/bash

sudo mount /mnt/bornhack_badge

./generative.native > generated/code.py
cp generated/code.py /tmp/
sudo cp /tmp/code.py /mnt/bornhack_badge/

sudo umount /mnt/bornhack_badge

