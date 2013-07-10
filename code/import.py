import cv2
import os

directory = os.path.dirname(__file__)
picLoc = os.path.join(directory, "../video-image/1m50s.png")

image = cv2.imread(picLoc)
cv2.imshow("", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
