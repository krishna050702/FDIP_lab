# Lab 5 date:- 31/03/23

import cv2
import numpy as np

path="./assets/nosiyCameraMan.jpg"
flag=0
noisy=cv2.imread(path,flag)
m,n=noisy.shape

img_new=np.zeros([m,n])

for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[noisy[i-1,j-1],
              noisy[i-1,j],
              noisy[i-1,j+1],
              noisy[i,j-1],
              noisy[i,j],
              noisy[i,j+1],
              noisy[i+1,j-1],
              noisy[i+1,j],
              noisy[i+1,j+1]]
        temp=sorted(temp)
        img_new[i,j]=temp[4]
        # temp=np.array(temp)
        # temp=temp/np.linalg.norm(temp)
        # img_new[i,j]=np.dot(temp,np.array([0,0,1]))
img1_new=cv2.medianBlur(noisy,5)
img_new=img_new.astype(np.uint8)
cv2.imshow('original',noisy)
cv2.imshow('final',img_new)
cv2.imshow('final1',img1_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
