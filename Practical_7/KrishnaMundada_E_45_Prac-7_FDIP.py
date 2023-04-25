# Date 21/04/23
# Name:- Krishna Mundada
# Roll no:- 45
# Batch:- E-3
#=========================================================================================================

import cv2
import numpy as np
img=cv2.imread('assets\lines.png',0)
cv2.imshow('original',img)

#for horizontal lines
kernel=np.ones((2,19),np.uint8)
horizontalLines=cv2.erode(img,kernel,iterations=1)

#For vertical lines
kernel = np.ones((19, 2), np.uint8)
vertical_lines = cv2.erode(img, kernel, iterations=1)

cv2.imshow('output_Horizontal Lines',horizontalLines)
cv2.imshow('output_Vertical Lines',vertical_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
