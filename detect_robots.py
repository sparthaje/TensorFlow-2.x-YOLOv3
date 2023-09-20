#================================================================
#
#   File name   : detect_mnist.py
#   Author      : PyLessons
#   Created date: 2020-08-12
#   Website     : https://pylessons.com/
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : mnist object detection example
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import random
import time
import tensorflow as tf
from yolov3.yolov4 import Create_Yolo
from yolov3.utils import detect_image2, detect_video
from yolov3.configs import *

label_txt = "roboflow/test/_annotations.txt"

yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
yolo.load_weights(f"./checkpoints/yolov3_custom_Tiny") # use keras weights

total_time = 0
total_accuracy = 0
total = 0
images = []
times = []

# detect_video(yolo, "roboflow/video.mp4", "roboflow/results/detections.mp4", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))

for x in open(label_txt).readlines():
    image_path = "roboflow/test/" + x.split(" ")[0]
    output_path = "results/" + x.split(" ")[0]
    try:
        img, t, acc = detect_image2(yolo, image_path, output_path, input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
    except:
        print(image_path, "didn't work?")
        continue
    
    total_time += t
    total_accuracy += acc
    total += 1
    images.append(img)
    times.append(t)

print(total / total_time, "Hz")
print(total_accuracy / total, "avg accuracy")



for image, d in zip(images, times):
    cv2.imshow('Image', image)
    cv2.waitKey(int(d * 1000))

    cv2.destroyWindow('Image')

cv2.destroyAllWindows()
