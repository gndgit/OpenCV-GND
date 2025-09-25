"""
    - It is a function in python cv2 here we use for making normal image into black and white based on the BRIGHTNESS.
    - syntax:ret, threshold_image = cv2.threshold(image, threshold_value, max_value, method)
    ret mean : return
                                    -> image: it is the main source of image
                                    -> threshold_value: it the range between 0-255 (least/lowest value)
                                    -> Max_value: this is the max threshold value i.e 255
                                    -> methord : in which methord you apply on this image:
                                    most common method is THRESH BINARY:
                                    what it does:
                                    it convert little bit bright pixrl to full bright and if little dark convert into full darken ; both value based on threshold_value and max_value
"""
import cv2
import numpy as np

image = cv2.imread(r"Collection_image\pexels-photo-8537298.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("ERROR Loading Image")
else:
    print("Loaded Successfully")
    ret, threshold_img = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY) #(src, lower_threshpoint, max_thresh, method)
    cv2.imshow("Original_image", image)
    cv2.imshow("Black and White image_image", threshold_img)
    print("Image Showing.......................")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    """What the number value nearly 120 it the set middle point value: 
        -> 90 - 0 :> BLACK
        130 - 255 :> WHITE
        
    """
