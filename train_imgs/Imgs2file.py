# -*- coding: utf-8 -*-
# @Time    : 18-5-9 上午10:51
# @Author  : JeeShao
# @File    : Imgs2file.py

import os
import cv2


POSTIVE_DIR = 'circle\\pos\\'
NEGATIVE_DIR = 'circle\\bg\\'
INFO_FILENAME = 'circle\\info.dat'
BG_FILENAME = 'circle\\bg.txt'


this_dir = os.path.abspath(os.path.dirname(__file__))
postive_url = os.path.join(this_dir, POSTIVE_DIR)
negative_url = os.path.join(this_dir, NEGATIVE_DIR)


# create info.dat
dir_list = os.listdir(postive_url)
dir_list.sort(key=lambda x:int(x.split('.')[0]))
with open(os.path.join(this_dir, INFO_FILENAME), 'wb') as file:
    # for dir in dir_list:
    #    imgs = os.listdir(os.path.join(postive_url,dir))
    #    imgs.sort(key=lambda x:int(x.split('.')[0]))
       for img_name in dir_list:
          img_url = os.path.join(postive_url, img_name)
          img = cv2.imread(img_url)
          rows, cols = img.shape[:2]
          file.write((img_url + " 1 0 0 %s %s\n" % (cols, rows )).encode())


# create pos0.txt
img_list = os.listdir(negative_url)
img_list.sort(key=lambda x:int(x.split('.')[0]))
with open(os.path.join(this_dir, BG_FILENAME), 'wb') as file:
    for img_name in img_list:
        file.write((negative_url + img_name + '\n').encode())