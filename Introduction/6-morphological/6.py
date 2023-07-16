import numpy as np
import cv2
import matplotlib.pyplot as plt

# Morphological Operations

# Erosion
# Dilation
# Closing
# Opening
# Gradient

rdr = cv2.imread('rdr.jpg')
gray = cv2.cvtColor(rdr, cv2.COLOR_BGR2GRAY)


_, mask = cv2.threshold(gray, 150 , 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 65, 1)


kernel = np.ones((5, 5), np.uint8)
kernel = np.ones((5, 5), np.uint8)

# Erosion
eroded= cv2.erode(mask, kernel, iterations=1)


# Dilation
dilated= cv2.dilate(mask, kernel, iterations=1)

# Closing 
closed= cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Opening 
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN)

# Gradient


cv2.imshow('RDR2', rdr) 
cv2.imshow('Mask', mask) 
cv2.imshow('Adaptive', adaptive) 

cv2.waitKey(0)
cv2.destroyAllWindows()
