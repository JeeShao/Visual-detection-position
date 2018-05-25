#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 17:37
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : test_classifier.py

import numpy as np
import cv2

cascade = cv2.CascadeClassifier('./classifier/square/cascade.xml')
# eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
# cap = cv2.VideoCapture(1)
scale = 2  # 缩放比例

# while True:
#     ret , img = cap.read()
#     # img = cv2.imread('./test_imgs/1.jpg',0)
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     img_rz = cv2.resize(gray,(gray.shape[1]//scale,gray.shape[0]//scale))
#
#     # ret,img = cap.read()
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     targets = cascade.detectMultiScale(img_rz, 1.3, 50)
#     for (x,y,w,h) in targets:
#         cv2.rectangle(img,(x*scale, y*scale),((x+w)*scale, (y+h)*scale),(255,0,0),2)
#
#     cv2.imshow('img', img)
#     cv2.waitKey(10)



img = cv2.imread('./test_imgs/21.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rz = cv2.resize(gray,(gray.shape[1]//scale,gray.shape[0]//scale))

# ret,img = cap.read()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
targets = cascade.detectMultiScale(img_rz, 1.1, 5)
#删除重复包括的框
tag = False
target = []
for i in range(0,len(targets)):
    for (x0, y0, w0, h0) in targets:
        if  targets[i][0]< x0 and targets[i][1] < y0 and targets[i][2] >= x0-targets[i][0]+w0 and targets[i][3] >= y0-targets[i][1]+h0:
            tag = False
            break
        else:tag = True
    if tag:
        target.append(targets[i])



for (x,y,w,h) in target:
    cv2.rectangle(img,(x*scale, y*scale),((x+w)*scale, (y+h)*scale),(0,0,255),2)

    # cv2.rectangle(img_rz,(x, y),((x+w), (y+h)),(255, 0, 0),2)


cv2.imshow('img', img)
cv2.waitKey(0)