import djitellopy
from djitellopy import Tello
import cv2, math, time
import numpy

import argparse
import os
import keyboard

"""
parser.add_argument('--face_cascade',help='Path to face cascade.', default=absol_path)
args = parser.parse_args()
face_cascade_name = args.face_cascade

face_cascade = cv2.CascadeClassifier(haarcascades_path)
if not face_cascade.load(f"haarcascade_frontalface_alt.xml"):
    print('error loading cascade classifier')
    exit(0)

def haar_detectFace(frame):
    frame_gray = cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in face:
        cv2.rectangle(frame_gray, (x,y),(x+w, y+h),(0,255,0), -1,8)
"""

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

drone.land()

