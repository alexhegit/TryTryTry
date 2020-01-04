import numpy as np
import os
import cv2
import time
import timeit
#import threading
import multiprocessing as mp
import sys

FPATH = "/tmp/cap"

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

def showVideoInfo(cap):
    try:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cap.get(cv2.CAP_PROP_FOURCC)
        #count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        ret, firstframe = cap.read()
        if ret:
            print("Current Settings:")
            print("FPS: %.2f" % fps)
            print("FOURCC: %s" %(decode_fourcc(fourcc)))
            #print("COUNT: %.2f" % count)
            print("WIDTH: %d" % size[0])
            print("HEIGHT: %d" % size[1])
            return cap, fps, size, firstframe
        else:
            print("Video can not read!")
    except:
        "Error in showVideoInfo"

def setVideoInfo(cap, fps, width, height):
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    #fourcc = cv2.CV_FOURCC('M','J','P','G')
    print("set fourcc, MJPG(1196444237): %d" %(fourcc))
    cap.set(cv2.CAP_PROP_FOURCC, fourcc)
    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def putVideoFrame(cap, qf):
    while (True):
        ret, frame = cap.read()
        #cv2.imshow("preview", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rotate_frame = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("rotate", rotate_frame)
        qf.put(rotate_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            qf.put(None)
            break
    print("Quit putVideoFrame")
    #print(" Producer: Lost Frame Queue Size: %d" %(qf.qsize()))

def initCamera(cap, fps):
    showVideoInfo(cap)
    setVideoInfo(cap, fps, 640, 480)
    showVideoInfo(cap)

def main(argv):
    vid = int(argv[1])
    print("Open /dev/video%d" %vid)
    #os.path.join("/dev/video", vid)
    #cap = cv2.VideoCapture("/dev/video"+vid)
    cap = cv2.VideoCapture(vid)
    if not (cap.isOpened()):
        print("Could not open camera!")

    fps = 120
    initCamera(cap, fps)

    count = 0
    t1 = time.time()
    while(True):
        #count = (count + 1) % fps
        count += 1
        ret, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('preview', frame)
        #cv2.imwrite(FPATH + str(vid) + str(count) + '.jpg', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    t2 = time.time()
    t = t2 - t1
    fps = count / t
    print("Time used: %d seconds, Frames: %d, FPS: %d" %(t, count,fps))

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please input video id")
    else:
        main(sys.argv)
