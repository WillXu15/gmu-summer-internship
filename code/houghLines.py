import cv2
import os
import math

def main():

	directory = os.path.dirname(__file__)
	picLoc = os.path.join(directory, "../video-image/1m50s.png")

	image = cv2.imread(picLoc)
	print "sending image to houghLines.py"

	a = hough(image)
	cv2.imshow("", a)
	cv2.waitKey(0)
	cv2.destroyAllChildren()

def hough(image):
	canny = cv2.Canny(image, 50, 200)
	houghLines = cv2.HoughLinesP(canny, 1, math.pi/180, 50)
	for x in range(len(houghLines)):
		pt1 = (houghLines[x][0], houghLines[x][1])
		pt2 = (houghLines[x][2], houghLines[x][3])
		cv2.line(image, pt1, pt2, (0,0,255), 3)
	return image
main()
