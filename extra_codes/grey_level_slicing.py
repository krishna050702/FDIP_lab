# Point to point operations
# 4. Grey Level Slicing

import cv2

img = cv2.imread(r"assets\hands.jpeg", 0)
img1 = cv2.resize(img, (500, 600))
cv2.imshow('Original Image', img1)

w,h = img1.shape
min_range = 80   # Specify the min and max range
max_range = 160
for i in range(0,w):
    for j in range(0,h):
        if img1[i][j]>min_range and img1[i][j]<max_range:
            img1[i][j] = 220

cv2.imshow('Grey Level Sliced Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


''' 4. GREY LEVEL SLICING
    Focuses on enhancing a specific range of grey level in an image.
    The intervals are pre-defined and pixels falling in that range are manipulated.
    This can be used to brighten the desired range of grey level while preserving the background quality in the range.'''