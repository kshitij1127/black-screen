import cv2
import numpy as np 
import time 

video = cv2.VideoCapture(0)
image = cv2.imread('b1.jpg')

while True:
    ret, img = video.read()
    print(image)
    frame = cv2.resize(img, (640, 480))
    image = cv2.resize(image, (640, 480))
    u_black = np.array([150, 153, 70])
    l_black = np.array([0, 0, 0])
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    f = frame - res
    f = np.where(f == 0, image, f)
    cv2.imshow("video", frame)
    cv2.imshow('mask', f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()