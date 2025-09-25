import cv2

# load the image
image = cv2.imread('My_Creation_SunFlower_cut.png')

# Check the image successfully load or not
if image is not None:
    print("Successfully Loaded the image")
    # Show the image to User using imshow("Title to display", variable_name_where the stored image)
    cv2.imshow("Image Showing", image)
    # continuous show upto not closed by user 
    cv2.waitKey(0) # for continuous show
    # clearing all window from background after closing the image 
    cv2.destroyAllWindows()
    print("Closed the image bcz u press key form keyboard")
else:
    print("Error while loading, Image not Found please check your path...")
