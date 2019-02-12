import cv2
import argparse as arg
import os
import time
import imutils

'''
parser = arg.ArgumentParser()
parser.add_argument("-d","--dirname",help="input save dirname")
args = parser.parse_args()

d_name = "database"
id_ = d_name + '/' + args.dirname

if not(os.path.isdir(d_name)):
	os.makedirs(os.path.join(d_name))
else:
	if not(os.path.isdir(id_)):
		os.makedirs(os.path.join(id_))
'''
cam = cv2.VideoCapture(1)
#cam.set(3,640)
#cam.set(4,480)

index = 1
pre = 0


while(True):
    ret, frame = cam.read()
    
    frame = imutils.resize(frame,width=300)

    cur = time.time()    
    sec = cur - pre
    pre = cur

    fps = 1/sec
    fps_text = "FPS : " + str(fps)    

    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    if k == ord('s'):
        #cv2.imwrite(id_+'/'+str(index)+".jpg", frame)
        cv2.imwrite("capture.jpg",frame)
        index += 1
        print('capture')
    
    cv2.putText(frame, fps_text, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0)) 
    
    cv2.imshow('image',frame)

cam.release()
cv2.destroyAllWindows()
