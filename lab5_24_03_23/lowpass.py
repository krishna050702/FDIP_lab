import cv2
# import Numpy
import numpy as np

img=cv2.imread("./assets/preview500.jpg")

kernel=np.array([[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]])

kernel=kernel/sum(kernel)
img_fil=cv2.filter2D(img,-1,kernel)
cv2.imshow('original',img)
cv2.imshow('filtered',img_fil)
cv2.waitKey(0)
cv2.destroyAllWindows()