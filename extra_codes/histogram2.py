import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread(r"D:\College\SEM6\FDVIP\Lab\Lab03\jk.jpg",1)

cv2.imshow("original",img1)
for i, col in enumerate(['b','g','r']):
    hist = cv2.calcHist([img1],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    plt.title("histogram_coloured")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()