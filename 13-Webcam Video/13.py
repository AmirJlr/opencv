import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    rec, frame = cap.read()
    
    cv.imshow('Frame', frame)

    exitKey=cv.waitKey(5) & 0xFF
    if exitKey == 27:
        break


"""
# Create a MASK for Captured Video
while True:
    rec, frame = cap.read()
    
    # original captured video
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # create blue MASK
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([115, 255, 255])

    mask_blue = cv.inRange(frame_hsv, lower_blue, upper_blue)
    frame_masked = cv.bitwise_and(frame, frame, mask=mask_blue)

    cv.imshow('Frame', frame)
    cv.imshow('Blue Mask', mask_blue)
    cv.imshow('Frame Masked', frame_masked)

    exitKey=cv.waitKey(5) & 0xFF
    if exitKey == 27:
        break
"""

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()