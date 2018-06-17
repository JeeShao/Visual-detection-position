#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 12:33
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : detection.py

import numpy as np
import cv2

circle_cascade = cv2.CascadeClassifier('./classifier/circle/cascade.xml')
square_cascade = cv2.CascadeClassifier('./classifier/square/cascade.xml')
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



img = cv2.imread('./test_imgs/6.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.equalizeHist(gray)
img_rz = cv2.resize(gray,(gray.shape[1]//scale,gray.shape[0]//scale))

cir_position ,squ_position= [], []
#删除重复包括的框
# ret,img = cap.read()
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cir_targets = circle_cascade.detectMultiScale(img_rz, 1.1, 50)
squ_targets = square_cascade.detectMultiScale(img_rz, 1.1, 50)

def trim_rectangle(targets):
    tag = False
    target = []
    for i in range(0,len(targets)):
        for (x0, y0, w0, h0) in targets:
            if  targets[i][0]< x0 and targets[i][1] < y0 and targets[i][2] >= x0-targets[i][0]+w0 and targets[i][3] >= y0-targets[i][1]+h0:
                tag = False
                break
            target.append(targets[i])
    return target



for (x,y,w,h) in trim_rectangle(cir_targets):
    cir_position.append([x*scale+w*scale//2,y*scale+h*scale//2])
    cv2.rectangle(img,(x*scale, y*scale),((x+w)*scale, (y+h)*scale),(0,0,255),2) #圆-红色
print("圆坐标：",cir_position)
for (x, y, w, h) in trim_rectangle(squ_targets):
    squ_position.append([x*scale+w*scale//2,y*scale+h*scale//2])
    cv2.rectangle(img, (x * scale, y * scale), ((x + w) * scale, (y + h) * scale), (255, 0, 0), 2)  #矩形-蓝色
print("矩形坐标：",squ_position)

cv2.imshow('img', img)
cv2.waitKey(0)