""" In this file we discuss about bluring the image
Here we trying to discuss about gaussian Blur
Syntax: cv2.GaussianBlur(image_object_variable, (kernel_size_x,kernel_size_y),sigma)
                        -> image_object_variable: Image stored variable
                        -> (kernel_size_x,kernel_size_y) : it defin the size of image it always odd number, even is not work here Eg: (3,3), (5,5), (7,7) etc
                        -> sigma : how many quantity you want to blur 
                                    '0' For cv2 auto detect blur according to your image

"""

import cv2


image = cv2.imread(r"Phase-4 (Image_filtering & Bluring)\tiger_image_.jpg")

if image is None:
    print("Not successfully loaded the image.")
else:
    print("successfully loaded the image...")
    Gaussian_blur_img = cv2.GaussianBlur(image, (9,9), 3) #(image_object_variable, (kernel_size_x,kernel_size_y),sigma)
    cv2.imshow("Original tiger image",image)
    cv2.imshow("Gaussian Blur tiger image",Gaussian_blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()