import cv
import cv2
import numpy as np
import tictoc

def main():
	N = 50
	print "OPENING VIDEO"	
	vid = cv2.VideoCapture()
	vid.open("write.avi")
	print "LOADING VIDEO"

	imgs = np.asarray([ vid.read()[1] for i in range(N+2) ])

	print "CONCATENATING VIDEO"
	imgs = np.concatenate( ( np.repeat( imgs[:1], N, axis = 0 ), imgs  ), axis = 0 )
	
	videowriter = cv2.VideoWriter("median.avi", cv.CV_FOURCC("M","J","P","G"), int(vid.get(5)), (int(vid.get(3)),int( vid.get(4))))

	total_frames = int(vid.get(7))
	print "FINDING MEDIAN"	
	## imgs is a num-frames x num-rows x num-cols x num-channels array.
	median_frame = np.median( imgs, axis=0 )
	frame_num = 0
	videowriter.write(median_frame.astype(np.uint8))

	while total_frames - frame_num != N:		
		frame_num += 1
		imgs[:-1] = imgs[1:]
		imgs[-1] = vid.read()[1]
		median_frame = np.median( imgs, axis=0 )
		videowriter.write(median_frame.astype(np.uint8))
		print "frame", frame_num, "was writen"

	print "======================================="

	imgs = np.concatenate( (imgs,  np.repeat( imgs[-1:], N, axis = 0) ), axis=0 )
	while total_frames-frame_num != 0:
		frame_num += 1
		imgs[:-1] = imgs[1:]
		median_frame = np.median( imgs[:101], axis = 0)
		videowriter.write(median_frame.astype(np.uint8))
		

if __name__ == "__main__": main()
