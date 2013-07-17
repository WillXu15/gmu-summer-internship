import cv2
import numpy as np
import os

def main():
	
	directory = os.path.dirname(__file__)
	vidLoc = os.path.join(directory, "../video-image/video.avi")

	vid = cv2.VideoCapture()
	vid.release()
	print vid.open(vidLoc)

	if vid.isOpened():
		print "you're good"
	
main()

