import cv2 as cv
counter = 0
cap = cv.VideoCapture(0)

while True :
    x , frame = cap.read()
    counter = counter + 1
    flipped_right = cv.flip(cv.transpose(frame),1)
    flipped_left = cv.flip(cv.transpose(frame),0)
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    if counter % 2 == 0 :
        cv.imshow('Image',flipped_right)
    else:
        cv.imshow('Image',flipped_left)
