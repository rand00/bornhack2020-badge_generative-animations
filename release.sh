#! /bin/bash

sudo mount /mnt/bornhack_badge

cp src/code.py /tmp/
cp generated/generated.txt /tmp/

sudo cp /tmp/code.py /mnt/bornhack_badge/
sudo cp /tmp/generated.txt /mnt/bornhack_badge/

sudo umount /mnt/bornhack_badge



