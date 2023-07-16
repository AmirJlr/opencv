import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('rma.jpg', 0)
img_c = cv.imread('rma.jpg', 1)

"""

# cv.IMREAD_COLOR (1)
# cv.IMREAD_GRAYSCALE (0)
# cv.IMREAD_UNCHANGED (-1)

cv.imshow('Santiago Bernabeo',img) 


cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('rma_gray.jpg', img)

"""

# plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.imshow(img_c, interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()