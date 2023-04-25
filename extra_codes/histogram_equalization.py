import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("D:\College\SEM6\FDVIP\Lab\Lab04\castle.png", 0)

equ1 = cv2.equalizeHist(img1)     # creating a Histogram Equalization using cv2.equalHist()
res1 = np.hstack((img1, equ1))    # stacking images side-by-side

cv2.imshow('Equalised', res1)

histogram1_original = cv2.calcHist([img1], [0], None, [256], [0, 256])
plt.title("Histogram of Image 1")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.plot(histogram1_original)
plt.show()

histogram1_equalized = cv2.calcHist([equ1], [0], None, [256], [0, 256])
plt.title("Histogram of Equalized Image 1")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.plot(histogram1_equalized)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


img2 = cv2.imread("D:\College\SEM6\FDVIP\Lab\Lab04\high_contrast.jpg", 0)

# creating a Histogram Equalization using cv2.equalHist()
equ2 = cv2.equalizeHist(img2)

# stacking images side-by-side
res2 = np.hstack((img2, equ2))

cv2.imshow('Equalised', res2)

histogram2_original = cv2.calcHist([img2], [0], None, [256], [0, 256])
plt.title("Histogram of Image 2")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.plot(histogram2_original)
plt.show()

histogram2_equalized = cv2.calcHist([equ2], [0], None, [256], [0, 256])
plt.title("Histogram of Equalized Image 2")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.plot(histogram2_equalized)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()