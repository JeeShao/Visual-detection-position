#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 18:27
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : copy_imgs.py
import os,shutil

bg = './circle/bg/'
pos = './pos/'

for i in  range(1,2001):
    shutil.copy(bg+"%d.jpg"%i,bg+"%d.jpg"%(i+2000))