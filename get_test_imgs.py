#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 15:31
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : get_test_imgs.py
import cv2

i = 20
path = './test_imgs/'
cap = cv2.VideoCapture(1)
cv2.namedWindow("img")
# cv2.resizeWindow('img', 40, 30)

while True:
    ret, img = cap.read()
    if ret:
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray = cv2.normalize(gray)
        cv2.imshow("img", img)
        if cv2.waitKey(10) & 0xff == ord('m'):
            cv2.imwrite(path+'%d.jpg'%i,img)
            print(i)
            i += 1