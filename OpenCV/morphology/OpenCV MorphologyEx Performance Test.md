# OpenCV mophologyEx Performance Test



## Example Code

```python
xilinx@pynq:~/Try/opencv/morphology$ cat cv2_morphology_profile.py 
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
ttt = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = timer()
print("Time Used", t2 - t1, "second")

t1 = time.time()
ttt = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = time.time()
print("Time Used", t2 - t1, "second")

t1 = time.process_time()
ttt = cv2.morphologyEx(g_img, cv2.MORPH_OPEN, (5,5))
t2 = time.process_time()
print("Time Used", t2 - t1, "second")

```

**Test Script:**

```

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
(tf2) ai@7730:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.4.2
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.00012079899897798896 second
Time Used 0.00013899803161621094 second
Time Used 7.454199999999689e-05 second
(tf2) ai@7730:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.4.2
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.00012185199739178643 second
Time Used 0.0001399517059326172 second
Time Used 7.49530000000026e-05 second
(tf2) ai@7730:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.4.2
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.00012205100210849196 second
Time Used 0.0001404285430908203 second
Time Used 7.50269999999914e-05 second
(tf2) ai@7730:~/Try/opencv/morphology$ 
```

The cv2.morphologyEx() used about 120us-140us.

*time.process_time() got different time that other two time count that need to further investigation*

### Jetson Nano

The OpenCV is prebuilt with the Nvidia original  image (jetson-nano-sd-r32.2.1.zip)  that also not enable by GPU.  You may find the details in this story https://devtalk.nvidia.com/default/topic/1049972/jetson-nano/opencv-cuda-python-with-jetson-nano/.

**I am also not sure if this per-built OpenCV enables with NEON of Arm to do the HW acceleration.**

Test result:

```
dlinano@jetson-nano:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.3.1
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.0018574989999251557 second
Time Used 0.0015256404876708984 second
Time Used 0.0012928130000000593 second
dlinano@jetson-nano:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.3.1
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.0015793140000823769 second
Time Used 0.0015461444854736328 second
Time Used 0.0012707809999999986 second
dlinano@jetson-nano:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.3.1
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.0014475919999767939 second
Time Used 0.0015473365783691406 second
Time Used 0.0012942190000000409 second
```

The cv2.morphologyEx() used about  1.5ms

### Ultra96 (v2.4 image)

Test result

```
xilinx@pynq:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.2.0
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.009192149999989851 second
Time Used 0.00800180435180664 second
Time Used 0.007716717000000095 second
xilinx@pynq:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.2.0
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.009225358000094275 second
Time Used 0.00796365737915039 second
Time Used 0.007694626999999787 second
xilinx@pynq:~/Try/opencv/morphology$ python3 cv2_morphology_profile.py 
cv2 version: 3.2.0
Image Dimensions : (640, 480, 3)
Image Dimensions : (640, 480)
Time Used 0.009212169000193171 second
Time Used 0.008016347885131836 second
Time Used 0.007663088000000151 second
```

The cv2.morphologyEx() used about  9ms

