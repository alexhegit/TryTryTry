import cv2
import numpy
import cProfile
import time

# read image
img_name='./lenna512x512.png'
src = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)

# apply guassian blur on src image
guss = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)
blur = cv2.blur(src,(5,5))
med = cv2.medianBlur(src, 5)

# display input and output image
#cv2.imshow("Gaussian Smoothing",numpy.hstack((src, guss, blur, med)))
#cv2.waitKey(0) # waits until a key is pressed
#cv2.destroyAllWindows() # destroys the window showing image

print("cv2 version:", cv2.__version__)
