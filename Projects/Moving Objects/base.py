import cv2


# function for frame resize :
def rescale_frame(frame, percent=20):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


video = cv2.VideoCapture('street_camera.mp4')
# get video frame per second :
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    _, frame1 = video.read()
    _, frame2 = video.read()

    # Process Video :

    # 2 frame for moving detection :

    resize_frame1 = rescale_frame(frame1)
    resize_frame2 = rescale_frame(frame2)

    frame_diff = cv2.absdiff(resize_frame1, resize_frame2)
    frame_diff_gr = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)

    # smoothing
    blurred_frame = cv2.GaussianBlur(frame_diff_gr, ksize=(5, 5), sigmaX=1)

    # threshold
    _, mask = cv2.threshold(blurred_frame, 10, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            (x, y, w, h) = cv2.boundingRect(contour)
            # cv2.rectangle(resize_frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(resize_frame1, (x + w - 100, y + h - 50), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Frame', resize_frame1)
    cv2.imshow('Blurred Frame', blurred_frame)
    cv2.imshow('Mask Frame', mask)

    keyexit = cv2.waitKey(5) & 0xFF
    if keyexit == 27:
        break

cv2.destroyAllWindows()
video.release()
