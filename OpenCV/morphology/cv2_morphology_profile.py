#!/usr/bin/env python

import cv2
import time, timeit
from timeit import default_timer as timer

print("cv2 version:", cv2.__version__)

IMG = './292.bmp'
img = cv2.imread(IMG)
print('Image Dimensions :', img.shape)

g_img = cv2.imread(IMG, cv2.IMREAD_GRAYSCALE)
print('Image Dimensions :', g_img.shape)


t1 = timer()
mop_img = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = timer()
print("Time Used", t2 - t1, "second")


t1 = time.time()
mop_img = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = time.time()
print("Time Used", t2 - t1, "second")

'''
t1 = time.process_time()
mop_img = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = time.process_time()
print("Time Used", t2 - t1, "second")
'''

ret = cv2.imwrite("./gray_img.bmp", g_img)
if ret:
    print("Success save gray_img.bmp")

ret = cv2.imwrite("./mop_img.bmp", mop_img)
if ret:
    print("Success save morphology mop_img.bmp")
