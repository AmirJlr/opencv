import numpy as np
import cv2


book = cv2.imread('bookpage.jpg')
gray = cv2.cvtColor(book, cv2.COLOR_BGR2GRAY)


# Manual Tresholding
ret, tresh = cv2.threshold(gray, 9, 255, cv2.THRESH_BINARY)

# OTSU Thresholding
ret2, tresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Adaptive Thresholding
tresh3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow("Book", book)
cv2.imshow("Tresh", tresh)
cv2.imshow("Adaptive", tresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()