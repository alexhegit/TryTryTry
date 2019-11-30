#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Author: He Ye (Alex)
# Date: 2019-11-13

import argparse
import cv2
import time
from multiprocessing import Process, Queue

VDEV = "/dev/video0"

def showVideoInfo(vhandle):
    try:
        fps = vhandle.get(cv2.CAP_PROP_FPS)
        #count = vhandle.get(cv2.CAP_PROP_FRAME_COUNT)
        size = (int(vhandle.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(vhandle.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        ret, firstframe = vhandle.read()
        if ret:
            print("FPS: %.2f" % fps)
            #print("COUNT: %.2f" % count)
            print("WIDTH: %d" % size[0])
            print("HEIGHT: %d" % size[1])
            return vhandle, fps, size, firstframe
        else:
            print("Video can not read!")
    except:
        "Error in showVideoInfo"

def setVideoInfo(vhandle, fps, width, height):
    try:
        vhandle.set(cv2.CAP_PROP_FPS, fps)
    except:
        "Error in setVideoInfo"

def consumer(qf, id):
    print("Consumer %d start" %(id))
    while True:
        if qf.empty():
            continue
        #print("Consumer %d, Frame Queue Size: %d" %(id, qf.qsize()))
        frame = qf.get()
        if frame is None:
            qf.put(None)
            break
        #print("- Consumer %d, Frame Queue Size: %d" %(id, qf.qsize()))
        cv2.imshow(str(id), frame)
        cv2.waitKey(1)
        #if cv2.waitKey(1) & 0xFF == ord('q'): break
    print("Consumer %d quit" %(id))

def producer(cap, qf):
    while (True):
        ret, frame = cap.read()
        cv2.imshow("preview", frame)
        rotate_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("rotate", rotate_frame)
        qf.put(rotate_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Producer sent stop signal")
            qf.put(None)
            break
    print("Quit producer, Frame Queue Size: %d" %(qf.qsize()))

def main(args):
    vdev = args.vdev
    thread_number = args.consumers
    try:
        cap = cv2.VideoCapture(vdev)
    except:
        "Failed to open" + str(vdev)

    showVideoInfo(cap)

    qf = Queue(maxsize = 0)
    thread_list = []

    pt = Process(target = producer, args = (cap, qf,))
    thread_list.append(pt)
    pt.start()

    for i in range(thread_number):
        ct = Process(target = consumer, args = (qf, i, ))
        thread_list.append(ct)
        ct.start()


    print("Process numbers = %d" %(len(thread_list)))
    for t in thread_list:
        t.join()

    print("Finished Join")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--nc", default=2, dest="consumers", help="number of consumer", type=int)
    parser.add_argument("--vdev", default=0, dest="vdev", help="video device id (/dev/videoX)", type=int)

    args = parser.parse_args()
    main(args)
