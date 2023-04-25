import cv2
# Image Flip, Addition, Weighted addition, Subtraction

img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab00\Lenna_(test_image).png", 1)
img2 = cv2.flip(img1, 1)
img3 = cv2.add(img1, img2)
img4 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
img5 = cv2.subtract(img1, img2)

cv2.imshow("Original", img1)
cv2.imshow("Flipped", img2)
cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow("Addition", img3)
cv2.imshow("Weighted Addition", img4)
cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow("Subtraction", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()

img6 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\small_stars.jpg", 1)
img7 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\star.jpg", 1)
img6 = cv2.resize(img6, (600,600))
img7 = cv2.resize(img7, (600,600))
img8 = cv2.subtract(img6, img7)

cv2.imshow("Original1", img6)
cv2.imshow("Original2", img7)
cv2.waitKey(0)
cv2.imshow("Subtraction", img8)
cv2.waitKey(0)
cv2.destroyAllWindows()