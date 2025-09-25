# in this we do perform the flipping the image 

import cv2

# load the image
image = cv2.imread(r"Phase-2 (Transformation & manipulation)\Horse.png")

if image is not None:
    print("successfully Loaded the image.")
    # Flip the image horizontally parameter: (image original variable, Flipcode)
    """Flipcode 1: Horizontal Flip (Left to right)
        Flipcode 0: Vertically flip (Top to bottom)
        filecode -1: Both horizontally and vertically"""
    flip_horizontal = cv2.flip(image, 1)
    flip_vertically = cv2.flip(image, 0)
    flip_both = cv2.flip(image, -1)
    
    
    cv2.imshow("Original Image",image)
    cv2.imshow("Horizontal Flip Image", flip_horizontal)
    cv2.imshow("Vertically Flip Image", flip_vertically)
    cv2.imshow("Both Flip Image", flip_both)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("\n\t\t|------| Error While Loading the image |------|")