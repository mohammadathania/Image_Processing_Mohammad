import cv2 as cv
'''img = cv.imread('dog-photo.png')
print(img)

cv.imshow('Figure',img)
cv.waitKey(0)
'''

counter = 0
cap = cv.VideoCapture(0)

while True :
    counter = counter + 1
    x , frame = cap.read()
    # cv.imshow('Image',frame)
    if cv.waitKey(5) & 0xFF == ord('q') :
        break
    flipped = cv.flip(frame,-1)
    #cv.imshow('Flipped',flipped)
    if counter % 2 == 0 :
        cv.imshow('Image',frame)
    else :
        cv.imshow('Image',flipped)