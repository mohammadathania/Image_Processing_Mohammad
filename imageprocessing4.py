import cv2 as cv
'''img = cv.imread('dog-photo.png')
cv.imshow('Frame',img)
cv.waitKey(0)'''
# Cropping
'''height = img.shape[0]
width = img.shape[1]
cropped = img[int((width-100)/2):int((width+100)/2),int((height-100)/2):int((height+100)/2)]
cv.imshow('Image',cropped)
cv.waitKey(0)'''

# Mouse Selection



def mouse(event,x,y,flags,param) :
    #print(x,y)
    if event == cv.EVENT_LBUTTONDOWN :
        print(x,y)

cap = cv.VideoCapture(0)
cv.namedWindow('Frame')

while True :
    x , frame = cap.read()
    cv.imshow('Frame',frame)
    if cv.waitKey(1000) & 0xFF == ord('q') :
        break
    cv.setMouseCallback('Frame',mouse)