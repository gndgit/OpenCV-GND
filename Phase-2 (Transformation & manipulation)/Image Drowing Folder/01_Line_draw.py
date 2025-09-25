'''Drawing a line over a image 
--> to draw a line we required 2 point between that two point we draw a line :: starting point --> If you know where you start and where you end than easily draw a line
--> so we set point1 and point 2 for drawing a line between them'''

import cv2

image = cv2.imread(r"Image drawing Folder\test_image.jpg")

if image is None:
    print("Error while loading pleasecheck the path...")
else:
    print("Image Loaded Successfully")
    
    # set point 1 and point 2
    pt1 = (50,100) # (X, Y)--> X = 50, Y=100
    pt2 = (300,100) # X = 300, Y = 100
    # Set color fot your line
    color = (255, 0, 0) # (Red, Green, Blue) RGB the range or each color is (0-255)
    # Define thickness of the line
    thickness = 4 # in px format mean 4px
    # Call the line() function and pass all these things
    cv2.line(image, pt1, pt2, color, thickness)
    # showing the image
    cv2.imshow('Line draw Image ', image)
    print("Image Showing")
    cv2.waitKey(0)
    cv2.destroyAllWindows()