# Author: He Ye (Alex)
# Date: 2019-11-13

import cv2
#import copy
from threading import Thread
from queue import Queue
#from Queue import Queue

VDEV = "/dev/video0"

def showVideoInfo(cap):
    try:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cap.get(cv2.CAP_PROP_FOURCC)
        #count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        ret, firstframe = cap.read()
        if ret:
            print("FPS: %.2f" % fps)
            print("FOURCC: %s" % fourcc)
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
    print("set fourcc, MJPG: 1196444237")
    print(fourcc)
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

class ImgCap(Thread):
    def __init__(self, cap, queue_list, signal):
        Thread.__init__(self)
        self.cap = cap
        self.qlist = queue_list
        self.signal = signal
        self.frame_count = 0
    def run(self):
        while (True):
            for queue in self.qlist:
                ret, frame = self.cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                rotate_frame = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
                queue.put(rotate_frame)
                self.frame_count += 1
            if self.signal == "OFF":
                for queue in self.qlist:
                    queue.put(None)
                break
        print("Quit ImgCap")
    def terminate(self):
        print("ImgCap OFF")
        self.signal = "OFF"
    def count_frame(self):
        return self.frame_count