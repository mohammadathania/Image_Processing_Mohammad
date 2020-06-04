import cv2 as cv
cap = cv.VideoCapture(0)
counter = 0
user_input = int(input("ENTER THE VALUE OF N ....."))
while True :
    counter = counter + 1
    x , frame = cap.read()
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    flipped = cv.flip(frame,-1)
    if (counter <= user_input) :
        cv.imshow("Image",frame)
    else :
        cv.imshow("Image",flipped)
