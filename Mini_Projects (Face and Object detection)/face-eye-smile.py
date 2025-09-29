# Face - eye - smile detection
import cv2

face_cascade = cv2.CascadeClassifier(r"Phase-7 (Face and Object detection)\Haar_xml_files\haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(r"Phase-7 (Face and Object detection)\Haar_xml_files\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"Phase-7 (Face and Object detection)\Haar_xml_files\haarcascade_smile.xml")

# on the video 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Check the video read or not
    if not ret:
        print("Failed to grab frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3)
        cv2.putText(frame, "Face Detected", (x,y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
        
        # ony region make for face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w] # it simple cutting only the face area bcz when i try to detect eye and smile it only search in this area only
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "eye detected", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(smiles) > 0:
            cv2.putText(frame, "Smile detected", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    
    cv2.imshow("Video Processed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Closing the Camera....")
        print("Closed the program, Thank you for using our program")
        break

cap.release()
cv2.destroyAllWindows()


# @gndgit