import cv2 as cv
img = cv.imread('dog-photo.png')
print(img)

print(img.shape)
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,0),4)
cv.line(img,(img.shape[1],0),(0,img.shape[0]),(0,0,0),4)
cv.imshow('Figure',img)
cv.waitKey(0)