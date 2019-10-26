import cv2
import numpy
import cProfile

# read image
img_name='../lenna512x512.png'
src = cv2.imread(img_name, cv2.IMREAD_UNCHANGED)
 
# apply guassian blur on src image
cProfile.run('dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)')

# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image