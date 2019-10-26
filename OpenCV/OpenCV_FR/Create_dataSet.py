#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:25:59 2019

@author: ai

Refer to:
    https://www.mkshell.com/face-recognition-dataset-generator/
"""

import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
sampleNum = 0
cam = cv2.VideoCapture(0)
Id = input('enter your id: ')
print("Current User ID", Id)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # incrementing sample number
        sampleNum = sampleNum + 1
        # saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User." + str(Id) + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('frame', img)
    # wait for 100 miliseconds
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum > 200:
        break

cam.release()
cv2.destroyAllWindows()
