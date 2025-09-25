# In this we see te how to rotate the image clock-wise and anti-clockwise
# in this we rotate the image from the center of the image point 

import cv2

# load the image 
image = cv2. imread(r"Phase-2 (Transformation & manipulation)\Horse.png")

# check the image is load or not
if image is not None:
    print("Image is loaded successfully...")
    (h,w) = image.shape[:2] # from shape attribute we extract the image height and width :: Basically it return Height, Width, Channels
    
    center = (w//2, h//2) # basically we perform the integer division to know the center point
    M = cv2.getRotationMatrix2D(center, 90, 1.0) # basically it convert the whole image into matrix format and this function take 3 parameter 1-> Center, 2-> angle: How many degree you rotate, 3-> scale: zoom in and zoom out purpose
    rotated_img = cv2.warpAffine(image,M, (w, h)) # this function actually rotate our image. Take parameter 1-> image_variable(original), 2-> metrix_variable: where we convert the image to metrix format at the above code , using getRotationMatrix2D() function
    
    
    # finally showing the image 
    cv2.imshow("Original Image: ",image)
    print("Original image Showing...")
    cv2.imshow("Rotated Image: ", rotated_img)
    print("Rotated Image showing...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("!!! Error : Image is not loaded successfully...")