import cv2

cam = cv2.VideoCapture(1)
index = 20

while(True):
    ret, frame = cam.read()
	
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite("test"+str(index)+".jpg", frame)
        index += 1
        print('capture')
        
    cv2.imshow('image',frame)

cam.release()
cv2.destroyAllWindows()
