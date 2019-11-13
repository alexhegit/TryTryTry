#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Author: He Ye (Alex)
# Date: 2019-11-13

import cv2

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


def main():
    try:
        cap = cv2.VideoCapture(VDEV)
    except:
        "Failed to open" + VDEV

    showVideoInfo(cap)

    while (True):
        ret, frame = cap.read()
        cv2.imshow("preview", frame)
        rotate_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("rotate", rotate_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destoryAllWindows()


if __name__ == '__main__':
    main()
