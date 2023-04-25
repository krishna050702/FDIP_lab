import cv2
import numpy as np
img=cv2.imread("./assets/Lenna1.jpg")
# new_img = cv2.resize(img, (300, 450))
cv2.imshow('Original image',img)
[w,h,d]=img.shape
for i in range(0,w):
    for j in range(0,h):
        if (img[i][j]>100).all() and (img[i][j]<200).all():
            img[i][j]=210
cv2.imshow('Resultant image',img)
cv2.waitKey(0)
cv2.destroyAllWindows