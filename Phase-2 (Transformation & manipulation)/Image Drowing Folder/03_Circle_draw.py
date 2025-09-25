""" --> In this We trying to draw the Circle over a image or video..
    --> basically it helps us to high-light any area over a image
    --> using cv2.circle() function we perform all this things
    --> It take parameter like rectangle(img, center, radius, color, thickness)
            -> img = original_image_variable
            -> center = Middle point- center (x,y)
            -> radius = r value in pixel mean from center how many distance to to round draw circle
            -> color = (b, g, r) range between (0-255)
            -> thickness = the bold of line in px eg: 4, 5.. linked this . 
                            if we pass -1 than it fill the color inside the circle
"""
import cv2

img = cv2.imread(r"Image Drowing Folder\test_image.jpg")

if img is None:
    print("Image is not loaded, please check the path")
else:
    print("Loaded successfully")
    
    center = (300,160) # (x,y)
    radius = 140 # in px
    color = (255,0,255) # (b,g,r)
    thickness = 4 # in px
    cv2.circle(img, center, radius, color, thickness)
    cv2.circle(img, center, 1, (0,0,0), 5)
    # cv2.line(img, center, (440,160), (200,0,0),3)#I trying to draw the radious-line of circle
    # Showing the image 
    cv2.imshow("Output Circle image", img)
    print("Showing the image")
    cv2.waitKey(0)
    cv2.destroyAllWindows()