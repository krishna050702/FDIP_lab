import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image=cv.imread("./assets/preview500.jpg")
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(image)

alpha=1.5
beta=50
image2=cv.convertScaleAbs(image,alpha=alpha,beta=beta)

cv.imwrite("Brightness and contrast.jpg",image2)
plt.subplot(1,2,2)
plt.title("Brightness and contrast")
plt.imshow(image2)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()