import cv2
import os
import numpy as np


class average_color:
    def __init__(self,image):
        self.image = image

    def face1(self):
        frame = self.image[0:50,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face2(self):
        frame = self.image[0:50,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face3(self):
        frame = self.image[0:50,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face4(self):
        frame = self.image[50:100,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face5(self):
        frame = self.image[50:100,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face6(self):
        frame = self.image[50:100,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face7(self):
        frame = self.image[100:150,0:50]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face8(self):
        frame = self.image[100:150,50:100]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)

    def face9(self):
        frame = self.image[100:150,100:150]
        avg = np.average(frame,axis = (0,1))
        avg = avg.astype(int)
        fill = np.zeros((50,50,3),np.uint8)
        fill[:] = avg
        #return fill
        cv2.imshow('image',fill)
        cv2.waitKey(0)
