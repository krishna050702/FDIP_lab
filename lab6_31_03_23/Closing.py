#dilation, erosion,opening, closing

import cv2
import numpy as np

path="./assets/hands.jpeg"
pathOpen="./assets/opening.png"
flag=0
img=cv2.imread(path,flag)
img1=cv2.imread(pathOpen,flag)
new_img = cv2.resize(img, (300, 450))

#binarize the image
binr=cv2.threshold(new_img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
binr1=cv2.threshold(img1,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#define the kernel
kernel=np.ones((3,3),np.uint8)

#invert the image
invert=cv2.bitwise_not(binr)

#dilate the image\
dilation=cv2.dilate(invert,kernel,iterations=1)
erosion=cv2.erode(invert,kernel,iterations=1)
open=cv2.morphologyEx(binr1,cv2.MORPH_OPEN,kernel,iterations=40)
close=cv2.morphologyEx(binr1,cv2.MORPH_CLOSE,kernel,iterations=40)

cv2.imshow("Opening Image",img1)
cv2.imshow("Original image",new_img)
cv2.imshow("dilated image",dilation)
cv2.imshow("Eroded image",erosion)
cv2.imshow("Opened image",open)
cv2.imshow("Closed image",close)
cv2.waitKey(0)
cv2.destroyAllWindows()
