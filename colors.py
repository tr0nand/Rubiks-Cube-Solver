import cv2
import os
import numpy as np


image = cv2.imread(os.path.join('img','img1.png'))
cv2.imshow('image1',image)
cv2.waitKey(0)
c = 0
for i in range(3):
    frame = image[c*50:c*50 + 50,0:50]
    cv2.imshow('image',frame)
    cv2.waitKey(0)

    avg = np.average(frame,axis=(0,1))
    avg = avg.astype(int)
    fill = np.zeros((50,50,3),np.uint8)
    fill[:] = avg
    cv2.imshow('image',fill)
    cv2.waitKey(0)

    frame = image[c*50:c*50 + 50,50:100]
    cv2.imshow('image',frame)
    cv2.waitKey(0)

    avg = np.average(frame,axis=(0,1))
    avg = avg.astype(int)
    fill = np.zeros((50,50,3),np.uint8)
    fill[:] = avg
    cv2.imshow('image',fill)
    cv2.waitKey(0)

    frame = image[c*50:c*50 + 50,100:150]
    cv2.imshow('image',frame)
    cv2.waitKey(0)

    avg = np.average(frame,axis=(0,1))
    avg = avg.astype(int)
    fill = np.zeros((50,50,3),np.uint8)
    fill[:] = avg
    cv2.imshow('image',fill)
    cv2.waitKey(0)

    c=c+1
