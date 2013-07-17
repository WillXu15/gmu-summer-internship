import cv2
import os
import math
import numpy

def main():

	directory = os.path.dirname(__file__)
	picLoc = os.path.join(directory, "../video-image/1m50s.png")

	image = cv2.imread(picLoc)
	print "Sending image to houghLines.py"
	a = hough(image)

	winname="TimeLapse Painting Video into Time Map File"
	cv2.namedWindow(winname, cv2.CV_WINDOW_AUTOSIZE)
	cv2.imshow(winname, a)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def hough(image):
	image = cv2.blur(image, (5,7))
	#image = cv2.GaussianBlur(image, (11,11),0)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	canny = cv2.Canny(image, 20, 175 )
	color_image = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
	houghLines = cv2.HoughLinesP(canny, 1, math.pi/180, 100, minLineLength = 250, maxLineGap = 100)
	houghLines = numpy.array(houghLines)
#-----------------------------------------------------------------------------------------
	print "="*20
	print "Number of edges:"
	print len(houghLines[0])
	print "="*20
	print "Pre-Overwrite Lines"
	print houghLines[0]
	print "="*20
	numLines=len(houghLines[0])-1
	overwrite=[]
	for z in range(numLines-1):
		count=z
		for x in range(numLines):
			if abs(houghLines[0][z][0]-houghLines[0][count+1][0])<15 or abs(houghLines[0][z][1]-houghLines[0][count+1][1])<15:
				overwrite.append(count+1)
			count+=1
		numLines-=1
	houghLines=numpy.delete(houghLines,(overwrite),axis=1)

	print "Post-Overwrite Lines"
	print houghLines[0]

	colorcountx=0
	colorcounty=0
	colorcountz=255
	colorc=0
	for x in range(len(houghLines[0])):
		pt1 = (houghLines[0][x][0], houghLines[0][x][1])
		pt2 = (houghLines[0][x][2], houghLines[0][x][3])
		cv2.line(color_image, pt1, pt2, (colorcountx,colorcounty,colorcountz), 3)
		if colorc==0:
			colorcounty+=255
			colorcountz-=255
		if colorc==1:
			colorcountx+=255
			colorcounty-=255
		if colorc==2:
			colorcounty+=255
		if colorc==3:
			colorcounty-=255
			colorcountz+=255
		if colorc==4:
			colorcountx-=255
			colorcounty+=255
			colorcountz+=255
		colorc+=1
		
	return color_image

main()
