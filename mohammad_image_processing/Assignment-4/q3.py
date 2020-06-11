import cv2
import numpy as np

img = cv2.imread('img.jpg')
counter = 0
points = []
def warpping(pt1,pt2,pt3,pt4):
    pts_1 = np.array([pt1,pt2,pt3,pt4],np.float32)
    pts_2 = np.array([(0, 0), (500, 0), (0, 600), (500, 600)], np.float32)
    perspective = cv2.getPerspectiveTransform(pts_1, pts_2)
    transformed = cv2.warpPerspective(img, perspective, (500, 600))
    cv2.imshow("image", img)
    cv2.imshow('img', transformed)
    cv2.waitKey(0)

def mouse(event,x,y,flags,param) :
    global counter
    if event == cv2.EVENT_LBUTTONDOWN :
        counter = counter + 1
        points.append((x, y))
        print((points))
        if counter == 4 :
            print(type(points[3]))
            warpping(points[0],points[1],points[2],points[3])

image = cv2.imread('img.jpg')
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse)
while True:
	cv2.imshow("image", image)
	if cv2.waitKey(1000) & 0xFF == ord("q"):
		break

