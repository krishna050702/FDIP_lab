import cv2
import numpy as np

img_original = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab03\veggy.jpg",1)
img = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab03\veggy.jpg",0)
[w,h] = img.shape
img1 = np.zeros([w,h,3], dtype=np.uint8)
img2 = np.zeros([w,h,3], dtype=np.uint8)
img3 = np.zeros([w,h,3], dtype=np.uint8)
img4 = np.zeros([w,h,3], dtype=np.uint8)
img5 = np.zeros([w,h,3], dtype=np.uint8)
img6 = np.zeros([w,h,3], dtype=np.uint8)
img7 = np.zeros([w,h,3], dtype=np.uint8)
img8 = np.zeros([w,h,3], dtype=np.uint8)

def bitget(nbr, pos):
    return (nbr>>pos) & 1

planes = 8
for i in range(0,w):
    for j in range(0,h):
        for p in range(planes-1, -1, -1):
            if p==7:
                img1[i][j] = 255 * bitget(img[i][j], p)
            elif p==6:
                img2[i][j] = 255 * bitget(img[i][j], p)
            elif p==5:
                img3[i][j] = 255 * bitget(img[i][j], p)
            elif p==4:
                img4[i][j] = 255 * bitget(img[i][j], p)
            elif p==3:
                img5[i][j] = 255 * bitget(img[i][j], p)
            elif p==2:
                img6[i][j] = 255 * bitget(img[i][j], p)
            elif p==1:
                img7[i][j] = 255 * bitget(img[i][j], p)
            else:
                img8[i][j] = 255 * bitget(img[i][j], p)

cv2.imshow('Original', img_original)
cv2.imshow("Greyscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Planes 08', img1)
cv2.imshow('Planes 07', img2)
cv2.imshow('Planes 06', img3)
cv2.imshow('Planes 05', img4)
cv2.waitKey(0)
cv2.imshow('Planes 04', img5)
cv2.imshow('Planes 03', img6)
cv2.imshow('Planes 02', img7)
cv2.imshow('Planes 01', img8)
cv2.waitKey(0)
cv2.destroyAllWindows()