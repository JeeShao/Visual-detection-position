#!/usr/bin/env bash

OUTPUT_FILE=classifier
VEC_FILE=train_imgs/train.vec
BG_FILE=train_imgs/bg.txt
NUM_POS=150
NUM_NEG=200
NUM_STAGE=5
VAL_BUFSIZE=1024
IDX_BUFSIZE=1024

STAGE_TYPE=BOOST
FEATURE_TYPE=HAAR
# FEATURE_TYPE=LBP
WEIGHT=27
HEIGHT=68

BT=GAB
MIN_HITRATE=0.995
MAX_FALSE_ALARM_RATE=0.05
WEIGHT_TRIM_RATE=0.95
MAX_DEPTH=1
MAX_WEAK_COUNT=100

MODE=BASIC


opencv_traincascade \
    -data $OUTPUT_FILE \
    -vec $VEC_FILE \
    -bg $BG_FILE \
    -numPos $NUM_POS \
    -numNeg $NUM_NEG \
    -numStages $NUM_STAGE \
    -precalcValBufSize $VAL_BUFSIZE \
    -precalcIdxBufSize $IDX_BUFSIZE \
    -stageType $STAGE_TYPE \
    -featureType $FEATURE_TYPE \
    -w $WEIGHT \
    -h $HEIGHT \
    -bt $BT \
    -minHitRate $MIN_HITRATE \
    -maxFalseAlarmRate $MAX_FALSE_ALARM_RATE \
    -weightTrimRate $WEIGHT_TRIM_RATE \
    -maxDepth $MAX_DEPTH \
    -maxWeakCount $MAX_WEAK_COUNT \
    -mode $MODE \
    # -baseFormatSave \