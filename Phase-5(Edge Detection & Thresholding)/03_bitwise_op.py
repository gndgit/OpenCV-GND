""" Bitwise operation on image:
    - 3 type of bit wise operation can do
        1. AND
        2. OR
        3.NOT
    
    1. AND->  cv2.bitwise_and(image_1, image_2)
                -> Used for cutout shape from one another
                -> it besically leave white area in image
    2. OR-> cv2.bitwise_or(image_1, image_2)
                -> Combine both image and show in one
    3. NOT -> cv2.bitwise_not(image)
            -> invert the image
            -> back --> white, white --> black
"""
import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8") # 300*300 metrix create
img2 = np.zeros((300,300), dtype="uint8")

# drawing a circle on img 1
cv2.circle(img1, (150,150),100, 255, -1)
# drawing a rectangle also
cv2.rectangle(img2, (100,100), (250,250), 255, -1)

# apply bitwise operation
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not_1 = cv2.bitwise_not(img1)
bitwise_not_2 = cv2.bitwise_not(img2)

# printing the image
# Circle
cv2.imshow("Circle image", img1)
# rectangle
cv2.imshow("Rectangle image", img2)
# ANd Operation
cv2.imshow("bitwise And _operation", bitwise_and)
# or Operation
cv2.imshow("bitwise or _operation", bitwise_or)
# not Operation
cv2.imshow("bitwise not1 _operation", bitwise_not_1)
# not Operation
cv2.imshow("bitwise not2 _operation", bitwise_not_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
