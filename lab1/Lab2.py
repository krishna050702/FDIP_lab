# Rotating Image
import cv2
import numpy as np
# load image
img = cv2.imread("./Lab00/Lenna.png",1)
img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Lenna image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# # load image
# img = cv2.imread("Lenna.png",1)
# # get number of pixels horizontally and vertically
# (height, width) = img.shape[0:2]
# new = cv2.resize(img, (1000, 450))
# cv2.imshow("Resized image",new)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()
