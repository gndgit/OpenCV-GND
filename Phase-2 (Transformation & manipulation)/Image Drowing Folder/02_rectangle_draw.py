""" --> In this We trying to draw the rectangle over a image or video..
    --> basically it helps us to high-light any area over a image
    --> using this help we use in face detection in image or video
    --> using this we detect an object or items in a image all thing based on requirement 
    --> using cv2.rectangle() function we perform all this things
    --> It take parameter like rectangle(img, pt1, pt2, color, thickness)
            -> img = original_image_variable
            -> pt1 = Point 1 on image means top-left corner point coordinate
            -> pt2 = Point 2 on image means bottom-right corner point coordinate
            -> color = (b, g, r) range between (0-255)
            -> thickness = the bold of line in px eg: 4, 5.. linked this . 
                            if we pass -1 than it fill the color inside the rectangle
"""
import cv2 

image = cv2.imread(r"Image drawing Folder\test_image.jpg")

if image is None:
    print("Not loaded successfully, Check the path")
else:
    print("Loaded the image")
    # set point 1 and point 2
    pt1 = (100,50)
    pt2 = (500,250)
    thickness = 4 # this is in px if we pass -1 than it fill the rectangle
    color = (255, 0,0 ) #(B, G, R)
    # call the function
    cv2.rectangle(image, pt1, pt2, color, thickness)
    # fill inside the rectangle 
    # cv2.rectangle(image, (105,55), (495,245), (0,0,200), -1) 
    # showing the image
    cv2.imshow("Rectangle drew..", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()