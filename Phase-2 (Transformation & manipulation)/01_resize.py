import cv2

# load the image
image = cv2.imread(r"Phase-2 (Transformation & manipulation)\Horse.png")

if image is None:
    print("Not Found")
# Showing The image
else:
    print("Load Successfully")
    
    # resize function app for resizing the image 
    resize = cv2.resize(image, (600, 900)) # it take input of src and the size weight and hight pixels

    # showing both image 
    cv2.imshow("Resize Image", resize)
    cv2.imshow("Original Size", image)
    done = cv2.imwrite("Horse_out.png",resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if done:
        print("saved successfully")
    else:
        print("Not loaded.")