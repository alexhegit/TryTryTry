# Python Parallel Programming Example

The producer-consumer model is very common in the real world. Here are my trying to use different way by  using Python Parallel Programming methodology to implement it.

For easy show, I use the camera as the producer with some consumers.

1. Producer
   - capture frame from camera
   - convert BGR to GRAY
   - Rotate 90 clockwise
2. Consumer
   - Just get the frame produced by the Producer



## Test Environment

| Item       | Version                                 | Comments               |
| ---------- | --------------------------------------- | ---------------------- |
| OS         | Ubuntu 18.04                            |                        |
| Python     | v3.7.3                                  | opencv-python 4.1.0.25 |
| CPU        | Intel(R) Xeon(R) E-2176M  CPU @ 2.70GHz |                        |
| DDR        | 64GB                                    |                        |
| USB Camera | Logitech Webcam C170                    | 640x480/MJPG           |
|            |                                         |                        |
|            |                                         |                        |

* You can use different camera for your test. 
* Logitech Webcam C170 support YUYV and MJPG with different resolution and FPS settings.
* I set Webcam C170 to 640x480/MJPG for test.
* The camera may have different settings. The v4l2-ctl is very good tools to get the details. Here is a logs of mine for sharing. https://github.com/alexhegit/Funny-tools/blob/master/MyUsage/v4l2-ctl.md 



Here is my checking of video device @ my machine.

```
$ v4l2-ctl --list-device
Webcam C170: Webcam C170 (usb-0000:00:14.0-1):
	/dev/video2
	/dev/video3

Integrated_Webcam_HD: Integrate (usb-0000:00:14.0-11):
	/dev/video0
	/dev/video1

ai@7730:~$ v4l2-ctl --list-formats-ext -d 2
ioctl: VIDIOC_ENUM_FMT
	Index       : 0
	Type        : Video Capture
	Pixel Format: 'YUYV'
	Name        : YUYV 4:2:2
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 176x144
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 160x120
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 544x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 432x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x176
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)

	Index       : 1
	Type        : Video Capture
	Pixel Format: 'MJPG' (compressed)
	Name        : Motion-JPEG
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 176x144
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 160x120
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 544x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 432x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x176
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 800x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 1024x768
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.067s (15.000 fps)


```





## Thread VS Process

To get good performance of FPS, we usually use multi-thread or multi-process model. I do try both of them and compare the performance like FPS, CPU loading, etc.

Python is very easy programming to use thread and process. Multi-thread in Python may limited by GIL (default interpretor by CPython) as well as  Multi-process without effect by GIL but may need more memory resource and copy  for IPC.

There are many topic to compare them. 

https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python 

https://blog.thedataincubator.com/2018/04/python-multi-threading-vs-multi-processing/

Or find more from Internet by yourself.  In-one-word, multi-thread is fit for I/O-bound task as well as multi-process is affinity for CPU-bound task.

I do not want to repeat the theory but just show the code to use it. At later I also do a simple performance test with my environment.



## Example Code

I'd like to record my trying in [my github](https://github.com/alexhegit/ ). Hope there are something you are also interested.

### Multi-thread example

https://github.com/alexhegit/TryTryTry/tree/master/Python/thread_class

### Multi-process example

https://github.com/alexhegit/TryTryTry/tree/master/Python/process_class



I use object-oriented class programming finished multi-thread example first and then very easy and quick convert it to multi-process example by some minor changes since process implementation is very similar with thread implementation in Python. 

Actually, the primal examples without object-oriented thinkings are in https://github.com/alexhegit/TryTryTry/tree/master/Python/process_thread. 



### Test

**Multi-thread**

