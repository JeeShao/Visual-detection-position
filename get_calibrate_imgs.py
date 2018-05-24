#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:23
# @Author  : Jee
# @Email   : jee_shao@163.com
# @File    : get_calibrate_imgs.py

import cv2
import numpy as np

mtx = np.array([[1.01067049e+03, 0.00000000e+00 ,4.25658858e+02], [0.00000000e+00 ,1.03918088e+03 ,2.30468360e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist = np.array([[-1.48376195e+00 ,-2.72491765e+00 , 9.05602739e-03, -1.54136710e-01, 2.09607881e+01]])

img = cv2.imread('./test_imgs/10002.jpg')

h,  w = img.shape[:2]

newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
# dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('./calibresult.jpg',dst)
