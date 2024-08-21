import cv2
import glob

import numpy as np

path = './*.png'

j=0
for i in glob.glob(path):
	if j>3:
		cv2.destroyAllWindows()
		break
	j+=1
	a=cv2.imread(i)
	cv2.imshow('l',a)
#	cv2.waitKey()
	ab=cv2.GaussianBlur(a, (3,3), 9) 
	edge = cv2.Canny(ab, threshold1 = 100, threshold2 = 20)
	lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, minLineLength=70, maxLineGap=20)

	# Draw the lines on the original image
	if lines is not None:
	    for line in lines:
#	    	print(line)
	    	x1, y1, x2, y2 = line[0]
	    	cv2.line(a, (x1, y1), (x2, y2), (0, 255, 0), 2)

	cv2.imshow('e', edge)
	cv2.imshow('p',a)
	cv2.waitKey()
	'''
	img_gray = cv2.cvtColor(a.copy(), cv2.COLOR_BGR2GRAY)
	# Blur the image for better edge detection
	img_blur = cv2.GaussianBlur(img_gray, (9,9), 9) 

	# Sobel Edge Detection
	sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=15) # Sobel Edge Detection on the X axis
	sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=15) # Sobel Edge Detection on the Y axis
	sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=15) # Combined X and Y Sobel Edge Detection
	# Display Sobel Edge Detection Images
	cv2.imshow('Sobel X', sobelx)
#	cv2.waitKey(0)
	cv2.imshow('Sobel Y', sobely)
#	cv2.waitKey(0)
	cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
	cv2.waitKey(0)
	'''

