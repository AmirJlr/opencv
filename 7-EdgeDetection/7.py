import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


image = cv.imread('road.jpg', 0)
noise_removed = cv.GaussianBlur(image, (5,5), 0)

# Laplacian
lap_1 = cv.Laplacian(image, cv.CV_64F, ksize=9)
lap_2 = cv.Laplacian(noise_removed, cv.CV_64F, ksize=9)

# titles = ['Original Image',"Laplacian with ksize=9", 'Laplacian with kszie=9 & Blured']
# images = [image, lap_1, lap_2]



# Sobel
sobelx = cv.Sobel(noise_removed, cv.CV_64F, 1, 0, ksize=5)

sobely = cv.Sobel(noise_removed, cv.CV_64F, 0, 1, ksize=5)


# titles = ['Noise Removed Image',"Sobel X", 'Sobel Y']
# images = [noise_removed, sobelx, sobely]

# plt.figure(figsize=(12,6))
# for i in range(3):
#     plt.subplot(1,3,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.tight_layout()
# plt.show()



# Canny
canny = cv.Canny(noise_removed, 100, 200)
 
titles = ['Noise Removed Image',"Laplacian", 'Sobel Y', 'Canny']
images = [noise_removed, sobelx, lap_2, canny]

plt.figure(figsize=(12,6))
for i in range(4):
    plt.subplot(1,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()