import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# image = cv.imread('rdr.jpg', 1)
# colors = ['b', 'g', 'r']

# for i, color in enumerate(colors):
#     hist = cv.calcHist(image, [i], None, [256], [0, 256])
#     plt.plot(hist, color = color)

image = cv.imread('clahe_1.jpg', 0)
hist = cv.calcHist(image, [0], None, [256], [0, 256]) 

equalize_img = cv.equalizeHist(image)
hist_equalized = cv.calcHist(equalize_img, [0], None, [256], [0, 256]) 

# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(image)
hist_clahe = cv.calcHist(equalize_img, [0], None, [256], [0, 256])


plt.subplot(321), plt.imshow(image, 'gray')
plt.xticks([])
plt.yticks([])
plt.subplot(322), plt.plot(hist)

plt.subplot(323), plt.imshow(equalize_img, 'gray')
plt.xticks([])
plt.yticks([])

plt.subplot(324), plt.plot(hist_equalized)

plt.subplot(325), plt.imshow(cl1, 'gray')
plt.xticks([])
plt.yticks([])

plt.subplot(326), plt.plot(hist_clahe)

plt.show()
