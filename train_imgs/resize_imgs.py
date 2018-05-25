#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 17:04
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : resize_imgs.py
import cv2,os

path = './square/pos1/'
to ='./pos0/'

l = os.listdir(path)
l.sort(key=lambda x:int(x.split('.')[0]))
for i in range(1,1001):
    img = cv2.imread(os.path.join(path,'%d.jpg'%i),0)
    img = cv2.resize(img,(30,30))
    cv2.imwrite(os.path.join('./square/pos/','%d.jpg'%i),img)