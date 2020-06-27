from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import os
from PIL import ImageTk,Image

root = Tk()

root.title('OCR App')
root.geometry('1200x720')

frame1 = Frame(root, bg='blue', width=500, height=720)
frame1.pack(side=RIGHT)

frame2 = Frame(root, bg='red', width=700, height=720)
frame2.pack(side=LEFT)



def open_file():
    global filepath, img
    filepath = filedialog.askopenfilename()
    img = cv2.imread(filepath)
    cv2.imshow('Image', img)


def close(name):
    if cv2.waitKey(1000) & 0xFF == 27:
        cv2.destroyWindow(name)


def crop_manual():
    global cropped
    points = []

    counter = 0

    def mouse_func(event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            if (x, y) is not None:
                points.append((x, y))
                # print((x,y))

            if len(points) == 4:
                print(points)
                req_pt = np.array([points[0], points[1], points[3], points[2]], np.float32)
                dst_pt = np.array([(0, 0), (700, 0), (0, 600), (700, 600)], np.float32)
                pers = cv2.getPerspectiveTransform(req_pt, dst_pt)
                cropped = cv2.warpPerspective(img, pers, (700, 600))
                cv2.imshow('Transformed', cropped)
                close('Transformed')
                return (cropped)

    cv2.namedWindow('Image')
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mouse_func)
    close('Image')

def auto_transform():
    global crop_auto

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_smooth = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ret, img_gray_smooth_thresh = cv2.threshold(img_gray_smooth, 180, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(img_gray_smooth_thresh, 150, 300)

    contour, heirarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contour]
    max_index = np.argmax(areas)
    max_contour = contour[max_index]

    perimeter = cv2.arcLength(max_contour, True)
    coordinates = cv2.approxPolyDP(max_contour, 0.01 * perimeter, True)

    pt1 = np.array([coordinates[1], coordinates[0], coordinates[2], coordinates[3]], np.float32)
    pt2 = np.array([(0, 0), (700, 0), (0, 600), (700, 600)], np.float32)

    pers = cv2.getPerspectiveTransform(pt1, pt2)
    crop_auto = cv2.warpPerspective(img, pers, (700, 600))
    # crop_auto = cv2.rotate(crop_auto, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow('Cropped', crop_auto)
    close('Cropped')

    return (crop_auto)



def show_text():
    global data_to_print

    # Gray Scale
    if auto_transform() is None:
        img = crop_manual()

    elif crop_manual() is None:
        img = auto_transform()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_smooth = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ret, img_gray_smooth_thresh = cv2.threshold(img_gray_smooth, 180, 300, cv2.THRESH_BINARY)

    data_to_print = pytesseract.image_to_string(img_gray_smooth_thresh)
    # content.append(data_to_print)

    text = pytesseract.image_to_data(img_gray_smooth_thresh, output_type=Output.DICT)

    no_word = len(text['text'])

    for i in range(no_word):
        if int(text['conf'][i]) > 50:
            x, y, width, height = text['left'][i], text['top'][i], text['width'][i], text['height'][i]
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow('OCR', img)
    close('OCR')

def blur_image():
    print('Blur Image')
    global avging
    avging = cv2.blur(img, (10, 10))

    cv2.imshow('Averaging', avging)
    cv2.waitKey(0)

    # Gaussian Blurring
    # Again, you can change the kernel size
    global gausBlur
    gausBlur = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow('Gaussian Blurring', gausBlur)
    cv2.waitKey(0)

    # Median blurring
    global medBlur
    medBlur = cv2.medianBlur(img, 5)
    cv2.imshow('Media Blurring', medBlur)
    cv2.waitKey(0)

    # Bilateral Filtering
    global bilFilter
    bilFilter = cv2.bilateralFilter(img, 9, 75, 75)
    cv2.imshow('Bilateral Filtering', bilFilter)
    cv2.waitKey(0)

def print_ocr_op():
    content = data_to_print
    txt_area.insert('1.0', content)

def save_image() :
    cv2.imwrite('save_image/IMG-'+'Average Blur'+'.jpeg', avging)
    cv2.imwrite('save_image/IMG-'+'Gaussian Blur'+'.jpeg', gausBlur)
    cv2.imwrite('save_image/IMG-'+'Median Blur'+'.jpeg', medBlur)
    cv2.imwrite('save_image/IMG-'+'Bilateral Filter Blur'+'.jpeg', bilFilter)
    cv2.imwrite('save_image/IMG-'+'Auto Cropped'+'.jpeg', crop_auto)
    cv2.imwrite('save_image/IMG-' + 'OCR' + '.jpeg', img)

def close_all():
    root.quit()


def save_txt_file():
    filepath = os.path.dirname(__file__)
    file = open(os.path.join(filepath, 'ocr.txt'), 'w')
    file.write(data_to_print)
    file.close()


select_file_btn = Button(frame1, text='Open Image', font=("Courier 15 bold"), command=open_file)
select_file_btn.config(width=20, height=3)
select_file_btn.place(x=50, y=50)

save_file_btn = Button(frame1, text='Save Image', font=("Courier 15 bold"), command=save_image)
save_file_btn.config(width=20, height=3)
save_file_btn.place(x=250, y=50)

auto_crop_btn = Button(frame1, text='Auto Crop', font=("Courier 15 bold"), command=auto_transform)
auto_crop_btn.config(width=20, height=3)
auto_crop_btn.place(x=50, y=150)

manual_crop_btn = Button(frame1, text='Manual Crop', font=("Courier 15 bold"), command=crop_manual)
manual_crop_btn.config(width=20, height=3)
manual_crop_btn.place(x=250, y=150)

ocr_btn = Button(frame1, text='OCR', font=("Courier 15 bold"), command=show_text)
ocr_btn.config(width=20, height=3)
ocr_btn.place(x=50, y=350)

print_txt_btn = Button(frame1, text='Print Text', font=("Courier 15 bold"), command=print_ocr_op)
print_txt_btn.config(width=20, height=3)
print_txt_btn.place(x=50, y=250)

save_btn = Button(frame1, text='Save Text', font=("Courier 15 bold"), command=save_txt_file, padx=5)
save_btn.config(width=20, height=3)
save_btn.place(x=250, y=250)

close_btn = Button(frame1, text='Close', font=("Courier 15 bold"), command=close_all)
close_btn.config(width=20, height=3)
close_btn.place(x=165, y=450)

heading = Label(frame2, text='Welcome to OCR App !',bg = 'red', font=("Courier 20 bold"))
heading.place(x=220, y=20)

txt_area = Text(frame2, width=90, height=47)
txt_area.place(x=30, y=60)

blur_image = Button(frame1, text='Blur Image', font=("Courier 15 bold"), command=blur_image)
blur_image.config(width=20, height=3)
blur_image.place(x=250, y=350)

madeBy = Button(frame1, text='Made By M.A', font=("Courier 15 bold") )
madeBy.config(width=20, height=3)
madeBy.place(x=305, y=650)


cv2.destroyAllWindows()
root.resizable(False, False)

root.mainloop()