```
# TryTryTry/Python/thread_class$ python demo.py --vdev 2 --jobs 4
init camera
FPS: 30.00
FOURCC: 1448695129.0
WIDTH: 640
HEIGHT: 480
set fourcc, MJPG: 1196444237
1196444237
FPS: 30.00
FOURCC: 1196444237.0
WIDTH: 640
HEIGHT: 480
start consumer
timeit
start producer
Quit ImgCap
Quit iTask
Quit iTask
Quit iTask
Quit iTask
Produce frames: 1782
Consume frames: 1782
Time Used: 76 second!
FPS: 23.292092


# top
top - 11:55:05 up  2:23,  1 user,  load average: 1.69, 1.12, 1.22
Tasks: 404 total,   2 running, 312 sleeping,   0 stopped,   0 zombie
%Cpu0  :  3.8 us,  0.3 sy,  0.0 ni, 82.2 id,  0.0 wa,  0.0 hi, 13.7 si,  0.0 st
%Cpu1  :  4.7 us,  0.7 sy,  0.0 ni, 93.4 id,  0.0 wa,  0.0 hi,  1.3 si,  0.0 st
%Cpu2  : 99.7 us,  0.0 sy,  0.0 ni,  0.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu3  :  5.0 us,  0.7 sy,  0.0 ni, 94.4 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  :  5.4 us,  0.0 sy,  0.0 ni, 94.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  :  5.5 us,  0.0 sy,  0.0 ni, 94.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  :  3.4 us,  0.0 sy,  0.0 ni, 96.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  4.0 us,  0.0 sy,  0.0 ni, 96.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  :  3.7 us,  0.0 sy,  0.0 ni, 96.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  :  5.3 us,  0.7 sy,  0.0 ni, 94.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 :  3.3 us,  4.9 sy,  0.0 ni, 91.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu11 :  5.0 us,  0.0 sy,  0.0 ni, 95.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 65794820 total, 56705820 free,  4061904 used,  5027096 buff/cache
KiB Swap:  8000508 total,  8000508 free,        0 used. 60605796 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                           
10475 ai        20   0 1606096  82692  52172 R 149.3  0.1   0:50.24 python                 
```

**Multi-process**

```
# TryTryTry/Python/process_class$ python demo.py --vdev 2 --jobs 4
init camera
FPS: 30.00
FOURCC: 1448695129.0
WIDTH: 640
HEIGHT: 480
set fourcc, MJPG: 1196444237
1196444237
FPS: 30.00
FOURCC: 1196444237.0
WIDTH: 640
HEIGHT: 480
start consumer
timeit
start producer
Quit ImgCap-5, frames 1837
Quit iTask-4, frames 459
Quit iTask-1, frames 460
Quit iTask-2, frames 459
Quit iTask-3, frames 459
Produce frames: 0
Consume frames: 0
Time Used: 61 second!
FPS: 0.000000
FPS: 29.967917


# top
top - 12:09:42 up  2:37,  1 user,  load average: 0.37, 0.37, 0.72
Tasks: 403 total,   1 running, 315 sleeping,   0 stopped,   0 zombie
%Cpu0  :  2.0 us,  1.0 sy,  0.0 ni, 96.7 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu1  :  3.3 us,  0.7 sy,  0.0 ni, 96.1 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu2  : 16.7 us,  0.6 sy,  0.0 ni, 82.4 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
%Cpu3  :  2.0 us,  0.3 sy,  0.0 ni, 97.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu4  :  1.0 us,  0.3 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu5  :  3.1 us,  0.3 sy,  0.0 ni, 96.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu6  :  0.7 us,  0.3 sy,  0.0 ni, 99.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu7  :  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu8  :  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu9  :  1.3 us,  0.0 sy,  0.0 ni, 98.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu10 :  0.0 us,  1.7 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
%Cpu11 :  0.3 us,  0.0 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 65794820 total, 56696056 free,  4067956 used,  5030808 buff/cache
KiB Swap:  8000508 total,  8000508 free,        0 used. 60597832 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                           
10837 ai        20   0 1242244  59360  28728 S  13.6  0.1   0:34.02 python                 
```

**NOTE:**

* --vdev to set video device
* --jobs to set the number of consumer as thread or process



The top show multi-process implementation has better FPS and lower CPU loading that means this producer-consumer task is CPU-bound.







