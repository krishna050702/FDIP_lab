import cv2
# Image Multiplication and Division

img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\small_stars.jpg", 0)
img2 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab02\star.jpg", 0)
img3 = cv2.resize(img1, (500,500))
img4 = cv2.resize(img2, (500,500))

img5 = cv2.multiply(img3, img4)
img6 = cv2.divide(img3, img4)
img7 = img3*0.8
img8 = img3/0.8

cv2.imshow("Original Image 1", img3)
cv2.imshow("Original Image 2", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Scalar Multiplication", img7)
cv2.imshow("Scalar Division", img8)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Multiplication", img5)
cv2.imshow("Division", img6)
cv2.waitKey(0)
cv2.destroyAllWindows()