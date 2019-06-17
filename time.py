#coding: utf-8

import subprocess
import time

a = time.time()
msg = subprocess.call(["./darknet", "detector", "train", "cfg/svhn.data", \
	"cfg/svhn-yolov3-tiny.cfg", "yolov3-tiny.weights", "-map", "-clear"]) 
b = time.time()
print('darknet training 9000 time-used: ', b-a)
