import numpy as np
import cv2 as cv

img=cv.imread("./assets/camera_man1.png",0)

[w,h]=img.shape
img1=np.zeros([w,h,3],dtype=np.uint8)
img2=np.zeros([w,h,3],dtype=np.uint8)
img3=np.zeros([w,h,3],dtype=np.uint8)
img4=np.zeros([w,h,3],dtype=np.uint8)
img5=np.zeros([w,h,3],dtype=np.uint8)
img6=np.zeros([w,h,3],dtype=np.uint8)
img7=np.zeros([w,h,3],dtype=np.uint8)
img8=np.zeros([w,h,3],dtype=np.uint8)

def bitget(nbr,pos):
    return (nbr>>pos) & 1

planes=8
for i in range(0,w):
    for j in range(0,h):
        for p in range(planes-1,-1,-1):
            if p==7:
                img1[i][j]=255*bitget(img[i][j],p)
            elif p==6:
                img2[i][j]=255*bitget(img[i][j],p)
            elif p==5:
                img3[i][j]=255*bitget(img[i][j],p)
            elif p==4:
                img4[i][j]=255*bitget(img[i][j],p)
            elif p==3:
                img5[i][j]=255*bitget(img[i][j],p)
            elif p==2:
                img6[i][j]=255*bitget(img[i][j],p)
            elif p==1:
                img7[i][j]=255*bitget(img[i][j],p)
            else:
                img8[i][j]=255*bitget(img[i][j],p)

cv.imshow('Plane 08',img1)
cv.imshow('Plane 07',img2)
cv.imshow('Plane 06',img3)
cv.imshow('Plane 05',img4)
cv.imshow('Plane 04',img5)
cv.imshow('Plane 03',img6)
cv.imshow('Plane 02',img7)
cv.imshow('Plane 01',img8)

cv.waitKey(0)
cv.destroyAllWindows
