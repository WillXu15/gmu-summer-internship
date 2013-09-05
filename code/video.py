import cv
import cv2
import numpy
import os
import time
def main():
#============================================Read video in==========================================================
	directory = os.path.dirname(__file__)
	vidLoc = os.path.join(directory, "../video-image/video.mp4")

	vid = cv2.VideoCapture()
	vid.open(vidLoc)

	vid.set(1,479)
	
#=====================================================Corners and Warping==================================================
	corners = numpy.array([[141,81],[179,663],[1125,527],[1083,86]], numpy.float32)
	
	topLength = corners[3][0] - corners[0][0]
	botLength = corners[2][0] - corners[1][0]

	leftLength = corners[1][1] - corners[0][1]
	rightLength = corners[2][1] - corners[3][1]
	
	avgTop = int((topLength + botLength)/2)
	avgLeft = int((leftLength + rightLength)/2)

	write = cv2.VideoWriter("write.mpg", cv.CV_FOURCC("M", "J", "P", "G"), int(vid.get(5)), (avgTop,avgLeft))

	newcorners = numpy.array([[0,0], [0, avgLeft], [avgTop, avgLeft], [avgTop,0]],numpy.float32)

	dsize = (avgTop, avgLeft)
#====================================================Warp all frames=====================================================
	for x in range(2820):
		debug, im = vid.read()
		transformMatrix = cv2.getPerspectiveTransform(corners, newcorners)

		image = cv2.warpPerspective(im, transformMatrix, dsize)
		
		write.write(image)
	
	
main()

