import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.open(0)

while(True):
	#capture frame by frame
	ret,frame = cap.read()
	#Our operations o the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xff == 27:
		break
		
		cvReleaseCapture(cap)
		cap.release()
		cap.destryAllWindows()