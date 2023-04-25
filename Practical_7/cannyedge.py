import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
img=cv2.imread("assets/parking_lot.jpg",cv2.IMREAD_GRAYSCALE)
#cv2.imshow('original',img)
# assert img is not None: "file could not read"
edges=cv2.Canny(img,100,200)
#print(img.shape)
plt.subplot(121), plt.imshow(img,cmap='gray')
plt.title('orginal image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge image'),plt.xticks([]),plt.yticks([])
plt.show()
