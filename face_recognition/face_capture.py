import cv2
import argparse as arg
import os

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

cam = cv2.VideoCapture(-1)
index = 1

while(True):
    ret, frame = cam.read()
	
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite(id_+'/'+str(index)+".jpg", frame)
        index += 1
        print('capture')
        
    cv2.imshow('image',frame)

cam.release()
cv2.destroyAllWindows()
