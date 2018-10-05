import cv2
import os
from average import average_color
from knn import colorrec



directory = 'img'
if not os.path.isdir(directory):
    os.mkdir(directory)
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

img_counter = 0
xpos = 125
ypos = 185
size = 50
colpredict = colorrec()
while rval and img_counter !=6:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 32:
        imgname = "img"+str(img_counter)+".png"
        frame = frame[ypos:ypos + 3*size,xpos:xpos+3*size]
        cv2.imwrite(os.path.join(directory,imgname), frame)
        img_counter = img_counter + 1
        print("Face {} taken".format(img_counter))
        cubeFace = average_color(frame)
        col1 = cubeFace.face1()
        print(colpredict.color(col1))
        col2 = cubeFace.face2()
        print(colpredict.color(col2))
        col3 = cubeFace.face3()
        print(colpredict.color(col3))
        col4 = cubeFace.face4()
        print(colpredict.color(col4))
        col5 = cubeFace.face5()
        print(colpredict.color(col5))
        col6 = cubeFace.face6()
        print(colpredict.color(col6))
        col7 = cubeFace.face7()
        print(colpredict.color(col7))
        col8 = cubeFace.face8()
        print(colpredict.color(col8))
        col9 = cubeFace.face9()
        print(colpredict.color(col9))


    else:
        cv2.rectangle(img=frame, pt1=(xpos, ypos),pt2=(xpos+size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos),pt2=(xpos + 2*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos),pt2=(xpos + 3*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos, ypos + size),pt2=(xpos+size,ypos+ 2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos + size),pt2=(xpos + 2*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + size),pt2=(xpos + 3*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos, ypos + 2*size),pt2=(xpos+size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + size, ypos+2*size),pt2=(xpos + 2*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + 2*size),pt2=(xpos + 3*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)

vc.release()
cv2.destroyWindow("preview")
