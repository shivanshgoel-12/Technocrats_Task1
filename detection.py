import cv2
import time
from imutils.video import VideoStream
#t,y = cv2.VideoCapture(0).read()
#cv2.imshow('frame',y)
#cv2.waitKey(0)
vs = cv2.VideoCapture(0)
time.sleep(2.0)
i=0
while True:
    i+=1
    print("HI")
    frame = vs.read()
    cv2.imshow('Screen',frame[1])
    cv2.waitKey(1)
    if i == 1000:
        break
vs.stop()