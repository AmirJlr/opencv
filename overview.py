import cv2
import matplotlib.pyplot as plt


# Reading an Image
img1 = cv2.imread('imgs/1.jpg', -1)
print('image shape  :', img1.shape)
b, g, r = cv2.split(img1)

# Display Image In OpenCV :
"""
cv2.imshow('Intro Image', img1)

key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('imgs/1_saved.png', img1)
cv2.destroyAllWindows()
"""

# Display Image In Matplotlib :
"""
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.show()
"""

# Bitwise Operations
"""
bitwise_and
bitwise_or
bitwise_xor
bitwise_not
"""

