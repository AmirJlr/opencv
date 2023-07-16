import cv2 as cv
import numpy as np


rdr = cv.imread('rdr.jpg', cv.IMREAD_COLOR)

cv.putText(rdr, 'Artour Morgan', (40, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5, lineType=cv.LINE_AA )

# cv.line(rdr, (0,0), (400,200), (20, 20, 200), 10)
# cv.rectangle(rdr, (0,0),(400,200), (0,255,0), 10)

# cv.circle(rdr, (140,25), 25, (255, 0, 0), -1)

# points = np.array([[0,0], [120, 70], [64, 99]], np.int32)
# cv.polylines(rdr, [points], True, color=(100, 100, 100))

cv.imshow('RDR', rdr)

cv.waitKey(0)
cv.destroyAllWindows()