import face_recognition
import cv2

cam = cv2.VideoCapture(-1)

my_image = face_recognition.load_image_file("jm.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(my_image)[0]

face_encoding = [my_face_encoding,obama_face_encoding]
face_names = ["jeamin","obama"]

# Initialize
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
pre = 0

while True:
	ret, image = cam.read()
	
	
	
	if cv2.waitKey(1) & 0xFF == 27:
        break
        
	cv2.imshow('id',image)
	
cam.release()
cv2.destroyAllWindows()



