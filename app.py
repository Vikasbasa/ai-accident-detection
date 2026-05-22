import cv2
import numpy as np

video = cv2.VideoCapture('videos/traffic.mp4')

while True:
    ret, frame = video.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)

    cv2.putText(
        frame,
        'Accident Detection Prototype Running',
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow('Traffic Monitoring System', frame)
    cv2.imshow('Processed Frames', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()