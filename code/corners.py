import cv2
import os
import math

def main():

	directory = os.path.dirname(__file__)
	picLoc = os.path.join(directory, "../video-image/1m50s.png")

	image = cv2.imread(picLoc)
	print "sending image to corners"
	a = corners(image)
	cv2.imshow("", a)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def corners(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#image = cv2.GaussianBlur(image, (11,11), 0)
	image = cv2.blur(image, (7,7))
	image = cv2.Canny(image, 150,200)
	corner = cv2.goodFeaturesToTrack(image, 4, 0.1, 100)
	color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
	for x in range(len(corner)):
		cv2.circle(color_image, (corner[x][0][0], corner[x][0][1]), 5, (0,0,255), 3)
	return color_image

main()