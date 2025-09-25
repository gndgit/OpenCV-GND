# Basic Video capture through webcam
import cv2

cap = cv2.VideoCapture(0)

''' Use a while loop so that it capture the video continuously when user not press any key
inside the loop we use read() function which is come with VideoCapture() function's Object mean 'cap' variable Like cap.read()
--> it return 2 value   
                        1> return: It return True of False ; true for capturing frame false for not capturing frames
                        2> Frames: it take video of a group of images

'''

while True:
    ret, frame = cap.read() # ret:return=True?False.   Frame: images
    
    if not ret: # mean not true
        print("Could Not read the Frame..")
        break
    print("Showing the video..")
    cv2.imshow("Webcam feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # ord()-it return ascii num and compare with 0xff hashcode 113-0xFF
        print("quitting....")
        break
cap.release()
cv2.destroyAllWindows()