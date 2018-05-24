#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 18:27
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : copy_imgs.py
import os,shutil

bg = './bg0/'
pos = './pos/'

for i in  range(1,801):
    shutil.copy(pos+"%d.jpg"%i,pos+"%d.jpg"%(i+800))