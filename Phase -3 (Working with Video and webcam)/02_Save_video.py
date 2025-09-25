# In this file we perform save the video into local storage
''' Steps:
            step 1: open the camera using videocapture() function
            step 2: Define the size/shape of the video mean width and height
            step 3: record the video and save in local storage
            step 4: show the video live...
            step 5: if user press 'q' than quit the video mean stop taking frames
            step 6: close the camera : release()
'''
import cv2

# step-1: open the camera 
camera = cv2.VideoCapture(0)

# step 2: define the shape of the video
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) 
#cv2.CAP_PROP_FRAME_WIDTH : this return the width of the camera and we type-casting to integer
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cv2.CAP_PROP_FRAME_HEIGHT : this return the Height of the camera and we type-casting to integer
# both attribute are come with the VideoCapture() function's Objects here : camera

# Compression format : .avi or .mp4 etc... 
codec = cv2.VideoWriter_fourcc(*'XVID') # Compress the video with XVID codec
# cv2.VideoWriter_fourcc(*'XVID') this function return the codec of the video
recorder = cv2.VideoWriter("My_video.avi",codec, 20, (frame_width, frame_height))
# syntax :: cv2.VideoWriter("filename.avi", compression_format, fps, (width, height))

while True:
    success, frame = camera.read()
    
    if not success:
        print("Not capturing the video :: ERROR")
        break
    
    recorder.write(frame) # this function present inside the VideoWrite() function
    # using this write() we save or record the frame and store in local storage
    cv2.imshow("Recording live", frame) # this show all frame live to user
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting.....")
        break

camera.release()
cv2.destroyAllWindows()