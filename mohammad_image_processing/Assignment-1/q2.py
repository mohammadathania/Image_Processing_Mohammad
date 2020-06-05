import cv2 as cv
counter = 0
cap = cv.VideoCapture(0)

while True :
    x , frame = cap.read()
    counter = counter + 1
    flipped_horizontal = cv.flip(frame,1)
    if cv.waitKey(1000) & 0xFF == ord('q') :
        break
    if counter % 2 == 0 :
        cv.imshow('Image',flipped_horizontal)
    else:
        cv.imshow('Image',frame)
