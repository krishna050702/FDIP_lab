import cv2
import numpy as np

## Read, Show, Greyscale, Rotate, Shape, Resize

# load image using imread
img = cv2.imread(r"assets\Lenna.png", cv2.IMREAD_COLOR)  # Flag = 1
img2 = cv2.imread(r"assets\Lenna.png", 0)   # Flag = 0 is cv2.IMREAD_GRAYSCALE
# Flag -1 is cv2.IMREAD_UNCHANGED

cv2.imshow("lena_img", img)   # lena_img is the window name
cv2.waitKey(100)     # Waits for a key to be pressed to close the window

cv2.imshow("lena_img_grey", img2)
cv2.waitKey(100)

img3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotate_img", img3)
cv2.waitKey(100)

img4 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotate_img_2", img4)
cv2.waitKey(100)

(h,w,d) = img.shape
print('width = {}, height = {}, depth = {}'.format(w,h,d))

new_img = cv2.resize(img, (300,200))
cv2.imshow("Resized1", new_img)
cv2.waitKey(0)

cv2.destroyAllWindows()