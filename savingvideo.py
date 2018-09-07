import numpy as np 	
import cv2

cap = cv2.VideoCapture(0)
cap.open(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('ajuu.avi',fourcc, 20.0,(640,480))

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		frame = cv2.flip(frame,0)

		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1000)& 0xff == ord('q'):
			break
		else:
			break

			cap.release()
			out.release()
			cv2.destroyAllWindows()
			sleep(60)
