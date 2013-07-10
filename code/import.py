import cv2
import os

directory = os.path.dirname(__file__)
picLoc = os.path.join(directory, "../video-image/1m50s.png")

image = cv2.imread(picLoc)
print "sending image to houghLines.py"
