# Cropping the image 
import cv2

# load the image
image = cv2.imread(r"C:\Users\user\Desktop\My Repo\OpenCV-CodeWithSagar\Phase-2 (Transformation & manipulation)\Horse.png")

# Check the image is perfectly load or not 
if image is not None:
    print("\nImage Loaded successfully\n")
    cropped = image[180:300, 100:250] # It take first y location than X location
    # it take image[startY:endY, startX:endX]
    
    cv2.imshow("Cropped Image: ", cropped)
    cv2.imshow("original image", image)
    
    # cropped image saved in local storage 
    success = cv2.imwrite("Horse.png",cropped)
    
    print("image show successfully")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Cropped")
    
else:
    print("Error file not found \n please check the path")  