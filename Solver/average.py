import cv2
import os
import numpy as np


class average_color:
    def __init__(self,image):
        self.image = image

    def create(self,avg):
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        cv2.imshow('Color',fill)
        cv2.waitKey(0)

    def makeface(self,faces,size,no):

        fill = np.zeros((size*3,size*3,3),np.uint8)
        for i in range(3):
            for j in range(3):
                if str(faces[i*3+j]) == str("['w']"):
                    col = (255,255,255)
                elif str(faces[i*3+j]) == str("['r']"):
                    col = (0,0,255)
                elif str(faces[i*3+j]) == str("['b']"):
                    col = (255,0,0)
                elif str(faces[i*3+j]) == str("['y']"):
                    col = (0,255,255)
                elif str(faces[i*3+j]) == str("['g']"):
                    col = (0,255,0)
                else :
                    col = (0,140,255)
                fill[i*size:(i+1)*size,j*size:(j+1)*size] = col
        fill[0:3*size,0:2] = (0,0,0)
        fill[0:3*size,size:size+2]=(0,0,0)
        fill[0:3*size,2*size:2*size+2]=(0,0,0)
        fill[0:3*size,3*size-2:3*size]=(0,0,0)
        fill[0:2,0:3*size] = (0,0,0)
        fill[size:size+2,0:3*size]=(0,0,0)
        fill[2*size:2*size+2,0:3*size]=(0,0,0)
        fill[3*size-2:3*size,0:3*size]=(0,0,0)
        cv2.imshow('Side'+str(no),fill)
        cv2.waitKey(0)


    def face1(self):
        frame = self.image[0:50,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face2(self):
        frame = self.image[0:50,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face3(self):
        frame = self.image[0:50,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face4(self):
        frame = self.image[50:100,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face5(self):
        frame = self.image[50:100,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face6(self):
        frame = self.image[50:100,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face7(self):
        frame = self.image[100:150,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face8(self):
        frame = self.image[100:150,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]

    def face9(self):
        frame = self.image[100:150,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        #self.create(avg)
        return [avg]