# Point to point operations
# 1. Digital Negative of binary image (0->1 and vice versa)

import cv2
img = cv2.imread('assets\hands.jpeg', 1)
img1 = cv2.resize(img, (500,600))
ret, b1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)      # converting greyscale to binary

cv2.imshow('Original', img1)
cv2.imshow('Binary', b1)
cv2.waitKey(0)

img2 = cv2.bitwise_not(b1)
cv2.imshow("Digital Negative", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
