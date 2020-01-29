import cv2
import numpy as np 
#import time
#from imutils.video import VideoStream
#t,y = cv2.VideoCapture(0).read()
#cv2.imshow('frame',y)
#cv2.waitKey(0)
vs = cv2.VideoCapture(0)
#time.sleep(2.0)
#i=0
while True:
    res,frame = vs.read()
    if res==True:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower=np.array([65,60,60])
        upper=np.array([80,255,255])
        mask=cv2.inRange(hsv,lower,upper)
        green=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('Mask',mask)
        cv2.imshow('Screen',frame)
        cv2.imshow('Green',green)
        k=cv2.waitKey(1)
        if k== 27:
            break
vs.release()


