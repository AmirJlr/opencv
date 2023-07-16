# Feature Selection

# SIFT
# SURF
# ORB

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('11.jpg', 1)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# SIFT
sift = cv.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(img, None)

img_sift = cv.drawKeypoints(img, keypoints_1, None)


# SURF 
# use openvc=3.4
# surf = cv.xfeatures2d.SURF_create(400)
# keypoints_2, descriptors_2 = surf.detectAndCompute(img, None)

# img_surf = cv.drawKeypoints(img, keypoints_2, None)

# ORB
orb = cv.ORB_create(nfeatures=1000)
keypoints_3, descriptors_3 = orb.detectAndCompute(img, None)

img_orb = cv.drawKeypoints(img, keypoints_3, None)


#v Plot Together
plt.subplot(131)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title('Image')

plt.subplot(132)
plt.imshow(img_sift)
plt.xticks([])
plt.yticks([])
plt.title('SIFT')

plt.subplot(133)
plt.imshow(img_orb)
plt.xticks([])
plt.yticks([])
plt.title('ORB')

plt.show()