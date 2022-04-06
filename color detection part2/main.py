import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _, frame=cap.read()
    cv2.imshow("frame",frame)
    frameHsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #red
    lower=np.array([161,155,84])
    high=np.array([179,255,255])
    mask=cv2.inRange(frameHsv,lower,high)



    key=cv2.waitKey(1)
    cv2.imshow("red",mask)
    if key==27:
        break;