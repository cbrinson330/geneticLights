import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG(5000, 16, 0.80)
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    bgSum = cv2.sumElems(fgmask)
    #if bgSum[0] > 10000:
        #print("FACE!")	
    #else:
        #print("NO FACE")
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
