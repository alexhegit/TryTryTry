# OpenCV blur Performance Test



## Example Code

```python
(tf) ai@7730:~/Try/opencv/blur$ cat AllBlur_performance.py 
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

```

**Test Script:**

```
(tf) ai@7730:~/Try/opencv/blur$ cat cProfile.sh 
#conda activate tf1
python3 -m cProfile AllBlur.py | grep -i blur
python3 -V
python3 -c 'import cv2; print("cv2 version:", cv2.__version__)'
```



## TEST

### X86 (DELL 7730 Precision)

| CPU                                     | GPU              |      |
| --------------------------------------- | ---------------- | ---- |
| Intel(R) Xeon(R) E-2176M  CPU @ 2.70GHz | Nvidia P5200 GPU |      |
|                                         |                  |      |
|                                         |                  |      |



The OpenCV is installed by conda that may not enable HW accelerated by CPU special instructions, GPU (CUDA). It need to re-compile the OpenCV to enable GPU/CPU acceleration.



Test result:

```
(tf) ai@7730:~/Try/opencv/blur$ sh cProfile.sh 
        1    0.000    0.000    0.076    0.076 AllBlur.py:1(<module>)
        1    0.001    0.001    0.001    0.001 {GaussianBlur}
        1    0.001    0.001    0.001    0.001 {blur}
        1    0.002    0.002    0.002    0.002 {medianBlur}
Python 3.7.3
cv2 version: 4.1.1
```



### Jetson Nano

The OpenCV is prebuilt with the Nvidia original  image (jetson-nano-sd-r32.2.1.zip)  that also not enable by GPU.  You may find the details in this story https://devtalk.nvidia.com/default/topic/1049972/jetson-nano/opencv-cuda-python-with-jetson-nano/.

**I am also not sure if this per-built OpenCV enables with NEON of Arm to do the HW acceleration.**

Test result:

```
ahe@JN:~/blur$ sh cProfile.sh 
        1    0.000    0.000    1.040    1.040 AllBlur.py:1(<module>)
        1    0.010    0.010    0.010    0.010 {GaussianBlur}
        1    0.004    0.004    0.004    0.004 {blur}
        1    0.014    0.014    0.014    0.014 {medianBlur}
Python 3.6.8
cv2 version: 3.3.1
```



Compile OpenCV with NEON

[ Install Opencv 4.1 on Nvidia Jetson Nano ](https://pysource.com/2019/08/26/install-opencv-4-1-on-nvidia-jetson-nano/)

 

https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.0.0_Nano.sh