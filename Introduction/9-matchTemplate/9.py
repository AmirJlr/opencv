import cv2
import numpy as np

image = cv2.imread('soccer_practice.jpg', 0)

ball_template = cv2.imread('ball.PNG', 0)
shoe_template = cv2.imread('shoe.PNG', 0)

h, w = ball_template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = image.copy()
    matched = cv2.matchTemplate(img2, ball_template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matched)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Matcheing...', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
