import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread ('image.jpg')
imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((15,15))
print(kernel)
'''
mean_thresh = cv2.adaptiveThreshold(imgGrey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,2)
filter = cv2.edgePreservingFilter(imgGrey)

dilate = cv2.dilate(imgGrey,kernel)
canny = cv2.Canny(dilate,12,50)'''

sobelx_kernel = np.array([-1,-2,-1,
                          0,0,0,
                          1,2,1])

sobelx = cv2.filter2D(imgGrey,-1,sobelx_kernel)
sobely_kernel = np.array([-1,0,1,
                          -2,0,2,
                          -1,0,1])

sobely = cv2.filter2D(sobelx,-1,sobelx_kernel)
plt.imshow(sobely)
plt.waitforbuttonpress()
