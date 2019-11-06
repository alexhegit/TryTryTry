#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Oct  6 19:05:15 2019

@author: alexhe (heye_dev@163.com)

"""

"""
A example of Multi-thread
"""
import numpy as np
import os
import cv2
import time
import timeit
import threading
import sys



def iTask(cmd, id):
    print("Thread ID: %d" %id)
    os.system(cmd)


def main(argv):

    threadAll = []
    threadnum = int(argv[1])
    cmd = "ls /tmp"

    print("Input thread number is %d" %threadnum)

    time1 = time.time()

    for i in range(int(threadnum)):
        t1 = threading.Thread(target=iTask, args=(cmd, i))
        threadAll.append(t1)
        t1.start()
    for x in threadAll:
        x.join()

    time2 = time.time()


    totalfiles = 270*threadnum
    timetotal = time2 - time1
    fps = float(totalfiles / timetotal)
    print("%.2f FPS" %fps)
    print("Total Files %d" %(totalfiles))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please input thread number.")
    else :
        main(sys.argv)
