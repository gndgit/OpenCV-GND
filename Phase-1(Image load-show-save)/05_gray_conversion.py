import cv2
#  load the image
image = cv2.imread("My_Creation_SunFlower_cut.png")
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Load Un-successfully...")