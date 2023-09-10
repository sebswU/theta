import djitellopy
from djitellopy import Tello
import cv2, math, time
import numpy as np

import argparse
import os
import keyboard

drone = Tello()
drone.connect()
# how you get the input stream for opencv
drone.streamon()
frame_read = drone.get_frame_read()

drone.takeoff()
haar = cv2.CascadeClassifier("haar.xml")
while True:
    img = frame_read.frame
    imgVJ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_res = haar.detectMultiScale(imgVJ, scaleFactor=1.2, minNeighbors=3)

    for (x,y,w,h) in haar_res:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=2)
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == ord('x'):
        break
    elif key == ord('w'):
        drone.move_forward(30)
    elif key == ord('s'):
        drone.move_back(30)
    elif key == ord('a'):
        drone.move_left(30)
    elif key == ord('d'):
        drone.move_right(30)
    elif key == ord('e'):
        drone.rotate_clockwise(30)
    elif key == ord('q'):
        drone.rotate_counter_clockwise(30)
    elif key == ord('r'):
        drone.move_up(30)
    elif key == ord('f'):
        drone.move_down(30)
def threeSixty(sps=1):
    coor = np.ndarray(shape=(3,3), dtype=float)
    theta = np.ndarray(shape=3, dtype=int)
    cv2.imwrite("picture.png", frame_read.frame)
    drone.curve_xyz_speed(0,0,0,-300,173,0, 50)
    drone.rotate_counter_clockwise(120)
    cv2.imwrite("picture1.png", frame_read.frame)
    drone.curve_xyz_speed(0, 0, 0, 0, -346, 0, 50)
    drone.rotate_counter_clockwise(120)
    cv2.imwrite("picture2.png", frame_read.frame)
    drone.curve_xyz_speed(0, 0, 0, 300, 173, 0, 50)
    drone.rotate_counter_clockwise(120)
    return 0
drone.land()

