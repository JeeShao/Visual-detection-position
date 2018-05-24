#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 16:19
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : demo.py
import cv2
import numpy as np

# mtx = np.array([[841.27408053 ,  0.     ,    387.48419207],[  0.     ,    847.30374135 ,233.05342913],
#  [  0.      ,     0.    ,       1.        ]])
# dist = np.array([[-1.07171130e+00,  1.28041492e+00 , 2.89159150e-03 ,-7.39445741e-02,-4.16619752e+00]])
# img = cv2.imread('./chessboard/15.jpg')
# h,  w = img.shape[:2]
# newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
#
# # undistort
# dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# # mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
# # dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
# # crop the image
# x,y,w,h = roi
# dst = dst[y:y+h, x:x+w]
# cv2.imwrite('./calibresult.jpg',dst)

img = cv2.imread("./train_imgs/circle_boxs0/35.jpg",0)
cv2.normalize(img,img)
cv2.imshow("a",img)
cv2.waitKey(0)