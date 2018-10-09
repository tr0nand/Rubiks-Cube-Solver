import cv2
import os
import random
import pandas as pd
import numpy as np


class av_color:
    def __init__(self,image,color):
        self.image = image
        self.color = color

    def create(self,avg):
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        cv2.imshow(color,fill)
        cv2.waitKey(0)

    def face1(self):
        frame = self.image[0:50,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face2(self):
        frame = self.image[0:50,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face3(self):
        frame = self.image[0:50,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face4(self):
        frame = self.image[50:100,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face5(self):
        frame = self.image[50:100,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face6(self):
        frame = self.image[50:100,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face7(self):
        frame = self.image[100:150,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face8(self):
        frame = self.image[100:150,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

    def face9(self):
        frame = self.image[100:150,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        self.create(avg)
        avg = [[avg[0],avg[1],avg[2],self.color]]
        return avg

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
df = pd.DataFrame()
img_counter = 0
xpos = 125
ypos = 185
size = 50
colors = ['Yellow','Red','Blue','White','Green','Orange']
ask = True
while rval and img_counter !=6:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    color = colors[img_counter]
    color = 'Orange'
    if(ask):
        print("Input color",color)
        ask = False
    if key == 32:
        color = 'Orange'
        frame = frame[ypos:ypos + 3*size,xpos:xpos+3*size]
        cv2.imshow(color,frame)
        cv2.waitKey(0)
        ask = True
        img_counter = img_counter + 1
        print("Face {} taken".format(img_counter))
        cubeFace = av_color(frame,color)
        col1 = cubeFace.face1()
        df = df.append(col1)
        col2 = cubeFace.face2()
        df = df.append(col2)
        col3 = cubeFace.face3()
        df = df.append(col3)
        col4 = cubeFace.face4()
        df = df.append(col4)
        col5 = cubeFace.face5()
        df = df.append(col5)
        col6 = cubeFace.face6()
        df = df.append(col6)
        col7 = cubeFace.face7()
        df = df.append(col7)
        col8 = cubeFace.face8()
        df = df.append(col8)
        col9 = cubeFace.face9()
        df = df.append(col9)


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
with open('Trainingdata.csv','a') as f:
    df.to_csv(f,header = False,mode='a',index=False)
