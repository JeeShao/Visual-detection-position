#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:23
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : get_calibrate_imgs.py

import cv2
cap = cv2.VideoCapture(1)
path = './chessboard/'
i = 1
while True:
    ret ,img = cap.read()
    if ret:
        cv2.imshow("img",img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(10) & 0xff == ord('m'):
            cv2.imwrite(path+"%d.jpg"%i,img)
            print(i)
            i+=1