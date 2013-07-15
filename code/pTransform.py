import cv2
import os
import numpy

def main():

	directory = os.path.dirname(__file__)
	picLoc = os.path.join(directory, "../video-image/1m50s.png")

	origImage = cv2.imread(picLoc)

	corners = numpy.array([[141,81],[179,663],[1125,527],[1083,86]], numpy.float32)
	
	topLength = corners[3][0] - corners[0][0]
	botLength = corners[2][0] - corners[1][0]

	leftLength = corners[1][1] - corners[0][1]
	rightLength = corners[2][1] - corners[3][1]
	
	avgTop = int((topLength + botLength)/2)
	avgLeft = int((leftLength + rightLength)/2)

	newcorners = numpy.array([[0,0], [0, avgLeft], [avgTop, avgLeft], [avgTop,0]],numpy.float32)

	dsize = (avgTop, avgLeft)
	
	transformMatrix = cv2.getPerspectiveTransform(corners, newcorners)

	image = cv2.warpPerspective(origImage, transformMatrix, dsize)

	cv2.imshow("", image)
	cv2.waitKey()
	cv2.destroyAllWindows()


main()
