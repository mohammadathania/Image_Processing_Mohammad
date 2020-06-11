import cv2
points = []
flag = 0
def mouse(event, x, y, flags, param):
	global points, flag
	if event == cv2.EVENT_LBUTTONDOWN:
		points = [(x, y)]
		flag = 1
	elif event == cv2.EVENT_LBUTTONUP:
		points.append((x, y))
		flag = 0
		cv2.rectangle(image, points[0], points[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

image = cv2.imread('dog-photo.png')
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse)
while True:
	cv2.imshow("image", image)
	if cv2.waitKey(1000) & 0xFF == ord("q"):
		break

if len(points) == 2:
	cropped = image[points[0][1]:points[1][1], points[0][0]:points[1][0]]
	cv2.imshow("Frame", cropped)
	cv2.waitKey(1000)
