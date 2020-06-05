import cv2 as cv

cap = cv.VideoCapture(0)
counter = 0
while True :
    x , frame = cap.read()
    counter = counter + 1
    if counter <= 100:
        cv.imwrite('dataset/IMG-'+str(counter)+'.jpeg', frame)
    else:
        break

