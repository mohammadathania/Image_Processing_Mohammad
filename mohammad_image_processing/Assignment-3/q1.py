import cv2 as cv
import numpy as np
import random
img = cv.imread('dog-photo.png')
print(img.shape)
#cv.rectangle(img)
width = int((img.shape[1])/7)
height = int((img.shape[0])/7)
print(width)
print(height)
rows = int(img.shape[0] / height)
print(rows)

counter = 0
while (counter<=rows) :

    x = 0
    y = counter * height
    y0 = y + height
    for i in range(1, 8):
        x0 = x + width
        cv.rectangle(img, (x, y), (x0, y0),
                     (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), -1)
        x = x0
        cv.imshow('Frame', img)
        cv.waitKey(500)
    counter = counter + 1