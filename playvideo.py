import numpy as np 
import cv2

cap = cv2.VideoCapture('Awesome.mp4')

cap.open('Awesome.mp4')

while(True):
	ret, frame = cap.read(0)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(25) & 0xff == 27:
		break
		cvReleaseCapture(cap)
		cap.release()
		cv2.destroyAllWindows()
		sleep(60)
