#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 17:04
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : resize_imgs.py
import cv2,os

path = './bg0/'
to ='./circle_boxs0/'

l = os.listdir(path)
l.sort(key=lambda x:int(x.split('.')[0]))
for i in range(1001,1501):
    img = cv2.imread(os.path.join(path,'%d.jpg'%i),0)
    img = cv2.resize(img,(40,40))
    cv2.imwrite(os.path.join('./bg/','%d.jpg'%i),img)