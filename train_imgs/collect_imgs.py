#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 13:40
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : collect_imgs.py
import cv2
to  = './charger/'
src = './pos/'

for i in range(1,40):
    img = cv2.imread(src+"%d.jpg"%i,0)
    img = cv2.resize(img,(45,60))
    cv2.imwrite(to+"%d.jpg"%i,img)