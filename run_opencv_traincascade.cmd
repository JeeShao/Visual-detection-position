opencv_traincascade.exe -data classifier -vec train_imgs/train.vec -bg train_imgs/bg.txt -numPos 300 -numNeg 600 -numStages 10
-w 30 -h 30 -minHitRate 0.995 -maxFalseAlarmRate 0.5 -weightTrimRate 0.95 -maxDepth 1 -maxWeakCount 100 -stageType BOOST
-featureType HAAR -precalcValBufSize 1024 -precalcIdxBufSize 1024 -mode BASIC

实际准备的正样本数量（读入vec-file的正样本数） >= numPos + (numStage - 1) * numPos * (1 - minHitRate)