import cv2
#  load the image
image = cv2.imread("My_Creation_SunFlower_cut.png",0) # 1 -> color, 2 -> grayscale, -1 -> unchanged(Default)

if image is None:
    print('Error loading , Please check the path')
else:
    print("Load successfully...")
    success = cv2.imwrite("output.jpg", image) # Store the image into local storage
    if success:
        print("Image saved successfully on \'output.jpg' name")
    else:
        print('Error while saving...')
    cv2.destroyAllWindows()