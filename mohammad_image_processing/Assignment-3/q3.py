import cv2 as cv
import numpy as np
import random
img = cv.imread('dog-photo.png')
print(img.shape)
width = int((img.shape[1])/7)
height = int((img.shape[0])/7)
print(width)
print(height)
rows = int(img.shape[0] / height)
print(rows)
counter = 0

while (counter <= rows) :
    if (counter % 2) == 0 :
        x = 0
        y = counter * height
        y0 = y + height
        for i in range(1, 8):
            x0 = x + width
            new = img.copy()
            cv.rectangle(new, (x, y), (x0, y0),
                         (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), -1)
            x = x0
            cv.imshow('Frame', new)
            cv.waitKey(500)

        counter = counter + 1

    else :
        x1 = x0
        y1 = y0
        y2 = y1 + height
        for i in range(1, 8):
            x2 = x1
            x1 = x1 - width
            new = img.copy()
            cv.rectangle(new, (x1, y1), (x2 , y2), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), -1)
            cv.imshow('Frame', new)
            cv.waitKey(500)
        counter = counter + 1

