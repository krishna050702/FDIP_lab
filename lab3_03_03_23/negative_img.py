#negative image
import cv2
import numpy as np
img=cv2.imread("./assets/Lenna.png")
print(img.dtype)
img_neg=255-img
cv2.imshow('negative',img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows