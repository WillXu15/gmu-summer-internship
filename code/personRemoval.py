import cv2
import numpy as np

def main():

	print "OPENING VIDEO"	
	vid = cv2.VideoCapture()
	vid.open("write.avi")
	print "LOADING VIDEO"
	imgs = np.asarray([ vid.read()[1] for i in range(int(vid.get(7))) ])
	vid.release()
	print "CONCATENATING VIDEO"
	imgs = np.concatenate( ( np.repeat( imgs[:1], 5, axis = 0 ), imgs, np.repeat( imgs[-1:], 5, axis = 0 ) ), axis = 0 )
	N = 5
	print "FINDING MEDIAN"
	## imgs is a num-frames x num-rows x num-cols x num-channels array.
	median_frame = np.median( imgs[N-5:N+6], axis=0 )
	frame_num = 0
	cv2.imshow(str(frame_num), median_frame.astype(np.uint8))
	key = cv2.waitKey()

	while key != 113:
		frame_num += 1
		N+=1
		median_frame = np.median( imgs[N-5:N+6], axis=0 )
		cv2.imshow(str(frame_num), median_frame.astype(np.uint8) )
		key = cv2.waitKey()

if __name__ == "__main__": main()
