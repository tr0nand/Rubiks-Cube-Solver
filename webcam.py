import cv2
import os

directory = 'img'
os.mkdir(directory)
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

img_counter = 0
while rval and img_counter !=6:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key == 32:
        imgname = "img"+str(img_counter)+".png"
        frame = frame[xpos:xpos + 3*size,ypos:ypos+3*size]
        cv2.imwrite(os.path.join(directory,imgname), frame)
        img_counter = img_counter + 1
        print("Face {} taken".format(img_counter))
    else:
        xpos = 175
        ypos = 175
        size = 50
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
