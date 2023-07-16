import cv2 as cv

# Haarcascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# camera
cap = cv.VideoCapture(0)

while True:
    rec, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    # bounding box on face
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # looking for eyes in face roi
        frame_gray_roi = frame_gray[y:y+h, x:x+w]
        frame_roi = frame[y:y+h, x:x+w]

        # detect eyes
        eyes = eye_cascade.detectMultiScale(frame_gray_roi)

        # bounding box on eyes
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(frame_roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)


    cv.imshow('Frame', frame)

    exitKey=cv.waitKey(5) & 0xFF
    if exitKey == 27:
        break


cap.release()
cv.destroyAllWindows()