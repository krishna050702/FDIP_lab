import cv2
import numpy as np

img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab03\veggy.jpg", 0)

# LOW PASS FILTER - A Low Pass Filter is more like an averaging process.
#prepare the 5x5 shaped filter
kernel1 = np.array([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])
kernel1 = kernel1/sum(kernel1)
img1_low = cv2.filter2D(img1,-1,kernel1)     #filter the source image

# HIGH PASS FILTER - A High Pass Filter is like an edge detector. It gives a high when there is a significant change in the adjacent pixel values.
#edge detection filter
kernel2 = np.array([[0.0, -1.0, 0.0],
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])
kernel2 = kernel2/(np.sum(kernel2) if np.sum(kernel2)!=0 else 1)
img1_high = cv2.filter2D(img1,-1,kernel2)     #filter the source image

cv2.imshow('Original', img1)
cv2.imshow('Low Pass Filtered', img1_low)
cv2.imshow('High Pass Filtered', img1_high)

cv2.waitKey(0)
cv2.destroyAllWindows()