import face_recognition
import cv2
import time

cam = cv2.VideoCapture(-1)

print("Loading image...")

my_image = face_recognition.load_image_file("jm.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Initialize
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
pre = 0

while True:
	ret, frame = cam.read()
	
	cur = time.time()
	sec = cur - pre
	pre = cur
    
	fps = 1/sec
	fps_text = "FPS : " + str(fps)
    
	cv2.putText(frame, fps_text, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
	
	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
	rgb_small_frame = small_frame[:,:,::-1]
	
	if process_this_frame:
		#face finding
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
		
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces([my_face_encoding],face_encoding)
			name = "UNKNOWN"

			if True in matches:
				name = "jjeamin" 

			cv2.putText(frame, name, (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
	
	if cv2.waitKey(1) & 0xFF == 27:
		break
        
	cv2.imshow('id',frame)
	
cam.release()
cv2.destroyAllWindows()



