import cv2 as cv
cap = cv.VideoCapture(0)
user_input = int(input("ENTER THE VALUR OF N ....."))
while True :
    x , frame = cap.read()
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    flipped = cv.flip(frame,-1)
    for i in range(0,user_input) :
        cv.imshow('Image',frame)