import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def mouse(event, x, y, flags, param):
	global points, flag
	if event == cv2.EVENT_LBUTTONDOWN:
		print((x,y))
		print(frame_height)
		print(frame_width)
		print(frame.shape)
		print(frame[x:x+frame_width,y:y+frame_height])


cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse)

while True :
	x,frame = cap.read()
	cv2.imshow('img',frame)
	frame_width = frame.shape[1]
	frame_height = frame.shape[0]
	if cv2.waitKey(1000) and 0xFF == ord('q') :
		break