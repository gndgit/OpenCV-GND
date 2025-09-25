""" This file we perform the median blur
this is used for removing black white or color dots from image
syntax : median = cv2/MedianBlur(image, kernel_size)
                            -> image : image obj variable
                            -> Kernel_size : it depends on window size and it should be odd"""

import cv2 
image = cv2.imread(r"Phase-4 (Image_filtering & Bluring)\scrach_image.png")
# image = cv2.resize(image, (540, 360))
if image is None:
    print("Not Loaded the image")
else:
    print("Loaded the image")
    median_blur = cv2.medianBlur(image, 9)
    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blur Image", median_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()