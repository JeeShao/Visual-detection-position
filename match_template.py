#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/17 15:01
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : match_template.py
import cv2
import numpy as np
cap = cv2.VideoCapture(1)
template_h = cv2.imread('template_imgs/square_h.png', 0)
template_v = cv2.imread('template_imgs/square_v.png', 0)

threshold = 0.7
while True:
    ret, img = cap.read()
    # img = cv2.imread('./test_imgs/20.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    h, w = template_h.shape[:2]  # rows->h, cols->w
    # 相关系数匹配方法：cv2.TM_CCOEFF
    res = cv2.matchTemplate(gray, template_h, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    loc = np.where(res >= threshold)
    if len(loc[0]):
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            break
    else:
        h, w = template_v.shape[:2]  # rows->h, cols->w
        # 相关系数匹配方法：cv2.TM_CCOEFF
        res = cv2.matchTemplate(gray, template_v, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)
            break
    # left_top = max_loc  # 左上角
    # right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    # cv2.rectangle(img, left_top, right_bottom, (0,0,255), 2)  # 画出矩形位置
    cv2.imshow("res",img)
    cv2.waitKey(10)
cv2.destroyAllWindows()