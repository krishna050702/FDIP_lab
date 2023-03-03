import cv2
img1 = cv2.imread('./Lab00/Lenna.png', 1)
img2 = cv2.imread('./Lab00/cameraman.jpg', 1)

#resize of image to add them
new = cv2.resize(img2, (512, 512))

# AND
l_and = cv2.bitwise_and(new, img1)
cv2.imshow("AND", l_and)

# OR
l_or = cv2.bitwise_or(new, img1)
cv2.imshow("OR", l_or)

# XOR
l_xor = cv2.bitwise_xor(new, img1)
cv2.imshow("XOR", l_xor)

# NOT
l_not = cv2.bitwise_not(img1)
cv2.imshow("NOT", l_not)

cv2.waitKey(0)
cv2.destroyAllWindows()