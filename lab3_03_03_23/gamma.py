import numpy as np
import cv2
#load the image
img=cv2.imread("./assets/hands.jpeg")
new_img = cv2.resize(img, (300, 450))
#apply gamma=2.2 on the normalised image and then multiply
gamma_two_point_two=np.array(255*(new_img/255)**2.2,dtype=np.uint8)
#similary apply gamma 0.4
gamma_point_four=np.array(255*(new_img/255)**0.4,dtype=np.uint8)
#display the images in subplots
img3=cv2.hconcat([gamma_two_point_two,gamma_point_four])
cv2.imshow('a2',img3)
cv2.waitKey(0)
cv2.destroyAllWindows