from matplotlib import pyplot as plt
import cv2 as cv

img=cv.imread("./assets/Lenna.png")
img2=cv.imread("./assets/Lenna.png",0)
cv.imshow('Image1',img)
cv.imshow('Image2',img2)
histr=cv.calcHist([img],[0],None,[256],[0,256])
histr2=cv.calcHist([img2],[0],None,[256],[0,256])
plt.title("Image")
plt.xlabel('bins')
plt.ylabel('No. of pixels')
plt.plot(histr)
plt.plot(histr2)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()