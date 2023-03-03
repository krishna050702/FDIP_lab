import cv2
img1 = cv2.imread('./assets/Lenna.png', 1)
img2 = cv2.imread('./assets/camera_man.jpg', 1)

(h,w,d)=img1.shape
print(f"Height= {h}\nWidth= {w}\nDepth= {d}")
(h,w,d)=img2.shape
print(f"Height= {h}\nWidth= {w}\nDepth= {d}")

#resize of image to add them
new = cv2.resize(img2, (512, 512))

#normal addition
add = cv2.add(img1,new)
cv2.imshow('Addition', add)

#Weighted addition
addw = cv2.addWeighted(img1, 0.2, new, 0.8, 0)
cv2.imshow('Weighted Addition', addw)

#normal subtraction
sub = cv2.subtract(img1,new)
cv2.imshow('Subtraction',sub)

#multiplication
mul = cv2.multiply(img1, new)
cv2.imshow('Multiplication',mul)

#division
div = cv2.divide(img1, new)
cv2.imshow('Division',div)

cv2.waitKey(0)
cv2.destroyAllWindows()