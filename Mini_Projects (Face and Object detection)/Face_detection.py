# face detection Full PROJECT -- GND
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r"Phase-7 (Face and Object detection)\Haar_xml_files\haarcascade_frontalface_default.xml") # cascadeClassifier () helps to read the xml cascade file

# for video capture
cap = cv2.VideoCapture(0) # 0 for webcam of laptop

while True:
    ret, frame = cap.read()
    # Check the video read or not
    if not ret:
        print("Failed to grab frame.")
        break
    # convert into gray scale bcz it work perfectly and good accuracy when use grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) # (img, scaleFactor, minneighbors)
                                        # - scaleFactor : how many u what the zoom level higher value low zoom and fast also than viceversa
                                        # - minneighbors: 
    """we pass the cascade variable which hold the cascade file
    - detectMultiScale() : using this function we scan and detect the objects (here use for face)
    # (img, scaleFactor, minneighbors)
            # scaleFactor : how many u what the zoom level higher value low zoom and fast also than viceversa
            1.1 : it is balanced, not too slow, blind
            # minneighbors = 5 : it test internally 5 times; this is a face/object or not
    """
    for (x, y, w, h) in faces:
        """ face return a list : in image where they detect the face it's location which is x & y and the pixel which is w & h for eg: (100,150, 80,80)
        - X: how far from left
        - y : how far from top
        - w : width of face
        - h : height of face
        """
        # draw rectangle
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        # according to syntax we pass (image, top-left corner, bottom-right corner, color, thickness) so we pass starting point x, y and ending point i simply add them with weight and height
        
        # SHowing the Image
        cv2.putText(frame, "Face Detected", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
    cv2.imshow("Webcam Face detection", frame)
        
        # for closing we give the 'q' bottom to close the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Closing the Camera....")
        print("Closed the program, Thank you for using our program")
        break

# off the camera 
cap.release()
cv2.destroyAllWindows()

# @gndgit