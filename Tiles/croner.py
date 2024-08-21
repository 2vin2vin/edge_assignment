import cv2
import glob

import numpy as np

path = './*.png'
def conversion(img1,img2):
	x1,y1 = img1.shape
#	print(img1.shape)
#	input()
	for i in range(0,x1):
		for j in range(0,y1):
			try:
#				print(img1[i][j])
				if img1[i][j]>150:
					img2[i][j]=0
			except Exception as e:
				print(i,j,e)
	return img2

for i in glob.glob(path):
	a=cv2.imread(i)
	cv2.imshow('original image',a)
	blur=cv2.GaussianBlur(a, (3,3), 9) 
#	cv2.imshow('first blur',blur)
	edge = cv2.Canny(blur, threshold1 = 80, threshold2 = 30)
	cv2.imshow('edges',edge)
	lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, minLineLength=50, maxLineGap=20)
	
	#create a black image panel
	black_img = np.ones(shape = cv2.imread(i,0).shape,dtype = np.uint8)
#	cv2.imshow('black',black_img)
	#add lines in it
	if lines is not None:
	    for line in lines:
#	    	print(line)
	    	x1, y1, x2, y2 = line[0]
	    	cv2.line(black_img, (x1, y1), (x2, y2), (255, 255, 255), 2)
	cv2.imshow('black_img_with_lines',black_img)
	#erode it
	kernel = np.ones((5, 5), np.uint8) 
	img_dilation = cv2.dilate(black_img, kernel, iterations=1) 
	cv2.imshow('dilate',img_dilation)
	
	#add erosion and minus the dilation
	img_erode = cv2.erode(img_dilation, kernel, iterations=4)
	cv2.imshow('dilate_eroded',img_erode)
	
	again_dilation = cv2.dilate(img_erode, kernel, iterations=4) 
	cv2.imshow('remover_dilate',again_dilation)
	
	converted_image = conversion(again_dilation, black_img)
	cv2.imshow('converted',converted_image)
	#apply gaussian filter
#	gaussed=cv2.GaussianBlur(img_dilation, (3,3), 9) 
#	cv2.imshow('erode_blurred',gaussed)
	edge = cv2.Canny(img_dilation, threshold1 = 80, threshold2 = 30)
	cv2.imshow('blacked_edge',edge)
	#then find lines and add to the image
	lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=20)

	# Draw the lines on the original image
	if lines is not None:
	    for line in lines:
#	    	print(line)
	    	x1, y1, x2, y2 = line[0]
	    	cv2.line(a, (x1, y1), (x2, y2), (0, 255, 0), 2)
	cv2.imshow('final',a)
	cv2.waitKey()
	#break


