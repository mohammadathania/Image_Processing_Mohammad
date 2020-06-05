import cv2 as cv
import time
import math

cap = cv.VideoCapture(0)
counter = 0

while True :
    counter = counter + 1
    startTime = time.time()
    for i in range(0, 5):
        print(i)
        time.sleep(1)#making delay of 1 sec
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Elapsed Time = %s" % elapsedTime)
    x , frame = cap.read()
    flipped = cv.flip(frame,-1)
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    if math.floor(elapsedTime) % counter == 0 :
        cv.imshow('Frame',flipped)
    else :
        cv.imshow('Frame', frame)
