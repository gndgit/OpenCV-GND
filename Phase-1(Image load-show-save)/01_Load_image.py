import cv2
import numpy as np

# read image from local storage
image = cv2.imread("My_Creation_SunFlower_cut.png")

# check the image is load or not
if image is None:
    print("Not Loaded image")
else:
    print("Image Load Successfully")