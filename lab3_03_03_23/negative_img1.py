import cv2
import numpy as np
img = cv2.imread('./assets/hands.jpeg', 1)

(height, width) = img.shape[0:2]
print(height, width)

new_img = cv2.resize(img, (300, 450))
#cv2.imshow("Resized image",new_img)

# Negative of image
img_neg = 255 - new_img
cv2.imshow('Negative', img_neg)

# Log Transformation Method
c = 255/np.log(1 + np.max(new_img))
log_img = c * (np.log(new_img * 1))
# Specify the data type so that we can
# float value will be converted to integer
log_img = np.array(log_img, dtype=np.uint8)
# Display both  image and log
cv2.imshow('Original', new_img)
cv2.imshow('Log', log_img)

cv2.waitKey(0)
cv2.destroyAllWindows()