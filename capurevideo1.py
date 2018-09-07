import numpy as np
import cv2

cap = cv2.VideoCapure(0)

while(True):
    ret,imf = cap.read('video output',img)
    k=cv2.waitKey(10)& 0xff
    if k == 27: 
        break
cap.release()
cv2.destroyAllWindows()
