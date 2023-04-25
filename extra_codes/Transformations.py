# Point to point operations
# 2. Log Transformation
# 3. Power Law Transformation / Law Transformation

import cv2
import numpy as np

img = cv2.imread('assets\hands.jpeg', 1)
img1 = cv2.resize(img, (500,600))
cv2.imshow("Original Image", img1)

c = 255/np.log(1 + np.max(img1))
log_transformed = c*(np.log(1+img1))
log_transformed = np.array(log_transformed, dtype = np.uint8)

cv2.imshow("Log Transformed Image", log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.5, 2.5, 3.5, 5.5]:
    img2 = np.array(255 * (img1 / 255) ** gamma, dtype='uint8')   # Apply gamma correction.
    cv2.imshow('gamma_transformed ' + str(gamma) + '.jpg', img2)
    cv2.waitKey(0)

cv2.destroyAllWindows()

'''2. LOG TRANSFORMATION
    s = clog(1+r), where c=scaling constant, r=pixel intensity
    c = 255/(log (1 + m)),  where m=maximum pixel value in the image
    Log transformation maps a narrow range of low-intensity input values to a wide range of output values.
    
    3. POWER LAW/ GAMMA TRANSFORMATION
    s = c r**gamma'''