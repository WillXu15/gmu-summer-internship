import cv2
import numpy as np
def main():
	print "OPENING VIDEO"	
	vid = cv2.VideoCapture()
	vid.open("write.avi")
#=================================frame 1==============================================================
	print "MAKING FIRST FRAME"
	debug, img = vid.read()
	H = int(vid.get(4))
	W = int(vid.get(3))

	current_B = [img[x/W][x%W][0] for x in range(H*W)]
	current_G = [img[x/W][x%W][1] for x in range(H*W)]
	current_R = [img[x/W][x%W][2] for x in range(H*W)]
	#maxB = current_B.index(max(current_B))
	#maxG = current_G.index(max(current_G))
	#maxR = current_R.index(max(current_R))
#===============================frame 2==========================================================================
	print "MAKING SECOND FRAME"
	debug, img2 = vid.read()
	f1_B = [img2[x/W][x%W][0] for x in range(H*W)]	
	f1_G = [img2[x/W][x%W][1] for x in range(H*W)]
	f1_R = [img2[x/W][x%W][2] for x in range(H*W)]
#===============================frame3==========================================================================
	print "MAKING THIRD FRAME"
	debug, img3 = vid.read()
	f2_B = [img3[x/W][x%W][0] for x in range(H*W)]
	f2_G = [img3[x/W][x%W][0] for x in range(H*W)]
	f2_R = [img3[x/W][x%W][0] for x in range(H*W)]
#==============================median=============================================================================
	print "CALCULATING MEDIAN"
	B = np.median([current_B, f1_B, f2_B], axis=0)
	G = np.median([current_G, f1_G, f2_G], axis=0)
	R = np.median([current_R, f1_R, f2_R], axis=0)	
	for x in range(H*W):
		img[x/W][x%W][0] = B[x]
		img[x/W][x%W][1] = G[x]
		img[x/W][x%W][2] = R[x]
	print "DISPLAYING IMAGE"
	cv2.imshow("",img)
	cv2.waitKey()
	cv2.destroyAllWindows()
	#print H, W, H*W

	#print "max blue", "[%d,%d,%d]" %(current_B[maxB], current_G[maxB], current_R[maxB])
	#print "max green", "[%d,%d,%d]" %(current_B[maxG], current_G[maxG], current_R[maxG])
	#print "max red", "[%d,%d,%d]" %(current_B[maxR], current_G[maxR], current_R[maxR])

if __name__ == "__main__": main()
