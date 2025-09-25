""" Here we just sharpen the image
besically it's kernel move to each pixels in image and compair with neighbour pixels and boost the middle pixel,
increase the contrast of that pixel and also value
eg: if the image is 3*3 metrix size image like 9 pixel point
:: sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
    ])
-> the above array i pass 5 at middle means: i boost the pixels value to 5X
-> at the corner i placed 0 for not apply filter on that corner pixels mean ignore that pixels
-> in middel of all outside row and column i passed -1 for unchange mean the pixel value same as original
:: in this way boost the image contrast and pixel value and make sharpen ovoral image. 
syntax: cv2.filter2D(src, ddepth, kernel)  
"""
import cv2
import numpy as np

image = cv2.imread(r"Phase-4 (Image_filtering & Bluring)\low_qualityimg_grl.png")
# we define our own kernel to filter out the image
sharpen_kernel = np.array([
                            [0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]
                            ])

if image is None:
    print("Not loaded the image")
else:
    print("Loaded the image")
    # image = cv2.resize(image, (720,540))
    median_blur = cv2.medianBlur(image, 9)
    sharpen_img = cv2.filter2D(median_blur, -1 , sharpen_kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpen Image", sharpen_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

