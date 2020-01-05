import os, sys, signal, time, timeit
import cv2
import numpy as np
from threading import Thread
from queue import Queue
#from Queue import Queue
from c_camera import ImgCap, initCamera

np.set_printoptions(threshold=sys.maxsize)

class iTask(Thread):
    def __init__(self, queue, signal):
        Thread.__init__(self)
        self.qf = queue
        self.signal = signal
        self.frame_count = 0
    def run(self):
        while (True):
            img = self.qf.get()
            if img is None:
                break
            self.frame_count += 1
        print("Quit iTask")
    def terminate(self):
        print("iTask OFF")
        self.signal = "OFF"
    def count_frame(self):
        return self.frame_count

'''
def singer(pd):
    global sign
    while (True):
        #print("singing..., %s" %sign)
        time.sleep(2)
        if sign == "OFF":
            pd.terminate()
            break
    print("Quit singer")
'''

sign = "ON"
pdd = None

def signal_handler(signum, frame):
    global sign
    sign = "OFF"
    print("Get signal: %s" %signal)
    pdd.terminate()

def demo(FLAGS):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("init camera")
    cap = cv2.VideoCapture(FLAGS.vdev)
    initCamera(cap, FLAGS.fps)
    time.sleep(1)

    global sign
    queue_list = []
    consumer_list = []
    thread_list = []

    print("start consumer")
    for i in range(FLAGS.jobs):
        queue = Queue(maxsize=0)
        queue_list.append(queue)
        consumer = iTask(queue, signal)
        consumer_list.append(consumer)
        thread_list.append(consumer)
        consumer.setDaemon(True)
        consumer.start()

    print("timeit")
    time_start = timeit.default_timer()

    global pdd
    print("start producer")
    producer = ImgCap(cap, queue_list, signal)
    pdd = producer
    thread_list.append(producer)
    producer.setDaemon(True)
    producer.start()

    '''
    print("start singing")
    sing = Thread(name="Singer", target=singer, args=(producer,))
    sing.setDaemon(True)
    sing.start()
    '''

    while True:
        alive = False
        #alive = alive or sing.isAlive()
        for t in thread_list:
            alive = alive or t.isAlive()
        if not alive:
            break

    time_end = timeit.default_timer()

    cap_frame_count = producer.count_frame()
    print("Produce frames: %d" %cap_frame_count)

    inference_frame_count = 0
    for consumer in consumer_list:
        fcnt = consumer.count_frame()
        inference_frame_count += fcnt
    print("Consume frames: %d" %inference_frame_count)

    cap.release()
    time_used = time_end - time_start
    print("Time Used: %d second!" %time_used)
    print("FPS: %.6f" %(inference_frame_count / time_used))