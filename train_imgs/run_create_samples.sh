#!/usr/bin/env bash

OUTPUT=train.vec
INFO_FILE=info.dat
BG_FILE=bg.txt
NUM=200
WEIGHT=40
HIGHT=60

opencv_createsamples \
    -vec $OUTPUT \
    -info $INFO_FILE \
    -bg $BG_FILE \
    -num $NUM \
    -show \
    -w $WEIGHT \
    -h $HIGHT