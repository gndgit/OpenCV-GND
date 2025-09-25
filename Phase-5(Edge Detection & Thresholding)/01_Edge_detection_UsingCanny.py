""" In this file we see the Canny edge detection code
    In canny edge detection it  is a function to finding edge from image which brightness is suddenly changeable
    syntax: edges = cv2.Canny(image, threshold_1, threshold_2)
                            -> image: Source image
                            -> threshold_1 : lower bound to detect week edge
                            -> threshold_2 : Upper bound to detect strong edge
            It basically work on a condition:
            if the threshold is BRIGHT enough than turn in into full bright (255)
            if the threshold is little Darken/darker than turn in into full Dark/Black (0)
"""
import cv2
import numpy as np

image = cv2.imread(r"Collection_image\Flower_image.png", cv2.IMREAD_GRAYSCALE)

if image  is None:
    print("ERROR Loading IMAGE")
else: 
    print("IMAGE Loaded Successfully....")
    edges = cv2.Canny(image, 50, 160) # (source_image, threshold_1, threshold_2)
    cv2.imshow("original_image", image)
    cv2.imshow("Edges_image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()