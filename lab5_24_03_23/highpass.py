import cv2
# import Numpy
import numpy as np

img=cv2.imread("./assets/preview500.jpg")

kernel=np.array([[0.0,-1.0,0.0],
                 [-1.0,4.0,-1.0],
                 [0.0,-1.0,0.0]])

kernel=kernel/np.sum(kernel)  if np.sum(kernel)!=0 else 1
img_fil=cv2.filter2D(img,-1,kernel)
cv2.imshow('original',img)
cv2.imshow('filtered',img_fil)
cv2.waitKey(0)
cv2.destroyAllWindows()