import cv2
import numpy as np 
import time 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

capture = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = capture.read()

bg = np.flip(bg)

while(capture.isOpened()):
    ret, img = capture.read()
    if not ret:
        break
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
    mask1 = cv2.inRange(hsv, l_black, u_black)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res = cv2.bitwise_and(img, img, mask=mask2)
    f = img - res
    f = np.where(f == 0, img, f)
    finaloutput = cv2.addWeighted(res, 1, res, 1 , 0)
    outputfile.write(finaloutput)
    cv2.imshow('magic', finaloutput)
    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()
    