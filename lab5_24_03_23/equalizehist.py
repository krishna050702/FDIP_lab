# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
# read image
path = "assets\camera_man.jpg"
flag = 0
img = cv2.imread(path, flag)

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow('cameraman', res)

cv2.waitKey(0)
cv2.destroyAllWindows()