import cv2 as cv
import numpy as np
def nothing(x):
    pass

barsWindow = 'Bars'
hl = 'Hue Low'
hh = 'Hue High'
sl = 'Saturation Low'
sh = 'Saturation High'
vl = 'Value Low'
vh = 'Value High'

cap = cv.VideoCapture(0)
cv.namedWindow(barsWindow, flags=cv.WINDOW_AUTOSIZE)
cv.createTrackbar(hl, barsWindow, 0, 179, nothing)
cv.createTrackbar(hh, barsWindow, 0, 179, nothing)
cv.createTrackbar(sl, barsWindow, 0, 255, nothing)
cv.createTrackbar(sh, barsWindow, 0, 255, nothing)
cv.createTrackbar(vl, barsWindow, 0, 255, nothing)
cv.createTrackbar(vh, barsWindow, 0, 255, nothing)
cv.setTrackbarPos(hl, barsWindow, 0)
cv.setTrackbarPos(hh, barsWindow, 179)
cv.setTrackbarPos(sl, barsWindow, 0)
cv.setTrackbarPos(sh, barsWindow, 255)
cv.setTrackbarPos(vl, barsWindow, 0)
cv.setTrackbarPos(vh, barsWindow, 255)

while (True):
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hul = cv.getTrackbarPos(hl, barsWindow)
    huh = cv.getTrackbarPos(hh, barsWindow)
    sal = cv.getTrackbarPos(sl, barsWindow)
    sah = cv.getTrackbarPos(sh, barsWindow)
    val = cv.getTrackbarPos(vl, barsWindow)
    vah = cv.getTrackbarPos(vh, barsWindow)
    hsv_low = np.array([hul, sal, val])
    hsv_high = np.array([huh, sah, vah])
    mask = cv.inRange(hsv, hsv_low, hsv_high)
    maskedFrame = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('Masked', maskedFrame)
    cv.imshow('Camera', frame)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break
