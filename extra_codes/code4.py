import cv2
# Logical Operations - Bitwise AND, OR, NOT, XOR

img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\small_stars.jpg", 0)
img2 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\star.jpg", 0)
img3 = cv2.resize(img1, (400,400))
img4 = cv2.resize(img2, (400,400))

img5 = cv2.bitwise_and(img3, img4)
img6 = cv2.bitwise_or(img4, img3)
img7 = cv2.bitwise_xor(img4, img3)
img8 = cv2.bitwise_not(img4)

cv2.imshow("AND", img5)
cv2.imshow("OR", img6)
cv2.imshow("XOR", img7)
cv2.imshow("NOT", img8)
cv2.waitKey(0)
cv2.destroyAllWindows()