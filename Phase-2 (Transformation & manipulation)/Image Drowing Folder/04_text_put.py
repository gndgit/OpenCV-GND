""" --> In this We trying to put a TEXT over a image or video..
    --> basically it helps us to high-light any area's TEXT(massage) over a image
    --> using cv2.putText() function we perform all this things
    --> It take parameter like rectangle(img, center, radius, color, thickness)
            -> img = original_image_variable
            -> text = What would be add TEXT on image -- Massage
            -> org = Location (x,y) - where it placed
            -> font = font Type
            -> fontScale = size of the text :: 1.0-> normal , 2.0-> Big size
            -> color = (b, g, r) range between (0-255)
            -> thickness = Bold text
"""
import cv2 

image = cv2.imread(r"Image Drowing Folder\test_image.jpg")

if image is None:
    print("Erroe while loading, please check the path...")
else:
    print("Successfully Loaded the Image..")
    text = "JeCkY"
    org = (160,180) # (x,y) location
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 3
    color =(180,50,255)
    thickness = 8
    cv2.putText(image,text, org, font, fontScale,color,thickness)
    # Showing the image 
    cv2.imshow("Add text to Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()