import cv2
import matplotlib.pyplot as plt
import numpy as np


img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab00\Lenna_(test_image).png", 0)
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img1)

alpha = 1.5  # control contrast by 1.5
beta = 50   # control brightness by 50
img2 = cv2.convertScaleAbs(img1, alpha=alpha, beta=beta)
plt.subplot(1, 2, 2)
plt.title("Brightness and Contrast")
plt.imshow(img2)
plt.show()