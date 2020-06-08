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

cv.rectangle(img,(width,height),(height,width),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
cv.imshow('Frame',img)
cv.waitKey(0)