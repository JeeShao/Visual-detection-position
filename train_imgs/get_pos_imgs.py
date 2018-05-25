#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 11:44
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : get_pos_imgs.py

import cv2

i = 401
path = './square/pos0/'
cap = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 40)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 30)
cv2.namedWindow("img")
# cv2.resizeWindow('img', 40, 30)

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray = cv2.normalize(gray)
        cv2.imshow("img", img)
        if cv2.waitKey(10) & 0xff == ord('m'):
            cv2.imwrite(path+'%d.jpg'%i,gray)
            print(i)
            i += 1